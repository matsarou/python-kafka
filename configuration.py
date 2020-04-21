# Database configuration
HOST = '127.0.0.1'
USER = 'root'
PASSWORD = 'M@rouli2'
DB = 'xedb'

# Kafka configuration
APP='classifieds_application'
KAFKA = f'kafka://localhost:9092'
TOPIC= 'data'
PARTITIONS = 1

#: How often we commit acknowledged messages: every n messages.
#: Used as default value the 10_000
BROKER_COMMIT_EVERY = 1000

#: Where the consumer should start reading offsets when there is no initial
#: offset, or the stored offset no longer exists, e.g. when starting a new
#: consumer for the first time. Options include 'earliest', 'latest', 'none'.
#: The default value for :setting:`consumer_auto_offset_reset` is the earliest.
CONSUMER_AUTO_OFFSET_RESET = 'latest'

#Time interval in seconds
TIME_WINDOW=60.0
# Parameters for stored procedure that calculates the margin by ad_type every {TIME_WINDOW} seconds
DT_START_FOR_MARGIN_BY_AD_TYPE = '2020-04-08T18:07:32.1688783Z'
DT_STOP_FOR_MARGIN_BY_AD_TYPE = '2020-04-09T00:57:32.5045605Z'
# Parameters for stored procedure that calculates the margin by payment_type every {TIME_WINDOW} seconds
DT_START_FOR_MARGIN_BY_PAYM_TYPE = '2020-04-08T18:07:32.1688783Z'
DT_STOP_FOR_MARGIN_BY_PAYM_TYPE = '2020-04-09T00:57:32.5045605Z'

