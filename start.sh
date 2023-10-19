
# compile functions

docker run --rm -v /users/kevinztw/pheromone/:/users/kevinztw -it ubuntu:18.04 bash -c \
    "apt update && \
    apt install -y g++ && \
    cd /users/kevinztw/examples/cpp/event_stream && \
    chmod +x compile.sh && \
    ./compile.sh"

# spin up pheromone cluster, including it's dependency annaKV
./deploy/cloudlab/deploy/cluster/start.sh

export PHERO_HOME=$(pwd)

# chmod +x ./examples/cpp/event_stream/upload.sh
cd $PHERO_HOME/examples/cpp/event_stream
./upload.sh

# ./deploy/cloudlab/deploy/cluster/cleanup.sh
cd $PHERO_HOME/client/pheromone 

# need to modify the client argument before run this
# python3 -m benchmarks.event_gen