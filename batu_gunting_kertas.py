
import random

class BatuGuntingKertas:
    def __init__(self, nama):
        self.nama = nama
        self.skor_pemain = 0
        self.skor_komputer = 0

    def bermain(self):
        pilihan = ["batu", "gunting", "kertas"]

        for ronde in range(1, 4):
            pemain = input("Pilih batu/gunting/kertas: ").lower().strip()

            if pemain not in pilihan:
                print("pilihan tidak valid")
                continue

            komputer = random.choice(pilihan)

            if pemain == komputer:
                print("seri")
            elif (
                (pemain == "batu" and komputer == "gunting")
                or (pemain == "gunting" and komputer == "kertas")
                or (pemain == "kertas" and komputer == "batu")
            ):
                print("kamu menang")
                self.skor_pemain += 1
            else:
                print("kamu kalah")
                self.skor_komputer += 1

        if self.skor_pemain > self.skor_komputer:
            print("kamu menang")
        elif self.skor_pemain < self.skor_komputer:
            print("kamu kalah")
        else:
            print("seri")


game = BatuGuntingKertas("Player 1")
game.bermain()
