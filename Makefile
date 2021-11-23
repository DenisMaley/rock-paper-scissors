ROUNDS=5
NAME=PLAYER

current_dir = $(shell pwd)

install:
	docker build -t rock-paper-scissors .

play-rps:
	docker run --rm -it rock-paper-scissors rps-game -r $(ROUNDS) -n $(NAME)

test-run:
	coverage run -m unittest discover -s tests

test-report:test-run
	coverage report

coverage-report:test-run
	coverage html && python -m webbrowser "file:$(current_dir)/htmlcov/index.html"