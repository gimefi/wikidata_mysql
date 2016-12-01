#-------------------------------------------------------------------------------
# Name:        index
# Purpose:
#
# Author:      zhx
#
# Created:     24/11/2016
# Copyright:   (c) zhx 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def creat_index_tb1(db,cursor):
    sql = "create index tb1_id \
            on table1(en)"
    try:
        cursor.execute(sql)
        print 'index add?'
        db.commit()
    except:
        print 'create index not success'
        db.rollback()
