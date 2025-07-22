from protocol_to_crf_generator.ct_cache import CTCache


def test_lru_cache_reduces_db_queries() -> None:
    calls = {"count": 0}

    def fetch(key: str) -> str:
        calls["count"] += 1
        return key.upper()

    cache = CTCache(fetch, maxsize=8)

    for _ in range(100):
        assert cache.lookup("test") == "TEST"

    assert calls["count"] == 1
    assert cache.hit_rate() >= 0.9
