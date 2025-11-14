import psutil
import time

before = psutil.net_io_counters()
time.sleep(1)
after = psutil.net_io_counters()

download_speed = after.bytes_recv - before.bytes_recv
upload_speed = after.bytes_sent - before.bytes_sent

print("Download Speed:", download_speed, "Bytes/s")
print("Upload Speed:", upload_speed, "Bytes/s")