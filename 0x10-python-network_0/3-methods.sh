#!/bin/bash
# Display all server accepted http methods.
curl -sI "$1" | awk '/Allow/ { print substr($0, index($0, $2)) }'
