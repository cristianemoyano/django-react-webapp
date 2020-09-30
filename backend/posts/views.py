from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.urls import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from posts.models import Post
from posts.serializers import PostSerializer
from users.serializers import UserSerializer


@api_view(['GET'])
def posts_list(request):
    """
    List  posts.
    """
    if request.method == 'GET':
        data = []
        nextPage = 1
        previousPage = 1
        customers = Post.objects.all()
        page = request.GET.get('page', 1)
        paginator = Paginator(customers, 10)
        try:
            data = paginator.page(page)
        except PageNotAnInteger:
            data = paginator.page(1)
        except EmptyPage:
            data = paginator.page(paginator.num_pages)

        serializer = PostSerializer(data, context={'request': request}, many=True)
        if data.has_next():
            nextPage = data.next_page_number()
        if data.has_previous():
            previousPage = data.previous_page_number()

        url = reverse('list_posts_api_v1')
        return Response({
            'data': serializer.data,
            'count': paginator.count,
            'numpages': paginator.num_pages,
            'nextlink': url + '?page=' + str(nextPage),
            'prevlink': url + '?page=' + str(previousPage)
        })


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def post_create(request):
    """
        Create a new post.
    """
    if request.method == 'POST':
        request_data = request.data
        request_data.update({
            'user': request.user.id,
        })

        serializer = PostSerializer(data=request_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def post_detail(request, pk):
    """
        Retrieve a POST by id.
    """
    try:
        post = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PostSerializer(post, context={'request': request})
        return Response(serializer.data)
