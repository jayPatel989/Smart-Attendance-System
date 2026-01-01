import sys
import os

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(PROJECT_ROOT)

from database.db_utils import clear_attendance

clear_attendance()
print("Attendance database records deleted successfully!")