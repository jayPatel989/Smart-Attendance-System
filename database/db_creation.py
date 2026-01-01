import sys
import os

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(PROJECT_ROOT)

from database.db_utils import init_database, init_admin_table
from auth.auth_utils import create_admin

init_database()
init_admin_table()

create_admin("admin", "adminisgood")

print("Database Created!")