from starlette.applications import Starlette
from starlette.responses import HTMLResponse
from starlette.routing import Route, Mount
from starlette.staticfiles import StaticFiles


async def homepage(request):
    """
    Homepage which uses server push to deliver the stylesheet.
    """
    await request.send_push_promise("/static/style.css")
    return HTMLResponse(
        '<html><head><link rel="stylesheet" href="/static/style.css"/></head></html>'
    )

routes = [
    Route("/", endpoint=homepage),
    Mount("/static", StaticFiles(directory="static"), name="static") ,
    Mount('/static', app=StaticFiles(directory='static', packages=['bootstrap4']), name="static"),
]

app = Starlette(routes=routes)