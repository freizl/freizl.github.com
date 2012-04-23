#!/usr/bin/python
from common_util import *
from option_util import DeployOption

class DeployUtil:
	def __init__(self, argv):
		self.logfile = 'deploy.log'
		self.opts, self.args = DeployOption(argv).parse_args()
		#TODO if nothing in the opts, echo help message
	def deploy(self):
		self._deploy(self.opts, self.args)

	""" if dirname is awXXX, doing awXXX/ant clean main undeploy deploy
	    if dirname is coreXXX, doing coreXXX/ant clean main publishLocal; then awXXX/ant clean main undeploy deploy
		if parameter A exists, doing awBuild 'ant -Dbuild.core=yes cleanAll main undeployAll deployAll
		if parameter T exists, deploy its dao wrapper after deploy module.
		if parameter C exists, compile clover"""
	#TODO refactoring the for loop.
	def _deploy(self, opts, dirlist):
		import os
		os.chdir(opts.workspace)	#TODO if is dir,change to the dir else echo waring message
		if os.path.isfile(self.logfile): os.remove(self.logfile)
	
		if opts.deployAll == True:		
			self._execute(['ant -f awBuild/build.xml -Dbuild.core=yes cleanAll main undeployAll deployAll'])
		elif len(dirlist) >= 1:
			ant_target = ['ant -f ','module_name_placehold','/build.xml clean ', 'main ', '']
			if opts.clover: ant_target[-2] = 'main.clover '
			build_success = True
			for dirname in dirlist:
				ant_target[1] = dirname
				if build_success and dirname.startswith('core') and not dirname == 'coreWebApp':
					ant_target[-1] = 'publishLocal'
					build_success = self._execute(ant_target)
					ant_target[1] = dirname.replace('core','aw')
				if build_success:
					ant_target[-1] = 'undeploy deploy '
					if opts.deployDao and not dirname == 'coreWebApp': ant_target.extend('deployDaoWrappers')
					build_success = self._execute(ant_target)
		else:
			print "no modules found"
		os.system('gvim '+ self.logfile + ' G')
	def _execute(self, cmd):
		return LoggerFactory(cmd, self.logfile).log_ant()

def main(argv):
	DeployUtil(argv).deploy()

if __name__ == '__main__':
	import sys
	main(sys.argv[1:])

