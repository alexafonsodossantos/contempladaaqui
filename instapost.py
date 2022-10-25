import requests
import config
import json
def postInstagramQuote():
#Post the Image
    image_location_1 = 'https://contempladaaqui.herokuapp.com/static/img/15006.png'
    post_url = 'https://graph.facebook.com/v10.0/{}/media'.format('17841447246430902')
    payload = {
    'image_url': image_location_1,
    'caption': 'Aqui seu dinheiro vale muito! Essa e outras oportunidades você encontra em www.contempladaaqui.com.br',
    'access_token': 'EAAGCdVQMxg4BADw9Dakw3I9wZB10EPYHjZAhyr9f7RQQoT6sw9NPDANDL5GUM1WGKJZC9NSKruZA1aRfRM0O4wZBxm7J7LILZCBRV2UGZAVmn4qRZBHVPvtZBryqG5M0AZBwJ17FQDp7B9JzrbzXZCbpIxPxAtn00BrLupOfKbrDZAMh8gZDZD'
    }
    r = requests.post(post_url, data=payload)
    print(r.text)
    result = json.loads(r.text)
    if 'id' in result:
        creation_id = result['id']
        second_url = 'https://graph.facebook.com/v10.0/{}/media_publish'.format('17841447246430902')
        second_payload = {
        'creation_id': creation_id,
        'access_token':'EAAGCdVQMxg4BADw9Dakw3I9wZB10EPYHjZAhyr9f7RQQoT6sw9NPDANDL5GUM1WGKJZC9NSKruZA1aRfRM0O4wZBxm7J7LILZCBRV2UGZAVmn4qRZBHVPvtZBryqG5M0AZBwJ17FQDp7B9JzrbzXZCbpIxPxAtn00BrLupOfKbrDZAMh8gZDZD'
        }
        r = requests.post(second_url, data=second_payload)
        print('--------Just posted to instagram--------')
        print(r.text)
    else:
        print('HOUSTON we have a problem')


postInstagramQuote()