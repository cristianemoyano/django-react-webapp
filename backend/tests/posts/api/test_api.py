import json

from rest_framework import status

from posts.models import Post
from posts.serializers import PostSerializer
from tests.posts.api.base import BaseListPostsApiV1


class TestListPostsApiV1(BaseListPostsApiV1):
    """ Test module for GET all posts API """

    def test_list_all_posts(self, api_client, setup_test):
        # get API response
        response = api_client.get(self.list_posts_url)
        # get data from db
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        assert response.data['data'] == serializer.data
        assert response.status_code == status.HTTP_200_OK

    def test_http_method_not_allowed(self, api_client, setup_test):
        response = api_client.post(self.list_posts_url)
        assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED


class TestCreatePostApiV1(BaseListPostsApiV1):
    """ Test module to create post API """

    def test_create_post(self, setup_test, api_client_with_credentials):
        payload = {
            'title': 'The Test',
            'post': 'Lorem ipsum.',
        }
        response = api_client_with_credentials.post(
            self.create_post_url,
            data=json.dumps(payload),
            content_type='application/json'
        )
        assert response.status_code == status.HTTP_201_CREATED

    def test_create_post_invalid_payload(self, setup_test, api_client_with_credentials):
        invalid_payload = {
            'name': 'Muffin',
            'color': 'White'
        }
        response = api_client_with_credentials.post(
            self.create_post_url,
            data=json.dumps(invalid_payload),
            content_type='application/json'
        )
        assert response.status_code == status.HTTP_400_BAD_REQUEST

    def test_http_method_not_allowed_with_credentials(self, setup_test, api_client_with_credentials):
        response = api_client_with_credentials.get(self.create_post_url)
        assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED

    def test_http_method_not_allowed(self, setup_test, api_client):
        response = api_client.get(self.create_post_url)
        assert response.status_code == status.HTTP_401_UNAUTHORIZED


class TestGetPostDetailApiV1(BaseListPostsApiV1):
    """ Test module for GET post detail API """

    def test_get_post_detail(self, api_client, setup_test):
        # get API response
        response = api_client.get(self.get_post_url)
        # get data from db
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        assert response.data == serializer.data[0]
        assert response.status_code == status.HTTP_200_OK

    def test_http_method_not_allowed(self, api_client, setup_test):
        response = api_client.post(self.get_post_url)
        assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED

    def test_invalid_id(self, api_client, setup_test):
        response = api_client.get(self.get_post_url_invalid)
        assert response.status_code == status.HTTP_404_NOT_FOUND
