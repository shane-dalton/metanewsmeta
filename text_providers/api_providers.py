import tweepy as tw

from django.conf import settings

class SmokeModel(object):
    def equals_four(self):
        return 4

class TwitterProvider():

    def __init__(self):
        self.auth = tw.OAuthHandler(settings.TWITTER_CONSUMER_KEY, settings.TWITTER_CONSUMER_SECRET)
        self.auth.set_access_token(settings.TWITTER_ACCESS_TOKEN, settings.TWITTER_ACCESS_TOKEN_SECRET)
        self.api=tw.API(self.auth,wait_on_rate_limit=True)

    def get_timeline_tweets_from_keyword(self, user_timeline_name, num_tweets=200):
        timeline_tweets = self.api.user_timeline(screen_name=user_timeline_name, count=200, include_rts=False, tweet_mode='extended')
        results = [
            {
                'username':user_timeline_name,
                'tweet_text': tweet.full_text,
                'created_date':tweet.created_at
            }
            for tweet in timeline_tweets
        ]
        return results
