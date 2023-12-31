from unittest import TestCase, main
import json
import requests

class TestCases(TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass
    
    def test_new_user(self):

        url = "http://127.0.0.1:8000/newUser"

        payload = json.dumps({
        "name": "mani",
        "email": "mani@gmail.com",
        "balance": 1100
        })
        headers = {
        'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload).json()
        
        self.assertEqual(response["status"], "success")
        
    def test_new_merchant(self):
        url = "http://127.0.0.1:8000/newMerchant"

        payload = json.dumps({
        "name": "mehfill",
        "email": "mehfill@gmail.com",
        "fee": 8
        })
        headers = {
        'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        self.assertEqual(response["status"], "success")
    
    def test_new_transact(self):
        url = "http://127.0.0.1:8000/transact"

        payload = json.dumps({
        "u_id": 3,
        "m_id": 3,
        "amount": 400
        })
        headers = {
        'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        self.assertEqual(response["status"], "success")
    
    def test_getMerchant_id(self):
        url = "http://127.0.0.1:8000/getMerchant/6"

        payload = {}
        headers = {}

        response = requests.request("GET", url, headers=headers, data=payload)
        self.assertEqual(response["status"], "success")


    def test_updateFee(self): 

        url = "http://127.0.0.1:8000/updateFee?mid=5&fee=3"

        payload = ""
        headers = {}

        response = requests.request("POST", url, headers=headers, data=payload)
        self.assertEqual(response["status"], "success")
    
    def test_reypay(self):
        url = "http://127.0.0.1:8000/repay?name=mani&amount=200"

        payload = {}
        headers = {}

        response = requests.request("POST", url, headers=headers, data=payload)
        self.assertEqual(response["status"], "success")
    
    def test_fee_merchant(self):

        url = "http://127.0.0.1:8000/fee/kfc"

        payload = ""
        headers = {}

        response = requests.request("GET", url, headers=headers, data=payload)
        self.assertEqual(response["status"], "success")
    
    def test_dues(self):

        url = "http://127.0.0.1:8000/dues/santhu"

        payload = ""
        headers = {}

        response = requests.request("GET", url, headers=headers, data=payload)
        self.assertEqual(response["status"], "success")
    
    def test_user_limit(self):
        url = "http://127.0.0.1:8000/usersAtLimit"

        payload = {}
        headers = {}

        response = requests.request("GET", url, headers=headers, data=payload)
        self.assertEqual(response["status"], "success")
    
    def test_total_dues(self):
        url = "http://127.0.0.1:8000/totalDues"

        payload = {}
        headers = {}

        response = requests.request("GET", url, headers=headers, data=payload)
        self.assertEqual(response["status"], "success")
    def test_some_test_Case(self):

        """
        1. When user limit exceedds should "Return insuffcient funds!" as messasge
        """
        
if __name__ == '__main__':
    main()