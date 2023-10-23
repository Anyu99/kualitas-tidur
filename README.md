# Laporan Proyek Machine Learning
### Nama : Juandhani Abimanyu
### Nim : 211351069
### Kelas : Malam B

## Domain Proyek

Tidur yang berkualitas sangat penting bagi manusia karena itu adalah saat di mana tubuh dan otak memiliki kesempatan untuk pulih, memperbaiki diri, dan mengembalikan energi. Tidur berkualitas juga berperan dalam menjaga keseimbangan hormon dan mendukung kesehatan mental dan fisik. Kurang tidur atau tidur yang buruk dapat berdampak negatif pada kinerja, konsentrasi, suasana hati, dan bahkan meningkatkan risiko masalah kesehatan seperti penyakit jantung, obesitas, dan gangguan mental. Oleh karena itu, tidur yang berkualitas adalah komponen penting dari gaya hidup sehat dan produktif.

## Business Understanding

Bedasarkan penjelasan sebelumnya penting untuk setiap individunya menjaga pola tidur dan hidup sehat, selain dari pada itu penting juga untuk mengetahui kualitas tidur yang selama ini dilakukan, apakah termasuk kedalam ganggunan tidur atau tidak.
Maka dari itu perlu dibuatkan sistem yang mudah diakses agar setiap individunya dapat mengetahui kualitas tidurnya, apakah termasuk kedalam ganguan tidur atau tidak.

Bagian laporan ini mencakup:

### Problem Statements

Menjelaskan pernyataan masalah latar belakang:
- Sulitnya untuk masyarakat umum agar mengetahui kualitas tidurnya
- Untuk mengetahui kualitas tidurnya, diperlukannya konsultasi dengan dokter yang mana biayanya tidaklah murah
- Tim kesehatan yang harus menganalisis gangguan tidur secara manual

### Goals

Menjelaskan tujuan dari pernyataan masalah:
- Dapat mempermudah masyarakat umum maupun tim kesehatan dalam melakukan klasifikasi kualitas tidur seseorang
- Dapat mempermudah masyarakat umum untuk mengetahui kualitas tidurnya tanpa harus mengeluarkan uang yang besar untuk bertemu dokter
    ### Solution statements
    - Pembuatan aplikasi yang dapat mempermudah proses klasifikasi kualitas tidur menjadi solusi untuk saat ini. Dengan adanya sistem yang dapat mempermudah dan dapat diakses oleh setiap orang, maka setiap orang dapat mengetahui kualitas tidurnya dan dapat segera menyadari adanya gangguan tidur atau tidak.
    - Pembuatan aplikasi ini menggunakan dataset yang diambil dari kaggle dan di deploy menggunakan bantuan streamlit. Model yang dibuat menggunakan metode klasifikasi dengan algoritma logistic regression.
      
## Data Understanding
Gambaran Umum Dataset:
Dataset Kesehatan dan Gaya Hidup Tidur terdiri dari 400 baris dan 13 kolom, yang mencakup berbagai variabel yang berkaitan dengan tidur dan kebiasaan sehari-hari. Dataset ini mencakup rincian seperti jenis kelamin, usia, pekerjaan, durasi tidur, kualitas tidur, tingkat aktivitas fisik, tingkat stres, kategori BMI, tekanan darah, detak jantung, langkah harian, dan ada tidaknya gangguan tidur.

Fitur Utama Dataset:
Metrik Tidur yang komprehensif: Jelajahi durasi, kualitas, dan faktor-faktor yang memengaruhi pola tidur.
Faktor Gaya Hidup: Menganalisis tingkat aktivitas fisik, tingkat stres, dan kategori BMI.
Kesehatan Kardiovaskular: Memeriksa tekanan darah dan pengukuran detak jantung.
Analisis Gangguan Tidur: Mengidentifikasi terjadinya gangguan tidur seperti Insomnia dan Sleep Apnea.<br> 

Dataset: [Sleep Health and Lifestyle Dataset](https://www.kaggle.com/datasets/uom190346a/sleep-health-and-lifestyle-dataset).

### Variabel-variabel pada Heart Failure Prediction Dataset adalah sebagai berikut:
- Person ID: Pengenal untuk setiap individu.
- Gender:  Jenis kelamin orang tersebut (Pria/Wanita).
- Age: The age of the person in years.
- Occupation: Pekerjaan atau profesi orang tersebut.
- Sleep Duration (hours): Jumlah jam orang tersebut tidur per hari.
- Quality of Sleep (scale: 1-10): Penilaian subjektif dari kualitas tidur, mulai dari 1 hingga 10.
- Physical Activity Level (minutes/day): The number of minutes the person engages in physical activity daily.
- Stress Level (scale: 1-10): Jumlah menit orang tersebut melakukan aktivitas fisik setiap hari.
- BMI Category: The BMI category of the person (e.g., Underweight, Normal, Overweight).
- Blood Pressure (systolic/diastolic): Kategori BMI orang tersebut (misalnya, Berat Badan Kurang, Normal, Berat Badan Berlebih).
- Heart Rate (bpm): Denyut jantung istirahat seseorang dalam denyut per menit.
- Daily Steps: Jumlah langkah yang dilakukan seseorang per hari.
- Sleep Disorder: Ada atau tidaknya gangguan tidur pada orang tersebut (Tidak Ada, Insomnia, Sleep Apnea).

**Detail tentang Kolom Gangguan Tidur:**
- Normal : Individu tidak menunjukkan gangguan tidur tertentu.
- Insomnia : Individu mengalami kesulitan untuk tidur atau tetap tertidur, yang menyebabkan tidur yang tidak memadai atau berkualitas buruk.
- Sleep Apnea :  Individu mengalami henti napas saat tidur, yang mengakibatkan gangguan pola tidur dan potensi risiko kesehatan.

## Data Preparation
Pada bagian ini Anda menerapkan dan menyebutkan teknik data preparation yang dilakukan. Teknik yang digunakan pada notebook dan laporan harus berurutan.


## Modeling
Tahapan ini membahas mengenai model machine learning yang digunakan untuk menyelesaikan permasalahan. Anda perlu menjelaskan tahapan dan parameter yang digunakan pada proses pemodelan.

**Rubrik/Kriteria Tambahan (Opsional)**: 
- Menjelaskan kelebihan dan kekurangan dari setiap algoritma yang digunakan.
- Jika menggunakan satu algoritma pada solution statement, lakukan proses improvement terhadap model dengan hyperparameter tuning. **Jelaskan proses improvement yang dilakukan**.
- Jika menggunakan dua atau lebih algoritma pada solution statement, maka pilih model terbaik sebagai solusi. **Jelaskan mengapa memilih model tersebut sebagai model terbaik**.

## Evaluation
Pada bagian ini anda perlu menyebutkan metrik evaluasi yang digunakan. Lalu anda perlu menjelaskan hasil proyek berdasarkan metrik evaluasi yang digunakan.

Sebagai contoh, Anda memiih kasus klasifikasi dan menggunakan metrik **akurasi, precision, recall, dan F1 score**. Jelaskan mengenai beberapa hal berikut:
- Penjelasan mengenai metrik yang digunakan
- Menjelaskan hasil proyek berdasarkan metrik evaluasi

Ingatlah, metrik evaluasi yang digunakan harus sesuai dengan konteks data, problem statement, dan solusi yang diinginkan.

**Rubrik/Kriteria Tambahan (Opsional)**: 
- Menjelaskan formula metrik dan bagaimana metrik tersebut bekerja.

## Deployment
pada bagian ini anda memberikan link project yang diupload melalui streamlit share. boleh ditambahkan screen shoot halaman webnya.

**---Ini adalah bagian akhir laporan---**

_Catatan:_
- _Anda dapat menambahkan gambar, kode, atau tabel ke dalam laporan jika diperlukan. Temukan caranya pada contoh dokumen markdown di situs editor [Dillinger](https://dillinger.io/), [Github Guides: Mastering markdown](https://guides.github.com/features/mastering-markdown/), atau sumber lain di internet. Semangat!_
- Jika terdapat penjelasan yang harus menyertakan code snippet, tuliskan dengan sewajarnya. Tidak perlu menuliskan keseluruhan kode project, cukup bagian yang ingin dijelaskan saja.

