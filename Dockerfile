from python:3.9

WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

# EXPOSE 80
EXPOSE 80

CMD ["python", "hello_world.py"]