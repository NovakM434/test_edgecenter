FROM python:3.10

RUN apt-get update && \
    apt-get install -y --no-install-recommends gnupg2 && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["pytest", "--browser=remote", "ui/tests/"]
