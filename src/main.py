from training import train, init, transform_to_str


def run():
    print("SOLDIERS SIMULATOR 0.1v")
    print("PRESS CTRL+C OR CTRL+D TO QUIT")
    soldiers_state = init()
    try:
        while True:
            order: str = input("We are waiting for orders, commander! >>> ")
            print(f"the commander says: {order!r}")
            soldiers_state = train(order, soldiers_state)
            print("I report the result of the order:")
            str_soldiers = transform_to_str(soldiers_state)
            print(str_soldiers)
    except (KeyboardInterrupt, EOFError):
        print()
        print("Goodbye commander!")


if __name__ == "__main__":
    run()
