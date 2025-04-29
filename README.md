## GPT-3.5 Turbo Hinglish Finetuning
This repository contains code and instructions for fine-tuning OpenAI's GPT-3.5 Turbo model on Hinglish (Hindi-English mixed language) datasets.
## Overview
This project demonstrates how to fine-tune GPT-3.5 Turbo to better understand and generate Hinglish content, improving model performance for code-switching between Hindi and English. The fine-tuned model can be used for applications like chatbots, content generation, and language processing systems targeting Indian users.

## Prerequisites

Python 3.10

OpenAI API key with fine-tuning access

Training dataset in JSONL format

## Installation

Clone this repository:
```bash
git clone https://github.com/JisnaP/Fine_Tuning_GPT3.5_Turbo
cd Fine_Tuning_GPT3.5_Turbo

```

Create and activate a virtual environment:
```bash
conda create -p ./venv python=3.10 -y
conda activate ./venv

```
Install the required packages:
```bash
pip install -r requirements.txt
```
Set up your OpenAI API key as an environment variable

## Dataset Preparation
Your training data should be in JSONL format with each line representing a conversation turn:
```json
{"messages": [{"role": "system", "content": "You are a helpful assistant that responds in Hinglish."}, {"role": "user", "content": "Mujhe ek accha quote batao"}, {"role": "assistant", "content": "Zindagi me kabhi haar mat manna, kyunki success milne tak failure normal hai."}]}
{"messages": [{"role": "system", "content": "You are a helpful assistant that responds in Hinglish."}, {"role": "user", "content": "Weather kaisa hai aaj?"}, {"role": "assistant", "content": "Mujhe current weather ka data nahi hai, lekin mai aapko help kar sakta hoon forecast check karne me."}]}

```
Save this file as data.jsonl.
## Fine-tuning Process
```python
python finetune.py

```
## Ensure the fine-tuning has completed successfully
```python
python check.py #Use your job id here

```
## Inferencing the fine-tuned model 
```python
python inference.py 

```
## Example usage

```python
response = client.chat.completions.create(
    model=job.fine_tuned_model,
    messages=[{"role": "user", "content": "kya tu train se aaya?"},
              {"role": "user", "content": "kya tumne woh news dekhi?"},
              {"role": "user", "content": "weekend ka plan ban gaya?"},
              {"role": "user", "content": "Sunday ko kya plan hai?"},]
)

```
## Example response
```bash
Nahi, main car se aaya hoon.
Nahi, mujhe konsi news ki baat kar rahe ho?
Haan, ek movie dekhne aur friends ke saath dinner plan kiya hai. Tumhara kya plan hai?
Mujhe Sunday ko kuch special plan nahi hai, bas relax karne ka socha hai. Tumhara kya plan hai?

```
## Dataset, Model, Hyperparameter and Prompt choice
**📚 Dataset Selection**
1. Quality: 

The effectiveness of fine-tuning largely depends on the quality of your dataset. Ensure that your data is clean, relevant, and representative of the tasks you want the model to perform.

2. Dataset size:

-Minimum: OpenAI requires at least 10 examples to fine-tune a model.

-Optimal: For meaningful improvements, it's recommended to use 50 to 100 well-crafted training examples.

-Large-scale Fine-tuning: For more complex tasks, consider using thousands of examples. 

**⚙️ Model Selection**

The GPT-3.5-turbo model is often the ideal choice for most users due to its balance of several key factors:

1. Cost-effectiveness: It's significantly less expensive than larger models like GPT-4, making it accessible for projects with budget constraints.
2. Speed: It processes requests much faster than larger models, which is critical for applications requiring real-time responses.
3. Capability balance: For many common tasks (content generation, Q&A, summarization, etc.), it delivers results that are good enough without the additional power of more advanced models.
4. Resource efficiency: It requires less computational resources to run, making it more environmentally friendly and practical for high-volume applications.
5. Lower token limits: It can handle reasonable context windows (typically 4K-16K tokens) suitable for most everyday tasks without needing the extended context capabilities of larger models.
6. Broad language support: While not as sophisticated as GPT-4 in handling complex multilingual tasks, it's still capable of working with many languages adequately.

**⚙️ Hyperparameter selection**
1. n_epochs:

Increase epochs if the model doesn't follow training data closely.

Decrease epochs if the model becomes less diverse.

2. Learning rate multiplier

-Higher values ( 2.0-3.0):

1. More aggressive learning from your dataset
2. Model adapts more quickly to your examples
3. Risk of overfitting, especially with small datasets
4. May lose some general knowledge if set too high

-Lower values ( 0.5-0.8):

1. More conservative learning
2. Preserves more of the original model's knowledge
3. May require more epochs to achieve desired results


**✍️ Prompt Selection**

1. The conversational chat format is essential for fine-tuning gpt-3.5-turbo.
2. Role-based structure: Each example must include messages with specific roles:
system: Optional context setting message (appears at the start)
user: Messages from the human/user
assistant: Messages the model should learn to generate
3. JSONL format requirement: Each training example must be formatted as a JSON object with a "messages" array containing these role-based messages.
4. Complete conversations: For optimal results, training examples should be complete conversation exchanges that demonstrate the desired behavior.
5. Format consistency: The model will learn from the exact format you provide, so consistency in your data preparation is crucial.

```json
{"messages": [{"role": "system", "content": "You are a helpful assistant."}, {"role": "user", "content": "Hello!"}, {"role": "assistant", "content": "Hi there! How can I help you today?"}]}
```
**Temperature settings selected :0.2**


## ✅ Evaluating quality in production

1. Human review: Regularly assess the model's outputs to ensure they meet quality standards. This can involve manual review of responses to check for relevance, accuracy, and appropriateness.

2. Evaluation metrics: Implement custom task-specific metrics to quantitatively assess model performance.

   - Code-Switching Accuracy: Measure how accurately the model switches between Hindi and English in   contextually appropriate ways.
   - Transliteration Consistency: Evaluate consistency in Hindi transliteration to Roman script
     Count inconsistencies in spelling of the same Hindi words across responses**
   - Response Relevance: Evaluate if responses directly address the user's query.
     Manual scoring on a scale (1-5) for relevance.
     Can be automated with embedding similarity measurement.
   - Automatic metrics where possible (BLEU/ROUGE, embedding similarity).

3. Feedback Loops: Incorporate user feedback to continuously refine and improve the model. This can involve collecting user ratings or comments on model outputs.

4. Safety Checks: Ensure that the model's outputs adhere to safety and ethical guidelines. Implement content filters and moderation tools as necessary.


## License
MIT License

