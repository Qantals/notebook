from torch.utils.data import Dataset, DataLoader
import numpy as np
from PIL import Image # read images, or using cv2
import os
from torchvision import transforms
from torch.utils.tensorboard import SummaryWriter # TensorBoard
from torchvision.utils import make_grid

writer = SummaryWriter("logs")

class MyData(Dataset):

    def __init__(self, root_dir, image_dir, label_dir, transform):
        # self赋值
        self.root_dir = root_dir
        self.image_dir = image_dir
        self.label_dir = label_dir
        # 获取路径
        self.label_path = os.path.join(self.root_dir, self.label_dir) # 拼接路径名，像字符串拼接
        self.image_path = os.path.join(self.root_dir, self.image_dir)
        # 获取文件名
        self.image_list = os.listdir(self.image_path) # 返回目录下所有文件名
        self.label_list = os.listdir(self.label_path)
        self.transform = transform
        # 因为label 和 Image文件名相同，进行一样的排序，可以保证取出的数据和label是一一对应的
        self.image_list.sort()
        self.label_list.sort()

    def __getitem__(self, idx): # 定义后可以使用MyData[0]取值
        # 取出一个样本
            # 样本名
        img_name = self.image_list[idx]
        label_name = self.label_list[idx]
            # 样本路径
        img_item_path = os.path.join(self.root_dir, self.image_dir, img_name)
        label_item_path = os.path.join(self.root_dir, self.label_dir, label_name)
            # 得到对象
        img = Image.open(img_item_path)
            # label文件夹都是txt，一行ant/bee
        with open(label_item_path, 'r') as f:
            label = f.readline()

        # img = np.array(img)
        img = self.transform(img)
        sample = {'img': img, 'label': label}
        # 返回一个dict
        return sample

    def __len__(self):
        assert len(self.image_list) == len(self.label_list)
        return len(self.image_list)

if __name__ == '__main__':
    transform = transforms.Compose([transforms.Resize((256, 256)), transforms.ToTensor()])
    root_dir = "./dataset/train"
    image_ants = "ants_image"
    label_ants = "ants_label"
    ants_dataset = MyData(root_dir, image_ants, label_ants, transform)
    image_bees = "bees_image"
    label_bees = "bees_label"
    bees_dataset = MyData(root_dir, image_bees, label_bees, transform)
    train_dataset = ants_dataset + bees_dataset # 拼接数据集

    # transforms = transforms.Compose([transforms.Resize(256, 256)])
    dataloader = DataLoader(train_dataset, batch_size=1, num_workers=2)

    # writer.add_image('error', train_dataset[119]['img']) # tag, y, x
    # writer.close()
    for i, j in enumerate(dataloader):
        # imgs, labels = j
        # print(type(j))
        # print(i, j['img'].shape)
        writer.add_image("train_data_b2", make_grid(j['img']), i)
    
    writer.close()



