import faust

from configuration import APP, KAFKA, PARTITIONS, TIME_WINDOW, TOPIC, BROKER_COMMIT_EVERY, CONSUMER_AUTO_OFFSET_RESET, \
    DT_START_FOR_MARGIN_BY_AD_TYPE, DT_STOP_FOR_MARGIN_BY_AD_TYPE, DT_START_FOR_MARGIN_BY_PAYM_TYPE, \
    DT_STOP_FOR_MARGIN_BY_PAYM_TYPE
from model import Classified, ClassifiedsTableModel

app = faust.App(APP, broker=KAFKA, topic_partitions=PARTITIONS,
                BROKER_COMMIT_EVERY = BROKER_COMMIT_EVERY,
                CONSUMER_AUTO_OFFSET_RESET=CONSUMER_AUTO_OFFSET_RESET)

classified_topic = app.topic(TOPIC, value_type=Classified)

model = ClassifiedsTableModel()

# Use async. I/O to perform other actions while processing the stream
@app.agent(classified_topic)
async def record_classifieds(stream):
    try:
        # get up to 15 events within a 30 second window:
        async for message in stream.group_by(Classified.ad_type).take(15, within=30.0):
            await model.start()
            await model.insert_classified(message)
    except faust.exceptions.ValueDecodeError as err:
        print("Oops!  Error {}".format(err))
        pass

from utils import execute_single_query
@app.timer(interval=TIME_WINDOW)
async def every_minute():
    print('WAKE UP')
    if (DT_START_FOR_MARGIN_BY_AD_TYPE and DT_STOP_FOR_MARGIN_BY_AD_TYPE):
        await execute_single_query("CALL margin_by_ad_type_procedure('" + DT_START_FOR_MARGIN_BY_AD_TYPE + "', '" + DT_STOP_FOR_MARGIN_BY_AD_TYPE + "');")
    if (DT_START_FOR_MARGIN_BY_PAYM_TYPE and DT_STOP_FOR_MARGIN_BY_PAYM_TYPE):
        await execute_single_query("CALL margin_by_payment_type_procedure('" + DT_START_FOR_MARGIN_BY_PAYM_TYPE + "', '" + DT_STOP_FOR_MARGIN_BY_PAYM_TYPE + "');")

if __name__ == '__main__':
 app.main()