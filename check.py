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