from collections import Counter


class TrackOrders:
    # aqui deve expor a quantidade de estoque
    def __init__(self):
        self.data = []

    def __len__(self):
        return len(self.data)

    def add_new_order(self, customer, order, day):
        self.data.append([customer, order, day])

    def get_menu(self):
        menu = {order[1] for order in self.data}
        return menu

    def get_dish_per_costumer(self, costumer):
        customer_orders = [
            order for order in self.data if order[0] == costumer]
        dishes = {}

        for order in customer_orders:
            if order[1] not in dishes:
                dishes[order[1]] = 1
            else:
                dishes[order[1]] += 1

        return dishes

    def get_working_days(self):
        days = [order[2] for order in self.data]
        return Counter(days)

    def get_most_ordered_dish_per_customer(self, customer):
        customer_dishes = self.get_dish_per_costumer(customer)
        return max(customer_dishes, key=customer_dishes.get)

    def get_never_ordered_per_customer(self, customer):
        customer_dishes = self.get_dish_per_costumer(customer)
        menu = self.get_menu()

        return menu.difference(set(customer_dishes.keys()))

    def get_days_never_visited_per_customer(self, customer):
        customer_orders = [
            order for order in self.data if order[0] == customer]
        customer_days = {day[2] for day in customer_orders}
        working_days = set(self.get_working_days())
        return working_days.difference(customer_days)

    def get_busiest_day(self):
        working_days = self.get_working_days()
        return max(working_days, key=working_days.get)

    def get_least_busy_day(self):
        working_days = self.get_working_days()
        return min(working_days, key=working_days.get)
