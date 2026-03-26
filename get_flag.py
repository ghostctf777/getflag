#!/usr/bin/env python3
import secrets
import string
from pathlib import Path

def gen_flag():
    alphabet = string.ascii_uppercase + string.digits
    return "TUIT_CTF{" + "".join(secrets.choice(alphabet) for _ in range(24)) + "}"

flag = gen_flag()
Path("secrets.txt").write_text(flag + "\n")
print(flag)
