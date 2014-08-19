'''append:
Append a string to a file
Usage: append [String] [File]
'''

from ... tools.toolbox import bash
import os

alias=['a']

def main(self, line):
    """Append to file"""
    args = bash(line)
    if args is None:
      return
    elif (len(args) != 2):
      print "append usage: append [String] [File]"
    else:
      content = args[0]
      target = args[1]
      if (os.path.isdir(target)):
        print "append: %s: Is a directory" % target
      elif (os.path.exists(target)):
        try:
          with open(target, 'a') as f:
            f.write("\n")
            f.write(content)
            f.close()
          print "Appending to: %s " % target
          print ">>>>"
          print content
          print ">>>>"
        except Exception:
          print "append: Unable to write to file %s" % target
