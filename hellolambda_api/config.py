from pathlib import Path

FLASK_PORT = 5285
ROOT_API_AWS = 'https://xxx.execute-api.us-west-2.amazonaws.com/dev'
ROOT_API_FLASK = f'http://localhost:{FLASK_PORT}'
LOCAL_AWS_PROFILE = 'hellolambda'
AWS_REGION = 'us-west-2'
APP_NAME = 'hellolambda'
S3_SITE_BUCKET = 'hellolambda.yourcompany.com'
CORS_ACCEPTABLE_ORIGINS = ['http://hellolambda.xxx.com']
PRODUCTION_DOMAINS = ['hellolambda.com', 'www.hellolambda.com']

TEST_PATH_PREFIX = '/test'

ROOTP = Path(__file__).parent.parent
SITE_ASSETS_DIR = ROOTP / 'hellolambdaapi/assets'

EMAIL = {
    'notification_addr': 'test@gmail.com',
    'from_addr': 'test2@gmail.com',
    'feedback_subject': 'Hellolambda Form Content'
}

DYNAMO_TABLE_NAME = 'hellolambda'


# Event limiter
MAX_DYNAMO_PER_DAY = 2000
MAX_EMAIL_PER_DAY = 100

# Global - Ugly but easy, and easier than flask.g
is_debug_server = None

#
# This is so I can test my code while still having a clean config file for the boilerplate.
# You can delete it or ignore it.
#
try:
    from hellolambda_api._private_config import *
except ImportError:
    pass
