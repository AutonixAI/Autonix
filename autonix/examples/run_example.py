# autonix/examples/run_example.py
from autonix.examples.example_agent import ExampleAgent
from autonix.examples.example_env import ExampleEnvironment

if __name__ == "__main__":
    agent = ExampleAgent(name="AutonixTestAgent")
    env = ExampleEnvironment()

    # Initial environment setup
    observation = env.get_observation()
    print(f"Observation: {observation}")

    # Agent interaction
    agent.perceive(observation)
    action = agent.act()
    print(f"Agent Action: {action}")

    # Environment reacts
    env.step(action)
    print(f"Environment State: {env.get_observation()}")