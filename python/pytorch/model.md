```py
# models
vgg16 = torchvision.models.vgg16(weights='IMAGENET1K_V1') # weights=torchvision.models.ResNet18_Weights.DEFAULT
print(vgg16) # see its structure
vgg16.add_module('add_linear', nn.Linear(1000, 10)) # add (add_linear) to end
vgg16.classifier.add_module('add_linear', nn.Linear(1000, 10)) # add to (classifier) cluster
vgg16.classifier[6] = nn.Linear(4096, 10) # modify(vgg16.classifier返回的是有__call__的对象)
nn.Sequential(*list(vgg16.children())[0]) # 查找并组合子模块

# save and load
    # save model and params
torch.save(vgg16, "vgg16_method1.pth")
vgg16 = torch.load("vgg16_method1.pth", map_location=torch.device('cpu'))
    # save weights
torch.save(vgg16.state_dict(), "vgg16_method2.pth")
vgg16 = torchvision.models.vgg16(pretrained=False)
vgg16.load_state_dict(torch.load("vgg16_method2.pth"))
# load自定义的module时需要有class的定义，可以用import实现

# mode(for dropout and so on)
tudui.train()
tudui.eval()
size = len(dataloader.dataset)
num_batches = len(dataloader)

# CUDA
CUDA_VISIBLE_DEVICES=0,1 # 使用两张卡
nranks = torch.cuda.device_count() # 可用显卡数

if torch.cuda.is_available():
    tudui = tudui.cuda()
    loss_fn = loss_fn.cuda()
    imgs = imgs.cuda()
    targets = targets.cuda()
targets.cpu() # CPU
    # manner 2
device = torch.device("cuda" if torch.cuda.is_available() else 'cpu') # 'cpu' 'cuda:0'
tudui = tudui.to(device)
tudui.to(device) # is OK

# test
image = image.convert('RGB')
image = torch.reshape(image, (1, 3, 32, 32))
predicted, actual = classes[pred[0].argmax(0)], classes[y]

```
