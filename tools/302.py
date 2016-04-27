#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys,base64,re

def redirect_url(request, domains_pattern):
    _l_temp = request.split()
    url = 'E'+_l_temp[0]
    if re.match(domains_pattern, request) != None:
        new_request = '302:http://www.healthsciencehot.com?'+base64.b64encode(url)
    else:
        new_request = ''
    return new_request
        
def main():
    domains = "(http://www.xvideos.com/)"
    domains_pattern = re.compile(domains)
        
    line = sys.stdin.readline().strip()
    while line:
        line = redirect_url(line, domains_pattern) + '\n'
        sys.stdout.write(line)
        sys.stdout.flush()
        line = sys.stdin.readline().strip()

if __name__ == '__main__':
    main()

