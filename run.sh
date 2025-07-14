#!/bin/bash
set -e
bash install.sh
source venv/bin/activate
nohup uvicorn main:app --host 0.0.0.0 --port 8000 &
echo "SUCCESS: FastAPI service started on port 8000"