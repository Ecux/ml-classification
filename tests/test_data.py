"""数据验证测试示例。

教学说明：接入真实项目后，在此检查样本特征维度、缺失值、
标签分布等数据质量问题。
"""


def test_data_dimension_placeholder() -> None:
    expected_dim = 4
    sample = [0.1, 0.2, 0.3, 0.4]
    assert len(sample) == expected_dim
