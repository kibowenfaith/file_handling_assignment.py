# file_handling_assignment.py

# File Creation
try:
    with open('my_file.txt', 'w') as f:
        f.write('Hello, world!\n')
        f.write('This is a file handling assignment\n')
        f.write('Created by: Your Name\n')
except Exception as e:
    print(f"Error creating file: {e}")

# File Reading and Display
try:
    with open('my_file.txt', 'r') as f:
        print(f.read())
except Exception as e:
    print(f"Error reading file: {e}")

# File Appending
try:
    with open('my_file.txt', 'a') as f:
        f.write('This is a new line added in append mode\n')
        f.write('This is another line added in append mode\n')
        f.write('This is the last line added in append mode\n')
except Exception as e:
    print(f"Error appending to file: {e}")

# Error Handling
try:
    with open('my_file.txt', 'r') as f:
        print(f.read())
except FileNotFoundError:
    print("File not found")
except PermissionError:
    print("Permission denied")
except Exception as e:
    print(f"Unexpected error: {e}")
finally:
    print("File handling complete.")