from firebase import firebase
import smbus
import time
import sys
import datetime
from time import strftime
firebase = firebase.FirebaseApplication('https://arboretum-78f7c.firebaseio.com/',None)

var = 1
while var==1:
    # Get I2C bus
    bus = smbus.SMBus(1)

    # SHT31 address, 0x45(68)
    # Send measurement command, 0x2C(44)
    #		0x06(06)	High repeatability measurement
    bus.write_i2c_block_data(0x45, 0x2C, [0x06])

    time.sleep(0.5)

    # SHT31 address, 0x44(68)
    # Read data back from 0x00(00), 6 bytes
    # Temp MSB, Temp LSB, Temp CRC, Humididty MSB, Humidity LSB, Humidity CRC
    data = bus.read_i2c_block_data(0x45, 0x00, 6)

    # Convert the data
    temp = data[0] * 256 + data[1]
    cTemp = -45 + (175 * temp / 65535.0)
#    fTemp = -49 + (315 * temp / 65535.0)
    humidity = 100 * (data[3] * 256 + data[4]) / 65535.0

    # Output data to screen
#    print "\n\nNew Reading----------------------"
#    print "Temperature in Celsius is : %.2f C" %cTemp
#    print "Temperature in Fahrenheit is : %.2f F" %fTemp
#    print "Relative Humidity is : %.2f %%RH" %humidity
#    print "\n"

    #store the host ID
    datetimeWrite = (time.strftime("%Y-%m-%d ")+time.strftime(" %H:%M:%S")) 
    result2 = firebase.put('Brampton/node1','time',datetimeWrite)
    result = firebase.put('Brampton/node1','temp',str(cTemp))
    result1 = firebase.put('Brampton/node1','humidity',str(humidity))
    print(result)
    print(result1)
    print(result2)

    time.sleep(5)
