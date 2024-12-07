```py
import torch
torch.cuda.is_available()
# 使用print()调试查看输出类型

Dataset?? # jupyter-overview


# packages
conda install pytorch torchvision torchaudio cpuonly -c pytorch
conda install nb_conda tensorboard matplotlib
pip install torch-tb-profiler opencv-python


# Pillow
from torchvision.io import read_image # replace
from PIL import Image
image = Image.open('2092.jpg') # PIL: (W,H)
img_array = np.array(img) # numpy: (H,W,C)
image.show()
image.save('1.jpg')
print(image.mode, image.size, image.format)
grey_image = image.convert('L')


# tensorboard
tensorboard --logdir=logs --port=6007
tensorboard --logdir dir
from torch.utils.tensorboard import SummaryWriter
writer = SummaryWriter("logs")
writer.add_scalar(tag,y,x)
writer.add_histogram(tag, values=param.data, global_step=epoch)
writer.add_image(tag, img_array, global_step=1,dataformats='HWC') # use tensor or ndarray
writer.add_image(tag, torch.utils.make_grid(img,nrow)) # make_grid: concatenate
writer.add_graph(model=tudui, input_to_model=x)
writer.add_embedding(images.view(-1, 28 * 28), metadata=class_labels, label_img=images.unsqueeze(1)) # for many images
writer.flush() # 立刻写入disk


# dataset
    # normal use
test_data = torchvision.datasets.CIFAR10(root="./dataset", train=False, transform=torchvision.transforms.ToTensor(), target_transform=..., download=True)
img, target = test_data[0]

mydataset = [[waveform, info],[waveform2, info2], ...] # 自定义dataset，可传入Dataloader
mydataset = torch.utils.data.TensorDataset(features, labels) # 要求tensor的size[0] 相同，每次读取tuple(Tensor1[idx], Tensor2[idx], ...)
train_ds, test_ds = torch.utils.data.random_split(vgg_dataset,[700,100])
    # ImageFolder
train = datasets.ImageFolder(root, transform) # 要求root/cat/abc.png; root/dog/d2.png
list = train.classes # label=str
dict = train.class_to_idx # str:num
train.imgs = [(path, label_num),(path,label_num2), ...]
train = [(img, label_num),(img,label_num2), ...]


# transforms
from torchvision import transforms
trans_totensor = transforms.ToTensor() # PIL,ndarray -> tensor, scale to [0,1] and change channel order
img_tensor = trans_totensor(img) # __call__()
transforms.ToPILImage()
transforms.Lambda(lambda y: torch.zeros(10, dtype=torch.float).scatter_(0, torch.tensor(y), value=1))
trans_norm = transforms.Normalize([mean,mean,mean],[std,std,std]) # repeat n channels times
trans_resize = transforms.Resize((H,W))
transforms.CenterCrop(224) # crop to 224*224 for vgg
trans_compose = transforms.Compose([trans_resize, trans_totensor])


# dataloader
from torch.utils.data import DataLoader
test_loader = DataLoader(dataset=test_data, batch_size=64, shuffle=True, num_workers=0, drop_last=True)
length = len(test_loader)
lentgh = len(test_loader.dataset)
for img, target in test_loader:

```
