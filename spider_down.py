import requests


class url_down(object):

    def download_url(self,url):
        if url is None:
            return None
        response = requests.get(url)
        if response.status_code!=200:
            return None
        else:
            return response.content.decode('utf-8')


