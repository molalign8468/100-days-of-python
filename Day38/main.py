import os
import requests
from dotenv import load_dotenv
from datetime import datetime
load_dotenv()

NUTRITIONIX_APP_ID = os.environ.get("NUTRITION_APP_ID")
NUTRITIONIX_API_KEY = os.environ.get("NUTRITION_API_KEY")
SHEETY_SECRET = os.environ.get("SECRET") 

NUTRITIONIX_EXERCISE_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEETY_ENDPOINT = "https://api.sheety.co/21bf6521e405f3a9823fecb48370630d/workoutTracking/workouts"

NUTRITIONIX_HEADERS = {
    "x-app-id": NUTRITIONIX_APP_ID,
    "x-app-key": NUTRITIONIX_API_KEY,
}

SHEETY_HEADERS = {
    "Authorization": f"Bearer {SHEETY_SECRET}"
}


def get_exercise_data(query):
    """Fetches exercise data from the Nutritionix API."""
    params = {
        "query": query,
    }

    try:
        response = requests.post(
            url=NUTRITIONIX_EXERCISE_ENDPOINT,
            json=params,
            headers=NUTRITIONIX_HEADERS
        )
        response.raise_for_status()
        return response.json()["exercises"]
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from Nutritionix API: {e}")
        return None

def log_workouts_to_sheety(exercise_list):
    """Logs a list of exercises to the Sheety Google Sheet."""
    if not exercise_list:
        print("No exercises to log.")
        return

    now = datetime.now()
    date = now.strftime("%d/%m/%Y")
    time = now.strftime("%H:%M:%S")

    for exercise in exercise_list:
        body = {
            "workout": {
                "date": date,
                "time": time,
                "exercise": exercise["name"].title(),
                "duration": exercise["duration_min"],
                "calories": exercise["nf_calories"]
            }
        }
        
        try:
            sheety_response = requests.post(
                url=SHEETY_ENDPOINT,
                headers=SHEETY_HEADERS,
                json=body
            )
            sheety_response.raise_for_status()
            print("Successfully logged workout to Sheety.")
        except requests.exceptions.RequestException as e:
            print(f"Error logging workout to Sheety: {e}")


if __name__ == "__main__":
    exercise_input = input("Tell me which exercise you did: ")
    
    exercise_data = get_exercise_data(exercise_input)
    
    if exercise_data:
        log_workouts_to_sheety(exercise_data)
    else:
        print("Could not retrieve exercise data. Aborting.")