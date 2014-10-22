Sub-Event Detection on Social Media
===================================

The aim the project was to detect the sub-event from the given twitter stream. The "sub event" of an vent is descibed as some important moment
in a given event for example if a soccer match is considered as an event then a goal or a red card to a player may be described as a sub event.

We propose and evaluate an approach that substantially shrinks the stream of tweets and consists of following two steps:

1. *Sub-event detection* - Determines if something relevant/ substantial has occurred.
2. *Sub-event summarization* - Summarizes a particular event to an understandable format.

Method Used
-----------

After removing the noise and shrinking the data, we have use some similarity measures like cosine similarity to cluster the similar tweets.
Tweets having similarity value greater than particular value are grouped together and considered as a part of same sub event. After the tweets
related to all sub events are separated, they are summarized using NLP toolkit. 

*Data:* US Presidential elections 2012

*Languages* Python

For more detailed understanding see [this](http://web.iiit.ac.in/~kshitij.kansal/13-15-Sub-event-Detection-on-Social-Media.html).

