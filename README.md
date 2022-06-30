# Blinkt

Fooling around with Blinkt! LED bars for Raspberry Pi 

## Pre-Requisites

On Raspbian:

    sudo apt-get install python3-blinkt python3-psutil

## Running

On Raspbian:

    python cpu_load.py

## Installing as a Service

On Raspbian:

    sudo cp cpu_load.py /opt
    sudo cp contrib/blinkt.service /lib/systemd/system
    sudo chmod 644 /lib/systemd/system/blinkt.service
    sudo systemctl enable blinkt.service
    sudo systemctl start blinkt.service

