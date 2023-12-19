# Use a base image with CUDA support
FROM nvcr.io/nvidia/pytorch:23.06-py3 

# Install make
RUN apt-get update && apt-get install -y make

# Set the working directory inside the container
WORKDIR /workdir

# Copy the requirements.txt file to the container
COPY requirements.txt .
COPY Makefile .

# Make file to control installation and set-up
RUN make setup

# Install the Python dependencies using make
RUN make install

# Could be also added to the requirements file
RUN pip install influxdb 
RUN pip install mlflow

# Copy the code files to the container
COPY . .
