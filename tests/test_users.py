import unittest
import requests
import json
import unittest
import string 
import random
class user(unittest.TestCase):
    def test_me(self):
        url = "https://dev.yuride.network/api/users/me/"
        header = {
            'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjQ5MDQxODgzLCJqdGkiOiIxNjQ3OWFjMDE2YWM0ZjFlYmZiMGFjYjlmMmExYzU3OCIsInVzZXJfaWQiOjEwMTR9.ZVz0bsJ6OpSiXM3A_dxELCO-BzGLCYe9SAmlPoT1WxE'}
        response = requests.get(url,headers=header)
        a = json.dumps(response.json())
        x = json.loads(a)
    
		
        self.assertEqual(x['username'],"swaggg")
        # print(x)
        self.assertEqual(response.status_code,200)

    def test_me_no_token(self):
        url = "https://dev.yuride.network/api/users/me/"
        header = {
            'Authorization': ''
 		}
        response = requests.get(url,headers=header)
        a = json.dumps(response.json())
        x = json.loads(a)

		
		
        self.assertEqual(response.status_code,403)

    def test_me_invalid_token(self):
        url = "https://dev.yuride.network/api/users/me/"
        header = {
            'Authorization': 'kkkk'
        }
		
        response = requests.get(url,headers=header)
        a = json.dumps(response.json())
        x = json.loads(a) 
        

        self.assertEqual(response.status_code,403)     
        if "username" not in x:	
            print("token_not_valid") 
        


		
if __name__ == "__main__":
	unittest.main()