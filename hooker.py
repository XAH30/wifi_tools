import pandas as pd
import subprocess
import winwifi


def wifi_connector():
    try:
        df = pd.read_csv('wifi_passwords.csv')
    except FileNotFoundError:
        df = pd.DataFrame(columns=['WiFi_name', 'password'])
    all_web_we_have_pass = []
    name_of_web_and_pass = []
    for row in range(len(df)):
        name_of_web_and_pass.append(df.WiFi_name[row])
        name_of_web_and_pass.append(df.password[row])
        all_web_we_have_pass.append(name_of_web_and_pass)
        name_of_web_and_pass = []
    results_of_find_wifi = subprocess.check_output("netsh wlan show network").decode("CP866").replace("\r", "").split(
        '\n')[4:]
    ssids = []
    row = 0
    while row < len(results_of_find_wifi):
        if row % 5 == 0:
            ssids.append(results_of_find_wifi[row])
        row += 1
    need_web = []
    for elements in ssids:
        need_web.append(elements[8:].replace(' ', ''))
    need_web = list(filter(None, need_web))
    web_we_can_connect = []
    for elements in all_web_we_have_pass:
        for webs in need_web:
            if elements[0] in need_web and elements[1] is not None:
                web_we_can_connect.append(elements[0])
                break
    if len(web_we_can_connect) >= 1:
        print("We can connect to this webs:")
        for web_id in range(len(web_we_can_connect)):
            print(f'ID [{web_id + 1}]:\t\tname of web [{web_we_can_connect[web_id]}]')
        now_need_web = int(input(f'Enter ID of web you w@nt to connect(from 1 to {len(web_we_can_connect)}): '))
        while now_need_web < 1 or now_need_web > len(web_we_can_connect):
            print("-=-We can't find this web in DataBase. Enter correct ID of web-=-")
            now_need_web = int(input(f'Enter ID of web you w@nt to connect(from 1 to {len(web_we_can_connect)}): '))
            if 1 <= now_need_web <= len(web_we_can_connect):
                break
        for elements in all_web_we_have_pass:
            if elements[0] == web_we_can_connect[now_need_web - 1]:
                ssid = elements[0]
                passwd = elements[1]
                break
        winwifi.WinWiFi.connect(ssid=ssid, passwd=passwd, remember=True)
        print(f'Name of web you choose [ {ssid} ]: Password [ {passwd} ]')
    else:
        print(
            "Sorry, but we can't connect to WiFi web now...\nPlease collect more WiFi passwords or try again later!\n")


def logo():
    print("Program was made by MrD1man41g")
    print("""                                      \\\\\\\\                                       ////                                 
                                      |\\\\\\\\                                     ////|                                 
                                      ||\\\\\\\\             /=======\             ////||                                 
                                      |||\\\\\\\\          ///=======\\\\\          ////|||                                 
                                      ||||\\\\\\\\       ////         \\\\\\\\       ////||||                                 
                                      |||| \\\\\\\\     ////           \\\\\\\\     //// ||||                                 
                                      ||||  \\\\\\\\   ////             \\\\\\\\   ////  ||||                                 
                                     ╔═╗╔═╗╔═══╗╔═══╗─╔╗─╔═╗╔═╗╔═══╗╔═╗─╔╗╔╗─╔╗─╔╗─╔═══╗                                
                                     ║║╚╝║║║╔═╗║╚╗╔╗║╔╝║─║║╚╝║║║╔═╗║║║╚╗║║║║─║║╔╝║─║╔═╗║                                
                                     ║╔╗╔╗║║╚═╝║─║║║║╚╗║─║╔╗╔╗║║║─║║║╔╗╚╝║║╚═╝║╚╗║─║║─╚╝                                
                                     ║║║║║║║╔╗╔╝─║║║║─║║─║║║║║║║╚═╝║║║╚╗║║╚══╗║─║║─║║╔═╗                                
                                     ║║║║║║║║║╚╗╔╝╚╝║╔╝╚╗║║║║║║║╔═╗║║║─║║║───║║╔╝╚╗║╚╩═║                                
                                     ╚╝╚╝╚╝╚╝╚═╝╚═══╝╚══╝╚╝╚╝╚╝╚╝─╚╝╚╝─╚═╝───╚╝╚══╝╚═══╝                                
                                      |||| ////     \\\\\\\\             ////   \\\\\\\\ ||||                                 
                                      ||||////       \\\\\\\\           ////     \\\\\\\\||||                                 
                                        \\|//          \\\\\\\\         ////        \\\\|//                                  
                                                       \\\\\\\\       ////                                                  
                                                        \\\\\\\\     ////                                                   
                                                         \\\\\\\\   ////                                                    
                                                          \\\\\\===///                                                     
                                                           \\\===//                                                      """)

def main():
    wifi_connector()
    logo()
    input(" Press any button to continue...")


if __name__ == '__main__':
    main()
