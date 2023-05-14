FROM python:3.8

COPY ./static/ /home/webmaster/app

RUN chmod -R 777 /home/webmaster/app \
    && useradd -ms /bin/bash webmaster

USER webmaster

WORKDIR /home/webmaster/app

EXPOSE 6543

CMD  /bin/sh /home/webmaster/app/entrypoint.sh