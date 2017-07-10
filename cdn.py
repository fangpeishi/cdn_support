# -*- coding: utf-8 -*-

import sys
from pelican import signals
import os
import re


reload(sys)
sys.setdefaultencoding('utf8')


def replace_link(pelican):
    cdn_type = pelican.settings['CDN_TYPE'] or [".css", ".js", ".jpeg", ".png", ".gif", ".jpg"]
    cdn_domain = pelican.settings['CDN_DOMAIN']

    for root, dirs, files in os.walk(pelican.settings['OUTPUT_PATH']):
        for outfile in files:
            if os.path.splitext(outfile)[1] in [".html", ".htm"]:
                file_path = os.path.join(root, outfile)
                with open(file_path, "r+") as f:
                    src = f.read()
                    for ext in cdn_type:
                        keyword = 'src'
                        if ext == ".css":
                            keyword = 'href'

                        pattern = keyword+'="(' + pelican.settings['SITEURL'] + '/|/)([^:"]*)\\' + ext+'"'
                        repl = keyword+'="//'+cdn_domain+'/'+r'\2'+ext+'"'
                        src = re.sub(pattern, repl, src)
                    f.seek(0)
                    f.write(src)



def register():
    signals.finalized.connect(replace_link)
