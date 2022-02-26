import sqlite3,json, datetime

def getDTdelta(delta, CF=True, UTC=False):
  if UTC==True:
    now = datetime.datetime.utcnow()
  else:
    now = datetime.datetime.now(datetime.timezone.utc).astimezone()

  rDatetime =  now - datetime.timedelta(seconds=(delta * 60))
  # print(rDatetime)

  if CF==True:
    rDatetime = rDatetime.strftime("%Y-%m-%dT%H:%M:%SZ")
  else:
    rDatetime = rDatetime.strftime("%Y-%m-%d %H:%M:%S.%f")
    rDatetime = rDatetime[:-3]
    #print(rDateTime)
  return rDatetime


DB_NAME = "./robotscripts/rpa.db"




def get_database_connection():
    con = sqlite3.connect(DB_NAME)
    return con


def create_table():
    # """
    # Creates a table ready to accept our data.

    # write code that will execute the given sql statement
    # on the database
    # """

    create_table = """ CREATE TABLE users (robotfilename text, username text, password text, active boolean); """

    con = get_database_connection()
    con.execute(create_table)
    con.close()

def insert_table(robotfilename, username, password, active=False):

    # print(jsonlist)

    add_data_stmt = ' INSERT INTO users ( robotfilename, username , password, active) VALUES(?,?,?,?)'


    # print(add_data_stmt)
    # print(item['count'])

    con = get_database_connection()

    # print(item['IP'])

    con.execute(add_data_stmt, (robotfilename, username, password, active))
    con.commit()
    con.close()

def read_data_from_db():
    # """
    # Return data from database.
    # """

    sql_query = ''' SELECT * FROM users where active=false LIMIT 1; '''

    con = get_database_connection()
    cur = con.cursor()

    cur.execute(sql_query)
    results = cur.fetchall()

    cur.close()
    con.close()

    return results




def delete_id(id):
    # """
    # Delete selected data from database.

    # execute the given sql statement to remove
    # the extra data
    # """

    sql_query = ''' DELETE FROM cfblocklist WHERE (ID = ? ); '''

    con = get_database_connection()
    con.execute(sql_query, (id,))
    con.commit()
    con.close()


def delete_by_time(tdelta):
    # """
    # Delete selected data from database.

    # execute the given sql statement to remove
    # the extra data
    # """

    sql_query = ''' DELETE FROM cfblocklist WHERE (time < ? ); '''


    con = get_database_connection()
    con.execute(sql_query, (getDTdelta(tdelta),))
    con.commit()
    con.close()


# get_database_connection()
# print(read_data_from_db())
# insert_table("TTRPA.robot", "TTRPA", "hellosecret", False)
# print(read_data_from_db())
