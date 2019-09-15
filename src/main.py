from training import train


def run():
    soldiers_state = [
        [" ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " "],
        [" ", " ", "↑", "↑", "↑", " ", " "],
        [" ", " ", "↑", "↑", "↑", " ", " "],
        [" ", " ", "↑", "↑", "↑", " ", " "],
        [" ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " "]
    ]
    while True:
        order: str = input("We are waiting for orders, commander!")
        print(f"the commander says {order}")
        soldiers_state = train(order, soldiers_state)
        print("I report the result of the order")
        print(*soldiers_state, sep="\n")


if __name__ == "__main__":
    run()
