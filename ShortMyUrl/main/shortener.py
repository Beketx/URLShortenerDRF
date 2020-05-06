import string
import hashlib
import random
import uuid
class ShortenerOfUrl:
    # token_size = 5
    # def init(self,token_size=None):  #initializing size here
    #     self.token_size = token_size
    def create_token(self):  #rendering random 5 digit token here
        # s = uuid.uuid4()
        letters = random.choice(string.ascii_letters)
        # x = ''.join(random.choice(letters) for i in range(5))
        x = hashlib.sha256(letters.encode()).hexdigest()
        e = x[:8]+'-'+x[8:12]+'-'+x[12:16]+'-'+x[16:20]+'-'+x[20:32]
        return e

        # letters = random.choice(string.ascii_letters)
        # return ''.join(s)