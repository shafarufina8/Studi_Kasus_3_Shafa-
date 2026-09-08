Daftar_Buku = ("Laskar Pelangi", "Bumi Manusia", "Negeri 5 Menara", "Laut Bercerita", "Cantik itu Luka")
List_Pinjaman = []

print("Daftar Buku")
for i, buku in enumerate(Daftar_Buku, 1):
    print(f"{i}. {buku}")

while True:
    print("\nPilih Menu:")
    print("1. Pinjam Buku")
    print("2. Hapus Buku dari Daftar Pinjaman")
    print("3. Lihat Daftar Pinjaman")

    Pilihan = input("Masukkan Pilihan Menu (1-3): ")

    if Pilihan == "1":
        Judul_Pinjaman = input("Masukkan Judul Buku yang ingin dipinjam:")

        if Judul_Pinjaman in Daftar_Buku:
            List_Pinjaman.append(Judul_Pinjaman)
            print(f"Buku {Judul_Pinjaman}, berhasil dipinjam!")
        else:
            print(f"Buku {Judul_Pinjaman} tidak ditemukan dalam daftar.")

    elif Pilihan == "2":
        if not List_Pinjaman:
            print("Belum ada buku yang dipinjam.")
        else:
            print("Daftar Buku yang Dipinjam:", List_Pinjaman)
            Hapus_Pinjaman = input("Masukkan judul buku yang ingin dihapus dari list pinjaman:")

            if Hapus_Pinjaman in List_Pinjaman:
                List_Pinjaman.remove(Hapus_Pinjaman)
                print(f"Buku {Hapus_Pinjaman} berhasil dihapus dari list pinjaman")
            else:
                print(f"Buku {Hapus_Pinjaman} tidak ditemukan dalam list pinjaman.")

    elif Pilihan == "3":
        break
    else:
        print("Pilihan tidak valid, silahkan coba lagi.")

if List_Pinjaman:
    print("Daftar buku berhasil dipinjam:")
    for i, buku in enumerate(List_Pinjaman, 1):
        print(f"{i}. {buku}")
else:
    print("Peter tidak meminjam buku apapun.")






            
