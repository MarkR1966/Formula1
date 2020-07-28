#!/bin/bash

if [[ "$(docker service -q markr1966/f1_service_1:latest 2> /dev/null)" == "" ]]; then
    docker build -t markr1966/f1_service_1 ./Service_1
    docker push markr1966/f1_service_1
else
    docker pull markr1966/f1_service_1
    docker service update service_1
fi

if [[ "$(docker service -q markr1966/f1_service_1:latest 2> /dev/null)" == "" ]]; then
    docker build -t markr1966/f1_service_2 ./Service_2
    docker push markr1966/f1_service_2
else
    docker pull markr1966/f1_service_2
    docker service update service_2
fi

if [[ "$(docker service -q markr1966/f1_service_1:latest 2> /dev/null)" == "" ]]; then
    docker build -t markr1966/f1_service_3 ./Service_3
    docker push markr1966/f1_service_3
else
    docker pull markr1966/f1_service_3
    docker service update service_3
fi

if [[ "$(docker service -q markr1966/f1_service_1:latest 2> /dev/null)" == "" ]]; then
    docker build -t markr1966/f1_service_4 ./Service_4
    docker push markr1966/f1_service_4
else
    docker pull markr1966/f1_service_4
    docker service update service_4
fi