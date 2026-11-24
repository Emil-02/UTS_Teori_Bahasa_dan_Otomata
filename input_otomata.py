def get_contoh_dfa():
    """Contoh bawaan DFA: Menerima string biner yang diakhiri '1'."""
    return {
        "states": {"q0", "q1"},
        "alphabet": ["0", "1"],
        "start": "q0",
        "final": {"q1"},
        "transitions": {
            ("q0", "0"): "q0",
            ("q0", "1"): "q1",
            ("q1", "0"): "q0",
            ("q1", "1"): "q1",
        },
    }


def get_contoh_nfa():
    """Contoh bawaan NFA: Menerima string biner yang diakhiri '01'."""
    return {
        "states": {"q0", "q1", "q2"},
        "alphabet": ["0", "1"],
        "start": "q0",
        "final": {"q2"},
        "transitions": {
            ("q0", "0"): {"q0", "q1"},
            ("q0", "1"): {"q0"},
            ("q1", "1"): {"q2"},
        },
    }


def input_otomata_manual(jenis="DFA"):
    """Meminta user memasukkan definisi 5-tuple DFA atau NFA lewat CLI."""
    print(f"\n--- INPUT {jenis} MANUAL ---")
    states = set(input("Masukkan semua state (pisah koma, misal q0,q1,q2): ").replace(" ", "").split(","))
    alphabet = input("Masukkan alfabet (pisah koma, misal 0,1): ").replace(" ", "").split(",")
    start = input("Masukkan start state (misal q0): ").strip()
    final = set(input("Masukkan final state (pisah koma, misal q2): ").replace(" ", "").split(","))

    transitions = {}
    print("\nMasukkan fungsi transisi:")
    for st in sorted(states):
        for sym in alphabet:
            if jenis == "DFA":
                tujuan = input(f"  δ({st}, '{sym}') -> ").strip()
                transitions[(st, sym)] = tujuan
            else:
                raw = input(f"  δ({st}, '{sym}') [pisah koma, kosongkan jika tidak ada] -> ").strip()
                if raw:
                    transitions[(st, sym)] = set(raw.replace(" ", "").split(","))
                else:
                    transitions[(st, sym)] = set()

    return {
        "states": states,
        "alphabet": alphabet,
        "start": start,
        "final": final,
        "transitions": transitions,
    }


def cetak_tabel(otomata, jenis="DFA"):
    """Menampilkan tabel transisi otomata secara rapi di terminal."""
    print(f"\nTabel Transisi {jenis}:")
    alphabet = otomata["alphabet"]
    header = f"{'State':<18} | " + " | ".join(f"Input '{a}'".ljust(14) for a in alphabet)
    print("-" * len(header))
    print(header)
    print("-" * len(header))

    for st in sorted(otomata["states"]):
        label = st
        if st == otomata["start"]:
            label = "-> " + label
        if st in otomata["final"]:
            label = "* " + label

        baris = f"{label:<18} | "
        kolom = []
        for sym in alphabet:
            if jenis == "DFA":
                tujuan = otomata["transitions"].get((st, sym), "-")
            else:
                tujuan_set = otomata["transitions"].get((st, sym), set())
                tujuan = "{" + ", ".join(sorted(tujuan_set)) + "}" if tujuan_set else "∅"
            kolom.append(tujuan.ljust(14))
        print(baris + " | ".join(kolom))

    print("-" * len(header))
    print("Keterangan: (->) Start State, (*) Final State, (∅) Kosong / Dead State")