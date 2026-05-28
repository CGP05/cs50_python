import re

name = input("what's your name? ").strip()
if matches := re.search(r"^(.+), *(.+)$", name):
    name = name.group(2) + "" + matches.group(1)
print(f"hello, {name}")