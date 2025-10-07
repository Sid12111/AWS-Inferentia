import torch
import time

# Load sample model
model_path = "./model/sample_model.pt"
model = torch.load(model_path)
model.eval()

# Sample input tensor
input_tensor = torch.randn(1, 3, 224, 224)

# Run inference
start_time = time.time()
output = model(input_tensor)
end_time = time.time()

print("Inference output:", output)
print("Inference time:", end_time - start_time, "seconds")
