import MySQLdb
host = 'localhost'
mysql_user = 'root'
mysql_password = 'route'


target = 'emotionML'

import unittest

conn = MySQLdb.connect(host,mysql_user,mysql_password)
from DbAdmin import DbAdministrator

dba = DbAdministrator(conn)
class test_DbAdmin(unittest.TestCase):
	def test_get_variables(self):
		assert dba.get_variables("log")
	

	def test_set_variables(self):
		pass
	def test_drop_user(self):
		pass
	def test_drop_database(self):
		pass
	def test_drop_table(self):
		pass

	def test_get_tables_list(self):
		dba.get_tables_list(target)

