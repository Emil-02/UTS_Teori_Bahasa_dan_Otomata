def simulasi_nfa(nfa, string_input, tampilkan_jejak=True):
    """Menguji apakah string_input diterima oleh NFA. Mengembalikan True/False."""
    if tampilkan_jejak:
        print(f"\n[SIMULASI NFA] Menguji string: '{string_input}'")

    state_aktif = {nfa["start"]}
    if tampilkan_jejak:
        print(f"Start State: {state_aktif}")

    for simbol in string_input:
        if simbol not in nfa["alphabet"]:
            print(f"Error: Simbol '{simbol}' tidak ada di alfabet {nfa['alphabet']}!")
            return None

        state_berikutnya = set()
        for st in state_aktif:
            tujuan = nfa["transitions"].get((st, simbol), set())
            state_berikutnya.update(tujuan)

        if tampilkan_jejak:
            tampil = state_berikutnya if state_berikutnya else "∅ (Kosong)"
            print(f"  δ({state_aktif}, '{simbol}') -> {tampil}")
        state_aktif = state_berikutnya

    # Diterima jika ada irisan (&) antara state_aktif dan final state
    diterima = bool(state_aktif & nfa["final"])
    if tampilkan_jejak:
        status = "ACCEPTED" if diterima else "REJECTED"
        tampil_akhir = state_aktif if state_aktif else "∅"
        print(f"Hasil NFA: {status} (State akhir: {tampil_akhir})")

    return diterima