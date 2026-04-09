from fastapi import FastAPI
from env import PowerCutEnv

app = FastAPI()

env = PowerCutEnv()

@app.post("/reset")
def reset():
    state = env.reset()
    return {"state": state}

@app.post("/step")
def step(action: int):
    state, reward, done = env.step(action)
    return {
        "state": state,
        "reward": reward,
        "done": done
    }

@app.get("/state")
def get_state():
    return {"state": env.state()}
