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

## 👤 Autor

**German Hernández Sarmiento**  
Proyecto Final – Máster en Desarrollo Full Stack

---

