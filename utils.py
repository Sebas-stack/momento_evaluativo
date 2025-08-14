import csv
import json
from datetime import datetime

def cargar_compras(ruta):
    """
    Lee data/compras.csv y valida los datos.
    
    Validaciones:
    - cantidad y precio_unitario > 0
    - fecha con formato YYYY-MM-DD
    
    Retorna lista de dicts válidos.
    """
    compras_validas = []
    
    try:
        archivo = open(ruta, 'r', encoding='utf-8')
        lector = csv.DictReader(archivo)
        
        for fila in lector:
            # Validar fecha
            fecha = fila['fecha']
            try:
                datetime.strptime(fecha, '%Y-%m-%d')
            except:
                print(f"Fecha inválida: {fecha}. Fila ignorada.")
                continue
            
            # Validar cantidad
            try:
                cantidad = float(fila['cantidad'])
                if cantidad <= 0:
                    print(f"Cantidad inválida: {cantidad}. Fila ignorada.")
                    continue
            except:
                print(f"Cantidad no es número: {fila['cantidad']}. Fila ignorada.")
                continue
            
            # Validar precio_unitario
            try:
                precio_unitario = float(fila['precio_unitario'])
                if precio_unitario <= 0:
                    print(f"Precio inválido: {precio_unitario}. Fila ignorada.")
                    continue
            except:
                print(f"Precio no es número: {fila['precio_unitario']}. Fila ignorada.")
                continue
            
            # Si llegamos aquí, todos los datos son válidos
            compra = {
                'fecha': fecha,
                'cliente': fila['cliente'],
                'producto': fila['producto'],
                'cantidad': cantidad,
                'precio_unitario': precio_unitario
            }
            compras_validas.append(compra)
        
        archivo.close()
        
    except:
        print(f"Error al leer el archivo {ruta}")
        return []
    
    print(f"Se cargaron {len(compras_validas)} registros válidos.")
    return compras_validas