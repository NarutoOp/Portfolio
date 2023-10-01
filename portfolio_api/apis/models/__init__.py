# Folder structure:
#==================
# models/
#   __init__.py
#   products.py
#   stocks.py

# In init.py (don't forget the period before model file name)
#===========
from .GeeksModel import GeeksModel

__all__ = [
    'GeeksModel'
]

# And run "py manage.py makemigrations" and "py manage.py migrate" as normal