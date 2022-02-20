# GPT3-NGen-WebApp
GPT-3 powered Web Application for generating corrective action. WebApp uses a finetuned model and is built on top of flask. 

# Running the webapp using the key information (without config file)
1. Update the key information from GPT3 in app.py file at `openai.api_key= <GPT-3-KEY-HERE>`
2. Move to the location of app.py file and run `python app.py` to trigger run for the flask app 

# Running app via Docker container (without config file)
1. Clone the repo and update you GPT-3 key in `app.py` file at `openai.api_key= <GPT-3-KEY-HERE>`
2. Move to the location where `app.py' file exists in the cloned folder 
3. Build docker using command: `docker build -f Dockerfile -t app_nga_2:latest .`
4. Run `docker run -p 8100:8100 -ti app_nga_2 /bin/bash -c "cd src && source activate nga_scratch && python api.py" `
5. If using linux, use link to directly navigate to the app, else use Docker App to launch the web-interface

# Running the webapp on local device (with config file) 
1. Create a config file that contains GPT-3 key information
2. Modify code in app.py to load config
3. Exporting of key is required before web-app is run: `export OPENAI_CONFIG=/path/to/config/openai.cfg`
4. Run python file for starting the webapp

