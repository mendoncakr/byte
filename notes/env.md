wSetting environment varibales in a django application:

getenv: https://pypi.python.org/pypi/django-getenv
dotenv: https://github.com/jpadilla/django-dotenv


in manage.py

include these:
import dotenv
dotenv.read_dotenv()

create your .env in your root and add to gitingore


EX:
in manage.py
print("DB_HOST={}".format(getenv.env('DB_HOST')) )

in .env

DB_HOST=FOO_BAR