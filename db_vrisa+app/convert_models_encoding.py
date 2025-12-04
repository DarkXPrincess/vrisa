from pathlib import Path

ruta = Path("vrisa/models.py")

# Leemos los bytes "dañados" (UTF-16 con null bytes)
data = ruta.read_bytes()

# Los decodificamos como UTF-16 (que es como realmente está guardado)
texto = data.decode("utf-16")

# Los volvemos a guardar como UTF-8 normalito
ruta.write_text(texto, encoding="utf-8")

print("Listo: vrisa/models.py convertido a UTF-8")