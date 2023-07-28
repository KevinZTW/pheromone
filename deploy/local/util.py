import kubernetes as k8s

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
service = client.read_namespaced_service(namespace="default", name='management-service')
print(service.spec)