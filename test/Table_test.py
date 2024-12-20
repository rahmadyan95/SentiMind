import customtkinter as ctk

# Fungsi untuk membuat tabel
def create_table(root, data):
    # Buat frame untuk tabel
    frame = ctk.CTkFrame(root)
    frame.pack(padx=10, pady=10)

    # Iterasi untuk menambahkan label sebagai header
    for col_num, col_name in enumerate(data[0]):
        header = ctk.CTkLabel(frame, text=col_name, width=20, height=2, corner_radius=5)
        header.grid(row=0, column=col_num, padx=5, pady=5)

    # Iterasi untuk menambahkan data tabel
    for row_num, row_data in enumerate(data[1:], start=1):
        for col_num, cell_data in enumerate(row_data):
            cell = ctk.CTkLabel(frame, text=cell_data, width=20, height=2, corner_radius=5)
            cell.grid(row=row_num, column=col_num, padx=5, pady=5)

# Buat data tabel (header dan data)
data = [
    ["No", "Nama", "Usia"],
    [1, "Ali", 30],
    [2, "Budi", 25],
    [3, "Cici", 28]
]

# Inisialisasi aplikasi
root = ctk.CTk()
root.title("Tabel dengan customtkinter")
root.geometry("300x200")

# Panggil fungsi untuk membuat tabel
create_table(root, data)

# Jalankan aplikasi
root.mainloop()
