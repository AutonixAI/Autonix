# autonix/core/memory.py
class AutonixMemory:
    def __init__(self):
        self.history = []

    def store(self, item):
        """Store an item in memory."""
        self.history.append(item)

    def retrieve(self, index=-1):
        """Retrieve an item from memory (default: last item)."""
        return self.history[index] if self.history else None