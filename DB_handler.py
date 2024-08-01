import psycopg2


#import docker
#client = docker.DockerClient()
#container = client.containers.get("wolverine_overflow-database-1")
#IP = container.attrs['NetworkSettings']['IPAddress']


def connect():
    DBconnection = psycopg2.connect("dbname='wolverine_overflow' host='database' user='username' password='password' port='5432'")
    DBcursor = DBconnection.cursor()
    return DBconnection, DBcursor

DBconnection, DBcursor = connect() # not good, should be in other file.




def check_if_exists(table, column, val):
    DBcursor.execute("""SELECT EXISTS(
        SELECT 1 FROM {} WHERE {} = '{}'
         LIMIT 1);""".format(table, column, val))
    return DBcursor.fetchone()[0]

def DBexec(query, vals):
    DBcursor.execute(query, vals)
    try:
        return DBcursor.fetchone()
    except:
        return None

def DBselect(table, column):
    DBcursor.execute("SELECT {} FROM {};".format(column,table))
    return DBcursor.fetchone()

def DBinsert(table, columns, vals):
    DBcursor.execute("""INSERT INTO {}({})
                     VALUES(%s);
                     """.format(table, columns), vals)

def DBnewtable(table_name):
    DBcursor.execute("CREATE TABLE {}();".format(table_name))


def DBdrop_column(table_name, column_name):
    DBcursor.execute("""ALTER TABLE {}
                     DROP COLUMN {};""".format(table_name, column_name))

def DBnewcolumn(table_name, column_name, type):
    DBcursor.execute("""ALTER TABLE {}
                     ADD {} {}""".format(table_name, column_name, type))

# TODO FIX THIS
def get_short_posts():
    DBcursor.execute("""
                     SELECT title, content, user, id
                     FROM 



""")

def get_comments(post):
    DBcursor.execute("""SELECT comments.content, commentuser
        FROM posts
        INNER JOIN comments ON comments.commentid = posts.postid;
""")




def update():
    DBconnection.commit()

def disconnect():
    DBcursor.close()
    DBconnection.close()


def create_default_table():
    DBcursor.execute("""
                     CREATE TABLE users (
                        username VARCHAR(31),
                        password VARCHAR(31),
                        mail VARCHAR(127),
                        id integer,
                        CONSTRAINT primaryk PRIMARY KEY (username)
                     );
                     """)
    DBconnection.commit()
def create_posts_table():
    DBcursor.execute("""
    CREATE TABLE posts(
        postid UUID,
        content TEXT,
        title TEXT,
        postuser VARCHAR(31),
        CONSTRAINT postidpkey PRIMARY KEY (postid)
    );
    """)
    DBconnection.commit()

def create_comments_table():
    DBcursor.execute("""
    CREATE TABLE comments(
        commentid UUID,
        content TEXT,
        commentuser VARCHAR(31),
                     
        CONSTRAINT postfkey
            FOREIGN KEY(commentid)
                REFERENCES posts(postid)
    );
                    """)
    DBconnection.commit()

def init_tables():
    print("shut up, bub!")
    create_comments_table()









#print(DBcursor.fetchall())
#DBconnection.commit()


#print(DBcursor.execute("SELECT * FROM thing"))

#DBcursor.execute("""INSERT INTO thing(thingcolumn, thingcolumn2)
#                 VALUES('hello', 'hello2');
#                 """)


#DBconnection = psycopg2.connect("dbname='new_testdb' user='dbuser' host='localhost' password='Bsmch@500K!'")


#DBcursor.execute("""UPDATE thing
#                 SET thingcolumn = 'hello';
#                 
#                 
#                 """)
