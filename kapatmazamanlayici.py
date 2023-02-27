import os
from tkinter import *
from time import *
from datetime import *

# x = datetime.now()
# print(x.strftime("%X"))


pencere = Tk()
pencere.title("Kaptma Zamanlayici")
pencere.iconbitmap("kapat2.ico")
pencere.geometry('430x180')
pencere.resizable(width=False, height=False)

def onbesd():
    os.system("shutdown /s /t 900")
    surebelirtiniz.config(text="")

def otuzd():
    os.system("shutdown /s /t 1800")
    surebelirtiniz.config(text="")   

def kirkbesd():
    os.system("shutdown /s /t 2700")
    surebelirtiniz.config(text="")
def birsaats():
    os.system("shutdown /s /t 3600")
    surebelirtiniz.config(text="")
def belirled():
    surebelirtiniz.config(text="")    
    saatdonustur=saatgir.get()
    saat2cagir=saatgir2.get()    
    dakikadonustur=dakikagir.get()
    dakika2cagir=dakikagir2.get()
    saniyedonustur=saniyegir.get()
    saatdonusmus=int(saatdonustur)
    saatformul=saatdonusmus*3600
    dakikadonusmus=int(dakikadonustur)
    dakikaformul=dakikadonusmus*60 
    saniyedonsumus=int(saniyedonustur)
    saniyeformul=saniyedonsumus*1
    if not(saatdonustur=='0') and not(dakikadonustur=='0') and not(saniyedonustur=='0'):
        sonformul=(saatformul+dakikaformul+saniyeformul)
        os.system(f"shutdown /s /t {sonformul}")    
    elif (not saatdonustur=='0') and not(dakikadonustur=='0') and (saniyedonustur=='0'):
        saatdakikaformul=saatformul+dakikaformul
        os.system(f"shutdown /s /t {saatdakikaformul}")
    elif(not saatdonustur=='0') and (dakikadonustur=='0') and (saniyedonustur=='0'):
        os.system(f"shutdown /s /t {saatformul}")
    elif(saatdonustur=='0') and (dakikadonustur=='0') and (saniyedonustur=='0') and (saat2cagir=='0') and (dakika2cagir=='0'):
        surebelirtiniz.config(text='Lütfen Bir Süre Belirtiniz')
    elif(saatdonustur=='0') and (not dakikadonustur=='0') and (saniyedonustur=='0'):
        os.system(f"shutdown /s /t {dakikaformul}")
    elif(saatdonustur=='0') and (not dakikadonustur=='0') and (not saniyedonustur=='0'):
        dsformul=(dakikaformul+saniyeformul)
        os.system(f"shutdown /s /t {dsformul}")
    elif(not saatdonustur=='0') and (dakikadonustur=='0') and (not saniyedonustur=='0'):
        saatsaniyeformul=saatformul+saniyeformul
        os.system(f"shutdown /s /t {saatsaniyeformul}")
    elif(saatdonustur=='0') and (dakikadonustur=='0') and (not saniyedonustur=='0'):
        os.system(f"shutdown /s /t {saniyeformul}")
    #--------------------------------------------
    saat2cagir=saatgir2.get()
    saat2cc=int(saat2cagir)
    dakika2cagir=dakikagir2.get()
    dakika2cc=int(dakika2cagir)
    # saniye2cagir=saniyegir2.get()
    # saniye2cc=int(saniye2cagir)
    simdikisaat = datetime.now()
    simdikisaatsss=(simdikisaat.strftime("%X"))
    saatcevir=simdikisaatsss[0:2]
    saatcevir2=int(saatcevir)
    dakikacevir=simdikisaatsss[3:5]
    dakikacevir2=int(dakikacevir)
    # saniyecevir=simdikisaatsss[5:0]
    # saniyecevir2=int(saniyecevir)
    zaman1 = timedelta(hours=saatcevir2, minutes=dakikacevir2)
    zaman2 = timedelta(hours=saat2cc, minutes=dakika2cc)
    formul=zaman2-zaman1
    formulcevir=str(formul)
    formulal=formulcevir[0]
    formulalc=int(formulal)
    formulal2=formulcevir[2:4]
    formulal2c=int(formulal2)
    # formulal3=formulcevir[4:1]
    # formulal3c=int(formulal3)
    saatsaniye=formulalc*3600
    dakikasaniye=formulal2c*60
    sonformul=saatsaniye+dakikasaniye
    os.system(f"shutdown /s /t {sonformul}")


def sayaclikapat():
    saat2cagir=saatgir2.get()
    dakika2cagir=dakikagir2.get()
    if saat2cagir=="0" and dakika2cagir=="0":
        surebelirtiniz.config(text="""Lütfen Saat ve Dakika 
Belirtiniz""")
    else:
        surebelirtiniz.config(text="") 

    saat2cc=int(saat2cagir)
    dakika2cc=int(dakika2cagir)
    # saniye2cagir=saniyegir2.get()
    # saniye2cc=int(saniye2cagir)
    simdikisaat = datetime.now()
    simdikisaatsss=(simdikisaat.strftime("%X"))
    saatcevir=simdikisaatsss[0:2]
    saatcevir2=int(saatcevir)
    dakikacevir=simdikisaatsss[3:5]
    dakikacevir2=int(dakikacevir)
    # saniyecevir=simdikisaatsss[5:0]
    # saniyecevir2=int(saniyecevir)
    zaman1 = timedelta(hours=saatcevir2, minutes=dakikacevir2)
    zaman2 = timedelta(hours=saat2cc, minutes=dakika2cc)
    formul=zaman2-zaman1
    formulcevir=str(formul)
    formulal=formulcevir[0]
    formulalc=int(formulal)
    formulal2=formulcevir[2:4]
    formulal2c=int(formulal2)
    # formulal3=formulcevir[4:1]
    # formulal3c=int(formulal3)
    saatsaniye=formulalc*3600
    dakikasaniye=formulal2c*60
    sonformul=saatsaniye+dakikasaniye
    os.system(f"shutdown /s /t {sonformul}")

def durdur():
    os.system("shutdown -a")
    surebelirtiniz.config(text=f"""Oturum Kapatma İptal
    Edildi""")

onbes=Button(pencere, activeforeground= "red")
onbes.place(x=20,y=15,height=50, width=50)
onbes.config(text='15', command=onbesd,font="Arial 18")

otuz=Button(pencere, activeforeground= "red")
otuz.place(x=80,y=15,height=50, width=50)
otuz.config(text='30', command=otuzd,font="Arial 18")

kirkbes=Button(pencere, activeforeground= "red")
kirkbes.place(x=140,y=15,height=50, width=50)
kirkbes.config(text='45', command=kirkbesd,font="Arial 18")

birsaat=Button(pencere, activeforeground= "red")
birsaat.place(x=200,y=15,height=50, width=50)
birsaat.config(text='60', command=birsaats,font="Arial 18")

baslat=Button(pencere, activeforeground= "red")
baslat.place(x=25,y=105,height=30, width=185)
baslat.config(text='Başlat', command=belirled,font="Arial 15")

durdurb=Button(pencere, activeforeground= "red")
durdurb.place(x=25,y=140,height=30, width=185)
durdurb.config(text='Durdur', command=durdur,font="Arial 15")

surebelirle=Label(pencere)
surebelirle.config(text='Süre Giriniz(Saat:Dakika:Saniye):', font=("Vertana",14))
surebelirle.place(x=25, y=75)

saat=StringVar()
saat.set("0")
saatgir=Entry(pencere,textvariable=saat)
saatgir.pack()
saatgir.place(x=309, y=79,height=22,width=17)

ikin1=Label(pencere)
ikin1.pack()
ikin1.place(x=325,y=75)
ikin1.config(text=':', font=("Vertana",14))

dakika=StringVar()
dakika.set("0")
dakikagir=Entry(pencere,textvariable=dakika)
dakikagir.pack()
dakikagir.place(x=337, y=79,height=22,width=17)

ikin2=Label(pencere)
ikin2.pack()
ikin2.place(x=353,y=75)
ikin2.config(text=':', font=("Vertana",14))

saniye=StringVar()
saniye.set("0")
saniyegir=Entry(pencere,textvariable=saniye)
saniyegir.pack()
saniyegir.place(x=365, y=79,height=22,width=17)

saatglabel=Label(pencere)
saatglabel.pack
saatglabel.place(x=257,y=13)
saatglabel.config(text='Saat Girebilirsiniz',font=("Vertana",11))

saat2=StringVar()
saat2.set("0")
saatgir2=Entry(pencere,textvariable=saat2)
saatgir2.pack()
saatgir2.place(x=259, y=41,height=22,width=17)

ikin3=Label(pencere)
ikin3.pack()
ikin3.place(x=275,y=36)
ikin3.config(text=':', font=("Vertana",15))

dakika2=StringVar()
dakika2.set("0")
dakikagir2=Entry(pencere,textvariable=dakika2)
dakikagir2.pack()
dakikagir2.place(x=287, y=41,height=22,width=17)

createdby=Label(pencere)
createdby.config(text="Created By 132",font=("Lucida Calligraphy",11))
createdby.place(x=300,y=153)

sayacbaslat=Button(pencere)
sayacbaslat.pack()
sayacbaslat.place(x=310,y= 40,width=90,height=22)
sayacbaslat.config(text='Sayaç Başlat',font=("Vertana",9),command=sayaclikapat)

surebelirtiniz=Label(pencere)
surebelirtiniz.pack
surebelirtiniz.place(x=240,y=107)
surebelirtiniz.config(text=f'',font=("Vertana", 12))

mainloop()
