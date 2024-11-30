FROM python:3.11.2-slim

WORKDIR /app

COPY inferencia.py .
COPY model.pkl .
COPY scaler.pkl .
COPY imputer.pkl .
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "inferencia.py"]
