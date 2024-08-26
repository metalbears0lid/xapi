import databases
import sqlalchemy
from xapi.config import config

# metadata stores info about tables/columns
metadata = sqlalchemy.MetaData()

# define tables/columns
post_table = sqlalchemy.Table(
    'posts',
    metadata,
    sqlalchemy.Column('id', sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column('body', sqlalchemy.String)
)

comment_table = sqlalchemy.Table(
    'comments',
    metadata,
    sqlalchemy.Column('id', sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column('body', sqlalchemy.String),
    sqlalchemy.Column('post_id', sqlalchemy.ForeignKey('posts.id'), nullable=False)
)

# engine allows sqlalchemy to connect to our database
engine = sqlalchemy.create_engine(
    config.DATABASE_URL, connect_args={'check_same_thread': False}
)

# tells engine to use the metadata to create all the tables/columns that the metadata object stores
metadata.create_all(engine)
# uses the databases modules to get us the database object which we use to interact w/ the database
database = databases.Database(
    config.DATABASE_URL, force_rollback=config.DB_FORCE_ROLL_BACK
)
