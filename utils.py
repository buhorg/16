from config import db, app
import json
from flask import request


def insert_data_to_model(Model, data_list):
    """
    Вставляем данный из списка в любую из 3-х моделей
    """
    for item in data_list:
        db.session.add(Model(**item))
    db.session.commit()


def all_data_to_show(query):
    """
    Переводим в список словарей строки таблицы
    """
    response_list = []
    for item in query:
        response_list.append(item.data_to_dict())
    return app.response_class(json.dumps(response_list, ensure_ascii=False, indent=4), status=200,
                              mimetype="application/json")


def universal_all_data_handler(Model):
    """
    Универсальный обработчик данных для любой из 3х моделей
    Отрабатываем методы
    GET (для всех записей), POST
    """
    if request.method == 'GET':
        return all_data_to_show(Model.query.all())
    elif request.method == 'POST':
        if isinstance(request.json, list):

            insert_data_to_model(Model, request.json)
        elif isinstance(request.json, dict):
            insert_data_to_model(Model, [request.json])
        else:
            return "Нет данных в формате json для вставки"
        return app.response_class(json.dumps(request.json, ensure_ascii=False, indent=4),
                                  status=200, mimetype="application/json")


def universal_data_handler(Model, uid, values):
    """
    Универсальный обработчик данных для любой из 3х моделей
    Отрабатываем методы
    GET (для конкретной по id), PUT, DELETE
    """
    if request.method == 'GET':
        try:
            return app.response_class(json.dumps(Model.query.get(uid).data_to_dict(), ensure_ascii=False, indent=4),
                                      status=200, mimetype="application/json")
        except Exception as e:
            print(e)
            return {}
    if request.method == 'PUT':
        try:
            db.session.query(Model).filter(Model.id == uid).update(values)
            db.session.commit()
            return app.response_class(json.dumps("Данные успешно обновились", ensure_ascii=False, indent=4),
                                      status=200, mimetype="application/json")
        except Exception as e:
            print(e)
            return {}
    if request.method == 'DELETE':
        try:
            db.session.query(Model).filter(Model.id == uid).delete()
            db.session.commit()
            return app.response_class(json.dumps("Данные успешно удалились", ensure_ascii=False, indent=4),
                                      status=200, mimetype="application/json")
        except Exception as e:
            print(e)
            return {}
