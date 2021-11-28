from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'general/welcome.html'

    def get_context_data(self, **kwargs):
        a = 5
        b = 12

        return a+b