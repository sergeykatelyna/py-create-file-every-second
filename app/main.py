from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        cur_datetime = datetime.now()
        cur_datetime_str = cur_datetime.strftime("%Y-%m-%d %H:%M:%S")
        cur_hour = cur_datetime.hour
        cur_min = cur_datetime.minute
        cur_sec = cur_datetime.second
        file_name = f"app-{cur_hour}_{cur_min}_{cur_sec}.log"
        with open(file_name, "w") as f:
            f.write(cur_datetime_str)
        print(f"{cur_datetime_str} {file_name}")
        sleep(1)


if __name__ == "__main__":
    main()
