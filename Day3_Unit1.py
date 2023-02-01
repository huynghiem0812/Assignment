import re

Tester = re.compile(
    r"^"
    r"(?!.*(\d)(-?\1){3})"
    r"[456]"
    r"\d{3}"
    r"(?:-?\d{4}){3}"
    r"$"
)
for _ in range(int(input())):
    if Tester.search(input()):
        print("Valid")
    else:
        print("Invalid")
