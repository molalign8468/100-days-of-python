import requests
import os
from dotenv import load_dotenv
from datetime import datetime
load_dotenv()

PIXELA_API_ENDPOINT = "https://pixe.la/v1"
PIXELA_TOKEN = os.environ.get("PIXELA_TOKEN")
GRAPH_ID = "graph1"

HEADERS = {
    "X-USER-TOKEN": PIXELA_TOKEN
}


def create_user(username):
    """
    Creates a new user on Pixela.
    Note: A user only needs to be created once.
    """
    if not username or not PIXELA_TOKEN:
        print("Please set USERNAME and PIXELA_TOKEN in your .env file.")
        return

    url = f"{PIXELA_API_ENDPOINT}/users"
    user_params = {
        "token": PIXELA_TOKEN,
        "username": username,
        "agreeTermsOfService": "yes",
        "notMinor": "yes"
    }
    
    try:
        response = requests.post(url=url, json=user_params)
        response.raise_for_status()
        print("User created successfully!")
        print(response.text)
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
        print(response.text)
    except Exception as err:
        print(f"An error occurred: {err}")

def create_graph(username,graph_id, name, unit, graph_type="int", color="shibafu"):
    """
    Creates a new graph for the authenticated user.
    """
    url = f"{PIXELA_API_ENDPOINT}/users/{username}/graphs"
    graph_config = {
        "id": graph_id,
        "name": name,
        "unit": unit,
        "type": graph_type,
        "color": color
    }
    
    try:
        response = requests.post(url=url, json=graph_config, headers=HEADERS)
        response.raise_for_status()
        print(f"Graph created successfully!\n Click to View:  https://pixe.la/v1/users/{username}/graphs/{graph_id}.html")
        print(response.text)
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
        print(response.text)
    except Exception as err:
        print(f"An error occurred: {err}")

def post_pixel(username,graph_id, date, quantity):
    """
    Posts a new pixel to a specified graph.
    """
    url = f"{PIXELA_API_ENDPOINT}/users/{username}/graphs/{graph_id}"
    pixel_data = {
        "date": date.strftime("%Y%m%d"),
        "quantity": str(quantity),
    }
    
    try:
        response = requests.post(url=url, json=pixel_data, headers=HEADERS)
        response.raise_for_status()
        print(f"Pixel posted successfully for {date.strftime('%Y%m%d')}!")
        print(response.text)
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
        print(response.text)
    except Exception as err:
        print(f"An error occurred: {err}")

def update_pixel(username,graph_id, date, new_quantity):
    """
    Updates an existing pixel with a new quantity.
    """
    url = f"{PIXELA_API_ENDPOINT}/users/{username}/graphs/{graph_id}/{date.strftime('%Y%m%d')}"
    update_data = {
        "quantity": str(new_quantity)
    }
    
    try:
        response = requests.put(url=url, json=update_data, headers=HEADERS)
        response.raise_for_status()
        print(f"Pixel for {date.strftime('%Y%m%d')} updated successfully!")
        print(response.text)
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
        print(response.text)
    except Exception as err:
        print(f"An error occurred: {err}")

def delete_pixel(username,graph_id, date):
    """
    Deletes an existing pixel from a graph.
    """
    url = f"{PIXELA_API_ENDPOINT}/users/{username}/graphs/{graph_id}/{date.strftime('%Y%m%d')}"
    
    try:
        response = requests.delete(url=url, headers=HEADERS)
        response.raise_for_status()
        print(f"Pixel for {date.strftime('%Y%m%d')} deleted successfully!")
        print(response.text)
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
        print(response.text)
    except Exception as err:
        print(f"An error occurred: {err}")

# --- Main Execution Block ---
if __name__ == "__main__":
    
    print("\nWelcome to the Pixela CLI. What would you like to do?")
    print("1. Create a new user (one-time)")
    print("2. Create a new graph (one-time)")
    print("3. Post a pixel")
    print("4. Update a pixel")
    print("5. Delete a pixel")
    print("6. Exit")

    while True:
        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            user_name = input("Enter new User name: ")
            create_user(user_name)
        elif choice == '2':
            username = input("Enter you Username: ")
            graph_id = input("Enter new graph ID: ")
            graph_name = input("Enter graph name: ")
            unit_measure = input("Enter unit of measure (e.g., commit, km, hour): ")
            create_graph(username,graph_id=graph_id, name=graph_name, unit=unit_measure)
        elif choice == '3':
            username = input("Enter you Username: ")
            graph_id = input("Enter graph ID: ")
            date_str = input("Enter date (YYYYMMDD) or 'today' for today's date: ")
            if date_str.lower() == 'today':
                date = datetime.now()
            else:
                date = datetime.strptime(date_str, "%Y%m%d")
            quantity = input("Enter quantity for the pixel: ")
            post_pixel(username,graph_id=graph_id, date=date, quantity=quantity)
        elif choice == '4':
            username = input("Enter you Username: ")
            graph_id = input("Enter graph ID: ")
            date_str = input("Enter date (YYYYMMDD) to update: ")
            date = datetime.strptime(date_str, "%Y%m%d")
            new_quantity = input("Enter new quantity for the pixel: ")
            update_pixel(username,graph_id=graph_id, date=date, new_quantity=new_quantity)
        elif choice == '5':
            username = input("Enter you Username: ")
            graph_id = input("Enter graph ID: ")
            date_str = input("Enter date (YYYYMMDD) to delete: ")
            date = datetime.strptime(date_str, "%Y%m%d")
            delete_pixel(username,graph_id=graph_id, date=date)
        elif choice == '6':
            print("Exiting.")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 6.")
            
    print("\nScript finished.")