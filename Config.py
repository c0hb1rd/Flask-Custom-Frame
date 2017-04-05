from os import getcwd, path


ROOT_PATH = getcwd()
LOG_PATH = path.join(getcwd(), 'Log.txt')

DB = ""
DB_HOST = "127.0.0.1"
DB_USER = "root"
DB_PASSWORD = ""
DB_CHARSET = "utf8"

SEC_KEY = ''

GET = ['GET']
POST = ['POST']
GAP = GET + POST


SER_HOST = "0.0.0.0"
SER_PORT = 5000


DEBUG = True
THREADED = True
TEMPLATES_AUTO_RELOAD = True
SECRET_KEY = ""
CACHE_SIZE = 0
