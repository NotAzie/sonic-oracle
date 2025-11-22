"""
server.py - Embedded REST API and HTTP server for programmatic access.
"""
import json
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
from .demo import DEMO_TRACKS
from .config import Config
from .scorer import SongScorer
from .deduplicator import CanonicalTrack

class SongFinderRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed = urlparse(self.path)
        path = parsed.path
        params = parse_qs(parsed.query)

        if path == "/api/v1/health":
            self._send_json({"status": "healthy", "version": "2.5.0-beast"})
        elif path == "/api/v1/demo":
            self._send_json({"status": "success", "data": DEMO_TRACKS})
        elif path == "/api/v1/rank":
            yr = int(params.get("year", [2021])[0])
            seeds = DEMO_TRACKS.get(yr, [])
            self._send_json({"year": yr, "count": len(seeds), "tracks": seeds})
        else:
            self._send_json({"error": "Endpoint not found"}, status=404)

    def _send_json(self, payload: dict, status: int = 200):
        body = json.dumps(payload).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        self.wfile.write(body)

def start_server(port: int = 8080):
    server = HTTPServer(("0.0.0.0", port), SongFinderRequestHandler)
    print(f"ViralSongFinder REST server running on http://127.0.0.1:{port}")
    server.serve_forever()
