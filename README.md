# dibbla-spark-cluster
This is a simple project to create a Spark cluster using Docker and Docker Compose. The project is based on the [bitnami Docker image](https://hub.docker.com/r/bitnami/spark/).

Notice that one would need to modify the volume paths in the `docker-compose.yml` file to match the local paths on the host machine.

## Issues to deal with before running anything
Here is the help from almighty ChatGPT: https://chatgpt.com/share/67c69a8b-1e90-8006-9c33-e6f5f40dbfd7

1. First of all, login with `--user root` option, and install sudo.
2. Create a new user and add to sudoer. We can login with that user later.
3. Install the javac and scala (corresponding version).
4. Try to compile and run.