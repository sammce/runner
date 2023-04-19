import os
import subprocess
import sys

def error(msg):
    print(msg)
    sys.exit(1)

tests = {
    "most-recent-leap-year.py": [("2022", "2020"), ("2016", "2016"), ("2015", "2012"), ("2014", "2012")],
    "sweets-per-child.py": [("30", "3"), ("35", "3"), ("40", "4"), ("55", "5")],
    "three-digit-number.py": [("7\n3\n8", "738"), ("4\n5\n1", "451"), ("9\n3\n1", "931")],
    "treble.py": [("10", "30"), ("5", "15"), ("2", "6")]
}

number_correct = 0

for file, cases in tests.items():
    print(os.getcwd())
    cwd = os.getcwd().lower()

    output = ""
    for case, answer in cases:
        with open("stdin.txt", "w") as f:
            f.write(case + "\n")

        res = subprocess.run(["python", f"{cwd}\\{file}", "<", "stdin.txt"])
        if res.stdout != output:
            print("CASE FAILED")
            break
    else:
        number_correct += 1

print("-" * 50)
print(number_correct)
