#!/bin/bash

docker build - < Dockerfile_pip_tools -t pip_tools_image
docker run --rm -it -v $(pwd):/app pip_tools_image pip-compile --output-file requirements.txt requirements.in
docker image rm pip_tools_image
