FROM python:3.9-slim-buster

# EXPOSE 8501

WORKDIR /app

COPY  r.txt requirements.txt

RUN pip install --upgrade pip

RUN pip3 install -r requirements.txt

COPY . .

RUN python -m nltk.downloader punkt

RUN python -m nltk.downloader stopwords

RUN python train_set.py

CMD ["streamlit", "run", "bot.py"]
