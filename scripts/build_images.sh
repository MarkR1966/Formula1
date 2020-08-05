#!/bin/bash

docker build --no-cache -t markr1966/f1_service_1 ./Service_1
docker push markr1966/f1_service_1
docker build --no-cache -t markr1966/f1_service_2 ./Service_2
docker push markr1966/f1_service_2
docker build --no-cache -t markr1966/f1_service_3 ./Service_3
docker push markr1966/f1_service_3
docker build --no-cache -t markr1966/f1_service_4 ./Service_4
docker push markr1966/f1_service_4
docker build --no-cache -t markr1966/nginx ./nginx
docker push markr1966/nginx:latest