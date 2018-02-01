from flask import Flask, request
import json 
from droneData import Swarm
from flask_api import FlaskAPI

app = FlaskAPI(__name__)

swarm = Swarm()

#----------------------------------------Routing/Mapping------------------------------------------

#-----------------------------------Handle requests to add drone to swarm----------------------------
@app.route('/', methods=['GET', 'POST'])
def clientIsAddingDrone():
    #once a POST request is made to index, we will initialize a new drone into the swarm
    if request.method == 'POST':
        print('\nAdding Drone To The Network')
        swarm.addDrone(request.get_json(force=True))
        return swarm.getDroneInfo(request.get_json(force=True)["id"])
    return "No Data"
#------------------------------------------------------------------------------------------------------

#-----------------------------------Handle requests to update dron data----------------------------
@app.route('/dronedata', methods=['GET', 'POST'])
def clientRequestedData():
    if request.method == 'POST':
        #print("JSON: ", request.get_json(force=True))
        return swarm.updateDroneInfo(request.get_json(force=True))
    if request.method == 'GET':
        print("\nGETTING DATA FOR DRONE : ",request.data['droneID'],"\n",type(request.data['droneID']))
        droneToReturn = swarm.getDroneInfo(request.data['droneID'])
        if droneToReturn is not None :
            return swarm.getDroneInfo(request.data['droneID'])

    return "NO_DATA"
#--------------------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------------------------------------------

#---------------Start the app--------------------------------------
if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000,debug=False)
#-----------------------------------------------------------------