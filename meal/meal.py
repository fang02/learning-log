def main():
    time = input("What time is it? ")
    time = convert(time)
    if 7 <= time <= 8:
        print("breakfast time")
    elif 12 <= time <= 13:
        print("lunch time") 
    elif 18 <= time <= 19:
        print("dinner time")
    else:
        print("")


def convert(time):
    parts = time.split(":")
    hours = int(parts[0])
    minutes = int(parts[1])
    total_time = hours + minutes / 60
    return total_time


if __name__ == "__main__":
    main()