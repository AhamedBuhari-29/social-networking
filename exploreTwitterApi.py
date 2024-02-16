# -*- coding: utf-8 -*-
"""
Created on Sun Jan 28 22:34:09 2024

@author: day1
"""
import requests
from requests_oauthlib import OAuth1
def get_authenticated_user(api_key,api_secret_key,access_token,access_token_secret):
    url = "https://api.twitter.com/2/users/me"
    auth = OAuth1(
        api_key,
        client_secret = api_secret_key,
        resource_owner_key = access_token,
        resource_owner_secret = access_token_secret
    )
    response = requests.get(url, auth=auth)
    if response.status_code == 200:
        user_data = response.json()
        print("User ID :", user_data["data"]["id"])
        print("Username:", user_data["data"]["username"])
    else:
        print("Error:", response.status_code,response.text)
api_key="TPGl6O0JcZBf5X9MdWwL9jD0P"
api_secret_key="3huV5Yu2rgiEASVZqQaGo920EJE4aDJTL7myZztx5um6BVeeAW"
access_token="1748232818294165504-Lhhe7crVmwW7PuNEeSdUqG6UZ7M5Yr"
access_token_secret="lMfL4RTRcXwt4I90ThZYoukhSOUFcq0TQ30asSXMTyRKN"
get_authenticated_user(api_key,api_secret_key,access_token,access_token_secret)

