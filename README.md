Kapatma Zamanlayıcısı
1) ShutdownTimer.exe'yi içinde Bir Yere Taşıyın.
2) thekapa2.ico dosyasını aynı konuşmayı taşıyın.
3) Exe için bir Kısayol oluşturun.
Not: Program 00'dan 09'a kadar Girilen Saatlerde(sadece sağ üstteki iki kutu)Çalışmaz. Bunun nedeni Python'daki strftime komutunda tek haneli saatleri yazarken başına 0 koymamasıdır(05:30 yerine 5:30 gibi).  

Shutdown Timer
1) Move ShutdownTimer.exe Somewhere in it.
2) Move thekapa2.ico file to the same speech.
3) Create a Shortcut for the Exe.
Note: The program will not run in the Hours Entered from 00 to 09 (only the two boxes at the top right). This is because the strftime command in Python does not prefix single-digit times with a 0 (like 5:30 instead of 05:30).
