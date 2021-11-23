NUM=5

install:
	docker build -t rock-paper-scissors .

play-rps:
	docker run --rm -it rock-paper-scissors rps-game -n $(NUM)
