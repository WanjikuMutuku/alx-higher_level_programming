#!/bin/bash
# takes URL, send request and displays body of response
curl -sX GET $1 -L
