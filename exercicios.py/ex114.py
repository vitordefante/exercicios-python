# código que verifica se uma URL é acessível

import requests


def url_checker(url):
    try:
        # Get Url
        get = requests.get(url)
        # if the request succeeds
        if get.status_code == 200:
            print(f"{url}\n\033[1;32mÉ acessível!")
        else:
            print(f"{url}\n\033[1;31mNao é acessível!\033[m")

    # Exception
    except requests.exceptions.RequestException as e:
        # print URL with Errs
        print(f"{url}\n\033[1;31mNao é acessível1!\033[m")


url_checker('https://facebook.com/')
