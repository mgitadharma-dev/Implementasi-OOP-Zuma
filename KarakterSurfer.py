
class KarakterSurfer:
    def __init__(self, nama):
        self.nama = nama
        self.skor = 0
        self.koin = 0
        self.is_running = True

    def berlari(self):
        self.is_running = True
        print(f"{self.nama} mulai berlari!")

    def ambil_koin(self, jumlah):
        if self.is_running:
            self.koin += jumlah
            self.skor += jumlah * 10
            print(f"{self.nama} berhasil mengambil {jumlah} koin!")
            print(f"Skor bertambah {jumlah * 10} poin.")
        else:
            print("Game over! Karakter tidak bisa mengambil koin.")

    def tabrak_rintangan(self):
        self.is_running = False
        print(f"{self.nama} menabrak rintangan!")
        print("GAME OVER!")

    def info_player(self):
        print("\n=== STATUS PLAYER ===")
        print(f"Nama       : {self.nama}")
        print(f"Skor       : {self.skor}")
        print(f"Koin       : {self.koin}")
        print(f"Sedang lari: {self.is_running}")


player1 = KarakterSurfer("Jake")

player1.info_player()

player1.berlari()

player1.ambil_koin(5)

player1.info_player()

player1.tabrak_rintangan()

player1.info_player()
