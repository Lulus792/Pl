Die Programme fur den Arduino befinden sich in arduino_scripts
Die fur den Red Pitaya in red_pitaya

Das script schwarzer_strahler_theo.py erstellt ein Bild mit den Theoretischen
kurven fur 750K, 800K und 850K

schwarzer_strahler gibst du als parameter deine datein mit Messdaten. Diser Plottet 
dann alle daten in einem Bild: schwarzer_strahler_auto data1.csv data2.csv

schwarzer_strahler_auto data1.csv data2.csv speichert bilder. Jedes Bild enthalt 
die Werte mit der dazugerhorigen theoretischen curve ohne fit 

schwarzer_strahler_auto_fit data1.csv data2.csv speichert bilder. Jedes Bild enthalt 
die Werte mit einem Fit der Fit paramter wird auch im Label ausgegeben, dadurch
muss man sich den code nicht anschauen

Datei strucktur:
x,y,T
val1,val2,T1
val3,val4
val5,val6
...
