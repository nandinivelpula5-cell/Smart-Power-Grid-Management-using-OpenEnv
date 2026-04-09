def grade(state):
    total = len(state.areas)
    powered = sum(1 for a in state.areas if a.has_power)

    # ⚡ Power restoration score
    power_score = powered / total

    # ⚠️ Penalty for complaints (more complaints → lower score)
    complaint_penalty = state.complaints * 0.03

    # ⏱ Time efficiency bonus (faster completion → better score)
    time_bonus = max(0, 0.2 - state.time * 0.01)

    # 🎯 Final score calculation
    score = power_score - complaint_penalty + time_bonus

    # 🔒 Clamp between 0 and 1
    return max(0.0, min(1.0, score))