import subprocess

def main():

    subprocess.call("lite_ap.py", shell=True)

    api_for = vk.API(access_token=os.getenv('TOKEN'))  # адрес токена вк

    main_for_all(api_for)



if __name__ == '__main__':
    main()
