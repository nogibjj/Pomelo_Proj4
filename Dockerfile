FROM python:3.8

WORKDIR /app

COPY Fast_API.py main.py requirements.txt gcp.json /app/

RUN pip install --no-cache-dir --upgrade -r requirements.txt

EXPOSE 8080

CMD [ "Fast_API.py" ]

ENTRYPOINT [ "python" ]

# CMD ["uvicorn", "Fast_API:app", "--host=0.0.0.0", "--port=80"]