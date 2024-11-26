
# Proyecto de Gestión y Análisis de Clientes Bancarios

**Requisitos Previos:**
- Python 3.8+
- Node.js 14+
- SQLite

---

## Estructura del Proyecto

### **Estructura Principal**
```
.
├── backend/
│   ├── clientes/         # App principal de Django
│   ├── db.sqlite3        # Base de datos (SQLite)
│   ├── manage.py         # Administrador de Django
├── frontend/
│   ├── src/              # Código fuente de React
│   ├── public/           # Archivos estáticos de React
│   ├── package.json      # Dependencias del frontend
├── clientes_banco.csv    # Archivo CSV de entrada
├── requirements.txt      # Dependencias del backend
```

### **Archivos Clave**
- **backend/clientes/models.py**: Define el modelo `Cliente`.
- **frontend/src/Statistics.js**: Componente que consume el endpoint `/stats/`.

---

## Backend

### **Modelo de Datos**
El modelo `Cliente` representa los datos del CSV con campos:
- `cliente_id`: Identificador único.
- `edad`: Edad del cliente.
- `genero`: Género (opciones: `Masculino`, `Femenino`, `No especificado`).
- `saldo`: Saldo promedio.
- `activo`: Estado (`True` o `False`).
- `nivel_de_satisfaccion`: Escala del 1 al 5.

### **API (Django REST Framework)**
#### **Endpoints Principales:**
- **`/clientes/`**: CRUD de clientes.
- **`/clientes/stats/`**: Estadísticas de clientes.

### **Limpieza de Datos**
El script `limpiar.py` automatiza la limpieza del archivo CSV:
- Elimina duplicados.
- Maneja valores nulos.
- Guarda un archivo limpio para cargarlo en la base de datos.

### **Carga de Datos**
El comando de Django `cargar_clientes` elimina los datos previos y carga el CSV limpio en la base de datos.

---

## 4. Frontend

### **Componentes Clave**
- **`Statistics.js`**:
  - Llama al endpoint `/clientes/stats/`.
  - Muestra estadísticas con un diseño mejorado (tarjetas y listas con Bootstrap).

### **Estilos**
- Fuente: **Roboto** (Google Fonts).
- Diseño: **Bootstrap**.

---

## 5. Instalación

### **Backend**
1. Crear un entorno virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate  # macOS/Linux
   venv\Scripts\activate     # Windows
   ```
2. Instalar dependencias:
   ```bash
   pip install -r requirements.txt
   ```

3. Realizar migraciones:
   ```bash
   python manage.py migrate
   ```

4. Crear un superusuario:
   ```bash
   python manage.py createsuperuser
   ```

5. Ejecutar el servidor:
   ```bash
   python manage.py runserver
   ```

### **Frontend**
1. Instalar dependencias:
   ```bash
   npm install
   ```

2. Ejecutar el servidor de desarrollo:
   ```bash
   npm start
   ```

---

## 6. Ejecución

### **Backend**
- Ejecutar en `http://localhost:8000/`.

### **Frontend**
- Acceder a `http://localhost:3000/`.

### **Ejemplo de Uso**
- Consultar estadísticas en `/clientes/stats/` desde el frontend.

---
