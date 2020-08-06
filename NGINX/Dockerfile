# information required to build nginx image and include required reverse_proxy.conf file
# use latest nginx image from Docker Hub
FROM nginx:latest

# set workdir to nginx directory
WORKDIR /etc/nginx

# ensure packages are latest
RUN apt update -y

# remove default.conf from nginx
RUN rm conf.d/default.conf

# copy required reverse_proxy.conf to nginx image
COPY reverse_proxy.conf conf.d/