from settings import Settings
from views import Views

def main():
    sett = Settings(4)
    sh = Views(sett)
    sh._start()

if __name__ == "__main__":
    main()

