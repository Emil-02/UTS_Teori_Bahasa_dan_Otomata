def simulasi_dfa(dfa, string_input, tampilkan_jejak=True):
    """Menguji apakah string_input diterima oleh DFA. Mengembalikan True/False."""
    if tampilkan_jejak:
        print(f"\n[SIMULASI DFA] Menguji string: '{string_input}'")

    state_sekarang = dfa["start"]
    if tampilkan_jejak:
        print(f"Start State: {state_sekarang}")

    for simbol in string_input:
        if simbol not in dfa["alphabet"]:
            print(f"Error: Simbol '{simbol}' tidak ada di alfabet {dfa['alphabet']}!")
            return None

        state_berikutnya = dfa["transitions"].get((state_sekarang, simbol))
        if tampilkan_jejak:
            print(f"  δ({state_sekarang}, '{simbol}') -> {state_berikutnya}")
        state_sekarang = state_berikutnya

    diterima = state_sekarang in dfa["final"]
    if tampilkan_jejak:
        status = "ACCEPTED" if diterima else "REJECTED"
        print(f"Hasil DFA: {status} (State akhir: {state_sekarang})")

    return diterima