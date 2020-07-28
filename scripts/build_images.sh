#!/bin/bash

if [[ "$(docker images -q markr1966/f1_service_1:latest 2> /dev/null)" == "" ]]; then
    docker build -t markr1966/f1_service_1 ./Service_1
fi

if [[ "$(docker images -q markr1966/f1_service_2:latest 2> /dev/null)" == "" ]]; then
    docker build -t markr1966/f1_service_2 ./Service_2
fi

if [[ "$(docker images -q markr1966/f1_service_3:latest 2> /dev/null)" == "" ]]; then
    docker build -t markr1966/f1_service_3 ./Service_3
fi

if [[ "$(docker images -q markr1966/f1_service_4:latest 2> /dev/null)" == "" ]]; then
    docker build -t markr1966/f1_service_4 ./Service_4
fi