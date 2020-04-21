# examples/send_to_agent.py
import asyncio
from classifieds_application import record_classifieds
from model import Classified

async def send_value() -> None:
    print(await record_classifieds.ask(Classified(id='yui0', customer_id='8e',
                                                  created_at="2019-08-04T23=34=19.5934998Z",text="txt2", ad_type="Premium", price=6.8,
                                                  currency="EUR",payment_type="Card",payment_cost=0.2)))

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(send_value())