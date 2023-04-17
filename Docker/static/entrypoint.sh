#!/bin/bash

cd my_project && cd pyramid_scaffold \
    && python3 -m venv env \
    && env/bin/pip install --upgrade pip setuptools \
    && env/bin/pip install -e . \
    && env/bin/pserve development.ini http_port=6543 host=127.0.0.1 \
    && echo '[+] Success !'