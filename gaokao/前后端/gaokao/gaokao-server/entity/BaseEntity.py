from peewee import *

database = MySQLDatabase('gaokaos', **{'charset': 'utf8', 'sql_mode': 'PIPES_AS_CONCAT', 'use_unicode': True, 'host': '127.0.0.1', 'port': 3306, 'user': 'root', 'passwd': 'root'})

class BaseEntity(Model):
    class Meta:
        database = database