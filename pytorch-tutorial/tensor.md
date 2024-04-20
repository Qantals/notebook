```py
import torch
# tensor
x = torch.tensor([[1,2,3],[4,5,6]],dtype=torch.float, device=another_tensor.device, requires_grad=True)
torch.is_tensor(a)
out.backward(v, retain_graph=True) # Jacobian Product v^TJ, saves to compute gradients more than once

# 数组
x.size(0) = x.shape[0] x.numel() # 元素个数
x.contiguous() # 内存重新组合好，在permute后
x = torch.from_numpy(a)
a = a.detach().cpu().numpy() # detach(): stop tracking gradient; first cpu then numpy
a = a.type(torch.float32) a.float() a.long()
x = x.to('cuda') x.device('cuda:0')
x.dtype=x.type() x.device
a.item() # 返回数值

# 变换
x = torch.cat([a,b],dim)
torch.view() # reshape
x.transpose_() # In-place operations 
x.permute(a,b,c) # transpose:交换两个； permute：任意个
x.squeeze(dim) x.unsqueeze(dim)
torch.clamp(input, min=None, max=None)
x.scatter_(dim, index, src): # 将src中所有的值分散到self 中，按照index指示的索引填入。如独热码

# Variable
from torch.autograd import Variable
x=Variable(tensor,requires_grad=True)
x.data # tensor
x.grad # another variable, has x.grad.data
x.grad_fn
x.requires_grad x.requires_grad_(True)
```
