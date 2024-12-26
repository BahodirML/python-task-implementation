Overview

This project includes a Python implementation that addresses several tasks, including data storage, word frequency analysis, polygon collision detection, and file/directory operations. It also integrates logging to track actions and follows PEP 8 standards.

Features

Data Storage:

Add, retrieve, delete, and list key-value pairs.

Top-K Frequent Words:

Analyze a text to find the top-k most frequent words, ignoring punctuation and case sensitivity.

Polygon Collision Detection:

Determine if two polygons collide based on their vertices.

File and Directory Operations:

Copy a source directory to a target directory.

Process files in a directory with specific extensions and count the number of lines in each file.

Logging:

Logs all actions performed in the program into an app.log file for traceability.

File Structure

main.py: Contains the complete implementation of all features.

app.log: A log file that records actions performed by the program.

How to Use

Prerequisites

Python 3.8 or higher.

Required libraries: os, shutil, collections, logging, datetime, typing.

Steps

Clone the repository or copy the code to your local machine.

Run the main.py script to execute the features.

Modify the input text, polygons, or directory paths in the main block as needed.

Example Usage

Data Storage

storage = DataStorage()
storage.add("key1", "value1")
print(storage.get("key1"))
storage.delete("key1")
print(storage.list())

Top-K Frequent Words

text = "Hello world! Hello everyone. This is a simple test. Test, test, hello."
k = 2
print(find_top_k_frequent_words(text, k))

Polygon Collision Detection

polygon1 = [(0, 0), (4, 0), (4, 4), (0, 4)]
polygon2 = [(2, 2), (6, 2), (6, 6), (2, 6)]
print(check_polygon_collision(polygon1, polygon2)) # Output: True

File and Directory Operations

file_processor = FileProcessor()
source_dir = "/path/to/source"
target_dir = "/path/to/target"
file_processor.copy_directory(source_dir, target_dir)

directory = "/path/to/directory"
extensions = [".txt", ".log"]
print(file_processor.process_files(directory, extensions))

Logging Format

All actions performed are logged in app.log with the following format:

[YYYY-MM-DD HH:MM:SS] ACTION: Description of the action

Git Integration

Initialize a local Git repository.

Commit the following four components as separate commits:

Implementation of the DataStorage class.

Implementation of the find_top_k_frequent_words function.

Implementation of the polygon collision detection function.

Implementation of the FileProcessor class.

Requirements

Follow PEP 8 standards.

Include minimal comments to explain the logic.

Ensure the application is modular and easy to extend.
