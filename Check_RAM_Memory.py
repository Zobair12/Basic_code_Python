import psutil

memory = psutil.virtual_memory()

def convert_size(size_bytes):
    # Convert bytes to GB
    gb= size_bytes / (1024 ** 3)
    return gb

total_gb = convert_size(memory.total)
available_gb = convert_size(memory.available)
user_gb = convert_size(memory.used)

print(f"Total RAM: {total_gb:.3f} GB")
print(f"Available RAM: {available_gb:.3f} GB")
print(f"User RAM: {user_gb:.3f} GB")
print(f"RAM User: {memory.percent}%")