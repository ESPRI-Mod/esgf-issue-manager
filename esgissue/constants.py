import os

# JSON issue schemas full path
JSON_SCHEMA_PATHS = {'create': '{0}/templates/create.json'.format(os.path.dirname(os.path.abspath(__file__))),
                     'update': '{0}/templates/update.json'.format(os.path.dirname(os.path.abspath(__file__))),
                     'close': '{0}/templates/close.json'.format(os.path.dirname(os.path.abspath(__file__))),
                     'retrieve': '{0}/templates/retrieve.json'.format(os.path.dirname(os.path.abspath(__file__)))}

# JSON FIELDS

UID = 'uid'
DATE_CREATED = 'dateCreated'
DATE_UPDATED = 'dateUpdated'
DATE_CLOSED = 'dateClosed'
DATASETS = 'datasets'
URL = 'url'
URLS = 'urls'
MATERIALS = 'materials'
ISSUES = 'issues'
ISSUE = 'issue'
STATUS = 'status'
STATUS_NEW = 'new'
STATUS_ONHOLD = 'onhold'
STATUS_WONTFIX = 'wontfix'
STATUS_RESOLVED = 'resolved'
PROJECT = 'project'

# ACTIONS

CREATE = 'create'
UPDATE = 'update'
CLOSE = 'close'
RETRIEVE = 'retrieve'
RETRIEVE_ALL = 'retrieve_all'
ACTIONS = [CREATE, UPDATE, CLOSE, RETRIEVE, RETRIEVE_ALL]


# PATH CONSTANTS
ISSUE_1 = 'issue_'
ISSUE_2 = '.json'
DSET_1 = 'dset_'
DSET_2 = '.txt'

# WebService

WEBSERVICE = 'WebService'
# URL_BASE = 'url_base'
HEADERS = {'Content-type': 'application/json', 'Accept': 'text/plain'}

# URL options
URLS = {
        'URL_BASE': 'http://localhost:5001',
        'CREATE': '/1/issue/create',
        'UPDATE': '/1/issue/update',
        'CLOSE': '/1/issue/close?uid=',
        'RETRIEVE': '/1/issue/retrieve?uid=',
        'RETRIEVE_ALL': '/1/issue/retrieve-all'
        }
# Regex

REGEX = 'Regex'

# CMIP5 REGEX
CMIP5_REGEX = '([a-zA-Z0-9]*)\.([a-zA-Z0-9]*)\.([a-zA-Z]*)\.([a-zA-Z0-9-]*)\.([a-zA-Z0-9]*)\.([a-zA-Z0-9]*)\.' \
              '([a-zA-Z]*)\.([a-zA-Z]*)\.(r\d*i\d*p\d*)((v|#)\d*)'
CMIP5_POS = {'project': 1, 'institute': 3, 'models': 4, 'experiments': 5, 'variables': 8}

REGEX_OPTIONS = {'cmip5': [CMIP5_REGEX, CMIP5_POS]}


# JSON FILE ORDER

INDEX_DICT = {1: 'uid', 2: 'title', 3: 'description', 4: 'institute', 5: 'project', 6: 'dateCreated', 7: 'dateUpdated',
              8: 'dateClosed', 9: 'models', 10: 'variables', 11: 'materials', 12: 'severity', 13: 'status', 14: 'url'}


# ERROR DICTIONARY
ERROR_DIC = {'title': [1, 'Title field missing or invalid.'], 'description': [2, 'Description field missing or invalid.'],
             'datasets': [3, 'Datasets are missing or invalid.'], 'severity': [4, 'Issue severity missing or invalid.'],
             'project': [5, 'Project field missing or invalid.'], 'models': [6, 'Models are missing or invalid.'],
             'status': [7, 'Status field missing or invalid.'], 'institute': [8, 'Institute field missing or invalid.'],
             'materials': [9, 'Materials field missing or invalid.'], 'urls': [10, 'URLs are missing or invalid.'],
             'id': [11, 'ID missing or invalid.'], 'uid': [11, 'UID missing or invalid.'],
             'datecreated': [12, 'Creation date missing or invalid.'],
             'dateupdated': [13, 'Update date missing or invalid.'],
             'dateclosed': [14, 'Closed date missing or invalid.'],
             'dataset_incoherent': [15, 'Incoherent dataset id with declared project DRS structure, '
                                        'please make sure both are coherent.'],
             'authentication': [17, 'Authentication failed. Make sure the credentials are correct.'],
             'authorization': [18, 'User lacks required privilege. Contact admins for further information.'],
             'connection_error': [19, 'Connection failed, server probably down. Contact admins.'],
             'connection_timeout': [20, 'Connection timed out, try again later.'],
             'multiple_ids': [21, 'Multiple issue ids were provided along with a single file destination, aborting.'],
             'validation_failed': [22, 'Json file validation failed for an unknown reason, please check said file.'],
             'unknown_command': [23, 'Command is unknown, check the documentation or help for further information'],
             'ws_request_failed': [24, 'WS request failed for unknown reason.'],
             'single_entry_field': [25, 'Field only supports single input per issue declaration.'],
             'unknown_error': [99, 'An unknown error has been detected. Please provide the admins with the error stack.'],
             }
# Authentication and authorization

ORGS_IDS = [23123271]

#
