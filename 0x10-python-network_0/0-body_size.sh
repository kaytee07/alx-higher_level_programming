#!bin/bash
# a bashscript that displays the size of the body of url passed
curl -s "$1" | wc -c
