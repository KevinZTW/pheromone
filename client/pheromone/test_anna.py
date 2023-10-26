from anna.client import AnnaTcpClient


kvs_addr="128.110.97.141"
ip="128.110.96.35"
thread_id=0

kvs_client = AnnaTcpClient(kvs_addr, ip, local=False, offset=thread_id + 10)


kvs_client.put("key", "value")

value = kvs_client.get("key")