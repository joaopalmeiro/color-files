.PHONY: isort black type format all

CMD:=pipenv run
FOLDER:=scripts

isort:
	$(CMD) isort $(FOLDER)

black:
	$(CMD) black $(FOLDER)

type:
	$(CMD) mypy $(FOLDER)

format: black isort

all: format type
