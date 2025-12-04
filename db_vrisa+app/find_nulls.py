# find_nulls.py
from pathlib import Path

for path in Path(".").rglob("*.py"):
    try:
        data = path.read_bytes()
    except Exception as e:
        print("No se pudo leer", path, e)
        continue
    if b"\x00" in data:
        print("Archivo con bytes nulos:", path)
