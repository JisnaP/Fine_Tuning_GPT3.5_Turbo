import openai
from openai import OpenAI
import os
from dotenv import load_dotenv
load_dotenv()
# Set openai API key
if "SSL_CERT_FILE" in os.environ:
    del os.environ["SSL_CERT_FILE"]

client=OpenAI(
    api_key= os.getenv("OPENAI_KEY"),
)
job = client.fine_tuning.jobs.retrieve("ftjob-0IrUNTltSJU99dw6Yo2J0nym")
print(job.status)
print(job.fine_tuned_model)  
response = client.chat.completions.create(
    model=job.fine_tuned_model,
    messages=[{"role": "user", "content": "kya tu train se aaya?"},
              {"role": "user", "content": "kya tumne woh news dekhi?"},
              {"role": "user", "content": "weekend ka plan ban gaya?"},
              {"role": "user", "content": "Sunday ko kya plan hai?"},],
              temperature=0.2
)
print(response.choices[0].message.content)

#save response to a text file
with open("response.txt", "w", encoding="utf-8") as f:
    f.write(response.choices[0].message.content)
