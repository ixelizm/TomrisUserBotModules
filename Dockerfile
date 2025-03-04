# Python 3.10 tabanlı bir imaj kullan
FROM python:3.10

# Çalışma dizinini belirle
WORKDIR /tomris

# Bağımlılıkları yükle
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Uygulama dosyalarını kopyala
COPY . .

# Uvicorn ile FastAPI uygulamasını başlat
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8080"]
