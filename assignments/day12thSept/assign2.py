import glob
import re

files = glob.glob("*.csv")

for file in files:
    # Matches exactly "data.csv" OR anything like "data_....csv"
    if re.match(r"^data(_.*)?\.csv$", file):
        print(f"CSV Match: {file}")
