import fnmatch
import os
import subprocess
import sys


class ProcOutput(object):
  def __init__(self, stdout=sys.stdout, fno=-1):
    self.fno = fno
    self.stdout = stdout

  def fileno(self):
    return self.fno

  def write(self, string):
    self.stdout.write(string)

  def readlines(self):
    return self.lines


def run_cmd(cmd, cwd='.', bufsize=1, **kwargs):
  """
  Runs a command in the backround by creating a new process and writes the output to a specified log file.

  :param cwd(str) - basedir to write/create the log file
  :param bufsize(int) - set the output buffering, default is 1
  """
  debug = kwargs.get('debug', True)
  if debug is True:
    stdout = kwargs.get('stdout', ProcOutput())
  else:
    stdout = open('/dev/null', 'w+')
  stderr = kwargs.get('stderr', stderr)
  proc_args = {
    'stdout': stdout,
    'stderr': stderr,
    'buffsize': buffsize,
    'cwd': cwd,
    'universal_newlines': True
  }

  with subprocess.Popen(cmd, **proc_args) as proc:
    pass


def find(root_dir, pattern='*'):
  matches = []
  for (root, dirnames, filenames) in os.walk(root_dir):
    for filename in fnmatch.filter(filenames, pattern):
      matches.append(os.path.join(root, filename))
  return matches
