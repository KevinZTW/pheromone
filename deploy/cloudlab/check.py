import os
import subprocess
import sys

cluster_name="cloudlab"
os.environ["PHERO_CLUSTER_NAME"] = cluster_name



def run_process(command):
    try:
        # subprocess.run(command, cwd='deploy/cluster/kops', check=True)
        subprocess.run(' '.join(command), cwd='deploy/cluster/kops', shell=True)
    except subprocess.CalledProcessError as e:
        print(f'''Unexpected error while running command {e.cmd}
        {e.stderr}

        Make sure to clean up the cluster object and state store before
        recreating the cluster.''')
        sys.exit(1)

run_process(['./modify_ig.sh', "routing", "2"])