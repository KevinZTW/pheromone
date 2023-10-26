# Deploy Pheromone on Cloudlab

## Basic

1. select the `k8s` profile (https://gitlab.flux.utah.edu/johnsond/k8s-profile)
2. chose k8s profile and create the experiment
	- 7 nodes and 5 public ip (probabaly 2 public ip should be enough I haven't tried yet)
	- for the hardware type, usually `Any type` works 
		- but  the node for `function` would consume around 27 GB memory (base on spec on `pheromone/deploy/cloudlab/deploy/cluster/yaml/ds/function-ds.yml`) we need to chose the machine with enough memory (e.g. APT Utah 6220)

3. wait for the setup completed email (~20 minutes)
4. ssh connect to the node-0
5. git clone https://github.com/KevinZTW/pheromone.git
6. `cd pheromone`
7. `./start.sh`
8. could exeucte `./deploy/cloudlab/deploy/cluster/cleanup.sh` if you want to remove all pheromone related service and pods
9. also there's `client/pheromone/test_anna.py` which is pretty simple script to test AnnaKV is up

### `start.sh`
This script would mainly do three thing

- compile the C++ code  `examples/cpp/event_stream` using  Ubuntu 18.04 docker container
- execute the `deploy/cloudlab/deploy/cluster/start.sh` to deploy pheromone, I would write down more detail in next sectoin
- upload the `event_stream` binary to pheromone cluster

Once the script finished successfully, we could find three  ip from the console output
- machine `node-0` IP
- AnnaKV (routing) service external IP 
- pheromone mangement service external IP

We need to adjust the code in `./client/pheromone/bench_common.py` with data above
The we could run the `event_stream` benchmark by
- `cd ~/pheromone/client/pheromone`
- `python3 -m benchmarks.event_gen`

### Pheromone deployment script 
- we use the `deploy/cloudlab/deploy/cluster/start.sh` to deploy pheromone

Mainly it would 
- install some dependencies for our benchmark python scripts
- label nodes to different role, most of our service would run on specific role, it won't deploy if related role is missing, I not sure if there's anything I missed
- run the `deploy.cluster.create_cluster` python script to create all pods, services, daemonsets for pheromone and annaKV
	- what I've done is 
		- remove the script to call kops spin up machine and the aws part
		- change to use k8s service external ip instead of k8s service address
	- it's also quite similiar to the origin [hydro project create cluster script](https://github.com/hydro-project/cluster/blob/master/hydro/cluster/create_cluster.py)


