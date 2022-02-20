from flask import Flask, request, render_template,jsonify
from gpt3_module import *

# Specify configuration information
CONFIG_VAR = "OPENAI_CONFIG"
KEY_NAME = "OPENAI_KEY"


app = Flask(__name__)
app.config.from_envvar(CONFIG_VAR)
set_openai_key(app.config[KEY_NAME])

# try:
#     openai.api_key= <GPT-3-KEY-HERE>
# except:
#     print("Please Enter Secret acceess key from GPT-3 API")

def convert_gpt3_input_format(prompt):
    """
    Convert the given prompt into a specified GPT-3 format for input into the model
    """
    return prompt + " \n\n###\n\n"


def process_issue_input(text_input):
    """
    Converts input text to a prompt, passes prompt to finetuned model, saves results
    from completions endpoint and returns output after post-processing for display
    """
    #Convert text to prompt format
    prompt = convert_gpt3_input_format(text_input)
    # Get API output from completions endpoint
    completion = get_openai_completions_endpt(model_params['model'], prompt, int(model_params['max_tokens']), [model_params['stop']], int(model_params['logprobs']))
    # Post process output from the api completion endpoint
    # processed_data = postprocess_data(completion)

    processed_data = completion

    return processed_data


@app.route('/processed', methods=['GET','POST'])
def post_input():
    text1 = request.form['text']
    word = request.args.get('text')
    processed_text = process_issue_input(text1)
    result = {
        "output": processed_text
    }
    result = {str(key): value for key, value in result.items()}
    return jsonify(result=result)

@app.route('/')
def home():
    return render_template('gpt3.html')
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8100)
