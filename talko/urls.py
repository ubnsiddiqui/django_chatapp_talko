from django.conf.urls import url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from talko import views

# SET THE NAMESPACE!
app_name = 'talko'

# Be careful setting the name to just /login use userlogin instead!
urlpatterns = [
    url(r'^register/$', views.register, name='register'),
    url(r'^user_login/$', views.user_login, name='user_login'),
    url(r'^chat_view/$', views.chat_view1, name='chat_view'),
    url(r'^chat_view/(?P<receiver>\d+)/$', views.chat_view2, name='view_chat'),
    url(r'^create_message/$', views.create_msg, name='create_msg'),
    url(r'^get_messages/(?P<reciever>\d+)/$', views.display_msg, name='display_msg'),
    url(r'^index/$', views.index, name='index'),
]
