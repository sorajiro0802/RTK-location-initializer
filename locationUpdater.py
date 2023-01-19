
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
    backup_name = f"backup_{file_path}"
    with open(backup_name, mode='w') as f:
        f.write(lines)
    
def main():
    pass
    attention()

if __name__=='__main__':
    main()
