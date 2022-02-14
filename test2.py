from psychopy import visual, monitors, core, event
mon = monitors.Monitor("testMonitor", distance=90)
win = visual.Window(monitor=mon, fullscr=True, units="deg")

g1 = visual.GratingStim(win=win, tex="sqrXsqr", units="deg", pos=(0,0), size=(24,23), sf=0.5)


g1.draw()
win.flip()
event.waitKeys()

win.close()
