FROM python:3.8

COPY ./static/ /app

WORKDIR /app

RUN chmod -R +x /app

EXPOSE 6543

CMD  /bin/sh /app/entrypoint.sh


