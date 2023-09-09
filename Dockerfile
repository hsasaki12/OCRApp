FROM python:3.9-slim

# Install Tesseract and Japanese and English language packs
RUN apt-get update && apt-get install -y tesseract-ocr tesseract-ocr-jpn tesseract-ocr-eng

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY ./app /app

CMD ["python", "main.py"]
