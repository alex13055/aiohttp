from views import news, comments
from aiohttp import web

def setup_routes(app):
    app.add_routes([web.get('/', news),
                    web.get('/news/{id}', comments)])

