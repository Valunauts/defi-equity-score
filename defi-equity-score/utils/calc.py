import numpy as np

def gini(array):
    array = np.array(array)
    array = array.flatten()
    if np.amin(array) < 0:
        array -= np.amin(array)
    array += 0.0000001  # Avoid zero division
    array = np.sort(array)
    index = np.arange(1, array.shape[0] + 1)
    n = array.shape[0]
    return ((np.sum((2 * index - n - 1) * array)) / (n * np.sum(array)))

def calculate_equity_score(data, alpha=0.6, gamma=2):
    rewards = [w["reward"] for w in data["wallets"]]
    assets = [w["asset"] for w in data["wallets"]]
    base_access_score = data.get("base_access_score", 1)
    reward_fairness_score = data.get("reward_fairness_score", 1)
    participation_inclusive_score = data.get("participation_inclusive_score", 1)
    top10_share = sum(sorted(rewards, reverse=True)[:10]) / (sum(rewards) + 0.0001)
    ineq_penalty = gini(assets)
    low_asset_pct = len([a for a in assets if a < 100]) / len(assets)
    score = (
        base_access_score
        + reward_fairness_score
        + participation_inclusive_score
        - alpha * (top10_share ** 2)
        - ineq_penalty
        + gamma * np.log1p(low_asset_pct)
    )
    return round(score, 4)
