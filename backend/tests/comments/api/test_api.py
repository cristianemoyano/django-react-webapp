import json

from rest_framework import status

from comments.models import Comment
from comments.serializers import CommentSerializer
from tests.comments.api.base import BaseCommentsApiV1


class TestListCommentsApiV1(BaseCommentsApiV1):
    """ Test module for GET all comments API """

    def test_list_all_comments(self, api_client, setup_test):
        # get API response
        response = api_client.get(self.list_comments_url)
        # get data from db
        comments = Comment.objects.all()
        serializer = CommentSerializer(comments, many=True)
        assert response.data['data'] == serializer.data
        assert response.status_code == status.HTTP_200_OK

    def test_http_method_not_allowed(self, api_client, setup_test):
        response = api_client.post(self.list_comments_url)
        assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED


class TestCreateCommentApiV1(BaseCommentsApiV1):
    """ Test module to create comment API """

    def test_create_comment(self, setup_test, api_client_with_credentials):
        payload = {
            'comment': 'The Comment',
            'post': self.post.id,
        }
        response = api_client_with_credentials.post(
            self.create_comment_url,
            data=json.dumps(payload),
            content_type='application/json'
        )
        assert response.status_code == status.HTTP_201_CREATED

    def test_create_comment_invalid_payload(self, setup_test, api_client_with_credentials):
        invalid_payload = {
            'name': 'Muffin',
            'color': 'White'
        }
        response = api_client_with_credentials.post(
            self.create_comment_url,
            data=json.dumps(invalid_payload),
            content_type='application/json'
        )
        assert response.status_code == status.HTTP_400_BAD_REQUEST

    def test_http_method_not_allowed_with_credentials(self, setup_test, api_client_with_credentials):
        response = api_client_with_credentials.get(self.create_comment_url)
        assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED

    def test_http_method_not_allowed(self, setup_test, api_client):
        response = api_client.get(self.create_comment_url)
        assert response.status_code == status.HTTP_401_UNAUTHORIZED


class TestGetCommentDetailApiV1(BaseCommentsApiV1):
    """ Test module for GET post detail API """

    def test_get_comment_detail(self, api_client, setup_test):
        # get API response
        response = api_client.get(self.get_comment_url)
        # get data from db
        comments = Comment.objects.all()
        serializer = CommentSerializer(comments, many=True)
        assert response.data == serializer.data[0]
        assert response.status_code == status.HTTP_200_OK

    def test_http_method_not_allowed(self, api_client, setup_test):
        response = api_client.post(self.get_comment_url)
        assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED

    def test_invalid_id(self, api_client, setup_test):
        response = api_client.get(self.get_comment_url_invalid)
        assert response.status_code == status.HTTP_404_NOT_FOUND
