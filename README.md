# locust-gke-test

This chart will create a load test environment using [Locust](http://locust.io/) on GKE.

## How to setup

### 1. create Locust task docker image

* creating docker image referening [Locust](http://locust.io/)
* push image to GCR

### 2. create GKE cluster

```sh
rake cluster:create
```

### 3. deploy

```sh
rake helm:install DOCKER_IMAGE=<your docker image>
```

### 4. perform from web ui

* see the LB's external IP and access from your browser

```sh
kubectl --namespace locust-gke-test get svc
```
