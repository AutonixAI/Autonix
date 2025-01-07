# autonix/core/environment.py
class AutonixEnvironment:
    def __init__(self):
        self.state = None

    def reset(self):
        """Reset the environment to its initial state."""
        raise NotImplementedError("This method should be overridden.")

    def step(self, action):
        """Update the environment based on the agent's action."""
        raise NotImplementedError("This method should be overridden.")

    def get_observation(self):
        """Return the current state as an observation for the agent."""
        raise NotImplementedError("This method should be overridden.")