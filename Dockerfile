
FROM python:3.10-slim
LABEL authors="santiago"

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir --upgrade -r requirements.txt

CMD ["python", "gerenciador.py"]