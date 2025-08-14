## Momento Evaluativo
Integrantes:
    - Sebastian Gutierrez: Sebas-stack
    - Angel Tamayo: angeltamayoz

## Descripción general
Este proyecto implementa un flujo completo de trabajo con **GitHub** (repositorio, issues, ramas, PRs, conflictos y releases) junto con el desarrollo en **Python** de un sistema para la **ingesta, validación, análisis y reporte** de datos de compras de clientes.  
El sistema procesa un archivo CSV con información de ventas, valida los datos según reglas de negocio y calcula estadísticas clave como ingresos totales, producto más rentable y compras por cliente.  
Además, genera un reporte JSON con un mensaje especial si se supera un umbral de ingresos.

## Objetivos principales
- Practicar la inicialización y gestión de proyectos en GitHub con **flujo de ramas, issues, tableros y releases**.
- Implementar en Python la lectura, validación y análisis de datos.
- Desarrollar un flujo de reportes automatizado para uso empresarial.

## 📝 Instrucciones de Ejecución y Pruebas

### 1. Requisitos
- Tener instalado Python 3 en tu sistema (no es necesario entorno virtual).
- Estar ubicado en la carpeta raíz del proyecto.

### 2. Ejecución del programa
1. Abre una terminal (PowerShell o CMD).
2. Navega a la carpeta del proyecto:
   ```powershell
   cd C:\Angel\CESDE\NuevasTecnologias
   ```
3. Ejecuta el programa principal:
   ```powershell
   python main.py
   ```
   o si tienes varios Python instalados:
   ```powershell
   py main.py
   ```

### 3. Pruebas
- El programa leerá el archivo `data/compras.csv`, validará los datos y mostrará un resumen en consola.
- Se generará automáticamente un archivo `reporte.json` con los resultados.
- Puedes modificar el archivo `data/compras.csv` para probar diferentes casos y validaciones (fechas incorrectas, cantidades negativas, etc.).

### 4. Notas
- No necesitas instalar paquetes adicionales.
- Si hay errores en los datos, el programa mostrará advertencias en la consola y solo procesará los registros válidos.