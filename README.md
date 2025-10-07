# Deep Learning Docker Images Optimized for AWS Inferentia

This project demonstrates **building custom deep learning container images optimized for AWS Inferentia instances** using Docker. The images provide faster and cost-efficient model inference.

## Features

- Custom Docker image for deep learning inference
- Optimized for AWS Inferentia via AWS Neuron SDK
- Example PyTorch model included
- Scalable and portable across AWS instances

## Project Structure

- `docker/` - Dockerfile and dependencies
- `app/` - Inference script
- `model/` - Pretrained or sample models
- `.gitignore` - Ignore unnecessary files

## Prerequisites

- Docker installed
- AWS account with Inferentia instances (Inf1)
- PyTorch and AWS Neuron SDK knowledge

## Build Docker Image

```bash
cd docker
docker build -t inferentia-ml-image .
```

## Run Container

```bash
docker run -it --rm inferentia-ml-image python /app/inference.py
```

## Using AWS Inferentia

- Ensure the container is deployed on **Inf1 instances** in AWS EC2.
- Neuron SDK will automatically optimize the model for Inferentia.
- Benchmark inference time to see performance improvements.

## Extending the Project

- Replace `sample_model.pt` with your own trained models.
- Add additional dependencies in `requirements.txt`.
- Integrate the container into AWS SageMaker or ECS for production deployment.

## License

MIT License
