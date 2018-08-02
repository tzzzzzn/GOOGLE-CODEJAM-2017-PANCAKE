def cat(filename,mode):
    f=open(filename,mode)
    if mode=='r':
    
        '''print(f.read())
        print()'''
    
        print(f.readline())
        f.seek(0)
        for x in f.readlines():
            print(x)
    else:
        f.write(input())
    f.close()
def main():
    cat(input("filename"),input("mode"))
    cat(input("filename"),input("mode"))
if __name__=="__main__":
    main()
