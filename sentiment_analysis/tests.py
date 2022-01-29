from django.test import TestCase
from django.urls import reverse, resolve
# Create your tests here.
from text_providers import api_providers


class BasicTestCase(TestCase):

    def test_smoke_model(self):

        test = api_providers.SmokeModel()
        self.assertTrue(test.equals_four()==4)

    def test_home_page_reachable(self):
        from metanewsmeta.views import HomeView
        url = reverse('home_page')
        self.assertEqual(url,'/')
        resolver = resolve('/')
        self.assertEqual(resolver.view_name, 'home_page')

    def test_twitter_provider(self):
        import text_providers
        provider = api_providers.TwitterProvider()
        test_tweets = provider.get_timeline_tweets_from_keyword(user_timeline_name='@cnn')
        self.assertTrue(len(test_tweets)>0)
