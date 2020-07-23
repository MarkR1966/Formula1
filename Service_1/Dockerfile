FROM python:alpine3.11

RUN mkdir -p /opt/f1

COPY . /opt/f1

WORKDIR /opt/f1

RUN pip3 install -r requirements.txt

ENTRYPOINT ["python3","app.py"]