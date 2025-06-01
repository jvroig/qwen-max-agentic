# Qwen-Max Agentic UI

## Overview

This repository provides a web-based chat interface and Python API backend that equips the Qwen-Max language model with powerful tools. These tools allow users to interact with their local or remote filesystem through natural language queries or direct API calls.

**Important Note**: This is an **educational implementation** designed to demonstrate how tool-calling works with Large Language Models (LLMs). It is **not intended for production use**. Please exercise caution when using this code, especially when interacting with sensitive filesystems. Always ensure proper security measures are in place if deploying similar solutions in real-world scenarios.


### Features

- **Get Current Working Directory**: Retrieve the current working directory.
- **Read Files**: Read the contents of files within the filesystem.
- **Write Files**: Write content to files in the filesystem.
- **Create Directories**: Create new directories in the filesystem.
- **List Directory Contents**: List all files and directories in a specified path (or the current working directory).
- **Git Operations**: Perform various Git operations such as cloning repositories, committing changes, and viewing commit history.

### Tools Description

1. **get-cwd**
    - **Description**: Get the current working directory.
    - **Parameters**: None.
    - **Returns**: String - information about the current working directory.

2. **read-file**
    - **Description**: Read a file in the filesystem.
    - **Parameters**:
      - `path` (required, string): Path and filename of the file to read.
    - **Returns**: String - the contents of the file specified in `path`.

3. **write-file**
    - **Description**: Write content to a file in the filesystem.
    - **Parameters**:
      - `path` (required, string): Path and filename of the file to write.
      - `content` (required, string): The content to write to the file.
    - **Returns**: String - confirmation message indicating success or failure.

4. **create-directory**
    - **Description**: Create a new directory in the filesystem.
    - **Parameters**:
      - `path` (required, string): Path of the directory to create.
    - **Returns**: String - confirmation message indicating success or failure.

5. **list-directory**
    - **Description**: List the contents of a directory in the filesystem.
    - **Parameters**:
      - `path` (optional, string): Path of the directory to list. If not provided, lists the current working directory.
    - **Returns**: String - a list of files and directories in the specified path.

6. **git-clone**
    - **Description**: Clone a git repository using HTTPS.
    - **Parameters**:
      - `repo_url` (required, string): The HTTPS URL of the repository to clone.
      - `target_path` (optional, string): The path where to clone the repository.
    - **Returns**: String - confirmation message indicating success or failure.

7. **git-commit**
    - **Description**: Stage all changes and create a commit.
    - **Parameters**:
      - `message` (required, string): The commit message.
      - `path` (optional, string): The path to the git repository (defaults to current directory).
    - **Returns**: String - confirmation message indicating success or failure.

8. **git-restore**
    - **Description**: Restore the repository or specific files to a previous state.
    - **Parameters**:
      - `commit_hash` (optional, string): The commit hash to restore to. If not provided, unstages all changes.
      - `path` (optional, string): The path to the git repository (defaults to current directory).
      - `files` (optional, list): List of specific files to restore. If not provided, restores everything.
    - **Returns**: String - confirmation message indicating success or failure.

9. **git-push**
    - **Description**: Push commits to a remote repository.
    - **Parameters**:
      - `remote` (optional, string): The remote name (defaults to 'origin').
      - `branch` (optional, string): The branch name to push to (defaults to 'main').
      - `path` (optional, string): The path to the git repository (defaults to current directory).
    - **Returns**: String - confirmation message indicating success or failure.

10. **git-log**
    - **Description**: Get the commit history of the repository.
    - **Parameters**:
      - `path` (optional, string): The path to the git repository (defaults to current directory).
      - `max_count` (optional, integer): Maximum number of commits to return.
      - `since` (optional, string): Get commits since this date (e.g., "2024-01-01" or "1 week ago").
    - **Returns**: String - JSON formatted commit history with hash, author, date, and message for each commit.

11. **git-show**
    - **Description**: Get detailed information about a specific commit.
    - **Parameters**:
      - `commit_hash` (required, string): The hash of the commit to inspect.
      - `path` (optional, string): The path to the git repository (defaults to current directory).
    - **Returns**: String - JSON formatted commit details including metadata and changed files.

12. **git-status**
    - **Description**: Get the current status of the repository.
    - **Parameters**:
      - `path` (optional, string): The path to the git repository (defaults to current directory).
    - **Returns**: String - JSON formatted repository status including staged, unstaged, and untracked changes.

13. **git-diff**
    - **Description**: Get the differences between commits, staged changes, or working directory.
    - **Parameters**:
      - `path` (optional, string): The path to the git repository (defaults to current directory).
      - `commit1` (optional, string): First commit hash for comparison.
      - `commit2` (optional, string): Second commit hash for comparison.
      - `staged` (optional, boolean): If True, show staged changes (ignored if commits are specified).
      - `file_path` (optional, string): Path to specific file to diff.
    - **Returns**: String - JSON formatted diff information including:
        - Summary (files changed, total additions/deletions)
        - Detailed changes per file with hunks showing exact line modifications.
### Installation

To get started with this project, follow these steps:

1. **Clone the Repository**

   ```bash
   git clone https://github.com/jvroig/qwen-max-agentic.git
   cd qwen-max-agentic

2. **Set Up a Virtual Environment (Optional but Recommended)**

    ```bash
    python3 -m venv venv
    source venv/bin/activate  
    # On Windows: venv\Scripts\activate
    ```

3. **Run the Backend API Server**

    ```bash
    python setup.py #this will install dependencies and create start.sh file
    bash start.sh #this will start the API server
    ```
    This will start the Python backend server on http://localhost:5001.

### Access the Web Interface

In your file browser, double-click the file index.html to load the chat interface in your default browser.

The web interface allows you to communicate with Qwen-Max using natural language commands. You can use it to perform operations like reading files, writing content, creating directories, etc., simply by typing instructions such as:

"Get the current working directory."
"Read the file at path /example/path/to/file.txt."
"Write 'Hello World' to the file at /example/path/to/file.txt."
"Create a new directory at /example/path/to/newdir."
"List the contents of the directory at /example/path/to/dir."

Enjoy interacting with Qwen-Max powered by filesystem tools!


**This README file was generated by Qwen-Max through Alibaba Cloud Model Studio!**