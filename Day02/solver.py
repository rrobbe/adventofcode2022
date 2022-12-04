data = [line.strip() for line in open('input', 'r')]
mapper = {
    "actions": {
        "Rock": {
            "loser": "Scissors",
            "score": 1,
            "values": ["A", "X"],
            "winner": "Paper",
        },
        "Paper": {
            "loser": "Rock",
            "score": 2,
            "values": ["B", "Y"],
            "winner": "Scissors",
        },
        "Scissors": {
            "loser": "Paper",
            "score": 3,
            "values": ["C", "Z"],
            "winner": "Rock",
        },
    },
    "results": {
        "Lose": {
            "score": 0,
            "values": "X",
        },
        "Draw": {
            "score": 3,
            "values": "Y",
        },
        "Win": {
            "score": 6,
            "values": "Z",
        },
    },
}

score1 = 0
score2 = 0


def determine_from_value(sub, value):
    for key in mapper[sub].keys():
        if value in mapper[sub][key]["values"]:
            value = key
    return value


def calculate_score(result, action):
    score = (
        mapper["results"][result]["score"] + mapper["actions"][action]["score"]
    )
    return score


def calculate_round_score_1(o_action, m_action):
    """
    o_action = opponent's action
    m_action = my action
    """
    if o_action == m_action:
        result = "Draw"
    elif m_action == mapper["actions"][o_action]["winner"]:
        result = "Win"
    else:
        result = "Lose"

    return calculate_score(
        result,
        m_action
    )


def calculate_round_score_2(o_action, d_result):
    """
    o_action = opponent's action
    d_result = desired result
    """
    if d_result == "Draw":
        return calculate_score(
            d_result,
            o_action,
        )
    if d_result == "Win":
        return calculate_score(
            d_result,
            mapper["actions"][o_action]["winner"],
        )
    if d_result == "Lose":
        return calculate_score(
            d_result,
            mapper["actions"][o_action]["loser"],
        )


for round_actions in data:
    opponent_action = determine_from_value("actions", round_actions.split()[0])
    my_action = determine_from_value("actions", round_actions.split()[1])
    desired_result = determine_from_value("results", round_actions.split()[1])

    score1 += calculate_round_score_1(opponent_action, my_action)
    score2 += calculate_round_score_2(opponent_action, desired_result)

print(f"score 1: {score1}")
print(f"score 2: {score2}")
