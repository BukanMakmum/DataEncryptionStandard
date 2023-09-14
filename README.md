# Enkripsi dan Dekripsi DES

Implementasi sederhana algoritma Data Encryption Standard (DES) menggunakan Python dan pustaka Tkinter untuk antarmuka pengguna grafis.

## Daftar Isi

- [Pendahuluan](#pendahuluan)
- [Fitur](#fitur)
- [Instalasi](#instalasi)
- [Penggunaan](#penggunaan)
- [Tangkapan Layar](#tangkapan-layar)
- [Lisensi](#lisensi)
- [Kontak](#kontak)

## Pendahuluan

Data Encryption Standard (DES) adalah cipher blok kunci simetris yang pernah banyak digunakan untuk enkripsi data. Proyek ini menyediakan aplikasi GUI sederhana untuk mengenkripsi dan mendekripsi teks menggunakan DES.

## Fitur

- Mengenkripsi Plaintext 16 digit heksadesimal dengan kunci dalam format heksadesimal.
- Mendekripsi Ciphertext 16 digit heksadesimal dengan menggunakan kunci yang sama yang digunakan untuk enkripsi.
- Menampilkan Debug Result (Khusus v2.0 setelahnya) Enkripsi dan Dekripsi (Kebenaran hasil debug masih dalam penyempurnaan)
- Antarmuka grafis yang ramah pengguna.
- Contoh Inpu dan Output
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

2. Masukkan teks biasa/teks sandi dan kunci dalam format heksadesimal.

3. Klik tombol "Enkripsi" atau "Dekripsi" sesuai kebutuhan.

4. Hasil akan ditampilkan di bidang "Hasil".

## Tangkapan Layar


![Hasil](https://github.com/BukanMakmum/DataEncryptionStandard/assets/32379649/99714f3f-0c6f-4fb3-b33e-5520e1fa2c70)



## Lisensi

Proyek ini dilisensikan di bawah Lisensi MIT - lihat berkas [LICENSE](LICENSE) untuk detailnya.

## Kontak

Untuk pertanyaan atau umpan balik, silakan hubungi pengembang:
- Nama: [Bukan Makmum]
- Email: [imamsyt22@mhs.usk.ac.id]

© 2023 BukanMakmum.
