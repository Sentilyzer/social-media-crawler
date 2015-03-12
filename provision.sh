#!/bin/bash

# set system timezone
echo "Europe/Berlin" | sudo tee /etc/timezone
dpkg-reconfigure -f noninteractive tzdata

# update package list and install essential packages
echo "Updating packages...\n"
apt-get update -y
echo "Installing packages...\n"
apt-get install -y build-essential curl git vim libssl-dev man python python-pip

# add github to known SSH hosts
ssh-keyscan -t rsa github.com >> ~/.ssh/known_hosts

# install python requirements from requirements.txt
cd /vagrant && pip install -r requirements.txt
