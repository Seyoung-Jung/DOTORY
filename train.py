import torch
from transformers import (PreTrainedTokenizerFast,
                          GPT2LMHeadModel,
                          DataCollatorForLanguageModeling,
                          LineByLineTextDataset,
                          TrainingArguments, 
                          Trainer)

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

tokenizer = PreTrainedTokenizerFast.from_pretrained('skt/kogpt2-base-v2', bos_token='</s>', eos_token='</s>', unk_token='<unk>', pad_token='<pad>', mask_token='<mask>')
# print('Length of tokenizer before add special tokens:', len(tokenizer))
tokenizer.add_special_tokens({
    'additional_special_tokens':['<전래동화>', '<이솝우화>', '<우주>', '<숲속>',
                                '<등장인물1>', '<등장인물2>', '<등장인물3>']
})
# print('Length of tokenizer after add special tokens:', len(tokenizer))

model = GPT2LMHeadModel.from_pretrained('skt/kogpt2-base-v2')
model.resize_token_embeddings(len(tokenizer))
model.to(device)
model.train()

data_collator = DataCollatorForLanguageModeling(tokenizer=tokenizer, mlm=False) # for batch
dataset = LineByLineTextDataset(tokenizer=tokenizer, file_path='./10sentence_df.txt', block_size=128)

EPOCHS = 100

train_args = TrainingArguments(
    output_dir = './checkpoint/10sentence_epoch100',
    overwrite_output_dir = True,
    dataloader_drop_last = True,
    per_device_train_batch_size = 128,
    learning_rate = 5e-5,
    num_train_epochs = EPOCHS
)
trainer = Trainer(
    model = model,
    args = train_args,
    data_collator = data_collator,
    train_dataset = dataset
)
trainer.train()
trainer.save_model()