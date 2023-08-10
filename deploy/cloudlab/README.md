# Deploy Pheromone on Cloudlab

### Create new experiment on Cloudlab

- chose k8s profile and create the experiment
	- 7 nodes and 5 public ip (maybe 2 public ip already enough?)
- wait for the setup complete email

### Connect to the node0 
```sh
ssh into the node-0
git clone https://github.com/KevinZTW/pheromone.git
pip install kubernetes
pip install zmq

kubectl label nodes node-0 role=management
kubectl label nodes node-1 role=general
kubectl label nodes node-2 role=routing
kubectl label nodes node-3 role=memory
kubectl label nodes node-4 role=function
kubectl label nodes node-5 role=coordinator
kubectl label nodes node-6 role=sender

# in below operation we don't use the ebs node

cd pheromone
export PHERO_HOME=$(pwd)
cd deploy/local
python3 -m deploy.cluster.create_cluster  -m 1 -r 1 -c 1 -f 1


sudo apt-get install protobuf-compiler
pip install protobuf==3.20.0

cd ../..
scripts/compile.sh #generate protos

cd client/anna_client
sudo python3 ./setup.py install

wget -qO- https://ipecho.net/plain | xargs echo # get my ip?
# fill in the ip, routing service's external ip as anna_address, management ip as pheromone_address in the PheromoneClient() argument in  /client/pheromone/bench_common.py
cd ../pheromone

$ pheromone/client/pheromone python3 -m benchmarks.event_gen
```
