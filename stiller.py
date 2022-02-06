import subprocess
import pandas as pd
import time


def extract_wifi_passwords():
    array_for_now_web = []
    all_web_array = []
    try:
        df = pd.read_csv('wifi_passwords.csv')
    except FileNotFoundError:
        df = pd.DataFrame(columns=['WiFi_name', 'password'])
    profiles_data = subprocess.check_output('netsh wlan show profiles').decode('CP866').split('\n')
    profiles = [i.split(':')[1].strip() for i in profiles_data if 'Все профили пользователей ' in i]
    for profile in profiles:
        profile_info = subprocess.check_output(f'netsh wlan show profile {profile} key=clear').decode('CP866').\
            split('\n')
        try:
            password = [i.split(':')[1].strip() for i in profile_info if 'Содержимое ключа' in i][0]
        except IndexError:
            password = None
        for web_we_had in range(len(df)):
            array_for_now_web.append(df.WiFi_name[web_we_had])
            array_for_now_web.append(df.password[web_we_had])
            all_web_array.append(array_for_now_web)
            array_for_now_web = []
        if [profile, password] in all_web_array:
            pass
        elif [profile, password] in all_web_array and password is not None:
            df.set_index('WiFi_name')
            df.drop([profile], axis=0)
            df.loc[len(df.index)] = [profile, password]
        elif [profile, password] in all_web_array and password is None:
            pass
        else:
            df.loc[len(df.index)] = [profile, password]
        df.to_csv('wifi_passwords.csv', index=False)
        with open('wifi_passwords.txt', mode='a', encoding='utf-8') as file:
            file.write(f'Profile: {profile}\nPassword: {password}\n{"-" * 20}\n')


def main():
    extract_wifi_passwords()
    time.sleep(2)

if __name__ == '__main__':
    main()
