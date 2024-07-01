import requests


def test_get_two_random_cat_facts():
    # Step 1: Send a GET request to the API endpoint
    response = requests.get('https://cat-fact.herokuapp.com/facts/random?animal_type=cat&amount=2')

    # Step 2: Get the answer and validate
    assert response.status_code == 200, f"Expected status code 200, but received {response.status_code}."
    assert response.headers['Content-Type'] == 'application/json; charset=utf-8', "The response is not in JSON format."

    json_response = response.json()
    assert isinstance(json_response, list), "JSON response is not an array"
    assert len(json_response) == 2, "An array does not contain two elements"

    for fact in json_response:
        assert '_id' in fact, "One of the elements of the array does not contain a key '_id'"
        assert '__v' in fact, "One of the elements of the array does not contain a key '__v'"
        assert 'text' in fact, "One of the elements of the array does not contain a key 'text'"
        assert 'updatedAt' in fact, "One of the elements of the array does not contain a key 'updatedAt'"
        assert 'deleted' in fact, "One of the elements of the array does not contain a key 'deleted'"
        assert 'source' in fact, "One of the elements of the array does not contain a key 'source'"
        assert 'sentCount' in fact, "One of the elements of the array does not contain a key 'sentCount'"

        assert isinstance(fact['_id'], str), "Key '_id' is not a string"
        assert isinstance(fact['__v'], int), "Key '__v' is not an integer"
        assert isinstance(fact['text'], str) and len(fact['text']) > 0, "Key 'text' is not a non-empty string"
        assert isinstance(fact['updatedAt'], str), "Key 'updatedAt' is not a string"
        assert isinstance(fact['deleted'], bool), "Key 'deleted' is not a boolean value"
        assert isinstance(fact['source'], str), "Key 'source' is not a string"
        assert isinstance(fact['sentCount'], int), "Key 'sentCount' is not an integer"


# Run the test
test_get_two_random_cat_facts()
