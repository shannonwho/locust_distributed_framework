#Multi-stage dockerfiles 
FROM locustio/locust AS test

WORKDIR /test
COPY . /test

RUN pip3 install -r locust/requirements.txt 

ADD . /test/