#!/bin/bash
# Make request to server and cause it to respond with "You got me!"
curl -sLX PUT -d "user_id=98" --header "Origin: HolbertonSchool" 0.0.0.0:5000/catch_me
