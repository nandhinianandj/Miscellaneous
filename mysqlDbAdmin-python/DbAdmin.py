## This is part of the wnframework project at google.
## http://code.google.com/p/wnframework/
##
##
import MySQLdb
class DbAdministrator(object):
	"""
    		Basically, a wrapper for oft-used mysql commands. like show tables,databases, variables etc...
    		#TODO:
		0.  Simplify / create settings for the restore database source folder
        	0a. Merge restore database and extract_sql(from webnotes_server_tools).
        	1. Setter and getter for different mysql variables.
        	2. Setter and getter for mysql variables at global level??
	"""

	def __init__(self,conn):
		if conn:
			self.conn = conn
		self.cursor = self.conn.cursor()

        def lock_table(self,table,lock_type):
            return self.cursor.execute("LOCK TABLES %S %S"%(table,lock_type))

        def unlock_tables(self):
            """
            Just stupid unlock tables
            """
            return self.cursor.execute("UNLOCK TABLES;")
	def get_variables(self,regex):
		"""
        Get variables that match the passed pattern regex
        """
		print ("SHOW VARIABLES LIKE '{0}{1}{2}';".format('%',regex,'%'))
		self.cursor.execute(("SHOW VARIABLES LIKE '{0}{1}{2}'".format('%',regex,'%')))
		return list(self.cursor.fetchall())

	#def drop_all_databases(self):
	#	self.db_list = self.get_database_list()
    #    for db in self.db_list:
    #    	self.drop_database(db)

	def use(self,db):
		"""Use the given db for all further operations."""
		self.cursor.execute("USE %s"%db)
		self.cursor.fetchall()

	def get_table_schema(self,table):
		"""Just returns the output of Desc tables."""
		self.cursor.execute("DESC %s"%table)
		return list(self.cursor.fetchall())


	def get_tables_list(self,target):
		""" """
		try:
			self.use(target)
			self.cursor.execute("SHOW TABLES")
			res = self.cursor.fetchall()
			if res:
				table_list = []
			for table in res:
				table_list.append(table[0])
			return table_list
		except Exception,e:
			raise e

	def create_user(self,user,password):
    	#Create user if it doesn't exist.
		try:
			print "Creating user %s" %user[:16]
			if password:
				self.cursor.execute("CREATE USER '%s'@'localhost' IDENTIFIED BY '%s';" % (user[:16], password))
			else:
				self.cursor.execute("CREATE USER '%s'@'localhost';"%user[:16])
		except Exception, e:
			raise e

	def delete_user(self,target):
        # delete user if exists
		try:
			print "Dropping user " ,target
			self.cursor.execute("DROP USER '%s'@'localhost';" % target)
		except Exception, e:
			if e.args[0]==1396:
				pass
			else:
				raise e

	def create_database(self,target):
		try:
			print "Creating Database", target
			self.cursor.execute("CREATE DATABASE IF NOT EXISTS `%s` ;" % target)
		except Exception,e:
			raise e

	def drop_database(self,target):
		try:
			print "Dropping Database:",target
			self.cursor.execute("DROP DATABASE IF EXISTS `%s`;"%target)
		except Exception,e:
			raise e

	def grant_all_privileges(self,target,user):
		try:
			print "Granting all privileges on %s to %s@localhost" %(target,user)
			self.cursor.execute("GRANT ALL PRIVILEGES ON `%s` . * TO '%s'@'localhost';" % (target, user))
		except Exception,e:
			raise e

	def grant_select_privilges(self,db,table,user):
		try:
			if table:
				print "Granting Read privileges on %s.%s to %s@localhost" %(db,table,user)
				self.cursor.execute("GRANT SELECT ON %s.%s to '%s'@'localhost';" % (db,table,user))
			else:
				print "Granting Read privileges on %s.* to %s@localhost" %(db,user)
				self.cursor.execute("GRANT SELECT ON %s.* to '%s'@'localhost';" % (db,user))
		except Exception,e:
			raise e

	def grant_privileges(self,privilege,db,table,user,host):
		try:
			print "Granting %s privilege on %s.%s to %s@%s"%(privilege,db,table,user,host)
			self.cursor.execute("GRANT %s ON %s.%s to '%s'@'%s';"%(privilege,db,table,user,host))
		except Exception,e:
			raise e

	def flush_privileges(self):
		try:
			print "Flushing privileges"
			self.cursor.execute("FLUSH PRIVILEGES")
		except Exception,e:
			raise e


	def get_database_list(self):
		try:
			db_list = []
			ret_db_list = self.cursor.execute("SHOW DATABASES")
			for db in ret_db_list:
				if db[0] not in ['information_schema', 'mysql', 'test', 'accounts']:
					db_list.append(db[0])
			return db_list
		except Exception,e:
			raise e

	def restore_database(self,target,source,root_password):
		try:
			ret = os.system("mysql -u root -p%s %s < %s"%(root_password,target,source))
			print "Restore DB Return status:",ret
		except Exception,e:
			raise e

	def drop_table(self,table_name):
		try:
			print "Dropping table %s" %(table_name)
			self.cursor.execute("DROP TABLE IF EXISTS %s "%(table_name))
		except Exception,e:
			raise e

	def set_transaction_isolation_level(self,scope='SESSION',level='READ COMMITTED'):
		#Sets the transaction isolation level. scope = global/session
		try:
			self.cursor.execute("SET %s TRANSACTION ISOLATION LEVEL %s"%(scope,level))
			print "Set transaction level ",scope, level
		except Exception,e:
			raise e

