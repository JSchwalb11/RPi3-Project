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

