#coding: utf-8

import requests


def run(target):
    "test backup file"
    results = []
    files = [
        "/backup.rar",
        "/backup.zip",
        "/backup.tar.gz",
        "/www.rar",
        "/www.zip",
        "/www.tar.gz",
        "/data.rar",
        "/data.zip",
        "/data.tar.gz"
    ]

    for i in target.split("."):
        files.append("/"+i+".rar")
        files.append("/"+i+".zip")
        files.append("/"+i+".tar.gz")

    f_seted = sorted(list(set(files)))

    for f in f_seted:
        url = "http://" + target + f
        print(url)
        try:
            r = requests.head(url, timeout=5)
        except Exception:
            continue
        else:
            r.close()
            if r.status_code == 200:
                results.append(url)
        print(target, "ok")

    return results
