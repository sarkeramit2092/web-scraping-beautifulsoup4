# JSON - JavaScript Object Notation

## What is JSON?
- **Text Format**: Used for storing and transporting data.
- **Self-descriptive** and easy to understand.
- **Used for data exchange** between computers.
- **Language-independent**.

### Example:
```json
{"name": "John", "age": 25, "height": 6}
```

## Parsing JSON
Parsing means converting a JSON string into a JavaScript object for better readability and manipulation.

---

## Handling JSON Data in Python
Python provides a built-in `json` module to handle JSON data.

### Example: JSON in Python
```python
import json

myDict = {
    "people": [
        {"name": "Ben", "age": 23, "height": 5.6},
        {"name": "Bob", "age": 25, "height": 5.6},
        {"name": "Alice", "age": 29, "height": 5.8}
    ]
}
```

### Converting Python Dictionary to JSON String
```python
json_string = json.dumps(myDict)
```

### Writing JSON Data to a File
```python
with open("my_data.json", "w") as f:
    f.write(json_string)
```

---

## Why Use the `requests` Module?
The `requests` module is used for **making HTTP requests**, whereas the `json` module is for **handling JSON data**.

### Fetching JSON Data from an API
```python
import requests

response = requests.get("https://jsonplaceholder.typicode.com/users")
users = response.json()
print(users[0]["name"])
```
**Output:**
```shell
Leanne Graham
```

### Difference Between `json` and `requests`
| Feature | `json` Module | `requests` Module |
|---------|--------------|-------------------|
| Purpose | Handles JSON serialization & deserialization | Sends HTTP requests to fetch/send data |
| Example Usage | `json.loads(json_data)` | `requests.get(url)` |
| Works With | Local JSON files & strings | Web APIs (REST APIs) |
| Converts JSON To | Python dictionaries/lists | Python dictionaries using `.json()` |

### Using Both Modules Together
```python
import requests
import json

url = "https://jsonplaceholder.typicode.com/posts"
response = requests.get(url)
data = response.json()

with open("posts.json", "w") as file:
    json.dump(data, file, indent=4)
```

---

## Summary
- `requests` is for **making web requests (APIs, web scraping)**.
- `json` is for **handling JSON data (parsing, writing, converting)**.
- **They are often used together when working with web APIs.**

