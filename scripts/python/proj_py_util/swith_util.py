#!/usr/bin/python
import sys,os
from common_util import LoggerFactory
from option_util import SwitchOption

"""switch to branch module by module"""
class SwitchUtil():
	def __init__(self, argv):
		self.opts, self.args = SwitchOption(argv).parse_args()
		print self.opts, self.args
		self.switch_cmd = ['svn switch http://10.3.160.78/vida/','','/branches/',self.opts.branchUrl,' ', '']
		#switch_cmd = ['svn switch svn://localhost/','','/branches/',self.opts.branchUrl,' ', '']
		self.exclude_dirs = [".svn","schip_dev"]
		self.logfile = 'switch.log'
		if not os.path.isdir(self.opts.workspace):
			print 'can not find the directory: %s' % self.opts.workspace
			sys.exit(1)
		if self.opts.workspace == 'trunk': print 'Main workspace (',self.opts.workspace,') is not allowed to be switched.'
		os.chdir(self.opts.workspace)
		if os.path.isfile(self.logfile): os.remove(self.logfile)
	def switch(self):
		_log = LoggerFactory('', self.logfile)
		def _do_switch(_dirname) :
			self.switch_cmd[1] = self.switch_cmd[-1] = _dirname
			_log.log(('').join(self.switch_cmd))
		map(_do_switch, [ d for d in os.listdir('.') if os.path.isdir(d) and not d in self.exclude_dirs ] )
		os.system('gvim ' + self.logfile)
	def _emptyAwLib(self):
		aw_lib = ["awLib"]
		dirs = ["core","aw","coreTest"]
		map(removeall, [os.path.join(aw_lib[0],x) for x in dirs])
	def _removeall(self, path):
		if not os.path.isdir(path): return
		files = os.listdir(path)
		for x in files:
			fullpath = os.path.join(path, x)
			if os.path.isfile(fullpath):
				os.remove(fullpath)
			elif os.path.isdir(fullpath) and fullpath.find("svn") < 0:
				removeall(fullpath)
				os.rmdir(fullpath)

def main(*argv):
	SwitchUtil(list(argv)).switch()

if __name__ == '__main__':
	import time
	start = time.clock()
	apply(main,sys.argv[1:])
	print 'Total Time: ', str(time.clock() - start)

