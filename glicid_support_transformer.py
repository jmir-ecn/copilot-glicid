import torch
from transformers import BertTokenizer, BertForSequenceClassification
from transformers import AdamW
from torch.utils.data import DataLoader, RandomSampler
from transformers import get_linear_schedule_with_warmup

# Define data directories
train_data_dir = '/jmir/git_repo/glicid_copilot/train'
test_data_dir = '/jmir/git_repo/glicid_copilot/test'


# Define a function to load your dataset
def load_dataset(data_dir, tokenizer, max_length):
    dataset = CustomDataset(data_dir, tokenizer, max_length)
    return dataset

# Initialize the BERT tokenizer and model
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertForSequenceClassification.from_pretrained('bert-base-uncased')

# Set device
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

# Define training parameters
epochs = 3
batch_size = 4
max_length = 128

# Load datasets
train_dataset = load_dataset(train_data_dir, tokenizer, max_length)
test_dataset = load_dataset(test_data_dir, tokenizer, max_length)

# Define dataloaders
train_dataloader = DataLoader(train_dataset, sampler=RandomSampler(train_dataset), batch_size=batch_size)
test_dataloader = DataLoader(test_dataset, batch_size=batch_size)

# Define optimizer and scheduler
optimizer = AdamW(model.parameters(), lr=2e-5, eps=1e-8)
total_steps = len(train_dataloader) * epochs
scheduler = get_linear_schedule_with_warmup(optimizer, num_warmup_steps=0, num_training_steps=total_steps)

# Training loop
for epoch in range(epochs):
    model.train()
    total_loss = 0
    for batch in train_dataloader:
        optimizer.zero_grad()
        inputs = batch['input_ids'].to(device)
        attention_mask = batch['attention_mask'].to(device)
        labels = batch['labels'].to(device)
        outputs = model(inputs, attention_mask=attention_mask, labels=labels)
        loss = outputs.loss
        total_loss += loss.item()
        loss.backward()
        optimizer.step()
        scheduler.step()

    avg_train_loss = total_loss / len(train_dataloader)
    print(f'Epoch {epoch+1}/{epochs}, Average Training Loss: {avg_train_loss:.4f}')

# Testing loop
model.eval()
total_correct = 0
total_samples = 0
with torch.no_grad():
    for batch in test_dataloader:
        inputs = batch['input_ids'].to(device)
        attention_mask = batch['attention_mask'].to(device)
        labels = batch['labels'].to(device)
        outputs = model(inputs, attention_mask=attention_mask)
        _, predicted = torch.max(outputs.logits, 1)
        total_correct += (predicted == labels).sum().item()
        total_samples += labels.size(0)

accuracy = total_correct / total_samples
print(f'Test Accuracy: {accuracy:.4f}')

