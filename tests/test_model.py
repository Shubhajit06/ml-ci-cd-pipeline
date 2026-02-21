from src.model import get_model

def test_model():
    model = get_model()
    assert model is not None
