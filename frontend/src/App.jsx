// Importamos los hooks básicos de React
// useState → manejar estado (datos dinámicos)
// useEffect → ejecutar código al cargar el componente
import { useEffect, useState } from "react";

function App() {

  // Estado que almacena la lista de gastos obtenidos del backend
  // Inicialmente es un array vacío
  const [expenses, setExpenses] = useState([]);

  // useEffect se ejecuta una sola vez cuando el componente se monta
  useEffect(() => {

    // Petición HTTP al backend Django
    fetch("http://127.0.0.1:8000/api/expenses/", {

      // Incluimos cookies de sesión para mantener la autenticación
      // Necesario porque Django usa autenticación basada en sesión
      credentials: "include",
    })

      // Convertimos la respuesta HTTP a formato JSON
      .then((res) => res.json())

      // Guardamos los datos recibidos en el estado expenses
      .then((data) => setExpenses(data))

      // Capturamos posibles errores de red o servidor
      .catch((err) => console.error(err));

  }, []); // Array vacío → solo se ejecuta al cargar la página

  return (
    <div>

      {/* Título principal */}
      <h1>Expenses</h1>

      {/* Renderizado condicional */}
      {/* Si no hay gastos, mostramos un mensaje */}
      {expenses.length === 0 ? (
        <p>No expenses yet</p>
      ) : (
        // Si hay gastos, los mostramos en una lista
        <ul>
          {expenses.map((exp) => (
            // key única requerida por React para optimizar renderizado
            <li key={exp.id}>
              {exp.date} - {exp.amount} - {exp.description}
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}

export default App;
