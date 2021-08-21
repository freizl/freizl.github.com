import sys, os

############################################ Log Factory
class LoggerFactory:
	#TODO cmd is a list. what happened if it's a string?
	#TODO logFileName='default.log'), antCmd='':
	def __init__(self, antCmd='', logFileName='default.log'):
		self.cmd = ('').join(antCmd)
		self.logfile = logFileName
		#if os.path.isfile(logFileName): os.remove(logFileName)
		print 'init log factory:', self.cmd, '>>>', self.logfile
	def log(self, command=None):
		if command : self.cmd = command
		out = ['\n',self.cmd,'\n']
		out.extend(self._pipe_sys_cmd())
		#out = ('').join(out)
		self._output_file(('').join(out))
		return out
	def log_ant(self):
		out = ('').join(self.log())
		if out.find('BUILD FAILED') >= 0:
			return False
		else:
			return True
	def _pipe_sys_cmd(self):
		i,k = os.popen4(self.cmd)
		i.close()
		out = k.readlines() 							# out = k.read()  
		ret = k.close() 								# ret value if none if successful
		return out[:]
	def _output_file(self, out='log nothing'):
		# file(logflle, 'a').write(out)
		file = open(self.logfile,'a')
		file.write(out)
		file.close

############################################ 
def timer(func, *args):
	import time
	start = time.clock()
	apply(func, args)
	return time.clock() - start

############################################### @deprecated with OptionParser class
def getopts(argv):
	if len(argv) == 0 or argv[0] == 'help':
		print "arguments required: merge_util.py -d modul_name -r branch_url"
		sys.exit(1)
	opts = {}
	while argv:
		if argv[0][0] == '-':
			opts[argv[0][1:]] = argv[1]
			argv = argv[2:]
		else:
			argv = argv[1:]
	if not 'm' in opts.keys() or not 'r' in opts.keys():
		print 'Not enough parameter. i.e.: -m awConcept -r AW_0-9-1_branch' 
		print opts.keys()
		sys.exit(1)
	else:
		return opts
