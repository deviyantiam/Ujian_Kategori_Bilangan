'''
jika berdasarkan soal, bilangan ganjil dan genap adalah bilangan asli,
maka bilangan negatif tidak termasuk genap ataupun ganjil
'''
bil=int(input('\nKetik angka : '))
def tipe(angka):
    s='bulat ' #karena inputnya sudah bilangan bulat, maka angka otomatis termasuk bilangan bulat
    y=0 #untuk menyimpan bilangan prima
    if angka<0:
        s+='negatif '
    else:
        s+='cacah '
        if angka==0:
            s+='nol '
        else:
            s+='asli '
            if angka%2==0:
                s+='genap '
            else:
                s+='ganjil '
            if angka>1:
                for i in range(2,angka): #dibagi mulai dari 2
                    if angka%i==0: #jika dibagi suatu bilangan tidak ada sisa, maka lanjut
                        y=0
                        break
                    else:
                        y=angka
                if y==0:
                    s+='komposit '
                else:
                    s+='prima '
    pj=len(s)
    sbaru=s[0:(pj-1)] #hapus spasi terakhir kalau tidak, list element terakhir adalah ''
    hasil=sbaru.split(' ')
    return hasil
print(tipe(bil))

                