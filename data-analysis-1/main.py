import pandas as pd

INPUT_LOCATION = "data/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv"
OUTPUT_LOCATION = "squirrel_count.csv"


def main():
    # Solution 1
    data = pd.read_csv(INPUT_LOCATION)
    # result = [{"Fur Color": "black", "Count": 0}, {"Fur Color": "gray", "Count": 0}, {"Fur Color": "red", "Count": 0}]
    #
    # colors = data["Primary Fur Color"].dropna().tolist()
    #
    # for color in colors:
    #     if color == "Black":
    #         result[0]["Count"] += 1
    #     if color == "Gray":
    #         result[1]["Count"] += 1
    #     if color == "Gray":
    #         result[2]["Count"] += 1
    #
    # pandas.DataFrame(result).to_csv(OUTPUT_LOCATION)

    # # Solution 1 (Optimal implementation)
    black_squirrel_count = len(data[data["Primary Fur Color"] == "Black"])
    gray_squirrel_count = len(data[data["Primary Fur Color"] == "Gray"])
    red_squirrel_count = len(data[data["Primary Fur Color"] == "Gray"])

    count_table = {
        "Fur Color": ["Black", "Gray", "Red"],
        "Count": [black_squirrel_count, gray_squirrel_count, red_squirrel_count]
    }

    pd.DataFrame(count_table).to_csv(OUTPUT_LOCATION)


if __name__ == '__main__':
    main()
