import requests
import config
import json
def postInstagramQuote(filename):
#Post the Image
    image_location_1 = 'https://contempladaaqui.herokuapp.com/static/img/'+filename+'.png'
    post_url = 'https://graph.facebook.com/v10.0/{}/media'.format('17841447246430902')
    payload = {
    'image_url': image_location_1,
    'caption': 'Aqui seu dinheiro vale muito! Essa e outras oportunidades você encontra em www.contempladaaqui.com.br',
    'access_token': 'EAAGCdVQMxg4BAPO0ug34l0ipXcxmarZB2Ro11gxZB98FfpvnP4GZANtiwhHgzLkrZBacIiVQAZAUkZBvZCbQM6yBedCr8ntYycLnB8DgFWFdUgWLlen4E02idIRTZBqdAZARXZCgM41rf607WNeShG1mWmFiXWQdDTPYjuQKPyPZBoZBWTj8uxwbeTt9j6Fqg6Jtc1HoEzQJKeCpUy1Y3oAmC8Tj'
    }
    r = requests.post(post_url, data=payload)
    print(r.text)
    result = json.loads(r.text)
    if 'id' in result:
        creation_id = result['id']
        second_url = 'https://graph.facebook.com/v10.0/{}/media_publish'.format('17841447246430902')
        second_payload = {
        'creation_id': creation_id,
        'access_token':'EAAGCdVQMxg4BAPO0ug34l0ipXcxmarZB2Ro11gxZB98FfpvnP4GZANtiwhHgzLkrZBacIiVQAZAUkZBvZCbQM6yBedCr8ntYycLnB8DgFWFdUgWLlen4E02idIRTZBqdAZARXZCgM41rf607WNeShG1mWmFiXWQdDTPYjuQKPyPZBoZBWTj8uxwbeTt9j6Fqg6Jtc1HoEzQJKeCpUy1Y3oAmC8Tj'
        }
        r = requests.post(second_url, data=second_payload)
        print('--------Just posted to instagram--------')
        print(r.text)
    else:
        print('HOUSTON we have a problem')


postInstagramQuote('15251')