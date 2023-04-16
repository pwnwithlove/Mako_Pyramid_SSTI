from pyramid.view import view_config


@view_config(route_name='home', renderer='miaou_test:templates/mytemplate.mako')
def my_view(request):
    return {'project': 'miaou_test'}
