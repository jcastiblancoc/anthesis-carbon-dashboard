# Anthesis - Carbon Emissions Dashboard

Anthesis app is a Knowledge test to apply to the backend role on Anthesis

---

## About

Anthesis Knowledge Test is a full-stack web application for tracking, analyzing, and visualizing carbon emissions data across different countries, activities, and emission types.

**Key Features:**
- Interactive dashboards with dynamic charts
- Advanced filtering by country, activity, emission type, and year
- Automatic data aggregation
- Comprehensive automated testing (100% backend coverage)
- Integrated code quality analysis with SonarQube
- Fully containerized with Docker

---

## Technology Stack

**Backend:**
- Python 3.12
- Django 5.1 + Django REST Framework
- PostgreSQL 16
- pytest + pytest-cov

**Frontend:**
- Angular 19
- TypeScript
- Chart.js
- Jasmine + Karma

**DevOps:**
- Docker + Docker Compose
- SonarQube
- Nginx

---

## Requirements

Before running the application, ensure your system has:

- **Docker Desktop** installed and running
- **8GB RAM** minimum
- **10GB free disk space**
- **Ports available:** 4200, 8000, 5433, 9000

---

## Quick Start

### One Command Setup

```bash
./start.sh
```

The script automatically:
1. Validates Docker installation
2. Builds and starts all services
3. Runs database migrations and seeds data
4. Executes 8 backend tests
5. Configures SonarQube (password + token)
6. Executes 2 frontend tests
7. Runs code quality analysis
8. Displays access URLs

**Total time:** 2-3 minutes

---

## Access URLs

After running `./start.sh`:

| Service | URL | Credentials |
|---------|-----|-------------|
| Frontend | http://localhost:4200 | - |
| Backend API | http://localhost:8000/api/emissions/ | - |
| Admin Panel | http://localhost:8000/admin | admin / admin |
| SonarQube | http://localhost:9000 | admin / Anthesis2025* |

**SonarQube Projects:**
- Backend: http://localhost:9000/dashboard?id=anthesis-backend
- Frontend: http://localhost:9000/dashboard?id=anthesis-frontend

---

## Project Structure

```
anthesis/
├── README.md
├── docker-compose.yml
├── start.sh
├── sonar-backend.properties
├── sonar-frontend.properties
│
├── backend_anthesis/
│   ├── api/
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── serializers.py
│   │   ├── filters.py
│   │   └── tests/
│   ├── config/
│   ├── Dockerfile
│   ├── entrypoint.sh
│   ├── requirements.txt
│   └── pytest.ini
│
└── frontend_anthesis/
    ├── src/
    │   ├── app/
    │   │   ├── components/
    │   │   ├── services/
    │   │   └── models/
    │   └── environments/
    ├── Dockerfile
    ├── nginx.conf
    ├── karma.conf.js
    └── package.json
```

---

## API Endpoints

**Base URL:** `http://localhost:8000/api/`

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/emissions/` | List all emissions |
| GET | `/emissions/?country=UK` | Filter by country |
| GET | `/emissions/?year=2023` | Filter by year |
| GET | `/emissions/?activity=Transport` | Filter by activity |
| GET | `/emissions/{id}/` | Get specific emission |

---

## Testing

### Backend Tests

```bash
docker-compose exec backend pytest
```

**Results:**
- 8 tests (100% passing)
- 2 tests per module (models, serializers, views, filters)
- Reports: `backend_anthesis/htmlcov/index.html`

### Frontend Tests

```bash
cd frontend_anthesis
npm test
```

**Results:**
- 2 tests (100% passing)
- Tests EmissionService (fetch data + error handling)
- Reports: `frontend_anthesis/coverage/index.html`

---

## Docker Commands

```bash
# View logs
docker-compose logs -f backend
docker-compose logs -f frontend

# Stop services
docker-compose down

# Restart services
docker-compose restart

# View status
docker-compose ps

# Clean restart (removes all data)
docker-compose down -v
./start.sh
```

---

## License

This project is private and confidential.

---

## Authors

Jeisson Castiblanco
