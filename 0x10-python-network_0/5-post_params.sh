#!/bin/bash
# takes in a URL, sends a POST request, and displays body of the response
curl -sX POST -d "email=test@gmail.com" -d "subject=I will always be here for PLD" "$1"
