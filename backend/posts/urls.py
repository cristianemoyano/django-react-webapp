from posts import views
from django.conf.urls import url

urlpatterns = [
	url(r'^api/v1/posts/$', views.posts_list, name='list_posts_api_v1'),
	url(r'^api/v1/posts/create/$', views.post_create, name='create_post_api_v1'),
    url(r'^api/v1/posts/(?P<pk>[0-9]+)$', views.post_detail, name='get_post_api_v1'),
]
