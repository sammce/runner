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

    if cwd != "c:\\users\\ctyblue\\desktop\\python\\exam":
        error("CWD is not exam directory")

    if os.path.exists("stdin.txt"):
        os.remove("stdin.txt")

    with open("stdin.txt", "a") as f:
        for test, _ in cases:
            f.write(test)

    output = ""
    for _, answer in cases:
        output += f"{answer}\n"

    res = subprocess.run(["python", f"{cwd}\\{file}", "<", "stdin.txt"])
    if res.stdout == output:
        number_correct += 1
    else:
        print("Test case failed")

    print(number_correct)
