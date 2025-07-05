
def tinhTong():
    sum = 0;
    with open("data71.txt", "r") as file:
        for line in file:
            line = line.strip()
            try:
                sum += float(line)
            except ValueError:
                pass 

    return sum


def main():
    sum = tinhTong()
    with open("data71.txt", "a") as file:
        file.write(f"{sum}\n")

if __name__ == "__main__":
    main()




