# autonix/core/agent.py
class AutonixAgent:
    def __init__(self, name="AutonixAgent"):
        self.name = name
        self.memory = {}

    def perceive(self, observation):
        """Process input observation from the environment."""
        raise NotImplementedError("This method should be overridden.")

    def decide(self):
        """Make a decision based on current state or observation."""
        raise NotImplementedError("This method should be overridden.")

    def act(self):
        """Return an action based on decision."""
        raise NotImplementedError("This method should be overridden.")