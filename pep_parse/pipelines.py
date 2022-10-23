import csv
import datetime as dt

from scrapy.exceptions import DropItem

from .constants import BASE_DIR, DATETIME_FORMAT


class PepParsePipeline:

    def open_spider(self, spider):
        self.pep_types = {}

    def process_item(self, item, spider):
        try:
            current_status = item['status']
            self.pep_types[current_status] = self.pep_types.get(
                current_status, 0) + 1
            return item
        except Exception:
            raise DropItem

    def close_spider(self, spider):
        results_dir = BASE_DIR / 'results'
        results_dir.mkdir(exist_ok=True)
        now = dt.datetime.now()
        now_formatted = now.strftime(DATETIME_FORMAT)
        file_name = f'status_summary_{now_formatted}.csv'
        file_path = results_dir / file_name
        total = sum(self.pep_types.values())
        with open(file_path, 'w', encoding='utf-8') as f:
            writer = csv.writer(f, dialect='unix')
            f.write('Статус,Количество\n')
            writer.writerows(self.pep_types.items())
            f.write(f'Total,{total}\n')
