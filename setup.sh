#!/bin/bash

pip install rasa-x==0.26.1 --extra-index-url https://pypi.rasa.com/simple
pip install bert-serving-client
pip install bert-serving-server
pip install rasa==1.8.1
pip install spacy
python -m spacy download en_core_web_sm
python -m spacy link en_core_web_sm en