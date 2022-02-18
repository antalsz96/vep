from psychopy import visual, monitors, core, event
import nidaqmx

#Psychopy setup
mon = monitors.Monitor("testMonitor", distance=90)
win = visual.Window(monitor=mon, fullscr=True, viewPos=(-11.45, -9), units="deg")
ISI = core.StaticPeriod(screenHz=85)

cross_hor = visual.Line(win=win, start=[11.4,9.5], end=[11.6,9.5], lineWidth=2, lineColor="red", units="deg")
cross_ver = visual.Line(win=win, start=[11.5,9.4], end=[11.5,9.6], lineWidth=2, lineColor="red", units="deg")


g1 = visual.GratingStim(win=win, tex="sqrXsqr", units="deg", pos=(0,0), size=(48,38), sf=0.5)
g2 = visual.GratingStim(win=win, tex="sqrXsqr", units="deg", pos=(0,0), size=(48,38), sf=0.5, contrast=-1)

timer = core.CountdownTimer(5)
while timer.getTime() > 0:
    with nidaqmx.Task() as task:
        task.do_channels.add_do_chan("Dev2/port0")

        # frame 1
        ISI.start(0.5)
        g1.draw()
        cross_ver.draw()
        cross_hor.draw()
        task.write(5)
        task.write(0)
        win.flip()
        ISI.complete()
        
        # frame 2
        ISI.start(0.5)
        g2.draw()
        cross_ver.draw()
        cross_hor.draw()
        task.write(5)
        task.write(0)
        win.flip()
        ISI.complete()

# g1.draw()
# cross_ver.draw()
# cross_hor.draw()
# win.flip()
# event.waitKeys()
# win.close()
