PLACEHOLDER = "[name]"
INPUT_LETTER_LOCATION = "./Input/Letters/starting_letter.txt"
INPUT_NAMES_LOCATION = "./Input/Names/invited_names.txt"
OUTPUT_LETTER_BASE_LOCATION = "./Output/ReadyToSend"


def main():

    # Read the generic letter and store it in a list
    with open(INPUT_LETTER_LOCATION) as file:
        generic_letter = file.read()

    # Read the "invited names" and store them in another list
    with open(INPUT_NAMES_LOCATION) as file:
        names_list = file.readlines()

    # Go through the names list and use each name to replace the name placeholder inside the generic letter
    actual_letter = []
    for i in range(len(names_list)):
        name = names_list[i].strip()
        actual_letter.append(generic_letter.replace(PLACEHOLDER, name))
        with open(OUTPUT_LETTER_BASE_LOCATION + f"/letter_for_{name}.txt", "w") as file:
            file.write(actual_letter[i])


if __name__ == '__main__':
    main()
