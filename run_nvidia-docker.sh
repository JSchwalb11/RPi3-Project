## Script to auto run nvidia-docker environment interactively
## You can add which image you would like to run in here
##
##
## Default is nvidia/cuda
##sudo nvidia-docker run -it nvidia/cuda
##
## Uncomment the following to use bvlc/caffe:gpu image
sudo nvidia-docker run -it bvlc/caffe:gpu

