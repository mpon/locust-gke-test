GIT_TAG=$(shell git rev-parse --short=8 HEAD)
IMAGE=${GCR_URL}/kinesis-test:${GIT_TAG}

build:
	docker build -t ${IMAGE} .
push:
	gcloud docker -- push ${IMAGE}
