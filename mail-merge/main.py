def main():

    # Read the generic letter and store it in a list
    with open("./Input/Letters/starting_letter.txt") as file:
        generic_letter = file.read()

    # Read the "invited names" and store them in another list
    with open("./Input/Names/invited_names.txt") as file:
        names_list = file.readlines()

    # Go through the names list and use each name to replace the name placeholder inside the generic letter
    actual_letter = []
    for i in range(len(names_list)):
        name = names_list[i].strip()
        actual_letter.append(generic_letter.replace("[name]", name))
        with open(f"./Output/ReadyToSend/letter_for_{name}.txt", "w") as file:
            file.write(actual_letter[i])


if __name__ == '__main__':
    main()
