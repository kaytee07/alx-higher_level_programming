#!/bin/bash
# display response code
curl -s -o /dev/null -w "%{http_code}" "$1"
