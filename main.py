import random


def main():
    print("Enter news headline: ")
    n = input()
    rand = random.randint(0, 100)

    if rand > 50:
        print("Increase")
    elif rand < 50:
        print("Decrease")
    else:
        print("Neutral")


if __name__ == "__main__":
    main()
