# To-Do List API (devsecops-p5-0110225138-Alyadwic)

## 1. Nama Aplikasi & Fungsi
**To-Do List API** adalah aplikasi REST API sederhana untuk mengelola daftar tugas.
Fitur: menambah tugas, melihat semua tugas, menandai tugas selesai, dan menghapus tugas.

## 2. Bahasa & Framework
- Python 3.11
- Flask (web framework)
- Pytest (unit testing)

## 3. Cara Menjalankan
```bash
python3 -m venv venv
source venv/bin/activate
python -m pip install -r requirements.txt
python -m pytest        # menjalankan unit test
python app.py           # menjalankan aplikasi
```
Buka `http://127.0.0.1:5000/tasks` (atau port 5001 jika port 5000 bentrok).

| Method | Endpoint | Fungsi |
|--------|----------|--------|
| GET | /tasks | Daftar semua tugas |
| POST | /tasks | Tambah tugas (`{"title": "..."}`) |
| PUT | /tasks/{id}/done | Tandai selesai |
| DELETE | /tasks/{id} | Hapus tugas |

## 4. Overview Pipeline CI/CD
Pipeline memakai **GitHub Actions** (`.github/workflows/devsecops.yml`), terpicu pada `push` dan `pull_request` ke branch `main`.

1. **Job `build`**: install dependencies dan menjalankan unit test dengan pytest.
2. **Job `sast-scan`** (bergantung pada `build` lewat `needs: build`): menjalankan **Bandit** untuk analisis keamanan kode, menyimpan laporan sebagai artifact, lalu menerapkan **Quality Gate**: pipeline gagal jika ditemukan kerentanan severity **Medium atau High**.
