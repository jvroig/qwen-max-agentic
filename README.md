# Qwen-Max Agentic UI

## Overview

This repository provides a web-based chat interface and Python API backend that equips the Qwen-Max language model with powerful tools. These tools allow users to interact with their local or remote filesystem, perform git operations, search the web, and execute Python code through natural language queries or direct API calls.

**Important Note**: This is an **educational implementation** designed to demonstrate how tool-calling works with Large Language Models (LLMs). It is **not intended for production use**. Please exercise caution when using this code, especially when interacting with sensitive filesystems. Always ensure proper security measures are in place if deploying similar solutions in real-world scenarios.

## Features

### Filesystem Operations
- **Get Current Working Directory**: Retrieve the current working directory
- **Advanced File Reading**: Read files with optional line numbering, range selection, and debug formatting
- **Write and Append Files**: Create new files or append content to existing ones
- **Advanced File Editing**: Line-based editing with diff preview and dry-run capability
- **File Management**: Copy, move, and delete files
- **Directory Operations**: Create, list, copy, and remove directories

### Git Operations
- **Repository Management**: Clone repositories, view status and history
- **Commit Operations**: Stage changes, create commits, and push to remotes
- **File Restoration**: Restore files or entire repositories to previous states
- **Diff Analysis**: Compare commits, staged changes, or working directory

### Web Tools
- **Web Search**: Search the internet using Brave Search API
- **Web Content Fetching**: Retrieve and clean content from web pages

### Python Execution
- **Code Execution**: Execute Python files or arbitrary Python code
- **Syntax Checking**: Validate Python code syntax before execution

## Tools Reference

### Filesystem Tools

#### 1. **get_cwd**
- **Description**: Get the current working directory
- **Parameters**: None
- **Returns**: String - information about the current working directory

#### 2. **read_file**
- **Description**: Read a file with optional line numbering, range selection, and debug formatting
- **Parameters**:
  - `path` (required, string): Path and filename of the file to read
  - `enumerate` (optional, boolean): Whether to include line numbers (defaults to False)
  - `start_line` (optional, integer): First line to read, 1-indexed (defaults to 1)
  - `end_line` (optional, integer): Last line to read, 1-indexed, None for all lines (defaults to None)
  - `show_repr` (optional, boolean): Whether to show Python's repr() of each line, revealing whitespace and special characters (defaults to False)
- **Returns**: String - the contents of the file (potentially formatted with line numbers or repr)

#### 3. **write_file**
- **Description**: Write content to a file in the filesystem
- **Parameters**:
  - `path` (required, string): Path and filename of the file to write
  - `content` (required, string): The content to write to the file
- **Returns**: String - confirmation message indicating success or failure

#### 4. **append_file**
- **Description**: Append content to an existing file in the filesystem
- **Parameters**:
  - `path` (required, string): Path and filename of the file to append to
  - `content` (required, string): The content to append to the file
- **Returns**: String - confirmation message indicating success or failure

#### 5. **edit_file**
- **Description**: Make a line-based edit to a file by replacing old_text with new_text. The old_text must appear exactly once in the file for safety
- **Parameters**:
  - `path` (required, string): Path and filename of the file to edit
  - `old_text` (required, string): Text to be replaced (must match exactly once)
  - `new_text` (required, string): Replacement text
  - `dry_run` (optional, boolean): If True, just return the diff without making changes (defaults to False)
- **Returns**: String - confirmation message with diff showing changes, or error message if editing fails

#### 6. **copy_file**
- **Description**: Copy a file from source to destination
- **Parameters**:
  - `source` (required, string): Path to the source file to copy
  - `destination` (required, string): Path where the file should be copied to
- **Returns**: String - confirmation message indicating success or failure

#### 7. **remove_file**
- **Description**: Remove/delete a single file
- **Parameters**:
  - `path` (required, string): Path to the file to delete
- **Returns**: String - confirmation message indicating success or failure

#### 8. **create_directory**
- **Description**: Create a new directory in the filesystem
- **Parameters**:
  - `path` (required, string): Path of the directory to create
- **Returns**: String - confirmation message indicating success or failure

#### 9. **list_directory**
- **Description**: List the contents of a directory in the filesystem
- **Parameters**:
  - `path` (optional, string): Path of the directory to list. If not provided, lists the current working directory
- **Returns**: String - a list of files and directories in the specified path

#### 10. **copy_directory**
- **Description**: Copy a directory and all its contents to a new location
- **Parameters**:
  - `source` (required, string): Path to the source directory to copy
  - `destination` (required, string): Path where the directory should be copied to
- **Returns**: String - confirmation message indicating success or failure

#### 11. **remove_directory**
- **Description**: Remove/delete a directory and all its contents
- **Parameters**:
  - `path` (required, string): Path to the directory to delete
- **Returns**: String - confirmation message indicating success or failure

### Git Tools

#### 12. **git_clone**
- **Description**: Clone a git repository using HTTPS
- **Parameters**:
  - `repo_url` (required, string): The HTTPS URL of the repository to clone
  - `target_path` (optional, string): The path where to clone the repository
- **Returns**: String - confirmation message indicating success or failure

#### 13. **git_commit**
- **Description**: Stage all changes and create a commit
- **Parameters**:
  - `message` (required, string): The commit message
  - `path` (optional, string): The path to the git repository (defaults to current directory)
- **Returns**: String - confirmation message indicating success or failure

#### 14. **git_restore**
- **Description**: Restore the repository or specific files to a previous state
- **Parameters**:
  - `commit_hash` (optional, string): The commit hash to restore to. If not provided, unstages all changes
  - `path` (optional, string): The path to the git repository (defaults to current directory)
  - `files` (optional, list): List of specific files to restore. If not provided, restores everything
- **Returns**: String - confirmation message indicating success or failure

#### 15. **git_push**
- **Description**: Push commits to a remote repository
- **Parameters**:
  - `remote` (optional, string): The remote name (defaults to 'origin')
  - `branch` (optional, string): The branch name to push to (defaults to 'main')
  - `path` (optional, string): The path to the git repository (defaults to current directory)
- **Returns**: String - confirmation message indicating success or failure

#### 16. **git_log**
- **Description**: Get the commit history of the repository
- **Parameters**:
  - `path` (optional, string): The path to the git repository (defaults to current directory)
  - `max_count` (optional, integer): Maximum number of commits to return
  - `since` (optional, string): Get commits since this date (e.g., "2024-01-01" or "1 week ago")
- **Returns**: String - JSON formatted commit history with hash, author, date, and message for each commit

#### 17. **git_show**
- **Description**: Get detailed information about a specific commit
- **Parameters**:
  - `commit_hash` (required, string): The hash of the commit to inspect
  - `path` (optional, string): The path to the git repository (defaults to current directory)
- **Returns**: String - JSON formatted commit details including metadata and changed files

#### 18. **git_status**
- **Description**: Get the current status of the repository
- **Parameters**:
  - `path` (optional, string): The path to the git repository (defaults to current directory)
- **Returns**: String - JSON formatted repository status including staged, unstaged, and untracked changes

#### 19. **git_diff**
- **Description**: Get the differences between commits, staged changes, or working directory
- **Parameters**:
  - `path` (optional, string): The path to the git repository (defaults to current directory)
  - `commit1` (optional, string): First commit hash for comparison
  - `commit2` (optional, string): Second commit hash for comparison
  - `staged` (optional, boolean): If True, show staged changes (ignored if commits are specified)
  - `file_path` (optional, string): Path to specific file to diff
- **Returns**: String - JSON formatted diff information including summary and detailed changes per file

### Web Tools

#### 20. **brave_web_search**
- **Description**: Search the web using Brave Search API. The responses contain summaries - use fetch_web_page to get full content from interesting results
- **Parameters**:
  - `query` (required, string): The search query to submit to Brave
  - `count` (optional, integer): The number of results to return (defaults to 10)
- **Returns**: Object - a JSON object containing search results or error information from the Brave Search API

#### 21. **fetch_web_page**
- **Description**: Fetch content from a specified URL. Good to use after doing a brave_web_search to get more details from interesting search results
- **Parameters**:
  - `url` (required, string): The URL to fetch content from
  - `headers` (optional, dictionary): Custom headers to include in the request (defaults to a standard User-Agent)
  - `timeout` (optional, integer): Request timeout in seconds (defaults to 30)
  - `clean` (optional, boolean): Whether to extract only the main content (defaults to True)
- **Returns**: String - the cleaned web page content as text, or an error object if the request fails

### Python Tools

#### 22. **python_execute_file**
- **Description**: Execute a Python file and return its output
- **Parameters**:
  - `file_path` (required, string): Path to the Python file to execute
- **Returns**: String - the output of the execution or an error message if execution fails

#### 23. **python_check_syntax**
- **Description**: Check the syntax of Python code
- **Parameters**:
  - `code` (optional, string): Python code to check
  - `file_path` (optional, string): Path to a Python file to check
- **Returns**: String - result of the syntax check

#### 24. **python_execute_code**
- **Description**: Execute arbitrary Python code and return its output
- **Parameters**:
  - `code` (required, string): Python code to execute
- **Returns**: String - the output of the execution or an error message if execution fails

## Installation

To get started with this project, follow these steps:

1. **Clone the Repository**

   ```bash
   git clone https://github.com/jvroig/qwen-max-agentic.git
   cd qwen-max-agentic
   ```

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

## Access the Web Interface

In your file browser, double-click the file index.html to load the chat interface in your default browser.

The web interface allows you to communicate with Qwen-Max using natural language commands. You can use it to perform operations like reading files, writing content, creating directories, etc., simply by typing instructions such as:

### Basic File Operations
- "Get the current working directory."
- "Read the file at path /example/path/to/file.txt."
- "Write 'Hello World' to the file at /example/path/to/file.txt."
- "Create a new directory at /example/path/to/newdir."
- "List the contents of the directory at /example/path/to/dir."

### Advanced File Operations
- "Read lines 50-100 of the log file with line numbers."
- "Show me the whitespace characters in config.txt using repr mode."
- "Edit myfile.py and replace 'old_function()' with 'new_function()' - show me the diff first."
- "Copy the entire project directory to create a backup."
- "Append today's log entry to the daily log file."

### Git Operations
- "Clone the repository from https://github.com/user/repo.git."
- "Show me the git status of the current directory."
- "Commit all changes with message 'Updated documentation'."
- "Show me the last 5 commits in the repository."

### Web and Python
- "Search the web for 'Python best practices 2024'."
- "Fetch the content from that interesting URL you found."
- "Execute the Python script test.py and show me the output."
- "Check if this Python code has any syntax errors."

Enjoy interacting with Qwen-Max powered by comprehensive development tools!

---

**This README file was updated to reflect the current comprehensive tool set available in the Qwen-Max Agentic UI.**
