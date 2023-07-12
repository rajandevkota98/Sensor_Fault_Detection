FROM python:3.7.6
RUN apt update -y  && install awscli -y
COPY . /app1
WORKDIR /app1
RUN pip install -r requirements.txt
CMD ["python", "main.py"]
