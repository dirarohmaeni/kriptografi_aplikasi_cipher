# APLIKASI CIPHER KLASIK

Repository ini berisi tiga aplikasi cipher klasik yang dibuat menggunakan bahasa pemrograman Python sebagai tugas mata kuliah Kriptografi.

## Identitas

**Nama:** Dira Rohmaeni  
**Program Studi:** Teknik Informatika  
**Mata Kuliah:** Kriptografi  
**Bahasa Pemrograman:** Python  

---

# DAFTAR APLIKASI

Repository ini terdiri dari:

1. Caesar Cipher
2. Vigenere Cipher
3. Columnar Transposition Cipher

Ketiga aplikasi menyediakan fitur enkripsi dan dekripsi.

---

# 1. CAESAR CIPHER

## Deskripsi

Caesar Cipher merupakan salah satu cipher klasik yang menggunakan teknik substitusi.

Pada metode ini, setiap huruf pada plaintext digeser berdasarkan nilai kunci tertentu. Misalnya, dengan kunci 3:

A menjadi D  
B menjadi E  
C menjadi F  

dan seterusnya.

## Rumus

### Enkripsi

c = (p + k) mod 26

### Dekripsi

p = (c - k) mod 26

Keterangan:

- p = plaintext
- c = ciphertext
- k = kunci

## Fitur

- Enkripsi pesan
- Dekripsi ciphertext
- Menggunakan kunci 0 sampai 25
- Mempertahankan huruf besar dan kecil
- Spasi dan tanda baca tidak diubah

## Contoh

Plaintext:

HELLO WORLD

Kunci:

3

Hasil enkripsi:

KHOOR ZRUOG

Jika ciphertext tersebut didekripsi menggunakan kunci 3, maka hasilnya kembali menjadi:

HELLO WORLD

## Cara Menjalankan

Buka terminal pada folder repository, kemudian jalankan:

python caesar_cipher.py

---

# 2. VIGENERE CIPHER

## Deskripsi

Vigenere Cipher merupakan cipher substitusi polialfabetik.

Berbeda dengan Caesar Cipher yang menggunakan satu nilai pergeseran, Vigenere Cipher menggunakan kata atau rangkaian huruf sebagai kunci.

Kunci akan digunakan secara berulang apabila panjang kunci lebih pendek daripada plaintext.

## Cara Kerja

Setiap huruf pada plaintext digeser berdasarkan nilai huruf pada kunci.

Nilai huruf:

A = 0  
B = 1  
C = 2  
...  
Z = 25

Contoh kunci:

KEY

Jika plaintext lebih panjang dari kunci, maka kunci digunakan secara berulang:

KEYKEYKEY...

## Fitur

- Enkripsi pesan
- Dekripsi ciphertext
- Menggunakan kata sebagai kunci
- Kunci harus berupa huruf
- Spasi dan tanda baca tetap dipertahankan

## Contoh

Plaintext:

HELLOWORLD

Kunci:

KEY

Kunci yang digunakan:

KEYKEYKEYK

Setelah proses enkripsi, akan diperoleh ciphertext sesuai dengan pergeseran berdasarkan kunci.

Ciphertext tersebut dapat dikembalikan menjadi plaintext menggunakan proses dekripsi dengan kunci yang sama.

## Cara Menjalankan

Buka terminal pada folder repository, kemudian jalankan:

python vigenere_cipher.py

---

# 3. COLUMNAR TRANSPOSITION CIPHER

## Deskripsi

Columnar Transposition Cipher merupakan cipher klasik yang menggunakan teknik transposisi.

Pada teknik transposisi, karakter tidak diganti dengan karakter lain, tetapi posisi karakter diubah.

Plaintext dituliskan ke dalam tabel berdasarkan jumlah karakter pada kunci. Setelah itu, karakter dibaca berdasarkan urutan kolom kunci.

## Cara Kerja

Contoh kunci:

TOMBAK

Plaintext terlebih dahulu dituliskan ke dalam tabel berdasarkan jumlah kolom dari kunci.

Kemudian kolom dibaca berdasarkan urutan alfabet dari karakter pada kunci untuk menghasilkan ciphertext.

## Fitur

- Enkripsi pesan
- Dekripsi ciphertext
- Menggunakan kata sebagai kunci
- Mengubah posisi karakter
- Menggunakan padding X apabila panjang plaintext tidak memenuhi jumlah kolom

## Contoh

Plaintext:

SISTEM DAN TEKNOLOGI INFORMASI ITB

Kunci:

TOMBAK

Spasi dihilangkan terlebih dahulu, kemudian plaintext dimasukkan ke dalam tabel dan dibaca berdasarkan urutan kolom kunci.

Hasil pembacaan kolom menghasilkan ciphertext.

## Cara Menjalankan

Buka terminal pada folder repository, kemudian jalankan:

python columnar_transposition.py

---

# FITUR APLIKASI

Ketiga aplikasi memiliki menu yang sama:

1. Enkripsi
2. Dekripsi
3. Keluar

Contoh tampilan:

==============================
       CAESAR CIPHER
==============================
1. Enkripsi
2. Dekripsi
3. Keluar
==============================

Pengguna dapat memilih proses yang ingin dilakukan melalui menu tersebut.

---

# TEKNOLOGI YANG DIGUNAKAN

- Python
- Visual Studio Code
- GitHub

Tidak menggunakan library eksternal sehingga aplikasi dapat dijalankan menggunakan Python standar.

---

# STRUKTUR PROJECT

```text
cipher/
│
├── caesar_cipher.py
├── vigenere_cipher.py
├── columnar_transposition.py
└── README.md