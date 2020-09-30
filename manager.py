import os
import sys
import messageModule as msg

def main():
    msg.initDataColector()
    os.system('python dataColector.py')

    msg.initDatabaseCreator()
    os.system('python databaseCreator.py ' + sys.argv[1])
    
    msg.finishExecution()

    
if __name__ == "__main__":
    main()