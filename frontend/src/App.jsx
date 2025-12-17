// Importamos los hooks básicos de React
// useState: permite manejar estado dentro del componente
// useEffect: permite ejecutar código cuando el componente se monta
import { useEffect, useState } from "react";

function App() {

  // Definimos un estado llamado "expenses"
  // Aquí se almacenará la lista de gastos obtenidos desde Django
  // Se inicializa como un array vacío porque aún no hay datos cargados
  const [expenses, setExpenses] = useState([]);

  // useEffect se ejecuta automáticamente cuando el componente se renderiza por primera vez
  // El array de dependencias vacío [] indica que se ejecuta SOLO una vez
  useEffect(() => {

    // Petición al backend usando una ruta relativa
    // El proxy de Vite se encarga de redirigirla a Django
    // Esto evita URLs hardcodeadas y facilita el despliegue
    fetch("/api/expenses/", {

      // credentials: "include" permite enviar las cookies de sesión
      // Es necesario porque Django usa autenticación basada en sesiones
      credentials: "include",
    })

      // Convertimos la respuesta HTTP en un objeto JavaScript (JSON)
      .then((res) => res.json())

      // Guardamos los datos recibidos en el estado "expenses"
      // Esto provoca que React vuelva a renderizar el componente
      .then((data) => setExpenses(data))

      // Capturamos posibles errores de red o del servidor
      // Esto evita fallos silenciosos y facilita el debugging
      .catch((error) => {
        console.error("Error fetching expenses:", error);
      });

  }, []);

  return (
    // Contenedor principal con padding para mejorar la presentación visual
    <div style={{ padding: "2rem" }}>

      {/* Título principal de la aplicación */}
      <h1>Finance Tracker</h1>

      {/* Renderizado condicional */}
      {/* Si el usuario no tiene gastos, mostramos un mensaje */}
      {expenses.length === 0 ? (
        <p>No expenses yet</p>
      ) : (
        // Si existen gastos, los mostramos en una lista
        <ul>
          {expenses.map((exp) => (
            // React necesita una key única por cada elemento
            // Usamos el id del gasto (pk del backend)
            <li key={exp.id}>
              {exp.date} – ${exp.amount} – {exp.description}
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}

export default App;
