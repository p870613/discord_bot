import json
import time

localtime = time.asctime( time.localtime(time.time()))
filename = time.strftime("%Y-%m-%d", time.localtime())
def write_file(data):
    ret = json.dumps(data)
    with open(filename + '.json', 'w') as fp:
        fp.write(ret)

def read_file():
    data = {}
    try:
        print()
        with open(filename + '.json', 'r',encoding="utf-8") as read_file:
            data = json.load(read_file)
    except:
        ret = json.dumps(data)
        with open(filename + '.json', 'w') as fp:
            fp.write(ret)
    return data


