import torch
from torchvision.datasets import MNIST
from torchvision.transforms import ToTensor
from torch.utils.data import DataLoader
from torch import nn
from torch import optim
from tqdm import tqdm

class ConvModel(nn.Module):
    def __init__(self):
        super().__init__()
        num_layers=4
        in_channels=[1,32,64,128]
        out_channels=[32,64,128,192]
        layers=[nn.Sequential(
            nn.Conv2d(in_channels[i],out_channels[i],3,padding=2),
            nn.BatchNorm2d(out_channels[i]),
            nn.ReLU(),
            nn.MaxPool2d(2),
        )for i in range(num_layers)]
        self.conv=nn.Sequential(*layers)
        self.fc=nn.Sequential(nn.Linear(192*3*3,192),nn.ReLU(),nn.Linear(192,10))
    def forward(self,x):
        x=self.conv(x)
        return self.fc(x.view(x.size(0),-1))
    
def train(model,dataloader):
    criterion=nn.CrossEntropyLoss()
    optimizer=optim.Adam(model.parameters(),lr=0.01)
    for _ in range(10):
        for x,y in tqdm(dataloader):
            optimizer.zero_grad()
            y_pred=model(x)
            loss=criterion(y_pred,y)
            loss.backward()
            optimizer.step()
        print("loss: ",loss.item())
    
def test(model,dataloader):
    accuracy=0
    for x,y in tqdm(dataloader):
        y_pred=model(x)
        accuracy+=(y_pred.argmax(dim=1)==y).float().mean().item()
    print("accuracy: ",accuracy/len(dataloader))

torch.manual_seed(0)

dataset_train=MNIST(root="./data",transform=ToTensor(),download=True)
dataset_test=MNIST(root="./data",train=False,transform=ToTensor(),download=True)
dataloader_train=DataLoader(dataset_train,batch_size=32,shuffle=True)
dataloader_test=DataLoader(dataset_test,batch_size=32)

model=ConvModel()
train(model,dataloader_train)
test(model,dataloader_test)