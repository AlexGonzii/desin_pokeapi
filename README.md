# ⚡ PokéAPI Desktop App

Esta es una aplicación de escritorio hecha en Python con PySide6 que permite buscar información de Pokémon usando la PokéAPI.

La idea de esta app es poder escribir el nombre o ID de un Pokémon y ver sus datos de forma rápida en una interfaz sencilla y visual.

---

## 🧠 ¿Cómo funciona?

La aplicación está conectada a la PokéAPI, una API pública que contiene información de todos los Pokémon.

Cuando el usuario escribe un nombre o número:
- Se hace una petición a la API
- Se obtiene la información del Pokémon
- Se muestra en la interfaz

---

## 🖥️ Interfaz

La aplicación tiene una interfaz muy simple:
- Un campo de texto para escribir el Pokémon
- Un botón para buscar
- Un área donde se muestran los datos

---

## 🧱 Estructura del proyecto

El proyecto está organizado usando el patrón MVC:

- **Vista (ui_main.py)** → Interfaz gráfica
- **Lógica (logic.py)** → Maneja las acciones
- **Main (main.py)** → Inicia la aplicación

Esto hace que el código sea más ordenado y fácil de mantener.

---

## ⚙️ Tecnologías usadas

- Python  
- PySide6  
- PokéAPI  
- PyInstaller (para generar el .exe)  
- GitHub Actions (para automatizar la compilación)

---

## 🚀 Compilación automática

Cada vez que se sube el proyecto a GitHub, se ejecuta un proceso automático que:

- Instala dependencias  
- Compila la aplicación  
- Genera un archivo .exe listo para usar  

---

## 📌 Objetivo

Este proyecto se ha creado como práctica para:

- Aprender a trabajar con APIs  
- Usar interfaces gráficas en Python  
- Aplicar arquitectura MVC  
- Automatizar builds con GitHub Actions  

---

## 💡 En resumen

Es una pequeña Pokédex de escritorio que te permite consultar Pokémon de forma rápida y sencilla desde una app hecha en Python.
