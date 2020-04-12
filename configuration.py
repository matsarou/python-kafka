# Database configuration
HOST = 'mtdataengineer.cg2t1fioak49.eu-west-3.rds.amazonaws.com'
USER = 'root'
PASSWORD = '6FUfYLHVeKdYTCQVCvnDkeRR'
DB = 'mtdataengineer'

# Kafka configuration
APP='classifieds_application'
KAFKA = f'kafka://15.188.172.135'
TOPIC= 'data'
PARTITIONS = 1

#Time interval in seconds
TIME_WINDOW=7.0

#: How often we commit acknowledged messages: every n messages.
#: Used as default value the 10_000
BROKER_COMMIT_EVERY = 1000

#: Where the consumer should start reading offsets when there is no initial
#: offset, or the stored offset no longer exists, e.g. when starting a new
#: consumer for the first time. Options include 'earliest', 'latest', 'none'.
#: The default value for :setting:`consumer_auto_offset_reset` is the earliest.
CONSUMER_AUTO_OFFSET_RESET = 'latest'

DT_START_FOR_MARGIN_BY_AD_TYPE = '2020-04-08T18:07:32.1688783Z'
DT_STOP_FOR_MARGIN_BY_AD_TYPE = '2020-04-09T00:57:32.5045605Z'

DT_START_FOR_MARGIN_BY_PAYM_TYPE = '2020-04-08T18:07:32.1688783Z'
DT_STOP_FOR_MARGIN_BY_PAYM_TYPE = '2020-04-09T00:57:32.5045605Z'

