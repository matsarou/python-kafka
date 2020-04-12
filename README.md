# Faust
Faust is a stream processing library, porting the ideas from Kafka Streams to Python.
It is used to build high performance distributed systems and real-time data pipelines that process billions of events every day.

## Faust worker
A Faust worker runs an application defined with the name "classifieds_application".
The Faust worker instance starts a Kafka consumer responsible for fetching messages from the subscribed topic "data".
The Kafka consumer commits the topic offsets, by default, every three seconds in a background task.
The configuration property "BROKER_COMMIT_EVERY" is overriden so that the consumer commits the new value of the topic offset every 1000 acknowledged messages.
The configuration property "CONSUMER_AUTO_OFFSET_RESET" is overriden with the value 'latest', so that the consumer shall start reading from
the latest existing offset, in case the application is restarted.

## Faust Agent
The Kafka consumer forwards the events to an agent that subscribes their interest to the "data" topic.
The agent gathers up to 15 events within a 30 second window, before it starts processing them. The messages are processed in batches of batch_size=15, for better performance.
The processing of the events includes the storing of the mapped Classified entries to the mysql "mtdataengineer" database.
The mapping of the received events to Classified objects is automatically performed with json deserialization.
The stream is partitioned based on the field ad_type of the message. The events with the same ad_type will go to the same partition.
I take advantage of the "upsert" functionality to avoid the duplicate messages. Duplicate messages are those that have the same id.
Mysql allows update or insert of rows into a table via the ON DUPLICATE KEY UPDATE clause of the INSERT statement.

## Open a Mysql client and connect to the mtdataengineer database with the command:
*mysql -u root -p mtdataengineer -h mtdataengineer.cg2t1fioak49.eu-west-3.rds.amazonaws.com*

## Execute the initial script "sql/initial_script.sql" in the Mysql client
Creates the tables Classifieds(with the classified records) and Margin_info(with the margins by ad_type and payment_type)

## Launch the application and start consuming the messages
One worker starts in the foreground by executing the command:
*faust -A classifieds_application worker -l info*

#### Check if the relevant Classified records exist in the database
In the mysql client, run select * from Classifieds;

## Run the Stored function "margin_func"
The stored function is responsible for calculating the margin of a single Classified record. It is used both by the sql script and the stored procedures.
Run the content of the file "sql/find_margin_stored_function.sql" in the Mysql client.

## Get the calculated value of margins, in a regular SQL script
The margins are calculated per ad_type and payment_type. The script can be found in the file "sql/find_margin_regular_script.sql".
The start and end datetime are not configurable, thus they must be hard coded.
The script uses the stored function "margin_func" and runs in the Mysql client.

## Run the stored procedures "margin_by_ad_type_procedure" and "margin_by_payment_type_procedure"
Run the content of the files "sql/find_margin_by_adtype_procedure.sql" and "sql/find_margin_by_paymenttype_procedure.sql" in the Mysql client.
There is a periodic timer that triggers them in hourly basis.The size of the time interval is configurable and it can change.
The start and end datetime are also configurable.

#### Check if the margins have been stored 
In the mysql client, run select * from Margin_info;

## BEST TO HAVE
* Create database scripts that can update the configuration properties at the runtime.
* Save the margins in two distributed tables for fast recovery and fault tolerance
* Add unit tests with pytest
* Still did not manage to make the worker run in an infinite loop.


