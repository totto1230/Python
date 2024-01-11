#!/usr/bin/env python3
##EXERCISE: INTERACT WITH THIS API: https://catfact.ninja/#/Facts
##GET THE 3 FIRST LETTERS
##INTERACT WITH THE GIPHY API (https://developers.giphy.com/docs/api/endpoint/#search) AND DISPLAY A GIF WITH THOSE LETTERS.
import requests, json, parse, config, webbrowser
from urllib import parse

def get_phrase():
    api_url = "https://catfact.ninja/fact"
    response = requests.get(url=api_url, headers={'accept' : 'application/json'})
    phrase = json.loads(response.text)
    return phrase

def split_phrase(phrase):
    complete = (phrase['fact'])
    splitted = complete.split()
    list_phrase = []
    for i in range(3):
        list_phrase.append(splitted[i])
    final_phrase = " ".join(list_phrase)
    print(f"COMPLETED: {complete} \n WORDS: {final_phrase}")
    return final_phrase

def get_gif(splitted):
    url_api = "http://api.giphy.com/v1/gifs/search"
    params = parse.urlencode({
            "q": splitted,
            "api_key": config.api_key,
            "limit": "1"
    })
    response=requests.get(url=url_api, params=params)
    complete = json.loads(response.text)
    ##RETURN URL OF THE GIF
    data_list = complete.get('data', [])
    urls = [item.get('embed_url', None) for item in data_list]
    url = ''.join(urls)
    webbrowser.open(url)

def _main():
    phrase = get_phrase()
    splitted = split_phrase(phrase)
    get_gif(splitted)

if __name__ == "__main__":
    _main()