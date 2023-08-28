import pandas

INPUT_LOCATION = "data/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv"
OUTPUT_LOCATION = "squirrel_count.csv"


def main():
    data = pandas.read_csv(INPUT_LOCATION)
    result = [{"Fur Color": "black", "Count": 0}, {"Fur Color": "gray", "Count": 0}, {"Fur Color": "red", "Count": 0}]

    colors = data["Primary Fur Color"].dropna().tolist()

    for color in colors:
        if color == "Black":
            result[0]["Count"] += 1
        if color == "Gray":
            result[1]["Count"] += 1
        if color == "Cinnamon":
            result[2]["Count"] += 1

    pandas.DataFrame(result).to_csv(OUTPUT_LOCATION)


if __name__ == '__main__':
    main()
