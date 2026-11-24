from dfa import simulasi_dfa
from nfa import simulasi_nfa


def format_state(state_set):
    """Mengubah frozenset menjadi teks rapi, misal {q0, q1} atau ∅."""
    if not state_set:
        return "∅"
    return "{" + ", ".join(sorted(state_set)) + "}"


def konversi_nfa_ke_dfa(nfa):
    """Mengonversi NFA menjadi DFA menggunakan algoritma Subset Construction."""
    start_frozen = frozenset([nfa["start"]])
    antrean = [start_frozen]
    sudah_diproses = {start_frozen}
    transisi_baru = {}
    final_baru = set()

    while antrean:
        state_sekarang = antrean.pop(0)

        # Jika gabungan state mengandung final state NFA, jadikan final state DFA
        if state_sekarang & nfa["final"]:
            final_baru.add(state_sekarang)

        for simbol in nfa["alphabet"]:
            tujuan_gabungan = set()
            for st in state_sekarang:
                tujuan_gabungan.update(nfa["transitions"].get((st, simbol), set()))

            tujuan_frozen = frozenset(tujuan_gabungan)
            transisi_baru[(state_sekarang, simbol)] = tujuan_frozen

            if tujuan_frozen not in sudah_diproses:
                sudah_diproses.add(tujuan_frozen)
                antrean.append(tujuan_frozen)

    # Kembalikan dalam format dictionary DFA standar agar bisa langsung disimulasikan
    return {
        "states": {format_state(st) for st in sudah_diproses},
        "alphabet": list(nfa["alphabet"]),
        "start": format_state(start_frozen),
        "final": {format_state(st) for st in final_baru},
        "transitions": {
            (format_state(st), sym): format_state(tujuan)
            for (st, sym), tujuan in transisi_baru.items()
        },
    }


def uji_ekivalensi(nfa, dfa_hasil, string_input):
    """Menguji string yang sama pada NFA asli dan DFA hasil konversi."""
    print(f"\n=== UJI EKIVALENSI UNTUK STRING: '{string_input}' ===")
    hasil_nfa = simulasi_nfa(nfa, string_input, tampilkan_jejak=True)
    hasil_dfa = simulasi_dfa(dfa_hasil, string_input, tampilkan_jejak=True)

    if hasil_nfa is None or hasil_dfa is None:
        return

    print("\n--- KESIMPULAN EKIVALENSI ---")
    if hasil_nfa == hasil_dfa:
        print("TERBUKTI EKIVALEN! NFA dan DFA hasil konversi memberikan keputusan yang sama.")
    else:
        print("TIDAK EKIVALEN! Periksa kembali definisi transisi.")