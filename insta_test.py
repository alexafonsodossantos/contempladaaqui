
import requests
access_token = "EAAGCdVQMxg4BAODtdalwOaZAgNeRlCpiSisAQye636uhaGZCRSKGWm7GupQbuhXONYgYZB7jlpk0VncDpFOhySa1bCPsZC00ize14dFbCriW5ZCZBGVOTsLaEff692H0k0gdNWH1fVZCfGRaBeYCW3AcgawT92OwPXWK29F2NZCjdd87sBZAb92GTHmPN6DvtyAIdePuczlZBsJLtbgLtLhpqb"
url = f"https://graph.facebook.com/v15.0/me/accounts?access_token={access_token}"


APP_ID = "424915409618446"
APP_SECRET = "e1f89e73c3c23f7b3ede0d5adc806f77"


#teste = requests.get(url).json()
#print(teste['data'][0]['access_token'])



url2 = f"https://graph.facebook.com/v15.0/oauth/access_token?grant_type=fb_exchange_token&client_id={APP_ID}&client_secret={APP_SECRET}&fb_exchange_token={access_token}"

#teste = requests.get(url2).json()
#print(teste)

page_id = "106231317705181"





L_TOKEN = "EAAGCdVQMxg4BABCG46IRMsGNmFlZBQqcrs0pXBPxZCZA4Hp4aEN2bFUHZCeqkY4WdbODjcw4med2CiuYrvChvJ9EZCMgp6jwJNlDngpup3uAlgUjjNxTgWRa7vLV5FenUFIsM2BzFl8j8ElcjRZCNpqZAK2ew9NuYZCaRag5QnO9ggZDZD"


url3 = f"https://graph.facebook.com/v10.0/{page_id}?fields=instagram_business_account&access_token={L_TOKEN}"


#teste = requests.get(url3).json()
#print(teste)



instagram_id = "17841447246430902"

public_img_path = ""
caption = ""


post_url = f"https://graph.facebook.com/v10.0/{instagram_id}/media?image_url={public_image_path}&caption={caption}&access_token={L_TOKEN}"

pub = request.post(post_url)
print(pub)