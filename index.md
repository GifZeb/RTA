# REAL TIME ARBORETUM

## Introduction
This project combines three sensors to get the temperature, humidity and soil moisture levels of the surroundings and display it on the screen. 

## Sensors
These are the sensors we are using:

### Chirp! Water sensor
https://www.adafruit.com/product/1965
### SHT31- Humidity and temperature sensor.
https://www.adafruit.com/product/2857
### OLED Display
https://www.adafruit.com/product/2719

## January 18th, 2019
Decided on the project and submitted the proposal.
[Proposal.docx](https://github.com/GifZeb/RTA/files/2823031/Proposal.docx)

## January 25th, 2019
Submitted Software Requirement Specification and started PCB Designing. The sensors are soldered already.
[SoftwareRequirementSpecifications.docx](https://github.com/GifZeb/RTA/files/2823035/SoftwareRequirementSpecifications.docx)

<img src="https://user-images.githubusercontent.com/43179715/52145141-3c16f780-262e-11e9-8dee-4e2f466e34ab.png" width="500" height="500">

## Febuary 1st ,2019
PCB is fully done and ready for soldering but we figured a problem at this point.

### PCB Front Side
<img src="https://user-images.githubusercontent.com/43179715/52144970-c27f0980-262d-11e9-96ef-0968ba6a1e12.jpg" width="500" height="500">

### PCB Back Side
<img src="https://user-images.githubusercontent.com/43179715/52144971-c317a000-262d-11e9-8339-edbdd1949e3f.jpg" width="500" height="500">

### Problems Faced
Socket Headers we are using have small pins but due to our massive wiring structure reqwuired for the working of sensor, This pcb required headers with long pins so that the soldering can be done from both sides
<img src="https://user-images.githubusercontent.com/43179715/52145078-112ca380-262e-11e9-9f1c-01fc8742172b.jpg" width="500" height="500">

Here the raspberry pi header is perfect but the headers for all the sensors should have long pins so that all the connections can be covered while soldering, this requires us to spend not more than 15 dollars.

## Febuary 8th ,2019
New Socket headers were bought and in total it added additional cost of 20 dollars in our budget. New soldered PCB along with the socket headers.
To confirm that the PCB is working properly, address was checked for all the sensors using command:
sudo i2cdetect -y 1
We got the correct address for all the sensors
SHT31 Address: 45
Chirp! Water Sensor Address: 20
OLED Display Address: 3c

<img src="https://user-images.githubusercontent.com/43179715/53652216-52f13f80-3c16-11e9-8c3e-cc2e6cad20d4.jpg" width="500" height="500">

## Febuary 15th ,2019
Reading Week

## Febuary 22th ,2019
Hardware, Database and App working fully.

### OLED Display
<img src="https://user-images.githubusercontent.com/43179715/53650878-88e0f480-3c13-11e9-9c81-11bb644dea0e.jpg" width="500" height="500">

### Data Display
<img src="https://user-images.githubusercontent.com/43179715/53650932-a6ae5980-3c13-11e9-9985-27390898a383.jpg" width="500" height="500">

## March 15th,2019
Other locations having no access to the sensor will get updated along with the updatation in the values  of sensor location. Some Random data will be generated so as to make other locations have some change in the results.

### Database
<img src="https://user-images.githubusercontent.com/43179715/54845432-abfd4200-4caf-11e9-93cb-c69b4bab6852.png" width="500" height="500">

## March 22nd, 2019
Working on the alarm system of Chirp! Water sensor. So that when the level goes really down then it will update and the values should not be just a number but something valueable which gives sense to soil moisture value. Maximum and minimum soil moisture values are measured to determine the range of soil moisture.
Also, the enclosure is up for fixing. There is a height problem.

## March 29th,2019
Prototype lab sent our latest version of enclosure this week. The random value generation by hardware for the locations without any sensors attached was fixed. Now, every five seconds, original sensor location value as well as simulated locations values are updated.
The problem we faced this week was setting up the moisture values. The real values are being updated but moisture values needed to be more elaborated for easy understanding. Maximum and minimum values are set as per moisture sensor range.  

### Work Distribution
Divya was working on setting the moisture values according to range of the Chirp! Water Sensor.
Jasleen worked on the enclosure.
Tarun updated the GitHub as well as all the reports and other documentations.

Soil moisture level calibration is fixed according to the range of the maximum and minimum levels. Enclosure have problem with the width and this would be third time we are fixing it. 
Underneath is the problem, we faced with the enclosure. We will be using the four parts of the same acrylic structure case we built. 
<img src="https://user-images.githubusercontent.com/43179715/55254649-d8283e00-522e-11e9-9259-b4d211e35897.jpg" width="500" height="500">
<img src="https://user-images.githubusercontent.com/43179715/55254653-d9596b00-522e-11e9-99e1-c333a67201b8.jpg" width="500" height="500">

## April 5th,2019
This week, the enclosure is finished and fits properly.
![enclose](https://user-images.githubusercontent.com/43179715/55646676-d10eac00-57a9-11e9-8c1a-c41966da06f9.jpg)

Calibration is finshed as well where the maximum and minimum values are measured by instering sensor end to the water to get maximum value which was 660 and mimimum value when it is dry. Then the database values was changed accordingly and new value is in prcentage for moisture level.
### Moisture value in Database 
![Capture](https://user-images.githubusercontent.com/43179715/55646550-707f6f00-57a9-11e9-8ffc-896d2375996c.PNG)

## April 12th, 2019
This week, no new stuff but demonstartion of the project and fixing the wifi of raspberry pi. Finishing up report which is not even in its half way. 


