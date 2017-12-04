#This is the README for saving docker instances

###############################################

docker container ls

#This will open the visible containers for docker instances in use currently
#Note the container ID for saving purposes.

###############################################

#Uncomment the next line to commit any changes made to some docker instance to the docker image.

#docker commit <containerID> <imageID> 

#<containerID> represents the container ID of the image your running found by the above command (docker container ls)
#<imageID> represents the image you want to commit to... if no image is overwritten, it will make another image with
#the given image ID
