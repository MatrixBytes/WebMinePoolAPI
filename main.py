class WebMinePool:
    def __init__(self, secret_key):
        self.secret_key = secret_key

    def setSecretKey(self, newsecretkey):
        self.secret_key = newsecretkey
    
    def createUser(self, username):
        req = json.loads(get(f'https://webminepool.com/api/{self.secret_key}/create_user/{username}').text)
        if req["success"] == False:
            return False, req["message"]
        else:
            return True, req["message"]

    def deleteUser(self, username):
        req = json.loads(get(f'https://webminepool.com/api/{self.secret_key}/delete_user/{username}').text)
        if req["success"] == False:
            return False, req["message"]
        else:
            return True, req["message"]

    def userHashes(self, username):
        req = json.loads(get(f'https://webminepool.com/api/{self.secret_key}/user_hashes/{username}').text)
        if req["success"] == False:
            return False, req["message"]
        else:
            return True, req["hashes"]

    def hashRate(self, amount):
        req = json.loads(get(f'https://webminepool.com/api/{self.secret_key}/hash_rate/{amount}').text)
        if req["success"] == False:
            return False, req["message"]
        else:
            return True, req["satoshi"]

    def Users(self):
        req = json.loads(get(f'https://webminepool.com/api/{self.secret_key}/users/').text)
        print(req)
        if req["success"] == False:
            return False, req["message"]
        else:
            return True, req["users"]
    
    def Balance(self):
        req = json.loads(get(f'https://webminepool.com/api/{self.secret_key}/balance/').text)
        if req["success"] == False:
            return False, req["message"]
        else:
            return True, req["balance"]
    
    def Withdraw(self, username, amount):
        req = json.loads(get(f'https://webminepool.com/api/{self.secret_key}/withdraw/{username}/{amount}').text)
        if req["success"] == False:
            return False, req["message"]
        else:
            return True, req["balance"]
    
    def resetAllUserHashes(self):
        req = json.loads(get(f'https://webminepool.com/api/{self.secret_key}/reset_all_user_hashes/').text)
        if req["success"] == False:
            return False, req["message"]
        else:
            return True, req["message"]

    def resetUserHashes(self, username):
        req = json.loads(get(f'https://webminepool.com/api/{self.secret_key}/reset_user_hashes/').text)
        if req["success"] == False:
            return False, req["message"]
        else:
            return True, req["message"]
