FROM ubuntu:20.04
ENV ANSIBLE_VERSION 2.9.17
RUN apt-get update; \
    apt-get install -y gcc python3; \
    apt-get install -y python3-pip; \
    apt-get clean all
RUN pip3 install --upgrade pip; \
    pip3 install "ansible==${ANSIBLE_VERSION}"; \
    pip3 install ansible

COPY file1.txt /home/.
COPY ../Packages/*.TapPackage /home/Packages/.