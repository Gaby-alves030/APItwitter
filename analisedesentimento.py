import tweepy

consumer_key = "K8c8ZwwjO5DNeScbSqZJOzgZg"
consumer_secret = "RjL6un0SfUAgSFq7ecbBHWWH7sYc18zd5OaAOIWiNeTglpN7eM"
access_token = "1640796693070336015-ARzjbJ6700I8zA1gHyGnsuzaHZduxK"
access_token_secret = "GaH6JHhUav7igaSf8kgaJgCrUZF4HhExyidKCAHbaK3e8"

# Autenticação do Tweepy
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Criar uma instância da API do Twitter
api = tweepy.API(auth)

# Definir o termo de pesquisa
query = "python"

# Coletar tweets usando a API do Twitter
tweets = api.search(q=query, lang="pt", count=10)

# Exibir os resultados
for tweet in tweets:
    print(tweet.text)
