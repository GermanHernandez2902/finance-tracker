// Importa la función defineConfig de Vite
// Se usa para obtener autocompletado y validación de configuración
import { defineConfig } from "vite"

// Plugin oficial de React para Vite
// Permite que Vite entienda JSX y React Fast Refresh
import react from "@vitejs/plugin-react"

// Exportamos la configuración de Vite
export default defineConfig({

  // Plugins que usa Vite
  // En este caso, solo el plugin de React
  plugins: [react()],

  // Configuración del servidor de desarrollo de Vite
  server: {

    // Definimos reglas de proxy
    // El proxy permite redirigir peticiones del frontend al backend
    proxy: {

      // Todas las peticiones que empiecen por /api
      // serán redirigidas automáticamente al backend Django
      "/api": {

        // Dirección del backend Django (servidor de desarrollo)
        target: "http://127.0.0.1:8000",

        // changeOrigin hace que la petición parezca venir del mismo origen
        // Evita problemas de CORS (CORS es un mecanismo de seguridad del navegador que controla qué 
        // orígenes pueden acceder a los recursos de un servidor.) y headers incorrectos
        changeOrigin: true,
      },
    },
  },
})
