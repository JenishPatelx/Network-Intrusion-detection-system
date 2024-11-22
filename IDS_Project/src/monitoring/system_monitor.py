import psutil

class SystemMonitor:
    """Monitors system metrics like CPU and memory usage."""
    
    def get_metrics(self):
        return {"cpu": psutil.cpu_percent(), "memory": psutil.virtual_memory().percent}

