FROM alpine:latest

MAINTAINER Tim Davis "timd@vmware.com"

RUN apk update && \
    apk add python3 && \
    apk add python3-dev && \
    apk add py-pip && \
    python3 -m ensurepip && \
    rm -r /usr/lib/python*/ensurepip && \
    pip3 install --upgrade pip setuptools && \
    if [ ! -e /usr/bin/pip ]; then ln -s pip3 /usr/bin/pip ; fi && \
    if [[ ! -e /usr/bin/python ]]; then ln -sf /usr/bin/python3 /usr/bin/python; fi && \
#    pip install --upgrade pip \
#    pip3 install setuptools \
    apk add py-flask && \
    apk add py-redis && \
    apk add py-requests && \
    apk add redis && \
    rm -rf /var/cache/* \
    rm -rf /root/.cache/*

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip3 install -r requirements.txt

COPY . /app

EXPOSE 5000

ENTRYPOINT [ "python3" ]

CMD [ "currency-service.py" ]
