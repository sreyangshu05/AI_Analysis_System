import time
from app.cache import Cache

def test_cache_set_and_get():
    cache = Cache(expiry=2)
    cache.set("key1", "value1")
    assert cache.get("key1") == "value1"

def test_cache_expiry():
    cache = Cache(expiry=1)
    cache.set("key1", "value1")
    time.sleep(2)
    assert cache.get("key1") is None

def test_cache_cleanup():
    cache = Cache(expiry=2)
    cache.set("key1", "value1")
    cache.set("key2", "value2")
    time.sleep(3)
    cache._cleanup()
    assert cache.get("key1") is None
    assert cache.get("key2") is None
