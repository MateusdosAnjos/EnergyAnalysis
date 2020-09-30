import os
import sys
import messageModule as msg

def main():
    msg.initDataColector()
    os.system('python dataColector.py')

    msg.initDatabaseCreator()
    os.system('python databaseCreator.py ' + sys.argv[1])
    
    msg.initQueries()
    if len(sys.argv) > 2:
        os.system('python queryExec.py '  + sys.argv[2])
    else:
        os.system('python queryExec.py')

    msg.finishExecution()


if __name__ == "__main__":
    main()