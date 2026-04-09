# ⚡ Smart Power Grid OpenEnv

## Description
This project simulates a real-world power distribution system where an agent manages power outages.

## Observation Space
- areas: list of area power states
- complaints: number of complaints
- time: timestep

## Action Space
- restore(area_id)
- ignore()

## Reward Function
- +0.3 for restoring power
- +0.4 bonus for high priority areas
- -penalty for complaints

## Tasks
- easy → 3 areas
- medium → 5 areas
- hard → 10 areas

## How to Run

pip install flask  
python baseline/run_agent.py