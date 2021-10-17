FROM python:3.8
# Run commands from /flask_math directory inside container
WORKDIR /flask_math
# Copy requirements from local to docker image
COPY requirements.txt /flask_math
# Install the dependencies in the docker image
RUN pip3 install -r requirements.txt --no-cache-dir
# Copy everything from the current dir to the image
COPY . .