from formula import *

#the main file to run the whole program
def main():
    application = QApplication([])
    window = Controller()
    window.show()
    application.exec_()

if __name__ == "__main__":
    main()