from openai import OpenAI
import os
from dotenv import load_dotenv
load_dotenv()
# Set openai API key
client=OpenAI(
    api_key= os.getenv("OPENAI_KEY"),
)

# Step 1: Upload the dataset
upload_response = client.files.create(
    file=open("data.jsonl", "rb"),
    purpose="fine-tune"
)
print(f"Uploaded file ID: {upload_response.id}")

# Step 2: Start fine-tuning job
fine_tune_response = client.fine_tuning.jobs.create(
    training_file=upload_response.id,
    model="gpt-3.5-turbo",
    hyperparameters={
         "n_epochs":4,
         "learning_rate_multiplier":0.05}
)
print(fine_tune_response)
print(f"Fine-tune job started: {fine_tune_response.id}")
