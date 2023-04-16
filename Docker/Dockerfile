FROM debian:11
RUN apt update \
&& apt install -y apt-transport-https \
&& apt install -y python3-pip \
&& apt install -y git \
&& python3 -m pip install --upgrade pip \
&& pip install mako \
&& apt clean -y \
&& apt-get install python3-venv -y \
&& export VENV=~/env \
&& python3 -m venv $VENV \
&& $VENV/bin/pip install "pyramid==2.0.1" \
&& $VENV/bin/pip install cookiecutter \
&& $VENV/bin/cookiecutter gh:Pylons/pyramid-cookiecutter-starter --checkout 2.0-branch --no-input --output-dir my_project

EXPOSE 6543 

CMD cd my_project && cd pyramid_scaffold \
&& python3 -m venv env \
&& env/bin/pip install --upgrade pip setuptools \
&& env/bin/pip install -e . \
&& env/bin/pserve development.ini http_port=6543 host=127.0.0.1 \
&& echo '[+] Success !'
