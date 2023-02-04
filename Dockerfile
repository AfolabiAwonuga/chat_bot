FROM python:3.9-slim-buster 

EXPOSE 8501
  
WORKDIR /app

COPY  requirements.txt requirements.txt

RUN apt-get update && apt-get install -y \
    build-essential \
    software-properties-common \
    && python -m pip install --upgrade pip \
    && pip install --default-timeout=200 --no-cache-dir -r requirements.txt \ 
    && rm -rf /var/lib/apt/lists/*

COPY . .

RUN python -m nltk.downloader punkt \
    && python -m nltk.downloader stopwords \
    && python train_set.py

CMD ["streamlit", "run", "bot.py"]
