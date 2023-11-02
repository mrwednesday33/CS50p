import sys

if len(sys.argv) != 2:
    sys.exit("Usage: python lines.py filename.py")

filename = sys.argv[1]

if not filename.endswith(".py"):
    sys.exit("Error: File must have .py extension")

try:
    with open(filename) as f:
        code_lines = 0
        for line in f:
            line = line.strip()
            if line.startswith("#") or not line:
                continue
            code_lines += 1
        print(f"File {filename} has {code_lines} lines of code (excluding comments and blank lines).")
except FileNotFoundError:
    sys.exit(f"Error: File {filename} not found.")
