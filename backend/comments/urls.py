from comments import views
from django.conf.urls import url

urlpatterns = [
    url(r'^api/v1/comments/$', views.comments_list, name='list_comments_api_v1'),
    url(r'^api/v1/comments/create/$', views.comment_create, name='create_comment_api_v1'),
    url(r'^api/v1/comments/(?P<pk>[0-9]+)$', views.comment_detail, name='get_comment_api_v1'),
]
