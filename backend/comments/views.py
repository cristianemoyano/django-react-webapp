from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.urls import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from comments.models import Comment
from comments.serializers import CommentSerializer


@api_view(['GET'])
def comments_list(request):
    """
    List  comments.
    """
    if request.method == 'GET':
        data = []
        nextPage = 1
        previousPage = 1
        customers = Comment.objects.all()
        page = request.GET.get('page', 1)
        paginator = Paginator(customers, 10)
        try:
            data = paginator.page(page)
        except PageNotAnInteger:
            data = paginator.page(1)
        except EmptyPage:
            data = paginator.page(paginator.num_pages)

        serializer = CommentSerializer(data, context={'request': request}, many=True)
        if data.has_next():
            nextPage = data.next_page_number()
        if data.has_previous():
            previousPage = data.previous_page_number()

        url = reverse('list_comments_api_v1')
        return Response({
            'data': serializer.data,
            'count': paginator.count,
            'numpages': paginator.num_pages,
            'nextlink': url + '?page=' + str(nextPage),
            'prevlink': url + '?page=' + str(previousPage)
        })


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def comment_create(request):
    """
        Create a new comment.
    """
    if request.method == 'POST':
        request_data = request.data
        request_data.update({
            'user': request.user.id,
        })

        serializer = CommentSerializer(data=request_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def comment_detail(request, pk):
    """
        Retrieve a comment by id.
    """
    try:
        comment = Comment.objects.get(pk=pk)
    except Comment.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CommentSerializer(comment, context={'request': request})
        return Response(serializer.data)
