# GraphLab TC — UNAH

Proyecto #6 de ISC-312 Teoría de la Computación: explorador de grafos, alcanzabilidad y problemas de decisión.

## Estado actual

**Versión inicial 0.1.0:** editor de grafos dirigidos funcional, visualización interactiva, guardar/cargar JSON, validaciones y pruebas iniciales.

**Pendiente:** algoritmos BFS/DFS y Vertex Cover del Desarrollador 1; visualización de recorridos y comparador del Desarrollador 2.

## Ejecutar en Windows (PowerShell en VS Code)

Requiere Python 3.11 o superior y Git instalado.

```powershell
py -3 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m streamlit run streamlit_app.py
```

Abrir la dirección local que indique la terminal (normalmente `http://localhost:8501`).

## Ejecutar pruebas

```powershell
.\.venv\Scripts\python.exe -m pytest -q
```

## Enviar el proyecto a GitHub

1. Crear un repositorio vacío llamado `GraphLab-TC-UNAH` (sin inicializar README ni `.gitignore`).
2. Abrir terminal en esta carpeta y ejecutar:

```powershell
git init
git branch -M main
git add .
git commit -m "Inicializar GraphLab TC y editor de grafos"
git remote add origin https://github.com/TU-USUARIO/GraphLab-TC-UNAH.git
git push -u origin main
```

Cambiar `TU-USUARIO` por el usuario real. Nunca subir contraseñas o tokens. Si Git solicita autenticación, completar el inicio de sesión por el método oficial.

## Despliegue web

Una vez integrado y probado, acceder a https://share.streamlit.io/ y seleccionar el repositorio GitHub, rama `main` y archivo `streamlit_app.py`.

## Estructura

- `core`: modelo y validaciones.
- `algoritmos`: implementación matemática (Dev. 1).
- `interfaz`: controles (Dev. 2).
- `utilidades`: visualización y métricas (Dev. 2).
- `docs`: acuerdos y manuales.
- `tests`: pruebas automatizadas.

## Requisitos académicos

El informe técnico cubrirá los fundamentos de autómatas, lenguajes, computabilidad, reducción y complejidad, además de los módulos funcionales. Se documentarán al menos 10 casos de prueba con resultados reales.
