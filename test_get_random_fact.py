import requests


def test_get_random_fact():
    # Step 1: Send GET request to the API endpoint
    response = requests.get('https://cat-fact.herokuapp.com/facts/random')

    # Step 2: Capture the response and validate
    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"
    assert response.headers["Content-Type"] == "application/json; charset=utf-8", "Response is not in JSON format"

    json_response = response.json()
    assert 'text' in json_response, "Response JSON does not contain 'text' key"
    assert isinstance(json_response['text'], str) and len(
        json_response['text']) > 0, "The 'text' key is not a non-empty string"


# Run the test
test_get_random_fact()
