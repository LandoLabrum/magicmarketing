# import environ
# import os

# class ez_env(object):
#     def __init__(self, env):
#         BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#         print(f"BASE: {BASE_DIR}")
#         environ.Env.read_env(os.path.join(BASE_DIR, '.env'))
#         self.env = env

#     @property
#     def get(self):
#         return self





# # False if not in os.environ because of casting above
# DEBUG = env('DEBUG')

# # Raises Django's ImproperlyConfigured
# # exception if SECRET_KEY not in os.environ
# SECRET_KEY = env('SECRET_KEY')