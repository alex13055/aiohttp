from aiohttp import web
import aiohttp_jinja2

async def news(reguest):
    return web.Response(text = 'Hello, news!')

async def comments(reguest):
    return web.Response(text = 'Hello, comments!')

async def error_404(request):
    return web.Response(text = '404')
