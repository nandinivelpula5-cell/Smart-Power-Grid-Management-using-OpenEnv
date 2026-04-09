from dataclasses import dataclass
from typing import List

@dataclass
class Area:
    id: int
    has_power: bool
    priority: int  # 1 (low) to 5 (high)

@dataclass
class State:
    areas: List[Area]
    complaints: int
    time: int