import random
from env.models import Area, State
from env.tasks import load_task

class PowerGridEnv:

    def __init__(self, level="easy"):
        self.level = level
        self.state = None

    # 🔁 RESET ENVIRONMENT
    def reset(self):
        task = load_task(self.level)

        self.state = State(
            areas=[
                Area(
                    id=i,
                    has_power=random.choice([True, False]),
                    priority=random.randint(1, 5)
                )
                for i in range(task["num_areas"])
            ],
            complaints=task["complaints"],
            time=0
        )

        return self.state

    # ⚙️ STEP FUNCTION (UPDATED & IMPROVED)
    def step(self, action):
        reward = 0.0

        # 🔧 Handle action
        if action["type"] == "restore":
            area = self.state.areas[action["area_id"]]

            if not area.has_power:
                area.has_power = True

                # base reward
                reward += 0.2

                # priority-based reward (higher priority = more reward)
                reward += area.priority * 0.1

        elif action["type"] == "ignore":
            reward -= 0.3

        # ⚠️ Penalty for complaints
        reward -= (self.state.complaints * 0.02)

        # 🎯 Bonus if all areas restored
        if all(a.has_power for a in self.state.areas):
            reward += 0.5

        # ⏱ Increase time
        self.state.time += 1

        # 🛑 Stop after 10 steps
        done = self.state.time >= 10

        # 🔒 Clamp reward between 0 and 1
        reward = max(0.0, min(1.0, reward))

        return self.state, reward, done, {}