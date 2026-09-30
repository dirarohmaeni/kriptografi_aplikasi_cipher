def urutan_kolom(kunci):
    return sorted(range(len(kunci)), key=lambda i: (kunci[i], i))


def enkripsi(teks, kunci):
    teks = teks.replace(" ", "")
    jumlah_kolom = len(kunci)

    # Tambahkan X jika panjang teks tidak memenuhi jumlah kolom
    sisa = len(teks) % jumlah_kolom

    if sisa != 0:
        teks += "X" * (jumlah_kolom - sisa)

    # Membuat tabel
    tabel = []

    for i in range(0, len(teks), jumlah_kolom):
        tabel.append(teks[i:i + jumlah_kolom])

    hasil = ""

    # Membaca kolom berdasarkan urutan alfabet kunci
    for kolom in urutan_kolom(kunci):
        for baris in tabel:
            hasil += baris[kolom]

    return hasil


def dekripsi(teks, kunci):
    jumlah_kolom = len(kunci)
    jumlah_baris = len(teks) // jumlah_kolom

    tabel = [
        [""] * jumlah_kolom
        for _ in range(jumlah_baris)
    ]

    indeks = 0

    # Mengisi tabel berdasarkan urutan kunci
    for kolom in urutan_kolom(kunci):
        for baris in range(jumlah_baris):
            tabel[baris][kolom] = teks[indeks]
            indeks += 1

    hasil = ""

    # Membaca tabel berdasarkan baris
    for baris in tabel:
        for karakter in baris:
            hasil += karakter

    # Menghapus padding X
    return hasil.rstrip("X")


while True:
    print("\n================================")
    print("   COLUMNAR TRANSPOSITION")
    print("================================")
    print("1. Enkripsi")
    print("2. Dekripsi")
    print("3. Keluar")
    print("================================")

    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        teks = input("Masukkan pesan: ")
        kunci = input("Masukkan kunci: ").upper()

        if kunci.isalpha():
            hasil = enkripsi(teks, kunci)
            print("Hasil enkripsi:", hasil)
        else:
            print("Kunci harus berupa huruf.")

    elif pilihan == "2":
        teks = input("Masukkan ciphertext: ")
        kunci = input("Masukkan kunci: ").upper()

        if kunci.isalpha():
            if len(teks) % len(kunci) == 0:
                hasil = dekripsi(teks, kunci)
                print("Hasil dekripsi:", hasil)
            else:
                print("Ciphertext tidak valid.")
        else:
            print("Kunci harus berupa huruf.")

    elif pilihan == "3":
        print("Program selesai.")
        break

    else:
        print("Pilihan tidak tersedia.")