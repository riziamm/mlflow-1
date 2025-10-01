# mlflow-1
trying out mlflow with a 2D image classification problem 
tutorial: https://www.youtube.com/watch?v=-NOIWzjJK-4


First setup the environment:
```markdown$ conda create -n mlenv1 python=3.12 -y
$ conda activate mlenv1
```

Setup githib repo, clone it to workstation/machine
$ git clone ...
Create folder struicture template
```markdown
$ python template.py
$ python setup.py
```
INstall the required packages
```markdown
$ pip install -r requirements.txt
```

Update github
```markdown
$ git add .
$ git commit -m "requirments added"
$ git push origin main
```

Setup logs with the src/__init__.py. Also creates the logs folder
Test>>
```markdown
$ python main.py
```
## Workflows

1. Update config.yaml
2. Update secrets.yaml [Optional]
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in src config
6. Update the components [ML/DL pipeline components]
7. Update the pipeline 
8. Update the main.py
9. Update the dvc.yaml [after completing everything]


## Data prep for 2DClassification
### put each classes in its own folder with class names as the folder names

