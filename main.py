from SubProgramGame import *

class MainProgramGame:

    def play_game():
        quiz = SubProgramGame()
        quiz.play()
    
    # FUNCTION RETURN TYPE TIDAK BERPARAMETER
    def opsi_game() -> None:
            print("========QUIZ FASHION=======")
            print("1. Mulai quiz")
            print("2. Keluar")

    def main_menu():
        while True:
            menu = input("Pilih menu (1/2): ")
            if menu == "1":
                MainProgramGame.play_game()
            elif menu == "2":
                print("Terima kasih telah bermain!")
                break
            else:
                print("Menu tidak tersedia!")
                continue
    
if __name__ == '__main__':
    MainProgramGame.opsi_game()
    MainProgramGame.main_menu()
