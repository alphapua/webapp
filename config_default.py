#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Michael Liao'

'''
Default configurations.
'''
import sae.const
LOCAL = True

if not LOCAL:
    configs = {
        'db': {
            'host': sae.const.MYSQL_HOST,
            'port': int(sae.const.MYSQL_PORT),
            'user': sae.const.MYSQL_USER,
            'password': sae.const.MYSQL_PASS,
            'database': sae.const.MYSQL_DB
        },
       'session': {
            'secret': 'AwEsOmE'
        }
    }
else:
    configs = {
        'db': {
            'host': '127.0.0.1',
            'port': 3306,
            'user': 'root',
            'password': '',
            'database': 'app_alphapua'
        },
        'session': {
            'secret': 'AwEsOmE'
        }
    }
