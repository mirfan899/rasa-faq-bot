#!/bin/bash
pip3.7 install --upgrade pip
pip install rasa-x --extra-index-url https://pypi.rasa.com/simple
pip install bert-serving-client
pip install bert-serving-server
pip install rasa
pip install spacy
pip install tensorflow-addons
python -m spacy download en_core_web_sm
python -m spacy link en_core_web_sm en