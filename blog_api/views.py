from rest_framework.generics import ListCreateAPIView, RetrieveDestroyAPIView
from blog.models import Post
from .serializers import PostSerializer


class PostList(ListCreateAPIView):
    queryset = Post.postobjects.all()
    serializer_class = PostSerializer


class PostDetail(RetrieveDestroyAPIView):
    queryset = Post.postobjects.all()
    serializer_class = PostSerializer
 