#mcr.microsoft.com/playwright/python:v1.51.0-noble
FROM python:3.11-slim

#Playwright required dependencies
RUN apt-get update && apt-get install -y \
    wget \
    gnupg \
    && rm -rf /var/lib/apt/lists/*

#set working dir inside of an image
WORKDIR /app

#copying required project files
COPY requirements.txt .
COPY tests/ ./tests/
COPY pages/ ./pages/
COPY .env .

#python project dependencies
RUN pip install --no-cache-dir -r requirements.txt

#browsers for playwright
RUN playwright install --with-deps chromium

#default command after container start
CMD ["pytest", "-c", "tests/pytest.ini"]