import vk  # импорт специализированной библиотеки для парсинга текста
import lite_ap


def main():
    
    try:
        api_for = vk.API(access_token=token)  # адрес токена вк
    except:  
        api_for = None

    lite_ap.main_for_all(api_for)
    
    return None

if __name__ == '__main__':
    main()
