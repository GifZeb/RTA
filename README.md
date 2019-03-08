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

### Purchases
![budget](https://user-images.githubusercontent.com/43179715/53663809-ba1dec80-3c34-11e9-8bbf-b638da49fa36.PNG)
### Gantt Chart
Tarun: PCB, All Documentation and maintaining github.
Divya: PCB, Hardware.
Jasleen: HArdware connection.

### Hardware Assembly
We are using three sensors:
SHT31-D Temperature and Humidity Sensor
Chirp! Water Sensor
OLED Display

### Configuration of Hardware and Software
Hardware and Software doesn't have any direct connection. They are connected through the firebase database which is responsible for sending current values of temperature, humidity and soil moisture to the android application designed for this sepcific project. 

### How to setup database
For setting up database, Firebase is used where datbase structure is defined as per our requirement. The same firebase database is called from app and hardware. Hardware sends the values of temperature, humidity and soil moisture to the firebase through internet connection and firebase further sends that data to the android application.
### Database structure
![datbasestruct](https://user-images.githubusercontent.com/43179715/53690619-1586d200-3d3c-11e9-99f0-93a4a3bd9b5b.PNG)

### Android APP Build Intructions
Please refer to the following link for the code:
https://github.com/GifZeb/Software-Project-master

### Running the Project
Our Project works fully as we are able to get the proper readings displayed on the firebase as well as on the app.
