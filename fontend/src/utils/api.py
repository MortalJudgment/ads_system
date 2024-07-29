import requests

API_URL = "http://localhost:8000"

def login_user(email, password):
    response = requests.post(f"{API_URL}/token", data={"username": email, "password": password})
    if response.status_code == 200:
        return "Login successful"
    else:
        return "Login failed"

def update_user_interests(user_id, interests):
    response = requests.post(f"{API_URL}/users/{user_id}/interests", json={"interests": interests})
    if response.status_code == 200:
        return "Interests updated successfully"
    else:
        return "Failed to update interests"

def send_message_to_agents(user_id, message):
    response = requests.post(f"{API_URL}/chat", json={"user_id": user_id, "message": message})
    if response.status_code == 200:
        return response.json()["response"]
    else:
        return "Failed to get response from agents"

def get_ads_for_user(user_id):
    response = requests.get(f"{API_URL}/ads/{user_id}")
    if response.status_code == 200:
        return response.json()
    else:
        return {}
    


def authenticate_user(name, age, email, interests):
    # Implement user authentication logic here
    # This could involve making a request to your backend API
    return True  # Placeholder

def get_ads(chat_history):
    # Implement logic to fetch ads based on chat history
    # This could involve making a request to your backend API
    return "New ads based on chat history"  # Placeholder