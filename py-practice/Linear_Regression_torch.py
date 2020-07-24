import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim
from tqdm import tqdm

class Net(nn.Module):
    def __init__(self):
        super(Net,self).__init__()
        self.linear = nn.Linear(3,1)
    def forward(self, x):
        y = self.linear(x)
        return y


def main():
    data = np.load('/work/yuzhe/lr_train_data.npy')
    x_train = torch.from_numpy(data[...,:3]).float()
    y_true = torch.from_numpy(data[...,3:]).float()

    model = Net()
    y_pred = model(x_train)

    criterion = nn.MSELoss()
    optimizer = optim.SGD(model.parameters(),lr=1e-1)
    num_epoch = 1000

    for epoch in tqdm(range(num_epoch)):
        y_pred = model(x_train)
        loss = criterion(y_pred,y_true)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

    print(model.linear.weight)
    
if __name__ == '__main__':
    main()
