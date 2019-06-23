FROM python:alpine

COPY . /var/pyzz/
WORKDIR /var/pyzz/

RUN pip install .
RUN pyzz
RUN pycpf