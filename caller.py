class SubProgramGame:
    
    def __init__(self):
        self.skor = 0
        self.total_pertanyaan = 6
    
    # METHOD NON RETURN TYPE
    def play(self):
        print("Selamat datang di Game Quiz Fashion!")
        jawaban = input('Apakah kamu siap bermain? (ya/tidak): ')
        if jawaban.lower() == 'ya':
            self.pertanyaan("Darimana kah brand ternama Prada dibuat? ", "itali")
            self.pertanyaan("Pada umumnya, bahan utama yang digunakan pada brand sepatu Dr.Martens adalah? ", "kulit")
            self.pertanyaan("Merek sepatu apa yang membuat koleksi Chuck Taylor All-Stars? ", "converse")
            self.pertanyaan("Apa slogan terkenal dari merek olahraga Nike? ", "just do it")
            self.pertanyaan("Birkin bag merupakan koleksi terkenal dari brand? ", "hermes")
            self.pertanyaan("Angka berapa yang sering dikaitkan dengan jeans Levis? ", "501")
            mark = end_game(self.skor, self.total_pertanyaan)
            print("Skor kamu:", round(mark))
        else:
            print("Kembali lagi yaa!")

    # METHOD NON RETURN TYPE
    def pertanyaan(self, text: str, answer: str) -> None:
        jawaban = input(f"Pertanyaan: {text}")
        if jawaban.lower() == answer.lower():
            self.skor += 1
            print("Jawaban benar!")
        else:
            print("Jawaban salah :(")

# FUNCTION RETURN TYPE BERPARAMETER           
def end_game(skor: int, total_pertanyaan: int) -> float:
    print("Terima kasih telah memainkan quiz ini!")
    print("Kamu mendapatkan", skor, "pertanyaan yang benar!")
    mark = (skor/total_pertanyaan)*100
    return mark 
