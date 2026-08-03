#!/usr/bin/env bash
set -o errexit

echo "Creating database tables..."
python -m app.database.init_db

echo "Starting SALIKSIK API..."
exec uvicorn app.main:app --host 0.0.0.0 --port "$PORT"