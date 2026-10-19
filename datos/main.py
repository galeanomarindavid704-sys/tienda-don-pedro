from pathlib import Path

archivo = Path("productos.txt")
lineas = archivo.read_text(encoding="utf-8").splitlines()

print("=== Inventario Tienda Don Pedro ===")
total_productos = 0
valor_total = 0

for linea in lineas:
    print("-", linea)
    total_productos += 1
    if "$" in linea:
        precio_str = linea.split("$")[1].replace(".", "").strip()
        valor_total += int(precio_str)

print(f"\nTotal de productos: {total_productos}")
print(f"Valor del inventario: ${valor_total}")