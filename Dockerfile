# Python base image
FROM python:3.10-slim

# Çalışma dizini oluştur
WORKDIR /app

# Bağımlılıkları kopyala ve kur
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && \
    pip install tensorflow==2.18.0 -f https://storage.googleapis.com/tensorflow/linux/cpu/tensorflow_cpu-2.18.0-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl && \
    pip install --no-cache-dir -r requirements.txt
    

# Tüm proje dosyalarını kopyala
COPY . .

# Uygulamayı çalıştır
EXPOSE 7001
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "7001"]