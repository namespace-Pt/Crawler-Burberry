def get_header(cookie=False):
    header = dict()
    with open('header.txt','r',encoding='utf-8') as f:
        for line in f:
            a,b = line.split(":",1)
            header[a.strip()] = b.strip()
    if not cookie:
        del header['cookie']
    return header

if __name__ == '__main__':
    print(get_header())