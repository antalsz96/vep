from psychopy import visual, monitors, core, event
mon = monitors.Monitor("testMonitor", distance=90)
win = visual.Window(monitor=mon, fullscr=True, viewPos=(-11.45, -9), units="deg")
ISI = core.StaticPeriod(screenHz=85)

g1 = visual.GratingStim(win=win, tex="sqrXsqr", units="deg", pos=(0,0), size=(48,38), sf=0.5)
g2 = visual.GratingStim(win=win, tex="sqrXsqr", units="deg", pos=(0,0), size=(48,38), sf=0.5, contrast=-1)

timer = core.CountdownTimer(15)
while timer.getTime() > 0:
    # frame 1
    ISI.start(0.5)
    g1.draw()
    win.flip()
    ISI.complete()
    
    # frame 2
    ISI.start(0.5)
    g2.draw()
    win.flip()
    ISI.complete()

    
