from os import getenv

settings = {
    'aws': {
        'access_key_id': getenv('AWS_ACCESS_KEY_ID'),
        'access_key_secret': getenv('AWS_SECRET_ACCESS_KEY'),
        'region': getenv('AWS_REGION')
    },
    'blob': {
        's3': {
            'endpoint': getenv('AWS_S3_ENDPOINT')
        }
    },
    'environment': getenv('ENVIRONMENT', 'development'),
    'sql': {
        'data_warehouse': {
            'connection_string': getenv('SAINT_ANALYTICS_DB_CONNECTION_STRING'),
            'saint_martyred_fact_table_name': getenv('SAINT_ANALYTICS_DB_SAINT_MARTYRED_FACT_TABLE_NAME')
        }
    },
}
