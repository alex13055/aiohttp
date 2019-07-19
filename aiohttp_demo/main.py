from aiohttp import web
#from settings import config
from routes import setup_routes
from middlewares import error_middleware

app = web.Application(middlewares=[error_middleware])
setup_routes(app)
#app['config'] = config
web.run_app(app, host='localhost', port=8084)
