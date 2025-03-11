# JSON - JavaScript Object Notation

Text Format : Storing and transporting data.
Self describing and easy to understand.
JSON is used to send data between computers.
JSON is language independent.
Example:

Key-value pairs:
'{"name": "John", "age": 25, "height": 6}'

Parse the JSON to a JavaScript object. Readability increases.

Let me know if you need any modifications or further assistance! 🚀

# what is parse meaning?

The word "parse" means to analyze and convert data into a structured format that can be understood and used by a program.

In programming, parsing refers to the process of taking a string (such as JSON, XML, or HTML) and converting it into a usable object or data structure.

For example, in JavaScript, we use JSON.parse() to convert a JSON string into a JavaScript object:


Here, JSON.parse() takes the JSON string and parses it into an object so that we can access its properties easily.

==========================================================================================================
myDict = {
    "people": [
        {
            "name": "Ben",
            "age": 23,
            "height": 5.6
        },
        {
            "name": "Bob",
            "age": 25,
            "height": 5.6
        },
        {
            "name": "Alice",
            "age": 29,
            "height": 5.8
        }
    ]
}
Now, the dictionary can be used in Python.

# loads and dumps
json_string = json.dumps(myDict)
with open("my_data.json","w") as f:
f.write(json_string)

You're working with Python's json module to serialize and store your dictionary (myDict) into a JSON file. Below is a complete explanation and correction of your code using json.dumps() and json.loads().

1️⃣ Explanation of dumps() and loads()
json.dumps(obj) → Converts a Python object (dictionary, list, etc.) into a JSON string.
json.loads(json_string) → Converts a JSON string back into a Python object.
Writing to a file (dump) → Use json.dump(obj, file, indent=4) to write JSON directly to a file.
Reading from a file (load) → Use json.load(file) to read JSON directly from a file.

2️⃣ Corrected Code

# Define dictionary
myDict = {
    "people": [
        {"name": "Ben", "age": 23, "height": 5.6},
        {"name": "Bob", "age": 25, "height": 5.6},
        {"name": "Alice", "age": 29, "height": 5.8}
    ]
}

# Convert Python dictionary to a JSON string
json_string = json.dumps(myDict, indent=4)  # Pretty print with indentation

# Write JSON string to a file
with open("my_data.json", "w") as f:
    f.write(json_string)  # Alternatively, use json.dump(myDict, f, indent=4)

print("JSON file saved successfully!")

# Read JSON file and convert back to a Python dictionary
with open("my_data.json", "r") as f:
    data = json.load(f)  # Use json.load() to read and parse JSON from a file

print("Data loaded from JSON file:", data)

3️⃣ Key Points
✅ json.dumps() converts a dictionary to a JSON string.
✅ json.dump(obj, file) writes JSON directly to a file (no need for .write()).
✅ json.loads(json_string) converts a JSON string back to a Python object.
✅ json.load(file) reads a JSON file and converts it into a Python object.


# f.write(json_string)

The line f.write(json_string) writes the JSON string to a file. However, a more Pythonic way to write JSON to a file is to use json.dump(), which directly writes the dictionary to the file in JSON format.

# To handle json data in Python, we use the json built-in library.

Yes, in Python, we use the built-in json module to handle JSON data. This module provides functions to encode (serialize) and decode (deserialize) JSON data.

🔹 Key Functions in the json Module
✅ 1. Convert Python Dictionary to JSON (Serialization)
We use json.dumps() to convert a Python dictionary to a JSON string.

import json

data = {"name": "Alice", "age": 25, "city": "New York"}

# Convert dictionary to JSON string
json_string = json.dumps(data, indent=4)  # 'indent' makes JSON readable
print(json_string)

📌 Output (Formatted JSON)

{
    "name": "Alice",
    "age": 25,
    "city": "New York"
}
✅ 2. Convert JSON String to Python Dictionary (Deserialization)
We use json.loads() to convert a JSON string into a Python dictionary.

# JSON string
json_data = '{"name": "Bob", "age": 30, "city": "London"}'

# Convert JSON string to Python dictionary
python_dict = json.loads(json_data)
print(python_dict["name"])  # Output: Bob

✅ 3. Write JSON Data to a File (json.dump())
Instead of writing a JSON string manually, use json.dump() to save JSON data to a file.

myDict = {"name": "Alice", "age": 29, "height": 5.8}

with open("data.json", "w") as file:
    json.dump(myDict, file, indent=4)  # Writes JSON data with indentation

✅ 4. Read JSON Data from a File (json.load())
To read JSON data from a file and convert it into a Python dictionary, use json.load().

with open("data.json", "r") as file:
    loaded_data = json.load(file)

print(loaded_data)  # Output: {'name': 'Alice', 'age': 29, 'height': 5.8}

# Summary of json Functions

json.dumps(obj, indent=4)	Converts Python object to a JSON string
json.loads(json_string)	Converts JSON string to a Python dictionary
json.dump(obj, file, indent=4)	Writes JSON data to a file
json.load(file)	Reads JSON data from a file



# The requests module in Python is used for making HTTP requests, whereas the json module is used for handling JSON data.

# Why Use the requests Module?
The requests module allows us to send HTTP requests (GET, POST, PUT, DELETE) to web servers and interact with APIs that return data in JSON format.

🚀 Example: Fetching JSON Data from an API
Let's say you want to get data from a public API.

import requests

# Send a GET request to an API
response = requests.get("https://jsonplaceholder.typicode.com/users")

# Convert the response JSON data to a Python list
users = response.json()

# Print first user’s name
print(users[0]["name"])
✅ Output:
Leanne Graham

🔹 Difference Between json and requests
Feature	json Module	requests Module
Purpose	Handles JSON serialization & deserialization	Sends HTTP requests to fetch or send data
Example Usage	json.loads(json_data)	requests.get(url)
Works With	Local JSON files & strings	Web APIs (REST APIs)
Converts JSON To	Python dictionaries/lists	Python dictionaries using .json()

🔹 When to Use Which?
Use requests when fetching data from a web API.
Use json when parsing or writing JSON data.

# Using Both Together

import requests
import json

url = "https://jsonplaceholder.typicode.com/posts"
response = requests.get(url)

# Convert response to Python dictionary
data = response.json()

# Save the response to a JSON file
with open("posts.json", "w") as file:
    json.dump(data, file, indent=4)
This fetches data from an API and saves it as a JSON file.

🚀 Summary
requests is for making web requests (APIs, web scraping)
json is for handling JSON data (parsing, writing, converting)
They are often used together when working with web APIs.