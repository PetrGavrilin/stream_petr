import subprocess

def main():
    
    import lite_ap.py as la

    api_for = vk.API(access_token=token)  # адрес токена вк

    la.main_for_all(api_for)
    
    return None



if __name__ == '__main__':
    main()
