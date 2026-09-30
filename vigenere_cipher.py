def vigenere_cipher(teks, kunci, enkripsi=True):
    hasil = ""
    indeks_kunci = 0

    kunci = kunci.upper()

    for karakter in teks:
        if karakter.isalpha():
            nilai_kunci = ord(kunci[indeks_kunci % len(kunci)]) - ord('A')

            if not enkripsi:
                nilai_kunci = -nilai_kunci

            if karakter.isupper():
                hasil += chr(
                    (ord(karakter) - ord('A') + nilai_kunci) % 26
                    + ord('A')
                )
            else:
                hasil += chr(
                    (ord(karakter) - ord('a') + nilai_kunci) % 26
                    + ord('a')
                )

            indeks_kunci += 1
        else:
            hasil += karakter

    return hasil


while True:
    print("\n==============================")
    print("       VIGENERE CIPHER")
    print("==============================")
    print("1. Enkripsi")
    print("2. Dekripsi")
    print("3. Keluar")
    print("==============================")

    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        teks = input("Masukkan pesan: ")
        kunci = input("Masukkan kunci: ")

        if kunci.isalpha():
            hasil = vigenere_cipher(teks, kunci, True)
            print("Hasil enkripsi:", hasil)
        else:
            print("Kunci harus berupa huruf.")

    elif pilihan == "2":
        teks = input("Masukkan ciphertext: ")
        kunci = input("Masukkan kunci: ")

        if kunci.isalpha():
            hasil = vigenere_cipher(teks, kunci, False)
            print("Hasil dekripsi:", hasil)
        else:
            print("Kunci harus berupa huruf.")

    elif pilihan == "3":
        print("Program selesai.")
        break

    else:
        print("Pilihan tidak tersedia.")