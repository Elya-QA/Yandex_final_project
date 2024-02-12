# Элеонора Жуматова, 13-я когорта — Дипломный проект. Инженер по тестированию плюс

import data
import sender_stand_request

def test_get_order_track():
        order_track = sender_stand_request.get_new_track_order()
        order_response = sender_stand_request.get_order_by_track(order_track)
        assert order_response.status_code == 200

