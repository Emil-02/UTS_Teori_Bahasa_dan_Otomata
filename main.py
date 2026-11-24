from input_otomata import get_contoh_dfa, get_contoh_nfa, input_otomata_manual, cetak_tabel
from dfa import simulasi_dfa
from nfa import simulasi_nfa
from konversi import konversi_nfa_ke_dfa, uji_ekivalensi


def pilih_sumber_data(jenis):
    print(f"\nPilih sumber data {jenis}:")
    print("1. Gunakan contoh bawaan")
    print("2. Input manual sendiri")
    sub = input("Pilihan (1/2): ").strip()
    if sub == "2":
        return input_otomata_manual(jenis)
    return get_contoh_dfa() if jenis == "DFA" else get_contoh_nfa()
def main():
    while True:
        print("\n==========================================")
        print("  PROGRAM TEORI BAHASA & OTOMATA (CLI)")
        print("==========================================")
        print("1. Simulasi DFA")
        print("2. Simulasi NFA")
        print("3. Konversi NFA ke DFA + Uji Ekivalensi")
        print("4. Keluar")

        pilihan = input("Pilih menu (1-4): ").strip()

        if pilihan == "1":
            dfa = pilih_sumber_data("DFA")
            cetak_tabel(dfa, "DFA")
            s = input("\nMasukkan string uji: ")
            simulasi_dfa(dfa, s)

        elif pilihan == "2":
            nfa = pilih_sumber_data("NFA")
            cetak_tabel(nfa, "NFA")
            s = input("\nMasukkan string uji: ")
            simulasi_nfa(nfa, s)

        elif pilihan == "3":
            nfa = pilih_sumber_data("NFA")
            cetak_tabel(nfa, "NFA (Asli)")

            print("\nMemproses konversi NFA ke DFA...")
            dfa_hasil = konversi_nfa_ke_dfa(nfa)
            cetak_tabel(dfa_hasil, "DFA (Hasil Konversi)")

            uji = input("\nIngin uji ekivalensi dengan string? (y/n): ").strip().lower()
            if uji == "y":
                s = input("Masukkan string uji: ")
                uji_ekivalensi(nfa, dfa_hasil, s)

        elif pilihan == "4":
            print("Program selesai.")
            break
        else:
            print("Pilihan tidak valid, silakan coba lagi.")


if __name__ == "__main__":
    main()