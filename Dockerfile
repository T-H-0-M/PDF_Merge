# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.11.3

COPY requirements.txt .
RUN python -m pip install -r requirements.txt

WORKDIR /app
COPY . /app

COPY main.py .
CMD ["python", "main.py"]
