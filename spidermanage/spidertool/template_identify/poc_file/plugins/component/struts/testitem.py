#!/usr/bin/env python
# encoding: utf-8
from ..t import T

class P(T):
    def __init__(self):
        T.__init__(self)
        keywords=['struts']
        print 'strute init'