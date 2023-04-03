from SubProgramGame import *

class MainProgramGame:
     
    def _init_(SubProgramGame) -> None:
        pass

    def play_game():
        quiz = SubProgramGame()
        quiz.play()
    
    def main_menu():
        while True:
            print("========QUIZ BRAND=======")
            print("1. Mulai quiz")
            print("2. Keluar")
            menu = input("Pilih menu (1/2): ")
            if menu == "1":
                MainProgramGame.play_game()
            elif menu == "2":
                print("Terima kasih telah bermain!")
                break
            else:
                print("Menu tidak tersedia!")
                continue

if _name_ == "_main_":
    MainProgramGame.main_menu()