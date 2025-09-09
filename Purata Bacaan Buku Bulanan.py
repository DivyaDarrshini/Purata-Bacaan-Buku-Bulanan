from tkinter import *

fields = ('Bilangan Buku', 'Bilangan Hari')

def purata(entries):
    x = int(entries['Bilangan Buku'].get())
    y = int(entries['Bilangan Hari'].get())

    if x < 1:
        print("Masukkan bilangan buku melebihi 1")

    if 29 > y or 31 < y:
        print("Masukkan bilangan hari antara 29 hingga 31")

    elif y == 29 or 30 or 31:
        z = x / y
        a = round(z, 2)
        purata = print("Purata Bacaan Buku pada Setiap Bulan:", a)

        if a > 5:
            print("Tahap IQ: Lebih daripada 140")
            print("Kelasifikasi: Pintar")

        elif 4 <= a <= 5:
            print("Tahap IQ: 120 hingga 140")
            print("Kelasifikasi: Baik")

        elif 3 <= a <= 4:
            print("Tahap IQ: 110 hingga 120")
            print("Kelasifikasi: Sederhana")

        elif 2 <= a <= 3:
            print("Tahap IQ: 90 hingga 110")
            print("Kelasifikasi: Memuaskan")

        elif 1 <= a <= 2:
            print("Tahap IQ: 80 hingga 90")
            print("Kelasifikasi: Kurang memuaskan")

        else:
            print("Tahap IQ: Kurang daripada 80")
            print("Kelasifikasi: Tidak memuaskan")

def makeform(root, fields):
    entries = {}
    for field in fields:
        row = Frame(root)
        lab = Label(row, width=22, text=field+": ", anchor='w')
        ent = Entry(row)
        ent.insert(0, "0")
        row.pack(side=TOP, fill=X, padx=5, pady=5)
        lab.pack(side=LEFT)
        ent.pack(side=RIGHT, expand=YES, fill=X)
        entries[field] = ent
    return entries

if __name__ == '__main__':
    root = Tk()
    root.title("Pengiraan Purata Bacaan Buku pada Setiap Bulan")
    ents = makeform(root, fields)
    root.bind('<Return>', (lambda event, e=ents: purata(e)))
    bl = Button(root, text='Kira', command=(lambda e=ents: purata(e)))
    bl.pack(side=LEFT, padx=5, pady=5)
    root.mainloop()
