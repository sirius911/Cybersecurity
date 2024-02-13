#!/bin/bash
read -p "Enter username: " username
read -s -p "Enter password: " password
docker build --build-arg USER_NAME=$username --build-arg USER_PASS=$password -t $1 .
