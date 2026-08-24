"""Permissions module for security and access control."""


def check_permission(command: str) -> str:
    """
    Classify a command into permission levels based on keyword matching.
    
    Args:
        command: Shell command to check
        
    Returns:
        str: "blocked", "confirm", or "allowed"
    """
    # Convert command to lowercase for case-insensitive matching
    command_lower = command.lower()
    
    # Define blocked keywords - these commands are dangerous and should be blocked
    blocked_keywords = [
        "rm -rf",
        "format",
        "del /f",
        "shutdown",
        "mkfs"
    ]
    
    # Define confirm keywords - these require user confirmation
    confirm_keywords = [
        "delete",
        "install",
        "uninstall",
        "sudo"
    ]
    
    # Check for blocked keywords first (highest priority)
    for keyword in blocked_keywords:
        if keyword in command_lower:
            return "blocked"
    
    # Check for confirm keywords
    for keyword in confirm_keywords:
        if keyword in command_lower:
            return "confirm"
    
    # Everything else is allowed
    return "allowed"


if __name__ == "__main__":
    # Test the check_permission function
    print("=" * 60)
    print("Testing Permission Check Functions")
    print("=" * 60)
    
    # Test cases
    test_cases = [
        ("rm -rf /", "blocked"),
        ("pip install requests", "confirm"),
        ("python app.py", "allowed")
    ]
    
    # Run tests
    for command, expected in test_cases:
        result = check_permission(command)
        status = "✓" if result == expected else "✗"
        
        print(f"\n{status} Command: {command}")
        print(f"  Expected: {expected}")
        print(f"  Got: {result}")
    
    print("\n" + "-" * 60)
    print("\nAdditional test cases:")
    print("-" * 60)
    
    additional_cases = [
        "sudo rm -rf /home",
        "format C:",
        "apt-get uninstall package",
        "mkdir new_folder",
        "ls -la",
        "mkfs.ext4 /dev/sda1",
        "python -m install module",
        "echo Hello World"
    ]
    
    for command in additional_cases:
        result = check_permission(command)
        print(f"\n  Command: {command}")
        print(f"  Permission: {result}")
    
    print("\n" + "=" * 60)
    print("Tests completed!")
    print("=" * 60)
