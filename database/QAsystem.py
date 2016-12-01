#-------------------------------------------------------------------------
# Name:        Q&A system
# Purpose:
#
# Author:      zhx
#
# Created:     22/11/2016
# Copyright:   (c) zhx 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------


def name_to_entity(db, cursor, name):
    # Given a name, return all the entities that match the name.
    sql = "select id\
           from table1\
           where en_name = '%s'" % \
        (name)
    res = 'The entities that match the input name has IDs: '
    try:
        print '--- query starts ---'
        print sql
        print '--- query answer ---'
        cursor.execute(sql)
        result = cursor.fetchall()
        for row in result:
            print row[0]
            res+='|'+row[0]+'|'
        print '--- query   ends ---'
    except:
        print 'query not success'
        db.rollback()
    return res

def entity_precatry_subs(db,cursor,id):
    sql = "select instance_of,subclass_of\
           from table1\
           where id = '%s' " % \
        (id)
    res = 'The result of query 2:\n\n'
    try:
        print '--- query starts ---'
        print sql
        print '--- query answer ---'
        cursor.execute(sql)
        result = cursor.fetchall()
        for row in result:
            res +='preceding catary:\n '+'\tinstance of: '+row[0]+'\n\tsubclass of: '+row[1]+'\n'
        print '--- query   ends ---'
    except:
        print 'query not success'
        db.rollback()
    return res   


def entity_stmt_entity(db, cursor, id):
    # Given an entity, return all entities that are co-occurred with this
    # entity in one statement.
    sql = "select id,property\
           from table2\
           where property in \
           (select property\
		   from table2\
		   where id = '%s')" % \
        (id)
    res = 'The result of query 3:\n'
    try:
        print '--- query starts ---'
        print sql
        print '--- query answer ---'
        cursor.execute(sql)
        result = cursor.fetchall()
        for row in result:
            res +='entity'+row[0]+'has the same property:'+row[1]+'\n'
        print '--- query   ends ---'
    except:
        print 'query not success'
        db.rollback()
    return res


def entity_to_statements(db, cursor, id):
    # Given an entity, return all the properties and statements it possesses.
    res = 'The result of query 4:\n'
    sql = "select en_name,cn_name\
        from table1\
        where ID = '%s' " %\
        (id)
    try:
        cursor.execute(sql)
        result = cursor.fetchall()
        for row in result:
            res += 'Enlish: '+row[0]+'\nChinese: '+row[1]+'\n'
    except:
        db.rollback()

    sql = "select property, value, qualifier, reference \
            from table2 \
            where id = '%s' " % \
        (id)

    try:
        print '--- query starts ---'
        print sql
        print '--- query answer ---'
        cursor.execute(sql)
        result = cursor.fetchall()
        for row in result:
            res+= 'statement:\n'
            res+= ('\tproperty: '+row[0]+'\n\tvalue: '+row[1]+'\n\tqualifier: '+row[2]+'\n\treference: '+row[3]+'\n')
        print '--- query   ends ---'
    except:
        print 'query not success'
        db.rollback()
    return res

def what_is_A_of_B(db, cursor, q_property, q_name):
    sql = "select id\
           from table1\
           where en_name = '%s'" % \
        (q_name)
    res = ''
    try:
        cursor.execute(sql)
        result = cursor.fetchall()
        if (result == None):
            res += 'No entity match the name'
        else:
            res += 'This is the results of you query:\n'
            for row in result:
                q_id = row[0]
                print 'id =',q_id
                sql = "select value, qualifier, reference\
                        from table2\
                        where id = '%s' and property = '%s'" %\
                    (q_id, q_property)
                cursor.execute(sql)
                result2 = cursor.fetchall()
                if(result2 != None):
                    for row2 in result2:
                        q_value = row2[0]
                        q_qualifier = row2[1]
                        q_reference = row2[2]
                        print 'The', q_property, 'of', q_name, 'is "', q_value, q_qualifier, '" according to', q_reference
                        res += 'The "' + q_property + '" of "' + q_name + '" is "' + q_value + \
                            '" on the condition "' + q_qualifier + '" according to "' + q_reference + '" \n'
        return res

    except:
        print 'query not success'
        res += 'query not success'
        return res
        db.rollback()

def property_max_entity(db, cursor, property):
    # Given an entity, return all the properties and statements it possesses.
    sql = "select  max(value)\
            from table2 \
            group by property\
            having property = '%s'" % \
            (property)
            #where id = '%s' " % \
        #(id)
    res = 'The result of query 4:\n'
    try:
        print '--- query starts ---'
        print sql
        print '--- query answer ---'
        cursor.execute(sql)
        result = cursor.fetchall()
        if (result==None): res+= 'there is no property'+property
        for row in result:
            maxvalue = row[0]
            sql = "select ID\
                from table2\
                where property = '%s' and value = '%s'" %\
                (property,maxvalue)
            cursor.execute(sql)
            result2 = cursor.fetchall()
            for row2 in result2:
                res+='id: '+row2[0]+' has a maximum vlaue: '+maxvalue+'\n'
        print '--- query   ends ---'
    except:
        print 'query not success'
        db.rollback()
    return res
