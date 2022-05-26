import unittest
import requests
import json
import unittest
import string 
import random

class refresh(unittest.TestCase):
    def test_refresh(self):
            url = "https://dev.yuride.network/api/token/refresh/"
        
            header = {
                "Accept": "application/json"
            }
            data = {
            "refresh": "string"
            }

            request = requests.post(url, headers=header, data=data)

            if "access" not in request.json():
                self. assertFalse(False, "NO ACCESS token")
            self.assertEqual(request.status_code,200)


    def test_refresh_no_body(self):
        url = "https://dev.yuride.network/api/token/refresh/"
    
        header = {
            "Accept": "application/json"
        }
        data = {
        "refresh": ""
        }

        request = requests.post(url, headers=header, data=data)

        self.assertEqual(request.status_code,400)

    def test_refresh_invalid_token(self):
        url = "https://dev.yuride.network/api/token/refresh/"
    
        header = {
            "Accept": "application/json"
        }
        data = {
        "refresh": 2
        }

        request = requests.post(url, headers=header, data=data)
         
        if "access" in request.text:
            raise AttributeError('Invalid Token!')

        self.assertEqual(request.status_code,401)