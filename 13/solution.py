def solve(file_path, res=[]):
    with open('input','r') as f:
        for line in f:
            res.append(int(line.replace('\n','')))

    return str(sum(res))[0:10]
            
def main():
    print solve('input')

if __name__ == '__main__':
    main()