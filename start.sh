#!/bin/bash

sudo apt-get update
sudo apt-get -y install python3-pip
pip3 --version

pip3 install -r requirements.txt

python3 main.py