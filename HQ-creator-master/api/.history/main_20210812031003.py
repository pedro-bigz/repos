from App import App
import sys

def main():
    app = App(sys.argv[1], sys.argv)

    print(sys.argv)

def getDestinationPath():
    return sys.argv[1]

def getOriginPaths():
    return sys.argv[1:]
        
if __name__  == "__main__":
    main()
        