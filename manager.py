
from typing import Any, Dict

from pydantic.types import PositiveInt

import json

from tinydb import TinyDB
from tinydb.table import Document


class Manager:
    def __init__(self, item_type: Any) -> None:
        self.max_id = 0
        self.collection: Dict[PositiveInt, Any] = {}
        self.item_type: Any = item_type
        db = TinyDB("db.json", sort_keys=True, indent=4)
        self.table = db.table(item_type.__name__.lower() + "s")
        for item in self.table:
            self.create(**item)

    def find_all(self):
        return list(self.collection.values())

    def find_by_id(self, id: PositiveInt):
        return self.collection[id]

    def save_item(self, id):
        item = self.find_by_id(id)
        self.table.upsert(Document(json.loads(item.json()), doc_id=id))

    def create(self, *args, save: bool = False, **kwargs):
        if "id" not in kwargs:
            kwargs["id"] = self.max_id + 1
        item = self.item_type(*args, **kwargs)
        self.collection[item.id] = item
        self.max_id = max(self.max_id, item.id)
        if save:
            self.save_item(item.id)
        return item
