import requests
import json
import argparse
from settings import TOKEN


def get_bitly_profile_info(token):    
    bitly_url = "https://api-ssl.bitly.com/v4/user" 
    bitly_header = {'Authorization' : 'Bearer {}'.format(token)} 
  
    response = requests.get(bitly_url, headers=bitly_header)        
    response.raise_for_status() 
  
    return json.loads(response.text)

def shorten_link(token, url):
    bitly_url = "https://api-ssl.bitly.com/v4/bitlinks"
    bitly_header = {'Authorization' : 'Bearer {}'.format(token)} 
    bitly_json = {'long_url' : url}
  
    response = requests.post(bitly_url, headers=bitly_header, json=bitly_json)
    response.raise_for_status()  
    obj = json.loads(response.text)
    bitlink = obj['id']
  
    return bitlink 

def count_clicks(token, link):
    bitly_url = 'https://api-ssl.bitly.com/v4/bitlinks/{}/clicks/summary'.format(link)
    bitly_header = {'Authorization' : 'Bearer {}'.format(token)}
    payload = {'unit': 'day', 'units': '-1'}

    response = requests.get(bitly_url, headers=bitly_header, params=payload)        
    response.raise_for_status() 
    obj = json.loads(response.text)
    clicks_count = obj['total_clicks']
  
    return clicks_count

def is_bitlink(token, url):
    bitly_url = 'https://api-ssl.bitly.com/v4/bitlinks/{}'.format(url)
    bitly_header = {'Authorization' : 'Bearer {}'.format(token)}
    
    response = requests.get(bitly_url, headers=bitly_header)    
    
    return response.ok
    
def main():
    #user_input = input("Enter link: ")
    parser = argparse.ArgumentParser()
    parser.add_argument('link', type=str)
    args = parser.parse_args()    

    if is_bitlink(TOKEN, args.link):
        print('Number of clicks on a link', count_clicks(TOKEN, args.link))
    else:
        print('Bitlink: ', shorten_link(TOKEN, args.link))

try:
    if __name__ == '__main__':
        main()
        
except requests.exceptions.HTTPError as error:
    print("Can't get data from server:\n{0}".format(error))
 