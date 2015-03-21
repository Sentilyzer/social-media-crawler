#!/bin/bash

DBUSER=smc
DBPASSWD=smcPASSWORD
DBHOST=localhost
DBNAME=smc_db

# set system timezone
echo "Europe/Berlin" | sudo tee /etc/timezone
dpkg-reconfigure -f noninteractive tzdata

# add github to known SSH Hosts
ssh-keyscan -t rsa github.com >> ~/.ssh/known_hosts

# add APT-Keys and Repositories

sudo add-apt-repository "deb http://www.rabbitmq.com/debian/ stable main"
wget https://www.rabbitmq.com/rabbitmq-signing-key-public.asc
sudo apt-key add rabbitmq-signing-key-public.asc

# update package list and install essential packages
apt-get update -y
apt-get upgrade -y

# install basic packages
apt-get install -y build-essential curl git vim libssl-dev man

# install python stuff
apt-get install -y python python-pip python-software-properties python-dev python-setuptools

# install rabbitmq
apt-get install -y rabbitmq-server

# mysql configuration variables needed for mysql setup
sudo debconf-set-selections <<< "mysql-server \
 mysql-server/root_password password $DBPASSWD"
sudo debconf-set-selections <<< "mysql-server \
 mysql-server/root_password_again password $DBPASSWD"

apt-get install -y mysql-server libmysqlclient-dev

# create database and user
mysql -uroot -p$DBPASSWD -e "CREATE DATABASE IF NOT EXISTS $DBNAME"
mysql -uroot -p$DBPASSWD -e "grant all privileges on $DBNAME.* to '$DBUSER'@'localhost' identified by '$DBPASSWD'"

# install social media crawler specific python packages
pip install -r /vagrant/requirements.txt
