import sys, getopt
from fetch_module import Fetch
from meta import MetaProcessor
from save import Save

from utils import *

_fetch = Fetch()
_save = Save()
mp = MetaProcessor()

def main(urls):
    for url in urls:
        _url = unify_urls(url)
        if mp.load_meta(_url):
            res = input("%s exists already, do you want to update metadata ? y/n " % (_url))
            if res!="y":
                continue
        html = _fetch.fetch_url(_url)
        _save.save_site(html, _url)
        _save.save_assets(html, _url)
        _save.save_meta(html, _url)

def get_metadata(url):
    url = unify_urls(url)
    metadata = mp.load_meta(url)
    if metadata:
        for k,v in metadata.items():
            print("%s : %s"%(k, v))
    else:
        print("This site does not exist.")

if __name__ == "__main__":
    argv = sys.argv[1:]
    opts, args = getopt.getopt(argv, "m:", "meta =")
    if len(opts) > 0:
        get_metadata(opts[0][1])
    elif len(args) > 0:
        main(args)
    else:
        print("Unknown command")
    

    