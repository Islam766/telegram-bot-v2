#!/usr/bin/python
# -*- coding: utf8 -*-

import requests


def urls_citata():
    """Рандомные цитаты с http://fucking-great-advice.ru"""
    contents = requests.get('http://fucking-great-advice.ru/api/random'
                            ).json()  # Берем котеек
    url = contents['text']
    return url
