"""
test_alerting.py - Unit tests for Outbreak Event Dispatcher and Alerting Bus.
"""
import unittest
from yt_song_finder.alerting import AlertDispatcher, AlertSeverity, MemoryAlertSink

class TestAlerting(unittest.TestCase):
    def test_threshold_dispatch(self):
        dispatcher = AlertDispatcher(warning_r0=3.0, critical_r0=5.0)
        sink = MemoryAlertSink()
        dispatcher.register_sink(sink)

        # 1. Supercritical triggers CRITICAL
        evt1 = dispatcher.evaluate_track("Song X", "Artist A", r0=6.2, eigen_virality=0.4)
        self.assertIsNotNone(evt1)
        self.assertEqual(evt1.severity, AlertSeverity.CRITICAL)

        # 2. Warning range triggers WARNING
        evt2 = dispatcher.evaluate_track("Song Y", "Artist B", r0=3.8, eigen_virality=0.2)
        self.assertIsNotNone(evt2)
        self.assertEqual(evt2.severity, AlertSeverity.WARNING)

        # 3. Subcritical does not dispatch alert
        evt3 = dispatcher.evaluate_track("Song Z", "Artist C", r0=0.8, eigen_virality=0.05)
        self.assertIsNone(evt3)

        self.assertEqual(len(sink.events), 2)
        self.assertIn("CRITICAL", sink.events[0].to_json())

if __name__ == "__main__":
    unittest.main()
