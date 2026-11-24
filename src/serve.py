"""推理服务（示例占位骨架）。

提供 /health 健康检查与 /predict 占位接口，供 CI 中 Docker 容器
启动后访问验证。接入真实项目时，在此加载模型并返回推理结果。
"""

import json
from http.server import BaseHTTPRequestHandler, HTTPServer


class Handler(BaseHTTPRequestHandler):
    def _send(self, code: int, payload: dict) -> None:
        body = json.dumps(payload).encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self) -> None:
        if self.path == "/health":
            self._send(200, {"status": "ok"})
        elif self.path == "/predict":
            self._send(200, {"result": "placeholder"})
        else:
            self._send(404, {"error": "not found"})

    def log_message(self, *args) -> None:  # 静默访问日志
        pass


if __name__ == "__main__":
    HTTPServer(("0.0.0.0", 8000), Handler).serve_forever()
