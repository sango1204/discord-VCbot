FROM python:3.11

WORKDIR /app

COPY requirements.txt .
COPY voice_bot.py .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "voice_bot.py"]
