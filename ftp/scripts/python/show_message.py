#! /usr/bin/env python
import sys

class CP037Helper:
	_CHARSET = 'cp037'
	def __init__(self, message):
		""" CP037Helper(message) - takes a message and converts it to a unicode format"""
		self.__message = unicode(message, self._CHARSET)
	def show_in_utf8(self):
		"show_in_utf8() - displays the message in utf8"
		print self.__message.encode('utf8')

if __name__ == '__main__':
	msg_file = open(sys.argv[1], 'r')
	CP037Helper(msg_file.read()).show_in_utf8()
	msg_file.close()
