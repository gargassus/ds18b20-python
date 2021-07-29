# Weather station

Weather station to collect data from various sensors

## Hardware:
* Raspberry Pi Zero W to be collective station which collects data from sensors and sends them to server pi 
* TODO: Raspberry Pi 3+? to be server and run influxdb/grafana

## Sensors:
* DS18B20 with diy waterproofing for water temperatures (2 sensors for different depths)
* TODO: Rain meter
* TODO: Humidity

## Software:
* Python script for reading water temperature from DS18B20
* InfluxDB to store data
* Grafana to present data
