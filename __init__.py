from fastapi import APIRouter

from lnbits.db import Database
from lnbits.helpers import template_renderer

db = Database("ext_deezy")

deezy_ext: APIRouter = APIRouter(prefix="/deezy", tags=["deezy"])

deezy_static_files = [
    {
        "path": "/deezy/static",
        "name": "deezy_static",
    }
]


def deezy_renderer():
    return template_renderer(["deezy/templates"])


from .views import *  # noqa: F401,F403
from .views_api import *  # noqa: F401,F403
