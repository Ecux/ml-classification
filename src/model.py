"""模型定义（示例占位骨架）。

教学说明：当前为纯 Python 占位实现，用于打通 CI 流水线；
接入真实项目时，可替换为 PyTorch / ONNX 模型，并保持输入输出
形状与测试用例一致。
"""

from typing import List


class PlaceholderModel:
    """占位模型：按输出维度返回结果列表。"""

    def __init__(self, input_dim: int = 4, output_dim: int = 2) -> None:
        self.input_dim = input_dim
        self.output_dim = output_dim

    def forward(self, x: List[float]) -> List[float]:
        """前向推理占位。

        Args:
            x: 输入特征列表，长度应等于 input_dim。

        Returns:
            长度为 output_dim 的输出列表。
        """
        if len(x) != self.input_dim:
            raise ValueError("输入特征维度与模型 input_dim 不一致")
        return [0.0] * self.output_dim
