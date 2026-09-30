def caesar_cipher(teks, kunci, enkripsi=True):
    hasil = ""

    if not enkripsi:
        kunci = -kunci

    for karakter in teks:
        if karakter.isupper():
            hasil += chr((ord(karakter) - ord('A') + kunci) % 26 + ord('A'))
        elif karakter.islower():
            hasil += chr((ord(karakter) - ord('a') + kunci) % 26 + ord('a'))
        else:
            hasil += karakter

    return hasil


while True:
    print("\n==============================")
    print("       CAESAR CIPHER")
    print("==============================")
    print("1. Enkripsi")
    print("2. Dekripsi")
    print("3. Keluar")
    print("==============================")

    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        teks = input("Masukkan pesan: ")
        kunci = int(input("Masukkan kunci (0-25): "))

        hasil = caesar_cipher(teks, kunci, True)
        print("Hasil enkripsi:", hasil)

    elif pilihan == "2":
        teks = input("Masukkan ciphertext: ")
        kunci = int(input("Masukkan kunci (0-25): "))

        hasil = caesar_cipher(teks, kunci, False)
        print("Hasil dekripsi:", hasil)

    elif pilihan == "3":
        print("Program selesai.")
        break

    else:
        print("Pilihan tidak tersedia.")