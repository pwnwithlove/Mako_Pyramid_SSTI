from pyramid.view import view_config
from pyramid.response import Response
from mako.template import Template


@view_config(route_name='index', renderer='pyramid_scaffold:templates/index.mako')
def index(request):
    return {'project': 'Pyramid Scaffold'}

@view_config(route_name='myaccount', renderer='pyramid_scaffold:templates/my-account.mako')
def myaccount(request):
    if 'user_login' in request.params:
        path_to_html_file_account = "pyramid_scaffold/templates/my-account.mako"
        html_file_account = open(path_to_html_file_account,"r").read()
        data = html_file_account.replace("{{user_login}}",request.params['user_login'])
        template = Template(data) 
        return Response(template.render())
    else:
        template = Template(filename="pyramid_scaffold/templates/my-account.mako")
        return Response(template.render())

@view_config(route_name='invalidusername', renderer='pyramid_scaffold:templates/invalid-username.mako')
def invalidusername(request):
    return {'project': 'Pyramid Scaffold'}


#def myaccount(request):
    #if 'user_login' in request.params:
        #template = Template(filename="pyramid_scaffold/templates/my-account.mako" & request.params['user_login']) #Création de la template
        #return Response(template.render())
    #else: 
        #"return Response(template.render())
