
import tkinter as tk
from tkinter import messagebox

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

# Membuat jendela GUI
window = tk.Tk()
window.title("Manhattan Similarity")
window.geometry("300x200")

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

# Membuat tombol untuk menghitung kesamaan
calculate_button = tk.Button(window, text="Hitung Similaritas", command=calculate_similarity)
calculate_button.pack()

# Menjalankan jendela GUI
window.mainloop()
