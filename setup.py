##############################################################################
#
# Copyright (c) 2006 Zope Corporation and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
"""Setup for zope.app.securitypolicy package

$Id$
"""

import os

from setuptools import setup, find_packages

def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

setup(name='zope.app.securitypolicy',
    version = '3.4.6dev',
    author='Zope Corporation and Contributors',
    author_email='zope3-dev@zope.org',
    description='Zope securitypolicy',
    long_description=(
        read('README.txt')
        + '\n\n' +
        read('CHANGES.txt')
        ),
    keywords = "zope3 security policy",
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Zope Public License',
        'Programming Language :: Python',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Topic :: Internet :: WWW/HTTP',
        'Framework :: Zope3'],
    url='http://svn.zope.org/zope.app.securitypolicy',
    license='ZPL 2.1',
    packages=find_packages('src'),
    package_dir = {'': 'src'},
    namespace_packages=['zope', 'zope.app'],
    extras_require = dict(test=['zope.app.testing']),
    install_requires=['setuptools',
                      'zope.annotation',
                      'zope.app.form',
                      'zope.app.security',
                      'zope.component [hook]',
                      'zope.configuration',
                      'zope.exceptions',
                      'zope.i18n',
                      'zope.i18nmessageid',
                      'zope.interface',
                      'zope.location',
                      'zope.schema',
                      'zope.security',
                      'zope.security',
                      ],
    include_package_data = True,
    zip_safe = False,
    )
