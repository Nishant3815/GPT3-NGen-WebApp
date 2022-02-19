import os 
import re
import openai
import json
import string
from retry import retry

# Load inputs and requisite dictionaries
inputs = open('model_inps.json')
inputs_json = json.load(inputs)
model_params = inputs_json['model_params']
acro_dict    = inputs_json['acro_dict']
rev_dict     = inputs_json['rev_dict']

def replace_acronym(text):
    for acr, full in acro_dict.items():
        text = text.replace(acr.lower(), full)
    return text

def remove_eos(text, eos_token=" <EOS>"):
    t2 = text.replace(eos_token, "")
    return t2

def replace_num_grp(text):
    t3 = re.sub('[\d]+', '#num', text)
    return t3

def revert_val(text1):
    for acr, full in rev_dict.items():
        text1 = text1.replace(acr, full)
    return text1

def postprocess_data(text):
    """
    Processes data: includes conversion from short form to full form and replacing numbers except a few top occuring ones
    """
    t1 = replace_acronym(text)
    t2 = remove_eos(t1)
    t3 = replace_num_grp(t2)
    t4 = revert_val(t3)
    return t4


@retry(Exception, tries=3, delay=15)
def get_openai_completions_endpt(model=model_params['model'], prompt= None, max_tokens= model_params['max_tokens'], \
    stop = [model_params['stop']], logprobs=model_params['logprobs']):

    """
    Run completions endpoint api using model input params loaded from json file
    """
    res = openai.Completion.create(model = model, prompt= prompt, max_tokens= max_tokens, stop=stop, logprobs= logprobs)
    completion = res['choices'][0]['text']
    completion = completion[1:]       # remove initial space

    return completion

def set_openai_key(key):
    """Sets OpenAI key."""
    openai.api_key = key


