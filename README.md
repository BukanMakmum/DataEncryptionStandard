# Enkripsi dan Dekripsi DES

Implementasi sederhana algoritma Data Encryption Standard (DES) menggunakan Python dan pustaka Tkinter untuk antarmuka pengguna grafis. Data Encryption Standard (DES) versi Education merupakan skrip yang dikembangkan untuk pembelajaran proses enkripsi dan dekripsi menggunakan DES.

## Daftar Isi

- [Pendahuluan](#pendahuluan)
- [Fitur](#fitur)
- [Instalasi](#instalasi)
- [Penggunaan](#penggunaan)
- [Tangkapan Layar](#tangkapan-layar)
- [Lisensi](#lisensi)
- [Kontak](#kontak)

## Pendahuluan

Algoritma DES (Data Encryption Standard) adalah sebuah algoritma kriptografi kunci simetris yang pertama kali dikembangkan pada tahun 1970-an dan menjadi standar enkripsi yang digunakan secara luas. DES dirancang untuk mengamankan kerahasiaan data dengan mengubahnya menjadi bentuk yang tidak dapat dibaca tanpa kunci enkripsi yang sesuai. Meskipun DES saat ini dianggap kurang aman karena panjang kunci yang terbatas, memahami konsep dasarnya masih penting dalam memahami kriptografi dan sejarah perkembangan algoritma enkripsi.
DES menggunakan kunci simetris, yang berarti kunci yang sama digunakan baik untuk enkripsi maupun dekripsi.  DES menggunakan kunci enkripsi dengan panjang 56 bit, tetapi hanya 48 bit yang digunakan secara efektif dalam proses enkripsi. Kunci ini digunakan untuk menghasilkan subkunci putaran. DES mengenkripsi data dalam bentuk blok, di mana setiap blok pesan yang akan dienkripsi memiliki panjang 64 bit. Pesan yang lebih panjang dibagi menjadi blok-blok 64 bit dan kemudian dienkripsi secara terpisah. Proses enkripsi DES melibatkan 16 putaran enkripsi yang berulang. Pada setiap putaran, blok pesan diubah dengan menggunakan subkunci yang dihasilkan dari kunci utama. Setiap putaran melibatkan operasi-operasi seperti substitusi dan permutasi untuk mencampuradukkan data. Sebelum putaran pertama dan setelah putaran ke-16, terjadi inisialisasi awal (initial permutation) dan permutasi akhir (final permutation) pada blok pesan. Inisialisasi awal mengatur data awal ke dalam urutan tertentu, sedangkan permutasi akhir mengubahnya kembali ke urutan aslinya.

## Fitur

- Enkripsi dan Dekripsi menggunakan DES;
- Input berupa 16 digit Heksadesimal;
- Output berupa 16 digit Heksadesimal dan 64 bit dalam biner;
- Tombol Salin untuk hasil biner Enkripsi/Dekripsi;
- Validasi input key dan teks plaintext/ciphertext;
- Menampilkan dan simpan hasil Debug Result Enkripsi dan Dekripsi (Khusus v2.0.beta setelahnya)
- Reset input; dan
- Tampilan modern menggunakan tkinter/antarmuka grafis yang ramah pengguna.
  
- Contoh Input dan Output
  ```bash
  Plaintext:   0123456789ABCDEF
  Key:         6281377383082ABC
  Ciphertext:  A157D624401FAF07

  Plaintext:   0123456789ABCDEF
  Key:         133457799BBCDFF1
  Ciphertext:  85E813540F0AB405

  Plaintext:   434F4D5055544552
  Key:         133457799BBCDFF1
  Ciphertext:  56F1D5C852AF813F

  Plaintext:   675A69675E5A6B5A
  Key:         5B5A57676A56676E
  Ciphertext:  974AFFBF86022D1F
   ```

## Instalasi

1. Clone repositori ini:

   ```bash
   git clone https://github.com/BukanMakmum/DataEncryptionStandard.git
   ```

2. Masuk ke direktori proyek:

   ```bash
   cd DataEncryptionStandard
   ```

3. Instal pustaka yang diperlukan:

   ```bash
   pip install tk
   pip install ttkthemes

   ```

## Penggunaan

1. Jalankan aplikasinya:

   ```bash
   DESvx.x.py atau DESvx.x.exe
   x.x = nomor versi
   ```

2. Masukkan 16 digit heksadesimal (64 bit) Plaintext/Ciphertext dan kunci.

3. Klik tombol "Enkripsi" atau "Dekripsi" sesuai kebutuhan.

4. Hasil akan ditampilkan di bidang "Hasil".

## Tangkapan Layar

![Hasil](https://github.com/BukanMakmum/DataEncryptionStandard/assets/32379649/aaf51557-e931-4e81-90d3-0f5aacf82b9f)

![Hasil2](https://github.com/BukanMakmum/DataEncryptionStandard/assets/32379649/620458fc-9694-4375-bcf1-ed0709e811ac)


## Lisensi

Proyek ini dilisensikan di bawah Lisensi MIT - lihat berkas [LICENSE](LICENSE) untuk detailnya.

## Kontak

Untuk pertanyaan atau umpan balik, silakan hubungi pengembang:
- Nama: [Bukan Makmum]
- Email: [imamsyt22@mhs.usk.ac.id]

© 2023 BukanMakmum.
