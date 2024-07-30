import os
import pyperclip

def generate_project_structure(path, indent=0):
    """
    Generate the project directory structure.
    
    Args:
        path (str): The directory path to scan.
        indent (int): The current indentation level for formatting.
    
    Returns:
        str: A formatted string representing the directory structure.
    """
    structure = ""
    try:
        # List all items in the directory
        items = sorted(os.listdir(path))
        
        for item in items:
            item_path = os.path.join(path, item)
            if os.path.isdir(item_path):
                # Add directory name with proper indentation
                structure += "│   " * indent + "├── " + item + "/\n"
                # Recursively add contents of the directory
                structure += generate_project_structure(item_path, indent + 1)
            else:
                # Add file name with proper indentation
                structure += "│   " * indent + "├── " + item + "\n"
    except PermissionError:
        # Handle permissions error if any directory is not accessible
        structure += "│   " * indent + "├── [Permission Denied]\n"
    
    return structure