# PythonApiTest

This repo is created to show subjects below:

* Using GET, POST and DELETE for API
* Pytest for generating HTML report.


[Pyhton]: https://www.python.org/
[Pytest]: https://docs.pytest.org/en/6.2.x/getting-started.html
[pytest-html]: https://pypi.org/project/pytest-html/

## How It Works

1. Install **[Pyhton]** to your pc.(Python 3.9.0)
2. Install **[Pytest]** to your pc via pip.
3. Install **[pytest-html]** to your pc.

## Usage
When every instalation is done you use command below for execution the test.

 ```sh
    $ pytest test_api.py --html=./results/report.html 
 ```
## Test Cases
### Task-1
* Set the Content-type=application/json
* Set path “pet”
* Create one pet with the following JSON model
```json
{
"category": {
"id": 0,
"name": "Pets"
},
"name": "Scout",
"photoUrls": [
"scout.png"
],
"tags": [
{
"id": 0,
"name": "pet-dog"
}
],
"status": "available"
}
```
* Verify the below requested in the response
 1. Status code should be 200
 2. Response should has an id
 3. Created name should be equal to the posted name
 4. Content-type should be application/json
 5. Response header should has a date value

### Task-2
* Set the Content-type=application/json
* Set path “pet”
* Set id as a path parameters (You can use the id from the response of the Task-1)
* Retrieve the pet information that you requested
* Verify the response
 1. Status code should be 200
 2. Response body should be equal to the Task-1’s response body
 3. Content-type should be application/json
 4. Response header should has a date value

### Task-3
* Set the Content-type=application/json
* Set path “pet”
* Set id as a path parameters (You can use the id from the response of the Task-2)
* Delete the pet that you searched
* Verify the response
 1. Status code should be 200
 2. Content-type should be application/json
 3. Response body message should equal to id
 4. Message should be equal to “unknown”
