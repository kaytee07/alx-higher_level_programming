#!/bin/bash
# Sends a JSON post request.
curl -s -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
