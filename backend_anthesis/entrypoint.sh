#!/bin/bash

set -e

echo "Starting Anthesis Backend..."
echo ""

echo "Waiting for database..."
while ! nc -z db 5432; do
  sleep 0.1
done
echo "[OK] Database is ready!"
echo ""

echo "Running migrations..."
python manage.py migrate --noinput
echo "[OK] Migrations completed!"
echo ""

echo "Seeding database..."
python seeder.py
echo "[OK] Database seeded!"
echo ""

echo "Running tests with coverage..."
pytest --cov=api --cov-report=xml --cov-report=html --cov-report=term-missing
TEST_EXIT_CODE=$?

if [ $TEST_EXIT_CODE -eq 0 ]; then
    echo ""
    echo "[OK] All tests passed!"
    echo "Coverage report generated"
    echo ""
else
    echo ""
    echo "ERROR: Tests failed! Exit code: $TEST_EXIT_CODE"
    echo "WARNING: Starting server anyway for debugging..."
    echo ""
fi

echo "Starting Gunicorn server..."
exec gunicorn config.wsgi:application --bind 0.0.0.0:8000 --workers 3 --timeout 60 --access-logfile - --error-logfile -
