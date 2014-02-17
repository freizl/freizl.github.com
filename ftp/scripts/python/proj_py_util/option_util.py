#!/usr/bin/python
import sys
from optparse import OptionParser

class VidaOption:
	def __init__(self, argv):
		self.parser = OptionParser()
		self.parser.add_option("-W", "--Workspace", dest="workspace", help="the workspace.")
		self.parser.set_defaults(workspace="trunk")
		self.argv = argv
	def parse_args(self):
		if len(self.argv) == 0: self.argv = ['-h']
		return self.parser.parse_args(self.argv)

class DeployOption(VidaOption):
	def __init__(self, argv):
		VidaOption.__init__(self, argv)
		self.parser.add_option("-A", "--All", action="store_true", dest="deployAll", help="deploy all modules.")
		self.parser.add_option("-T", "--Test", action="store_true", dest="deployDao", help="deploy dao wrappers")
		self.parser.add_option("-C", "--Clover", action="store_true", dest="clover", help="clover compile")

class MergeOption(VidaOption):
	def __init__(self, argv):
		VidaOption.__init__(self, argv)
		self.parser.add_option("-B", "--Branch", dest="branchName", help="The name of branch being merge.")
		self.parser.add_option("-M", "--Module", dest="moduleName", help="The module name which is about to be merged.")
		self.parser.add_option("-U", "--UserName", dest="userName", help="Filter svn log by the User Name")
		self.parser.set_defaults(userName="")

class SwitchOption(VidaOption):
	def __init__(self, argv):
		VidaOption.__init__(self, argv)
		self.parser.add_option("-U", "--Url", dest="branchUrl", help="Switch to a branch.")
		self.parser.add_option("-T", "--Trunk", action="store_true", dest="trunk", help="Switch to Trunk.")
		self.parser.set_defaults(workspace="branch")

################## Self Testing
def main(argv):
	print 'unit test on DeployOption'
	opts, args = DeployOption(argv).parse_args()
	print opts
	print args

if __name__ == '__main__':
	main(sys.argv[1:])
