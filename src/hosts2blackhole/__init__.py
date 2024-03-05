import requests

def cli():
  print ('Works!')
  r = requests.get('http://sbc.io/hosts/hosts')
  outfile = open('blacklist','w')
  outfile.write(r.text)
  outfile.close()
  print ('blackhole file created')