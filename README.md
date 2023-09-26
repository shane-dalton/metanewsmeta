# metanewsmeta
The end goal is to produce a time series collection data pipeline that serves as a
sentiment aggregation platform for news from twitter and displays the
positivity/negativity of a subset of news stations on a daily basis.


Current Progress:
- Integration and creation of twitter service provider abstraction for retrieving tweets
- Integration of Vader NLP sentiment analysis of tweets
- Initial Integration tests


Planned Progress:
- Integration of CI/CD through circle ci
- Deployment via ECS
- Sampled Twitter decahose/1% tweet stream analysis 
