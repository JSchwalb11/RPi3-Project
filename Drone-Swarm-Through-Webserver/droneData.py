import json
import time
#--------------What the Drone data structure will look like--------------
#-------This is not the actual object used to store active drones--------
# ----a one element list, which contains a dictionary--------------------
#-----whose keys are the Drone ID, and whose value is another dict containing the params------
Drones = [
            {
            "ID":1,
            "latitude":"~",
            "longitude":"~",
            "altitude":"~",
            "armed":"False"
            },
            {
            "ID":2,
            "latitude":'~',
            "longitude":'~',
            "altitude":'~',
            "armed":'True'
            }
        ]
#--------------------^^For Visual Aid Only^^----------------------------
class Swarm(object) :   

    #--------------------Constructor Function--------------------------    
    def __init__(self): 
        self.swarm = []
    #------------------------------------------------------------------

    #--------------------Member Functions------------------------------
    def findDroneByID(self,value):
        index=0
        for drone in self.swarm:
            # for attribute, value in drone.items():
            #      if(attribute == "id"):
            if(drone["id"]==value):
                return drone
            index=index+1
        return None
    def getIndexOfDroneByID(self,value):
        index=0
        for drone in self.swarm:
            # for attribute, value in drone.items():
            #      if(attribute == "id"):
            if(drone["id"]==value):
                return index
            index=index+1
        return None
    def addDrone(self,data):
        #This function is used to add a drone to the swarm.
        self.swarm.append(data)
        print("\nAdded a drone with params",data,"\n")
        print("Current Swarm Stats\n----------------------\n",self.swarm,"\n")
    def removeDrone(self,data):
        pass # we need a function to remove a drone from the network
    def getNumNodesInSwarm(self):
        return self.swarm.count

    def updateDroneInfo(self,data):
        index = 0
        print("\n\nDATA: ",data," TYPE: ",type(data))
        # for drone in self.swarm:
        #     for attribute, value in drone.items():
        #          if(attribute == "id"):
        #              if(data["id"]==value):
        #                 print("udpate this drone")
        #                 self.swarm[index] = data
        #                 return data
        indxDroneToUpdate = self.getIndexOfDroneByID(data["id"])
        if self.swarm[indxDroneToUpdate] :
            #print("\nSuccessfully Updated Drone\n",droneToUpdate,"\nWith\n",data,"\n")
            self.swarm[indxDroneToUpdate]=data
            print("Current Swarm Stats\n----------------------\n",self.swarm,"\n")
            return self.swarm[indxDroneToUpdate]
        else:
            print("\nDid not find drone by id, no recrod updated\n")
            return  "Could Not Find Drone To Update"
        
    def getDroneInfo(self,idOfDrone):
        #print("\n\n DRONE PARAMS TO RETURN: ",self.findDroneByID(idOfDrone),"\n\n")
        return self.findDroneByID(idOfDrone)
    #------------------------------------------------------------------       