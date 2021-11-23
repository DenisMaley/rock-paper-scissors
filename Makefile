ROUNDS=5
NAME=PLAYER

install:
	docker build -t rock-paper-scissors .

play-rps:
	docker run --rm -it rock-paper-scissors rps-game -r $(ROUNDS) -n $(NAME)
