from env.environment import PowerGridEnv
from env.grader import grade

env = PowerGridEnv(level="medium")
state = env.reset()

total_reward = 0

print("\n⚡ SMART POWER GRID SIMULATION STARTED\n")

for step in range(10):
    action = {"type": "ignore"}

    # 🔥 smarter logic: pick highest priority area without power
    best_area = -1
    best_priority = -1

    for i, area in enumerate(state.areas):
        if not area.has_power and area.priority > best_priority:
            best_priority = area.priority
            best_area = i

    if best_area != -1:
        action = {"type": "restore", "area_id": best_area}

    state, reward, done, _ = env.step(action)
    total_reward += reward

    # 🎨 CLI visualization
    print(f"\nStep {step+1}")
    print("Areas Status:")
    for a in state.areas:
        status = "🟢 ON" if a.has_power else "🔴 OFF"
        print(f"Area {a.id} | Priority: {a.priority} | {status}")

    print(f"Complaints: {state.complaints}")
    print(f"Reward: {round(reward,2)}")

    if done:
        break

final_score = grade(state)

print("\n✅ SIMULATION COMPLETE")
print("Total Reward:", round(total_reward,2))
print("Final Score:", round(final_score,2))