def pretty(d, indent=0):
   for key, value in d.items():
      print('\t' * indent + str(key))
      if isinstance(value, dict):
         pretty(value, indent+1)
      else:
         print('\t' * (indent+1) + str(value))

def testJson(json_object):
   with open("mechafiles/Tests/test.json", "w") as outfile:
      outfile.write(json_object)
