"""模型形状测试示例。"""

from src.model import PlaceholderModel


def test_model_output_shape() -> None:
    model = PlaceholderModel(input_dim=4, output_dim=2)
    output = model.forward([0.1, 0.2, 0.3, 0.4])
    assert len(output) == 2
