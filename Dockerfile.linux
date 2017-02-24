#
# Python Dockerfile for Linux Docker Servers
#

# Pull base docker image
FROM python:latest

# Define working directory.
COPY . /data
WORKDIR /data

RUN pip install -r requirements.txt

# Define default command.
CMD ["python", "/data/sample/hello.py"]
