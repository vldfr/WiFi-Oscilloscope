# sensor/routing.py
from channels.sessions import SessionMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.conf.urls import url
from channels.auth import AuthMiddlewareStack
from channels.security.websocket import AllowedHostsOriginValidator, OriginValidator

from sensor.consumers import SensorConsumer

application = ProtocolTypeRouter({
    'websocket': AllowedHostsOriginValidator(
        AuthMiddlewareStack(
            SessionMiddlewareStack(
                URLRouter(
                    [
                        url(r"^sensor/(?P<sensor>[\w.@+-]+)/$", SensorConsumer)
                    ]
                )
            )
        )
    )
    # (http->django views is added by default)
})
