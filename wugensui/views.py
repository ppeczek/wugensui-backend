from django.views.generic import TemplateView

from .models import Video


class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['videos'] = Video.objects.all()
        return context
