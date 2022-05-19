import mne, glob
import pandas as pd
import neurokit2 as nk
import matplotlib.pyplot as plt
import numpy as np

markdowns=[]
images=[]
for file in glob.glob("*.vhdr"):
    # Raw data
    raw = mne.io.read_raw_brainvision(file)
    filename=file.split(sep='.')[0]
    patient=filename.split('_')[:-2]
    patient=f"{patient[0]}_{patient[1]}_{patient[2]}"
    date=raw.info['meas_date']
    # Selecting & renaming channels
    temp = raw.copy().pick_channels(['5', '17', '29', '30', '31'])
    temp.rename_channels({'5':'Fz', '17':'mastoid', '29':'O1', '30':'Oz', '31':'O2'})

    # Notch filter
    notch = temp.load_data().notch_filter(freqs=(50, 251, 50))
    # Bandwidth filter
    filtered = notch.filter(l_freq=0.1, h_freq=40)
    # Setting reference to channel 5 = Fz
    filtered.set_eeg_reference(ref_channels=['Fz'])

    # Averaging events and plotting them
    events, event_ids = mne.events_from_annotations(filtered)
    epochs = mne.Epochs(filtered, events, tmin=-0.1, tmax=0.25, baseline=(-0.1,0), event_id=event_ids, preload=True, event_repeated='merge', picks=['O1', 'Oz', 'O2'], verbose='ERROR').average()

    # Peak detection for each channel
    peaks={'O1':{'N70':[], 'P100':[]}, 'Oz':{'N70':[], 'P100':[]}, 'O2':{'N70':[], 'P100':[]}, 'file':filename}
    for i in ['O1', 'Oz', 'O2']:
        i_epochs = mne.Epochs(filtered, events, baseline=(-0.1,0), tmin=-0.1, tmax=0.25, event_id=event_ids, preload=True, event_repeated='merge', picks=[i], verbose='WARNING').resample(100000).average()
        ch, n70_peak_ms, n70_peak_ampl = i_epochs.get_peak(mode='neg', return_amplitude=True, ch_type='eeg', )
        ch, p100_peak_ms, p100_peak_ampl = i_epochs.get_peak(mode='pos', return_amplitude=True, ch_type='eeg')
        peaks[i]['N70']=[f"{round(n70_peak_ms*1000,3)}ms", f"{round(n70_peak_ampl*1e06, 3)}uV"]
        peaks[i]['P100']=[f"{round(p100_peak_ms*1000,3)}ms", f"{round(p100_peak_ampl*1e06, 3)}uV"]

        # print(f"{ch} N70 peak at {round(n70_peak_ms*1000, 3)}ms and {round(n70_peak_ampl*1e06, 3)}uV")
        # print(f"{ch} P100 peak at {round(p100_peak_ms*1000, 3)}ms and {round(p100_peak_ampl*1e06, 3)}uV")
    
    df=pd.DataFrame(peaks)
    md=df.to_markdown(tablefmt="html")
    markdowns.append(md)
    # print(md)
    plot=epochs.plot(titles=filename, show=False).savefig(filename)
    images.append(filename)
    # plots.append(plot)


# Create html from the plots and peaks
# images=[]
# for image in glob.glob("*.png"):
#     images.append(image)

html_text=f'''
<html>
    <h1>{patient}</h1>
    <h3>{date}</h3>
    <body>
        <div class="frame" style="float:left"><img src="{images[0]}.png">
            <div class="frame" style="font-family:courier; float:right">{markdowns[0]}</div><br><hr align="left"><br>
        </div>           
        <div class="frame" style="float:left"><img src="{images[1]}.png">
            <div class="frame" style="font-family:courier; float:right">{markdowns[1]}</div><br><hr align="left"><br>
        </div>   
        <div class="frame" style="float:left"><img src="{images[2]}.png">
            <div class="frame" style="font-family:courier; float:right">{markdowns[2]}</div><br><hr align="left"><br>
        </div>
        <div class="frame" style="float:left"><img src="{images[3]}.png">
            <div class="frame" style="font-family:courier; float:right">{markdowns[3]}</div>
        </div>
    </body>
</html>
'''
html_file = open(f"{patient}.html","w")
html_file.write(html_text)
html_file.close()

# print(markdowns)