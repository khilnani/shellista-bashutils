'''write:
Write a string to a file

Usage:
  write [String] [File]
  w [String] [File]
'''

from ... tools.toolbox import bash
import os

alias=['w']

def main(self, line):
    """Write to file"""
    args = bash(line)
    if args is None:
      return
    elif (len(args) != 2):
      print "write usage: write [String] [File] or: w [String] [File]"
    else:
      content = args[0]
      target = args[1]
      if (os.path.exists(target)):
        print "write: %s: File exists. Use: append [String] [File] or: a [String] [File]" % target
      elif (os.path.isdir(target)):
        print "write: %s: Is a directory" % target
      else:
        try:
          with open(target, 'w') as f:
            f.write(content)
            f.close()
          print "Writing to: %s " % target
          print ">>>>"
          print content
          print ">>>>"
        except Exception:
          print "write: Unable to create file %s" % target
