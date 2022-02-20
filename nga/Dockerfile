FROM ubuntu:18.04
ENV PATH="/root/miniconda3/bin:${PATH}"
ARG PATH="/root/miniconda3/bin:${PATH}"

RUN apt update \
    && apt install -y htop python3-dev wget

RUN wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh \
    && mkdir root/.conda \
    && sh Miniconda3-latest-Linux-x86_64.sh -b \
    && rm -f Miniconda3-latest-Linux-x86_64.sh

RUN conda create -y -n nga_scratch python=3.7


COPY openai.cfg  src/openai.cfg

RUN export OPENAI_CONFIG=src/openai.cfg
#WORKDIR /app

#COPY . /app

COPY . src/
RUN /bin/bash -c "cd src \
    && source activate nga_scratch \
    && pip install -r requirements.txt"
	

	
EXPOSE 8100

#ENTRYPOINT ["python3"]

#CMD ['./src/app.py']
	





