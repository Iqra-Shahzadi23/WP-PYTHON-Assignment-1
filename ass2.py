import requests
from datetime import datetime


# Function to fetch data from API
def fetch_cat_fact():
    url = "https://catfact.ninja/fact"

    try:
        response = requests.get(url)

        # Raise error if request fails
        response.raise_for_status()

        # Convert JSON to Python dictionary
        data = response.json()

        return data

    except requests.exceptions.RequestException as e:
        print("Error:", e)
        return None


# Function to display information
def display_fact(data):
    print("\n========== Daily Digest ==========")
    print("Date :", datetime.now().strftime("%Y-%m-%d"))
    print("API  : Cat Fact API")
    print("Fact :", data["fact"])
    print("Length:", data["length"])


# Function to save report
def save_report(data):
    with open("daily_report.txt", "w") as file:
        file.write("========== Daily Report ==========\n")
        file.write(f"Date: {datetime.now().strftime('%Y-%m-%d')}\n")
        file.write("API Name: Cat Fact API\n")
        file.write(f"Fact: {data['fact']}\n")
        file.write(f"Length: {data['length']} characters\n")

    print("\nReport saved as 'daily_report.txt'")


# Main function
def main():

    data = fetch_cat_fact()

    if data:
        display_fact(data)
        save_report(data)


# Start Program
main()