from dronekit import connect
from dronekit.lib import VehicleMode, LocationGlobal
import RPi.GPIO as GPIO
from lib_nrf24 import NRF24
import time
import spidev


connectionString="/dev/ttyACM0"
print ("Connecting To Vehicle on: %s" %connectionString)
vehicle = connect(connectionString,wait_ready=True)

print("Connected To Drone")

GPIO.setmode(GPIO.BCM)

pipes = [[0xe7, 0xe7, 0xe7, 0xe7, 0xe7], [0xc2, 0xc2, 0xc2, 0xc2, 0xc2]]

radio = NRF24(GPIO, spidev.SpiDev())

radio.begin(0, 17)


radio.setPayloadSize(32)
radio.setChannel(0x70)

radio.setDataRate(NRF24.BR_2MBPS)
radio.setPALevel(NRF24.PA_LOW)
radio.setAutoAck(True)
radio.enableDynamicPayloads()
radio.enableAckPayload()

#Open Writing and Reading pipe so we can Do both
radio.openWritingPipe(pipes[1])
radio.openReadingPipe(1, pipes[0]); #Since writing pipe on slave is 0 we read on 0
#radio.printDetails()

def receiveData():
    noResponse = False
    countTimeOut=0;
    radio.startListening()
    #time.sleep(1/2)
    print('started listening')
    print 'Waiting for response'
    while not radio.available(0):
        countTimeOut=countTimeOut+1
        if countTimeOut>100:
            noresponse = True
            break
        time.sleep(1/100)
    if noResponse == True:
        print 'No Response'
    receivedMessage = []
    radio.read(receivedMessage, radio.getDynamicPayloadSize())
    string = ""
    for n in receivedMessage:
        if ( n>=32 and n<=126 ):
            string += chr(n)
            
    print("The Slave Sent Back: %s" % string)
    radio.stopListening()
    
    #time.sleep(1)
    print('stopped listening')
    
while True:
    command = "GET_ALTITUDE"
    radio.write(list(command))
    print("Master Sent The Command {}".format(command))
    
    #check for ack payload
    if radio.isAckPayloadAvailable():
        returnedPL = []
        radio.read(returnedPL, radio.getDynamicPayloadSize())
        print("Returned Payload is {}".format(returnedPL))
        receiveData()
        
    else:
        print("No Payload Received")
        
    time.sleep(1)
