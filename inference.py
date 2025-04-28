import openai
from openai import OpenAI
import os
from dotenv import load_dotenv
load_dotenv()
# Set openai API key


client=OpenAI(
    api_key= os.getenv("OPENAI_KEY"),
)
job = client.fine_tuning.jobs.retrieve("ftjob-EMDDWll6dMUFGfAV6Jte7SFc")
print(job.status)
print(job.fine_tuned_model)  
response = client.chat.completions.create(
    model=job.fine_tuned_model,
    messages=[{"role": "user", "content": "kya tu train se aaya?"},
              {"role": "user", "content": "kya tumne woh news dekhi?"},
              {"role": "user", "content": "weekend ka plan ban gaya?"},]
)
print(response.choices[0].message.content)
