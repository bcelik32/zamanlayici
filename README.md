Kapatma Zamanlayıcısı
1) kapatmazamanlayici.exe'yi Bilgisayar İçinde Bir Yere Taşıyın.
2) kapat2.ico Dosyasını Aynı Konuma Taşıyın.
3) Exe için bir Kısayol oluşturun.
4) Kısayolu Çalıştırın.
Not: Program 00'dan 09'a kadar Girilen Saatlerde(sadece sağ üstteki iki kutu)Çalışmaz. Bunun nedeni Python'daki strftime komutunda tek haneli saatleri yazarken başına 0 koymamasıdır(05:30 yerine 5:30 gibi).  

Shutdown Timer
1) Move the shutdowntimer.exe Somewhere Inside the Computer.
2) Move the close2.ico File to the Same Location.
3) Create a Shortcut for the Exe.
4) Run the Shortcut.
Note: The program will not run in the Hours Entered from 00 to 09 (only the two boxes at the top right). This is because the strftime command in Python does not prefix single-digit times with a 0 (like 5:30 instead of 05:30).
