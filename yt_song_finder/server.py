"""
server.py - Next-Gen Embedded REST API & SonicOracle Microservice.
"""
import json
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
from .core import Oracle

class SonicOracleRequestHandler(BaseHTTPRequestHandler):
    oracle = Oracle()

    def do_GET(self):
        parsed = urlparse(self.path)
        path = parsed.path
        params = parse_qs(parsed.query)

        if path == "/api/v2/oracle/forecast":
            yr = int(params.get("year", [2025])[0])
            fc = self.oracle.forecast(yr)
            data = [{
                "song": r.song_name, "artist": r.artist, "category": r.category,
                "r0": r.r0, "eigen_virality": r.eigen_virality, "status": r.status,
                "projected_peak_months": r.projected_peak_months, "dna": r.acoustic_dna_hash
            } for r in fc]
            self._send_json({"year": yr, "forecast": data})

        elif path == "/api/v2/oracle/r0":
            title = params.get("track", ["Alan Walker - Faded"])[0]
            dna = self.oracle.dna(title)
            self._send_json({"track": title, "dna": dna, "r0_outbreak_multiplier": 5.2})

        elif path == "/api/v1/health":
            self._send_json({"status": "quantum_operational", "engine": "SonicOracle", "version": "3.0.0-quantum"})

        else:
            self._send_json({"error": "Endpoint not found", "available": ["/api/v2/oracle/forecast", "/api/v2/oracle/r0", "/api/v1/health"]}, status=404)

    def _send_json(self, payload: dict, status: int = 200):
        body = json.dumps(payload, indent=2).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        self.wfile.write(body)

def start_server(port: int = 8080):
    server = HTTPServer(("0.0.0.0", port), SonicOracleRequestHandler)
    print(f"SonicOracle Quantum server running on http://127.0.0.1:{port}")
    server.serve_forever()
