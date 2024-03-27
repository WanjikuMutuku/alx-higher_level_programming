#!/bin/bash
# takes in a URL,sends a GET request, and displays the body of the response
curl -sX GET $1 -H "X-HolbertonSchool-User-Id: 98" -L
