# autonix/examples/example_agent.py
from autonix.core.agent import AutonixAgent

class ExampleAgent(AutonixAgent):
    def perceive(self, observation):
        self.memory["last_observation"] = observation

    def decide(self):
        return "action_based_on_" + self.memory.get("last_observation", "nothing")

    def act(self):
        return self.decide()