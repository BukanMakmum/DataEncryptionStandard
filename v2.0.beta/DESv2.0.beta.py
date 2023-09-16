import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import Menu  # Tambahkan ini untuk mengimpor modul menu
from ttkthemes import ThemedStyle
from tkinter import scrolledtext  # Import the scrolledtext module
from tkinter import filedialog
import webbrowser # Fungsi untuk mengarahkan ke alamat email saat teks hak cipta diklik
import os

# Initial Permutation (IP) table
IP = [58, 50, 42, 34, 26, 18, 10, 2, 60, 52, 44, 36, 28, 20, 12, 4,
      62, 54, 46, 38, 30, 22, 14, 6, 64, 56, 48, 40, 32, 24, 16, 8,
      57, 49, 41, 33, 25, 17, 9, 1, 59, 51, 43, 35, 27, 19, 11, 3,
      61, 53, 45, 37, 29, 21, 13, 5, 63, 55, 47, 39, 31, 23, 15, 7]

# Final Permutation (FP) table
FP = [40, 8, 48, 16, 56, 24, 64, 32, 39, 7, 47, 15, 55, 23, 63, 31,
      38, 6, 46, 14, 54, 22, 62, 30, 37, 5, 45, 13, 53, 21, 61, 29,
      36, 4, 44, 12, 52, 20, 60, 28, 35, 3, 43, 11, 51, 19, 59, 27,
      34, 2, 42, 10, 50, 18, 58, 26, 33, 1, 41, 9, 49, 17, 57, 25]

# Tabel Kompresi Kunci PC-1
PC1 = [57, 49, 41, 33, 25, 17, 9,
       1, 58, 50, 42, 34, 26, 18,
       10, 2, 59, 51, 43, 35, 27,
       19, 11, 3, 60, 52, 44, 36,
       63, 55, 47, 39, 31, 23, 15,
       7, 62, 54, 46, 38, 30, 22,
       14, 6, 61, 53, 45, 37, 29,
       21, 13, 5, 28, 20, 12, 4]

# Tabel Kompresi Kunci PC-2
PC2 = [14, 17, 11, 24, 1, 5,
       3, 28, 15, 6, 21, 10,
       23, 19, 12, 4, 26, 8,
       16, 7, 27, 20, 13, 2,
       41, 52, 31, 37, 47, 55,
       30, 40, 51, 45, 33, 48,
       44, 49, 39, 56, 34, 53,
       46, 42, 50, 36, 29, 32]

# Expansion Box (EBox) table
EBox = [32, 1, 2, 3, 4, 5, 4, 5, 6, 7, 8, 9, 8, 9, 10, 11,
        12, 13, 12, 13, 14, 15, 16, 17, 16, 17, 18, 19, 20, 21, 20, 21,
        22, 23, 24, 25, 24, 25, 26, 27, 28, 29, 28, 29, 30, 31, 32, 1]

# S-Box tables
SBox = [
    # S1
    [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7,
     0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8,
     4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0,
     15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13],

    # S2
    [15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10,
     3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5,
     0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15,
     13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9],

    # S3
    [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8,
     13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1,
     13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7,
     1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12],

    # S4
    [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15,
     13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9,
     10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4,
     3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14],

    # S5
    [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9,
     14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6,
     4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14,
     11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3],

    # S6
    [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11,
     10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8,
     9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6,
     4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13],

    # S7
    [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1,
     13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6,
     1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2,
     6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12],

    # S8
    [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7,
     1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2,
     7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8,
     2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]
]

# P-Box permutation
PBox = [16, 7, 20, 21, 29, 12, 28, 17,
        1, 15, 23, 26, 5, 18, 31, 10,
        2, 8, 24, 14, 32, 27, 3, 9,
        19, 13, 30, 6, 22, 11, 4, 25]

# Tabel pergeseran bit untuk subkunci
ShiftBits = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]

# Fungsi untuk melakukan permutasi dengan tabel yang diberikan
def permute(data, table):
    return ''.join(data[i - 1] for i in table)

# Fungsi untuk melakukan pergeseran bit (left shift) pada data
def left_shift(data, shift_amount):
    return data[shift_amount:] + data[:shift_amount]

# Buat variabel global untuk menyimpan hasil debug dari berbagai koding
global debug_results
debug_results = []

# Fungsi untuk menghasilkan subkunci menggunakan tabel PC-1 dan tabel pergeseran bit
def generate_subkeys(key):
    global PC1, PC2, ShiftBits, debug_results
    
    key_bin = bin(int(key, 16))[2:].zfill(64)
    generate_subkeys_debug_counter = 1  # Inisialisasi nomor urut debug

    # Debug: Menambahkan judul "Generate Subkeys" ke hasil debug
    debug_results.append("Generate Subkeys:")
    
    # Debug: Menampilkan kunci awal (heksadesimal)
    debug_results.append(f"{generate_subkeys_debug_counter}. Kunci Awal (heksadesimal): {key}")
    generate_subkeys_debug_counter += 1
    
    # Debug: Menampilkan kunci awal (biner 64-bit)
    debug_results.append(f"{generate_subkeys_debug_counter}. Kunci Awal (biner 64-bit): {key_bin}")
    generate_subkeys_debug_counter += 1

    # Lakukan "parity bit drop" sesuai dengan deskripsi yang Anda berikan
    key_parity_dropped = ''.join(key_bin[i] for i in range(64) if (i + 1) % 8 != 0)
    
    # Debug: Menampilkan nilai Parity Drop (biner 56-bit)
    debug_results.append(f"{generate_subkeys_debug_counter}. Parity drop kunci (biner 56-bit): {key_parity_dropped}")
    generate_subkeys_debug_counter += 1

    # Lakukan permutasi sesuai dengan tabel PC1 yang telah didefinisikan
    key_permuted = permute(key_bin, PC1)
    
    # Debug: Menampilkan nilai setelah permutasi PC1 (biner 56-bit)
    debug_results.append(f"{generate_subkeys_debug_counter}. Permutasi PC-1 kunci (biner 56-bit) : {key_permuted}")
    generate_subkeys_debug_counter += 1

    left_key, right_key = key_permuted[:28], key_permuted[28:]
    subkeys = []

    for round_num, shift_amount in enumerate(ShiftBits, start=1):
        left_key = left_shift(left_key, shift_amount)
        right_key = left_shift(right_key, shift_amount)

        # Debug: Menampilkan ronde yang sedang berlangsung
        debug_results.append("")  # Baris kosong
        debug_results.append(f"Ronde {round_num}:")

        # Debug: Menampilkan 28 bit sebelah kiri setelah pergeseran
        debug_results.append(f"{generate_subkeys_debug_counter}. 28 bit sebelah kiri, shift left {shift_amount} bit ke kiri (Ronde-{round_num}): {left_key}")
        generate_subkeys_debug_counter += 1
        
        # Debug: Menampilkan 28 bit sebelah kanan setelah pergeseran
        debug_results.append(f"{generate_subkeys_debug_counter}. 28 bit sebelah kanan, shift left {shift_amount} bit ke kiri (Ronde-{round_num}): {right_key}")
        generate_subkeys_debug_counter += 1

        subkey = permute(left_key + right_key, PC2)  # Menggunakan PC2 dari variabel global
        subkeys.append(subkey)

        # Debug: Menampilkan subkunci setiap ronde
        debug_results.append(f"{generate_subkeys_debug_counter}. Permutasi kompresi PC-2 (kunci Ronde-{round_num}): {subkey}")
        generate_subkeys_debug_counter += 1

    # Sisipkan baris kosong (enter) setelah hasil debug dari bagian enkripsi
    debug_results.append("")  # Baris kosong

    return subkeys

# Fungsi untuk melakukan enkripsi dengan algoritma DES
def encrypt(data, subkeys):
    global debug_results  # Tambahkan variabel global
    encrypt_debug_counter = 1  # Inisialisasi nomor urut debug

    copy_button.config(state="normal")
    data_bin = bin(int(data, 16))[2:].zfill(64)
    debug_results.append("")  # Baris kosong

    # Debug: Menambahkan hasil debug dari fungsi encrypt
    debug_results.append("Encrypt:")
    debug_results.append(f"{encrypt_debug_counter}. Plaintext (heksadesimal): " + data)
    encrypt_debug_counter += 1

    debug_results.append(f"{encrypt_debug_counter}. Plaintext (biner 64-bit): " + data_bin)
    encrypt_debug_counter += 1

    # Inisialisasi awal permutation
    data_permuted = permute(data_bin, IP)
    debug_results.append(f"{encrypt_debug_counter}. Permutasi Awal IP (biner 64-bit): " + data_permuted)
    encrypt_debug_counter += 1

    left_half = data_permuted[:32]
    right_half = data_permuted[32:]

    # Debug: Menampilkan hasil split 32-bit sebelah kiri
    debug_results.append(f"{encrypt_debug_counter}. Split 32-bit sebelah kiri: " + left_half)
    encrypt_debug_counter += 1

    # Debug: Menampilkan hasil split 32-bit sebelah kanan
    debug_results.append(f"{encrypt_debug_counter}. Split 32-bit sebelah kanan: " + right_half)
    encrypt_debug_counter += 1

    for i in range(16):
        # Debug: Menampilkan ronde yang sedang berlangsung
        debug_results.append("")  # Baris kosong
        debug_results.append(f"Ronde {i + 1}:")

        # Debug: Menampilkan subkunci ronde yang digunakan
        debug_results.append(f"{encrypt_debug_counter}. Subkunci Ronde-{i + 1} (biner 48-bit): " + subkeys[i])
        encrypt_debug_counter += 1

        # Ekspansi
        right_expanded = permute(right_half, EBox)
        debug_results.append(f"{encrypt_debug_counter}. Permutasi Ekspansi terhadap 32-bit sebelah kanan menjadi 48-bit: " + right_expanded)
        encrypt_debug_counter += 1

        # XOR Permutasi Ekspansi (biner 48-bit) dengan Subkunci (biner 48-bit)
        subkey = subkeys[i]
        right_xor = bin(int(right_expanded, 2) ^ int(subkey, 2))[2:].zfill(48)
        debug_results.append(f"{encrypt_debug_counter}. XOR Permutasi Ekspansi (biner 48-bit) dengan Subkunci (biner 48-bit): " + right_xor)
        encrypt_debug_counter += 1

        # Inisialisasi string debug sementara untuk S-Box substitution
        sbox_debug_temp = ""

        # S-Box substitution
        sbox_output = ""
        for j in range(8):
            sbox_input = right_xor[j * 6: (j + 1) * 6]
            row = int(sbox_input[0] + sbox_input[5], 2)
            col = int(sbox_input[1:5], 2)
            sbox_value = SBox[j][row * 16 + col]
            sbox_output += format(sbox_value, '04b')

            # Format pesan debug sementara dengan spasi 5 karakter
            sbox_debug_temp += f"    Bagian 6-bit ke {j+1}\n"
            sbox_debug_temp += f"    Indek baris \t\t: {row}\n"
            sbox_debug_temp += f"    Indek kolom \t\t: {col}\n"
            sbox_debug_temp += f"    4-bit Output S{j+1}\t: {format(sbox_value, '04b')}\n\n"

        # Debug: Menampilkan hasil substitusi S-Box per ronde ke debug sementara
        debug_results.append(f"{encrypt_debug_counter}. Hasil substitusi S-Box per ronde ke-{i + 1}:\n{sbox_debug_temp}")
        debug_results.append(f"    Total 32-bit output S-Boks Substitusi ronde ke-{i + 1}: " + sbox_output)
        encrypt_debug_counter += 1
        debug_results.append("")  # Baris kosong

        # P-Box permutation
        right_permuted = permute(sbox_output, PBox)
        debug_results.append(f"{encrypt_debug_counter}. Permutasi P-Box (biner 32-bit): " + right_permuted)
        encrypt_debug_counter += 1

        # Menampilkan left_half (biner 32-bit)
        debug_results.append(f"{encrypt_debug_counter}. Left Half (biner 32-bit): " + left_half)
        encrypt_debug_counter += 1

        # XOR Permutasi P-Box (biner 32-bit) dengan Left Half (biner 32-bit)
        right_xor = bin(int(left_half, 2) ^ int(right_permuted, 2))[2:].zfill(32)
        debug_results.append(f"{encrypt_debug_counter}. XOR Permutasi P-Box (biner 32-bit) dengan Left Half (biner 32-bit): " + right_xor)
        encrypt_debug_counter += 1

        # Debug: Menampilkan hasil gabungan Split 32-bit sebelah kanan dengan XOR Permutasi P-Box (biner 32-bit) dengan Left Half (biner 32-bit)
        debug_results.append(f"{encrypt_debug_counter}. Gabungan Split 32-bit sebelah kanan dengan XOR Permutasi P-Box (biner 32-bit) dengan Left Half (biner 32-bit): " + right_half + right_xor)
        encrypt_debug_counter += 1

        # Debug: Menampilkan hasil gabungan Split 32-bit sebelah kanan dengan XOR Permutasi P-Box (biner 32-bit) dengan Left Half (biner 32-bit)
        if i == 15:  # Ini adalah ronde ke-16
            debug_results.append(f"{encrypt_debug_counter}. Gabungan Split 32-bit sebelah kanan dengan XOR Permutasi P-Box (biner 32-bit) dengan Left Half (biner 32-bit) pada ronde ke-16: " + right_half + right_xor)
            encrypt_debug_counter += 1

        # Update left_half dan right_half untuk iterasi berikutnya
        left_half = right_half
        right_half = right_xor

    # Final Permutation
    combined = right_half + left_half
    # R16+L16
    if i == 15:  # Ini adalah ronde ke-16
        debug_results.append(f"{encrypt_debug_counter}. Hasil left_half dan right_half (biner 64-bit) pada ronde ke-16: " + combined)
    encrypt_debug_counter += 1
    ciphertext = permute(combined, FP)
    debug_results.append("")  # Baris kosong

    # Judul Hasil Encrypt:
    debug_results.append("Hasil Encrypt:")

    # Debug: Menampilkan ciphertext (biner)
    debug_results.append(f"{encrypt_debug_counter}. Ciphertext (biner 64-bit): " + ciphertext)
    
    # Konversi ciphertext dari biner ke heksadesimal
    ciphertext_hex = hex(int(ciphertext, 2))[2:].upper()
    debug_results.append(f"{encrypt_debug_counter}. Ciphertext (heksadesimal): " + ciphertext_hex)

    # Sisipkan baris kosong (enter) setelah hasil debug dari bagian enkripsi
    debug_results.append("")  # Baris kosong

    return ciphertext

# Fungsi untuk melakukan dekripsi dengan algoritma DES
def decrypt(data, subkeys):
    global debug_results  # Tambahkan variabel global
    decrypt_debug_counter = 1  # Inisialisasi nomor urut debug

    copy_button.config(state="normal")
    data_bin = bin(int(data, 16))[2:].zfill(64)
    debug_results.append("")  # Baris kosong

    # Debug: Menambahkan hasil debug "Decrypt" ke hasil debug
    debug_results.append("Decrypt:")

    # Debug: Menambahkan ciphertext dalam format heksadesimal
    debug_results.append(f"{decrypt_debug_counter}. Ciphertext (heksadesimal): {data}")
    decrypt_debug_counter += 1

    # Debug: Menambahkan ciphertext dalam format biner
    debug_results.append(f"{decrypt_debug_counter}. Ciphertext (biner 64-bit): {data_bin}")
    decrypt_debug_counter += 1

    # Inisialisasi awal permutation
    data_permuted = permute(data_bin, IP)

    left_half = data_permuted[:32]
    right_half = data_permuted[32:]

    for i in range(16):
        debug_results.append("")  # Baris kosong
        debug_results.append(f"Ronde {i + 1}:")

        # Ekspansi
        right_expanded = permute(right_half, EBox)
        debug_results.append(f"{decrypt_debug_counter}. Ekspansi Ronde-{i + 1} (biner 48-bit): " + right_expanded)
        decrypt_debug_counter += 1

        # XOR dengan subkunci (dalam urutan terbalik)
        subkey = subkeys[15 - i]
        right_xor = bin(int(right_expanded, 2) ^ int(subkey, 2))[2:].zfill(48)
        debug_results.append(f"{decrypt_debug_counter}. XOR dengan Subkunci Ronde-{i + 1} (biner 48-bit): " + right_xor)
        decrypt_debug_counter += 1

        # S-Box substitution
        sbox_output = ""
        for j in range(8):
            sbox_input = right_xor[j * 6: (j + 1) * 6]
            row = int(sbox_input[0] + sbox_input[5], 2)
            col = int(sbox_input[1:5], 2)
            sbox_value = SBox[j][row * 16 + col]
            sbox_output += format(sbox_value, '04b')
        
        debug_results.append(f"{decrypt_debug_counter}. Hasil Substitusi S-Box Ronde-{i + 1} (biner 32-bit): " + sbox_output)
        decrypt_debug_counter += 1

        # P-Box permutation
        right_permuted = permute(sbox_output, PBox)
        debug_results.append(f"{decrypt_debug_counter}. Permutasi P-Box Ronde-{i + 1} (biner 32-bit): " + right_permuted)
        decrypt_debug_counter += 1

        # XOR dengan left_half
        right_xor = bin(int(left_half, 2) ^ int(right_permuted, 2))[2:].zfill(32)
        debug_results.append(f"{decrypt_debug_counter}. XOR dengan Left Half Ronde-{i + 1} (biner 32-bit): " + right_xor)
        decrypt_debug_counter += 1

        # Update left_half dan right_half untuk iterasi berikutnya
        left_half = right_half
        right_half = right_xor

    # Gabungkan left_half dan right_half
    combined = right_half + left_half
    debug_results.append("")  # Baris kosong

    # Judul Hasil Decrypt:
    debug_results.append("Hasil Decrypt:")

    # Final permutation
    plaintext = permute(combined, FP)
    debug_results.append(f"{decrypt_debug_counter}. Plaintext (biner 64-bit): " + plaintext)

    # Konversi plaintext dari biner ke heksadesimal
    plaintext_hex = hex(int(plaintext, 2))[2:].upper()
    debug_results.append(f"{decrypt_debug_counter}. Plaintext (heksadesimal): " + plaintext_hex)

    # Sisipkan baris kosong (enter) setelah hasil debug dari bagian dekripsi
    debug_results.append("")  # Baris kosong

    return plaintext

# Fungsi untuk mendekripsi teks saat tombol "Enkripsi" ditekan
def encrypt_text():
    global encryption_done
     # Hapus hasil debug yang sudah ada
    debug_results.clear()

    encryption_done = True
    copy_button.config(state="disabled")
    input_key = key_entry.get()
    input_text_hex = input_entry.get()

    try:
        # Cek apakah input adalah 16 karakter heksadesimal
        if not all(c in "0123456789ABCDEF" for c in input_key) or len(input_key) != 16:
            messagebox.showerror("Error", "Key harus berupa 16 karakter heksadesimal")
            return

        if not all(c in "0123456789ABCDEF" for c in input_text_hex) or len(input_text_hex) != 16:
            messagebox.showerror("Error", "Plaintext/Ciphertext harus berupa 16 karakter heksadesimal")
            return
        
        plaintext_bin = bin(int(input_text_hex, 16))[2:].zfill(64)
        #print("1. Plaintext asli dalam bentuk biner 64 bit:", plaintext_bin)

        # Debug: Menampilkan nilai kunci asli dalam bentuk biner
        key_bin = bin(int(input_key, 16))[2:].zfill(64)
        #print("2. Nilai kunci asli dalam bentuk biner 64 bit:", key_bin)

        # Enkripsi input heksadesimal
        subkeys = generate_subkeys(input_key)
        ciphertext_bin = encrypt(input_text_hex, subkeys)

        # Membagi ciphertext_bin menjadi 4 baris dengan 16 digit per baris dan menambahkan spasi setiap 4 digit
        formatted_ciphertext = '\n'.join([' '.join(ciphertext_bin[i:i+4] for i in range(j, j+16, 4)) for j in range(0, len(ciphertext_bin), 16)])

        # Menetapkan teks ke bin_output_text
        bin_output_text["text"] = formatted_ciphertext

        # Konversi ciphertext dari biner ke heksadesimal
        ciphertext_hex = hex(int(ciphertext_bin, 2))[2:].upper().zfill(16)

        # Tampilkan ciphertext dalam format 16 karakter heksadesimal
        hex_output_entry.delete(0, tk.END)
        hex_output_entry.insert(0, ciphertext_hex)
        
         # Mengatur warna latar belakang label bin_output_text saat dekripsi selesai
        bin_output_text.configure(background="#C0C0C0")

    except Exception as e:
        messagebox.showerror("Error", f"Terjadi kesalahan: {str(e)}")

# Fungsi untuk mendekripsi teks saat tombol "Dekripsi" ditekan
def decrypt_text():
    global encryption_done
     # Hapus hasil debug yang sudah ada
    debug_results.clear()

    encryption_done = True
    copy_button.config(state="disabled")
    input_key = key_entry.get()
    ciphertext_hex = input_entry.get()

    try:
        # Cek apakah input adalah 16 karakter heksadesimal
        if not all(c in "0123456789ABCDEF" for c in input_key) or len(input_key) != 16:
            messagebox.showerror("Error", "Key harus berupa 16 karakter heksadesimal")
            return

        if not all(c in "0123456789ABCDEF" for c in ciphertext_hex) or len(ciphertext_hex) != 16:
            messagebox.showerror("Error", "Ciphertext harus berupa 16 karakter heksadesimal")
            return

        # Dekripsi ciphertext heksadesimal
        subkeys = generate_subkeys(input_key)
        plaintext_bin = decrypt(ciphertext_hex, subkeys)

        
        # Membagi plaintext_bin menjadi 4 baris dengan 16 digit per baris dan menambahkan spasi setiap 4 digit
        formatted_plaintext = '\n'.join([plaintext_bin[i:i+4] + ' ' + plaintext_bin[i+4:i+8] + ' ' + plaintext_bin[i+8:i+12] + ' ' + plaintext_bin[i+12:i+16] for i in range(0, len(plaintext_bin), 16)])

        # Menetapkan teks ke bin_output_text
        bin_output_text["text"] = formatted_plaintext

        # Konversi plaintext dari biner ke heksadesimal
        plaintext_hex = hex(int(plaintext_bin, 2))[2:].upper().zfill(16)

        # Tampilkan plaintext dalam format 16 karakter heksadesimal
        hex_output_entry.delete(0, tk.END)
        hex_output_entry.insert(0, plaintext_hex)

         # Mengatur warna latar belakang label bin_output_text saat dekripsi selesai
        bin_output_text.configure(background="#FFFFFF")

    except Exception as e:
        messagebox.showerror("Error", f"Terjadi kesalahan: {str(e)}")

# Fungsi untuk mereset input dan output
def reset_fields():
    copy_button.config(state="disabled")
    input_entry.delete(0, tk.END)
    key_entry.delete(0, tk.END)
    hex_output_entry.delete(0, tk.END)
    bin_output_text["text"] = ""

    # Mengatur warna latar belakang label bin_output_text agar hilang
    bin_output_text.configure(background="")
    encryption_done = False  # Setel enkripsi status yang dilakukan ke False agar warna label biner hilang

# Fungsi untuk mengatur jendela di tengah layar
def center_window(window, width, height):
    # Mendapatkan lebar dan tinggi layar
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    # Menghitung posisi x dan y untuk menempatkan jendela di tengah layar
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2

    # Mengatur geometri jendela sesuai dengan posisi dan ukuran yang telah dihitung
    window.geometry(f"{width}x{height}+{x}+{y}")
    window.resizable(False, False)  # Menonaktifkan kemampuan untuk merubah ukuran jendela

# Buat jendela utama
window = tk.Tk()
window.title("Data Encryption Standard")
app_version = "Education 2.0.beta"

# Ganti favicon dengan file ikon yang sesuai
#window.iconbitmap("favicon.ico")  # Ganti "favicon.ico" dengan path ke file ikon Anda

# Mengatur ukuran jendela
window_width = 350
window_height = 500

# Variabel global untuk melacak apakah enkripsi atau dekripsi telah dilakukan
encryption_done = False

# Inisialisasi global variable
debug_option_enabled = False

# Menyimpan jendela di tengah layar
center_window(window, window_width, window_height)

# Menggunakan tema modern
style = ThemedStyle(window)
style.set_theme("plastik")

# Mendapatkan direktori saat ini di mana skrip berjalan
current_directory = os.path.dirname(__file__)

# Gabungkan direktori saat ini dengan nama file ikon favicon
favicon_path = os.path.join(current_directory, "favicon.ico")

# Atur favicon
window.iconbitmap(default=favicon_path)


# Mengambil teks judul dari jendela
judul_jendela = window.title()

# Label judul dengan font yang lebih besar
title_label = ttk.Label(window, text=judul_jendela, font=("Helvetica", 14, "bold"))
title_label.pack(pady=(20, 5))  # Padding atas 20, bawah 5

# Label versi dengan font yang lebih kecil
version_label = ttk.Label(window, text=f"Versi {app_version}", font=("Helvetica", 10))
version_label.pack()

# Agar label versi berada di bawah label judul
title_label.pack(pady=(20, 0))

# Frame untuk teks masukan dan kunci
input_frame = ttk.Frame(window)
input_frame.pack(pady=10)  # Padding atas 10

text_label = ttk.Label(input_frame, text="Plaintext/Ciphertext:")
text_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
input_entry = ttk.Entry(input_frame)
input_entry.grid(row=0, column=1, padx=10, pady=10)

key_label = ttk.Label(input_frame, text="Key (Hex):")
key_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")
key_entry = ttk.Entry(input_frame)
key_entry.grid(row=1, column=1, padx=10, pady=10)

# Tombol Enkripsi, Dekripsi, dan Reset
button_frame = ttk.Frame(window)
button_frame.pack(pady=10)  # Padding atas 10

reset_button = ttk.Button(button_frame, text="Reset", command=reset_fields)
reset_button.grid(row=0, column=0, padx=10, pady=10)

decrypt_button = ttk.Button(button_frame, text="Dekripsi", command=decrypt_text)
decrypt_button.grid(row=0, column=1, padx=10, pady=10)

encrypt_button = ttk.Button(button_frame, text="Enkripsi", command=encrypt_text)
encrypt_button.grid(row=0, column=2, padx=10, pady=10)

# Frame untuk teks hasil enkripsi/dekripsi dalam format heksadesimal
hex_output_frame = ttk.Frame(window)
hex_output_frame.pack(pady=10)  # Padding atas 10

hex_output_label = ttk.Label(hex_output_frame, text="Hasil (Heksadesimal):")
hex_output_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

hex_output_entry = ttk.Entry(hex_output_frame)
hex_output_entry.grid(row=0, column=1, padx=10, pady=10)

# Frame untuk teks hasil enkripsi/dekripsi dalam format biner
bin_output_frame = ttk.Frame(window)
bin_output_frame.pack(pady=10)  # Padding atas 10

# Menambahkan border dan relief pada frame hasil biner
bin_output_frame["borderwidth"] = 1  # Lebar border
bin_output_frame["relief"] = "solid"  # Jenis relief

# Text untuk menampilkan hasil biner dalam frame dengan gaya khusus
# Text untuk menampilkan hasil biner dalam frame dengan gaya khusus
bin_output_text = ttk.Label(bin_output_frame, font=("Arial", 10, "bold"), text=" 🔑 ", anchor="center", style="Custom.TLabel", foreground="#000000")  # Ubah warna font ke hijau gelap dan buat teks tebal
bin_output_text.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")  # Gunakan sticky="nsew"

# Agar label "Hasil Biner" dan hasil biner berada di tengah secara horizontal dan vertikal
bin_output_frame.grid_rowconfigure(0, weight=1)
bin_output_frame.grid_columnconfigure(0, weight=1)


# Buat frame untuk tombol Salin
button_frame = ttk.Frame(window)
button_frame.pack(pady=10)

# Menghide tombol Salin
def hide_copy_button():
    if not encryption_done:
        copy_button.config(state=tk.DISABLED)  # Menonaktifkan tombol "Salin"
    else:
        copy_button.config(state=tk.NORMAL)  # Mengaktifkan kembali tombol "Salin"

# Menambahkan tombol Salin
def copy_to_clipboard():
    binary_result = bin_output_text["text"]
    # Menghapus clipboard sebelum menyalin
    window.clipboard_clear()
    # Menyalin teks ke clipboard
    window.clipboard_append(binary_result)
    # Menyimpan perubahan ke clipboard
    window.update()
    
    # Menampilkan pesan berhasil disalin ke clipboard
    messagebox.showinfo("Info", "Teks berhasil disalin ke clipboard")

copy_button = ttk.Button(button_frame, text="Salin", command=copy_to_clipboard)
copy_button.grid(row=0, column=0, padx=10)

# Atur ukuran maksimum frame
bin_output_frame.grid_propagate(False)  # Mencegah frame menyesuaikan ukuran dengan kontennya
bin_output_frame.config(width=270, height=90)  # Sesuaikan ukuran maksimum frame sesuai kebutuhan

# Fungsi untuk mengaktifkan atau menonaktifkan opsi "Debug Result"
def toggle_debug_option():
    global debug_option_enabled
    debug_option_enabled = not debug_option_enabled
    if debug_option_enabled:
        file_menu.entryconfig("Debug Result", state=tk.NORMAL)
    else:
        file_menu.entryconfig("Debug Result", state=tk.DISABLED)

# Inisialisasi variabel untuk melacak hasil cetak debug yang telah dilakukan
printed_debug_results = set()

# Variabel global untuk menyimpan hasil debug
debug_results = []

# Inisialisasi variabel debug_text_widget
debug_text_widget = None

# Fungsi untuk membuka jendela debug
def open_debug_result(debug_text):
    global debug_window, debug_text_widget  # Menetapkan variabel global
    debug_window = None  # Inisialisasi variabel debug_window

    if debug_window is not None:
        # Jika jendela debug sudah ada, tutup terlebih dahulu
        debug_window.destroy()

    # Buat jendela debug baru
    debug_window = tk.Toplevel(window)
    debug_window.title("Debug Result")  # Menetapkan judul jendela debug

    # Atur ukuran jendela debug (misalnya, 1000x600 piksel)
    debug_window.geometry("1200x600")

    # Mendapatkan ukuran layar
    screen_width = debug_window.winfo_screenwidth()
    screen_height = debug_window.winfo_screenheight()

    # Menghitung posisi x dan y untuk memusatkan jendela
    x = (screen_width - 1200) // 2
    y = (screen_height - 600) // 2

    # Menetapkan posisi jendela di tengah
    debug_window.geometry(f"1200x600+{x}+{y}")

    # Buat widget teks di jendela debug dengan wrap teks
    global debug_text_widget  # Jadikan debug_text_widget sebagai variabel global
    debug_text_widget = scrolledtext.ScrolledText(debug_window, wrap=tk.WORD)
    debug_text_widget.pack(fill=tk.BOTH, expand=True)  # Mengisi dan memperluas widget ke seluruh jendela

    # Tampilkan hasil debug dalam widget teks
    debug_text_widget.insert(tk.END, debug_text)  # Menyisipkan teks debug ke dalam widget teks

    # Buat menu bar
    menubar = Menu(debug_window)
    debug_window.config(menu=menubar)

    # Buat menu "File"
    file_menu = Menu(menubar, tearoff=0)
    menubar.add_cascade(label="File", menu=file_menu)

    # Tambahkan opsi "Save" ke menu "File"
    file_menu.add_command(label="Save", command=save_debug_text)

    # Tambahkan opsi "Exit" ke menu "File"
    file_menu.add_command(label="Exit", command=close_debug_window)

# Fungsi untuk menutup jendela debug
def close_debug_window():
    global debug_window
    if debug_window is not None:
        debug_window.destroy()

# Fungsi untuk menyimpan teks debug ke file
def save_debug_text():
    global debug_text_widget  # Jadikan debug_text_widget sebagai variabel global
    if debug_text_widget is not None:
        # Mendapatkan teks dari widget teks
        debug_text = debug_text_widget.get("1.0", tk.END)

        # Munculkan dialog penyimpanan file
        file_path = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text files", "*.txt"), ("All files", "*.*")],
        )

        if file_path:
            # Menyimpan teks ke file yang dipilih
            with open(file_path, "w") as file:
                file.write(debug_text)

# Fungsi untuk menggabungkan hasil debug dari berbagai bagian fungsi enkripsi
def handle_debug_result():
    global debug_results  # Tambahkan variabel global

    key = key_entry.get()  # Ambil kunci dari kotak input
    if not key:
        messagebox.showerror("Error", "Jalankan Enkripsi atau Dekripsi sebelum mengklik Debug Result.")
        return  # Keluar dari fungsi jika kunci kosong

    # Membuat teks hasil debug
    debug_result = []
    debug_result.append("Hasil Debug:")

    # Tambahkan hasil debug dari berbagai bagian fungsi enkripsi ke dalam daftar debug_result
    debug_result.extend(debug_results)

    # Menggabungkan hasil debug menjadi satu string
    debug_text = "\n".join(debug_result)

    # Menampilkan hasil debug di jendela debug
    open_debug_result(debug_text)

# Fungsi untuk keluar dari aplikasi
def exit_app():
    window.quit()

def show_about_info():
    # Gunakan teks judul jendela dan versi aplikasi untuk mengatur teks keterangan
    window_title = window.title()
    email = "imamsyt22@mhs.usk.ac.id"  # Ganti dengan alamat email Anda
    about_info = f"{window_title}\nVersi {app_version}\n\nDikembangkan oleh [Bukan Makmum]\nEmail: {email}"
    result = messagebox.showinfo("About", about_info, icon=messagebox.INFO)
    if result:
        open_github()

def open_github():
    webbrowser.open("https://github.com/BukanMakmum/DataEncryptionStandard.git")  # Ganti dengan URL repositori GitHub Anda

# Membuat objek menu utama
menubar = tk.Menu(window)
window.config(menu=menubar)

# Membuat menu "File" tanpa garis putus-putus
file_menu = tk.Menu(menubar, tearoff=False)
menubar.add_cascade(label="File", menu=file_menu)

# Menambahkan opsi "Debug Result" di menu "File" dan menonaktifkannya saat pertama kali dibuat
file_menu.add_command(label="Debug Result", command=handle_debug_result, state=tk.DISABLED)

# Menambahkan opsi "Exit" di menu "File" tanpa garis pemisah
file_menu.add_command(label="Exit", command=exit_app)

# Menambahkan opsi "About" di menu utama
menubar.add_command(label="About", command=show_about_info)

# Menambahkan keterangan hak cipta di tengah bawah
copyright_label = ttk.Label(window, text="© 2023 BukanMakmum.", font=("Helvetica", 8, "bold"), foreground="grey", cursor="hand2")
copyright_label.pack(side=tk.BOTTOM, pady=(0, 10), fill=tk.X)

# Mengatur teks hak cipta menjadi rata tengah horizontal
copyright_label.configure(anchor="center", justify="center")

def open_email(event):
    webbrowser.open("mailto:imamsayuti.usk@gmail.com")

# Menghubungkan fungsi dengan klik pada teks hak cipta
copyright_label.bind("<Button-1>", open_email)

# Memanggil fungsi untuk menonaktifkan tombol "Salin" pada awalnya
hide_copy_button()
toggle_debug_option()

# Memulai aplikasi
window.mainloop()