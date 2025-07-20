.PHONY: build run dev shell clean logs

IMAGE_NAME := chapter-2
CONTAINER_NAME := chapter-2-app

build:
	docker build -t $(IMAGE_NAME) .

run:
	docker run --rm -it -v $(PWD):/app $(IMAGE_NAME)

dev:
	docker compose up

shell:
	docker run --rm -it -v $(PWD):/app --entrypoint /bin/bash $(IMAGE_NAME)

clean:
	docker compose down
	docker rmi $(IMAGE_NAME) 2>/dev/null || true
	docker system prune -f

logs:
	docker compose logs -f

rebuild: clean build
