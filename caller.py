class SubProgramGame:
    
    def _init_(self):
        self.score = 0
        self.total_questions = 6
    
    def play(self):
        print("Selamat datang di Game Tebak Brand!")
        jawaban = input('Apakah kamu siap bermain? (ya/tidak): ')
        if jawaban.lower() == 'ya':
            self.question("Darimana kah brand ternama Prada dibuat? ", "itali")
            self.question("Pada umumnya, bahan utama yang digunakan pada brand sepatu Dr.Martens adalah? ", "kulit")
            self.question("Merek sepatu apa yang membuat koleksi Chuck Taylor All-Stars? ", "converse")
            self.question("Apa slogan terkenal dari merek olahraga Nike? ", "just do it")
            self.question("Birkin bag merupakan koleksi terkenal dari brand? ", "hermes")
            self.question("Angka berapa yang sering dikaitkan dengan jeans Levis? ", "501")
            self.end_game()
        else:
            print("Kembali lagi yaa!")
    
    def question(self, text, answer):
        jawaban = input(f"Pertanyaan: {text}")
        if jawaban.lower() == answer.lower():
            self.score += 1
            print("Jawaban benar!")
        else:
            print("Jawaban salah :(")
            
    def end_game(self):
        print("Terima kasih telah memainkan quiz ini!")
        print("Kamu mendapatkan", self.score, "pertanyaan yang benar!")
        mark = (self.score/self.total_questions)*100
        print("Score kamu:", mark)
