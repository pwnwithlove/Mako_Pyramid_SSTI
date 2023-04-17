FROM debian:11

# Install dependencies
RUN apt -y -qq update \
    && apt install -y -qq apt-transport-https python3-pip git python3-venv

# Install mako and pyramid
RUN python3 -m pip install --upgrade pip \
    && pip install mako \
    && apt clean -y \
    && export VENV=~/env \
    && python3 -m venv $VENV \
    && $VENV/bin/pip install "pyramid==2.0.1" \
    && $VENV/bin/pip install cookiecutter \
    && $VENV/bin/cookiecutter gh:Pylons/pyramid-cookiecutter-starter --checkout 2.0-branch --no-input --output-dir my_project

# Copy static files
COPY ./static/ /

RUN chmod +x /entrypoint.sh

EXPOSE 6543

CMD ./entrypoint.sh
