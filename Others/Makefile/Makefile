.PHONY: print_path
.DEFAULT_GOAL := help
VENV_NAME?=venv
# --------------------------------------------------------------------- # 
# Windows # 
# --------------------------------------------------------------------- # 
ifeq ($(OS), Windows_NT)

# ====== FEATURE CORRELATION ======
main: ## Repeat the same functions as in Linux
# ...

# --------------------------------------------------------------------- # 
# LINUX # 
# --------------------------------------------------------------------- # 
main: ## Runs main function

test:  ## Run full project test file with no warnings
	python3 -m pytest -p no:warnings
	
install: requirements.txt  # Install requirements.txt
	python -m pip install --upgrade pip
	pip install -r requirements.txt

print_tree:  ## Print root tree
	python3 print_tree.py

print_path:  ## Print the Current Directory
	@echo "The current path is: $(CURDIR)"
	@ls $(CURDIR)

clean:  ## Remove images and paths
	rm -rf whatever_is_needed/

help:  ## This help message
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

setup:  ## Build a source and build distribution formats
	echo "setup"

endif

.PHONY: clean help setup
