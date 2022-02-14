from psychopy import visual, monitors, core, event
mon = monitors.Monitor("testMonitor", distance=90)
#mon.setDistance("90")
win = visual.Window(monitor=mon, fullscr=True, viewPos=(-11.45, -9), units="deg")
ISI = core.StaticPeriod(screenHz=85)
black_1_xys = []
white_1_xys = []
black_2_xys = []
white_2_xys = []


# FRAME 1
for r in range(24):
    if r%2==0:
        for c in range(19):
            if c%2==0:
                color="white"
                x=r
                y=c
                white_1_xys.append([x,y])
            else:
                color="black"
                x=r
                y=c
                black_1_xys.append([x,y])
    else:
        for c in range(19):
            if c%2==0:
                color="black"
                x=r
                y=c
                black_1_xys.append([x,y])
            else:
                color="white"
                x=r
                y=c
                white_1_xys.append([x,y])

## FRAME 2
black_2_xys = white_1_xys
white_2_xys = black_1_xys

g1 = visual.GratingStim(win=win, tex="sqrXsqr", units="deg", pos=(0,0), size=(48,38), sf=0.5)
g2 = visual.GratingStim(win=win, tex="sqrXsqr", units="deg", pos=(0,0), size=(48,38), sf=0.5, contrast=-1)
timer = core.CountdownTimer(15)
while timer.getTime() > 0:
    g1.draw()
    win.flip()
    ISI.start(0.5)
    for pos_b, pos_w in zip(black_1_xys, white_1_xys):
        black_1 = visual.rect.Rect(win=win, size=(1,1.1), pos=pos_b, fillColor="black", units="deg")
        white_1 = visual.rect.Rect(win=win, size=(1,1.1), pos=pos_w, fillColor="white", units="deg")
        black_1.draw()
        white_1.draw()
    ISI.complete()
    win.flip()

    ISI.start(0.5)
    for pos_b, pos_w in zip(black_2_xys, white_2_xys):
        black_2 = visual.rect.Rect(win=win, size=(1,1.1), pos=pos_b, fillColor="black", units="deg")
        white_2 = visual.rect.Rect(win=win, size=(1,1.1), pos=pos_w, fillColor="white", units="deg")
        black_2.draw()
        white_2.draw()
    ISI.complete()
    win.flip()
