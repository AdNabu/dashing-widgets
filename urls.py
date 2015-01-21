from django.conf.urls import url
from widgets import UserCards

urlpatterns = [
    url(r'^users', UserCards.as_view(), name='users_widget'),
]