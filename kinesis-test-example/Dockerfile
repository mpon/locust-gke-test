#ref: https://github.com/GoogleCloudPlatform/distributed-load-testing-using-kubernetes/blob/master/docker-image/Dockerfile
FROM python:2.7.8

LABEL  maintainer "mpon <qqw75pn9@gmail.com>"

# Install locustio
RUN pip install locustio pyzmq boto

# Add the external tasks directory into /tasks
ADD locust-tasks /locust-tasks
COPY locust-tasks/.boto /root/.boto

# Expose the required Locust ports
EXPOSE 5557 5558 8089

# Set script to be executable
RUN chmod 755 /locust-tasks/run.sh

# Start Locust using LOCUS_OPTS environment variable
ENTRYPOINT ["/locust-tasks/run.sh"]
