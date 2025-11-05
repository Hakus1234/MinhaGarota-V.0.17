layeredimage tempo_mapa:

    if tempo == 0:
        "extra/tempo_0.png"

    elif tempo == 1:
        "extra/tempo_1.png"

    elif tempo == 2:
        "extra/tempo_2.png"

    elif tempo >= 3:
        "extra/tempo_3.png"

layeredimage casa:

    if tempo <= 1:
        Movie(play='fundo_1.webm')

    elif tempo == 2:
        Movie(play='fundo_2.webm')

    else:
        Movie(play='fundo_3.webm')

    if chovendo:
        "fundo_chuva"
    if chovendo:
        Movie(play="chuva.webm", mask="chuva_mask.webm")

    group local:

        attribute estudo:
            "casa_estudo"

        attribute sala:
            "casa_sala_new"

        attribute sala2:
            "casa_sala2"

        attribute quarto:
            "quarto"

layeredimage cidade:

    if tempo <= 1:
        Movie(play='fundo_1.webm')

    elif tempo == 2:
        Movie(play='fundo_2.webm')

    else:
        Movie(play='fundo_3.webm')

    if chovendo:
        "fundo_chuva"
    if chovendo:
        Movie(play="chuva.webm", mask="chuva_mask.webm")

    group local:

        attribute cinema:
            "cidade_cinema"

layeredimage mc:

    if tempo <= 1:
        Movie(play='fundo_1.webm')

    elif tempo == 2:
        Movie(play='fundo_2.webm')

    else:
        Movie(play='fundo_3.webm')

    if chovendo:
        "fundo_chuva"
    if chovendo:
        Movie(play="chuva.webm", mask="chuva_mask.webm")

    group local:

        attribute insta2:
            "mc_insta2"

        attribute mc_celular16:
            "mc_celular16"

layeredimage praia:

    if tempo <= 1:
        Movie(play='fundo_1.webm')

    elif tempo == 2:
        Movie(play='fundo_2.webm')

    else:
        Movie(play='fundo_3.webm')

    if chovendo:
        "fundo_chuva"
    if chovendo:
        Movie(play="chuva.webm", mask="chuva_mask.webm")

    group local:

        attribute praia1:
            "praia1"

        attribute praia2:
            "praia2"

        attribute praia5:
            "praia5"

        attribute praia7:
            "praia7"

        attribute praia9:
            "praia9"

        attribute praia11:
            "praia11"

        attribute praia17:
            "praia17"

        attribute praia19:
            "praia19"

        attribute praia20:
            "praia20"

        attribute praia21:
            "praia21"

        attribute praia24:
            "praia24"

        attribute praia26:
            "praia26"

        attribute praia29:
            "praia29"

        attribute praia31:
            "praia31"

        attribute praia32:
            "praia32"

        attribute praia34:
            "praia34"

        attribute praia35:
            "praia35"

        attribute praia36:
            "praia36"

        attribute praia37:
            "praia37"

        attribute praia38:
            "praia38"

        attribute praia39:
            "praia39"

        attribute praia44:
            "praia44"

        attribute praia49:
            "praia49"

        attribute praia50:
            "praia50"

        attribute praia51:
            "praia51"

        attribute praia52:
            "praia52"

        attribute praia55:
            "praia55"

        attribute praia56:
            "praia56"

        attribute praia58:
            "praia58"

        attribute praia60:
            "praia60"

        attribute praia62:
            "praia62"

        attribute praia63:
            "praia63"

        attribute praia64:
            "praia64"

        attribute praia65:
            "praia65"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
