FROM python:3.9

EXPOSE 8080
RUN mkdir -p /usr/src/test-app/

WORKDIR /usr/src/test-app/

COPY ./ ./
RUN pip install --upgrade pip

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt