FROM python:3.8
LABEL maintainer="austin.dn.wu@modovision.com"

WORKDIR /flask_weather_app
COPY requirements.txt requirements.txt

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .

EXPOSE 5000 5000

# ENTRYPOINT [ "python" ]
CMD ["python", "-m", "flask", "run", "--host=0.0.0.0"]
