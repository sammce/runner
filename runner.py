import os
import sys
from samutil.formatting import Formatter as fmt

def error(msg):
    print(fmt.error(msg))
    sys.exit(1)

tests = {
    "most-recent-leap-year.py": [("2022", "2020"), ("2016", "2016"), ("2015", "2012"), ("2014", "2012")],
    "sweets-per-child.py": [("30", "3"), ("35", "3"), ("40", "4"), ("55", "5")],
    "three-digit-number.py": [("7\n3\n8", "738"), ("4\n5\n1", "451"), ("9\n3\n1", "931")],
}

for file, cases in tests.items():
    print(os.getcwd())
