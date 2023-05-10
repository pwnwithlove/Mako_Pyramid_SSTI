#!/bin/bash

cd my_project/Pyramid_Server \
    && python3 -m venv env \
    && env/bin/pip install --upgrade pip setuptools \
    && env/bin/pip install -e . \
    && env/bin/pserve development.ini \
    && echo '[+] Success !'