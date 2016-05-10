import urllib.parse
import urllib.request
import re
import os
import tqdm


def connect(url):
    try:
        req = urllib.request.Request(url)
        resp = urllib.request.urlopen(req)
        respData = resp.read()

        saveFile = open('withHeaders.txt', 'w')
        saveFile.write(str(respData))
        saveFile.close()
    except Exception as e:
        print(str(e))


def download(url):
    url = url[0:-5].replace('res', 'src') + '/'


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
    file_list = os.listdir('./done_webm')
    done_list = [url + i for i in file_list]

    done_set = set(done_list)
    downl_set = st_set.difference(done_set)
    if len(downl_set) != 0:
        os.chdir('./done_webm')
        for i in tqdm.tqdm(downl_set):
            fileName = i.split('/')
            urllib.request.urlretrieve(i, fileName[-1])

if __name__ == '__main__':
    connect('https://2ch.hk/b/res/126102702.html')
    download('https://2ch.hk/b/res/126102702.html')
