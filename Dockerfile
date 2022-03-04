FROM python:3.7

ENV PYTHONPATH src/

ENV API_PORT=8080
ENV API_BASE_URL=0.0.0.0
ENV API_DEBUG_MODE="False"

EXPOSE 8080

WORKDIR /app

COPY ./requirements.txt ./requirements.txt

RUN python -m pip install --upgrade pip && \
  pip install -r requirements.txt

COPY . .

CMD python src/__main__.py
