# Capstone Project 1 - Aplikasi Pengelolaan Data Nilai Siswa

Project ini adalah sebuah aplikasi berbasis terminal yang digunakan untuk mengelola data nilai siswa dari dua jurusan, yaitu IPA dan IPS. Aplikasi ini menyediakan berbagai fitur seperti menampilkan data siswa, menambah data, menghapus data, memperbarui data, hingga menampilkan rapor kelas maupun individu siswa.

## Fitur Utama

1. **Menampilkan Data Nilai Siswa**
   - Melihat data siswa dari jurusan IPA atau IPS.
   - Data mencakup nama, gender, jurusan, dan nilai dari berbagai mata pelajaran sesuai dengan jurusan siswa.

2. **Menambah Data Siswa**
   - Menambahkan data siswa baru untuk jurusan IPA atau IPS.
   - Data yang dimasukkan meliputi ID siswa, nama, gender, dan nilai mata pelajaran.

3. **Menghapus Data Siswa**
   - Menghapus data siswa tertentu berdasarkan ID siswa.

4. **Memperbarui Data Siswa**
   - Memperbarui informasi siswa tertentu seperti nama, gender, atau nilai mata pelajaran berdasarkan ID siswa.

5. **Rapor Kelas**
   - Menampilkan statistik nilai kelas, seperti nilai maksimum, minimum, dan rata-rata untuk setiap mata pelajaran.

6. **Rapor Siswa**
   - Menampilkan nilai lengkap untuk siswa tertentu berdasarkan ID siswa.

7. **Keluar Program**
   - Mengakhiri aplikasi.

## Cara Penggunaan

1. **Instalasi**
   - Pastikan Python 3.x sudah terinstal di sistem Anda.
   - Instal pustaka Python yang diperlukan:
     ```bash
     pip install tabulate
     ```

2. **Menjalankan Program**
   - Jalankan file Python menggunakan perintah berikut:
     ```bash
     python <nama_file>.py
     ```

3. **Navigasi Menu**
   - Pilih menu berdasarkan angka yang tersedia di antarmuka program.
   - Ikuti instruksi yang diberikan untuk setiap fitur.

## Struktur Data

Data siswa disimpan dalam bentuk dictionary untuk masing-masing jurusan:

**IPA**
  - ID siswa
  - Nama
  - Gender
  - Nilai dari berbagai mata pelajaran (Matematika, Fisika, Kimia, Biologi, Bahasa Indonesia, Bahasa Inggris)

**IPS**
  - Sama seperti IPA, tetapi mata pelajaran Fisika, Kimia, dan Biologi digantikan dengan mata pelajaran Ekonomi, Geografi, dan Sosiologi.

## Dependensi

Proyek ini memerlukan pustaka pihak ketiga:
- **Tabulate**: Untuk menampilkan data dalam format tabel yang lebih mudah dibaca.

## Catatan Tambahan

- Pastikan ID siswa yang dimasukkan bersifat unik untuk menghindari konflik data.
- Program ini hanya dapat menerima input angka untuk nilai pelajaran dengan rentang 0-100.

## Pengembang

- **Nama**: Abizar Ghifari Winandita
- **Batch**: JCDS 2502
- **Proyek**: Capstone Project 1

## Lisensi

Proyek ini dibuat untuk keperluan pembelajaran dan terbuka untuk dikembangkan lebih lanjut.
