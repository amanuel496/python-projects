from music_data import get_data


def main():
    user_request = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
    get_data(user_request)


if __name__ == '__main__':
    main()
