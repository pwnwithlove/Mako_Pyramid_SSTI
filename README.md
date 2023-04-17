Projet en cours de développement

# Mako  

Mako est un moteur de templates pour le langage de programmation *Python*. Mako est utilisé par *Reddit*. Il s'agit du langage de template inclus par défaut dans les frameworks Web Pylons et Pyramid. [Mako](https://www.makotemplates.org/) utilise [pyramid](http://www.pylonsproject.org/), à l'instar de jinja utilisé dans *django*.
Son principal atout est de pouvoir utiliser directement du python à l'aide des balises **<% %>** dans les templates.

Pour installer mako: 
```sh
pip install mako
```

[Exemple templates](https://docs.makotemplates.org/en/latest/syntax.html): 
```python
<%inherit file="base.html"/>
<%
    rows = [[v for v in range(0,10)] for row in range(0,10)]
%>
<table>
    % for row in rows:
        ${makerow(row)}
    % endfor
</table>

<%def name="makerow(row)">
    <tr>
    % for name in row:
        <td>${name}</td>\
    % endfor
    </tr>
</%def>
```

Exemple utilisation: 
```python
from mako.template import Template

mytemplate = Template("hello, ${name}!")
print(mytemplate.render(name="jack"))
```

# Docker

Pour lancer le docker: 
```sh
docker build -t mako .
docker run -it --rm mako
docker run --rm --net="host" mako
```

# Pyramid 

[Pyramid](https://trypyramid.com/) est un framework de développement web open source en *Python*. Il s'agit d'un framework minimaliste.

Pour setup pyramid en local: 
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
