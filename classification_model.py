import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, TensorDataset

class SingleLayerNN(nn.Module):
    def __init__(self):
        super(SingleLayerNN, self).__init__()
        self.fc = nn.Linear(1, 1)  

    def forward(self, x):
        x = self.fc(x)
        x = torch.sigmoid(x) 
        return x

X_train = torch.linspace(-1, 1, 640).view(-1, 1) 
y_train = (X_train > 0).float()  

dataset = TensorDataset(X_train, y_train)
data_loader = DataLoader(dataset, batch_size=32, shuffle=True)

model = SingleLayerNN()

criterion = nn.BCELoss()  
optimizer = optim.SGD(model.parameters(), lr=0.01)  

best_loss = float('inf')  
patience = 50 
counter = 0  

num_epochs = 1000
for epoch in range(num_epochs):
    for inputs, labels in data_loader:
        outputs = model(inputs)
        loss = criterion(outputs, labels)

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        
    if loss.item() < best_loss:
        best_loss = loss.item() 
        counter = 0  
    else:
        counter += 1 
    
    if counter >= patience:
        print(f"Early stopping at epoch {epoch+1}, best loss: {best_loss:.4f}")
        break

    if (epoch + 1) % 100 == 0:
        print(f'Epoch [{epoch + 1}/{num_epochs}], Loss: {loss.item():.4f}')

model.eval() 
with torch.no_grad():
    test_input = torch.tensor([[0.5], [-0.5]])
    test_output = model(test_input)
    predicted = (test_output > 0.5).float()
    print(f'Test Input: {test_input.view(-1).tolist()}')
    print(f'Predicted Output: {predicted.view(-1).tolist()}')


num_samples = 100
num_positive = int(0.8 * num_samples)  # label 1: 80 positive number
num_negative = num_samples - num_positive  # label 2: 20 negative number


positive_samples = torch.rand(num_positive, 1)  # generate 80 numbers (0,1) 
negative_samples = -torch.rand(num_negative, 1)  # generate 20 numbers (-1,0)

test_input = torch.cat([positive_samples, negative_samples], dim=0)  # (100, 1)
test_labels = torch.cat([torch.ones(num_positive, 1), torch.zeros(num_negative, 1)], dim=0)  # labels

indices = torch.randperm(num_samples)
test_input = test_input[indices]
test_labels = test_labels[indices]


model.eval()
with torch.no_grad():
    test_output = model(test_input) 
    predicted = (test_output > 0.5).float()  
    accuracy = (predicted == test_labels).float().mean().item() 

print(f'Accuracy on imbalanced test set (20% negative, 80% positive): {accuracy:.4f}')
