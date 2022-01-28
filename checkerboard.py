from psychopy import visual, core

win = visual.Window(size=[800,800], monitor="testMonitor", units="pix", viewPos=(-400,-400))
check_size=0.5
cross1 = visual.Line(win=win, start=[0.9,1], end=[1.1,1], lineWidth=2, lineColor="red", units="norm")
cross2 = visual.Line(win=win, start=[1,0.9], end=[1,1.1], lineWidth=2, lineColor="red", units="norm")

for frameN in range(10):
    for r in range(5):
        for c in range(5):
            if r%2:
                if not c%2:
                    fill="white"
                else:
                    fill="black"
                
            else:
                if not c%2:
                    fill="black"
                else:
                    fill="white"
            
            rect_1 = visual.rect.Rect(win=win, size=check_size, pos=[0.25+c/2, 0.25+r/2], fillColor=fill, units="norm")
            rect_2 = visual.rect.Rect(win=win, size=check_size, pos=[0.75+c/2, 0.75+r/2], fillColor=fill, units="norm")
            rect_1.draw()
            rect_2.draw()

    cross1.draw()
    cross2.draw()
    win.flip()
    core.wait(0.5)

    for r in range(5):
        for c in range(5):
            if r%2:
                if not c%2:
                    fill="black"
                else:
                    fill="white"
                
            else:
                if not c%2:
                    fill="white"
                else:
                    fill="black"
            
            rect_1 = visual.rect.Rect(win=win, size=check_size, pos=[0.25+c/2, 0.25+r/2], fillColor=fill, units="norm")
            rect_2 = visual.rect.Rect(win=win, size=check_size, pos=[0.75+c/2, 0.75+r/2], fillColor=fill, units="norm")
            rect_1.draw()
            rect_2.draw()
    
    cross1.draw()
    cross2.draw()
    win.flip()
    core.wait(0.5)