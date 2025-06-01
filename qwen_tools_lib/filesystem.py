import os
import shutil

def get_cwd():
    """
    Get the current working directory.
    
    Returns:
        str: The current working directory path.
    """
    try:
        return os.getcwd()
    except Exception as e:
        return f"Error getting current working directory: {e}"

def read_file(path):
    """
    Read the contents of a file.
    
    Args:
        path (str): The path to the file to read.
        
    Returns:
        str: The contents of the file, or an error message if reading fails.
    """
    try:
        with open(path, 'r') as file:
            return file.read()
    except FileNotFoundError:
        return f"File not found: {path}"
    except PermissionError:
        return f"Permission denied: {path}"
    except Exception as e:
        return f"Error reading file: {e}"

def write_file(path, content):
    """
    Write content to a file.
    
    Args:
        path (str): The path to the file to write.
        content (str): The content to write to the file.
        
    Returns:
        str: A confirmation message, or an error message if writing fails.
    """
    try:
        with open(path, 'w') as file:
            file.write(content)
        return f"File written successfully: {path}"
    except PermissionError:
        return f"Permission denied: {path}"
    except Exception as e:
        return f"Error writing file: {e}"

def create_directory(path):
    """
    Create a new directory.
    
    Args:
        path (str): The path of the directory to create.
        
    Returns:
        str: A confirmation message, or an error message if creation fails.
    """
    try:
        os.makedirs(path, exist_ok=True)  # `exist_ok=True` ensures no error if the directory already exists
        return f"Directory created successfully: {path}"
    except PermissionError:
        return f"Permission denied: {path}"
    except Exception as e:
        return f"Error creating directory: {e}"

def list_directory(path="."):
    """
    List the contents of a directory.
    
    Args:
        path (str): The path of the directory to list. Defaults to the current directory (".").
        
    Returns:
        str: A list of files and directories, or an error message if listing fails.
    """
    try:
        import time
        contents = os.listdir(path)
        return f"Contents of directory '{path}': {', '.join(contents)}"
    except FileNotFoundError:
        return f"Directory not found: {path}"
    except PermissionError:
        return f"Permission denied: {path}"
    except Exception as e:
        return f"Error listing directory: {e}"

def copy_file(source, destination):
    """
    Copy a file from source to destination.
    
    Args:
        source (str): The path to the source file to copy.
        destination (str): The path where the file should be copied to.
        
    Returns:
        str: A confirmation message, or an error message if copying fails.
    """
    try:
        shutil.copy2(source, destination)
        return f"File copied successfully from {source} to {destination}"
    except FileNotFoundError:
        return f"Source file not found: {source}"
    except PermissionError:
        return f"Permission denied: Cannot copy from {source} to {destination}"
    except shutil.SameFileError:
        return f"Error: Source and destination are the same file: {source}"
    except IsADirectoryError:
        return f"Error: Destination is a directory: {destination}"
    except Exception as e:
        return f"Error copying file: {e}"

def remove_file(path):
    """
    Remove/delete a single file.
    
    Args:
        path (str): The path to the file to delete.
        
    Returns:
        str: A confirmation message, or an error message if deletion fails.
    """
    try:
        os.remove(path)
        return f"File removed successfully: {path}"
    except FileNotFoundError:
        return f"File not found: {path}"
    except PermissionError:
        return f"Permission denied: {path}"
    except IsADirectoryError:
        return f"Error: Path is a directory, not a file: {path}"
    except Exception as e:
        return f"Error removing file: {e}"

def remove_directory(path):
    """
    Remove/delete a directory and all its contents.
    
    Args:
        path (str): The path to the directory to delete.
        
    Returns:
        str: A confirmation message, or an error message if deletion fails.
    """
    try:
        shutil.rmtree(path)
        return f"Directory removed successfully: {path}"
    except FileNotFoundError:
        return f"Directory not found: {path}"
    except PermissionError:
        return f"Permission denied: {path}"
    except NotADirectoryError:
        return f"Error: Path is not a directory: {path}"
    except Exception as e:
        return f"Error removing directory: {e}"


def copy_directory(source, destination):
    """
    Copy a directory and all its contents to a new location.
    
    Args:
        source (str): The path to the source directory to copy.
        destination (str): The path where the directory should be copied to.
        
    Returns:
        str: A confirmation message, or an error message if copying fails.
    """
    try:
        shutil.copytree(source, destination)
        return f"Directory copied successfully from {source} to {destination}"
    except FileNotFoundError:
        return f"Source directory not found: {source}"
    except PermissionError:
        return f"Permission denied: Cannot copy from {source} to {destination}"
    except FileExistsError:
        return f"Error: Destination directory already exists: {destination}"
    except NotADirectoryError:
        return f"Error: Source is not a directory: {source}"
    except Exception as e:
        return f"Error copying directory: {e}"


def append_file(path, content):
    """
    Append content to an existing file.
    
    Args:
        path (str): The path to the file to append to.
        content (str): The content to append to the file.
        
    Returns:
        str: A confirmation message, or an error message if appending fails.
    """
    try:
        with open(path, 'a') as file:
            file.write(content)
        return f"Content appended successfully to: {path}"
    except FileNotFoundError:
        return f"File not found: {path}"
    except PermissionError:
        return f"Permission denied: {path}"
    except IsADirectoryError:
        return f"Error: Path is a directory, not a file: {path}"
    except Exception as e:
        return f"Error appending to file: {e}"
