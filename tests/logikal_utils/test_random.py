from logikal_utils.random import DEFAULT_RANDOM_SEED


def test_default_random_seed() -> None:
    assert bool(DEFAULT_RANDOM_SEED)
