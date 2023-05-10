# Mako  

Mako est un moteur de templates pour le langage de programmation *Python*. Mako est utilisé par *Reddit*. Il s'agit du langage de template inclus par défaut dans les frameworks Web Pylons et Pyramid. [Pyramid](http://www.pylonsproject.org/) dans notre cas utilise [Mako](https://www.makotemplates.org/), à l'instar de jinja utilisé dans *django*.
Son principal atout est de pouvoir utiliser directement du python à l'aide des balises **<% %>** dans les templates.

Pour installer mako: 
```sh
pip install mako
```

# Pyramid 

[Pyramid](https://trypyramid.com/) est un framework de développement web open source en *Python*. Il s'agit d'un framework minimaliste.

Pour setup pyramid en local avec [cookiecutter](https://github.com/cookiecutter/cookiecutter)

```sh
apt-get install python3-venv

export VENV=~/env
python3 -m venv $VENV

$VENV/bin/pip install "pyramid==2.0.1"
$VENV/bin/pip install cookiecutter
$VENV/bin/cookiecutter gh:Pylons/pyramid-cookiecutter-starter --checkout 2.0-branch 
cd lenomchoisis
python3 -m venv env
env/bin/pip install --upgrade pip setuptools
env/bin/pip install -e .
env/bin/pserve development.ini --reload

```

Pour lancer l'environnement présent dans Pyramid Server: 

```sh
cd Pyramid Server
python3 -m venv env
env/bin/pip install --upgrade pip setuptools
env/bin/pip install -e .
env/bin/pserve development.ini --reload
```
