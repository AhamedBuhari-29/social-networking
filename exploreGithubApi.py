# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 23:07:44 2024

@author: day1
"""

import requests
def get_user_info(username,token):
    url=f"https://api.github.com/users/{username}"
    headers={"Authorization":f"Bearer{token}"}
    response=requests.get(url,headers=headers)
    
    if response.status_code==200:
     user_data=response.json()
     print(f"User:{user_data['login']}")
     print(f"Name:{user_data['name']}")
     print(f"Followers:{user_data['followers']}")
     print(f"Public repositories:{user_data['public_repos']}")
    else:
     print(f"Error:{response.status_code}")
get_user_info('Ahamedbuhari2002','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')