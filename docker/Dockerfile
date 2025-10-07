# Use NVIDIA PyTorch image as base
FROM nvcr.io/nvidia/pytorch:23.05-py3

# Install AWS Neuron SDK for Inferentia
RUN apt-get update &&     apt-get install -y awscli curl unzip &&     curl https://s3.amazonaws.com/aws-neuron-us-east-1/Neuron-Package/1.29.0/aws-neuron-sdk-1.29.0.0.tar.gz -o aws-neuron-sdk.tar.gz &&     tar -xzf aws-neuron-sdk.tar.gz &&     ./aws-neuron-sdk-1.29.0.0/install.sh &&     rm -rf aws-neuron-sdk*

# Set working directory
WORKDIR /app

# Copy dependencies
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy app
COPY ../app/ /app/
COPY ../model/ /app/model/

# Default command
CMD ["python", "inference.py"]
