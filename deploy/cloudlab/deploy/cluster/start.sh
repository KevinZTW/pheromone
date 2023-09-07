export PHERO_HOME=$(pwd)

pip install kubernetes
pip install zmq

sudo apt-get install protobuf-compiler
pip install protobuf==3.20.0
pip install numpy



kubectl label nodes node-0 role=management
kubectl label nodes node-1 role=general
kubectl label nodes node-2 role=routing
kubectl label nodes node-3 role=memory
kubectl label nodes node-4 role=function
kubectl label nodes node-5 role=coordinator
kubectl label nodes node-6 role=sender



cd deploy/cloudlab
python3 -m deploy.cluster.create_cluster  -m 1 -r 1 -c 1 -f 1



/bin/bash ${PHERO_HOME}/scripts/compile.sh

cd ../..
cd client/anna_client 
sudo python3 ./setup.py install

echo "host IP:"
wget -qO- https://ipecho.net/plain | xargs echo
cd ../pheromone