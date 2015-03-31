import oauth2 as oauth,json
def tweets(username, count=20,key="**********************", secret="**************************", http_method="GET", post_body=None, http_headers=None):
    url="https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name="+username+"&count="+str(count)
    consumer = oauth.Consumer(key="********************", secret="**********************************")
    token = oauth.Token(key=key, secret=secret)
    client = oauth.Client(consumer, token)
    resp, content = client.request( url )
    return json.loads(content)
