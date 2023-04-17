from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response
from mako.template import Template

def hello_world(request):
    # Si l'utilisateur a déjà entré un pseudonyme, afficher un message de bienvenue personnalisé
    if 'pseudo' in request.params:
        template = Template(filename='pyramid.mako')
        return Response(template.render(pseudo=request.params['pseudo']))
        #return Response('Bonjour, {}!'.format(request.params['pseudo']))
    # Sinon, afficher un formulaire demandant à l'utilisateur d'entrer un pseudonyme
    else:
        return Response('Entrez votre pseudonyme : <form><input name="pseudo"></form>')

# Configurer l'application Pyramid
if __name__ == '__main__':
    config = Configurator()
    config.add_route('hello', '/')
    config.add_view(hello_world, route_name='hello')
    app = config.make_wsgi_app()

    # Lancer le serveur web
    server = make_server('0.0.0.0', 6543, app)
    server.serve_forever()

