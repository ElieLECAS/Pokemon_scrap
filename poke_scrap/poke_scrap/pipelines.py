# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class PokeScrapPipeline:
    def process_item(self, item, spider):

        adapter = ItemAdapter(item)

        lowercase_keys = ['categories', 'tags']
        for lowercase_key in lowercase_keys:
            value = adapter.get(lowercase_key)
            if isinstance(value, str):  # Check if the value is a string
                adapter[lowercase_key] = value.lower()
            elif isinstance(value, list):  # Check if the value is a list
                # Assuming you want to lowercase each element in the list
                adapter[lowercase_key] = [element.lower() for element in value]
            elif value is not None:
                # Handle other types as needed
                adapter[lowercase_key] = str(value).lower()

        floats = ["price", "weight"]
        for i in floats:
            value = adapter.get(i)
            adapter[i] = float(value)

        return item
