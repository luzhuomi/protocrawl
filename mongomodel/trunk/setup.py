#!/usr/bin/env python

from distutils.core import setup

setup(  name='mongomodel',
        version='0.1',
        description='DB Models using mongo model',
        author='Kenny Lu',
        author_email='luzhuomi@gmail.com',
        url='',
        packages=['mongomodel'
	          ,'mongomodel.crawl'
                  ,'mongomodel.crawl.hwz'
                  ,'mongomodel.crawl.toc'
                  ,'mongomodel.crawl.twitter'
		 ],
	platforms=["any"],
        long_description="This module offers a model-style interface to the Mongo DB.",
        requires=['mongoengine'],

     )

