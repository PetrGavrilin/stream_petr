import subprocess

def main():
    
    import lite_ap.py

    api_for = vk.API(access_token=token)  # адрес токена вк

    lite_ap.main_for_all(api_for)
    
    return None



if __name__ == '__main__':
    main()
