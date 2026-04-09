import requests

URL = "http://localhost:7860"

# Reset
res = requests.post(f"{URL}/reset")
state = res.json()["state"]

total_reward = 0

for _ in range(10):
    action = 0  # simple policy

    res = requests.post(f"{URL}/step", params={"action": action})
    data = res.json()

    total_reward += data["reward"]

    if data["done"]:
        break

print("Final Reward:", total_reward)
