# host file
# linux & max /etc/hosts
# C:\Windows\System32\drivers\etc\hosts

import time
from datetime import datetime as dt

host_path = r"hosts"
redirect = "127.0.0.1"
website_list = ["www.facebook.com", "facebook.com"]

while True:
    time.sleep(5)
    print(dt.now())
    dt_start = dt(dt.now().year, dt.now().month, dt.now().day, 23, 21)
    dt_end = dt(dt.now().year, dt.now().month, dt.now().day, 23, 22)

    if dt_start < dt.now() < dt_end:
        print("Working hours...")
        with open(host_path, 'r+') as f:
            content = f.read()
            for website in website_list:
                if website in content:
                    print(website, " is present")
                    pass
                else:
                    print(website, " is added")
                    f.write(redirect + " " + website + "\n")
    else:
        print("Fun hours...")
        with open(host_path, 'r+') as f:
            content = f.readlines()
            f.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    f.write(line)
            f.truncate()

