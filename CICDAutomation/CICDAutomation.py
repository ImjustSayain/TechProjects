#!/usr/bin/env python3
"""
CI/CD Automation Test Script
Tests for the existence and content of index.html
"""

import os
import sys

# Get the absolute path to the directory where this script is located
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
HTML_FILE_PATH = os.path.join(SCRIPT_DIR, "index.html")

def test_index_exists():
    """Test that index.html exists in the correct location."""
    print(f"Checking for index.html at: {HTML_FILE_PATH}")
    assert os.path.exists(HTML_FILE_PATH), f"ERROR: index.html not found at {HTML_FILE_PATH}!"
    print("✅ index.html found successfully!")

def test_index_contains_title():
    """Test that index.html contains the expected content."""
    with open(HTML_FILE_PATH, 'r') as file:
        content = file.read()
    
    print("Checking for required content in index.html...")
    
    # Check for multiple key elements to be more thorough
    assert "World" in content, "ERROR: Expected content 'World' not found in index.html!"
    assert "<h1>" in content, "ERROR: No HTML heading found in index.html!"
    assert "<title>" in content, "ERROR: No HTML title tag found in index.html!"
    
    print("✅ All content tests passed!")

if __name__ == "__main__":
    print("🚀 Starting CI/CD Automation Tests...")
    print("=" * 50)
    
    try:
        test_index_exists()
        test_index_contains_title()
        
        print("=" * 50)
        print("🎉 SUCCESS: All tests passed!")
        print("The CI/CD pipeline would proceed to deployment.")
        sys.exit(0)
        
    except AssertionError as e:
        print("=" * 50)
        print(f"❌ TEST FAILED: {e}")
        print("\n📋 Debug Info:")
        print(f"Current Working Directory: {os.getcwd()}")
        print(f"Files in directory: {os.listdir()}")
        sys.exit(1)
    except Exception as e:
        print("=" * 50)
        print(f"💥 UNEXPECTED ERROR: {e}")
        sys.exit(1)