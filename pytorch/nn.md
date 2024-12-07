```py
from torch import nn
import torch.nn.functional as F # low layer

# MyClass
class Tudui(nn.Module):
    def __init__(self):
        super(Tudui, self).__init__()

# layers
output = F.conv2d(input, kernel, stride=1, padding=1) # write by your self
self.conv1 = nn.Conv2d(in_channels=3, out_channels=6, kernel_size=3, stride=1, padding=0)
x = F.relu(F.max_pool2d(self.conv2_drop(self.conv2(x)), 2))
nn.Linear(input_size, output_size) # may need: nn.flatten() and keeps minibatch dimension
x = F.relu(self.fc2(x))
nn.Dropout2d()
x = F.dropout(x, p=0.5, training=self.training) # 控制输入部分数据为0
F.log_softmax(x,dim=1)

# Sequential
self.model1 = nn.Sequential(...)
print(tudui) # see model params

# loss
L1Loss(reduction='sum') MSELoss() CrossEntroyLoss(y,labels)
loss = nn.CrossEntropyLoss()

# optimizer
optim = torch.optim.SGD(params=tudui.parameters(), lr=0.01)
    result_loss = loss(outputs, targets)
    optim.zero_grad()
    result_loss.backward()
    optim.step()
running_loss = running_loss + result_loss # for one epoch

optimizer.param_groups # list of dict
optimizer.param_groups[0].keys() = dict_keys(['params', 'lr', 'betas', 'eps', 'weight_decay', 'amsgrad', 'maximize'])
optimizer.param_groups[0]['params'] # list
optimizer = optim.SGD( # 不同子网络的学习率
    [{'params': net.features.parameters()}, # 学习率为1e-5
     {'params': net.classifiter.parameters(), 'lr': 1e-2}], lr=1e-5
)
# 修改学习率
for param_group in optimizer.param_groups:
    param_group["lr"] = lr 


# initialize weights
def weight_init(m):
    classname = m.__class__.__name__
    if isinstance(m, nn.Linear): | if classname.find('Linear') != -1:
        nn.init.xavier_normal_(m.weight)
        nn.init.constant_(m.bias, 0)
    elif isinstance(m, nn.Conv2d): elif classname.find('Conv') != -1:
        nn.init.kaiming_normal_(m.weight, mode='fan_in', nonlinearity='relu')
    elif isinstance(m, (nn.BatchNorm2d, nn.GroupNorm)): elif classname.find('BatchNorm') != -1:
        nn.init.constant_(m.weight, 1)
        nn.init.constant_(m.bias, 0)
model.apply(weight_init) # 不断遍历model的各个模块-深度优先算法
# manner 2: define in __init__() function
for m in self.modules():
    if isinstance(m, (nn.Conv1d, nn.Linear)):
        nn.init.kaiming_normal_(m.weight.data)
        if m.bias is not None:
            nn.init.zeros_(m.bias)
# module
class Net(nn.module):
    self.features=nn.Sequential(nn.Conv2d(), nn.Linear(),...)
    self.classifier=nn.Sequential(nn.Conv2d(), nn.Linear(),...)
model = Net()
model.features[0] = nn.Conv2d(...)
model.features[0].(weight/bias).(data/grad.data)

for layer in model.modules():
    # layer=Net,features,Conv2d,... 深度优先迭代所有层级的nn.module对象
    if isinstance(layer, nn.Conv2d):
for name, layer in model.named_modules():
    # name='features', 'features.0',...根据定义的实例属性self.features=nn.Sequential(...)确定
    if 'conv' in name:
module.children() # 只包括features, classifier
module.named_children() # 只包括features, classifier
model.parameters() # list of tensors
model.named_parameters() # name=features.0.bias, features.0.weight
model.state_dict() = OrderedDict([(name,params),...]) # name=features.0.weight/bias

pretrained_dict['conv1.weight'] = pretrained_dict['conv1.weight'][:200,:,:,:]   # 假设保留前200个卷积核
```
