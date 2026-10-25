
class KatakZuma:
    def __init__(self, warna_awal):
        self.warna_peluru = warna_awal
        self.skor = 0
        self.is_active = True

    def ganti_warna(self, warna_baru):
        self.warna_peluru = warna_baru

    def tembak(self):
        if self.is_active:
            self.skor += 50
            print(f"Katak menembakkan bola {self.warna_peluru}!")
            print("Skor bertambah 50 poin.")
        else:
            print("Katak tidak aktif!")

    def info_status(self):
        print("STATUS KATAK ZUMA")
        print(f"Warna peluru : {self.warna_peluru}")
        print(f"Skor         : {self.skor}")
        print(f"Aktif        : {self.is_active}")


katak_player = KatakZuma("Kuning")

katak_player.info_status()

katak_player.ganti_warna("Merah")

katak_player.tembak()

katak_player.info_status()
