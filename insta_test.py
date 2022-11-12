
import requests
access_token = "EAAGCdVQMxg4BAMgALWTRfYViIoIvhCh7riG0ncEZBqN0E92W7hmtkxJj1nmJqbvAb3T8TVzwUTWWTxiAQlZASwR42T82JsRRYpFK7jB43RvXbphWwNGZCHHxo6ICFqzLc7qSSPAuP4QHIEV4SB9Pq9RwvegdTmcLZCZA9NleetTiFXU2Sl3nR3PDlAZBcvMr7WoXKAXxJxBEbZAdoNTPSoJ"
url = f"https://graph.facebook.com/v15.0/me/accounts?access_token={access_token}"


APP_ID = "424915409618446"
APP_SECRET = "e1f89e73c3c23f7b3ede0d5adc806f77"


#teste = requests.get(url).json()
#print(teste['data'][0]['access_token'])



url2 = f"https://graph.facebook.com/v15.0/oauth/access_token?grant_type=fb_exchange_token&client_id={APP_ID}&client_secret={APP_SECRET}&fb_exchange_token={access_token}"

teste = requests.get(url2)
print(teste.text)
page_id = "106231317705181"

#url3 = f"https://graph.facebook.com/v10.0/{page_id}?fields=instagram_business_account&access_token={L_TOKEN}"


#teste = requests.get(url3).json()
#print(teste)



instagram_id = "17841447246430902"

public_img_path = "http://contempladaaqui.herokuapp.com/cotas/static/img/15336.png"
caption = "Teste"


#post_url = f"https://graph.facebook.com/v10.0/{instagram_id}/media?image_url={public_img_path}&caption={caption}&access_token={L_TOKEN}"

#pub = requests.post(post_url).json()
#post_id = pub['id']


#url4 = f"https://graph.facebook.com/v10.0/{instagram_id}/media_publish?creation_id={post_id}&access_token={L_TOKEN}"
#pub = requests.post(url4)
#print(pub.text)