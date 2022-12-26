class InventoryControl:
    INGREDIENTS = {
        'hamburguer': ['pao', 'carne', 'queijo'],
        'pizza': ['massa', 'queijo', 'molho'],
        'misto-quente': ['pao', 'queijo', 'presunto'],
        'coxinha': ['massa', 'frango'],
    }
    MINIMUM_INVENTORY = {
        'pao': 50,
        'carne': 50,
        'queijo': 100,
        'molho': 50,
        'presunto': 50,
        'massa': 50,
        'frango': 50,
    }

    def __init__(self):
        self.ingredients_to_buy = {
            'pao': 0,
            'carne': 0,
            'queijo': 0,
            'molho': 0,
            'presunto': 0,
            'massa': 0,
            'frango': 0,
        }
        self.stock_control = {
            'pao': self.MINIMUM_INVENTORY['pao'],
            'carne': self.MINIMUM_INVENTORY['carne'],
            'queijo': self.MINIMUM_INVENTORY['queijo'],
            'molho': self.MINIMUM_INVENTORY['molho'],
            'presunto': self.MINIMUM_INVENTORY['presunto'],
            'massa': self.MINIMUM_INVENTORY['massa'],
            'frango': self.MINIMUM_INVENTORY['frango'],
        }

    def add_new_order(self, customer, order, day):
        for ing in self.INGREDIENTS[order]:
            self.ingredients_to_buy[ing] += 1
            self.stock_control[ing] -= 1
            if self.ingredients_to_buy[ing] > self.MINIMUM_INVENTORY[ing]:
                return False

    def get_quantities_to_buy(self):
        return self.ingredients_to_buy

    def get_available_dishes(self):
        missing_ingredients = {
            ing for ing in self.stock_control
            if self.stock_control[ing] < 1
        }

        available_dishes = set()
        for dish in self.INGREDIENTS:
            ingredients = set(self.INGREDIENTS[dish])
            if len(ingredients.intersection(missing_ingredients)) == 0:
                available_dishes.add(dish)

        return available_dishes
