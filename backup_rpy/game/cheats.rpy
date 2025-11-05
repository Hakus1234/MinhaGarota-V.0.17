init python:
    import renpy.store as store

    def _cheat_bounds(varname):
        entry = CHEAT_LOOKUP.get(varname)
        if not entry:
            return None, None
        return entry.get("min"), entry.get("max")

    def cheat_adjust(varname, delta):
        """
        Incrementa a variável informada pelo delta recebido.
        Cria a variável automaticamente caso ainda não exista.
        """
        current = getattr(store, varname, 0)
        try:
            new_value = current + delta
        except TypeError:
            # Se o valor atual não aceita soma, apenas define o delta.
            new_value = delta
        min_value, max_value = _cheat_bounds(varname)
        if min_value is not None:
            new_value = max(min_value, new_value)
        if max_value is not None:
            new_value = min(max_value, new_value)
        setattr(store, varname, new_value)

    def cheat_set(varname, value):
        """
        Define a variável para um valor específico.
        """
        min_value, max_value = _cheat_bounds(varname)
        if min_value is not None:
            value = max(min_value, value)
        if max_value is not None:
            value = min(max_value, value)
        setattr(store, varname, value)

    def cheat_toggle(varname):
        """
        Alterna booleans de forma simples.
        """
        setattr(store, varname, not getattr(store, varname, False))

    CHEAT_SECTIONS = [
        {
            "title": "Recursos",
            "entries": [
                {"label": "Dinheiro", "var": "dinheiro", "step": 100, "large_step": 1000, "min": 0, "max": 99999},
                {"label": "Moedas de Ouro", "var": "moeda", "step": 1, "large_step": 10, "min": 0, "max": 999},
                {"label": "Dinheiro (Limite)", "var": "dinheiro_max", "step": 100, "large_step": 500, "min": 0, "max": 99999},
                {"label": "Cuidado", "var": "cuidado", "step": 5, "large_step": 25, "min": 0, "max": 200},
                {"label": "Fama", "var": "fama", "step": 5, "large_step": 25, "min": 0, "max": 200},
                {"label": "Exibicionismo", "var": "exibicionismo", "step": 5, "large_step": 25, "min": 0, "max": 200},
            ],
        },
        {
            "title": "Atributos",
            "entries": [
                {"label": "Coragem", "var": "coragem", "step": 1, "large_step": 5, "min": 0, "max": 200},
                {"label": "Vivência", "var": "vivencia", "step": 1, "large_step": 5, "min": 0, "max": 200},
                {"label": "Sexualidade", "var": "sexualidade", "step": 1, "large_step": 5, "min": 0, "max": 200},
                {"label": "Trabalho EXP", "var": "trabalho_exp", "step": 5, "large_step": 25, "min": 0, "max": 500},
                {"label": "Cuidado (Max)", "var": "cuidado_max", "step": 5, "large_step": 25, "min": 0, "max": 500},
                {"label": "Tempo Atual", "var": "tempo", "step": 1, "large_step": 5, "min": 0, "max": 10},
                {"label": "Dia Total", "var": "dia_total", "step": 1, "large_step": 7, "min": 1, "max": 365},
                {"label": "Semana", "var": "semana", "step": 1, "large_step": 4, "min": 1, "max": 52},
            ],
        },
        {
            "title": "Relacionamentos",
            "entries": [
                {"label": "Gabriel Pontos", "var": "gabriel_pontos", "step": 1, "large_step": 5, "min": 0, "max": 500},
                {"label": "Fernando Pontos", "var": "fernando_pontos", "step": 1, "large_step": 5, "min": 0, "max": 500},
                {"label": "Jasper Pontos", "var": "jasper_pontos", "step": 1, "large_step": 5, "min": 0, "max": 500},
                {"label": "Chefe Pontos", "var": "chefe_pontos", "step": 1, "large_step": 5, "min": 0, "max": 500},
                {"label": "Zaza Pontos", "var": "zaza_pontos", "step": 1, "large_step": 5, "min": 0, "max": 500},
                {"label": "Stalker Pontos", "var": "stalker_pontos", "step": 1, "large_step": 5, "min": 0, "max": 500},
                {"label": "Beto Pontos", "var": "beto_pontos", "step": 1, "large_step": 5, "min": 0, "max": 500},
                {"label": "Silva Pontos", "var": "silva_pontos", "step": 1, "large_step": 5, "min": 0, "max": 500},
            ],
        },
        {
            "title": "Modos e Flags",
            "entries": [
                {"label": "Modo Streamer", "var": "streamer", "type": "toggle"},
                {"label": "Virgem", "var": "virgem", "type": "toggle"},
                {"label": "Primeira vez concluída", "var": "primeira_vez", "type": "toggle"},
                {"label": "Namorando", "var": "namorando", "type": "toggle"},
                {"label": "Fado Desbloqueado", "var": "fado", "type": "toggle"},
            ],
        },
    ]

    CHEAT_LOOKUP = {
        entry["var"]: entry
        for section in CHEAT_SECTIONS
        for entry in section["entries"]
        if entry.get("type") != "toggle"
    }

    config.overlay_screens.append("cheat_shortcut")


screen cheat_menu():
    tag menu
    modal True

    add Solid("#0008")

    key "K_ESCAPE" action Return()
    key "mouseup_3" action Return()

    frame:
        align (0.5, 0.5)
        xmaximum 900
        ymaximum 640
        padding (30, 30, 30, 30)
        if renpy.loadable("gui/frame.png"):
            background Frame("gui/frame.png", 20, tile=True)
        else:
            background "#1a1a1a"
        has vbox spacing 20

        text "Menu de Cheats" style "menu_title"
        text "Ajuste rapidamente recursos e relacionamentos para testes." style "menu_text"

        viewport:
            ymaximum 460
            mousewheel True
            draggable True
            scrollbars "vertical"
            has vbox spacing 18

            for section in CHEAT_SECTIONS:
                $ entries = section["entries"]
                frame:
                    padding (15, 15, 15, 15)
                    background "#0c0c0c90"
                    has vbox spacing 12

                    text section["title"] style "menu_label"

                    for entry in entries:
                        $ varname = entry["var"]
                        $ entry_label = entry.get("label", varname)
                        if entry.get("type") == "toggle":
                            $ value = getattr(store, varname, False)
                            $ status = "Ativo" if value else "Desativado"
                            hbox:
                                spacing 12
                                text "[entry_label]: [status]" style "menu_choice"
                                textbutton "Alternar" action Function(cheat_toggle, varname)
                        else:
                            $ current = getattr(store, varname, entry.get("min", 0))
                            $ step = entry.get("step", 1)
                            $ big = entry.get("large_step", step * 5 if step else None)
                            hbox:
                                spacing 8
                                text "[entry_label]: [current]" style "menu_choice"

                                textbutton "+" + str(step) action Function(cheat_adjust, varname, step)
                                textbutton "-" + str(step) action Function(cheat_adjust, varname, -step)

                                if big:
                                    textbutton "+" + str(big) action Function(cheat_adjust, varname, big)
                                    textbutton "-" + str(big) action Function(cheat_adjust, varname, -big)

                                if "max" in entry:
                                    textbutton "Max" action Function(cheat_set, varname, entry["max"])
                                if "min" in entry:
                                    textbutton "Zerar" action Function(cheat_set, varname, entry["min"])

        textbutton "Fechar" action Return() xalign 0.5


screen cheat_shortcut():
    key "K_F7" action ShowMenu("cheat_menu")
