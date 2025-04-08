# .gitignore

Owner: Andrés Carrancá
Tags: Process

A .gitignore file is a text file that tells Git which files or folders to ignore in a project. It's important because it helps keep your repository clean by excluding unnecessary files (like compiled code, temporary files, or sensitive information) from version control, reducing clutter and potential security risks.

# Basic .gitignore for Python

```
# Byte-compiled / optimized / DLL files
__pycache__/
*.py[cod]
*$py.class

# C extensions
*.so

# Distribution / packaging
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
share/python-wheels/
*.egg-info/
.installed.cfg
*.egg
MANIFEST

# Installer logs
pip-log.txt
pip-delete-this-directory.txt

# Unit test / coverage reports
htmlcov/
.tox/
.nox/
.coverage
.coverage.*
.cache
nosetests.xml
coverage.xml
*.cover
*.py,cover
.hypothesis/
.pytest_cache/
cover/

# Environments
.env
.venv
env/
venv/
ENV/
env.bak/
venv.bak/
```

## Ignoring Complete Folders

To ignore a complete folder, simply add the folder name followed by a forward slash to your .gitignore file:

```
folder_to_ignore/
```

## Ignoring Everything in a Folder Except Specific Files

To ignore everything in a folder except for specific files, use the following syntax:

```
# Ignore everything in the folder
folder_name/*

# But not these files...
!folder_name/.gitkeep
!folder_name/important_file.txt
```

## What is .gitkeep?

.gitkeep is not a special file recognized by Git. It's a convention used by developers to keep an otherwise empty directory in a Git repository. Git doesn't track empty directories, so adding a .gitkeep file (which can be empty) allows you to maintain the directory structure in your repository.

## Important Notes

- The .gitignore file should be placed in the root directory of your repository.
- You can use patterns with wildcards. For example, *.log will ignore all files with the .log extension.
- Lines starting with # are comments and are ignored by Git.
- You can negate a pattern by starting it with an exclamation point (!). This is useful for including specific files that would otherwise be ignored.
- Remember to commit and push your .gitignore file so that other collaborators can benefit from the same ignore rules.
- You can have multiple .gitignore files in different directories of your repository, but it's generally cleaner to have a single file at the root.