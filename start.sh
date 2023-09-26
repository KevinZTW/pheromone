
# compile functions
docker run --rm -v /users/kevinztw/pheromone/:/users/kevinztw -it ubuntu:18.04 bash -c \
    "apt update && \
    apt install -y g++ && \
    cd /users/kevinztw/examples/cpp/event_stream && \
    chmod +x compile.sh && \
    ./compile.sh"

cd /users/kevinztw/pheromone/examples/cpp/event_stream
chmod +x upload.sh
./upload.sh

# spin up pheromone
./deploy/cloudlab/deploy/cluster/start.sh

# ./deploy/cloudlab/deploy/cluster/cleanup.sh