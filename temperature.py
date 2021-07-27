#!/usr/bin/env python

import os
import glob
import time

 
os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

base_dir = '/sys/bus/w1/devices/'

# Typical reading
# 73 01 4b 46 7f ff 0d 10 41 : crc=41 YES
# 73 01 4b 46 7f ff 0d 10 41 t=23187

while True:
  
  for sensor in glob.glob(base_dir + "28-00*/w1_slave"):
    id = sensor.split("/")[5]

    try:
      f = open(sensor, "r")
      data = f.read()
      f.close()
      if "YES" in data:
        (discard, sep, reading) = data.partition(' t=')
        t = float(reading) / 1000.0
        print("{} {:.1f}".format(id, t))
      else:
        print("999.9")

      except:
        print("Failed to read sensor")
        pass

      time.sleep(3.0)
