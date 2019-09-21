from django.urls import path

from ......views.api.charts.pie import views


urlpatterns = [
    path(
        'list/requests/b5365a061939e26d935afd01cd29086c0328eb206c7547603202fc31ef005f5bcd76a53862316a3d28085a052e3395d43fb62e0d5893c430a3b4af14590cd168/',
        views.RequestsListApiView.as_view()
    ),
]
