FROM python:3.12-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH=/app

COPY requirements*.txt ./

# Task 65.9.1F - single, version-pinned source of truth for the CPU-only
# Torch dependency (see backend/requirements-torch-cpu.txt for the full
# root-cause/provenance investigation of the previously unpinned,
# duplicated `pip install ... torch` command this replaces).
RUN pip install --no-cache-dir --retries 10 --timeout 300 -r requirements-torch-cpu.txt
RUN pip install --no-cache-dir --retries 10 --timeout 300 -r requirements.txt

COPY . .

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
