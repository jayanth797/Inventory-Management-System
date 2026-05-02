# 📦 Inventory Management System

A full-stack Inventory Management System built using Django, featuring authentication, analytics, REST APIs, and containerized deployment.

🚀 **Features**
*   **User Authentication**: Secure Login/Logout system.
*   **User-specific Inventory**: Data isolation ensures users only see their own products.
*   **Full CRUD**: Create, Read, Update, and Delete products.
*   **Search & Pagination**: Easily find and navigate through large inventories.
*   **Dashboard Analytics**: Visual overview of total products, quantity, and inventory value.
*   **Interactive Charts**: Data visualization using Chart.js (Bar and Pie charts).
*   **REST API**: Built with Django REST Framework for programmatic access.
*   **Dockerized**: Fully containerized with PostgreSQL for easy deployment.

🛠 **Tech Stack**
*   **Backend**: Django, Django REST Framework
*   **Database**: PostgreSQL
*   **Frontend**: HTML, Vanilla CSS, Chart.js
*   **Deployment**: Docker, Docker Compose, Gunicorn

📊 **Key Highlights**
*   Secure multi-user system with data privacy.
*   API-ready backend at `/api/products/`.
*   Scalable architecture using Docker Compose.
*   Real-time analytics dashboard with low-stock alerts.

⚙️ **Setup Instructions**

1. **Clone the repository**:
   ```bash
   git clone <your-repo-url>
   cd jaypro
   ```

2. **Start the application using Docker**:
   ```bash
   sudo docker-compose up --build -d
   ```

3. **Run migrations inside the container**:
   ```bash
   sudo docker-compose exec web python manage.py migrate
   ```

4. **Create a superuser**:
   ```bash
   sudo docker-compose exec web python manage.py createsuperuser
   ```

🌐 **API Endpoints**
*   `GET /api/products/` - List all products (Authenticated)
*   `POST /api/products/` - Create a new product
*   `GET /api/products/<id>/` - Retrieve a specific product
*   `PUT /api/products/<id>/` - Update a product
*   `DELETE /api/products/<id>/` - Delete a product

📸 **Screenshots**
*(Coming Soon: Add dashboard + product list screenshots here)*

---
👨‍💻 **Author**: Jay
