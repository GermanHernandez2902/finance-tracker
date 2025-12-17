// Importamos StrictMode desde React
// StrictMode es una herramienta de desarrollo que ayuda a detectar
// posibles problemas en el código (no afecta producción)
import { StrictMode } from "react";

// Importamos createRoot desde react-dom/client
// createRoot es la API moderna de React 18 para renderizar la app
import { createRoot } from "react-dom/client";

// Importamos los estilos globales de la aplicación
// Aquí suelen ir resets, tipografías y estilos generales
import "./index.css";

// Importamos el componente principal de la aplicación
// Este es NUESTRO App.jsx (no el demo de Vite)
import App from "./App.jsx";

// Buscamos el div con id="root" que está en index.html
// Dentro de este nodo React va a montar toda la aplicación
const rootElement = document.getElementById("root");

// Creamos la raíz de React y renderizamos la aplicación
createRoot(rootElement).render(
  <StrictMode>
    {/* App es el componente raíz de toda la aplicación */}
    {/* Desde aquí se renderiza TODO el frontend */}
    <App />
  </StrictMode>
);
