import urllib.parse
import urllib.request
import re
import os

def connect():
    try:
        url = 'https://2ch.hk/b/res/126009073.html'

        req = urllib.request.Request(url)
        resp = urllib.request.urlopen(req)
        respData = resp.read()

        saveFile = open('withHeaders.txt', 'w')
        saveFile.write(str(respData))
        saveFile.close()
    except Exception as e:
        print(str(e))


def my_read():
    f = open('withHeaders.txt', 'r')
    string = f.read()
    match = r'href="(.*?)"'
    need = re.findall(match, string)
    st_list = []
    for st in need:
        if st.endswith('.webm'):
            st = st.replace('..', 'https://2ch.hk/b')
            st_list.append(st)

    st_set = set(st_list)
    done_set = os.listdir('./done_webm')
    st_set = st_set.difference(done_set)
    if len(st_set) != 0:
        os.chdir('./done_webm')
        for i in st_set:
            print(i, '...')
            fileName = i.split('/')
            urllib.request.urlretrieve(i, fileName[-1])
            print('Done')
if __name__ == '__main__':
    connect()
    my_read()