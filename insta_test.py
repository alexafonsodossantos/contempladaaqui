
import requests
access_token = "EAAGCdVQMxg4BAHfOrK6RqQJzcn3mq3RDmNLiK1LHyeZBZAl5eyZBfGVEAAGCdVQMxg4BAJ4mmabLg1ilu44JbgZCuKUwwPZCgzrg9RZBWwZB977JmgoihX0YtMNrJHB2VDzuKh1ilmAGSAOW8SimaZBICy977SutE4Tnf91NZAXlNZBQw5hEc3YjIORlMIe7l3MBupV4luqMknUcPZBDbGshHZAA2COkxxuZCxr5cS86B0ysh5AO879I8QZAm6hs9PX3ZBZBQVprBpuOcI3URbZCDfv25mevZCgo0ZBkiMvWt4vqhb2pXGaeXtmo8IiiJWhOh4J2hN8iYhoPstc1tRv2XZBhoPjqQx7WbGBQLtAIMaQeJ60UZAWC6FVhdQnuwSmZCTyFyVWzqgMPhEgzgrvr90C3Qzg7kJZAXBmCRLmEOAYLlUSlSLGC"
url = f"https://graph.facebook.com/v15.0/me/accounts?access_token={access_token}"


APP_ID = "424915409618446"
APP_SECRET = "e1f89e73c3c23f7b3ede0d5adc806f77"


#teste = requests.get(url).json()
#print(teste['data'][0]['access_token'])



url2 = f"https://graph.facebook.com/v15.0/oauth/access_token?grant_type=fb_exchange_token&client_id={APP_ID}&client_secret={APP_SECRET}&fb_exchange_token={access_token}"

teste = requests.get(url2).json()
L_TOKEN = teste['access_token']

page_id = "106231317705181"
instagram_id = "17841447246430902"
url3 = f"https://graph.facebook.com/v10.0/{page_id}?fields=instagram_business_account&access_token={L_TOKEN}"

public_img_path = "http://contempladaaqui.herokuapp.com/cotas/static/img/15336.png"
caption = "Teste"


post_url = f"https://graph.facebook.com/v10.0/{instagram_id}/media?image_url={public_img_path}&caption={caption}&access_token={L_TOKEN}"

pub = requests.post(post_url).json()
post_id = pub['id']


url4 = f"https://graph.facebook.com/v10.0/{instagram_id}/media_publish?creation_id={post_id}&access_token={L_TOKEN}"
pub = requests.post(url4)
print(pub.text)