#!/bin/bash
cd src
export OPENAI_CONFIG=openai.cfg
source activate nga_scratch
python api.py
