import os
from subprocess import Popen, PIPE
import sys
import platform

def error(msg):
    print(msg)
    sys.exit(1)

def red_text(msg):
    print(f"\033[91m{msg}\033[0m")

def green_text(msg):
    print(f"\033[92m{msg}\033[0m")

tests = {
    "most-recent-leap-year.py": [("2022", "2020"), ("2016", "2016"), ("2015", "2012"), ("2014", "2012")],
    "sweets-per-child.py": [("30", "3"), ("35", "3"), ("40", "4"), ("55", "5")],
    "three-digit-number.py": [("7\n3\n8", "738"), ("4\n5\n1", "451"), ("9\n3\n1", "931")],
    "treble.py": [("10", "30"), ("5", "15"), ("2", "6")]
}

is_windows = platform.system() == "Windows"
py_command = "python" if is_windows else "python3"
separator = "\\" if is_windows else "/"

number_correct = 0
print()

for file, cases in tests.items():
    cwd = os.getcwd().lower()

    for case, answer in cases:
        res = Popen([py_command, f"{cwd}{separator}{file}"], stdout=PIPE, stdin=PIPE, stderr=PIPE)
        out, err = res.communicate(input=case.encode("utf-8"))
        out = out.decode("utf-8").strip()

        if out != answer:
            red_text(file)
            break
    else:
        green_text(file)
        number_correct += 1

print("-" * 50)
print("Correct:", number_correct)
