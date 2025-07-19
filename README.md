# Evaluación Módulo 3

## Gestor de Tareas – Consola (Python)
Aplicación ligera de línea de comandos que permite agregar, listar, marcar como completadas y eliminar tareas usando solo Python estándar.
Ideal para quienes necesitan un organizador simple y portable sin depender de herramientas externas.

## Objetivo
Poner en práctica los conceptos fundamentales de Python:  
Estructuras de datos: list y dict  
Funciones y modularidad  
Control de flujo (if, while, try/except)  
Manejo básico de archivos (persistencia al salir)

--- Gestor de Tareas ---  
1. Agregar tarea  
2. Ver tareas  
3. Marcar tarea como completada  
4. Eliminar tarea  
5. Salir  
Elige una opción:

Cuando eliges salir (5) el programa ejecuta:
os.system(f'echo "{str(tareas)}" >> evaluación_de_modulo_3.txt')

Esto añade la lista completa de tareas al archivo evaluación_de_modulo_3.txt (una línea por ejecución), evitando pérdida de datos.