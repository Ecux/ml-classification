"""推理测试示例。

教学说明：可在此接入真实推理调用，测量推理延迟（案例要求 <200ms）；
当前为占位断言，保证 CI 流程可跑通。
"""

import time


def test_inference_latency_placeholder() -> None:
    start = time.perf_counter()
    # 占位：替换为真实模型推理调用
    elapsed_ms = (time.perf_counter() - start) * 1000
    assert elapsed_ms < 200
