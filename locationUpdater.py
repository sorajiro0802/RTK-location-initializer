import sys

def attention():
    print(
        """
        ※ 区切りはピリオドで入力してください
        入力例: 35.40.52.9746 (<= 35° 40′ 52.9746″)
        """
        )

def makeBack(file_path):
    with open(file_path, mode='r') as f:
        lines = f.read()
    backup_name = "backup_{}".format(file_path)
    with open(backup_name, mode='w') as f:
        f.write(lines)

def base60_to_decimal(base60_number):
    base60_parts = [int(num) for num in base60_number.split('.')]
    # check input number
    if len(base60_parts) != 4:
        raise ValueError
    degree = base60_parts[0]
    minute = base60_parts[1] / 60
    second = float("{}.{}".format(base60_parts[2], base60_parts[3])) / 60 / 60
    return round(degree + minute + second, 8)

def updateLLH(file_path, latitude, longitude, height):
    with open(file_path, mode='r') as f:
        lines = f.readlines()
    cnt = 0
    for line in lines:
        if "-p" in line:
            lines[cnt] = "-p {} {} {}".format(latitude, longitude, height)
        cnt += 1
    
    with open(file_path, mode='w') as f:
        f.writelines(lines)
    
def main():
    attention()
    system_arg = sys.argv
    file = system_arg[1]

    latitude = input("緯度を入力>> ")
    longitude = input("経度を入力>> ")
    dec_height = float(input("高さを入力>> "))
    
    dec_latitude = base60_to_decimal(latitude)
    dec_longitude = base60_to_decimal(longitude)
    
    makeBack(file)
    updateLLH(file, dec_latitude, dec_longitude, dec_height)
    print(f"-- update finished --")
    
if __name__=='__main__':
    main()
