# autonix/examples/example_env.py
from autonix.core.environment import AutonixEnvironment

class ExampleEnvironment(AutonixEnvironment):
    def __init__(self):
        super().__init__()
        self.state = "initial_state"

    def reset(self):
        self.state = "initial_state"

    def step(self, action):
        self.state = f"updated_state_after_{action}"

    def get_observation(self):
        return self.state