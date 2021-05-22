.PHONY: isort black format

CMD:=pipenv run
FOLDER:=scripts

isort:
	$(CMD) isort $(FOLDER)

black:
	$(CMD) black $(FOLDER)

format: black isort
