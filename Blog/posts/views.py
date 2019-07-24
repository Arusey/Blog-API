from django.shortcuts import get_object_or_404
from rest_framework import status, viewsets
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from .models import Posts
from .serializers import PostSerializer
from .renderers import PostJSONRenderer


def get_post(slug):
    try:
        post = Posts.objects.get(slug=slug)
        return post
    except Posts.DoesNotExist:
        raise NotFound(
            {"error": "Post not found"}
        )


class PostViewSet(viewsets.ViewSet):
    queryset = Posts.objects.all()
    serializer_class = PostSerializer
    renderer_classes = (PostJSONRenderer,)

    def list(self, request):
        queryset = Posts.objects.order_by("created_at")
        serializer = PostSerializer(
            queryset, many=True, context={'request': request})
        return Response({"Posts": serializer.data})

    def create(self, request):
        """create an post"""
        post = request.data
        serializer = self.serializer_class(
            data=post, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        """Returns posts with the given slug if exists"""
        queryset = Posts.objects.all()
        post = get_object_or_404(queryset, pk=pk)
        serializer = PostSerializer(post, context={'request': request})
        return Response(serializer.data)

    def update(self, request, pk=None):
        """update a post"""
        queryset = Posts.objects.all()
        post = get_object_or_404(queryset, pk=pk)
        post_data = request.data
        serializer = self.serializer_class(
            data=post_data, partial=False)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):
        queryset = Posts.objects.all()
        post = get_object_or_404(queryset, pk=pk)
        post_data = request.data
        serializer = self.serializer_class(
            instance=post, data=post_data, partial=True,
            context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        queryset = Posts.objects.all()
        post = get_object_or_404(queryset, pk=pk)
        post.delete()
        return Response({"message": "post deleted successfully"}, status=status.HTTP_200_OK)
