# Notes of OpanAI Fine-Tuning

## Fine-Tuning Steps
### prepare and upload training data 
Data sets must be a jsonl document, where each line is a prompt-completion pair corresponding to a training example. We can use open ai provided tools [cli-data](https://platform.openai.com/docs/guides/fine-tuning/cli-data-preparation-tool) to format our datasets into required format.  


### train a new fine-tuned model 
Designing prompts and completions for fine-tuning is different from design your prompts for use with our base models(Davinci, Curie, Babbage, Ada). In particular, while prompts for base models often consist of multiple examples("few-shot learning"), for fine-tuning, each training example generally consists of a single input example and its associated output, without the need to give detailed instructions or include multiple examples in the same prompt.

And the more training examples we have, the finer the model trained. 
 
* user your fine-tuned model

##  

## References
* [find-tuning](https://platform.openai.com/docs/guides/fine-tuning)
