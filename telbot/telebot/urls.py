from django.conf import settings, urls.url
from . import views

urlpatterns = [
    url(r'^/$', views.telegram_bot),
]
