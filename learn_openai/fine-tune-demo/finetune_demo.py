import os
import openai

openai.api_key = 'sk-${your_openai_api_key}'
os.environ['OPENAI_API_KEY'] = openai.api_key
models = openai.Model.list()
#print(models)

# command should be executed in your console shell command 
#!openai api fine_tunes.create -t  /Users/nanachi/repository/openai/fine-tune-demo/dataset/finetune_dataset1.txt  -m davinci --suffix 'davinci_model_002'

fine_tune_job_id_001 = "ft-jobname"
# command should be executed in your console shell command 
#!openai api fine_tunes.follow -i $fine_tune_job_id_001

# command should be executed in your console shell command 
#!openai api fine_tunes.results -i $fine_tune_job_id_001


models = openai.Model.list()

model = "davinci:ft-personal:davinci-model-001-${timestamp}"
prompt = "Samsung Galaxy Feel"
response = openai.Completion.create(model=model,prompt=prompt)
print(response)
print(response["choices"][0]["text"])

import json

# set up the OpenAI API key
openai.api_key = "sk-xxxx"

# set up the prompt
prompt = "What is the meaning of life?"

# generate text using the OpenAI API
response = openai.Completion.create(
  engine="davinci", # chose your prefer engine here 
  prompt=prompt,
  max_tokens=100,
  n=1,
  stop=None,
  temperature=0.7
)

# print the generated text
print(response.choices[0].text)

# provide feedback on the generated text
feedback = {
  "text": response.choices[0].text,
  "model": "davinci",
  "prompt": prompt,
  "rating": 4, # rating value 
  "comment": "This is a great response!"
}

# send the feedback to the OpenAI API to enhance model 
response = openai.Feedback.create(json.dumps(feedback))

