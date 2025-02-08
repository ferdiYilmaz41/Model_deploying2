# Python base image
FROM python:3.8-slim

# Çalışma dizini oluştur
WORKDIR /app

# Bağımlılıkları kopyala ve kur
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt


# Tüm proje dosyalarını kopyala
COPY . .

# Uygulamayı çalıştır
EXPOSE 7001
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "7001"]