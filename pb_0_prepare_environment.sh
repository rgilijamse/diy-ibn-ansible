#!/bin/bash

# make sure you're running Python 3.7+

# install requirements
pip install -r requirements.txt

# create folder structure
mkdir configs
mkdir inventory
mkdir inventory/host_vars
mkdir inventory/group_vars
