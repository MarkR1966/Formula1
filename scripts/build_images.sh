#!/bin/bash
# build image for service_1 and push to DockerHub
docker build --no-cache -t markr1966/f1_service_1 ./Service_1
docker push markr1966/f1_service_1

# build image for service_2 and push to DockerHub
docker build --no-cache -t markr1966/f1_service_2 ./Service_2
docker push markr1966/f1_service_2

# build image for service_3 and push to DockerHub
docker build --no-cache -t markr1966/f1_service_3 ./Service_3
docker push markr1966/f1_service_3

# build image for service_4 and push to DockerHub
docker build --no-cache -t markr1966/f1_service_4 ./Service_4
docker push markr1966/f1_service_4
