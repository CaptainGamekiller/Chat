# Read the .txt file!
def read_file(filename):
    lines = []
    with open(filename, 'r', encoding = 'utf-8-sig') as f: # .txt檔常出現開頭有"\ufeff"，這時候就需要加"-sig"來消除，表示utf-8的另一個版本。
        for line in f:
            lines.append(line.strip())
    return lines

# This function add ": " between name and chat record.
# 此function 在人名與對話內容中間，新增 ":"符號。解法:設一個變量來儲存人名，到不是人名的那一行我們才裝入new清單
# 要清楚loop的步驟，當遇到人名，沒遇到人名，走到路線不一樣!
def convert(lines):
    new = []
    person = None # 如果遇到不是人名開頭的.txt檔，會crash，所以設為None，讓person有值
    for line in lines:
        if line == 'Calvin':
            person = 'Calvin'
            continue
        elif line == 'Tom':
            person = 'Tom'
            continue
        if person: # 跟上面搭配使用，表如果person有值，我們才執行下面指令
           new.append(person + ": " + line)
    return new

# Write to the output.txt file!
def write_file(filename, lines):
    with open(filename, 'w')as f:
        for line in lines: # 這行別忘了，一行一行拿出來
            f.write(line + '\n') # f 的 write功能
# Main function
def main():
    lines = read_file('chat.txt')
    lines = convert(lines)
    print(lines)
    write_file('output_chat.txt', lines)

main()


