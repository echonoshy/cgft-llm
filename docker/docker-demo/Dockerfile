FROM python:3.10-slim 

LABEL maintainer="panhu"
LABEL version=1.0
LABEL desc="A docker bigv"

WORKDIR /app

ARG APP_VER=1.0
ENV APP_ENV=1.0

COPY . /app/
EXPOSE 5000



HEALTHCHECK --interval=10s --timeout=3s --retries=3 CMD curl --fail http://localhost:5000/ || exit 1

RUN pip install flask


CMD ["python", "app.py"]
