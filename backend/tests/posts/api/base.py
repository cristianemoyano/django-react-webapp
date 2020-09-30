from django.contrib.auth.models import User
import pytest
from django.urls import reverse

from posts.models import Post
from users.models import Profile


@pytest.mark.django_db
class BaseListPostsApiV1(object):
    """ Test module for GET all posts API """

    @pytest.fixture
    def setup_test(self, request):
        self.user = User.objects.create()
        self.profile = Profile.objects.create(
            website='http://127.0.0.1:8000',
            user=self.user,
        )
        self.post = Post.objects.create(
            title='Test',
            post='Lorem ipsum',
            user=self.user,
        )
        self.list_posts_url = reverse('list_posts_api_v1')
        self.create_post_url = reverse('create_post_api_v1')
        self.get_post_url = reverse('get_post_api_v1', kwargs={'pk': self.post.pk})
        self.get_post_url_invalid = reverse('get_post_api_v1', kwargs={'pk': self.post.pk + 9999})
