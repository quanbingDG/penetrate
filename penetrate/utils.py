#!/usr/bin/env python
# -*- coding:utf8 -*-


""" 
@author: quanbing 
@file: utils.py 
@time: 2019/09/25
@contact: quanbinks@sina.com
"""


def check_lenth(x, y):
	try:
		if len(x) == len(y):
			return True
	except:
		return False
	return False
