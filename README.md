# Warehouse Management API

### REST API for managing products, inventory, and orders on a warehouse using **FastAPI** and **SQLAlchemy**.

## Features

- **Product Management**: Create, read, update, and delete products.
- **Order Management**: Create and manage customer orders.
- **Inventory Management**: Automatically update stock levels upon order creation.
- **Business Logic**: Ensures enough stock before order creation, throws an error if stock is insufficient.
- **Documentation**: Automatically generated API docs with **Swagger** and **OpenAPI**.

---


##  Getting Started

### Clone the repository:
```bash
git clone https://github.com/offonyes/FastApiTestCase.git
```
```bash
cd FastApiTestCase
```


###  Use Docker!

To build and run the project via Docker:

1. Make sure Docker is installed and running.
2. Create .env fle with:
```plaintext
POSTGRES_USER=...
POSTGRES_PASSWORD=...
POSTGRES_DB=...
POSTGRES_PORT=...
POSTGRES_HOST=...
```
3. Start the app with:
   ```bash
   docker compose up --build
   ```
   or
   ```
   sudo docker compose up --build
   ```

This will run both the FastAPI server and the PostgreSQL database.

The API will be available at: **`http://localhost:8000`**

---

## API Documentation

Once the app is running, you can explore the **interactive API documentation** using:

- Swagger UI: [http://localhost:8000/docs](http://localhost:8000/docs)
- OpenAPI schema: [http://localhost:8000/openapi.json](http://localhost:8000/openapi.json)

---

##  API Endpoints

### **Products:**
- **POST** `/products/` — Create a new product.
- **GET** `/products/` — Get a list of all products.
- **GET** `/products/{id}/` — Get details of a specific product by ID.
- **PUT** `/products/{id}/` — Update an existing product by ID.
- **DELETE** `/products/{id}/` — Delete a product by ID.

### **Orders:**
- **POST** `/orders/` — Create a new order.
- **GET** `/orders/` — Get a list of all orders.
- **GET** `/orders/{id}/` — Get details of a specific order by ID.
- **PATCH** `/orders/{id}/status/` — Update the status of an order.

---

## Running Tests

To run the tests for the project, you can use `pytest`:

```bash
pytest
```

Tests include basic validation for the creation of products and orders, as well as inventory management.

---

## Technologies

- **FastAPI**: High-performance web framework for building APIs.
- **SQLAlchemy**: ORM for handling database operations.
- **PostgreSQL**: Reliable and scalable relational database.
- **Alembic**: Tool for database migrations.
- **Docker**: Containerization for easy deployment and development.
- **pytest**: Framework for unit and integration tests.

---

##  Contact

If you have any questions, feel free to reach out to:

- **Author**: Dimitri Katranidis
- **Telegram**: @dimitri_katranidis

