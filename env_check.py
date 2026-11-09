import torch

print(torch.__version__)
print(torch.cuda.is_available())
print(torch.cuda.get_device_name(0))

print(dir(torch))
print(dir(torch.cuda))
print(dir(torch.cuda.is_available))
print(help(torch.cuda.is_available))