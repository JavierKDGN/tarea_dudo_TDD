# TDD: Simulador de Juego "Dudo"

## Instrucciones de ejecución:

### En Linux:

Una vez clonado el proyecto, para correr los tests bastará con ejecutar el siguiente comando en el terminal:
```bash
[ruta-repositorio]$ ./test.sh
```
Este comando automáticamente creará un entorno virtual (si este no existía ya), descargará las dependencias del proyecto y mostrará el resultado de los tests e información de cobertura.

### En Windows:

Si por otra parte está ejecutando el proyecto en Windows, deberá crear el entorno virtual, descargar las dependencias (usando el archivo `requirements.txt`) y ejecutar `pytest` manualmente. Para esto último, ejecute:
```power-shell
[ruta-repositorio]> python3 -m pytest --cov='src' --cov-report='term-missing'
```