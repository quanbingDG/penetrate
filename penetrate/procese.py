#!/usr/bin/env python
# -*- coding:utf8 -*-


""" 
@author: quanbing 
@file: procese.py 
@time: 2019/09/25
@contact: quanbinks@sina.com
"""

import pandas as pd
import numpy as np


class procese:
	def __init__(self):
		pass

	@staticmethod
	def split_data(data: [pd.Series, list], bins: int = 10, assign: bool = False,
	               right=True, labels=None, retbins=False, precision=3,
	               include_lowest=False, duplicates='raise'):
		if not assign:
			return pd.qcut(data, bins, labels=labels, retbins=retbins, precision=precision, duplicates=duplicates)
		elif assign:
			return pd.cut(data, bins, right=right, labels=labels, retbins=retbins,
			              precision=precision, include_lowest=include_lowest,
			              duplicates=duplicates)

	@staticmethod
	def get_unique(data: pd.Series, dorpna=True):
		return data.unique().dropna() if dorpna else data.unique()

	@staticmethod
	def get_bins(x, unique_bins):
		if np.isnan(x):
			return 'nan'
		for i in unique_bins:
			if x in i:
				return str(i)
		raise ValueError('the x value is out of the unique_bins, please check your split_bins')
