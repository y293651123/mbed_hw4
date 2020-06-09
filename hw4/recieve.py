import matplotlib.pyplot as plt
import numpy as np
import serial
import time

t = np.arange(0,10,1) 
tilt = np.arange(0,10,1)

serdev = '/dev/ttyUSB0'
s = serial.Serial(serdev, 9600)

for i in range(0, int(10)):
    line=s.readline() # Read an echo string from K66F terminated with '\n'
    # print line
    tilt[i] = int(line)  

fig, ax = plt.subplots(1, 1)
ax.plot(t,tilt, color = "green", linewidth = 1, linestyle = "-", label = "tilt")
# Show legend
ax.legend(loc='lower left', frameon=False)
ax.set_xlabel('Timestamp')
ax.set_ylabel('number')
plt.show()

s.close()