# Blinkt

Fooling around with Blinkt! LED bars for Raspberry Pi 

Based on Pimoroni code: https://github.com/pimoroni/blinkt

## Pre-Requisites

On Raspbian:

    sudo apt-get install python3-blinkt python3-psutil

## Running

On Raspbian:

    python cpu_load.py

## Installing as a Service

On Raspbian:

    sudo mkdir /opt/blinkt
    sudo cp cpu_load.py /opt/blinkt
    sudo cp contrib/blinkt.service /lib/systemd/system
    sudo chmod 644 /lib/systemd/system/blinkt.service
    sudo systemctl daemon-reload
    sudo systemctl enable blinkt.service
    sudo systemctl start blinkt.service

