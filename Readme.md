# RestAPI - Project

## Cat Facts API Test Cases
This repository contains test cases for the Cat Facts API available at Cat Facts API. The tests are written in Python and utilize the requests library for sending HTTP requests.


## Prerequisites
- Python 3.x
- requests library (can be installed using pip install requests)

Running the Tests
To run the tests, simply execute the Python scripts.
For example, to run the test for retrieving a random cat fact:

##### _python test_get_random_cat_fact.py_

Test Case 1: Retrieve a Random Fact

| **Step**|                **Action**               |                **Expected Result**                            |
|-----|:----------------------------------------------:|:----------------------------------------------------------:|
| 1   |       Send GET request to /facts/random        |       The API returns a response with status code 200      |
| 2   |         Validate response status code          |    Status code is 200                                      |
| 3   |         Validate response content type         |  Content-Type header is application/json; charset=utf-8    |
| 4   |              Parse JSON response               |  The response is a valid JSON                              |
| 5   | Validate presence of text key in JSON response |  The text key is present in the JSON response              |
| 6   |  Validate that text key is a non-empty string  |  The text key is a non-empty string                        |

Test Case 2: Retrieve Two Random Cat Fact

| **Step** |                         **Action**                         |                               **Expected Result**                        |
|----------|:----------------------------------------------------------:|:-------------------------------------------------------------------------|
| 1        | Send GET request to /facts/random?animal_type=cat&amount=2 |                 The API returns a response with status code 200          |
| 2        |               Validate response status code                |                                Status code is 200                        |
| 3        |               Validate response content type               |              Content-Type header is application/json; charset=utf-8      |
| 4        |                    Parse JSON response                     |                           The response is a valid JSON                   |
| 5        |    Validate that JSON response is an array                 |                             The response is an array                     |
| 6        |                   Validate array length                    |                     The array contains exactly two elements              |
| 7        |      Validate presence of keys in each array element       | Each element contains _id, __v, text, updatedAt, deleted, source, sentCount keys |
| 8        |       Validate types of values in each array element       |         Each key has the correct type (e.g., text is a non-empty string) |