import os
import time
import schedule
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from ext_register import CrawlGuaHao
from combination import Combination
from local_to_remote import Transfer
from start import run

crawl = CrawlGuaHao()
combine = Combination()
transfer = Transfer()

schedule.every().day.at("17:00").do(crawl.main)
schedule.every().day.at("18:10").do(combine.save_to_mongo)
schedule.every().day.at("18:30").do(transfer.transfer_data)
schedule.every().sunday.at("08:00").do(run)

while True:
    schedule.run_pending()
    time.sleep(60)
