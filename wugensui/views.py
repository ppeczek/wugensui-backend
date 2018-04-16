from django.views.generic import TemplateView

from rest_framework import response, status
from rest_framework_mongoengine import viewsets

from .models import Video
from .serializers import VideoSerializer


class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['videos'] = Video.objects.all()
        return context


class VideoViewSet(viewsets.ModelViewSet):
    queryset = Video.objects.all()
    lookup_field = 'id'
    serializer_class = VideoSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.get_serializer().destroy(instance)
        print("Instance destroyed!")
        return response.Response(status=status.HTTP_204_NO_CONTENT)
