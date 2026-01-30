# 💰 Finance-Tracker

**Finance-Tracker** es una aplicación web de gestión de finanzas personales desarrollada como **Proyecto Final del Máster en Desarrollo Full Stack**.  
Permite a los usuarios registrar ingresos y gastos, visualizar su balance financiero y mantener un control claro y estructurado de su economía.

La aplicación integra un **backend robusto en Django** con autenticación basada en sesiones y un **frontend desacoplado en React**, comunicados mediante una API REST segura.

👉 **Demo en producción:**  
🔗 https://finance-tracker-jl22.onrender.com

---

## 🚀 Características principales

- 🔐 **Autenticación de usuarios** mediante sesiones (Django Auth)
- 📊 **Dashboard financiero** con balance automático
- 💵 Registro y visualización de **ingresos**
- 💸 Registro y visualización de **gastos**
- ⚖️ Cálculo dinámico del **balance total**
- 🧠 Separación clara entre frontend y backend
- 🌐 Aplicación desplegada en producción

---

## 🖥️ Vista general del sistema

### Landing pública
- Página de bienvenida
- Acceso a inicio de sesión
- Redirección segura al dashboard tras autenticación

### Dashboard (protegido)
- Acceso exclusivo para usuarios autenticados
- Visualización de:
  - Balance total
  - Total de ingresos
  - Total de gastos
- Listado detallado de ingresos y gastos
- Gestión de sesión (logout)

---

## 🧩 Arquitectura del proyecto

El sistema sigue una **arquitectura desacoplada frontend/backend**:

### 🔙 Backend
- **Framework:** Django  
- **Autenticación:** Django Sessions  
- **API REST:** Endpoints protegidos por sesión  
- **Base de datos:** SQLite (entorno académico)  
- **Gestión de estáticos:** WhiteNoise  

### 🔜 Frontend
- **Framework:** React  
- **Bundler:** Vite  
- **Consumo de API:** Fetch API con cookies (`credentials: include`)  
- **Build de producción:** servido como archivos estáticos por Django  


---

## 🔐 Seguridad y autenticación

- Acceso al dashboard restringido a usuarios autenticados
- Uso de **cookies seguras** y protección CSRF
- Sesiones gestionadas íntegramente por Django
- Frontend sin credenciales hardcodeadas

---

## 🌍 Despliegue

La aplicación está desplegada en **Render** y accesible públicamente:

🔗 **Producción:** https://finance-tracker-jl22.onrender.com

El flujo de despliegue incluye:
- Build del frontend en React
- Copia del build a `/static/frontend`
- Servicio del frontend mediante Django + WhiteNoise

---

## 🎓 Contexto académico

Este proyecto fue desarrollado como **Proyecto Final del Máster en Desarrollo Full Stack**, demostrando competencias en:

- Desarrollo backend con Django
- Desarrollo frontend con React
- Integración frontend-backend mediante API REST
- Autenticación y seguridad
- Despliegue en entorno de producción
- Arquitectura limpia y escalable

---
⚙️ Instalación y ejecución en local

Este proyecto está estructurado con un backend en Django que sirve directamente el frontend React ya compilado como archivos estáticos.

🔎 Importante:
El repositorio no incluye el código fuente del frontend React, únicamente el build final (dist) integrado dentro del backend.
Por lo tanto, no es necesario ni posible ejecutar React en local desde este repositorio.

📋 Requisitos previos

Python 3.10 o superior

Conda (Anaconda o Miniconda)

Git

📥 Clonar el repositorio
git clone https://github.com/GermanHernandez2902/finance-tracker.git
cd finance-tracker

🐍 Backend (Django)

El backend se ejecuta utilizando un entorno Conda.

Crear el entorno (si no existe):

conda create -n finance-tracker python=3.10


Activar el entorno:

conda activate finance-tracker


Instalar dependencias:

pip install -r requirements.txt


Ejecutar migraciones:

python manage.py migrate


Iniciar el servidor:

python manage.py runserver

🌐 Acceso a la aplicación

Una vez iniciado el servidor, la aplicación completa estará disponible en:

http://127.0.0.1:8000/


Django servirá automáticamente el frontend React desde:

finance-tracker/static/frontend/

⚛️ Nota sobre el frontend (React)

Durante la fase de desarrollo:

El backend Django se ejecutaba en una terminal utilizando Conda

El frontend React se desarrolló y ejecutó en una terminal separada utilizando pnpm

Para producción, el frontend fue compilado (pnpm build) y el resultado (dist) se integró manualmente dentro del backend

Este enfoque refleja un flujo profesional real de integración Full Stack, donde el frontend desacoplado se entrega finalmente como build estático.

---
## 👤 Autor

**German Hernández Sarmiento**  
Proyecto Final – Máster en Desarrollo Full Stack

---

