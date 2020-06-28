from fdfs_client.client import *
trackers = get_tracker_conf('/etc/fdfs/client.conf')
client = Fdfs_client(trackers)
list = []
for i in range(1, 3):
    ret = client.upload_by_filename('/home/python/Desktop/goods/adv0%d.jpg' % i)
    list.append(ret['Remote file_id'])
print(list)
