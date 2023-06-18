import tkinter as tk
from tkinter import messagebox, filedialog
import csv

def manhattan_similarity(vector1, vector2):
    # Pastikan kedua vektor memiliki panjang yang sama
    if len(vector1) != len(vector2):
        raise ValueError("Panjang vektor tidak sama")

    # Hitung selisih absolut dari setiap elemen vektor dan jumlahkan
    distance = sum(abs(x - y) for x, y in zip(vector1, vector2))
    similarity = 1 / (1 + distance)
    return distance, similarity

def calculate_similarity():
    try:
        # Memperoleh vektor a dan b dari input pengguna
        vector_a = list(map(int, entry_a.get().split(",")))
        vector_b = list(map(int, entry_b.get().split(",")))

        # Memastikan kedua vektor memiliki panjang yang sama
        if len(vector_a) != len(vector_b):
            raise ValueError("Panjang vektor tidak sama")

        # Menghitung jarak dan kesamaan menggunakan fungsi manhattan_similarity
        distance, similarity = manhattan_similarity(vector_a, vector_b)

        # Menampilkan hasil pada messagebox
        messagebox.showinfo("Hasil", f"Distance: {distance}\nSimilarity Score: {similarity}")

    except Exception as e:
        messagebox.showerror("Error", str(e))

def reset_fields():
    entry_a.delete(0, tk.END)
    entry_b.delete(0, tk.END)

def browse_csv():
    global csv_file
    csv_file = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
    if csv_file:
        messagebox.showinfo("Info", f"File CSV yang dipilih: {csv_file}")
        load_csv_data()

def load_csv_data():
    try:
        with open(csv_file, "r") as file:
            reader = csv.reader(file)
            data = list(reader)

            if len(data) >= 2:
                vector_a = list(map(str, data[0]))
                vector_b = list(map(str, data[1]))

                entry_a.delete(0, tk.END)
                entry_a.insert(tk.END, ",".join(vector_a))

                entry_b.delete(0, tk.END)
                entry_b.insert(tk.END, ",".join(vector_b))
            else:
                raise ValueError("Data vektor tidak lengkap dalam file CSV")

    except Exception as e:
        messagebox.showerror("Error", str(e))

def go_back():
    window.destroy()

# Membuat jendela GUI
window = tk.Tk()
window.title("Manhattan Similarity")
window.geometry("300x250")

# Membuat label dan entry untuk vektor a
label_a = tk.Label(window, text="Vektor a:")
label_a.pack()
entry_a = tk.Entry(window)
entry_a.pack()

# Membuat label dan entry untuk vektor b
label_b = tk.Label(window, text="Vektor b:")
label_b.pack()
entry_b = tk.Entry(window)
entry_b.pack()

# Membuat frame untuk tombol
button_frame = tk.Frame(window)
button_frame.pack()

# Membuat tombol untuk memilih file CSV
browse_button = tk.Button(button_frame, text="Pilih File CSV", command=browse_csv)
browse_button.pack(side=tk.LEFT)

# Membuat tombol untuk menghitung kesamaan
calculate_button = tk.Button(button_frame, text="Hitung Similaritas", command=calculate_similarity)
calculate_button.pack(side=tk.LEFT)

# Membuat tombol reset
reset_button = tk.Button(button_frame, text="Reset", command=reset_fields)
reset_button.pack(side=tk.LEFT)

# Membuat tombol back
back_button = tk.Button(window, text="Back", command=go_back)
back_button.pack(pady=10)

# Menjalankan jendela GUI
window.mainloop()