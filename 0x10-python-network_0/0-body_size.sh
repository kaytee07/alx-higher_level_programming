#!/bin/bash
# display the size of the body in byte
curl -s "$1" | wc -c
