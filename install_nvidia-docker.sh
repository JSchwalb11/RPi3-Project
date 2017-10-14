#!/bin/bash
# A simple script to install docker-ce
sudo apt-get update
sudo add-apt-repository ppa:graphics-drivers/ppa
sudo apt-get update
sudo apt-get install nvidia-384
sudo-apt-get install \
apt-transport-https \
ca-certificates \
curl \
software-properties-common
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo apt-get fingerprint 0EBFCD88
sudo add-apt-repository \
	“deb[arch=amd64] https://download.docker.com/linux/ubuntu \
	$(lsb_release -cs) \
	stable”
sudo apt-get install docker-ce

## Extension to install_docker-ce program to include NVIDIA-docker
wget -P /tmp	https://github.com/NVIDIA/nvidia-docker/releases/download/v1.0.1/nvidia-docker_1.0.1-1_amd64.deb
sudo dpkg -i /tmp/nvidia-docker*.deb && rm /tmp/nvidia-docker*.deb
sudo apt-get install nvidia-modprobe

## Uncomment the following to auto-pull nvidia/cuda
## sudo nvidia-docker pull --no-cache nvidia/cuda
##
##
## Uncomment the following to auto-pull bvlc/caffe:gpu
## sudo nvidia-docker pull --no-cache bvlc/caffe:gpu
##
##
## Uncomment the following to auto-pull/run nvidia/cuda and test to see if it recognizes GPU
## sudo nvidia-docker run nvidia/cuda nvidia-smi
##
##
## Uncomment the following to auto-pull/run/interactive-console for nvidia/cuda
## sudo nvidia-docker run -it nvidia/cuda 
##
##
## More auto run commands can be found in run_nvidia-docker.sh
