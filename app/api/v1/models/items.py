items = []

class ItemsModel():
    def __init__(self):
        self.items = items
        self.item_id = len(items)+1
        

    def add_item(self, name, price, image, quantity):
        item = {
            "item_id": self.item_id,
            "name": name,
            "price": price,
            "image": image,
            "quantity": quantity
            }
        self.items.append(item)

        return item

    def get_all(self):
        return self.items

    def get_by_id(self, item_id):
        if len(items) > 0:
            for item in items:
                id = item.get('item_id')
                if id == item_id:
                    return item
            else:
                return False

    def get_by_name_and_price(self, name, price):
        if len(items) > 0:
            for item in items:
                item_name = item.get('name')
                item_price = item.get('price')

                if name == item_name and price == item_price:
                    return item