#/bin/bash

docker stop -t0 : demo_api ; docker rm demo_api

docker build -t demo_cdr_web_api  .

touch "$(pwd)/cdr.txt"

docker run --name demo_api  -p 5000:5000 --mount type=bind,source="$(pwd)"/cdr.txt,target=/app/cdr.txt -d demo_cdr_web_api

docker logs -f demo_api
