import nidaqmx

task = nidaqmx.Task()
task.do_channels.add_do_chan("Dev2/port0/line0:2")
task.do_channels.add_do_chan("Dev2/port1/line0:2")

# for channel in task.do_channels:
#     print(channel.physical_channel)
task.read(4)
# val = 0
# while 0 <= val <= 7:
#     task.write(val, )
#     val = int(input("Enter bw 0-7"))
    
# task.write([[4,7], [4,7]])

# if task.is_task_done():
#     print(task.read())
#     task.write(0)
#     task.close()

task.close()