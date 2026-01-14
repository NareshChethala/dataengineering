# dataengineering
## 1. Docker
* Isolated contatiner from the system
* To run an image:
    * docker run imagename
    * docker run -it imagename ### used to open the image in interative mode
* Whatever we do inside a docker image is isolated from the host system
* When we run "docker run" we are just creating a container using the docker image so whatever we make changes or run inside the container doesnt make any changes to the original image and also the changes that we make additionally inside the docker image doesn't save to the image. Docker containers are stateless.
* We can change the entrypoint by using the tag --entrypoint
    * docker run -it --entrypoint=bash python:3.13.11 --> this will open the container in bash
* docker ps -a will give us all the instances of opened containers
* docker ps -aq will give us the tags of opened conatiners
* docker rm `docker ps -aq` will remove all the containers
* This is an example for volume mapping
    * docker run -it --entrypoint=bash -v $(pwd)/test:/app/test python:3.13.11 --> this will keep the test folder in the local repo inside the docker
 