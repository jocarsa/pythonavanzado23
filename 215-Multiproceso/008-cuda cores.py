import pynvml

# Initialize NVML
pynvml.nvmlInit()

# Get the number of NVIDIA GPUs
num_gpus = pynvml.nvmlDeviceGetCount()

# Loop through each GPU
for i in range(num_gpus):
    # Get the GPU handle
    handle = pynvml.nvmlDeviceGetHandleByIndex(i)

    # Get the GPU name
    name = pynvml.nvmlDeviceGetName(handle).decode()

    # Get the number of CUDA cores
    cuda_cores = pynvml.nvmlDeviceGetAttribute(handle, pynvml.NVML_DEVICE_ATTRIBUTE_MULTIPROCESSOR_COUNT) * \
                 pynvml.nvmlDeviceGetAttribute(handle, pynvml.NVML_DEVICE_ATTRIBUTE_MULTIPROCESSOR_CORES)

    print(f"GPU {i+1}: {name} - CUDA Cores: {cuda_cores}")

# Shutdown NVML
pynvml.nvmlShutdown()
