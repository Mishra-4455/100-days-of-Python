from datetime import datetime
import os
import json
import requests
from zoneinfo import ZoneInfo

API_KEY = os.environ["AI_API_KEY"]

URL = "https://api.groq.com/openai/v1/chat/completions"
sheets_url = "https://api.sheety.co/3efbc19396a16c03f085b60fc87c3e5b/myWorkouts/workouts"

SYSTEM_PROMPT = """
You are an exercise data extraction and calorie estimation assistant.

Analyze the user's sentence and identify every exercise performed.

Return a JSON array containing one dictionary per exercise.

Each dictionary must contain exactly these keys:
- Exercise: name of the exercise, as a string
- Duration: duration in minutes, as a number
- Calories: estimated calories burned, as a number

RULES:
1. Create separate entries for multiple exercises.
2. If only a running distance is given, estimate duration
   using an average running pace and calculate calories.
3. If only duration is given, estimate distance at an
   average pace appropriate for the exercise and calculate calories.
4. If both distance and duration are given, use both.
5. Estimate missing values using reasonable assumptions for
   an average adult weighing approximately 70 kg.
6. Calculate the estimates yourself.
7. Duration must be a number in minutes, without units.
8. Calories must be a number, not a string.
9. Do not include distance as an additional dictionary key.
10. Return a JSON object with a single key named "exercises".
    The value of "exercises" must be an array containing one
    dictionary per exercise.
    Do not return the array directly at the top level.
    Do not include markdown or explanations.
11. If no exercise can be identified, return an empty array.
"""

user_input = input("Describe your exercise: ")

llm_data = {
    "model": "openai/gpt-oss-120b",
    "messages": [
        {
            "role": "system",
            "content": SYSTEM_PROMPT
        },
        {
            "role": "user",
            "content": user_input
        }
    ],
    "temperature": 0.2
}

llm_headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

current = datetime.now(ZoneInfo("Asia/Kolkata"))
current_date = current.strftime("%d/%m/%Y")
current_time = current.strftime("%H:%M:%S")

exercises = []

try:
    response = requests.post(
        URL,
        headers=llm_headers,
        json=llm_data,
        timeout=60
    )

    if not response.ok:
        print("Status code:", response.status_code)
        print("Error details:", response.text)
    else:
        response_data = response.json()
        content = response_data["choices"][0]["message"]["content"]

        result = json.loads(content)
        exercises = result["exercises"]

except requests.exceptions.RequestException as error:
    print("Request failed:", error)

for exercise in exercises:
    sheets_input = {
        "workout": {
            "date" : current_date,
            "time" : current_time,
            "exercise" : exercise["Exercise"],
            "duration" : exercise["Duration"],
            "calories" : exercise["Calories"]
        }
    }
    sheets_response = requests.post(sheets_url, json=sheets_input)
    print(sheets_response.text)