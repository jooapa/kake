"""Start of kake"""
import sys
import os

def main_function():
    """Main function of the project."""

    check_args()


def check_args():
    """Check the arguments of the project."""

class Project:
    """Project class for the project."""

    def __init__(self, name):
        self.name = name
        self.include = []
        self.lib = []
        self.src = []
        self.flags = []

    def get_name(self):
        """Get the name of the project."""
        return self.name

    def set_name(self, name):
        """Set the name of the project."""
        self.name = name

    def add_include(self, include):
        """Add include to the project."""
        self.include = include

    def add_lib(self, lib):
        """Add lib to the project."""
        self.lib = lib

    def add_src(self, src: list) -> None:
        """Add src to the project."""
        self.src = src

    def add_flags(self, flags):
        """Add flags to the project."""
        self.flags = flags

    def build(self):
        """Build the project."""
        print("Building the project.")