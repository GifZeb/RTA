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

### Gantt Chart
Total time we took for this project is 95 days. We used android app developed for our software project and implemented it according to the sensors.
Tarun: PCB,All the stuff related to SHT31-D, signup and lgin in app, connecting app with database, All Documentation and maintaining github.
Divya: PCB, Hardware working together, settings in app, intents and layouts in app.
Jasleen: Hardware connection with firebase, retriving database values in app.
Software took most of the time, hardware only took time at PCB stage which was the most crutial part as it has to be right to run the sensors. Futher stuff of connecing hardware to firebase only took a week.

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
### PCB Design
![pcb_design](https://user-images.githubusercontent.com/43179715/52145141-3c16f780-262e-11e9-8dee-4e2f466e34ab.png)

#### PCB Front Side
<img src="https://user-images.githubusercontent.com/43179715/52144970-c27f0980-262d-11e9-96ef-0968ba6a1e12.jpg" width="500" height="500">

#### PCB Back Side
<img src="https://user-images.githubusercontent.com/43179715/52144971-c317a000-262d-11e9-8339-edbdd1949e3f.jpg" width="500" height="500">

### Power Up
After all the components are connected, your PCB should look like this.
 <img src="https://user-images.githubusercontent.com/43179715/52145078-112ca380-262e-11e9-9f1c-01fc8742172b.jpg" width="500" height="500">
 
### i2c Detection Proof (0x45)
Type the following command in terminal

````
i2cdetect -y 1
````
To confirm that the PCB is working properly, address was checked for all the sensors using command:
sudo i2cdetect -y 1
We got the correct address for all the sensors
SHT31 Address: 45
Chirp! Water Sensor Address: 20
OLED Display Address: 3c

<img src="https://user-images.githubusercontent.com/43179715/53652216-52f13f80-3c16-11e9-8c3e-cc2e6cad20d4.jpg" width="500" height="500">

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
https://github.com/GifZeb/RTA/tree/master/CODE

### Final Testing
Running python script will get you the readings

#### Data Display
<img src="https://user-images.githubusercontent.com/43179715/53650932-a6ae5980-3c13-11e9-9985-27390898a383.jpg" width="500" height="500">

#### OLED Display
<img src="https://user-images.githubusercontent.com/43179715/53650878-88e0f480-3c13-11e9-9c81-11bb644dea0e.jpg" width="500" height="500">

## Configuration of Hardware and Software
Hardware and Software doesn't have any direct connection. They are connected through the firebase database which is responsible for sending current values of temperature, humidity and soil moisture to the android application designed for this sepcific project. 

## How to setup database
For setting up database, Firebase is used where datbase structure is defined as per our requirement. The same firebase database is called from app and hardware. Hardware sends the values of temperature, humidity and soil moisture to the firebase through internet connection and firebase further sends that data to the android application.
## Database structure
![datbasestruct](https://user-images.githubusercontent.com/43179715/53690619-1586d200-3d3c-11e9-99f0-93a4a3bd9b5b.PNG)

## Android APP Build Intructions
Please refer to the following link for the code:
https://github.com/GifZeb/Software-Project-master

## Running the Project
Our Project works fully as we are able to get the proper readings displayed on the firebase as well as on the app. Python coding is done in raspberry pi 3 to establish a connection between firebase and hardware, and the same firebase is further connected to the app. At first, after running the python codes for all the three sensors simultaneously, hardware sends the values of temperature, humidity and soil moisture to the database after every 5 seconds (gets updated). Than OLED Monochrome Display retrieves temperature and moisture values from the database and displays it on hardware. At the same time, firebase sends these values to the Android application which also gets updated every 5 seconds.
