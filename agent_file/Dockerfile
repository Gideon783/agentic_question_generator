FROM python:3.13-slim
WORKDIR /app

RUN apt-get update && apt-get install -y curl wget gnupg libglib2.0-0 libnss3 libatk-bridge2.0-0 libgtk-3-0 libx11-xcb1 libxcb-dri3-0 libdrm2 libxshmfence1 libxrandr2 libxdamage1 libasound2 fonts-liberation libappindicator3-1 lsb-release && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

RUN playwright install --with-deps

RUN adduser --disabled-password --gecos "" myuser && \
    chown -R myuser:myuser /app

COPY . .

COPY .env .env

USER myuser

ENV PATH="/home/myuser/.local/bin:$PATH"

RUN playwright install

CMD ["sh", "-c", "uvicorn main:app --host 0.0.0.0 --port 8000"]