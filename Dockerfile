FROM python:3.9-slim
WORKDIR /app
COPY . /app
RUN apt-get update && \
    apt-get install -y && \
    apt-get clean && \
    pip install --upgrade pip && \
    pip install -r requirements.txt && \
    python -m playwright install && \
    python -m playwright install-deps

CMD ["pytest", "--html=reports/report.html"]