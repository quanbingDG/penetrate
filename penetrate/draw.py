#!/usr/bin/env python
# -*- coding:utf8 -*-


"""
@author: quanbing
@file: test.py
@time: 2019/09/25
@contact: quanbinks@sina.com
@software: PyCharm
"""


from pyecharts.charts import Bar
from pyecharts import options as opts


def bar(x: list, y: list, name: str, title='主标题', subtitle='副标题') -> Bar:
	"""
	:param x: axis x data
	:param y: axis y data
	:param name: the data columns
	:param title: the title of the draw
	:param subtitle: the subtitle of the draw
	:return: object Bar, you can user render() or render_notebook() render the draw page
	### doctest
	>>> x = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
	>>> y = [5, 20, 36, 10, 75, 90]
	>>> name = '商家A'
	>>> title='主标题'
	>>> subtitle='副标题'
	>>> test = bar(x, y, name, title, subtitle)
	>>> hasattr(test, 'render')
	True
	"""

	bar_ = (
		Bar()
			.add_xaxis(x)
			.add_yaxis(name, y)
			.set_global_opts(title_opts=opts.TitleOpts(title=title, subtitle=subtitle))

	)
	return bar_


def bar_multiple(x: list, y: list, name: list, title='主标题', subtitle='副标题') -> Bar:
	"""
	:param x:
	:param y:
	:param name:
	:param title:
	:param subtitle:
	:return:
	### doctest
	>>> x = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
	>>> y = [[5, 20, 36, 10, 75, 90],[10, 20, 30, 40, 50, 60]]
	>>> name = ['商家A', '商家B']
	>>> title='主标题'
	>>> subtitle='副标题'
	>>> test = bar_multiple(x, y, name, title, subtitle)
	>>> hasattr(test, 'render')
	True
	"""
	if len(name) != len(y):
		raise ValueError("the paramter 'name' and 'y' must be same lenth ")

	bar_ = Bar()
	bar_.add_xaxis(x)
	try:
		[bar_.add_yaxis(name[i], y[i]) for i in range(len(name))]
	except:
		raise
	bar_.set_global_opts(title_opts=opts.TitleOpts(title=title, subtitle=subtitle))

	return bar_


if __name__ == '__main__':
	import doctest
	doctest.testmod()


