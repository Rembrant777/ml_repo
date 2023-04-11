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
