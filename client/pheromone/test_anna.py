kvs_client = AnnaTcpClient(kvs_addr, ip, local=False, offset=thread_id + 10)


kvs_client.put("key", "value")

value = kvs_client.get("key")