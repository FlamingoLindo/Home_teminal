import os
import platform

def clear_console():
    """Clear the console based on the operating system."""
    os.system("cls" if platform.system() == "Windows" else "clear")

def open_url(url):
    """Open a URL in the default web browser"""
    try:
        os.system(f"start chrome {url}")
    except Exception as e:
        print(f"Failed to open URL {url}. Error: {e}")

def open_firefox_url(url):
    """Open a URL in the default web browser"""
    try:
        os.system(f"start firefox {url}")
    except Exception as e:
        print(f"Failed to open URL {url}. Error: {e}")