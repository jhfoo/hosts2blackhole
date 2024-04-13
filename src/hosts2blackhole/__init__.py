# core
import argparse
import re

# community
import requests

FILE_HOSTS = 'blacklist'
DEF_FILE_OUT = 'blacklist.conf'

def parseLine(line):
  matches = re.search(r'^([\.\d]+)\s(.+)', line)
  if matches:
    return {
      "address": matches.group(1),
      "domain": matches.group(2)
    }
  # else
  return None

def cli():
  global DEF_FILE_OUT

  parser = argparse.ArgumentParser()
  parser.add_argument('-o', '--out')
  args = parser.parse_args()

  OutFilename = args.out if args.out else DEF_FILE_OUT
  print (f'outfile: {OutFilename}')

  # print ('Downloading latest list...')
  # r = requests.get('http://sbc.io/hosts/hosts')
  # outfile = open(FILE_HOSTS,'w')
  # outfile.write(r.text)
  # outfile.close()
  # print ('Done')

  with open(OutFilename,'w') as outfile:
    LineCount = 0
    DomainCount = 0
    print ('Parsing data...')
    with open(FILE_HOSTS,'r') as infile:
      while True:
        line = infile.readline()
        if not line:
          break

        # else
        LineCount += 1
        record = parseLine(line.strip())
        if record:
          outfile.write (f"address=/{record['domain']}/{record['address']}\n")
          DomainCount += 1
      # infile.close()

  print (f'Lines parsed: {LineCount}')
  print (f'Domains parsed: {DomainCount}')