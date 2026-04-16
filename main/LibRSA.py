# Importing
import math
import base64 

def createKeyString(p: int,q: int) -> str:
    stringCombined = f"{p}:{q}"
    return base64.b64encode(stringCombined.encode()).decode()


def decode_str(b64: str) -> str:
    return base64.b64decode(b64).decode()

# Test Later