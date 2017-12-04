from dronekit import connect
from dronekit.lib import VehicleMode, LocationGlobal
import RPi.GPIO as GPIO
from lib_nrf24 import NRF24
import time
import spidev

connectionString= '/dev/ttyACM0'
print 'connecting to vehicle on: %s' %connectionString
vehicle = connect(connectionString,wait_ready=True)

print 'Connected To Drone'

GPIO.setmode(GPIO.BCM)

pipes = [[0xe7,0xe7,0xe7,0xe7,0xe7],[0xc2,0xc2,0xc2,0xc2,0xc2]]

radio = NRF24(GPIO, spidev.SpiDev())
radio.begin(0,17)
radio.setPayloadSize(32)
radio.setChannel(0x70)

radio.setDataRate(NRF24.BR_2MBPS)
radio.setPALevel(NRF24.PA_LOW)
radio.setAutoAck(True)
radio.enableDynamicPayloads()
radio.enableAckPayload()

radio.openReadingPipe (1, pipes[1])
radio.openWritingPipe (pipes[0])

radio.startListening() #Since this is receiver pi we are begin listening first thing
print 'started Listening'

def getAltitude():
    return vehicle.location.global_frame.alt

def sendData(ID,value):
    #stop listening so we can send back the data
    radio.stopListening()
    message = list(ID) + list(str(value)) #Must be less than or equal to 32Bytes
    radio.write(message)
    print 'Sent Data : %s' % value
    radio.startListening()

#Main Loop
while True:
        
    ackPL = [1]
    print 'waiting to receive...'
    while not radio.available(0):
        time.sleep(1/100)
    print 'received'
    
    receivedMessage = []
    radio.read(receivedMessage,radio.getDynamicPayloadSize())
    print("Received: {}".format(receivedMessage))
    
    #decode the array thats received in receivedMessage
    command=''
    for n in receivedMessage:
        # decode into standard unicode set
        if(n>=32 and n<=126):
            command+=chr(n)
    print(command)
    
    if command == 'GET_ALTITUDE':
        print 'Received Command To Get Altitude'
        alt=getAltitude()
        sendData('SlaveDrone_Alt_',alt)
    
    radio.writeAckPayload(1,ackPL,len(ackPL))
    print("Loaded Payload Reply of {}".format(ackPL))
    
    time.sleep(1)
    
