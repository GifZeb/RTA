# Real Time Arboretum

## BUILD INSTRUCTIONS

## Table of Contents
1. [Purchases](#purchases)
2. [Gantt Chart](#gantt-chart)
3. [Hardware Assembly](#hardware-assembly)
4. [Configuration of Hardware and Software](#configuration-of-hardware-and-software)
5. [How to setup database](#how-to-setup-database)
6. [Database Structure](#database-structure)
7. [Android App Build Intructions](#android-app-build-intructions)
8. [Running the Project](#running-the-project)

## Purchases
![budget](https://user-images.githubusercontent.com/43179715/53663809-ba1dec80-3c34-11e9-8bbf-b638da49fa36.PNG)

## Gantt Chart
Tarun: PCB, All Documentation and maintaining github.
Divya: PCB, Hardware.
Jasleen: Hardware connection.

## Hardware Assembly
We are using three sensors:
SHT31-D Temperature and Humidity Sensor
https://www.adafruit.com/product/2857
Chirp! Water Sensor
https://www.adafruit.com/product/1965
OLED Display
https://www.adafruit.com/product/2719

### Setting up Raspberry Pi
First step after getting your raspberry pi is to set it up. Follow the steps below:
1. Download [Raspbian](https://www.raspberrypi.org/downloads/) to be installed on your raspberry pi.
2. Use [SDCardFormatter](https://www.sdcard.org/downloads/formatter_4/) to format your SD card and flash downloaded OS on your SD card.
3. Insert SD card in raspberry pi and connect the side devices like keyboard and mouse.
4. Switch on the power and finish the further setup.

### Hardware Testing

After software installation, i made the connections using jumper wires from sensor to breadboard and breadboard to raspberry pi.

Wiring:
![pcb_design](https://user-images.githubusercontent.com/43179715/52145141-3c16f780-262e-11e9-8dee-4e2f466e34ab.png)

### i2c Detection Proof (0x45)
Type the following command in terminal

````
i2cdetect -y 1
````
<img src="https://user-images.githubusercontent.com/43179715/53652216-52f13f80-3c16-11e9-8c3e-cc2e6cad20d4.jpg" width="500" height="500">

### PCB Design
![pcb_design](https://user-images.githubusercontent.com/43179715/52145141-3c16f780-262e-11e9-8dee-4e2f466e34ab.png)

### Unit Testing
Follow these steps to get readings from your sensor.
````
sudo apt-get update
````
````
sudo apt-get upgrade
````
To install sht31d libraies, run this command
````
sudo pip3 install adafruit-circuitpython-sht31d
````
### Python Script
You can use the code underneath to get the readings from your sensor:

### Final Testing
Running python script will get you the readings
<img src="https://user-images.githubusercontent.com/43179715/53650932-a6ae5980-3c13-11e9-9985-27390898a383.jpg" width="500" height="500">

### Configuration of Hardware and Software
Hardware and Software doesn't have any direct connection. They are connected through the firebase database which is responsible for sending current values of temperature, humidity and soil moisture to the android application designed for this specific project. 

### How to setup database
For setting up database, Firebase is used where datbase structure is defined as per our requirement. The same firebase database is called from app and hardware. Hardware sends the values of temperature, humidity and soil moisture to the firebase through internet connection and firebase further sends that data to the android application.

### Database structure
![datbasestruct](https://user-images.githubusercontent.com/43179715/53690619-1586d200-3d3c-11e9-99f0-93a4a3bd9b5b.PNG)

### Android APP Build Intructions
Please refer to the following link for the code:
https://github.com/GifZeb/Software-Project-master

### Running the Project
Our Project works fully as we are able to get the proper readings displayed on the firebase as well as on the app.
