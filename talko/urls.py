from django.conf.urls import url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from talko import views

# SET THE NAMESPACE!
app_name = 'talko'

# Be careful setting the name to just /login use userlogin instead!
urlpatterns=[
    url(r'^register/$', views.register, name='register'),
    url(r'^user_login/$', views.user_login, name='user_login'),
    url(r'^chat_view/$', views.chat_view, name='chat_view'),
]

urlpatterns += staticfiles_urlpatterns()

