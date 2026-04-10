from fastapi import FastAPI, Request
from env import PowerCutEnv

app = FastAPI()
env = PowerCutEnv()

@app.post("/reset")
def reset():
    return env.reset()

@app.post("/step")
async def step(request: Request):
    data = await request.json()
    action = data.get("action", 0)

    state, reward, done = env.step(action)

    return {"state": state, "reward": reward, "done": done}
