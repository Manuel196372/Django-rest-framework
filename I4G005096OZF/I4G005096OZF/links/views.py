from django.shortcuts import render

# Create your views here.
class PostListApi(viewsets.modelViewSet) :
    queryset = Links.objects.filter(active=True)
    serializer_class = LinkSerializer

class PostCreateApi(viewsets.modelViewSet) :
    queryset = Links.objects.filter(active=True)
    serializer_class = LinkSerializer

class PostDetailApi(viewsets.modelViewSet) :
    queryset = Links.objects.filter(active=True)
    serializer_class = LinkSerializer

class PostUpdateApi(viewsets.modelViewSet) :
    queryset = Links.objects.filter(active=True)
    serializer_class = LinkSerializer