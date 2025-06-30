import numpy as np
from ml.model import inference
from sklearn.ensemble import RandomForestClassifier
from ml.model import compute_model_metrics, train_model


def test_train_model_runs():
    """
    Test that train_model runs without errors
    """
    X = np.random.rand(10, 5)
    y = np.random.randint(0, 2, 10)
    model = train_model(X, y)
    assert model is not None


def test_inference_runs():
    """
    Test that inference runs and returns predictions
    """
    X = np.random.rand(10, 5)
    y = np.random.randint(0, 2, 10)
    model = RandomForestClassifier().fit(X, y)
    preds = inference(model, X)
    assert len(preds) == len(y)


def test_metrics_computation():
    """
    Test that compute_model_metrics returns precision,
    recall, and fbeta as floats
    """
    y = [0, 1, 1, 0]
    preds = [0, 1, 0, 0]
    p, r, fb = compute_model_metrics(y, preds)
    assert isinstance(p, float)
    assert isinstance(r, float)
    assert isinstance(fb, float)
