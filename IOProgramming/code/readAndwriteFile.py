filename = "C:\\Users\\杨康\\Desktop\\learngit\\问题集.md"

# 打开文件

# 读文件
try:
    with open(filename, 'r', encoding='utf8', errors='ignore') as f:
        for line in f.readlines():
            print(line.strip())

    with open(filename, 'a', encoding='utf8') as file:
        file.write("\n i have modify this file")

except UnicodeDecodeError as e:
    print(f"open file failed: {e}")
