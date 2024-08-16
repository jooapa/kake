"""Kakefile for the test suite."""
from src.kake import Project


project = Project("kake_test")

project.add_src(["src/*.cpp"])

project.build()
