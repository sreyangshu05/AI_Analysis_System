import time
from collections import OrderedDict

class Cache:
    def __init__(self, expiry=3600):
        self.cache = OrderedDict()
        self.expiry = expiry

    def set(self, key, value):
        self.cache[key] = (value, time.time())
        self._cleanup()

    def get(self, key):
        self._cleanup()
        return self.cache.get(key, (None,))[0]

    def _cleanup(self):
        current_time = time.time()
        keys_to_delete = [
            key for key, (_, timestamp) in self.cache.items()
            if current_time - timestamp > self.expiry
        ]
        for key in keys_to_delete:
            del self.cache[key]
