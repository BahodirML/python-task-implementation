import os
import shutil
from collections import Counter
import logging
from datetime import datetime
from typing import List, Tuple

logging.basicConfig(
    filename='app.log',
    level=logging.INFO,
    format='%(Y-%m-%d %H:%M:%S) %(message)s'
)

class DataStorage:
    def __init__(self):
        self.data = {}

    def add(self, key, value):
        self.data[key] = value
        logging.info(f"Added key: {key}, value: {value}")

    def get(self, key):
        value = self.data.get(key, None)
        logging.info(f"Retrieved key: {key}, value: {value}")
        return value

    def delete(self, key):
        if key in self.data:
            del self.data[key]
            logging.info(f"Deleted key: {key}")
        else:
            logging.warning(f"Key not found for deletion: {key}")

    def list(self):
        logging.info("Listed all data")
        return self.data

def find_top_k_frequent_words(text, k):
    words = ''.join(c.lower() if c.isalnum() else ' ' for c in text).split()
    counter = Counter(words)
    top_k = counter.most_common(k)
    logging.info(f"Top {k} frequent words: {top_k}")
    return top_k

def check_polygon_collision(polygon1, polygon2):
    def do_lines_intersect(p1, q1, p2, q2):
        def orientation(p, q, r):
            val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
            if val == 0:
                return 0
            return 1 if val > 0 else 2

        def on_segment(p, q, r):
            if min(p[0], r[0]) <= q[0] <= max(p[0], r[0]) and min(p[1], r[1]) <= q[1] <= max(p[1], r[1]):
                return True
            return False

        o1 = orientation(p1, q1, p2)
        o2 = orientation(p1, q1, q2)
        o3 = orientation(p2, q2, p1)
        o4 = orientation(p2, q2, q1)

        if o1 != o2 and o3 != o4:
            return True
        if o1 == 0 and on_segment(p1, p2, q1):
            return True
        if o2 == 0 and on_segment(p1, q2, q1):
            return True
        if o3 == 0 and on_segment(p2, p1, q2):
            return True
        if o4 == 0 and on_segment(p2, q1, q2):
            return True

        return False

    n1 = len(polygon1)
    n2 = len(polygon2)

    for i in range(n1):
        for j in range(n2):
            if do_lines_intersect(
                polygon1[i], polygon1[(i + 1) % n1], polygon2[j], polygon2[(j + 1) % n2]
            ):
                logging.info("Polygons collide")
                return True

    logging.info("Polygons do not collide")
    return False

class FileProcessor:
    def copy_directory(self, source_dir: str, target_dir: str) -> None:
        if not os.path.exists(source_dir):
            raise FileNotFoundError(f"Source directory does not exist: {source_dir}")
        if os.path.exists(target_dir):
            shutil.rmtree(target_dir)
        shutil.copytree(source_dir, target_dir)
        logging.info(f"Copied directory from {source_dir} to {target_dir}")

    def process_files(self, directory: str, extensions: List[str]) -> List[Tuple[str, int]]:
        if not os.path.exists(directory):
            raise FileNotFoundError(f"Directory does not exist: {directory}")
        result = []
        for root, _, files in os.walk(directory):
            for file in files:
                if any(file.endswith(ext) for ext in extensions):
                    file_path = os.path.join(root, file)
                    with open(file_path, 'r') as f:
                        line_count = sum(1 for _ in f)
                    result.append((file, line_count))
                    logging.info(f"Processed file: {file}, Lines: {line_count}")
        return result

if __name__ == "__main__":
    storage = DataStorage()
    storage.add("key1", "value1")
    storage.add("key2", "value2")
    print(storage.get("key1"))
    storage.delete("key2")
    print(storage.list())

    text = "Hello world! Hello everyone. This is a simple test. Test, test, hello."
    k = 2
    print(find_top_k_frequent_words(text, k))

    polygon1 = [(0, 0), (4, 0), (4, 4), (0, 4)]
    polygon2 = [(2, 2), (6, 2), (6, 6), (2, 6)]
    polygon3 = [(5, 5), (7, 5), (7, 7), (5, 7)]

    print(check_polygon_collision(polygon1, polygon2))
    print(check_polygon_collision(polygon1, polygon3))

    file_processor = FileProcessor()
    source_dir = "source_directory"
    target_dir = "destination_directory"
    file_processor.copy_directory(source_dir, target_dir)

    directory = "."
    extensions = [".txt", ".log"]
    print(file_processor.process_files(directory, extensions))