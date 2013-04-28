#!/usr/bin/env python



# backup
eval_ori = eval 

# Sandboxing
def safe_scope():
	import math
	safe_list = ['math', 'map', 'reduce', 'filter', 'sum', 
	'sorted', 'range', 'max', 'min', 'dict', 'dir', 'int', 
	'str', 'enumerate', 'tuple', 'type', 'any', 'all', 'isinstance',
	'pow', 'basestring', 'issubclass', 'bin', 'iter', 'property', 'bool', 'len',
	'bytearray', 'float', 'list', 'unichr', 'callable', 'format', 'unicode', 'chr',
	'frozenset', 'long', 'vars', 'getattr', 'setattr', 'repr', 'zip', 'reversed', 'complex',
	'hasattr', 'round', 'hash', 'delattr', 'next', 'set', 'oct', 'id', 'slice', 'object']
	return dict([ (k, eval_ori(k)) for k in safe_list ])

def eval(code):
	return eval_ori(code, {"__builtins__": None}, safe_scope())