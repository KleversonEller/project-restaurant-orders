import csv
import os.path


def read_csv(path_to_file):
    with open(path_to_file, 'r') as file:
        data = csv.reader(file)
        return list(data)


def get_working_days(orders):
    working_days = {order[2] for order in orders}
    return working_days


def get_menu(orders):
    menu = {order[1] for order in orders}
    return menu


def get_disher_by_client(orders, client):
    client_orders = [order for order in orders if order[0] == client]
    dishes = {}

    for order in client_orders:
        if order[1] not in dishes:
            dishes[order[1]] = 1
        else:
            dishes[order[1]] += 1

    return dishes


def get_days_by_client(orders, client):
    client_orders = [order for order in orders if order[0] == client]

    return {day[2] for day in client_orders}


def analyze_log(path_to_file):
    if not path_to_file.endswith("csv"):
        raise FileNotFoundError(f"Extensão inválida: '{path_to_file}'")
    if os.path.exists(path_to_file):
        orders = read_csv('data/orders_1.csv')
    else:
        raise FileNotFoundError(f"Arquivo inexistente: {path_to_file}")

    menu = get_menu(orders)
    working_days = get_working_days(orders)

    maria_dishes = get_disher_by_client(orders, 'maria')
    most_frequent_dish_by_client = max(maria_dishes, key=maria_dishes.get)

    arnaldo_dishes = get_disher_by_client(orders, 'arnaldo')

    joao_dishes = get_disher_by_client(orders, 'joao')
    not_ordered_dishes_by_joao = menu.difference(set(joao_dishes.keys()))

    joao_days = get_days_by_client(orders, 'joao')
    joao_ausent_days = working_days.difference(joao_days)

    with open('data/mkt_campaign.txt', 'w') as file:
        file.write(
            f'{most_frequent_dish_by_client}\n' +
            f'{arnaldo_dishes["hamburguer"]}\n' +
            f'{not_ordered_dishes_by_joao}\n' +
            f'{joao_ausent_days}'
        )
