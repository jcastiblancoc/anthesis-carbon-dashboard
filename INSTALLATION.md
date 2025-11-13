# Anthesis - Installation Guide

## Quick Start (3 steps)

### 1. Extract the ZIP file
```bash
unzip anthesis-project.zip
cd anthesis
```

### 2. Make start.sh executable
```bash
chmod +x start.sh
```

### 3. Run the application
```bash
./start.sh
```

That's it! The script will automatically:
- Validate Docker installation
- Build all Docker images
- Start all services
- Run tests
- Configure SonarQube
- Display access URLs

**Total time:** ~2-3 minutes

---

## Requirements

Before running, ensure you have:
- **Docker Desktop** installed and running
- **8GB RAM** minimum
- **10GB free disk space**
- **Ports available:** 4200, 8000, 5433, 9000

---

## Access URLs

After running `./start.sh`, access:

| Service | URL | Credentials |
|---------|-----|-------------|
| Frontend | http://localhost:4200 | - |
| Backend API | http://localhost:8000/api/emissions/ | - |
| Admin Panel | http://localhost:8000/admin | admin / admin |
| SonarQube | http://localhost:9000 | admin / Anthesis2025* |

---

## Troubleshooting

### Docker not running
```bash
# Start Docker Desktop and try again
```

### Port already in use
```bash
# Stop conflicting services
lsof -ti:8000 | xargs kill -9  # Backend
lsof -ti:4200 | xargs kill -9  # Frontend
lsof -ti:9000 | xargs kill -9  # SonarQube
```

### Clean restart
```bash
docker-compose down -v
./start.sh
```

---

## What's Included

- ✓ Complete source code (Backend + Frontend)
- ✓ Docker configuration
- ✓ Environment variables (.env)
- ✓ Automated setup script (start.sh)
- ✓ Unit tests (10 tests total)
- ✓ SonarQube integration
- ✓ Complete documentation

---

## Project Structure

```
anthesis/
├── README.md              # Full documentation
├── INSTALLATION.md        # This file
├── start.sh              # Main setup script
├── docker-compose.yml    # Docker orchestration
├── .env                  # Environment variables
├── backend_anthesis/     # Django backend
└── frontend_anthesis/    # Angular frontend
```

---

## Support

For detailed documentation, see `README.md`

---

**Happy coding!**
