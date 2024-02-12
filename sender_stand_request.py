import configuration
import requests
import data

# Запрос на создание заказа
def post_new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
                         json = body,
                         headers = data.header)


def get_new_track_order():
    order_response = post_new_order(data.order_body)
    return order_response.json()["track"]




def get_order_by_track(track):
    return requests.get(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH + f"?t={track}")