from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [
    path("",views.home,name="aiesec-home"),
    path("login",views.login,name="aiesec-login"),
    path("submit",views.submit,name="aiesec-submit")
]

urlpatterns+=staticfiles_urlpatterns()