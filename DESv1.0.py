import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from ttkthemes import ThemedStyle
# Fungsi untuk mengarahkan ke alamat email saat teks hak cipta diklik
import webbrowser

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
    global PC1, PC2, ShiftBits

    key_bin = bin(int(key, 16))[2:].zfill(64)

    # Lakukan "parity bit drop" sesuai dengan deskripsi yang Anda berikan
    key_parity_dropped = ''.join(key_bin[i] for i in range(64) if (i + 1) % 8 != 0)

    # Lakukan permutasi sesuai dengan tabel PC1 yang telah didefinisikan
    key_permuted = permute(key_bin, PC1)

    left_key, right_key = key_permuted[:28], key_permuted[28:]
    subkeys = []

    for round_num, shift_amount in enumerate(ShiftBits, start=1):
        left_key = left_shift(left_key, shift_amount)
        right_key = left_shift(right_key, shift_amount)

        subkey = permute(left_key + right_key, PC2)
        subkeys.append(subkey)

    return subkeys

# Fungsi untuk melakukan enkripsi dengan algoritma DES
def encrypt(data, subkeys):
    data_bin = bin(int(data, 16))[2:].zfill(64)
    data_permuted = permute(data_bin, IP)
    
    left_half = data_permuted[:32]
    right_half = data_permuted[32:]

    for i in range(16):
        subkey = subkeys[i]
        right_expanded = permute(right_half, EBox)
        right_xor = bin(int(right_expanded, 2) ^ int(subkey, 2))[2:].zfill(48)
        sbox_output = ""
        
        for j in range(8):
            sbox_input = right_xor[j * 6: (j + 1) * 6]
            row = int(sbox_input[0] + sbox_input[5], 2)
            col = int(sbox_input[1:5], 2)
            sbox_value = SBox[j][row * 16 + col]
            sbox_output += format(sbox_value, '04b')
        
        right_permuted = permute(sbox_output, PBox)
        right_xor = bin(int(left_half, 2) ^ int(right_permuted, 2))[2:].zfill(32)
        left_half = right_half
        right_half = right_xor

    combined = right_half + left_half
    ciphertext = permute(combined, FP)
    
    return ciphertext

# Fungsi untuk melakukan dekripsi dengan algoritma DES
def decrypt(data, subkeys):
    data_bin = bin(int(data, 16))[2:].zfill(64)
    data_permuted = permute(data_bin, IP)
    
    left_half = data_permuted[:32]
    right_half = data_permuted[32:]

    for i in range(16):
        subkey = subkeys[15 - i]
        right_expanded = permute(right_half, EBox)
        right_xor = bin(int(right_expanded, 2) ^ int(subkey, 2))[2:].zfill(48)
        sbox_output = ""
        
        for j in range(8):
            sbox_input = right_xor[j * 6: (j + 1) * 6]
            row = int(sbox_input[0] + sbox_input[5], 2)
            col = int(sbox_input[1:5], 2)
            sbox_value = SBox[j][row * 16 + col]
            sbox_output += format(sbox_value, '04b')
        
        right_permuted = permute(sbox_output, PBox)
        right_xor = bin(int(left_half, 2) ^ int(right_permuted, 2))[2:].zfill(32)
        left_half = right_half
        right_half = right_xor

    combined = right_half + left_half
    plaintext = permute(combined, FP)
    
    return plaintext

# Fungsi untuk mendekripsi teks saat tombol "Enkripsi" ditekan
def encrypt_text():
    global encryption_done

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
        
        subkeys = generate_subkeys(input_key)
        ciphertext_bin = encrypt(input_text_hex, subkeys)

        formatted_ciphertext = '\n'.join([' '.join(ciphertext_bin[i:i+4] for i in range(j, j+16, 4)) for j in range(0, len(ciphertext_bin), 16)])

        bin_output_text["text"] = formatted_ciphertext

        ciphertext_hex = hex(int(ciphertext_bin, 2))[2:].upper().zfill(16)

        hex_output_entry.delete(0, tk.END)
        hex_output_entry.insert(0, ciphertext_hex)

        encryption_done = True  # Mengatur encryption_done menjadi True setelah enkripsi selesai
        hide_copy_button()  # Memanggil fungsi hide_copy_button() untuk mengaktifkan tombol "Salin"

    except Exception as e:
        messagebox.showerror("Error", f"Terjadi kesalahan: {str(e)}")

# Fungsi untuk mendekripsi teks saat tombol "Dekripsi" ditekan
def decrypt_text():
    global encryption_done

    encryption_done = True
    copy_button.config(state="disabled")
    input_key = key_entry.get()
    ciphertext_hex = input_entry.get()

    try:
        if not all(c in "0123456789ABCDEF" for c in input_key) or len(input_key) != 16:
            messagebox.showerror("Error", "Key harus berupa 16 karakter heksadesimal")
            return

        if not all(c in "0123456789ABCDEF" for c in ciphertext_hex) or len(ciphertext_hex) != 16:
            messagebox.showerror("Error", "Ciphertext harus berupa 16 karakter heksadesimal")
            return

        subkeys = generate_subkeys(input_key)
        plaintext_bin = decrypt(ciphertext_hex, subkeys)

        formatted_plaintext = '\n'.join([plaintext_bin[i:i+4] + ' ' + plaintext_bin[i+4:i+8] + ' ' + plaintext_bin[i+8:i+12] + ' ' + plaintext_bin[i+12:i+16] for i in range(0, len(plaintext_bin), 16)])

        bin_output_text["text"] = formatted_plaintext

        plaintext_hex = hex(int(plaintext_bin, 2))[2:].upper().zfill(16)

        hex_output_entry.delete(0, tk.END)
        hex_output_entry.insert(0, plaintext_hex)

        encryption_done = True  # Mengatur encryption_done menjadi True setelah enkripsi selesai
        hide_copy_button()  # Memanggil fungsi hide_copy_button() untuk mengaktifkan tombol "Salin"

    except Exception as e:
        messagebox.showerror("Error", f"Terjadi kesalahan: {str(e)}")

# Fungsi untuk mereset input dan output
def reset_fields():
    copy_button.config(state="disabled")
    input_entry.delete(0, tk.END)
    key_entry.delete(0, tk.END)
    hex_output_entry.delete(0, tk.END)
    bin_output_text["text"] = ""

# Fungsi untuk mengatur jendela di tengah layar
def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    
    window.geometry(f"{width}x{height}+{x}+{y}")

# Membuat jendela tkinter
window = tk.Tk()
window.title("Data Encryption Standar")

# Mengatur ukuran jendela
window_width = 350
window_height = 500

# Variabel global
encryption_done = False  # Inisialisasi variabel encryption_done

# Menyimpan jendela di tengah layar
center_window(window, window_width, window_height)

# Menggunakan tema modern
style = ThemedStyle(window)
style.set_theme("plastik")

# Versi aplikasi
app_version = "Education 1.0"

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
label_frame = ttk.Frame(window)
label_frame.pack(pady=0)  # Padding atas 10

# Atur warna font dan huruf tebal dalam gaya
style.configure("Bold.TLabel", font=("Arial", 10, "bold"), foreground="black")

# Label untuk hasil
result_label = ttk.Label(label_frame, text="Hasil Biner", font=("Arial", 10), style="Bold.TLabel")
result_label.grid(row=0, column=0, padx=0, pady=0, sticky="nsew")

# Frame untuk teks hasil enkripsi/dekripsi dalam format biner
bin_output_frame = ttk.Frame(window)
bin_output_frame.pack(pady=10)  # Padding atas 10

# Atur gaya dengan latar belakang yang berbeda
style.configure("Custom.TLabel", background="#FFFFFF")  # Ganti "#FFFFFF" dengan warna latar belakang yang Anda inginkan

# Text untuk menampilkan hasil biner dalam frame dengan gaya khusus
bin_output_text = ttk.Label(bin_output_frame, font=("Arial", 10), text=" 🔑 ", anchor="center", style="Custom.TLabel")
bin_output_text.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")  # Gunakan sticky="nsew"

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

#Dilarang hapus, sesama pengembang/pemrograman/mahasiswa/sarjana harus saling menghargai karya orang lain!
copyright_label = ttk.Label(window, text="© 2023 BukanMakmum.", font=("Helvetica", 8, "bold"), foreground="grey", cursor="hand2")
copyright_label.pack(side=tk.BOTTOM, pady=(0, 10), fill=tk.X)
#Jika ingin berkontribusi silakan Clone Github berikut https://github.com/BukanMakmum/DataEncryptionStandard.git
#User sangat menghargai kontribusi Anda, dengan menampilkan profil di halaman kontribusi. 
# Mengatur teks hak cipta menjadi rata tengah horizontal
copyright_label.configure(anchor="center", justify="center")

def open_email(event):
    webbrowser.open("mailto:imamsyt22@mhs.usk.ac.id")

# Menghubungkan fungsi dengan klik pada teks hak cipta
copyright_label.bind("<Button-1>", open_email)

# Memanggil fungsi untuk menonaktifkan tombol "Salin" pada awalnya
hide_copy_button()

# Memulai aplikasi
window.mainloop()