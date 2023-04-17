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
    
@view_config(route_name='hello_posa')
def hello_posa(request):
    # Si l'utilisateur a déjà entré un pseudonyme, afficher un message de bienvenue personnalisé
    if 'pseudo' in request.params:
        template = Template("<p>mimi <code>%s</code></p>" % request.params['pseudo']) #Création de la template
        return Response(template.render())
        #return Response('Bonjour, {}!'.format(request.params['pseudo']))
    # Sinon, afficher un formulaire demandant à l'utilisateur d'entrer un pseudonyme
    else:
        return Response('Entrez votre pseudonyme : <form><input name="pseudo"></form>')
    



    from pyramid.view import view_config
from pyramid.response import Response
from mako.template import Template


@view_config(route_name='index', renderer='pyramid_scaffold:templates/index.mako')
def index(request):
    return {'project': 'Pyramid Scaffold'}

@view_config(route_name='myaccount', renderer='pyramid_scaffold:templates/my-account.mako')
def myaccount(request):
    return {'project': 'Pyramid Scaffold'}

#def myaccount(request):
    #if 'user_login' in request.params:
        #template = Template(filename="pyramid_scaffold/templates/my-account.mako" & request.params['user_login']) #Création de la template
        #return Response(template.render())
    #else: 
        #"return Response(template.render())

