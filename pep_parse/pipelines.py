

class PepParsePipeline:
    
    def open_spider(self, spider):
        self.pep_types = {}
    
    def process_item(self, item, spider):
        current_status = item['status']
        self.pep_types[current_status] = self.pep_types.get(
                                            current_status, 0) + 1
        
