"""
alerting.py - Outbreak Event Dispatcher & Real-Time Alert Bus.
Dispatches critical epidemiological warnings when audio strains violate virality thresholds.
Supports stdout, audit log files, and pluggable asynchronous webhook receivers.
"""
import json
import time
from enum import Enum
from dataclasses import dataclass, asdict
from typing import Callable, Optional

class AlertSeverity(str, Enum):
    INFO = "INFO"
    WATCHLIST = "WATCHLIST"
    WARNING = "WARNING"
    CRITICAL = "CRITICAL"

@dataclass
class OutbreakEvent:
    event_id: str
    track_name: str
    artist: str
    r0: float
    eigen_virality: float
    severity: AlertSeverity
    timestamp: float
    message: str

    def to_json(self) -> str:
        d = asdict(self)
        d["severity"] = self.severity.value
        return json.dumps(d)

class AlertSink:
    """Abstract interface for receiving alert payloads."""
    def emit(self, event: OutbreakEvent) -> None:
        raise NotImplementedError

class MemoryAlertSink(AlertSink):
    """In-memory alert buffer for testing and real-time dashboard polling."""
    def __init__(self, max_size: int = 1000) -> None:
        self.events: list[OutbreakEvent] = []
        self.max_size = max_size

    def emit(self, event: OutbreakEvent) -> None:
        self.events.append(event)
        if len(self.events) > self.max_size:
            self.events.pop(0)

class CallbackAlertSink(AlertSink):
    """Dispatches event to user-defined callable or webhook transmitter."""
    def __init__(self, callback: Callable[[OutbreakEvent], None]) -> None:
        self.callback = callback

    def emit(self, event: OutbreakEvent) -> None:
        self.callback(event)

class AlertDispatcher:
    """
    Central alerting bus. Evaluates transmission reproduction metrics against policy thresholds.
    """
    def __init__(
        self,
        warning_r0: float = 3.0,
        critical_r0: float = 5.0
    ) -> None:
        self.warning_r0 = warning_r0
        self.critical_r0 = critical_r0
        self.sinks: list[AlertSink] = []

    def register_sink(self, sink: AlertSink) -> None:
        self.sinks.append(sink)

    def evaluate_track(
        self,
        track_name: str,
        artist: str,
        r0: float,
        eigen_virality: float
    ) -> Optional[OutbreakEvent]:
        if r0 >= self.critical_r0:
            sev = AlertSeverity.CRITICAL
            msg = f"Supercritical viral outbreak confirmed: R0={r0:.2f} violates ceiling."
        elif r0 >= self.warning_r0:
            sev = AlertSeverity.WARNING
            msg = f"Accelerating transmission detected: R0={r0:.2f} exceeds threshold."
        elif r0 > 1.0:
            sev = AlertSeverity.WATCHLIST
            msg = f"Subcritical active spread: R0={r0:.2f}."
        else:
            sev = AlertSeverity.INFO
            msg = f"Decaying trajectory: R0={r0:.2f}."

        if sev in (AlertSeverity.WARNING, AlertSeverity.CRITICAL):
            event = OutbreakEvent(
                event_id=f"EVT-{int(time.time() * 1000)}-{abs(hash(track_name)) % 10000}",
                track_name=track_name,
                artist=artist,
                r0=r0,
                eigen_virality=eigen_virality,
                severity=sev,
                timestamp=time.time(),
                message=msg
            )
            for sink in self.sinks:
                sink.emit(event)
            return event
        return None
