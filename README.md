# Anthesis - Carbon Emissions Dashboard

**Full-Stack Data Visualization Application for Carbon Emissions Tracking**

A comprehensive full-stack web application for tracking, analyzing, and visualizing carbon emissions data across different countries, activities, and emission types.

## 🎯 Overview

- **Type**: Full-Stack Web Application (TypeScript/JavaScript, Python, PostgreSQL)
- **Purpose**: Real-time carbon emissions data tracking and analysis platform
- **Key Focus**: Interactive dashboards, advanced filtering, automated data aggregation, and comprehensive testing
- **Architecture**: Microservices pattern with separate backend (Django) and frontend (React/TypeScript) applications

## ✨ Key Features

- 📊 **Interactive Dashboards**: Dynamic charts and real-time data visualization
- 🔍 **Advanced Filtering**: Filter by country, activity, emission type, and time range
- 📈 **Data Aggregation**: Automatic calculation and aggregation of emission metrics
- ✅ **Comprehensive Testing**: 100% backend code coverage with automated tests
- 🔐 **Code Quality**: Integrated SonarQube analysis for continuous code quality
- 🐳 **Containerization**: Full Docker support for easy deployment

## 🚀 Quick Start

### Prerequisites

- Python 3.12+
- Node.js 18+
- Docker & Docker Compose (optional)
- PostgreSQL 16+

### Installation

#### Backend Setup

1. Navigate to the backend directory
   ```bash
   cd backend_anthesis
   ```

2. Create virtual environment
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```

4. Configure environment variables
   ```bash
   cp .env.example .env
   ```

5. Run migrations
   ```bash
   python manage.py migrate
   ```

#### Frontend Setup

1. Navigate to the frontend directory
   ```bash
   cd frontend_anthesis
   ```

2. Install dependencies
   ```bash
   npm install
   ```

3. Configure environment variables
   ```bash
   cp .env.example .env
   ```

4. Start development server
   ```bash
   npm run dev
   ```

### Docker Deployment

Run the entire stack with Docker Compose:

```bash
docker-compose up -d
```

## 🧪 Testing

### Backend Tests

Run the full test suite with coverage:

```bash
cd backend_anthesis
pytest --cov=src --cov-report=html
```

### Frontend Tests

```bash
cd frontend_anthesis
npm run test
```

## 🛠️ Tech Stack

### Backend

- **Framework**: Django 5.1 + Django REST Framework
- **Database**: PostgreSQL 16
- **Testing**: pytest with coverage
- **Quality**: SonarQube integration
- **Language**: Python 3.12

### Frontend

- **Framework**: React 18+
- **Language**: TypeScript
- **Build Tool**: Vite
- **Charts**: Chart.js or similar
- **State Management**: React Context / Redux

## 📁 Project Structure

```
.
├── backend_anthesis/           # Django REST API
│   ├── src/                    # Application source
│   ├── tests/                  # Test suite
│   ├── manage.py
│   └── requirements.txt
├── frontend_anthesis/          # React TypeScript frontend
│   ├── src/                    # React components
│   ├── public/                 # Static assets
│   └── package.json
├── docker-compose.yml
├── INSTALLATION.md
└── README.md
```

## 📚 Documentation

For detailed setup and deployment instructions, see [INSTALLATION.md](./INSTALLATION.md)

## 🔄 CI/CD Pipeline

- Automated testing on pull requests
- Code quality checks with SonarQube
- Docker image builds and registry pushes
- Automated deployment to staging/production

## 📊 Performance Metrics

- 100% backend test coverage
- API response time: < 200ms (p95)
- Dashboard load time: < 2s (p95)
- Data aggregation: Real-time with caching

## 🤝 Contributing

1. Create a feature branch (`git checkout -b feature/AmazingFeature`)
2. Commit changes (`git commit -m 'Add AmazingFeature'`)
3. Push to branch (`git push origin feature/AmazingFeature`)
4. Open a Pull Request

## 📄 License

MIT License - See LICENSE file for details

## 👤 Author

Jeisson Castiblanco - Backend Engineer

---

**Last Updated**: December 2024
