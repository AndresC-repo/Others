# ArgParser in Python: A Simple Guide

Owner: Andrés Carrancá
Tags: Process

ArgParser is a module in Python that makes it easy to write user-friendly command-line interfaces. It allows you to define and parse command-line arguments for your scripts.

## How to Use ArgParser

Here's a simple example using two files: arg_parser.py and [main.py](http://main.py)

### arg_parser.py

```python
import argparse

def create_parser():
    parser = argparse.ArgumentParser(description="A simple argument parser example")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    parser.add_argument("--count", type=int, default=1, help="Number of times to perform an action")
    return parser
```

### [main.py](http://main.py)

```python
from arg_parser import create_parser

def main():
    parser = create_parser()
    args = parser.parse_args()

    if args.verbose:
        print(f"Verbose mode is on")
    
    print(f"Performing action {args.count} time(s)")

if __name__ == "__main__":
    main()
```

In this example, we've defined two arguments:

- --verbose: A boolean flag (True if present, False if not)
- --count: An integer with a default value of 1

To run the script, you would use commands like:

```bash
python main.py
python main.py --verbose
python main.py --count 5
python main.py --verbose --count 3
```

This setup allows you to easily add or modify arguments in arg_parser.py without changing the main script logic.

### ArgParser in Makefile

To make running these commands easier, you can create a Makefile with the following content:

```makefile
.PHONY: run verbose count verbose-count

run:
	python main.py

verbose:
	python main.py --verbose

count:
	python main.py --count 5

verbose-count:
	python main.py --verbose --count 3
	
```

With this Makefile, you can now use the following commands:

```bash
make run
make verbose
make count
make verbose-count
```

This simplifies the process of running your script with different arguments and makes it more convenient for other developers to use your tool.