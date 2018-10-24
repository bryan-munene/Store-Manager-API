sales = []
sale_items = []

class SalesModel():
    def __init__(self):
        self.sale_items = sale_items
        self.sales = sales
        self.sale_id = len(sales)
        
    def add_sale_items(self, item_id, name, quantity, price, total):
        self.sale_item_id = len(sale_items)+1
        self.sale_id = len(sales)+1
        
        sale_item = {
            "sale_item_id": self.sale_item_id,
            "sale_id": self.sale_id,
            "item_id": item_id,
            "item_name": name,
            "quantity": quantity,
            "price": price,
            "total": total
            }

        sale_items.append(sale_item)

        return sale_item

    def add_sales(self, payment_mode, grand, items):
        self.sale_id = len(sales)+1
        sale = {
            "sale_id": self.sale_id,
            "payment_mode": payment_mode,
            "grand_total": grand,
            "number_of_items": items
            }

        self.sales.append(sale)

        return sale


    def get_all_sales(self):
        return sales

    def get_all_sale_items(self):
        return sale_items

    def get_sale_items_by_sale_id(self, sale_id):
        same_sale = []
        if len(sale_items) > 0:
            for sale_item in sale_items:
                id = sale_item.get('sale_id')
                if id == sale_id:
                    same_sale.append(sale_item)
            return same_sale
        

    def get_sales_by_sale_id(self, sale_id):
        if len(sales) > 0:
            for sale in sales:
                id = sale.get('sale_id')
                if id == sale_id:
                    return sale
            

    