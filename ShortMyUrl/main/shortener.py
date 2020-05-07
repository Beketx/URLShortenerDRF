import string
import hashlib
import random

class ShortenerOfUrl:
    def create_token(self):  #rendering random uuid token here
        letters = random.choice(string.ascii_letters)
        x = hashlib.sha256(letters.encode()).hexdigest()
        e = x[:8]+'-'+x[8:12]+'-'+x[12:16]+'-'+x[16:20]+'-'+x[20:32]
        return e