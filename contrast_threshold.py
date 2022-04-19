from fileinput import filename
from psychopy import core, visual, event, gui, data
from psychopy.tools.filetools import fromFile, toFile
import pandas as pd


try:  # try to get a previous parameters file
    expInfo = fromFile('lastParams.pickle')
except:  # if not there then use a default set
    expInfo = {'observer':'jwp'}
expInfo['dateStr'] = data.getDateStr()  # add the current time
# present a dialogue to change params
dlg = gui.DlgFromDict(expInfo, title='simple JND Exp', fixed=['dateStr'])
if dlg.OK:
    toFile('lastParams.pickle', expInfo)  # save params to file for next time
else:
    core.quit()  # the user hit cancel so exit

fileName = expInfo['observer'] + expInfo['dateStr']
dataFile = open(fileName+'.csv', 'w')  # a simple text file with 'comma-separated-values'
dataFile.write('mean,sd,median\n')

# df = pd.DataFrame(columns=['mean', 'sd', 'median'])
win = visual.Window([800,600],allowGUI=True, monitor='testMonitor', units='deg')
stimulus = visual.GratingStim(win=win, tex='sin', size=15,
                             pos=[0,0], units='deg', mask='circle')

fixation = visual.GratingStim(win, color=-1, colorSpace='rgb', pos=[0,0],
                              tex=None, mask='circle', size=0.2)

# create staircase object
# trying to find out the point where subject's response is 50 / 50
# if wanted to do a 2AFC then the defaults for pThreshold and gamma
# are good. As start value, we'll use 50% contrast, with SD = 20%
staircase = data.QuestHandler(startVal=0.5, startValSd=0.2,
                            pThreshold=0.63, beta=3.5,gamma=0.01, delta=0.01,
                            nTrials=40, minVal=0, maxVal=1)

for thisContrast in staircase:
    # setup stimulus
    stimulus.setContrast(thisContrast)
    stimulus.draw()
    fixation.draw()
    win.flip()
    core.wait(0.5)
    # get response
    thisResp=None
    while thisResp==None:
        allKeys=event.waitKeys()
        for thisKey in allKeys:
            if thisKey=='left':
                thisResp=0
            elif thisKey=='right':
                thisResp=1
            elif thisKey in ['q', 'escape']:
                core.quit()  # abort experiment
        event.clearEvents()  # clear other (eg mouse) events - they clog the buffer
    # inform QUEST of the response, needed to calculate next level
    staircase.addResponse(thisResp)

mean = staircase.mean()
sd = staircase.sd()
median = staircase.quantile(0.5)
# df.append({'mean':mean, 'sd':sd, 'median':median}, ignore_index=True)
# df.to_csv(f"{fileName}.csv")

dataFile.write(f"{mean},{sd},{median}")
dataFile.close()
# can now access 1 of 3 suggested threshold levels
# print(staircase.epsilon)
print(mean)
print(sd)
print(median)
