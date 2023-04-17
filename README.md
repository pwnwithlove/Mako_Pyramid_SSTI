Projet en cours de développement

# Mako  

Mako est un moteur de templates pour le langage de programmation *Python*. Mako est utilisé par *Reddit*. Il s'agit du langage de template inclus par défaut dans les frameworks Web Pylons et Pyramid. [Pyramid](http://www.pylonsproject.org/) dans notre cas utilise [Mako](https://www.makotemplates.org/), à l'instar de jinja utilisé dans *django*.
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

Pour lancer l'environnement présent dans Pyramid Server: 

```sh
cd Pyramid Server
python3 -m venv env
env/bin/pip install --upgrade pip setuptools
env/bin/pip install -e .
env/bin/pserve development.ini --reload
```


Pour ajouter un nouveau projet, il faut add dans le path `/myproject/myproject/views/default.py`:

```python
from pyramid.view import view_config
from pyramid.response import Response
from mako.template import Template

@view_config(route_name='hello')
def hello_world(request):
    # Si l'utilisateur a déjà entré un pseudonyme, afficher un message de bienvenue personnalisé
    if 'pseudo' in request.params:
        template = Template("<p>mimi <code>%s</code></p>" % request.params['pseudo']) #Création de la template
        return Response(template.render())
        #return Response('Bonjour, {}!'.format(request.params['pseudo']))
    # Sinon, afficher un formulaire demandant à l'utilisateur d'entrer un pseudonyme
    else:
        return Response('Entrez votre pseudonyme : <form><input name="pseudo"></form>')
```

Pour ajouter une page html externe: 
```python
from pyramid.view import view_config

@view_config(route_name='index', renderer='pyramid_scaffold:templates/index.mako')

def index(request):

return {'project': 'Pyramid Scaffold'}

  
@view_config(route_name='myaccount',
renderer='pyramid_scaffold:templates/my-account.mako')

def myaccount(request):

return {'project': 'Pyramid Scaffold'}
```

Et add dans /myproject/myproject/routes.py:

```python
from pyramid.config import Configurator

def includeme(config):
    config.add_route('hello', '/')
    config.add_route('index', '/')
	config.add_route('myaccount', '/my-account')

```

Puis lancer le serv !:
```sh
$VENV/bin/pserve development.ini --reload
```


# Docker

Pour lancer le docker: 
```sh
docker build -t mako .
docker run -it --rm mako
docker run --rm --net="host" mako
```

Stopper tout les dockers: 
```
docker stop $(docker ps -a -q)
```

Kill les dockers: 
```sh
docker rmi -f $(docker images -aq)
```
