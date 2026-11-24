# UTS Teori Bahasa dan Otomata

Program CLI untuk mensimulasikan **DFA**, **NFA**, dan **konversi NFA ke DFA** menggunakan algoritma *Subset Construction*. Dibuat untuk memenuhi tugas UTS mata kuliah Teori Bahasa dan Otomata.

## Fitur

- **Simulasi DFA** — menguji apakah sebuah string diterima oleh DFA, lengkap dengan jejak transisi tiap simbol.
- **Simulasi NFA** — menelusuri himpunan state aktif dan menampilkan jejak transisi.
- **Konversi NFA ke DFA** — *Subset Construction*, menampilkan tabel DFA hasil konversi.
- **Uji ekivalensi** — membandingkan keputusan NFA asli dengan DFA hasil konversi untuk string yang sama.
- **Input manual** — mendefinisikan 5-tuple sendiri lewat terminal, atau memakai contoh bawaan.

## Struktur Proyek

| File | Deskripsi |
| --- | --- |
| `main.py` | Menu utama (CLI) |
| `dfa.py` | Simulasi DFA |
| `nfa.py` | Simulasi NFA |
| `konversi.py` | Konversi NFA ke DFA + uji ekivalensi |
| `input_otomata.py` | Contoh otomata, input manual, dan pencetakan tabel transisi |

## Menjalankan

Prasyarat: Python 3.10+ (tanpa dependensi eksternal).

```bash
python main.py
```

Contoh alur:

1. Pilih `1` untuk simulasi DFA.
2. Pilih `1` untuk memakai contoh bawaan.
3. Masukkan string uji, misalnya `011`.

Untuk konversi NFA ke DFA, pilih menu `3`, lalu masukkan string uji saat diminta.

## Tim

- [@Emil-02](https://github.com/Emil-02)
- [@muhamad-pasyafatir-adiyat](https://github.com/muhamad-pasyafatir-adiyat)
- [@AhmadAliDwilZaydi](https://github.com/AhmadAliDwilZaydi)
- [@rwfly06](https://github.com/rwfly06)

## Lisensi

[MIT](LICENSE)
