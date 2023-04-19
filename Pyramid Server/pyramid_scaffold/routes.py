def includeme(config):
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('index', '/')
    config.add_route('myaccount', '/my-account')
    config.add_route('test', '/test')
    config.add_route('invalidusername','/invalid-username')
