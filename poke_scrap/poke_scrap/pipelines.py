# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
# Corrected pipelines.py
import sqlite3

class PokeScrapPipeline:

    def __init__(self, db_path):
        self.db_path = db_path

    @classmethod
    def from_crawler(cls, crawler):
        settings = crawler.settings
        db_path = settings.get('DB_PATH', 'default.db')  # Default to 'default.db' if not provided
        return cls(db_path)

    def open_spider(self, spider):
        self.conn = sqlite3.connect(self.db_path)
        self.cursor = self.conn.cursor()

    def close_spider(self, spider):
        self.conn.close()

    def process_item(self, item, spider):
        # Assuming you have a table named 'products'
        self.cursor.execute("""
            INSERT INTO products (name, price, description, stock, sku, categories, tags, weight, height, length, width)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            item['name'],
            item['price'],
            item['description'],
            item['stock'],
            item['sku'],
            ', '.join(item['categories']),
            ', '.join(item['tags']),
            item['weight'],
            item['height'],
            item['length'],
            item['width']
        ))
        self.conn.commit()
        return item


# class PokeScrapPipeline:
#     def process_item(self, item, spider):

#         adapter = ItemAdapter(item)

#         lowercase_keys = ['categories', 'tags']
#         for lowercase_key in lowercase_keys:
#             value = adapter.get(lowercase_key)
#             if isinstance(value, str):  # Check if the value is a string
#                 adapter[lowercase_key] = value.lower()
#             elif isinstance(value, list):  # Check if the value is a list
#                 # Assuming you want to lowercase each element in the list
#                 adapter[lowercase_key] = [element.lower() for element in value]
#             elif value is not None:
#                 # Handle other types as needed
#                 adapter[lowercase_key] = str(value).lower()

#         floats = ["price", "weight"]
#         for i in floats:
#             value = adapter.get(i)
#             adapter[i] = float(value)

#         return item

# class SaveToSQLitePipeline:

#     def __init__(self):
#         self.conn = sqlite3.connect(
#             host = "localhost",
#             user = 'root',
#             password = '',
#             database = 'books'
#         )

#         self.cur = self.conn.cursor()

#         self.cur.execute("""
#         CREATE TABLE IF NOT EXISTS pokemon(
#             id int NOT NULL auto_increment,
#             name text,
#             price DECIMAL,
#             description text,
#             stock INTEGER,
#             sku INTEGER,
#             categories text,
#             tags text,
#             weight DECIMAL,
#             height INTEGER,
#             length INTEGER,
#             width INTEGER
#         )
# """)
    
#     def process_item(self,item,spider):
#         self.cur.execute(""" insert into pokemon()
#             name,
#             price,
#             description,
#             stock,
#             sku,
#             categories,
#             tags,
#             weight,
#             height,
#             length,
#             width
#             ) values (
#                 ?,
#                 ?,
#                 ?,
#                 ?,
#                 ?,
#                 ?,
#                 ?,
#                 ?,        
#                 ?,
#                 ?,
#                 ?
#             )""", (
#         item["name"],
#         item["price"],
#         item["description"],
#         item["stock"],
#         item["sku"],
#         item["categories"],
#         item["tags"],
#         item["weight"],
#         item["height"],
#         item["length"],
#         item["width"]
#             )
#             )
        
#         self.conn.commit()
#         return item
    
#     def close_spider(self, spider):
#         self.cur.close()
#         self.conn.close()