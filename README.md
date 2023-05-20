# UAS
Code Base UAS Pemrograman Web Berbasis IoT

A. Temperature Sensor
    Fungsi  : mengukur suhu area smart farm
    Jangkah : 10 - 50 °C
B. Soil Moisture Sensor 
    Fungsi  : mengukur kelembapan tanah
    Jangkah : 0 - 100 %
C. Light Intensity Sensor
    Fungsi  : mengukur jumlah cahaya di area smart farm
    Jangkah : 0 - 10000 lux
D. Irrigation System
    Fungsi  : mengalirkan air ke dalam Smart Farm untuk membasahi tanah
    Jangkah : 0 - 100 L


Jika suhu terlalu tinggi/terlalu rendah maka air yang dialirkan berkurang
Jika intensitas cahaya meningkat maka air yang dialirkan meningkat
Jika kelembapan tanah menurun maka air yang dialirkan meningkat


Training data (machinelearning/irrigation.csv)
temp,soil,light,irrigation
25,50,5000,10
30,40,3000,8
28,60,4000,9
20,70,2000,7
15,30,1000,5
22,55,4500,9
27,45,3500,8
32,35,2500,7
18,65,1500,6
10,20,500,4
24,60,5500,11
29,50,4500,10
26,70,3500,8
14,40,2500,6
21,35,1500,5
12,25,2000,5
17,45,5500,10
23,55,4500,9
28,50,3500,8
16,65,2500,7
