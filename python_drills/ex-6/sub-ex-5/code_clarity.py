# code_clarity.py

# Constants
MAX_RETRIES = 3
TIMEOUT = 5

def calculate_score(score: int, attempts: int) -> int:
    """
    Calculate the final score based on the number of attempts.
    If too many attempts, return a penalty score.
    """
    if attempts > MAX_RETRIES:
        return score - 10  # penalty for exceeding max retries
    return score

def is_valid_user(user_id: int) -> bool:
    """
    Check if the user is valid based on the user_id.
    """
    # For simplicity, assume user_id should be positive
    return user_id > 0

def process_data(data: list) -> list:
    """
    Process data, remove None values, and return cleaned data.
    """
    cleaned_data = []
    for item in data:
        if item is not None:
            cleaned_data.append(item)
    return cleaned_data

def fetch_data_from_server(url: str) -> dict:
    """
    Fetch data from a server and return the response in dictionary form.
    """
    response = {
        "status": "success",
        "data": {"username": "user123", "score": 100}
    }
    return response

def main():
    # Example usage of functions
    score = 80
    attempts = 5
    final_score = calculate_score(score, attempts)
    print(f"Final Score: {final_score}")

    user_id = 123
    if is_valid_user(user_id):
        print(f"User {user_id} is valid.")
    else:
        print(f"User {user_id} is not valid.")

    raw_data = [1, None, 3, 4, None, 6]
    cleaned_data = process_data(raw_data)
    print(f"Cleaned Data: {cleaned_data}")

    server_data = fetch_data_from_server("https://example.com")
    print(f"Server Response: {server_data['data']}")

if __name__ == "__main__":
    main()
