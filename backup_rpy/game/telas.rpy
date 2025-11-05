screen navegar():
    tag navegar

    modal True
    zorder 99

    predict False

    use tempo_mapa

    if area == "tutorial":

        if mapa == "parte1":

            frame:

                background None
                xalign 0.794
                yalign 0.31

                imagebutton auto "extra/icone_action_%s.webp" at flutuando, z05:
                    xalign 0.5
                    yalign 0.5
                    action Jump("intro_parte3")

        elif mapa == "parte2":

            frame:

                background None
                xanchor 0.5
                yanchor 0.5
                yalign 0.98
                xalign 0.5

                imagebutton auto "extra/icone_porta_%s.webp" at flutuando:
                    xalign 0.5
                    yalign 0.5
                    action Jump("intro_parte4")

        elif mapa == "parte3":

            frame:

                background None
                xalign 0.425
                yalign 0.35

                imagebutton auto "extra/icone_porta_%s.webp" at flutuando, z05:
                    xalign 0.5
                    yalign 0.5
                    action Jump("gabriel_evento")

        elif mapa == "guardar":

            frame:

                background None
                xalign 0.51
                yalign 0.4

                imagebutton auto "extra/icone_porta_%s.webp" at flutuando:
                    xalign 0.5
                    yalign 0.5
                    action Jump("tutorial_parte2")

            frame:

                background None
                xalign 0.451
                yalign 0.17

                imagebutton auto "extra/botao_fala_%s.png" at flutuando:
                    xalign 0.5
                    yalign 0.5
                    action Jump("tutorial_parte3")

            frame:

                background None
                xalign 0.7
                yalign 0.55

                imagebutton auto "extra/botao_dormir_%s.png" at flutuando:
                    xalign 0.5
                    yalign 0.5
                    action Jump("tutorial_parte4")

            frame:

                background None
                xalign 0.11
                yalign 0.3

                imagebutton auto "extra/icone_action_%s.webp" at flutuando:
                    xalign 0.5
                    yalign 0.5
                    action Jump("tutorial_roupa")

    elif area == "mapa":

        frame:

            background None
            xalign 0.96
            yalign 0.9

            imagebutton idle "mapa_casa.webp" at flutuando:
                xalign 0.5
                yalign 0.5
                action Jump("corredor")

        frame:

            background None
            xalign 0.145
            yalign 0.85

            imagebutton idle "mapa_bar.webp" at flutuando:
                xalign 0.5
                yalign 0.5
                action Jump("boteco")


        if zaza >= 7:

            frame:

                background None
                xalign 0.435
                yalign 0.41

                imagebutton idle "mapa_boutique.webp" at flutuando:
                    xalign 0.5
                    yalign 0.5
                    action Jump("boutique")

        if mercado > 0:

            frame:

                background None
                xalign 0.605
                yalign 0.195

                imagebutton idle "mapa_mercado.webp" at flutuando:
                    xalign 0.5
                    yalign 0.5
                    action Jump("mercado")

    elif area == "casa":

        if mapa == "sala":

            frame:

                background None
                xalign 0.794
                yalign 0.31

                imagebutton auto "extra/icone_action_%s.webp" at flutuando, z05:
                    xalign 0.5
                    yalign 0.5
                    action Jump("espelho")

            frame:

                background None
                xanchor 0.5
                yanchor 0.5
                yalign 0.98
                xalign 0.5

                imagebutton auto "extra/icone_porta_%s.webp" at flutuando:
                    xalign 0.5
                    yalign 0.5
                    action Jump("corredor")

            frame:

                background None
                xalign 0.18
                yalign 0.45

                imagebutton idle "extra/botao_dormir_idle.png" at flutuando, z04:
                    xalign 0.5
                    yalign 0.5
                    action Jump("cama")

            frame:

                background None
                xalign 0.71
                yalign 0.55

                imagebutton auto "extra/icone_action_%s.webp" at flutuando, z07:
                    xalign 0.5
                    yalign 0.5
                    action Jump("celular")

            frame:

                background None
                xalign 0.865
                yalign 0.53

                imagebutton idle "extra/icone_livros_idle.webp" at flutuando, z065:
                    xalign 0.5
                    yalign 0.5
                    action Jump("estudar")

            frame:

                background None
                xalign 0.085
                yalign 0.46

                imagebutton auto "extra/icone_action_%s.webp" at flutuando, z05:
                    xalign 0.5
                    yalign 0.5
                    action Jump("tv")

            imagebutton auto "extra/seta_%s.png" at seta_direita action Jump("sala2")

        elif mapa == "sala2":

            frame:

                background None
                xanchor 0.5
                yanchor 0.5
                yalign 0.45
                xalign 0.877

                imagebutton auto "extra/icone_porta_%s.webp" at flutuando, z09:
                    xalign 0.5
                    yalign 0.5
                    action Jump("banheiro")

            imagebutton auto "extra/seta_%s.png" at seta_esquerda action Jump("sala")

        elif mapa == "corredor":

            frame:

                background None
                xalign 0.36
                yalign 0.3

                imagebutton auto "extra/icone_porta_%s.webp" at flutuando, z04:
                    xalign 0.5
                    yalign 0.5
                    action Jump("sala")

            frame:

                background None
                xalign 0.425
                yalign 0.35

                imagebutton auto "extra/icone_porta_%s.webp" at flutuando, z05:
                    xalign 0.5
                    yalign 0.5
                    action Jump("gabriel_evento")

            frame:

                background None
                xanchor 0.5
                yanchor 0.5
                yalign 0.98
                xalign 0.5

                imagebutton auto "extra/icone_mapa_%s.webp" at flutuando:
                    xalign 0.5
                    yalign 0.5
                    action Jump("mapa")

    elif area == "boteco":

        if mapa == "boteco1":

            frame:

                background None
                xalign 0.714
                yalign 0.26

                imagebutton auto "extra/botao_fala_%s.png" at flutuando, z06:
                    xalign 0.5
                    yalign 0.5
                    action Jump("jasper_evento")

            if trabalho >= 8:

                frame:

                    background None
                    xalign 0.32
                    yalign 0.38

                    imagebutton auto "extra/icone_action_%s.webp" at flutuando, z07:
                        xalign 0.5
                        yalign 0.5
                        action Jump("trabalhar")

            if fama > 0:

                frame:

                    background None
                    xalign 0.453
                    yalign 0.29

                    imagebutton auto "extra/botao_fala_%s.png" at flutuando, z045:
                        xalign 0.5
                        yalign 0.5
                        action Jump("akemi_evento")

            frame:

                background None
                xanchor 0.5
                yanchor 0.5
                yalign 0.98
                xalign 0.5

                imagebutton auto "extra/icone_mapa_%s.webp" at flutuando:
                    xalign 0.5
                    yalign 0.5
                    action Jump("mapa")

    elif area == "boutique":

        if mapa == "boutique1":

            frame:

                background None
                xalign 0.171
                yalign 0.253

                imagebutton auto "extra/botao_fala_%s.png" at flutuando, z05:
                    xalign 0.5
                    yalign 0.5
                    action Jump("nathan_evento")

            frame:

                background None
                xalign 0.71
                yalign 0.3

                imagebutton auto "extra/icone_action_%s.webp" at flutuando, z08:
                    xalign 0.5
                    yalign 0.5
                    action Jump("boutique_evento")

            frame:

                background None
                xanchor 0.5
                yanchor 0.5
                yalign 0.98
                xalign 0.5

                imagebutton auto "extra/icone_mapa_%s.webp" at flutuando:
                    xalign 0.5
                    yalign 0.5
                    action Jump("corredor")

    elif area == "mercado":

        if mapa == "mercado1":

            frame:

                background None
                xalign 0.972
                yalign 0.72

                imagebutton auto "extra/icone_action_%s.webp" at flutuando, z08:
                    xalign 0.5
                    yalign 0.5
                    action Jump("mercado_evento")

            frame:

                background None
                xanchor 0.5
                yanchor 0.5
                yalign 0.98
                xalign 0.5

                imagebutton auto "extra/icone_mapa_%s.webp" at flutuando:
                    xalign 0.5
                    yalign 0.5
                    action Jump("corredor")

screen menu_perfil():
    tag principal

    modal True
    zorder 98

    frame:

        xysize (1280, 720)
        background "menu_fundo.webp"

        has hbox

        spacing 30

        frame:

            background None
            xysize (263, 720)

            use menu_lateral

        frame:

            background None
            xysize (977, 720)
            xalign 0.5
            xanchor 0.5

            has vbox

            spacing 30
            xalign 0.5
            xanchor 0.5

            text "Perfil e Conquistas":
                size 36
                xalign 0.5
                text_align 0.5
                outlines [(0, "#000", 2, 2)]

            text "Data: [semana_dia], [dia]/[mes] - Dinheiro: C$ [dinheiro] - Moedas de Ouro: [moeda]":
                size 24
                xalign 0.5
                text_align 0.5
                outlines [(0, "#000", 1, 1)]

            hbox:

                spacing 40

                vbox:

                    spacing 20

                    hbox:

                        spacing 20
                        xalign 0.5
                        xanchor 0.5

                        add "menu_aries.webp"

                        vbox:

                            spacing 1

                            text "Áries (Coragem)":
                                size 18
                                xalign 0.5
                                yalign 0.5
                                outlines [(0, "#000", 1, 1)]

                            bar:
                                xalign 0.5
                                yalign 0.5
                                xsize 250
                                ysize 40
                                value coragem
                                range 30

                        text "[coragem]":
                            size 36
                            xalign 0.5
                            yalign 0.5
                            outlines [(0, "#000", 2, 2)]

                    hbox:

                        spacing 20
                        xalign 0.5
                        xanchor 0.5

                        add "menu_escorpiao.webp"

                        vbox:

                            spacing 1

                            text "Escorpião (Sexualidade)":
                                size 18
                                xalign 0.5
                                yalign 0.5
                                outlines [(0, "#000", 1, 1)]

                            bar:
                                xalign 0.5
                                yalign 0.5
                                xsize 250
                                ysize 40
                                value sexualidade
                                range sexualidade_max

                        text "[sexualidade]":
                            size 36
                            xalign 0.5
                            yalign 0.5
                            outlines [(0, "#000", 2, 2)]

                    hbox:

                        spacing 20
                        xalign 0.5
                        xanchor 0.5

                        if trabalho_exp > 0:

                            add "menu_touro.webp"

                            vbox:

                                spacing 1

                                text "Touro (Trabalho)":
                                    size 18
                                    xalign 0.5
                                    yalign 0.5
                                    outlines [(0, "#000", 1, 1)]

                                bar:
                                    xalign 0.5
                                    yalign 0.5
                                    xsize 250
                                    ysize 40
                                    value trabalho_exp
                                    range trabalho_exp_max

                            text "[trabalho_exp]":
                                size 36
                                xalign 0.5
                                yalign 0.5
                                outlines [(0, "#000", 2, 2)]

                        else:

                            add "menu_question.webp"

                            bar:
                                xalign 0.5
                                yalign 0.5
                                xsize 250
                                ysize 40
                                value 0
                                range 30

                            text "0":
                                size 36
                                xalign 0.5
                                yalign 0.5
                                outlines [(0, "#000", 2, 2)]

                    hbox:

                        spacing 20
                        xalign 0.5
                        xanchor 0.5

                        if estudo > 0:

                            add "menu_gemeos.webp"

                            vbox:

                                spacing 1

                                text "Gêmeos (Estudo)":
                                    size 18
                                    xalign 0.5
                                    yalign 0.5
                                    outlines [(0, "#000", 1, 1)]

                                bar:
                                    xalign 0.5
                                    yalign 0.5
                                    xsize 250
                                    ysize 40
                                    value estudo
                                    range estudo_max

                            text "[estudo]":
                                size 36
                                xalign 0.5
                                yalign 0.5
                                outlines [(0, "#000", 2, 2)]

                        else:

                            add "menu_question.webp"

                            bar:
                                xalign 0.5
                                yalign 0.5
                                xsize 250
                                ysize 40
                                value 0
                                range 30

                            text "0":
                                size 36
                                xalign 0.5
                                yalign 0.5
                                outlines [(0, "#000", 2, 2)]

                    hbox:

                        spacing 20
                        xalign 0.5
                        xanchor 0.5

                        add "menu_sagitario.webp"

                        vbox:

                            spacing 1

                            text "Sagitário (Autoestima)":
                                size 18
                                xalign 0.5
                                yalign 0.5
                                outlines [(0, "#000", 1, 1)]

                            bar:
                                xalign 0.5
                                yalign 0.5
                                xsize 250
                                ysize 40
                                value cuidado
                                range cuidado_max

                        text "[cuidado]":
                            size 36
                            xalign 0.5
                            yalign 0.5
                            outlines [(0, "#000", 2, 2)]

                vbox:

                    spacing 20

                    hbox:

                        spacing 20
                        xalign 0.5
                        xanchor 0.5

                        if fama_pontos > 0:

                            add "menu_leao.webp"

                            vbox:

                                spacing 1

                                text "Leão (Fama)":
                                    size 18
                                    xalign 0.5
                                    yalign 0.5
                                    outlines [(0, "#000", 1, 1)]

                                bar:
                                    xalign 0.5
                                    yalign 0.5
                                    xsize 250
                                    ysize 40
                                    value fama_pontos
                                    range fama_max

                            text "[fama_pontos]":
                                size 36
                                xalign 0.5
                                yalign 0.5
                                outlines [(0, "#000", 2, 2)]

                        else:

                            add "menu_question.webp"

                            bar:
                                xalign 0.5
                                yalign 0.5
                                xsize 250
                                ysize 40
                                value 0
                                range 30

                            text "0":
                                size 36
                                xalign 0.5
                                yalign 0.5
                                outlines [(0, "#000", 2, 2)]

                    hbox:

                        spacing 20
                        xalign 0.5
                        xanchor 0.5

                        if exibicionismo_pontos > 0:

                            add "menu_libra.webp"

                            vbox:

                                spacing 1

                                text "Libra (Romantismo)":
                                    size 18
                                    xalign 0.5
                                    yalign 0.5
                                    outlines [(0, "#000", 1, 1)]

                                bar:
                                    xalign 0.5
                                    yalign 0.5
                                    xsize 250
                                    ysize 40
                                    value exibicionismo_pontos
                                    range exibicionismo_max

                            text "[exibicionismo_pontos]":
                                size 36
                                xalign 0.5
                                yalign 0.5
                                outlines [(0, "#000", 2, 2)]

                        else:

                            add "menu_question.webp"

                            bar:
                                xalign 0.5
                                yalign 0.5
                                xsize 250
                                ysize 40
                                value 0
                                range 30

                            text "0":
                                size 36
                                xalign 0.5
                                yalign 0.5
                                outlines [(0, "#000", 2, 2)]

                    hbox:

                        spacing 20
                        xalign 0.5
                        xanchor 0.5

                        add "menu_question.webp"

                        bar:
                            xalign 0.5
                            yalign 0.5
                            xsize 250
                            ysize 40
                            value 0
                            range 30

                        text "0":
                            size 36
                            xalign 0.5
                            yalign 0.5
                            outlines [(0, "#000", 2, 2)]

                    hbox:

                        spacing 20
                        xalign 0.5
                        xanchor 0.5

                        add "menu_question.webp"

                        bar:
                            xalign 0.5
                            yalign 0.5
                            xsize 250
                            ysize 40
                            value 0
                            range 30

                        text "0":
                            size 36
                            xalign 0.5
                            yalign 0.5
                            outlines [(0, "#000", 2, 2)]

                    hbox:

                        spacing 20
                        xalign 0.5
                        xanchor 0.5

                        add "menu_question.webp"

                        bar:
                            xalign 0.5
                            yalign 0.5
                            xsize 250
                            ysize 40
                            value 0
                            range 30

                        text "0":
                            size 36
                            xalign 0.5
                            yalign 0.5
                            outlines [(0, "#000", 2, 2)]

screen menu_relacionamentos():
    tag principal

    modal True
    zorder 98

    frame:

        xysize (1280, 720)
        background "menu_fundo.webp"

        has hbox

        spacing 30

        frame:

            background None
            xysize (263, 720)

            use menu_lateral

        frame:

            background None
            xysize (977, 720)
            xalign 0.5
            xanchor 0.5

            has vbox

            spacing 30
            xalign 0.5
            xanchor 0.5

            text "Relacionamentos":
                size 36
                xalign 0.5
                text_align 0.5
                outlines [(0, "#000", 2, 2)]

            text "Como vai sua relação com cada pessoa que você conhece?":
                size 24
                xalign 0.5
                text_align 0.5
                outlines [(0, "#000", 1, 1)]






            hbox:

                spacing 40

                vbox:

                    spacing 20

                    hbox:

                        spacing 20
                        xalign 0.5
                        xanchor 0.5

                        if gabriel_pontos > 0:

                            add "menu_gabriel.webp"

                            vbox:

                                spacing 1

                                text "Gabriel (vizinho)":
                                    size 18
                                    xalign 0.5
                                    yalign 0.5
                                    outlines [(0, "#000", 1, 1)]

                                bar:
                                    xalign 0.5
                                    yalign 0.5
                                    xsize 250
                                    ysize 40
                                    value gabriel_pontos
                                    range gabriel_pontos_max

                            text "[gabriel_pontos]":
                                size 36
                                xalign 0.5
                                yalign 0.5
                                outlines [(0, "#000", 2, 2)]

                        else:

                            add "menu_question.webp"

                            bar:
                                xalign 0.5
                                yalign 0.5
                                xsize 250
                                ysize 40
                                value 0
                                range 30

                            text "0":
                                size 36
                                xalign 0.5
                                yalign 0.5
                                outlines [(0, "#000", 2, 2)]

                    hbox:

                        spacing 20
                        xalign 0.5
                        xanchor 0.5

                        if fernando_pontos > 0:

                            add "menu_fernando.webp"

                            vbox:

                                spacing 1

                                text "Fernando (locador)":
                                    size 18
                                    xalign 0.5
                                    yalign 0.5
                                    outlines [(0, "#000", 1, 1)]

                                bar:
                                    xalign 0.5
                                    yalign 0.5
                                    xsize 250
                                    ysize 40
                                    value fernando_pontos
                                    range fernando_pontos_max

                            text "[fernando_pontos]":
                                size 36
                                xalign 0.5
                                yalign 0.5
                                outlines [(0, "#000", 2, 2)]

                        else:

                            add "menu_question.webp"

                            bar:
                                xalign 0.5
                                yalign 0.5
                                xsize 250
                                ysize 40
                                value 0
                                range 30

                            text "0":
                                size 36
                                xalign 0.5
                                yalign 0.5
                                outlines [(0, "#000", 2, 2)]

                    hbox:

                        spacing 20
                        xalign 0.5
                        xanchor 0.5

                        if jasper_pontos > 0:

                            add "menu_jasper.webp"

                            vbox:

                                spacing 1

                                text "Jasper (chefe)":
                                    size 18
                                    xalign 0.5
                                    yalign 0.5
                                    outlines [(0, "#000", 1, 1)]

                                bar:
                                    xalign 0.5
                                    yalign 0.5
                                    xsize 250
                                    ysize 40
                                    value jasper_pontos
                                    range jasper_pontos_max

                            text "[jasper_pontos]":
                                size 36
                                xalign 0.5
                                yalign 0.5
                                outlines [(0, "#000", 2, 2)]

                        else:

                            add "menu_question.webp"

                            bar:
                                xalign 0.5
                                yalign 0.5
                                xsize 250
                                ysize 40
                                value 0
                                range 30

                            text "0":
                                size 36
                                xalign 0.5
                                yalign 0.5
                                outlines [(0, "#000", 2, 2)]

                    hbox:

                        spacing 20
                        xalign 0.5
                        xanchor 0.5

                        if akemi_pontos > 0:

                            add "menu_akemi.webp"

                            vbox:

                                spacing 1

                                text "Akemi (amiga do trabalho)":
                                    size 18
                                    xalign 0.5
                                    yalign 0.5
                                    outlines [(0, "#000", 1, 1)]

                                bar:
                                    xalign 0.5
                                    yalign 0.5
                                    xsize 250
                                    ysize 40
                                    value akemi_pontos
                                    range akemi_pontos_max

                            text "[akemi_pontos]":
                                size 36
                                xalign 0.5
                                yalign 0.5
                                outlines [(0, "#000", 2, 2)]

                        else:

                            add "menu_question.webp"

                            bar:
                                xalign 0.5
                                yalign 0.5
                                xsize 250
                                ysize 40
                                value 0
                                range 30

                            text "0":
                                size 36
                                xalign 0.5
                                yalign 0.5
                                outlines [(0, "#000", 2, 2)]

                    hbox:

                        spacing 20
                        xalign 0.5
                        xanchor 0.5

                        if trabalho_quente > 0:

                            add "menu_tarados.webp"

                            vbox:

                                spacing 1

                                text "Tarados do Bar (clientes)":
                                    size 18
                                    xalign 0.5
                                    yalign 0.5
                                    outlines [(0, "#000", 1, 1)]

                                bar:
                                    xalign 0.5
                                    yalign 0.5
                                    xsize 250
                                    ysize 40
                                    value trabalho_quente
                                    range 45

                            text "[trabalho_quente]":
                                size 36
                                xalign 0.5
                                yalign 0.5
                                outlines [(0, "#000", 2, 2)]

                        else:

                            add "menu_question.webp"

                            bar:
                                xalign 0.5
                                yalign 0.5
                                xsize 250
                                ysize 40
                                value 0
                                range 30

                            text "0":
                                size 36
                                xalign 0.5
                                yalign 0.5
                                outlines [(0, "#000", 2, 2)]

                vbox:

                    spacing 20

                    hbox:

                        spacing 20
                        xalign 0.5
                        xanchor 0.5

                        if chefe_pontos > 0:

                            add "menu_chefe.webp"

                            vbox:

                                spacing 1

                                text "Editor Chefe (VIP)":
                                    size 18
                                    xalign 0.5
                                    yalign 0.5
                                    outlines [(0, "#000", 1, 1)]

                                bar:
                                    xalign 0.5
                                    yalign 0.5
                                    xsize 250
                                    ysize 40
                                    value chefe_pontos
                                    range chefe_pontos_max

                            text "[chefe_pontos]":
                                size 36
                                xalign 0.5
                                yalign 0.5
                                outlines [(0, "#000", 2, 2)]

                        else:

                            add "menu_question.webp"

                            bar:
                                xalign 0.5
                                yalign 0.5
                                xsize 250
                                ysize 40
                                value 0
                                range 30

                            text "0":
                                size 36
                                xalign 0.5
                                yalign 0.5
                                outlines [(0, "#000", 2, 2)]

                    hbox:

                        spacing 20
                        xalign 0.5
                        xanchor 0.5

                        if silva_pontos > 0:

                            add "menu_silva.webp"

                            vbox:

                                spacing 1

                                text "[s] (vizinho)":
                                    size 18
                                    xalign 0.5
                                    yalign 0.5
                                    outlines [(0, "#000", 1, 1)]

                                bar:
                                    xalign 0.5
                                    yalign 0.5
                                    xsize 250
                                    ysize 40
                                    value silva_pontos
                                    range silva_pontos_max

                            text "[silva_pontos]":
                                size 36
                                xalign 0.5
                                yalign 0.5
                                outlines [(0, "#000", 2, 2)]

                        else:

                            add "menu_question.webp"

                            bar:
                                xalign 0.5
                                yalign 0.5
                                xsize 250
                                ysize 40
                                value 0
                                range 30

                            text "0":
                                size 36
                                xalign 0.5
                                yalign 0.5
                                outlines [(0, "#000", 2, 2)]

                    hbox:

                        spacing 20
                        xalign 0.5
                        xanchor 0.5

                        if zaza_pontos > 0:

                            add "menu_zaza.webp"

                            vbox:

                                spacing 1

                                text "Verônica Zaza (VIP)":
                                    size 18
                                    xalign 0.5
                                    yalign 0.5
                                    outlines [(0, "#000", 1, 1)]

                                bar:
                                    xalign 0.5
                                    yalign 0.5
                                    xsize 250
                                    ysize 40
                                    value zaza_pontos
                                    range zaza_pontos_max

                            text "[zaza_pontos]":
                                size 36
                                xalign 0.5
                                yalign 0.5
                                outlines [(0, "#000", 2, 2)]

                        else:

                            add "menu_question.webp"

                            bar:
                                xalign 0.5
                                yalign 0.5
                                xsize 250
                                ysize 40
                                value 0
                                range 30

                            text "0":
                                size 36
                                xalign 0.5
                                yalign 0.5
                                outlines [(0, "#000", 2, 2)]

                    hbox:

                        spacing 20
                        xalign 0.5
                        xanchor 0.5

                        if stalker_pontos > 0:

                            add "menu_stalker.webp"

                            vbox:

                                spacing 1

                                text "[ta] (cinema)":
                                    size 18
                                    xalign 0.5
                                    yalign 0.5
                                    outlines [(0, "#000", 1, 1)]

                                bar:
                                    xalign 0.5
                                    yalign 0.5
                                    xsize 250
                                    ysize 40
                                    value stalker_pontos
                                    range stalker_pontos_max

                            text "[stalker_pontos]":
                                size 36
                                xalign 0.5
                                yalign 0.5
                                outlines [(0, "#000", 2, 2)]

                        else:

                            add "menu_question.webp"

                            bar:
                                xalign 0.5
                                yalign 0.5
                                xsize 250
                                ysize 40
                                value 0
                                range 30

                            text "0":
                                size 36
                                xalign 0.5
                                yalign 0.5
                                outlines [(0, "#000", 2, 2)]

                    hbox:

                        spacing 20
                        xalign 0.5
                        xanchor 0.5

                        if beto_pontos > 0:

                            add "menu_beto.webp"

                            vbox:

                                spacing 1

                                text "Beto (mercado)":
                                    size 18
                                    xalign 0.5
                                    yalign 0.5
                                    outlines [(0, "#000", 1, 1)]

                                bar:
                                    xalign 0.5
                                    yalign 0.5
                                    xsize 250
                                    ysize 40
                                    value beto_pontos
                                    range beto_pontos_max

                            text "[beto_pontos]":
                                size 36
                                xalign 0.5
                                yalign 0.5
                                outlines [(0, "#000", 2, 2)]

                        else:

                            add "menu_question.webp"

                            bar:
                                xalign 0.5
                                yalign 0.5
                                xsize 250
                                ysize 40
                                value 0
                                range 30

                            text "0":
                                size 36
                                xalign 0.5
                                yalign 0.5
                                outlines [(0, "#000", 2, 2)]

screen menu_loja():
    tag principal

    modal True
    zorder 98

    frame:

        xysize (1280, 720)
        background "menu_fundo.webp"

        has hbox

        spacing 30

        frame:

            background None
            xysize (263, 720)

            use menu_lateral

        frame:

            background None
            xysize (977, 720)
            xalign 0.5
            xanchor 0.5

            has vbox

            spacing 30
            xalign 0.5
            xanchor 0.5

            text "Loja":
                size 36
                xalign 0.5
                text_align 0.5
                outlines [(0, "#000", 2, 2)]

            text "Em breve":
                size 24
                xalign 0.5
                text_align 0.5
                outlines [(0, "#000", 1, 1)]

screen menu_config():
    tag principal

    modal True
    zorder 98

    frame:

        xysize (1280, 720)
        background "menu_fundo.webp"

        has hbox

        spacing 40

        frame:

            background None
            xysize (263, 720)

            use menu_lateral

        frame:

            background None
            xysize (977, 720)
            xalign 0.5
            xanchor 0.5

            has vbox

            spacing 28
            xalign 0.5
            xanchor 0.5

            text "Configure Seu Jogo":
                size 36
                xalign 0.5
                outlines [(0, "#000", 2, 2)]

            text "Arraste as barras para ajustar o volume \n e outras configurações do seu jogo":
                size 24
                xalign 0.5
                text_align 0.5
                outlines [(0, "#000", 2, 2)]

            hbox:

                spacing 20

                vbox:

                    spacing 10

                    if config.has_music:

                        label _("Volume da Música")

                        hbox:
                            bar:
                                value Preference("music volume")
                                xalign 0.5
                                xsize 300
                                ysize 50

                vbox:

                    spacing 10

                    if config.has_sound:

                        label _("Volume dos Sons")

                        hbox:
                            bar:
                                value Preference("sound volume")
                                xalign 0.5
                                xsize 300
                                ysize 50

                            if config.sample_sound:
                                textbutton _("Test") action Play("sound", config.sample_sound)

            hbox:

                spacing 20

                vbox:

                    spacing 10

                    label _("Volume da Escrita")

                    hbox:
                        bar:
                            value Preference("tec volume")
                            xalign 0.5
                            xsize 300
                            ysize 50

                vbox:

                    spacing 10

                    label _("Velocidade da Escrita")

                    hbox:
                        bar:
                            value Preference("text speed")
                            xalign 0.5
                            xsize 300
                            ysize 50

            hbox:

                spacing 20
                xalign 0.5

                imagebutton idle "extra/botao_insta_idle.webp":
                    action OpenURL('https://www.instagram.com/geikogames/')

                imagebutton idle "extra/botao_face_idle.webp":
                    action OpenURL('https://www.facebook.com/celebrityhuntergame')

                imagebutton idle "extra/botao_twitter_idle.webp":
                    action OpenURL('https://twitter.com/geikogames')

                imagebutton idle "extra/botao_zap_idle.webp":
                    action OpenURL('https://chat.whatsapp.com/LYYxWrSLY1MAX85loSQshU')

                imagebutton idle "extra/botao_geiko_idle.webp":
                    action OpenURL('https://linktr.ee/geikogames')

            text "Versão [config.version]":
                size 24
                xalign 0.5
                text_align 0.5
                outlines [(0, "#000", 2, 2)]

screen menu_lateral():

    zorder 99

    vbox:

        spacing 25

        vbox:

            spacing 10

            add "menu_mcm.webp"

            text "[mc]":
                size 36
                xalign 0.5
                yalign 0.5
                yanchor 0.5
                outlines [(0, "#000", 2, 2)]

            text "Universitária":
                size 24
                xalign 0.5
                text_align 0.5
                outlines [(0, "#000", 2, 2)]

        imagebutton idle "menu_perfil.webp":
            xalign 0.5
            xanchor 0.5
            action ShowMenu('menu_perfil')

        imagebutton idle "menu_relacionamentos.webp":
            xalign 0.5
            xanchor 0.5
            action ShowMenu('menu_relacionamentos')






        imagebutton idle "menu_config.webp":
            xalign 0.5
            xanchor 0.5
            action ShowMenu('menu_config')

    imagebutton idle "menu_fechar.webp":
        xalign 0.5
        yalign 0.975
        action [ Play("sound", "audio/closing.mp3"), Return() ]

screen escolhe_personagem():
    tag navegar

    modal True
    zorder 99

    imagebutton idle "escolha_garota.webp":
        xalign 0.03
        xanchor 0.0

        action Jump("escolhe_garota")

    imagebutton idle "escolha_fado.webp":
        xalign 1.0
        xanchor 1.0

        action Jump("escolhe_fado")

screen escolhe_nome():

    modal True

    frame:
        xysize (625,245)
        xalign 0.5
        yalign 0.5
        xpadding 30
        ypadding 30

        background "extra/painel_criacao_personagem.webp"

        has vbox

        xalign 0.5
        spacing 15

        text "{b}Informe seu nome{/b}" xalign 0.5 xanchor 0.5

        vbox:

            xalign 0

            button:
                xsize 450
                background "extra/campo_input.webp"
                xalign 0.5
                id "input_1"
                action NullAction()

                add Input(hover_color="#ec2098",size=22, color="#ec2098", changed=nome_func, length=15, button=renpy.get_widget("escolhe_nome","input_1")) yalign 1.0

        vbox:

            xalign 0.5

            textbutton "Confirmar":
                top_padding 35
                left_padding 80
                background "extra/botao_idle.webp"
                action [ Hide("escolhe_nome"), Return() ]

screen tempo_mapa():

    zorder 99

    imagebutton idle "extra/icone_menu_idle.webp":
        xalign 0.995
        yalign 0.01
        action [ Play("sound", "audio/starting.mp3"), ShowMenu('menu_perfil') ]

    add "tempo_mapa":
        xalign 0.996
        yalign 0.09

screen esconde():

    modal True
    zorder 99

    imagemap:

        ground "transparent.png"
        hotspot (0, 0, 1280, 720) focus_mask None action Return()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
