from django.test import TestCase
from django.urls import reverse, resolve
# Create your tests here.
from text_providers import api_providers
import pytest
from django.conf import settings

@pytest.mark.django_db
def test_smoke_model():
    test = api_providers.SmokeModel()
    assert(test.equals_four()==4)

def test_home_page_reachable(client):
    url = reverse('home_page')
    response = client.get(url)
    assert response.status_code == 200


# def test_twitter_provider():
#     provider = api_providers.TwitterProvider()
#     test_tweets = provider.get_timeline_tweets_from_keyword(user_timeline_name='@cnn')
#     assert(len(test_tweets)>0)
