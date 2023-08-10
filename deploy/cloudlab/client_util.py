import kubernetes as k8s
from deploy.cluster import util

NAMESPACE = 'default'

def get_service_address_minikube(client, svc_name):
    service = client.read_namespaced_service(namespace=NAMESPACE,
                                             name=svc_name)

    return service.spec.cluster_ip


def init_k8s():
    cfg = k8s.config
    cfg.load_kube_config()
    client = k8s.client.CoreV1Api()
    apps_client = k8s.client.AppsV1Api()

    return client, apps_client

client, apps_client = init_k8s()
cfg = k8s.config
cfg.load_kube_config()
client = k8s.client.CoreV1Api()
# service = client.read_namespaced_service(namespace="default", name='management-service')
# print(service)


# service = client.read_namespaced_service(namespace=NAMESPACE,
#                                                  name='routing-service')
# print(service)
route_addr = util.get_service_address(client, 'routing-service')
print(route_addr)


res = util.get_pod_ips(client, 'role=function', is_running=True)
print(res)

