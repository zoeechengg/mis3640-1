import webbrowser


def calculate_bmi(weight, height):
    bmi = 703 * weight / (height * height)
    if bmi <= 18.5:
        print(f"your bmi is {bmi:.1f}. You are underweighted.")
        webbrowser.open("https://www.mcdonalds.com/us/en-us.html")
    # elif bmi > 18.5 and bmi <= 25:
    elif 18.5 < bmi <= 25:
        print(f"your bmi is {bmi:.1f}. You are normal-weighted.")
    elif 25 < bmi < 30:
        print(f"your bmi is {bmi:.1f}. You are overweighted.")
    else:
        print(f"your bmi is {bmi:.1f}. You are obese.")


def main():
    weight = input("Enter your weight: ")
    height = input("Enter your height: ")
    weight = float(weight)
    height = float(height)

    calculate_bmi(weight, height)


if __name__ == "__main__":
    main()
