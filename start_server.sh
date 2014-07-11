#!/bin/bash

spawn-fcgi -d /home/dane/leak_demo -f /home/dane/leak_demo/main.py -a 127.0.0.1 -p 2148
