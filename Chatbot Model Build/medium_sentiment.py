import nltk
from nltk.corpus import twitter_samples
from nltk.tokenize import TweetTokenizer
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
import re

nltk.download('twitter_samples')

tokenizer = TweetTokenizer(preserve_case=False, strip_handles=True, reduce_len=True)

stop_words = stopwords.words('english')
stemmer = PorterStemmer()

def clean_tweet(tweet):
    tweet = re.sub(r'\$\w*', '', tweet)  # Remove tickers
    tweet = re.sub(r'https?:\/\/.*[\r\n]*', '', tweet)  # Remove hyperlinks
    tweet = re.sub(r'#', '', tweet)  # Remove hashtags
    tweet_tokens = tokenizer.tokenize(tweet)
    tweets_clean = []
    for word in tweet_tokens:
        if (word not in stop_words and word.isalpha()):
            stem_word = stemmer.stem(word)
            tweets_clean.append(stem_word)
    return tweets_clean

def get_word_frequency(words):
    word_frequency = {}
    for word in words:
        if word in word_frequency:
            word_frequency[word] += 1
        else:
            word_frequency[word] = 1
    return word_frequency

positive_tweets = twitter_samples.strings('positive_tweets.json')
negative_tweets = twitter_samples.strings('negative_tweets.json')

positive_stemmed_tokens = [clean_tweet(tweet) for tweet in positive_tweets]
negative_stemmed_tokens = [clean_tweet(tweet) for tweet in negative_tweets]

positive_features = [(get_word_frequency(tokens), 'Positive') for tokens in positive_stemmed_tokens]
negative_features = [(get_word_frequency(tokens), 'Negative') for tokens in negative_stemmed_tokens]
all_features = positive_features + negative_features

import random

random.shuffle(all_features)

train_set = all_features[:int(len(all_features)*0.8)]
test_set = all_features[int(len(all_features)*0.8):]

from nltk.classify import NaiveBayesClassifier

classifier = NaiveBayesClassifier.train(train_set)

def get_accuracy(test_set, classifier):
    correct = 0
    for (features, label) in test_set:
        prediction = classifier.classify(features)
        if prediction == label:
            correct += 1
    accuracy = float(correct) / len(test_set)
    return accuracy

accuracy = get_accuracy(test_set, classifier)
print('Accuracy:', accuracy)

def predict_sentiment(tweet):
    cleaned_tweet = clean_tweet(tweet)
    features = get_word_frequency(cleaned_tweet)
    return classifier.classify(features)

positive_tests = [
    "I loved the new features in the latest update. Great job!",
    "The customer support was fantastic. I'm very impressed!",
    "What a wonderful experience shopping with this brand!",
    "The team did a great job with their attention to detail.",
    "The new collection is absolutely beautiful and trendy!",
    "Fantastic quality and super quick delivery!",
    "This store always exceeds my expectations!",
    "The customer service is exceptional and very helpful!",
    "I'm very pleased with my purchase, would buy again.",
    "The packaging is so cute and eco-friendly.",
    "The product design is stunning, and the material is high-quality.",
    "Super impressed by how fast I got my order!",
    "The whole experience was just excellent.",
    "Can't wait to recommend this brand to my friends!",
    "Amazing customer support and the staff were polite.",
    "The store had exactly what I needed.",
    "Great deals and an overall wonderful shopping experience.",
    "Easy-to-use website and amazing prices.",
    "The product quality was far beyond my expectations!",
    "This new line is stunning; can't wait to buy more.",
    "Shopping here was an absolute delight.",
    "They go above and beyond for their customers.",
    "I'm thrilled with the fast and helpful service.",
    "The design was creative and quite innovative.",
    "Great deals on all my favorite items!",
    "The items arrived in perfect condition.",
    "Such a reliable company; never lets me down.",
    "Absolutely in love with this product!",
    "A seamless buying process and super friendly staff.",
    "The product quality was even better than advertised.",
    "Every time I shop here, I'm never disappointed.",
    "Just received my order and everything is perfect!",
    "The features exceeded my expectations.",
    "Very happy with the quality and prices!",
    "Their customer service team is incredible.",
    "Perfect for my needs, and the delivery was fast.",
    "Their products are always dependable.",
    "This company deserves all the praise.",
    "Can't imagine a better shopping experience.",
    "Love how user-friendly their website is.",
    "The shipping was quicker than expected.",
    "Their loyalty program offers fantastic deals.",
    "Always my go-to store for quality items.",
    "Their customer care team is super responsive.",
    "A very satisfying shopping experience overall.",
    "Very innovative designs at reasonable prices.",
    "I always trust this store with my purchases.",
    "Such a refreshing approach to customer support.",
    "Unbelievably good prices on amazing products.",
    "My order was processed and delivered quickly.",
    "Top-notch quality and a fair price."
]

# Negative tweets
negative_tests = [
    "I'm very disappointed with the quality of the product.",
    "Terrible service and long wait times. I won't return.",
    "The product didn't match the description at all!",
    "Customer support was slow and unhelpful.",
    "The quality of the fabric was poor and uncomfortable.",
    "The website was difficult to navigate and confusing.",
    "The store staff were rude and unprofessional.",
    "The product broke after just one use.",
    "The color of the item was completely off.",
    "Shipping took much longer than expected.",
    "My package arrived damaged and unusable.",
    "The product design is flawed and impractical.",
    "Can't believe the terrible quality for this price.",
    "Customer service never responded to my concerns.",
    "The app kept crashing whenever I tried to check out.",
    "Their refund policy is too strict and unfair.",
    "This company doesn't care about its customers.",
    "The packaging was cheap and flimsy.",
    "I got charged for something I never ordered.",
    "My order got lost, and they refused to help.",
    "The whole buying process was a total mess.",
    "The product is nothing like the advertisement.",
    "I'm utterly frustrated with this brand.",
    "The staff were dismissive and unhelpful.",
    "The product was missing key features.",
    "Can't believe I wasted money on this.",
    "There's no consistency in the quality.",
    "They never replied to my support tickets.",
    "I'm so dissatisfied with my purchase.",
    "They completely ignored my complaint.",
    "This was the worst shopping experience ever.",
    "Every time I call, I'm put on hold for hours.",
    "I got the wrong item and they won't fix it.",
    "The return policy is overly complicated.",
    "I feel cheated by their deceptive marketing.",
    "The reviews made it sound much better than it is.",
    "I received an expired product. Unacceptable.",
    "I won't buy from this store again. Horrible.",
    "The checkout process kept glitching.",
    "They sent me an entirely different item.",
    "The sizing was inaccurate and misleading.",
    "The product looks cheap and poorly made.",
    "It was a mistake trusting this company.",
    "The website lacks basic functionality.",
    "The material quality is simply subpar.",
    "This is the last time I'm shopping here.",
    "Terrible policies that hurt customers.",
    "Nothing about this experience was positive.",
    "The entire system seems broken and flawed.",
    "Their marketing is completely misleading.",
    "I hate this product."
]

i = 0
tweet_test = positive_tests[i]
print(str(i) + ". " + tweet_test + "\t\t" + predict_sentiment(tweet_test)) # Should be Positive

tweet_test = negative_tests[i]
print(str(i) + ". " + tweet_test + "\t\t" + predict_sentiment(tweet_test)) # Should be Negative

i+=1
tweet_test = positive_tests[i]
print(str(i) + ". " + tweet_test + "\t\t" + predict_sentiment(tweet_test)) # Should be Positive

tweet_test = negative_tests[i]
print(str(i) + ". " + tweet_test + "\t\t" + predict_sentiment(tweet_test)) # Should be Negative

i+=1
tweet_test = positive_tests[i]
print(str(i) + ". " + tweet_test + "\t\t" + predict_sentiment(tweet_test)) # Should be Positive

tweet_test = negative_tests[i]
print(str(i) + ". " + tweet_test + "\t\t" + predict_sentiment(tweet_test)) # Should be Negative

i+=1
tweet_test = positive_tests[i]
print(str(i) + ". " + tweet_test + "\t\t" + predict_sentiment(tweet_test)) # Should be Positive

tweet_test = negative_tests[i]
print(str(i) + ". " + tweet_test + "\t\t" + predict_sentiment(tweet_test)) # Should be Negative

i+=1
tweet_test = positive_tests[i]
print(str(i) + ". " + tweet_test + "\t\t" + predict_sentiment(tweet_test)) # Should be Positive

tweet_test = negative_tests[i]
print(str(i) + ". " + tweet_test + "\t\t" + predict_sentiment(tweet_test)) # Should be Negative

i+=1
tweet_test = positive_tests[i]
print(str(i) + ". " + tweet_test + "\t\t" + predict_sentiment(tweet_test)) # Should be Positive

tweet_test = negative_tests[i]
print(str(i) + ". " + tweet_test + "\t\t" + predict_sentiment(tweet_test)) # Should be Negative

i+=1
tweet_test = positive_tests[i]
print(str(i) + ". " + tweet_test + "\t\t" + predict_sentiment(tweet_test)) # Should be Positive

tweet_test = negative_tests[i]
print(str(i) + ". " + tweet_test + "\t\t" + predict_sentiment(tweet_test)) # Should be Negative

i+=1
tweet_test = positive_tests[i]
print(str(i) + ". " + tweet_test + "\t\t" + predict_sentiment(tweet_test)) # Should be Positive

tweet_test = negative_tests[i]
print(str(i) + ". " + tweet_test + "\t\t" + predict_sentiment(tweet_test)) # Should be Negative

i+=1
tweet_test = positive_tests[i]
print(str(i) + ". " + tweet_test + "\t\t" + predict_sentiment(tweet_test)) # Should be Positive

tweet_test = negative_tests[i]
print(str(i) + ". " + tweet_test + "\t\t" + predict_sentiment(tweet_test)) # Should be Negative

i+=1
tweet_test = positive_tests[i]
print(str(i) + ". " + tweet_test + "\t\t" + predict_sentiment(tweet_test)) # Should be Positive

tweet_test = negative_tests[i]
print(str(i) + ". " + tweet_test + "\t\t" + predict_sentiment(tweet_test)) # Should be Negative

i+=1
tweet_test = positive_tests[i]
print(str(i) + ". " + tweet_test + "\t\t" + predict_sentiment(tweet_test)) # Should be Positive

tweet_test = negative_tests[i]
print(str(i) + ". " + tweet_test + "\t\t" + predict_sentiment(tweet_test)) # Should be Negative

i+=1
tweet_test = positive_tests[i]
print(str(i) + ". " + tweet_test + "\t\t" + predict_sentiment(tweet_test)) # Should be Positive

tweet_test = negative_tests[i]
print(str(i) + ". " + tweet_test + "\t\t" + predict_sentiment(tweet_test)) # Should be Negative

i+=1
tweet_test = positive_tests[i]
print(str(i) + ". " + tweet_test + "\t\t" + predict_sentiment(tweet_test)) # Should be Positive

tweet_test = negative_tests[i]
print(str(i) + ". " + tweet_test + "\t\t" + predict_sentiment(tweet_test)) # Should be Negative

i+=1
tweet_test = positive_tests[i]
print(str(i) + ". " + tweet_test + "\t\t" + predict_sentiment(tweet_test)) # Should be Positive

tweet_test = negative_tests[i]
print(str(i) + ". " + tweet_test + "\t\t" + predict_sentiment(tweet_test)) # Should be Negative

i+=1
tweet_test = positive_tests[i]
print(str(i) + ". " + tweet_test + "\t\t" + predict_sentiment(tweet_test)) # Should be Positive

tweet_test = negative_tests[i]
print(str(i) + ". " + tweet_test + "\t\t" + predict_sentiment(tweet_test)) # Should be Negative

i+=1
tweet_test = positive_tests[i]
print(str(i) + ". " + tweet_test + "\t\t" + predict_sentiment(tweet_test)) # Should be Positive

tweet_test = negative_tests[i]
print(str(i) + ". " + tweet_test + "\t\t" + predict_sentiment(tweet_test)) # Should be Negative

i+=1
tweet_test = positive_tests[i]
print(str(i) + ". " + tweet_test + "\t\t" + predict_sentiment(tweet_test)) # Should be Positive

tweet_test = negative_tests[i]
print(str(i) + ". " + tweet_test + "\t\t" + predict_sentiment(tweet_test)) # Should be Negative

i+=1
tweet_test = positive_tests[i]
print(str(i) + ". " + tweet_test + "\t\t" + predict_sentiment(tweet_test)) # Should be Positive

tweet_test = negative_tests[i]
print(str(i) + ". " + tweet_test + "\t\t" + predict_sentiment(tweet_test)) # Should be Negative

i+=1
tweet_test = positive_tests[i]
print(str(i) + ". " + tweet_test + "\t\t" + predict_sentiment(tweet_test)) # Should be Positive

tweet_test = negative_tests[i]
print(str(i) + ". " + tweet_test + "\t\t" + predict_sentiment(tweet_test)) # Should be Negative

i+=1
tweet_test = positive_tests[i]
print(str(i) + ". " + tweet_test + "\t\t" + predict_sentiment(tweet_test)) # Should be Positive

tweet_test = negative_tests[i]
print(str(i) + ". " + tweet_test + "\t\t" + predict_sentiment(tweet_test)) # Should be Negative

i+=1
tweet_test = positive_tests[i]
print(str(i) + ". " + tweet_test + "\t\t" + predict_sentiment(tweet_test)) # Should be Positive

tweet_test = negative_tests[i]
print(str(i) + ". " + tweet_test + "\t\t" + predict_sentiment(tweet_test)) # Should be Negative

i+=1
tweet_test = positive_tests[i]
print(str(i) + ". " + tweet_test + "\t\t" + predict_sentiment(tweet_test)) # Should be Positive

tweet_test = negative_tests[i]
print(str(i) + ". " + tweet_test + "\t\t" + predict_sentiment(tweet_test)) # Should be Negative

i+=1
tweet_test = positive_tests[i]
print(str(i) + ". " + tweet_test + "\t\t" + predict_sentiment(tweet_test)) # Should be Positive

tweet_test = negative_tests[i]
print(str(i) + ". " + tweet_test + "\t\t" + predict_sentiment(tweet_test)) # Should be Negative

i+=1
tweet_test = positive_tests[i]
print(str(i) + ". " + tweet_test + "\t\t" + predict_sentiment(tweet_test)) # Should be Positive

tweet_test = negative_tests[i]
print(str(i) + ". " + tweet_test + "\t\t" + predict_sentiment(tweet_test)) # Should be Negative

i+=1
tweet_test = positive_tests[i]
print(str(i) + ". " + tweet_test + "\t\t" + predict_sentiment(tweet_test)) # Should be Positive

tweet_test = negative_tests[i]
print(str(i) + ". " + tweet_test + "\t\t" + predict_sentiment(tweet_test)) # Should be Negative

i+=1
tweet_test = positive_tests[i]
print(str(i) + ". " + tweet_test + "\t\t" + predict_sentiment(tweet_test)) # Should be Positive

tweet_test = negative_tests[i]
print(str(i) + ". " + tweet_test + "\t\t" + predict_sentiment(tweet_test)) # Should be Negative

i+=1
tweet_test = positive_tests[i]
print(str(i) + ". " + tweet_test + "\t\t" + predict_sentiment(tweet_test)) # Should be Positive

tweet_test = negative_tests[i]
print(str(i) + ". " + tweet_test + "\t\t" + predict_sentiment(tweet_test)) # Should be Negative

i+=1
tweet_test = positive_tests[i]
print(str(i) + ". " + tweet_test + "\t\t" + predict_sentiment(tweet_test)) # Should be Positive

tweet_test = negative_tests[i]
print(str(i) + ". " + tweet_test + "\t\t" + predict_sentiment(tweet_test)) # Should be Negative

i+=1
tweet_test = positive_tests[i]
print(str(i) + ". " + tweet_test + "\t\t" + predict_sentiment(tweet_test)) # Should be Positive

tweet_test = negative_tests[i]
print(str(i) + ". " + tweet_test + "\t\t" + predict_sentiment(tweet_test)) # Should be Negative

i+=1
tweet_test = positive_tests[i]
print(str(i) + ". " + tweet_test + "\t\t" + predict_sentiment(tweet_test)) # Should be Positive

tweet_test = negative_tests[i]
print(str(i) + ". " + tweet_test + "\t\t" + predict_sentiment(tweet_test)) # Should be Negative

i+=1
tweet_test = positive_tests[i]
print(str(i) + ". " + tweet_test + "\t\t" + predict_sentiment(tweet_test)) # Should be Positive

tweet_test = negative_tests[i]
print(str(i) + ". " + tweet_test + "\t\t" + predict_sentiment(tweet_test)) # Should be Negative

i+=1
tweet_test = positive_tests[i]
print(str(i) + ". " + tweet_test + "\t\t" + predict_sentiment(tweet_test)) # Should be Positive

tweet_test = negative_tests[i]
print(str(i) + ". " + tweet_test + "\t\t" + predict_sentiment(tweet_test)) # Should be Negative

i+=1
tweet_test = positive_tests[i]
print(str(i) + ". " + tweet_test + "\t\t" + predict_sentiment(tweet_test)) # Should be Positive

tweet_test = negative_tests[i]
print(str(i) + ". " + tweet_test + "\t\t" + predict_sentiment(tweet_test)) # Should be Negative

i+=1
tweet_test = positive_tests[i]
print(str(i) + ". " + tweet_test + "\t\t" + predict_sentiment(tweet_test)) # Should be Positive

tweet_test = negative_tests[i]
print(str(i) + ". " + tweet_test + "\t\t" + predict_sentiment(tweet_test)) # Should be Negative

i+=1
tweet_test = positive_tests[i]
print(str(i) + ". " + tweet_test + "\t\t" + predict_sentiment(tweet_test)) # Should be Positive

tweet_test = negative_tests[i]
print(str(i) + ". " + tweet_test + "\t\t" + predict_sentiment(tweet_test)) # Should be Negative

i+=1
tweet_test = positive_tests[i]
print(str(i) + ". " + tweet_test + "\t\t" + predict_sentiment(tweet_test)) # Should be Positive

tweet_test = negative_tests[i]
print(str(i) + ". " + tweet_test + "\t\t" + predict_sentiment(tweet_test)) # Should be Negative

i+=1
tweet_test = positive_tests[i]
print(str(i) + ". " + tweet_test + "\t\t" + predict_sentiment(tweet_test)) # Should be Positive

tweet_test = negative_tests[i]
print(str(i) + ". " + tweet_test + "\t\t" + predict_sentiment(tweet_test)) # Should be Negative

i+=1
tweet_test = positive_tests[i]
print(str(i) + ". " + tweet_test + "\t\t" + predict_sentiment(tweet_test)) # Should be Positive

tweet_test = negative_tests[i]
print(str(i) + ". " + tweet_test + "\t\t" + predict_sentiment(tweet_test)) # Should be Negative

i+=1
tweet_test = positive_tests[i]
print(str(i) + ". " + tweet_test + "\t\t" + predict_sentiment(tweet_test)) # Should be Positive

tweet_test = negative_tests[i]
print(str(i) + ". " + tweet_test + "\t\t" + predict_sentiment(tweet_test)) # Should be Negative

i+=1
tweet_test = positive_tests[i]
print(str(i) + ". " + tweet_test + "\t\t" + predict_sentiment(tweet_test)) # Should be Positive

tweet_test = negative_tests[i]
print(str(i) + ". " + tweet_test + "\t\t" + predict_sentiment(tweet_test)) # Should be Negative

i+=1
tweet_test = positive_tests[i]
print(str(i) + ". " + tweet_test + "\t\t" + predict_sentiment(tweet_test)) # Should be Positive

tweet_test = negative_tests[i]
print(str(i) + ". " + tweet_test + "\t\t" + predict_sentiment(tweet_test)) # Should be Negative

i+=1
tweet_test = positive_tests[i]
print(str(i) + ". " + tweet_test + "\t\t" + predict_sentiment(tweet_test)) # Should be Positive

tweet_test = negative_tests[i]
print(str(i) + ". " + tweet_test + "\t\t" + predict_sentiment(tweet_test)) # Should be Negative

i+=1
tweet_test = positive_tests[i]
print(str(i) + ". " + tweet_test + "\t\t" + predict_sentiment(tweet_test)) # Should be Positive

tweet_test = negative_tests[i]
print(str(i) + ". " + tweet_test + "\t\t" + predict_sentiment(tweet_test)) # Should be Negative

i+=1
tweet_test = positive_tests[i]
print(str(i) + ". " + tweet_test + "\t\t" + predict_sentiment(tweet_test)) # Should be Positive

tweet_test = negative_tests[i]
print(str(i) + ". " + tweet_test + "\t\t" + predict_sentiment(tweet_test)) # Should be Negative

i+=1
tweet_test = positive_tests[i]
print(str(i) + ". " + tweet_test + "\t\t" + predict_sentiment(tweet_test)) # Should be Positive

tweet_test = negative_tests[i]
print(str(i) + ". " + tweet_test + "\t\t" + predict_sentiment(tweet_test)) # Should be Negative

i+=1
tweet_test = positive_tests[i]
print(str(i) + ". " + tweet_test + "\t\t" + predict_sentiment(tweet_test)) # Should be Positive

tweet_test = negative_tests[i]
print(str(i) + ". " + tweet_test + "\t\t" + predict_sentiment(tweet_test)) # Should be Negative

i+=1
tweet_test = positive_tests[i]
print(str(i) + ". " + tweet_test + "\t\t" + predict_sentiment(tweet_test)) # Should be Positive

tweet_test = negative_tests[i]
print(str(i) + ". " + tweet_test + "\t\t" + predict_sentiment(tweet_test)) # Should be Negative

i+=1
tweet_test = positive_tests[i]
print(str(i) + ". " + tweet_test + "\t\t" + predict_sentiment(tweet_test)) # Should be Positive

tweet_test = negative_tests[i]
print(str(i) + ". " + tweet_test + "\t\t" + predict_sentiment(tweet_test)) # Should be Negative

i+=1
tweet_test = positive_tests[i]
print(str(i) + ". " + tweet_test + "\t\t" + predict_sentiment(tweet_test)) # Should be Positive

tweet_test = negative_tests[i]
print(str(i) + ". " + tweet_test + "\t\t" + predict_sentiment(tweet_test)) # Should be Negative

i+=1
tweet_test = positive_tests[i]
print(str(i) + ". " + tweet_test + "\t\t" + predict_sentiment(tweet_test)) # Should be Positive

tweet_test = negative_tests[i]
print(str(i) + ". " + tweet_test + "\t\t" + predict_sentiment(tweet_test)) # Should be Negative

i+=1
tweet_test = positive_tests[i]
print(str(i) + ". " + tweet_test + "\t\t" + predict_sentiment(tweet_test)) # Should be Positive

tweet_test = negative_tests[i]
print(str(i) + ". " + tweet_test + "\t\t" + predict_sentiment(tweet_test)) # Should be Negative