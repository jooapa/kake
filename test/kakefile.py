"""Kakefile for the test suite."""
import sys
import os

from src.kake import Project

project = Project("kake_test")

project.add_src(["src/*.cpp"])

project.add_include(
    [
        "include/calc",
        "include/magic"
    ]
)

project.build()
