# aplikasi kalkulator sederhana
# dengan module Tkinter

import tkinter as tk

kalkulasi = ""

# fungsi untuk kalkulasi dan perhitungan
def tambah_ke_kalkulasi(simbol):
	global kalkulasi
	kalkulasi += str(simbol)
	text_result.delete(1.0, "end")
	text_result.insert(1.0, kalkulasi)

def evaluasi_kalkulasi():
	global kalkulasi
	try:
		kalkulasi = str(eval(kalkulasi))
		text_result.delete(1.0, "end")
		text_result.insert(1.0, kalkulasi)
	except:
		bersih_teks()
		text_result.insert(1.0, "Error")

def bersih_teks():
	global kalkulasi
	kalkulasi = ""
	text_result.delete(1.0, "end")

# jendela aplikasi
root = tk.Tk()
root.title("Calculator")
root.geometry("532x425")

# kolom teks untuk menampilkan hasil dan input
text_result = tk.Text(root, height=2, width=24, font=("Arial", 30))
text_result.grid(columnspan=5)

# tombol
tmb_1 = tk.Button(root, text="1", command= lambda : tambah_ke_kalkulasi(1), width=12,height=2, font=("Arial", 14))
tmb_1.grid(row=2, column=1)
tmb_2 = tk.Button(root, text="2", command= lambda : tambah_ke_kalkulasi(2), width=12,height=2, font=("Arial", 14))
tmb_2.grid(row=2, column=2)
tmb_3 = tk.Button(root, text="3", command= lambda : tambah_ke_kalkulasi(3), width=12,height=2, font=("Arial", 14))
tmb_3.grid(row=2, column=3)
tmb_3 = tk.Button(root, text="4", command= lambda : tambah_ke_kalkulasi(4), width=12,height=2, font=("Arial", 14))
tmb_3.grid(row=3, column=1)
tmb_3 = tk.Button(root, text="5", command= lambda : tambah_ke_kalkulasi(5), width=12,height=2, font=("Arial", 14))
tmb_3.grid(row=3, column=2)
tmb_3 = tk.Button(root, text="6", command= lambda : tambah_ke_kalkulasi(6), width=12,height=2, font=("Arial", 14))
tmb_3.grid(row=3, column=3)
tmb_3 = tk.Button(root, text="7", command= lambda : tambah_ke_kalkulasi(7), width=12,height=2, font=("Arial", 14))
tmb_3.grid(row=4, column=1)
tmb_3 = tk.Button(root, text="8", command= lambda : tambah_ke_kalkulasi(8), width=12,height=2, font=("Arial", 14))
tmb_3.grid(row=4, column=2)
tmb_3 = tk.Button(root, text="9", command= lambda : tambah_ke_kalkulasi(9), width=12,height=2, font=("Arial", 14))
tmb_3.grid(row=4, column=3)
tmb_3 = tk.Button(root, text="0", command= lambda : tambah_ke_kalkulasi(0), width=12,height=2, font=("Arial", 14))
tmb_3.grid(row=5, column=2)

# simbol aritmatika
tmb_tambah = tk.Button(root, text="+", command= lambda : tambah_ke_kalkulasi("+"), width=8,height=2, font=("Arial", 14))
tmb_tambah.grid(row=2, column=4)
tmb_kurang = tk.Button(root, text="-", command= lambda : tambah_ke_kalkulasi("-"), width=8,height=2, font=("Arial", 14))
tmb_kurang.grid(row=3, column=4)
tmb_kali = tk.Button(root, text="x", command= lambda : tambah_ke_kalkulasi("*"), width=8,height=2, font=("Arial", 14))
tmb_kali.grid(row=4, column=4)
tmb_bagi = tk.Button(root, text="/", command= lambda : tambah_ke_kalkulasi("/"), width=8,height=2, font=("Arial", 14))
tmb_bagi.grid(row=5, column=4)
tmb_kur1 = tk.Button(root, text="(", command= lambda : tambah_ke_kalkulasi("("), width=12,height=2, font=("Arial", 14))
tmb_kur1.grid(row=5, column=1)
tmb_kur2 = tk.Button(root, text=")", command= lambda : tambah_ke_kalkulasi(")"), width=12,height=2, font=("Arial", 14))
tmb_kur2.grid(row=5, column=3)

# tomboh hasil perhitungan
tmb_bersih = tk.Button(root, text="C", command=bersih_teks, width=25,height=3, font=("Arial", 14))
tmb_bersih.grid(row=6, column=1, columnspan=2)
tmb_sama_dengan = tk.Button(root, text="=", command=evaluasi_kalkulasi,height=3, width=21, font=("Arial", 14))
tmb_sama_dengan.grid(row=6, column=3, columnspan=2)

root.mainloop()