from typing import List, Union

STATE = List[List[str]]

def init() -> STATE:
    return [
        [" ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " "],
        [" ", " ", "↑", "↑", "↑", " ", " "],
        [" ", " ", "↑", "↑", "↑", " ", " "],
        [" ", " ", "↑", "↑", "↑", " ", " "],
        [" ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " "],
    ]


def train(command: str, soldiers: STATE) -> STATE:
    return soldiers


def transform_to_str(soldiers: STATE) -> str:
    return "\n".join(str(row) for row in soldiers)
