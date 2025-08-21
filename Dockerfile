FROM python:3.11-slim

WORKDIR /data
COPY ./data/ /data/

WORKDIR /app
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY ./app/ /app/

RUN python -m nltk.downloader -d /usr/local/share/nltk_data vader_lexicon
ENV NLTK_DATA=/usr/local/share/nltk_data

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]