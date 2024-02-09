FROM python:3.12   

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1  

COPY . .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

WORKDIR /pythagore
EXPOSE 8000  
RUN chmod +x migrate.sh
ENTRYPOINT ["./migrate.sh"]
CMD ["gunicorn", "pythagore.wsgi:application", "--bind", "0.0.0.0:8000", "--log-level", "debug", "--timeout", "90"]
