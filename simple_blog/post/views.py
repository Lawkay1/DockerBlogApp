# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, BasePermission
from .models import BlogPost
from .serializers import BlogPostSerializer
from django.shortcuts import get_object_or_404

class BlogPostListCreateAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        queryset = BlogPost.objects.filter(author=request.user)
        serializer = BlogPostSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BlogPostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(author=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class IsOwnerOrReadOnly(BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """
    def has_object_permission(self, request, view, obj):
     
        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return True

        
        return obj.owner == request.user


class BlogPostRetrieveUpdateDestroyAPIView(APIView):
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def get_object(self, pk):
        return get_object_or_404(BlogPost, pk=pk)

    def get(self, request, pk):
        blogpost = self.get_object(pk)
        serializer = BlogPostSerializer(blogpost)
        return Response(serializer.data)

    def put(self, request, pk):
        blogpost = self.get_object(pk)
        serializer = BlogPostSerializer(blogpost, data=request.data)
        if blogpost.author != request.user:
            return Response({"error": "You do not have permission to update this post."}, status=status.HTTP_403_FORBIDDEN)         

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        blogpost = self.get_object(pk)
        if blogpost.author != request.user:
            return Response({"error": "You do not have permission to delete this post."}, status=status.HTTP_403_FORBIDDEN)      
        blogpost.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
