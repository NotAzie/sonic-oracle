FROM python:3.12-slim
WORKDIR /app
COPY pyproject.toml .
COPY src ./src
COPY config ./config
COPY main.py .
RUN pip install --no-cache-dir .
ENTRYPOINT ["python", "main.py"]
CMD ["--radar"]
