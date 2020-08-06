# Information required to build Service_1 image and include required python libraries
# Use alpine 3.11 image with included python from Docker Hub. Used due to small image size
FROM python:alpine3.11
# Update files
RUN apt update -y
# Create directory to store Service_1 application in
RUN mkdir -p /opt/f1
# Copy the required files to the direcory
COPY . /opt/f1
# Set the working directory to Service_1 installation directory
WORKDIR /opt/f1
# Install the required python libraries for Service_1
RUN pip3 install -r requirements.txt
# Set the required Entry point to launch the Service_1 application
ENTRYPOINT ["python3","app.py"]