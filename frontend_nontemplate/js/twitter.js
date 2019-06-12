const TWITTER_BASE_URL = 'https://api.twitter.com/1.1/search/tweets.json'

const cb = new Codebird();
cb.setConsumerKey(TWITTER_API_KEY, TWITTER_SECRET_KEY);

cb.__call('search_tweets', {
    q: "NYC"
}, reply => {
    console.log(reply)
    console.log('here')
});