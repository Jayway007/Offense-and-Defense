# [Comands](https://docs.docker.com/engine/reference/commandline/docker/)
- --version / -v
- search "keyword" : search for specific images through the Docker Hub
- pull tenent/container: pull a specific image from the Docker Hub
- images : 
- ps : list running containers
- stop/restart/kill : stop/restart a container using the name or id
- run : create a container from an image
  - -p / --publish [host-port]:[container-port] : publish container's port to host
  - --rm : Automatically remove the container when it exists
- exec : Execute a command in a running container
  - docker exec [OPTIONS] container-id commands [ARGS]
  - --name : name of container
  - -d / --detach : detached mode : run command in background
  - -t / ---tty : Allocate a pseudo-TTY
  - -i / --interactive : Keep STDIN open even if not attached
  - -w / --workdir : Working directory inside the container, if not exist will create inside the container
- attach : Attach your terminal's standard input, output and error to a running container
- logs container-id : check the logs of container
- inspect : Provide detailed information on constructs


## Example
- Setup a log4j vulnerability:
```bash
service docker start
docker pull vulfocus/log4j2-rce-2021-12-09
docker run -tid -p 38080:8080 vulfocus/log4j2-rce-2021-12-09
```
## Resources
- [awesome-docker](https://awesome-docker.netlify.app/) : A curated list of Docker resources and projects
