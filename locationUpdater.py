import math

def makeBack(file_path):
    with open(file_path, mode='r') as f:
        lines = f.read()
    backup_name = f"backup_{file_path}"
    with open(backup_name, mode='w') as f:
        f.write(lines)
    
def main():
    pass

if __name__=='__main__':
    main()
