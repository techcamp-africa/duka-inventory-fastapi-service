FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

# WORKDIR /app/

COPY  . /app

COPY ./requirements.txt .

# upgrade pip and install required python packages
RUN pip install -U pip
RUN pip install -r requirements.txt
# RUN pip install argon2_cffi
