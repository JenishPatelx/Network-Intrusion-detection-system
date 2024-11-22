from src.monitoring.system_monitor import SystemMonitor

def test_system_monitor():
    monitor = SystemMonitor()
    metrics = monitor.get_metrics()
    assert "cpu" in metrics and "memory" in metrics
    assert metrics["cpu"] >= 0 and metrics["memory"] >= 0

