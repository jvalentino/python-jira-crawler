#!/bin/bash
clear
rm -rf target/*.json
ulimit -m unlimited  # Unlimited physical memory
ulimit -v unlimited  # Unlimited virtual memory

python3 src/main/python/main.py
