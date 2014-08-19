'''write:
Write a string to a file
Usage: write [String] [Filename]
'''

from .. tools.toolbox import bash
import os


def main(self, line):
    """print file"""
    args = bash(line)
    if args is None:
      return
    elif (len(args) != 2):
      print "write usage: write [String] [Filename]"
    else:
      content = args[0]
      target = args[1]
      if (os.path.exists(target)):
        print "write: %s: File exists" % target
      elif (os.path.isdir(target)):
        print "write: %s: Is a directory" % target
      else:
        try:
          contents = ""
          with open(target, 'w') as f:
            f.write(content)
            f.close()
          print "Writing to: %s " % target
          print ">>>>"
          print contents
          print ">>>>"
        except Exception:
          print "write: Unable to create file %s" % target