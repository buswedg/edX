#!/usr/bin/env python

import sys
import string

while True:
  line = sys.stdin.readline()
  if not line:
    break

  row = string.strip(line, "\n ")
  log_date, requests, inbound_bytes, outbound_bytes = string.split(row, "\t")
  inbound_mbytes = long(inbound_bytes) / 1048576
  outbound_mbytes = long(outbound_bytes) / 1048576
  print "\t".join([log_date, requests, str(inbound_mbytes), str(outbound_mbytes)])

