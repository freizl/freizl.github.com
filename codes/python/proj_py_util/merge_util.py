#!/usr/bin/python
import sys, os
from common_util import LoggerFactory
from option_util import MergeOption

class SvnMerge:
	def __init__(self, argv):
		self.opts, self.args = MergeOption(argv).parse_args()
		if not os.path.isdir(self.opts.workspace):
			print 'can not find the directory: %s' % opts.workspace
			sys.exit(1)
		os.chdir(self.opts.workspace)	
		if not os.path.isfile('svnmerge.py'): os.system('cp ../svnmerge.py . ')
		self.list = ['python svnmerge.py','',self.opts.moduleName, ' -S ', 'branches/', self.opts.branchName]

	def do_avail_check(self):
		self.list[1] = ' avail --log '
		out = self._execute(self.list)
		#if not '' == self.opts.userName:
		out = self._exstract_svn_log(out, self.opts.userName)
		#print ('').join(out)

	def do_merge(self, svn_revisions):
		self.list[1] = ' merge -r ' + svn_revisions + ' '
		self._execute(self.list)

	def _execute(self, cmd):
		return LoggerFactory(cmd).log()

	def _exstract_svn_log(self, message, user_name=''):
		if '' == self.opts.userName:
			print ('').join(message)
			return
		#TODO better way to extract the log?
		start_index, end_index = 0, 0
		svn_log_line_break = '-' * 72
		result = ['']
		for i in range(len(message)):
			if svn_log_line_break in message[i] and user_name in message[i+1]:
				start_index = i
				i += 3 # why forward 3 steps?because at least one merge item list.
				while i <= len(message) and not svn_log_line_break in message[i]:
					i += 1
				end_index = i - 1
				result.extend(message[start_index:end_index])
		print result

def main(argv):
	#print 'the opts:', opts
	svnMerge = SvnMerge(argv)
	svnMerge.do_avail_check()
	svn_revisions = raw_input('continue merge?(input repo version or exit(q)):')
	if len(svn_revisions) == 0 or svn_revisions == 'q':
		return
	svnMerge.do_merge(svn_revisions)

if __name__ == '__main__': 
	main(sys.argv[1:])
