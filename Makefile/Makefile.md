# Makefile

Owner: Andrés Carrancá
Tags: Process

# What is a Makefile?

A Makefile is a special file used in software development to automate the build process and manage dependencies between files. It contains a set of rules that define how to compile and link a program.

## Usefulness of Makefiles

Makefiles are particularly useful for:

- Automating repetitive tasks
- Managing complex build processes
- Ensuring consistent builds across different environments
- Saving time by only rebuilding what's necessary

## Short Example (Python-related)

While Python doesn't require compilation like C or C++, Makefiles can still be useful for Python projects. Here's a simple example:

```makefile
.PHONY: test clean

IMAGE_NAME = sun-position-app

help list:  ## List the commands
	@echo "---------------------------------------------------"
	@echo "Available commands:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-15s\033[0m %s\n", $$1, $$2}'
	@echo "---------------------------------------------------"

test:
    python -m pytest tests/

clean:  ## Clean up Python bytecode files and __pycache__ directories
	find . -type f -name '*.pyc' -delete
	find . -type d -name '__pycache__' -exec rm -r {} +
	docker rmi -f $(IMAGE_NAME)

run:  ## Run main file
    python main.py
    
run_docker:  ## Run Docker container 
    docker run --rm -it -v .:/app $(IMAGE_NAME)

install:  ## you can also add any setup requirements here
    pip install -r requirements.txt
```

This Makefile defines tasks for running tests, cleaning up compiled Python files, running the main script, and installing dependencies. You can execute these tasks by running commands like `make test` or `make clean`.

## How to Use the Makefile

To use the Makefile, you need to have Make installed on your system. Here are some examples of how to call the Makefile:

```bash
# List available commands
make list

# Run tests
make test

# Clean up Python bytecode files and remove Docker image
make clean

# Run the main Python script
make run

# Run the Docker container
make run_docker

# Install dependencies
make install
```

You can execute these commands in your terminal from the directory where the Makefile is located. Each command will run the corresponding task defined in the Makefile.

## Installing Make

### Linux

Make is usually pre-installed on most Linux distributions. To check if it's installed, open a terminal and type:

```bash
make --version
```

If it's not installed, you can easily install it using your distribution's package manager:

- For Ubuntu or Debian:

```bash
sudo apt-get update
sudo apt-get install make
```

- For Fedora:

```bash
sudo dnf install make
```

- For CentOS or RHEL:

```bash
sudo yum install make
```

### Windows

On Windows, you have several options to install Make:

- **Chocolatey:** If you have Chocolatey package manager installed, you can run:

```powershell
choco install make
```

- **MinGW:** You can install MinGW, which includes Make. Download the MinGW installer from the official website and select the mingw32-make package during installation.
- **Windows Subsystem for Linux (WSL):** If you're using WSL, you can install Make as you would on a Linux system.

After installation, you may need to add the Make executable to your system's PATH environment variable to use it from any directory in the command prompt or PowerShell.