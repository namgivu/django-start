#!/usr/bin/env bash

#ref. https://www.digitalocean.com/community/tutorials/how-to-install-mysql-on-ubuntu-16-04#introduction
sudo apt-get update
sudo apt-get install mysql-server
sudo mysql_secure_installation
