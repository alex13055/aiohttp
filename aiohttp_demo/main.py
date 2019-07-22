from aiohttp import web
from routes import setup_routes
from middlewares import error_middleware

app = web.Application(middlewares=[error_middleware])
setup_routes(app)
web.run_app(app, host='localhost', port=8084)
