FROM python:3.12-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH=/app

COPY requirements*.txt ./

RUN pip install --no-cache-dir --retries 10 --timeout 300 --index-url https://download.pytorch.org/whl/cpu torch
RUN pip install --no-cache-dir --retries 10 --timeout 300 -r requirements.txt

COPY . .

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
