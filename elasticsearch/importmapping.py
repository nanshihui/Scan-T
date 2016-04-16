#!/usr/bin/python
#coding:utf-8

from datetime import datetime
from elasticsearch import Elasticsearch
es=Elasticsearch()
es.indices.create(index='datap',ignore=400)
es.index(index='datap',doc_type='snifferdata',id=42,body={
		"any":"data", 
		"timestamp": datetime.now()

	})