#!/usr/bin/env python

import sys

squid_log = '/var/log/squid/access.log'

domain_pv = {}
domain_size = {}
for line in open(squid_log, 'r'):
	try:
		[time, resp_time, ip, status, size, method, url, ident, server, type] = line.split()
		domain = url.lstrip('http://').split('/')[0]
		domain_pv.setdefault(domain, 0)
		domain_size.setdefault(domain, 0)
		domain_pv[domain] += 1
		domain_size[domain] += int(size)
	except Exception,e:
		print e

domain_pv = sorted(domain_pv.items(), key=lambda domain_pv:domain_pv[1], reverse=True)
domain_size = sorted(domain_size.items(), key=lambda domain_size:domain_size[1], reverse=True)

if len(sys.argv) > 1 and sys.argv[1] == 'pv':
	for domain in domain_pv:
		print domain[1], '\t', domain[0]
else:
	for domain in domain_size:
		print domain[1], '\t', domain[0]
