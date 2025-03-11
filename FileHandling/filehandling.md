# File Handling in Python

Python provides built-in functions to work with files. The `open()` function is used to open files, and different modes allow reading, writing, and modifying files.

## Opening a File

```python
f = open("filename.txt", "mode")
```

## File Open Modes

| Mode | Description |
|------|-------------|
| `"r"` | Read mode (default). Opens the file for reading. Fails if the file does not exist. |
| `"w"` | Write mode. Creates a new file or overwrites an existing file. |
| `"x"` | Exclusive creation mode. Fails if the file exists. |
| `"a"` | Append mode. Adds data to an existing file without overwriting. |
| `"b"` | Binary mode. Used for non-text files (e.g., images, videos). |
| `"t"` | Text mode (default). Used for text files. |
| `"+"` | Read and write mode. |

---

## Writing to a File

```python
with open("test.txt", "w") as f:
    f.write("Hello, this is a test file.")
```

### Appending to a File
```python
with open("test.txt", "a") as f:
    f.write("\nAppending more text.")
```

## Reading a File

### Reading the Entire File
```python
with open("test.txt", "r") as f:
    content = f.read()
    print(content)
```

### Reading Line by Line
```python
with open("test.txt", "r") as f:
    for line in f:
        print(line.strip())
```

### Reading a Specific Number of Characters
```python
with open("test.txt", "r") as f:
    print(f.read(10))  # Reads first 10 characters
```

---

## Checking If a File Exists Before Opening
```python
import os

if os.path.exists("test.txt"):
    with open("test.txt", "r") as f:
        print(f.read())
else:
    print("File does not exist.")
```

---

## Deleting a File

```python
import os

if os.path.exists("test.txt"):
    os.remove("test.txt")
    print("File deleted.")
else:
    print("File not found.")
```

---

## Why Use `os` in File Handling?

Using the `os` module in Python is essential for file handling beyond just reading and writing. It provides functions to interact with the operating system, such as checking file existence, deleting files, renaming them, and working with directories.

### **1. Check if a File Exists Before Reading/Writing**
```python
import os

if os.path.exists("test.txt"):
    with open("test.txt", "r") as f:
        print(f.read())
else:
    print("File does not exist.")
```

### **2. Delete a File**
```python
import os

if os.path.exists("test.txt"):
    os.remove("test.txt")
    print("File deleted.")
else:
    print("File not found.")
```

### **3. Get File Metadata (Size, Path, etc.)**
```python
import os

file = "test.txt"

if os.path.exists(file):
    print(f"File Size: {os.path.getsize(file)} bytes")
    print(f"Absolute Path: {os.path.abspath(file)}")
```

### **4. Create and Remove Directories**
```python
import os

os.mkdir("new_folder")  # Creates a folder
os.rmdir("new_folder")  # Removes an empty folder
```

### **5. List Files in a Directory**
```python
import os

files = os.listdir(".")  # Lists files in the current directory
print(files)
```

### **When Not to Use `os`**
- For basic file read/write operations (`open()` is sufficient).
- When working with file paths, prefer `pathlib` (introduced in Python 3.4) over `os.path`.

---

## Best Practices
- Always use `with open()` to avoid leaving files open.
- Use `try-except` to handle file errors.
- Check if a file exists before trying to read or delete it.
- Use the correct mode (`"w"`, `"a"`, `"r"`, etc.) depending on your needs.

---

### Example: Full File Handling Script
```python
import os

def file_operations():
    filename = "example.txt"
    
    # Write to file
    with open(filename, "w") as f:
        f.write("This is an example file.\n")
    
    # Append text
    with open(filename, "a") as f:
        f.write("Appending new data.\n")
    
    # Read file
    with open(filename, "r") as f:
        print(f.read())
    
    # Delete file
    if os.path.exists(filename):
        os.remove(filename)
        print("File deleted.")
    else:
        print("File not found.")

file_operations()
```

---

This guide provides an overview of Python file handling. Practice and experiment with different modes to gain a better understanding. 🚀

