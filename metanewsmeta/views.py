from django.views.generic import TemplateView
from text_providers.api_providers import TwitterProvider

class HomeView(TemplateView):
    template_name = 'general/welcome.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        a = 5
        b = 12
        c = 45
        d = 12
        provider = TwitterProvider()
        context['Twitter_info'] = provider.get_timeline_tweets_from_keyword(user_timeline_name='@cnn', num_tweets=200)
        return context