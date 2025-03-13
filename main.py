import sys
from dotenv import load_dotenv
from get_series_info import get_series_info
from dotenv import load_dotenv

load_dotenv()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <serie_name>")
        print('Example: python3 main.py "The Sopranos"')
        return

    series_name = sys.argv[1]
    info = get_series_info(series_name)
    print(info)

if __name__ == "__main__":
    main()