# Test

## Deskripsi Proyek
Proyek ini bertujuan untuk membangun dan melatih model machine learning untuk:
* **Klasifikasi weekly study hours:** Klasifikasi weekly study hours berdasarkan atribut MathScore, ReadingScore, and WritingScore.
* **Klasifikasi gambar:** Mengklasifikasikan gambar dengan kategori kucing atau anjing.
* **Analisis sentimen:** Menganalisis sentimen teks dalam dataset yang disediakan.

Dataset yang digunakan untuk melatih dan mengevaluasi model disimpan dalam folder `data`. Proses pelatihan dan evaluasi model dilakukan dalam notebook Jupyter yang terdapat dalam folder `notebook`. Model yang telah dilatih kemudian diunggah ke Hugging Face untuk dibagikan dan digunakan lebih lanjut.

## Struktur Folder
* **.venv:** Lingkungan virtual Python untuk mengelola dependensi proyek.
* **data:** Berisi dataset yang digunakan dalam berbagai tahap proyek, termasuk teks untuk analisis sentimen dan gambar kucing serta anjing untuk klasifikasi.
* **model:** Menyimpan model yang telah dilatih dan siap digunakan.
* **notebook:** Berisi notebook Jupyter untuk:
    * **Preprocessing data:** Membersihkan dan mempersiapkan data untuk pelatihan model.
    * **Pelatihan model:** Melatih model untuk tugas analisis sentimen dan klasifikasi gambar.
    * **Evaluasi model:** Mengevaluasi kinerja model pada data uji.
    * **Deployment:** Mengunggah model ke Hugging Face.
* **others:** Berisi file tambahan seperti label, konfigurasi, dll.
* **pyfile:** Berisi skrip Python yang digunakan dalam proyek.
* **.gitignore:** Menentukan file yang tidak perlu di-track oleh Git.
* **README.md:** File ini (Anda sedang membacanya).
* **requirements.txt:** Mencantumkan daftar dependensi proyek.

## Cara Menggunakan
1. **Kloning Repositori:**
   ```bash
   git clone https://github.com/tribber93/Test_YoniTribber.git
   cd Test_YoniTribber

Membuat Lingkungan Virtual:

    python -m venv venv
    source venv/bin/activate

Instal Dependensi:

    pip install -r requirements.txt

Menjalankan Notebook: 

Gunakan Jupyter Notebook untuk menjalankan notebook yang ada di folder notebook.


Model yang telah dilatih dapat ditemukan di: 
- [Model Klasifikasi Weekly Study Hours](https://huggingface.co/tribber93/test-classification-model)
- [Model Klasifikasi Gambar](https://huggingface.co/tribber93/test-image-classification-model)
- [Model Sentimen Analisis](https://huggingface.co/tribber93/test-sentimen-analisis)
