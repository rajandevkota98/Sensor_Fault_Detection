FROM python:3.7.6
COPY . /app1
WORKDIR /app1
RUN pip install -r requirements.txt
CMD ["python", "main.py"]