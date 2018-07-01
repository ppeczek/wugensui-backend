from django.views.generic import ListView, TemplateView

from rest_framework import response, status, viewsets

from .models import Video
from .serializers import VideoSerializer


class HomeView(TemplateView):
    template_name = 'home.html'


class VideoListView(ListView):
    model = Video
    template_name = 'video-list.html'
    context_object_name = 'videos'
    paginate_by = 12
    queryset = Video.objects.all()


class VideoViewSet(viewsets.ModelViewSet):
    queryset = Video.objects.all()
    lookup_field = 'id'
    serializer_class = VideoSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.get_serializer().destroy(instance)
        print("Instance destroyed!")
        return response.Response(status=status.HTTP_204_NO_CONTENT)
