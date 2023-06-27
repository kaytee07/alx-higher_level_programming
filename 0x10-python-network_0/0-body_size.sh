#!/usr/bin/env bash
# a bashscript that displays the size of the body of url passed


if [ $# -lt 1 ];
then
    echo "Usage: $0 <URL>"
    exit 1
fi

url=$1
response=$(curl -sI "$url")
content_length=$( echo "$response" | grep -i 'Content-Length' | awk '{print $2}')
echo "$content_length"
