from django.contrib.auth.models import User
import pytest
from django.urls import reverse

from posts.models import Post
from comments.models import Comment
from users.models import Profile


@pytest.mark.django_db
class BaseCommentsApiV1(object):
    """ Base Test module for comments API """

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
        self.comment = Comment.objects.create(
            comment='Comment',
            post=self.post,
            user=self.user,
        )
        self.list_comments_url = reverse('list_comments_api_v1')
        self.create_comment_url = reverse('create_comment_api_v1')
        self.get_comment_url = reverse('get_comment_api_v1', kwargs={'pk': self.comment.pk})
        self.get_comment_url_invalid = reverse('get_comment_api_v1', kwargs={'pk': self.comment.pk + 9999})
