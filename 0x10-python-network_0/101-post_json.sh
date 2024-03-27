#!/bin/bash
# Send JSON POST request and display response body
curl -s -X POST -H "Content-Type: application/json" -d "$(cat $2)" "$1"
