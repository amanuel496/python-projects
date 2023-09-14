import datetime
import requests
import env

NUTRITIONIX_API_ENDPOINT = env.NUTRITIONIX_API_ENDPOINT
APP_ID = env.APP_ID
APP_KEY = env.APP_KEY
SHEETY_ENDPOINT = env.SHEETY_ENDPOINT
BEARER = env.BEARER


def main():
    headers = {
        "x-app-id": APP_ID,
        "x-app-key": APP_KEY,
        "Content-Type": "application/json"
    }

    nutritionix_req_body = {
        "query": input("Tell me which exercise you did: "), # Example user input: Ran 5k and cycled for 20 minutes
        "gender": "male",
        "weight_kg": 79,
        "height_cm": 172,
        "age": 28
    }

    nutritionix_response = requests.post(url=NUTRITIONIX_API_ENDPOINT, json=nutritionix_req_body, headers=headers)
    # print(nutritionix_response.raise_for_status())

    exercise_data = nutritionix_response.json()["exercises"]
    exercises = []
    for exercise in exercise_data:
        ex = {
            "name": exercise["name"],
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }

        exercises.append(ex)

    sheety_headers = {
        "Authorization": BEARER,
        "Content-Type": "application/json"
    }

    today = datetime.datetime.now()
    date = today.date().strftime("%d/%m/%Y")
    time_now = today.time().strftime("%H:%M:%S")
    for exercise in exercises:
        sheety_body = {
            "workout": {
                "date": date,
                "time": time_now,
                "exercise": exercise["name"].title(),
                "duration": exercise["duration"],
                "calories": exercise["calories"]
            }
        }
        sheety_response = requests.post(url=SHEETY_ENDPOINT, json=sheety_body, headers=sheety_headers)
        print(sheety_response.raise_for_status())


if __name__ == '__main__':
    main()
