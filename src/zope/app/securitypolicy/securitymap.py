##############################################################################
#
# Copyright (c) 2001, 2002 Zope Corporation and Contributors.
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
"""Generic two-dimensional array type (in context of security)

$Id$
"""

import zope.deferredimport

zope.deferredimport.deprecated(
    "It has moved to zope.securitypolicy.securitymap  This reference will be "
    "removed somedays",
    SecurityMap = 'zope.securitypolicy.grantinfo:SecurityMap',
    PersistentSecurityMap = 'zope.securitypolicy.grantinfo:PersistentSecurityMap',
    AnnotationSecurityMap = 'zope.securitypolicy.grantinfo:AnnotationSecurityMap',
    )
