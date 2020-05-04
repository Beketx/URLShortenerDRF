import random
import string
import hashlib


class shortenerOfUrl:
    token_size = 5
    def init(self,token_size=None):  #initializing size here
        self.token_size = token_size
    def create_token(self):  #rendering random 5 digit token here
        letters = string.ascii_letters
        return ''.join(hashlib.sha256(letters.encode()).hexdigest())
    #
    # def encrypt_url(long_url):
    #     token = hashlib.sha256(long_url.encode()).hexdigest()