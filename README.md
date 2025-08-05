# FastAPI Auth Clean Architecture

API REST de autenticación construida con FastAPI, siguiendo principios de Clean Architecture y patrones de diseño para un código limpio, mantenible y escalable.

---

## Funcionalidad

Esta API permite autenticar usuarios mediante dos métodos configurables en tiempo de ejecución:

- **JWT**: Genera un token JWT simulado para el usuario.
- **Session**: Genera una cookie de sesión simulada.

---

## Patrones de Diseño Utilizados

- **Strategy**: Permite seleccionar dinámicamente la estrategia de autenticación (JWT o Session) sin modificar la lógica del servicio.
- **Repository**: Abstrae el acceso a datos, desacoplando la lógica de negocio del almacenamiento.
- **Service Layer**: Centraliza la lógica de negocio, coordinando repositorios y estrategias.
- **Clean Architecture**: Separación clara de capas (domain, services, repositories, api) para facilitar mantenimiento y pruebas.

---

## Estructura

app/
├── api/ # Rutas FastAPI
├── domain/ # Modelos y patrones (estrategias)
├── repositories/ # Acceso a datos
├── services/ # Lógica de negocio
└── main.py # Punto de entrada
tests/ # Pruebas automatizadas


---

## Tests y Cobertura

- Tests automatizados con `pytest` y `TestClient` de FastAPI.
- Cobertura del 100% asegurada con `coverage.py`.

---

## Cómo usar

1. Crear entorno virtual e instalar dependencias:

```bash
python -m venv env
source env/bin/activate  # Linux/macOS
.\env\Scripts\activate   # Windows

pip install -r requirements.txt

2. Ejecutar servdor
uvicorn app.main:app --reload

3. Probar endpoint /login con JSON
{
  "username": "JohnDoe",
  "password": "123456",
  "method": "jwt"
}
