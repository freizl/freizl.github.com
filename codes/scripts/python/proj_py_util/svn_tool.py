#!/c/Python23/python
import sys,os
from common_util import LoggerFactory

def removeall(path):
	if not os.path.isdir(path):
		return
	files = os.listdir(path)
	for x in files:
		fullpath = os.path.join(path, x)
		if os.path.isfile(fullpath):
			os.remove(fullpath)
		elif os.path.isdir(fullpath) and fullpath.find("svn") < 0:
			removeall(fullpath)
			os.rmdir(fullpath)

def empty_awLib():
	print 'start to empty awLib';
	aw_lib = ["awLib"]
	dirs = ["core","aw","coreTest"]
	map(removeall, [os.path.join(aw_lib[0],x) for x in dirs])

def execute(cmd, logfile):
	return LoggerFactory(cmd, logfile).log()

def svn_action(workspace, action, action_all=False):
	exclude_dirs = [".svn","schip_dev"]
	action_name = ['svn'] + action + ['.log']
	logfile = ('').join(action_name[1:])
	if os.path.isfile(logfile): os.remove(logfile) 

	_logger = LoggerFactory('', logfile)
	if action_all:
		action_name[-1] = '.'
		_logger.log((' ').join(action_name))
	else:
		dirlist = [ d for d in os.listdir('.') if os.path.isdir(d) and not d in exclude_dirs ]
		for _dir in dirlist:
			action_name[-1] = _dir
			_logger.log((' ').join(action_name))
	os.system('gvim ' + logfile)

def argv_help(argv):
	if len(argv) == 0 or argv[0] == 'help':
		print "arguments required: command --w dirname --a true update|status"
		sys.exit(1)
	opts = {}
	out = []
	while argv:
		if argv[0][0:2] == '--':
			opts[argv[0][2:]] = argv[1]
			argv = argv[2:]
		else:
			out = out + [argv[0]]
			argv = argv[1:]
	if not 'w' in opts.keys() or not os.path.isdir(opts['w'])  :
		opts['w'] = 'trunk'
		print 'can find a directory. use default %s' % opts['w']
	return opts, out

def main(*argv):
	opts, action = argv_help(argv)
	os.chdir(opts['w'])
	if action[0].find('st') < 0: empty_awLib();
	svn_action(opts['w'], action[:], 'a' in opts.keys())

if __name__ == '__main__': #TODO use 'try expect' to report error	
	#TODO leverage timer function in common_util
	import time
	start = time.clock()
	apply(main,sys.argv[1:])
	print 'Total Time: ', str(time.clock() - start)

