import pandas as pd


def cleaner():
    try:
        pd.read_csv('wifi_passwords.csv').dropna(axis=0).to_csv('wifi_passwords.csv', index=False)
    except FileNotFoundError:
        print('File not found. Collect more passwords!')


def main():
    cleaner()
    input(" Press any button to continue...")


if __name__ == '__main__':
    main()
