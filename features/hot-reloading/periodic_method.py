import time
import cachetools

from utils import change_conf_file

ROTATE = 5

@cachetools.cached(cachetools.TTLCache(1, ROTATE))
def reload():
    print('Cache cleared, reloading config...')
    with open('config.txt') as f:
        parameters = f.read()
    return parameters

class Model():
    def log(self):
        self.model = reload()
        print(self.model)

if __name__ == '__main__':
    # Reload automatically every [ROTATE] seconds
    model = Model()
    while True:
        time.sleep(2)
        change_conf_file() # change data
        model.log()