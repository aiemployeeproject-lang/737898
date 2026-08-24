"""Filesystem tools for file and directory operations."""

from pathlib import Path


def create_folder(path: str) -> bool:
    """
    Create a folder at the specified path.
    
    Args:
        path: Directory path to create
        
    Returns:
        bool: True if successful, False otherwise
    """
    try:
        folder = Path(path)
        folder.mkdir(parents=True, exist_ok=True)
        print(f"✓ Folder created successfully: {path}")
        return True
    except Exception as e:
        print(f"✗ Error creating folder '{path}': {e}")
        return False


def write_file(path: str, content: str) -> bool:
    """
    Write content to a file at the specified path.
    
    Args:
        path: File path to write to
        content: Content to write to the file
        
    Returns:
        bool: True if successful, False otherwise
    """
    try:
        file_path = Path(path)
        # Create parent directories if they don't exist
        file_path.parent.mkdir(parents=True, exist_ok=True)
        file_path.write_text(content)
        print(f"✓ File written successfully: {path}")
        return True
    except Exception as e:
        print(f"✗ Error writing file '{path}': {e}")
        return False


def read_file(path: str) -> str:
    """
    Read and return the content of a file.
    
    Args:
        path: File path to read from
        
    Returns:
        str: File content if successful, empty string otherwise
    """
    try:
        file_path = Path(path)
        content = file_path.read_text()
        print(f"✓ File read successfully: {path}")
        return content
    except FileNotFoundError:
        print(f"✗ File not found: {path}")
        return ""
    except Exception as e:
        print(f"✗ Error reading file '{path}': {e}")
        return ""


if __name__ == "__main__":
    # Test the filesystem functions
    print("=" * 50)
    print("Testing Filesystem Functions")
    print("=" * 50)
    
    # Test 1: Create a folder
    print("\nTest 1: Creating folder 'test_workspace'")
    create_folder("test_workspace")
    
    # Test 2: Write a file
    print("\nTest 2: Writing to test_workspace/test.txt")
    write_file("test_workspace/test.txt", "Hello AI Employee")
    
    # Test 3: Read the file back
    print("\nTest 3: Reading from test_workspace/test.txt")
    content = read_file("test_workspace/test.txt")
    print(f"Content: {content}")
    
    print("\n" + "=" * 50)
    print("Tests completed!")
    print("=" * 50)
