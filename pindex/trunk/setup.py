#!/usr/bin/env python

from distutils.core import setup

setup(  name='pindex',
        version='0.1',
        description='full text index via solr',
        author='Kenny Lu',
        author_email='luzhuomi@gmail.com',
        url='',
        packages=['pindex'
	          #,'pindex.index'
		 ],
	platforms=["any"],
        long_description="This module offers a full text index via solr.",
        requires=['pysolr'],

     )

