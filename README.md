Install rasa x
```shell script
pip install rasa-x==0.26.1 --extra-index-url https://pypi.rasa.com/simple
```

Install spacy
```shell script
pip install spacy
python -m spacy download en_core_web_sm
python -m spacy link en_core_web_sm en
```

Train model
```shell script
python -m rasa train
```
launch model gui
```shell script
python m rasa x
```

launch model in background with cors
```shell script
python -m rasa run --enable-api --cors "*"
```

### floyd shit
```shell script
floyd run --gpu --env tensorflow-2.1 "bash setup.sh && python -m rasa train"
floyd run --gpu --env tensorflow-2.1 "bash setup.sh && python -m rasa run" --mode serve
floyd run --gpu --env tensorflow-2.0 "bash setup.sh && python -m rasa train"
floyd run --gpu --env tensorflow-2.0 "bash setup.sh && python -m rasa run"
floyd run --gpu --env tensorflow-2.0 "bash setup.sh && python -m rasa run" --mode serve
floyd run --gpu --env tensorflow-2.0 --mode serve
```

## deploy to floyd
```shell script
floyd run --mode serve
```
for pyenv
```shell script
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
```