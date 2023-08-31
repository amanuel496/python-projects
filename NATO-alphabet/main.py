import pandas as pd


def main():
    data = pd.read_csv("nato_phonetic_alphabet.csv")
    data_dict = {}
    for (index, row) in data.iterrows():
        data_dict[row.letter] = row.code

    while True:
        name = input("Enter a word or enter Q to quit: ").upper()
        if name == "Q":
            break
        try:
            phonetic_code = [data_dict[letter] for letter in name]
        except KeyError:
            print("Sorry, only letters in the alphabet please.")
        else:
            print(phonetic_code)


if __name__ == "__main__":
    main()
