# Capstone Project 1 - Abizar Ghifari Winandita - Aplikasi Pengelolaan Data Nilai Siswa (Revised Edition)

from tabulate import tabulate

# Tampilan menu utama
def menu_utama():
    print()
    print(f"Menu Utama:\n\n 1. Menampilkan Data Nilai Siswa\n 2. Menambah Data Siswa\n 3. Menghapus Data Siswa\n 4. Memperbarui Data Siswa\n 5. Rapor Kelas\n 6. Rapor Siswa\n 7. Exit Program")

print()
# Database Dummy
database_siswa_ipa = {"id_student" : ["000", "001", "002", "003", "004"], 
                "nama" : ["Abizar Winandita", "Aditya Anindito", "Galuh Sayranti", "Khairillah Fathinuzul", "Wulandari Ismiyati"], 
                "gender" : ["L","L","P","L","P"], 
                "jurusan" : ["IPA","IPA","IPA","IPA","IPA"],
                "nilai_matematika" : [90, 80, 85, 95, 75],
                "nilai_fisika" : [85, 82, 85, 90, 90],
                "nilai_kimia" : [95, 75, 80, 90, 80],
                "nilai_biologi" : [70, 79, 90, 85, 100],
                "nilai_bindo" : [65, 60, 75, 80, 80],
                "nilai_bing" : [100, 70, 60, 90, 95]
                }
# Database Dummy
database_siswa_ips = {"id_student" : ["000", "001", "002", "003", "004"], 
                "nama" : ["Muhammad Faiz", "Muhammad Zukfikar", "Alvira Rahmadania","Umar Abdulhafizh", "Naufal Winandita"], 
                "gender" : ["L","L","P","L","P"], 
                "jurusan" : ["IPS","IPS","IPS","IPS","IPS"],
                "nilai_matematika" : [90, 80, 85, 90, 92],
                "nilai_ekonomi" : [85, 82, 83, 92, 90],
                "nilai_geografi" : [95, 75, 90, 95, 80],
                "nilai_sosiologi" : [70, 79, 75, 88, 81],
                "nilai_bindo" : [65, 60, 80, 90, 83],
                "nilai_bing" : [100, 70, 90, 95, 93]
                }

# Tampilan menu 1 --> Melihat database jurusan IPA atau IPS
def menu_1():
    print()
    while True: # Infinite loop selama benar, maka program akan terus berjalan
        try: # Try & Except untuk menangani ketika program terjadi error
            print(f"Database Nilai Siswa:\n\n 1. Data nilai siswa jurusan IPA\n 2. Data nilai siswa jurusan IPS\n 3. Kembali ke menu utama") #Tampilan sub-menu untuk menampilkan database
            print()
            pilih_submenu = int(input("Pilih opsi menu 1-3: "))
            if pilih_submenu == 1: # User pilih untuk melihat database jurusan IPA
                print(tabulate(database_siswa_ipa,headers = database_siswa_ipa.keys(), tablefmt="pretty"))
            elif pilih_submenu == 2: # User pilih untuk melihat database jurusan IPS
                print(tabulate(database_siswa_ips,headers = database_siswa_ipa.keys(), tablefmt="pretty"))
            elif pilih_submenu == 3: # User pilih untuk keluar dari program "Melihat database jurusan IPA/IPS"
                print()
                print("Selesai menampilkan database nilai siswa.")
                break #  Break untuk menyelesaikan looping dan keluar dari sub-menu / Kembali ke menu utama
            else:
                print()
                print(f"Opsi tidak tersedia.") # "Opsi tidak tersedia" muncul jika user menulis angka selain angka 1-3
                print()
        except ValueError:
            print()
            print(f"Input tidak valid.") # "Input tidak valid" muncul jika user menulis selain numerik
            print()

# Tampilan menu 2 --> Menambah database siswa jurusan IPA atau IPS
def menu_2(): # Coba improvisasi pakai function berpola
    print()
    while True: # Infinite loop selama benar, maka program akan terus berjalan
        try: # Try & Except untuk menangani ketika program terjadi error, Menempatkan Try pada kode yang kemungkinan akan menimbulkan error
            print(f"Pilihan Untuk Menambah Data Siswa:\n\n 1. Menambah data nilai siswa jurusan IPA\n 2. Menambah data nilai siswa jurusan IPS\n 3. Kembali ke menu utama") #Tampilan sub-menu untuk menambahkan data
            print()
            menambah_data_siswa = int(input("Pilih opsi menu 1-3: "))
            if menambah_data_siswa == 1: # Pilih 1 jika user ingin menambah database siswa jurusan IPA
                while True:
                    id_student_baru = input("Input ID siswa (3 angka): ")
                    if id_student_baru.isdigit() and len(id_student_baru) == 3 and id_student_baru not in database_siswa_ipa["id_student"]: # Conditional statement untuk validasi input dari user
                        break
                    else:
                        print(f"ID siswa tidak sesuai format atau sudah terpakai. Silahkan coba lagi.")
                nama_baru = input("Input nama lengkap siswa: ").title()
                while True:
                    gender_baru = input("Input jenis kelamin siswa (L/P): ").title()
                    if gender_baru == "L" or gender_baru == "P": # Conditional statement supaya user hanya bisa mengisi L atau P
                        break
                    else:
                        print(f"Input gagal. Jenis kelamin hanya bisa diisi oleh huruf L/P")
                jurusan_baru = "IPA"
                while True:
                    nilai_matematika_baru = int(input("Nilai Matematika: "))
                    if nilai_matematika_baru >= 0 and nilai_matematika_baru <= 100: # Conditional statement untuk mencegah user memasukan data di luar range yang telah ditetapkan (1-100)
                        break
                    else:
                        print(f"Input nilai Matematika gagal. Harap masukkan angka 0 - 100.")
                while True:
                    nilai_fisika_baru= int(input("Nilai Fisika: "))
                    if nilai_fisika_baru >= 0 and nilai_fisika_baru <= 100:
                        break
                    else:
                        print(f"Input nilai Fisika gagal. Harap masukkan angka 0 - 100.")
                while True:
                    nilai_kimia_baru = int(input("Nilai Kimia: "))
                    if nilai_kimia_baru >= 0 and nilai_kimia_baru <= 100:
                        break
                    else:
                        print(f"Input nilai Kimia gagal. Harap masukkan angka 0 - 100.")
                while True:
                    nilai_biologi_baru = int(input("Nilai Biologi: "))
                    if nilai_biologi_baru >= 0 and nilai_biologi_baru <= 100:
                        break
                    else:
                        print(f"Input nilai Biologi gagal. Harap masukkan angka 0 - 100.")
                while True:
                    nilai_bindo_baru = int(input("Nilai Bahasa Indonesia: "))
                    if nilai_bindo_baru >= 0 and nilai_bindo_baru <= 100:
                        break
                    else:
                        print(f"Input nilai Bahasa Indonesia gagal. Harap masukkan angka 0 - 100.")
                while True:
                    nilai_bing_baru = int(input("Nilai Bahasa Inggris: "))
                    if nilai_bing_baru >= 0 and nilai_bing_baru <= 100:
                        break
                    else:
                        print(f"Input nilai Bahasa Inggris gagal. Harap masukkan angka 0 - 100.")
            
                # Memasukkan data siswa baru ke database_siswa_ipa, coba append berpola dibuat function sekalian sama sub looping
                database_siswa_ipa["id_student"].append(id_student_baru)
                database_siswa_ipa["nama"].append(nama_baru)
                database_siswa_ipa["gender"].append(gender_baru)
                database_siswa_ipa["jurusan"].append(jurusan_baru)
                database_siswa_ipa["nilai_matematika"].append(nilai_matematika_baru)
                database_siswa_ipa["nilai_fisika"].append(nilai_fisika_baru)
                database_siswa_ipa["nilai_kimia"].append(nilai_kimia_baru)
                database_siswa_ipa["nilai_biologi"].append(nilai_biologi_baru)
                database_siswa_ipa["nilai_bindo"].append(nilai_bindo_baru)
                database_siswa_ipa["nilai_bing"].append(nilai_bing_baru)

                print(tabulate(database_siswa_ipa,headers = database_siswa_ipa.keys(), tablefmt="pretty"))
                print()
                print(f"Data siswa berhasil disimpan ke 'Database Siswa IPA'.") # Jika user berhasil menambahkan data ke dalam database

            elif menambah_data_siswa == 2: # Pilih 2 jika user ingin menambah database siswa jurusan IPS
                while True:
                    id_student_baru = input("Input ID siswa (3 angka): ")
                    if id_student_baru.isdigit() and len(id_student_baru) == 3 and id_student_baru not in database_siswa_ips["id_student"]:
                        break
                    else:
                        print(f"ID siswa tidak sesuai format atau sudah terpakai. Silahkan coba lagi.")
                nama_baru = input("Input nama lengkap siswa: ").title()
                while True:
                    gender_baru = input("Input jenis kelamin siswa (L/P): ").title()
                    if gender_baru == "L" or gender_baru == "P":
                        break
                    else:
                        print(f"Input gagal. Jenis kelamin hanya bisa diisi oleh huruf L/P")
                jurusan_baru = "IPS"
                while True:
                    nilai_matematika_baru = int(input("Nilai Matematika: "))
                    if nilai_matematika_baru >= 0 and nilai_matematika_baru <= 100:
                        break
                    else:
                        print(f"Input nilai Matematika gagal. Harap masukkan angka 0 - 100.")
                while True:
                    nilai_ekonomi_baru= int(input("Nilai Ekonomi: "))
                    if nilai_ekonomi_baru >= 0 and nilai_ekonomi_baru <= 100:
                        break
                    else:
                        print(f"Input nilai Ekonomi gagal. Harap masukkan angka 0 - 100.")
                while True:
                    nilai_geografi_baru = int(input("Nilai Geografi: "))
                    if nilai_geografi_baru >= 0 and nilai_geografi_baru <= 100:
                        break
                    else:
                        print(f"Input nilai Geografi gagal. Harap masukkan angka 0 - 100.")
                while True:
                    nilai_sosiologi_baru = int(input("Nilai Sosiologi: "))
                    if nilai_sosiologi_baru >= 0 and nilai_sosiologi_baru <= 100:
                        break
                    else:
                        print(f"Input nilai Sosiologi gagal. Harap masukkan angka 0 - 100.")
                while True:
                    nilai_bindo_baru = int(input("Nilai Bahasa Indonesia: "))
                    if nilai_bindo_baru >= 0 and nilai_bindo_baru <= 100:
                        break
                    else:
                        print(f"Input nilai Bahasa Indonesia gagal. Harap masukkan angka 0 - 100.")
                while True:
                    nilai_bing_baru = int(input("Nilai Bahasa Inggris: "))
                    if nilai_bing_baru >= 0 and nilai_bing_baru <= 100:
                        break
                    else:
                        print(f"Input nilai Bahasa Inggris gagal. Harap masukkan angka 0 - 100.")

                # Masukin data siswa baru ke database_siswa_ips
                database_siswa_ips["id_student"].append(id_student_baru)
                database_siswa_ips["nama"].append(nama_baru)
                database_siswa_ips["gender"].append(gender_baru)
                database_siswa_ips["jurusan"].append(jurusan_baru)
                database_siswa_ips["nilai_matematika"].append(nilai_matematika_baru)
                database_siswa_ips["nilai_ekonomi"].append(nilai_ekonomi_baru)
                database_siswa_ips["nilai_geografi"].append(nilai_geografi_baru)
                database_siswa_ips["nilai_sosiologi"].append(nilai_sosiologi_baru)
                database_siswa_ips["nilai_bindo"].append(nilai_bindo_baru)
                database_siswa_ips["nilai_bing"].append(nilai_bing_baru)

                print(tabulate(database_siswa_ips,headers = database_siswa_ips.keys(), tablefmt="pretty"))
                print()
                print(f"Data siswa berhasil disimpan ke 'Database Siswa IPS'.")
            
            elif menambah_data_siswa == 3: # Pilih 3 jika user ingin keluar dari sub-menu
                print()
                print("Selesai menambahkan data siswa.")
                break

            else: # Output yang terjadi ketika user pilih selain angka 1-3
                print()
                print(f"Opsi tidak tersedia.")
                print()

        except ValueError: # Menangkap error jika ada dan menentukan tindakan saat error terjadi
            print()
            print(f"Input tidak valid.")
            print()

# Tampilan menu 3 --> Menghapus data siswa jurusan IPA/IPS
def menu_3():
    print()
    while True: # Infinite loop selama benar, maka program akan terus berjalan
        try: # Try & Except untuk menangani ketika program terjadi error, Menempatkan Try pada kode yang kemungkinan akan menimbulkan error
            print(f"Pilihan Untuk Menghapus Data Siswa:\n\n 1. Menghapus data nilai siswa jurusan IPA\n 2. Menghapus data nilai siswa jurusan IPS\n 3. Kembali ke menu utama") # Tampilan sub-menu untuk menghapus data siswa
            print()
            menghapus_data_siswa = int(input("Pilih opsi menu 1-3: "))

            if menghapus_data_siswa == 1: # Kalo user pilih 1 maka akan diarahkan ke database siswa IPA
                print(tabulate(database_siswa_ipa,headers = database_siswa_ipa.keys(), tablefmt="pretty"))
                id_student_hapus_ipa = input("Masukkan 'ID Student' siswa IPA yang ingin dihapus (3 angka): ")

                if id_student_hapus_ipa in database_siswa_ipa["id_student"]: # Melakukan pengecekan ada valuenya gak di key id_student
                    find_index_hapus_ipa = database_siswa_ipa["id_student"].index(id_student_hapus_ipa) # Menemukan index untuk value 000/001/dst itu ada di index ke berapa
                    for key_ipa in database_siswa_ipa.keys():
                        del database_siswa_ipa[key_ipa][find_index_hapus_ipa] # Looping setiap key di database_siswa_ipa, lalu menghapus value di index tertentu pada seluruh key-nya
                    print(f"Data siswa dengan ID '{id_student_hapus_ipa}' berhasil dihapus dari 'Database Jurusan IPA'.")
                    print()
                    print(tabulate(database_siswa_ipa,headers = database_siswa_ipa.keys(), tablefmt="pretty"))
                else:
                    print(f"Siswa dengan ID '{id_student_hapus_ipa}' tidak ada di dalam 'Database Jurusan IPA'.") # Terjadi ketika ID siswa tidak ditemukan

            elif menghapus_data_siswa == 2: # Kalo user pilih 2 maka akan diarahkan ke database siswa IPS
                print(tabulate(database_siswa_ips,headers = database_siswa_ips.keys(), tablefmt="pretty"))
                id_student_hapus_ips = input("Masukkan 'ID Student' siswa IPS yang ingin dihapus (3 angka): ")

                if id_student_hapus_ips in database_siswa_ips["id_student"]: # Melakukan pengecekan ada valuenya gak di key id_student
                    find_index_hapus_ips = database_siswa_ips["id_student"].index(id_student_hapus_ips) # Menemukan index untuk value 000/001/dst itu ada di index ke berapa
                    for key_ips in database_siswa_ips.keys():
                        del database_siswa_ips[key_ips][find_index_hapus_ips] # Looping setiap key di database_siswa_ipa, lalu menghapus value di index tertentu pada seluruh key-nya
                    print(f"Data siswa dengan ID '{id_student_hapus_ips}' berhasil dihapus dari 'Database Jurusan IPS'.")
                    print()
                    print(tabulate(database_siswa_ips,headers = database_siswa_ips.keys(), tablefmt="pretty"))

                else:
                    print(f"Siswa dengan ID '{id_student_hapus_ips}' tidak ada di dalam 'Database Jurusan IPS'.")

            elif menghapus_data_siswa == 3: # Jika user ingin keluar dari program menghapus data siswa
                    print()
                    print("Selesai menghapus data siswa.")
                    break

            else:
                print()
                print(f"Opsi tidak tersedia") # Jika user memilih opsi di luar range opsi (1-3)
                print()

        except ValueError: # Menangkap error jika ada dan menentukan tindakan saat error terjadi
            print()
            print(f"Input tidak valid.")
            print()

# Tampilan menu 4 --> Melakukan perbaruan data siswa jurusan IPA/IPS
def menu_4():
    print()
    while True: # Infinite loop selama benar, maka program akan terus berjalan
        try: # Try & Except untuk menangani ketika program terjadi error, Menempatkan Try pada kode yang kemungkinan akan menimbulkan error
            print(f"Pilihan Untuk Memperbarui Data Siswa:\n\n 1. Memperbarui data nilai siswa jurusan IPA\n 2. Memperbarui data nilai siswa jurusan IPS\n 3. Kembali ke menu utama") # Tampilan sub-menu untuk memperbarui data siswa
            print()
            update_data_siswa = int(input("Pilih opsi menu 1-3: "))

            if update_data_siswa == 1: # Jika user pilih IPA
                print(tabulate(database_siswa_ipa,headers = database_siswa_ipa.keys(), tablefmt="pretty"))
                while True:
                    print(f"Pilih opsi untuk memperbarui nilai pada kolom tertentu:\n 1. Memperbarui Nama Siswa\n 2. Memperbarui Jenis Kelamin Siswa\n 3. Memperbarui Nilai Matematika\n 4. Memperbarui Nilai Fisika\n 5. Memperbarui Nilai Kimia\n 6. Memperbarui Nilai Biologi\n 7. Memperbarui Nilai Bahasa Indonesia\n 8. Memperbarui Nilai Bahasa Inggris\n 9. Exit Program")
                    print()
                    pilih_opsi_update = int(input("Masukkan opsi angka 1 - 9: "))

                    if pilih_opsi_update == 9:
                        print()
                        print("Selesai melakukan pembaruan pada 'Database Jurusan IPA'.")
                        break

                    if pilih_opsi_update < 1 or pilih_opsi_update > 9:
                        print()
                        print(f"Opsi tidak tersedia")
                        print()
                        continue

                    id_student_update = input("Masukkan ID siswa IPA yang ingin diperbarui (3 angka): ")
                    while True:
                        if id_student_update.isdigit() and len(id_student_update) == 3 and id_student_update in database_siswa_ipa["id_student"]: # Conditional statement untuk validasi input dari user
                            break
                        else:
                            print(f"ID siswa '{id_student_update}' tidak sesuai format atau belum terdaftar di 'Database Jurusan IPA'. Silahkan coba lagi.")
                            break

                    find_index = database_siswa_ipa["id_student"].index(id_student_update)

                    if pilih_opsi_update == 1:
                        update_nama = input(f"Masukkan nama lengkap baru siswa dengan nomor ID '{id_student_update}': ").title()
                        database_siswa_ipa["nama"][find_index] = update_nama
                        print(tabulate(database_siswa_ipa,headers = database_siswa_ipa.keys(), tablefmt="pretty"))
                        print()
                        print(f"Nama siswa dengan ID '{id_student_update}' berhasil diubah menjadi '{update_nama}'.")

                    elif pilih_opsi_update == 2:
                        while True:
                            update_gender = input(f"Masukkan jenis kelamin terbaru untuk siswa dengan nomor ID '{id_student_update}': ").title()
                            if update_gender == "L" or update_gender == "P":
                                database_siswa_ipa["gender"][find_index] = update_gender
                                print(tabulate(database_siswa_ipa,headers = database_siswa_ipa.keys(), tablefmt="pretty"))
                                print()
                                print(f"Jenis Kelamin siswa dengan ID '{id_student_update}' berhasil diubah menjadi '{update_gender}'.") 
                                break
                            else:
                                print(f"Data gagal diperbarui. Jenis kelamin hanya bisa diisi oleh huruf L/P")

                    elif pilih_opsi_update == 3:
                        while True:
                            update_nilai_matematika = int(input(f"Masukkan 'Nilai Matematika' terbaru untuk siswa dengan ID '{id_student_update}': "))
                            if update_nilai_matematika >= 0 and update_nilai_matematika <= 100:
                                database_siswa_ipa["nilai_matematika"][find_index] = update_nilai_matematika
                                print(tabulate(database_siswa_ipa,headers = database_siswa_ipa.keys(), tablefmt="pretty"))
                                print()
                                print(f"Nilai Matematika siswa dengan ID '{id_student_update}' berhasil diubah menjadi '{update_nilai_matematika}'")
                                break
                            else:
                                print(f"Nilai Matematika gagal diperbarui. Harap masukkan angka 0 - 100.")

                    elif pilih_opsi_update == 4:
                        while True:
                            update_nilai_fisika = int(input(f"Masukkan 'Nilai Fisika' terbaru untuk siswa dengan ID '{id_student_update}': "))
                            if update_nilai_fisika >= 0 and update_nilai_fisika <= 100:
                                database_siswa_ipa["nilai_fisika"][find_index] = update_nilai_fisika
                                print(tabulate(database_siswa_ipa,headers = database_siswa_ipa.keys(), tablefmt="pretty"))
                                print()
                                print(f"Nilai Fisika siswa dengan ID '{id_student_update}' berhasil diubah menjadi '{update_nilai_fisika}'")
                                break
                            else:
                                print(f"Nilai Fisika gagal diperbarui. Harap masukkan angka 0 - 100.")

                    elif pilih_opsi_update == 5:
                        while True:
                            update_nilai_kimia = int(input(f"Masukkan 'Nilai Kimia' terbaru untuk siswa dengan ID '{id_student_update}': "))
                            if update_nilai_kimia >= 0 and update_nilai_kimia <= 100:
                                database_siswa_ipa["nilai_kimia"][find_index] = update_nilai_kimia
                                print(tabulate(database_siswa_ipa,headers = database_siswa_ipa.keys(), tablefmt="pretty"))
                                print()
                                print(f"Nilai Kimia siswa dengan ID '{id_student_update}' berhasil diubah menjadi '{update_nilai_kimia}'")
                                break
                            else:
                                print(f"Nilai Kimia gagal diperbarui. Harap masukkan angka 0 - 100.")

                    elif pilih_opsi_update == 6:
                        while True:
                            update_nilai_biologi = int(input(f"Masukkan 'Nilai Biologi' terbaru untuk siswa dengan ID '{id_student_update}': "))
                            if update_nilai_biologi >= 0 and update_nilai_biologi <= 100:
                                database_siswa_ipa["nilai_biologi"][find_index] = update_nilai_biologi
                                print(tabulate(database_siswa_ipa,headers = database_siswa_ipa.keys(), tablefmt="pretty"))
                                print()
                                print(f"Nilai Biologi siswa dengan ID '{id_student_update}' berhasil diubah menjadi '{update_nilai_biologi}'")
                                break
                            else:
                                print(f"Nilai Biologi gagal diperbarui. Harap masukkan angka 0 - 100.")

                    elif pilih_opsi_update == 7:
                        while True:
                            update_nilai_bindo = int(input(f"Masukkan 'Nilai Bahasa Indonesia' terbaru untuk siswa dengan ID '{id_student_update}': "))
                            if update_nilai_bindo >= 0 and update_nilai_bindo <= 100:
                                database_siswa_ipa["nilai_bindo"][find_index] = update_nilai_bindo
                                print(tabulate(database_siswa_ipa,headers = database_siswa_ipa.keys(), tablefmt="pretty"))
                                print()
                                print(f"Nilai Bahasa Indonesia siswa dengan ID '{id_student_update}' berhasil diubah menjadi '{update_nilai_bindo}'")
                                break
                            else:
                                print(f"Nilai Bahasa Indonesia gagal diperbarui. Harap masukkan angka 0 - 100.")

                    elif pilih_opsi_update == 8:
                        while True:
                            update_nilai_bing = int(input(f"Masukkan 'Nilai Bahasa Inggris' terbaru untuk siswa dengan ID '{id_student_update}': "))
                            if update_nilai_bing >= 0 and update_nilai_bing <= 100:
                                database_siswa_ipa["nilai_bing"][find_index] = update_nilai_bing
                                print(tabulate(database_siswa_ipa,headers = database_siswa_ipa.keys(), tablefmt="pretty"))
                                print()
                                print(f"Nilai Bahasa Inggris siswa dengan ID '{id_student_update}' berhasil diubah menjadi '{update_nilai_bing}'")
                                break
                            else:
                                print(f"Nilai Bahasa Inggris gagal diperbarui. Harap masukkan angka 0 - 100.")

            elif update_data_siswa == 2: # Jika user pilih IPS
                print(tabulate(database_siswa_ips,headers = database_siswa_ips.keys(), tablefmt="pretty"))
                while True:
                    print(f"Pilih opsi untuk memperbarui nilai pada kolom tertentu:\n\n 1. Memperbarui Nama Siswa\n 2. Memperbarui Jenis Kelamin Siswa\n 3. Memperbarui Nilai Matematika\n 4. Memperbarui Nilai Ekonomi\n 5. Memperbarui Nilai Geografi\n 6. Memperbarui Nilai Sosiologi\n 7. Memperbarui Nilai Bahasa Indonesia\n 8. Memperbarui Nilai Bahasa Inggris\n 9. Exit Program")
                    print()
                    pilih_opsi_update = int(input("Masukkan opsi angka 1 - 9: "))

                    if pilih_opsi_update == 9:
                        print()
                        print("Selesai melakukan pembaruan pada 'Database Jurusan IPS'.")
                        break

                    if pilih_opsi_update < 1 or pilih_opsi_update > 9:
                        print()
                        print(f"Opsi tidak tersedia")
                        print()
                        continue

                    id_student_update = input("Masukkan ID siswa IPS yang ingin diperbarui (3 angka): ")
                    while True:
                        if id_student_update.isdigit() and len(id_student_update) == 3 and id_student_update in database_siswa_ips["id_student"]:
                            break
                        else:
                            print(f"ID siswa '{id_student_update}' tidak sesuai format atau belum terdaftar di 'Database Jurusan IPS'. Silahkan coba lagi.")
                            break

                    find_index = database_siswa_ips["id_student"].index(id_student_update)

                    if pilih_opsi_update == 1:
                        update_nama = input(f"Masukkan nama lengkap baru siswa dengan nomor ID '{id_student_update}': ").title()
                        database_siswa_ips["nama"][find_index] = update_nama
                        print(tabulate(database_siswa_ips,headers = database_siswa_ips.keys(), tablefmt="pretty"))
                        print()
                        print(f"Nama siswa dengan ID '{id_student_update}' berhasil diubah menjadi '{update_nama}'.")

                    elif pilih_opsi_update == 2:
                        while True:
                            update_gender = input(f"Masukkan jenis kelamin terbaru untuk siswa dengan nomor ID '{id_student_update}': ").title()
                            if update_gender == "L" or update_gender == "P":
                                database_siswa_ips["gender"][find_index] = update_gender
                                print(tabulate(database_siswa_ips,headers = database_siswa_ips.keys(), tablefmt="pretty"))
                                print()
                                print(f"Jenis Kelamin siswa dengan ID '{id_student_update}' berhasil diubah menjadi '{update_gender}'.") 
                                break
                            else:
                                print(f"Data gagal diperbarui. Jenis kelamin hanya bisa diisi oleh huruf L/P")

                    elif pilih_opsi_update == 3:
                        while True:
                            update_nilai_matematika = int(input(f"Masukkan 'Nilai Matematika' terbaru untuk siswa dengan ID '{id_student_update}': "))
                            if update_nilai_matematika >= 0 and update_nilai_matematika <= 100:
                                database_siswa_ips["nilai_matematika"][find_index] = update_nilai_matematika
                                print(tabulate(database_siswa_ips,headers = database_siswa_ips.keys(), tablefmt="pretty"))
                                print()
                                print(f"Nilai Matematika siswa dengan ID '{id_student_update}' berhasil diubah menjadi '{update_nilai_matematika}'")
                                break
                            else:
                                print(f"Nilai Matematika gagal diperbarui. Harap masukkan angka 0 - 100.")

                    elif pilih_opsi_update == 4:
                        while True:
                            update_nilai_ekonomi = int(input(f"Masukkan 'Nilai Ekonomi' terbaru untuk siswa dengan ID '{id_student_update}': "))
                            if update_nilai_ekonomi >= 0 and update_nilai_ekonomi <= 100:
                                database_siswa_ips["nilai_ekonomi"][find_index] = update_nilai_ekonomi
                                print(tabulate(database_siswa_ips,headers = database_siswa_ips.keys(), tablefmt="pretty"))
                                print()
                                print(f"Nilai Ekonomi siswa dengan ID '{id_student_update}' berhasil diubah menjadi '{update_nilai_ekonomi}'")
                                break
                            else:
                                print(f"Nilai Ekonomi gagal diperbarui. Harap masukkan angka 0 - 100.")

                    elif pilih_opsi_update == 5:
                        while True:
                            update_nilai_geografi = int(input(f"Masukkan 'Nilai Geografi' terbaru untuk siswa dengan ID '{id_student_update}': "))
                            if update_nilai_geografi >= 0 and update_nilai_geografi <= 100:
                                database_siswa_ips["nilai_geografi"][find_index] = update_nilai_geografi
                                print(tabulate(database_siswa_ips,headers = database_siswa_ips.keys(), tablefmt="pretty"))
                                print()
                                print(f"Nilai Geografi siswa dengan ID '{id_student_update}' berhasil diubah menjadi '{update_nilai_geografi}'")
                                break
                            else:
                                print(f"Nilai Geografi gagal diperbarui. Harap masukkan angka 0 - 100.")

                    elif pilih_opsi_update == 6:
                        while True:
                            update_nilai_sosiologi = int(input(f"Masukkan 'Nilai Sosiologi' terbaru untuk siswa dengan ID '{id_student_update}': "))
                            if update_nilai_sosiologi >= 0 and update_nilai_sosiologi <= 100:
                                database_siswa_ips["nilai_sosiologi"][find_index] = update_nilai_sosiologi
                                print(tabulate(database_siswa_ips,headers = database_siswa_ips.keys(), tablefmt="pretty"))
                                print()
                                print(f"Nilai Sosiologi siswa dengan ID '{id_student_update}' berhasil diubah menjadi '{update_nilai_sosiologi}'")
                                break
                            else:
                                print(f"Nilai Sosiologi gagal diperbarui. Harap masukkan angka 0 - 100.")

                    elif pilih_opsi_update == 7:
                        while True:
                            update_nilai_bindo = int(input(f"Masukkan 'Nilai Bahasa Indonesia' terbaru untuk siswa dengan ID '{id_student_update}': "))
                            if update_nilai_bindo >= 0 and update_nilai_bindo <= 100:
                                database_siswa_ips["nilai_bindo"][find_index] = update_nilai_bindo
                                print(tabulate(database_siswa_ips,headers = database_siswa_ips.keys(), tablefmt="pretty"))
                                print()
                                print(f"Nilai Bahasa Indonesia siswa dengan ID '{id_student_update}' berhasil diubah menjadi '{update_nilai_bindo}'")
                                break
                            else:
                                print(f"Nilai Bahasa Indonesia gagal diperbarui. Harap masukkan angka 0 - 100.")

                    elif pilih_opsi_update == 8:
                        while True:
                            update_nilai_bing = int(input(f"Masukkan 'Nilai Bahasa Inggris' terbaru untuk siswa dengan ID '{id_student_update}': "))
                            if update_nilai_bing >= 0 and update_nilai_bing <= 100:
                                database_siswa_ips["nilai_bing"][find_index] = update_nilai_bing
                                print(tabulate(database_siswa_ips,headers = database_siswa_ips.keys(), tablefmt="pretty"))
                                print()
                                print(f"Nilai Bahasa Inggris siswa dengan ID '{id_student_update}' berhasil diubah menjadi '{update_nilai_bing}'")
                                break
                            else:
                                print(f"Nilai Bahasa Inggris gagal diperbarui. Harap masukkan angka 0 - 100.")

            elif update_data_siswa == 3: # User memilih untuk selesai memperbarui data siswa
                print()
                print("Selesai memperbarui data siswa.")
                break

            else:
                print()
                print(f"Opsi tidak tersedia")
                print()

        except ValueError: # Menangkap error jika ada dan menentukan tindakan saat error terjadi
            print()
            print(f"Input tidak valid.")
            print()

# Tampilan menu 5 --> Menampilkan rapor kelas
def menu_5():
    print()
    while True: # Infinite loop selama benar, maka program akan terus berjalan
        try: # Try & Except untuk menangani ketika program terjadi error, Menempatkan Try pada kode yang kemungkinan akan menimbulkan error
            print()
            print(f"Pilihan Untuk Melihat Rapor Kelas:\n\n 1. Rapor kelas jurusan IPA\n 2. Rapor kelas jurusan IPS\n 3. Kembali ke menu utama")
            print()
            menampilkan_rapor_kelas = int(input("Pilih opsi menu 1-3: "))
            if menampilkan_rapor_kelas == 1: # Jika user pilih IPA
            
                keys_terpilih_ipa = list(database_siswa_ipa.keys())[4:]# Keys terpilih untuk menghitung rata2

                values_terpilih_ipa = []

                for key_ipa in keys_terpilih_ipa:
                    values_terpilih_ipa.append(database_siswa_ipa[key_ipa]) # Looping untuk menampilkan nilai2 siswa per pelajaran
            
                rata2_siswa_ipa = []

                for rata2_pelajaran_ipa in zip(*values_terpilih_ipa):
                    rata2_pelajaran_ipa = round((sum(rata2_pelajaran_ipa)/len(rata2_pelajaran_ipa)),3)
                    rata2_siswa_ipa.append(rata2_pelajaran_ipa)

                database_siswa_ipa["rata2_siswa"] = rata2_siswa_ipa

                print(tabulate(database_siswa_ipa,headers = database_siswa_ipa.keys(), tablefmt="pretty"))
                print()

                statistik_nilai_ipa = {}

                for mata_pelajaran_ipa in keys_terpilih_ipa:
                    nilai_pelajaran = database_siswa_ipa[mata_pelajaran_ipa]
                    nilai_max = max(nilai_pelajaran)
                    nilai_min = min(nilai_pelajaran)
                    nilai_average = round((sum(nilai_pelajaran)/len(nilai_pelajaran)),3)

                    statistik_nilai_ipa[mata_pelajaran_ipa] = {"max": nilai_max, # Buat outputnya jadi nested dictionary {nilai_matematika : {max: x, min: y, average: z}} dst
                                                                "min": nilai_min,
                                                                "average": nilai_average}
                    
                for idx,val in statistik_nilai_ipa.items():
                    print(f"Statistik dari {idx} adalah sebagai berikut: ")
                    print(f"Nilai max: {val["max"]}")
                    print(f"Nilai min: {val["min"]}")
                    print(f"Nilai rata-rata: {val["average"]}")
                    print()  

            elif menampilkan_rapor_kelas == 2: # Jika user pilih IPS
            
                keys_terpilih_ips = list(database_siswa_ips.keys())[4:]

                values_terpilih_ips = []

                for key_ips in keys_terpilih_ips:
                    values_terpilih_ips.append(database_siswa_ips[key_ips]) # Looping untuk menampilkan nilai2 siswa per pelajaran
            
                rata2_siswa_ips = []

                for rata2_pelajaran_ips in zip(*values_terpilih_ips):
                    rata2_pelajaran_ips = round((sum(rata2_pelajaran_ips)/len(rata2_pelajaran_ips)),3)
                    rata2_siswa_ips.append(rata2_pelajaran_ips)

                database_siswa_ips["rata2_siswa"] = rata2_siswa_ips

                print(tabulate(database_siswa_ips,headers = database_siswa_ips.keys(), tablefmt="pretty"))
                print()

                statistik_nilai_ips = {}

                for mata_pelajaran_ips in keys_terpilih_ips:
                    nilai_pelajaran = database_siswa_ips[mata_pelajaran_ips]
                    nilai_max = max(nilai_pelajaran)
                    nilai_min = min(nilai_pelajaran)
                    nilai_average = round((sum(nilai_pelajaran)/len(nilai_pelajaran)),3)

                    statistik_nilai_ips[mata_pelajaran_ips] = {"max": nilai_max, # buat outputnya jadi nested dictionary {nilai_matematika : {max: x, min: y, average: z}} dst
                                                                "min": nilai_min,
                                                                "average": nilai_average}
                    
                for idx,val in statistik_nilai_ips.items():
                    print(f"Statistik dari {idx} adalah sebagai berikut: ")
                    print(f"Nilai max: {val["max"]}")
                    print(f"Nilai min: {val["min"]}")
                    print(f"Nilai rata-rata: {val["average"]}")
                    print()  
            
            elif menampilkan_rapor_kelas == 3:
                print()
                print("Selesai melihat rapor kelas.")
                break

            else: # Jawaban jika user pilih selain IPA IPS
                print()
                print(f"Opsi tidak tersedia.")
                print()
        
        except ValueError: # Menangkap error jika ada dan menentukan tindakan saat error terjadi
            print()
            print(f"Input tidak valid.")
            print()

# Tampilan menu 6 --> Menampilkan rapor siswa
def menu_6():
    print()
    while True: # Infinite loop selama benar, maka program akan terus berjalan
        try: # Try & Except untuk menangani ketika program terjadi error, Menempatkan Try pada kode yang kemungkinan akan menimbulkan error
            print()
            print(f"Pilihan Untuk Melihat Rapor Siswa:\n\n 1. Rapor siswa jurusan IPA\n 2. Rapor siswa jurusan IPS\n 3. Kembali ke menu utama")
            print()
            menampilkan_rapor_siswa = int(input("Pilih opsi menu 1-3: "))
            if menampilkan_rapor_siswa == 1:
                print(tabulate(database_siswa_ipa,headers = database_siswa_ipa.keys(), tablefmt="pretty"))
                id_siswa_ipa = input("Masukkan salah satu ID siswa IPA untuk melihat rapor siswa (3 angka): ")
                print()
                if id_siswa_ipa in database_siswa_ipa["id_student"]:
                    find_index = database_siswa_ipa["id_student"].index(id_siswa_ipa) # Menemukan index dari id siswa yang diinput
                    print(f"Berikut adalah nilai rapor dari '{database_siswa_ipa["nama"][find_index]}': ")
                    print()
                    for key in database_siswa_ipa.keys(): # Looping seluruh key pada database
                        print(f"{key} = {database_siswa_ipa[key][find_index]}") # Print seluruh key pada database + value sesuai dengan index
                else:
                    print(f"Siswa dengan ID '{id_siswa_ipa}' tidak ada di dalam 'Database Jurusan IPA'")

            elif menampilkan_rapor_siswa == 2:
                print(tabulate(database_siswa_ips,headers = database_siswa_ips.keys(), tablefmt="pretty"))
                id_siswa_ips = input("Masukkan salah satu ID siswa IPS untuk melihat rapor siswa (3 angka): ")
                print()
                if id_siswa_ips in database_siswa_ips["id_student"]:
                    find_index = database_siswa_ips["id_student"].index(id_siswa_ips)
                    print(f"Berikut adalah nilai rapor dari '{database_siswa_ips["nama"][find_index]}': ")
                    print()
                    for key in database_siswa_ips.keys():
                        print(f"{key} = {database_siswa_ips[key][find_index]}")
                else:
                    print(f"Siswa dengan ID '{id_siswa_ips}' tidak ada di dalam 'Database Jurusan IPS'")

            elif menampilkan_rapor_siswa == 3:
                print()
                print("Selesai melihat rapor kelas.")
                break

            else: # Jawaban jika user pilih selain IPA IPS
                print()
                print(f"Opsi tidak tersedia.")
                print()

        except ValueError: # Menangkap error jika ada dan menentukan tindakan saat error terjadi
            print()
            print(f"Input tidak valid.")
            print()

# Tampilan menu 7 --> Exit program
def menu_7():
    print()
    print("Terima kasih!")
    print()

while True:
    try:
        menu_utama()
        print()
        pilih_menu = int(input(f"Masukkan angka menu yang ingin dijalankan: "))
        if pilih_menu == 1:
            menu_1()
            print()
        elif pilih_menu == 2:
            menu_2()
            print()
        elif pilih_menu == 3:
            menu_3()
            print()
        elif pilih_menu == 4:
            menu_4()
            print()
        elif pilih_menu == 5:
            menu_5()
            print()
        elif pilih_menu == 6:
            menu_6()
            print()
        elif pilih_menu == 7:
            menu_7()
            print()
        else:
            print(f"Data tidak tersedia")
    except ValueError:
        print()
        print(f"Input tidak valid.")
        print()