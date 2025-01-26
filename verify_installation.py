import importlib
import altair as alt
import pandas as pd

def check_package(package_name):
    try:
        importlib.import_module(package_name)
        print(f"{package_name} is installed.")
    except ImportError:
        print(f"{package_name} is NOT installed.")

packages = ["numpy", "pandas", "matplotlib", "scipy", "sklearn"]

for package in packages:
    check_package(package)

print("Altair and Pandas are installed correctly.")