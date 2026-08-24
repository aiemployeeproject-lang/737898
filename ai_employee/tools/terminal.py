"""Terminal tools for executing shell commands and scripts."""

import subprocess
import sys


def run_command(command: str) -> dict:
    """
    Execute a shell command and capture its output.
    
    Args:
        command: Shell command to execute
        
    Returns:
        dict: Contains 'stdout', 'stderr', and 'success' keys
              success is True if return_code is 0, False otherwise
    """
    try:
        # Run the command with a 30-second timeout
        result = subprocess.run(
            command,
            shell=True,
            capture_output=True,
            text=True,
            timeout=30
        )
        
        # Determine success based on return code
        success = result.returncode == 0
        
        return {
            "stdout": result.stdout,
            "stderr": result.stderr,
            "success": success,
            "return_code": result.returncode
        }
    
    except subprocess.TimeoutExpired:
        error_msg = f"Command timed out after 30 seconds: {command}"
        print(f"✗ {error_msg}")
        return {
            "stdout": "",
            "stderr": error_msg,
            "success": False,
            "return_code": -1
        }
    
    except Exception as e:
        error_msg = f"Error executing command: {str(e)}"
        print(f"✗ {error_msg}")
        return {
            "stdout": "",
            "stderr": error_msg,
            "success": False,
            "return_code": -1
        }


if __name__ == "__main__":
    # Test the run_command function
    print("=" * 50)
    print("Testing Terminal Functions")
    print("=" * 50)
    
    # Test 1: Run a simple echo command
    print("\nTest 1: Running 'echo Hello'")
    result = run_command("echo Hello")
    
    print("\nResult Dictionary:")
    print(f"  stdout: {result['stdout'].strip()}")
    print(f"  stderr: {result['stderr']}")
    print(f"  success: {result['success']}")
    print(f"  return_code: {result['return_code']}")
    
    # Test 2: Run a command that fails
    print("\n" + "-" * 50)
    print("\nTest 2: Running a failing command")
    result = run_command("false")
    
    print("\nResult Dictionary:")
    print(f"  stdout: {result['stdout']}")
    print(f"  stderr: {result['stderr']}")
    print(f"  success: {result['success']}")
    print(f"  return_code: {result['return_code']}")
    
    # Test 3: Run a command that produces stderr
    print("\n" + "-" * 50)
    print("\nTest 3: Running command with stderr output")
    result = run_command("python -c \"import sys; sys.stderr.write('Test error')\"")
    
    print("\nResult Dictionary:")
    print(f"  stdout: {result['stdout']}")
    print(f"  stderr: {result['stderr']}")
    print(f"  success: {result['success']}")
    print(f"  return_code: {result['return_code']}")
    
    print("\n" + "=" * 50)
    print("Tests completed!")
    print("=" * 50)
