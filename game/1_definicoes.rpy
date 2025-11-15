define sounds = ['audio/A1.ogg', 'audio/A2.ogg', 'audio/A3.ogg', 'audio/A4.ogg', 'audio/A5.ogg', 'audio/B1.ogg', 'audio/B2.ogg', 'audio/B3.ogg', 'audio/B4.ogg', 'audio/B5.ogg']

init python:
    if renpy.android:
        config.rollback_enabled = False

    class _PythonSDLActivityStub(object):
        @staticmethod
        def iniciaVariaveis():
            pass

        @staticmethod
        def pegaLogado():
            return True

        @staticmethod
        def carregaJogo():
            pass

        @staticmethod
        def carregaHistoria():
            pass

        @staticmethod
        def pegaBanned():
            return False

        @staticmethod
        def setaBanned():
            pass

        @staticmethod
        def pegaBacker():
            return True

        @staticmethod
        def pegaTempo():
            pass

        @staticmethod
        def checaTempo():
            return True

        @staticmethod
        def pegaCreditos():
            return 0

        @staticmethod
        def abreLogin():
            pass

        @staticmethod
        def pegaEmail():
            return "offline@local"

        @staticmethod
        def pegaUid():
            return "OFFLINE"

        @staticmethod
        def registraEvento(*args, **kwargs):
            pass

        @staticmethod
        def salvaHistoria():
            pass

        @staticmethod
        def checkDaily():
            return False

        @staticmethod
        def pegaDaily():
            return ""

        @staticmethod
        def setDaily():
            pass

    PythonSDLActivity = _PythonSDLActivityStub

    import random
    import renpy.store as store

    def nome_func(newstring):
        store.pnome = newstring

    def prompt_store_input(var_name, prompt, length=15, allow=None):
        """
        Abre um prompt de texto nativo (funciona melhor no Android) e armazena
        o resultado na variável solicitada.
        """
        def _inner():
            current_value = getattr(store, var_name, "")
            new_value = renpy.input(prompt, default=current_value, length=length, allow=allow)
            if new_value is None:
                return

            new_value = new_value.strip()
            if not new_value:
                return

            setattr(store, var_name, new_value)

        renpy.invoke_in_new_context(_inner)
        renpy.restart_interaction()



    renpy.music.register_channel("tec", "tec", loop=None, stop_on_mute=True, tight=False, buffer_queue=True, movie=False, framedrop=True)

    renpy.music.set_volume(0.5, delay=0, channel='tec')

    def type_sound(event, interact=True, **kwargs):
        if not interact:
            return
        
        if event == "show":
            renpy.sound.play(renpy.random.choice(sounds), channel="tec")
            renpy.sound.queue(renpy.random.choice(sounds), channel="tec")
            renpy.sound.queue(renpy.random.choice(sounds), channel="tec")
            renpy.sound.queue(renpy.random.choice(sounds), channel="tec")
            renpy.sound.queue(renpy.random.choice(sounds), channel="tec")
            renpy.sound.queue(renpy.random.choice(sounds), channel="tec")
            renpy.sound.queue(renpy.random.choice(sounds), channel="tec")
            renpy.sound.queue(renpy.random.choice(sounds), channel="tec")
            renpy.sound.queue(renpy.random.choice(sounds), channel="tec")
            renpy.sound.queue(renpy.random.choice(sounds), channel="tec")
            renpy.sound.queue(renpy.random.choice(sounds), channel="tec")
            renpy.sound.queue(renpy.random.choice(sounds), channel="tec")
            renpy.sound.queue(renpy.random.choice(sounds), channel="tec")
            renpy.sound.queue(renpy.random.choice(sounds), channel="tec")
            renpy.sound.queue(renpy.random.choice(sounds), channel="tec")
            renpy.sound.queue(renpy.random.choice(sounds), channel="tec")
            renpy.sound.queue(renpy.random.choice(sounds), channel="tec")
            renpy.sound.queue(renpy.random.choice(sounds), channel="tec")
            renpy.sound.queue(renpy.random.choice(sounds), channel="tec")
            renpy.sound.queue(renpy.random.choice(sounds), channel="tec")
            renpy.sound.queue(renpy.random.choice(sounds), channel="tec")
            renpy.sound.queue(renpy.random.choice(sounds), channel="tec")
            renpy.sound.queue(renpy.random.choice(sounds), channel="tec")
            renpy.sound.queue(renpy.random.choice(sounds), channel="tec")
            renpy.sound.queue(renpy.random.choice(sounds), channel="tec")
            renpy.sound.queue(renpy.random.choice(sounds), channel="tec")
            renpy.sound.queue(renpy.random.choice(sounds), channel="tec")
            renpy.sound.queue(renpy.random.choice(sounds), channel="tec")
            renpy.sound.queue(renpy.random.choice(sounds), channel="tec")
        
        elif event == "slow_done" or event == "end":
            renpy.sound.stop(channel="tec")

define e = Character("Eileen")

define mc = Character("[pnome]")
define p = Character("[npcnome]")
define pi = Character("Pixel", what_color="#e720f5")
define d = Character("Dilema", what_color="#e720f5")
define t = Character("TUTORIAL", what_color="#319bd4")
define c1 = Character("[c1_nome]")
define d1 = Character("[d1_nome]")
define f = Character("Fado", what_color="#287a3e")
define fe = Character("[fe_nome]")
define g = Character("[g_nome]")
define j = Character("[j_nome]")
define a = Character("[a_nome]")
define c = Character("[c_nome]")
define z = Character("[z_nome]")
define b = Character("[b_nome]")
define n = Character("[n_nome]")
define s = Character("[s_nome]")
define ta = Character("[ta_nome]")
define l = Character("Luca")
define le = Character("[le_nome]")
define g1 = Character("Bruno")
define g2 = Character("Rodrigo")
define jo = Character("JÃ£o")
define pe = Character("Primo Pedro")
define he = Character("Tio Heitor")
define h = Character("Tio Heitor")
define m = Character("MÃ£e")
define pa = Character("Coach Pablo")
define pab = Character("Coach Pablo")
define fa = Character("FÃ¡bio")
define s2 = Character("[s2_nome]")

define pnome = "Melissa"
define fe_nome = "Homem"
define g_nome = "???"
define j_nome = "???"
define a_nome = "Akemi"
define c_nome = "Velho"
define z_nome = "Senhora"
define b_nome = "Garoto"
define n_nome = "Homem"
define s_nome = "Pai"
define ta_nome = "Tarado"
define le_nome = "Garoto de BonÃ©"
define s2_nome = "SeguranÃ§a"



image ani01 = Movie(play="/images/ani/mg_ani03.webm")
image ani02 = Movie(play="/images/ani/mg_ani01.webm")
image ani03 = Movie(play="/images/ani/mg_ani02.webm")
image ani04 = Movie(play="/images/ani/mg_ani04.webm")
image ani05 = Movie(play="/images/ani/mg_ani05.webm")
image ani06 = Movie(play="/images/ani/mg_ani06.webm")
image ani07 = Movie(play="/images/ani/mg_ani07.webm")
image ani08 = Movie(play="/images/ani/mg_ani08.webm")
image ani09 = Movie(play="/images/ani/mg_ani09.webm")
image ani10 = Movie(play="/images/ani/mg_ani10.webm")
image ani11 = Movie(play="/images/ani/mg_ani11.webm")
image ani12 = Movie(play="/images/ani/mg_ani12.webm")
image ani13 = Movie(play="/images/ani/mg_ani13.webm")
image ani14 = Movie(play="/images/ani/mg_ani14.webm")
image ani15 = Movie(play="/images/ani/mg_ani15.webm")
image ani16 = Movie(play="/images/ani/mg_ani16.webm")
image ani17 = Movie(play="/images/ani/mg_ani17.webm")
image ani18 = Movie(play="/images/ani/mg_ani18.webm")
image ani19 = Movie(play="/images/ani/mg_ani19.webm")
image ani20 = Movie(play="/images/ani/mg_ani20.webm")
image ani21 = Movie(play="/images/ani/mg_ani21.webm")
image ani22 = Movie(play="/images/ani/mg_ani22.webm")
image ani23 = Movie(play="/images/ani/mg_ani23.webm")
image ani24 = Movie(play="/images/ani/mg_ani24.webm")
image ani25 = Movie(play="/images/ani/mg_ani25.webm")
image ani26 = Movie(play="/images/ani/mg_ani26.webm")
image ani27 = Movie(play="/images/ani/mg_ani27.webm")
image ani28 = Movie(play="/images/ani/mg_ani28.webm")
image ani29 = Movie(play="/images/ani/mg_ani29.webm")
image ani30 = Movie(play="/images/ani/mg_ani30.webm")
image ani31 = Movie(play="/images/ani/mg_ani31.webm")
image ani32 = Movie(play="/images/ani/mg_ani32.webm")
image ani33 = Movie(play="/images/ani/mg_ani33.webm")
image ani34 = Movie(play="/images/ani/mg_ani34.webm")
image ani35 = Movie(play="/images/ani/mg_ani35.webm")
image ani36 = Movie(play="/images/ani/mg_ani36.webm")
image ani37 = Movie(play="/images/ani/mg_ani37.webm")
image ani38 = Movie(play="/images/ani/mg_ani38.webm")
image ani39 = Movie(play="/images/ani/mg_ani39.webm")
image ani40 = Movie(play="/images/ani/mg_ani40.webm")
image ani41 = Movie(play="/images/ani/mg_ani41.webm")
image ani42 = Movie(play="/images/ani/mg_ani42.webm")
image ani43 = Movie(play="/images/ani/mg_ani43.webm")
image ani44 = Movie(play="/images/ani/mg_ani44.webm")
image ani45 = Movie(play="/images/ani/mg_ani45.webm")
image ani46 = Movie(play="/images/ani/mg_ani46.webm")
image ani47 = Movie(play="/images/ani/mg_ani47.webm")
image ani48 = Movie(play="/images/ani/mg_ani48.webm")
image ani49 = Movie(play="/images/ani/mg_ani49.webm")
image ani50 = Movie(play="/images/ani/mg_ani50.webm")
image ani51 = Movie(play="/images/ani/mg_ani51.webm")
image ani52 = Movie(play="/images/ani/mg_ani52.webm")
image ani53 = Movie(play="/images/ani/mg_ani53.webm")
image ani54 = Movie(play="/images/ani/mg_ani54.webm")
image ani55 = Movie(play="/images/ani/mg_ani55.webm")
image ani56 = Movie(play="/images/ani/mg_ani56.webm")
image ani57 = Movie(play="/images/ani/mg_ani57.webm")
image ani58 = Movie(play="/images/ani/mg_ani58.webm")
image ani59 = Movie(play="/images/ani/mg_ani59.webm")
image ani60 = Movie(play="/images/ani/mg_ani60.webm")
image ani61 = Movie(play="/images/ani/mg_ani61.webm")
image ani62 = Movie(play="/images/ani/mg_ani62.webm")
image ani63 = Movie(play="/images/ani/mg_ani63.webm")
image ani64 = Movie(play="/images/ani/mg_ani64.webm")
image ani65 = Movie(play="/images/ani/mg_ani65.webm")
image ani66 = Movie(play="/images/ani/mg_ani66.webm")
image ani67 = Movie(play="/images/ani/mg_ani67.webm")
image ani68 = Movie(play="/images/ani/mg_ani68.webm")
image ani69 = Movie(play="/images/ani/mg_ani69.webm")
image ani70 = Movie(play="/images/ani/mg_ani70.webm")
image ani71 = Movie(play="/images/ani/mg_ani71.webm")
image ani72 = Movie(play="/images/ani/mg_ani72.webm")
image ani73 = Movie(play="/images/ani/mg_ani73.webm")
image ani74 = Movie(play="/images/ani/mg_ani74.webm")
image ani75 = Movie(play="/images/ani/mg_ani75.webm")
image ani76 = Movie(play="/images/ani/mg_ani76.webm")
image ani77 = Movie(play="/images/ani/mg_ani77.webm")
image ani78 = Movie(play="/images/ani/mg_ani78.webm")
image ani79 = Movie(play="/images/ani/mg_ani79.webm")
image ani80 = Movie(play="/images/ani/mg_ani80.webm")
image ani81 = Movie(play="/images/ani/mg_ani81.webm")
image ani82 = Movie(play="/images/ani/mg_ani82.webm")
image ani83 = Movie(play="/images/ani/mg_ani83.webm")
image ani84 = Movie(play="/images/ani/mg_ani84.webm")
image ani85 = Movie(play="/images/ani/mg_ani85.webm")
image ani86 = Movie(play="/images/ani/mg_ani86.webm")
image ani87 = Movie(play="/images/ani/mg_ani87.webm")
image ani88 = Movie(play="/images/ani/mg_ani88.webm")
image ani89 = Movie(play="/images/ani/mg_ani89.webm")
image ani90 = Movie(play="/images/ani/mg_ani90.webm")
image ani91 = Movie(play="/images/ani/mg_ani91.webm")
image ani92 = Movie(play="/images/ani/mg_ani92.webm")
image ani93 = Movie(play="/images/ani/mg_ani93.webm")
image ani94 = Movie(play="/images/ani/mg_ani94.webm")
image ani95 = Movie(play="/images/ani/mg_ani95.webm")
image ani96 = Movie(play="/images/ani/mg_ani96.webm")
image ani97 = Movie(play="/images/ani/mg_ani97.webm")
image ani98 = Movie(play="/images/ani/mg_ani98.webm")
image ani99 = Movie(play="/images/ani/mg_ani99.webm")
image ani100 = Movie(play="/images/ani/mg_ani100.webm")
image ani101 = Movie(play="/images/ani/mg_ani101.webm")
image ani102 = Movie(play="/images/ani/mg_ani102.webm")




default uid = "NOID"
default userlogado = True
define premium = False
default mulher = False
default fado = False
default tempo = 1
default tempo_agora = 0
default streamer = False

default persistent.banned = False
default persistent.intro = False

image black = "#000"
image black_scene = "#000"
image white = "#ffffff"
image red = "#FF0000"
image logo = "extra/geiko.webp"

default banho_hoje = False
default lanche_hoje = False
default dia = 1
default mes = 1
default ano = 2363
default dia_total = 1
default semana = 1
default semana_dia = "segunda"
default intro = 0

default coragem = 0
default vivencia = 0
default sexualidade = 0
default sexualidade_max = 45
default gabriel_pontos = 0
default gabriel_pontos_max = 20
default fernando_pontos = 0
default fernando_pontos_max = 10
default jasper_pontos = 0
default jasper_pontos_max = 10
default akemi_pontos = 0
default akemi_pontos_max = 5


default dilema2 = 0
default dilema3 = 0

default sonho = 0
default porta = 0
default gabriel = 0
default influencia = 0
default trabalho = 0
default jasper_dinheiro = False
default gabriel_beijo = 0
default primeiro_beijo = False
default gabriel_falou = False
default gabriel_fala = 0
default mapa = 0
default dinheiro = 0
default fernando = 0
default nao_pagou = 0
default trabalho_tutorial = 0
default trabalho_vez = 12
default trabalho_quente = 0
default trabalho_exp = 0
default trabalho_exp_max = 50
default trabalho_nivel = 0
default trabalho_quente_chance = 0
default trabalho_evento = False
default recusou_trabalho_quente = False
default pai_porta = False
default pai_quente = 0
default gabriel_historia = 0
default porta_daily = False
default aluguel = 200
default aluguel_perdao = 0
default fernando_quente = 0
default toalha2 = False
default masturbacao = 0
default masturbacao_gabriel = 0
default estudo = 0
default estudo_max = 15
default estudou = False
default gabriel_paga = False
default trabalhou = False
default trabalho_arruma = False
default trabalho_arruma2 = False
default akemi_falou = False
default chefe = 0
default chefe_vez = 0
default zaza_vez = 0
default zaza = 0
default chefe_pontos = 0
default chefe_pontos_max = 30
default chefe_fala = 0
default rand3 = 0
default rand4 = 0
default din = 0
default sentou_beber = False
default chefe_conta = 0
default pai = 0
default namorando = False
default gabriel_pai = 0
default fadolandia = 0
default moeda = 0
default p1341 = False
default moeda_banco = 0
default moeda_total = 0
default moeda_adicionar = 0
default nuvem_tutorial = False
default primeiro_namoro = False
default compras_info = 0
default compras_info2 = 0
default dtempo = False
default fernando_arruma = False
default sexo_arruma1 = False
default cor_arruma1 = False
default cuidado = 0
default cuidado_max = 30
default cuidou = 1
default produto = 0
default produto_total = 0
default drink_nivel = 0
default futebol = False
default gabriel_cinema = 0
default mercado = 0
default beijou_mercado = 0
default roupa1 = 0
default boutique = 0
default roupa2 = 0
default roupa3 = 0
default nathan = 0
default silva_pontos = 0
default silva_pontos_max = 9
default jasper_pernas_chance = 0
default jasper_pernas = 0
default jasper_pernas_final = False
default chefe_chance = False
default chefe_sumiu = 0
default sex_arruma1 = False
default mc_fim_jogo = 0
default roupa4 = 0
default roupa4_2 = False
default gabriel_pai_viu = False
default max_cuidado = False
default zaza_pontos = 0
default zaza_pontos_max = 9
default stalker = 0
default stalker_pontos = 0
default stalker_pontos_max = 9
default tv = 0
default tv_check = False
default beto_namorada = False
default beto_gab = False
default beto_pontos = 0
default beto_pontos_max = 9
default dinheiro_max = 1000
default gab_cinema = False
default gab_jogo = False
default silva_fala = 0
default fernando_fala = 0
default roupa5 = 0
default beto_fala = 0
default tarado_fala1 = 0
default tarado_resposta1 = 0
default tarado_resposta2 = 0
default gabriel_boanoite = 0
default silva_boanoite = 0
default gabriel_pegacao = 0
default akemi_fala = 0
default jasper_fala = 0
default zaza_random = 0
default familia_check = False
default familia = 0
default fama = 0
default roupa6 = 0
default chovendo = False
default chuva_fala = 0
default dia_fala = 0
default nathan_quente = 0
default jasper = 0

default akemi_interesse = False
default fama_pontos = 0
default fama_max = 9
default foto_sexual = 0
default celular_check = False
default jasper_quente = 0
default jasper_tesao = 0
default akemi_beijo = 0
default jasper_drink = 0
default mast_fala = 0
default terminou = False
default mae_quente = 0
default pedro_quente = 0
default roupa7 = 0
default fernando_recusou = False
default fernando_beijou = 0
default silva_apanhou = 0
default exibicionismo_pontos = 0
default exibicionismo_max = 94
default exibicionismo_evento = True
default exibicionismo = 0
default passou_protetor = 0
default roupa8 = 0
default nathan_masturbacao = False
default pedro_foto = False
default silva_esposa = False
default noite = 0
default virgem = True
default primeira_vez = False

image intro_casa_d = im.Blur("intro_casa.webp", 1.15)
image fado1_d = im.Blur("intro_fado3.webp", 1.15)



image mcm_banho2_d = im.Blur("mcm_banho2.webp", 20)
image mcm_banho1_d = im.Blur("mcm_banho1.webp", 20)
image mcm_roupa2_d = im.Blur("mcm_roupa2.webp", 20)
image mcm_roupa3_d = im.Blur("mcm_roupa3.webp", 20)
image porta1_d = im.Blur("porta1.webp", 20)
image porta2_d = im.Blur("porta2.webp", 20)
image porta3_d = im.Blur("porta3.webp", 20)
image porta4_d = im.Blur("porta4.webp", 20)
image banho3_d = im.Blur("banho3.webp", 20)
image banho4_d = im.Blur("banho4.webp", 20)
image cama3_d = im.Blur("cama3.webp", 20)
image cama4_d = im.Blur("cama4.webp", 20)
image pai7_d = im.Blur("pai7.webp", 20)
image cama5_d = im.Blur("cama5.webp", 20)
image cama6_d = im.Blur("cama6.webp", 20)
image cama7_d = im.Blur("cama7.webp", 20)
image cama8_d = im.Blur("cama8.webp", 20)

label opening:
    jump before_main_menu

screen tela_login():
    tag menu

    modal True















    if not userlogado:

        vbox:

            spacing 30
            xalign 0.5
            xanchor 0.5
            yalign 0.5
            yanchor 0.5

            add "extra/mensagem_menu.png" xalign 0.5 xanchor 0.5 at transform_blink

            textbutton "Entrar":
                xalign 0.45
                xanchor 0.5
                top_padding 35
                left_padding 100
                background "extra/botao_idle.webp"
                action Call("fazer_login")







    else:

        add "extra/mensagem_inicial.png" xalign 0.5 xanchor 0.5 yalign 0.5 yanchor 0.5 at transform_blink

        imagemap:
            ground "extra/transparent.png"
            hotspot (0, 0,1280, 720) focus_mask None action Jump("main_menu")

screen tela_inicial():
    tag menu

    modal True















    add "extra/mensagem_inicial.png" xalign 0.5 xanchor 0.5 yalign 0.5 yanchor 0.5 at transform_blink

    imagemap:
        ground "extra/transparent.png"
        hotspot (0, 0,1280, 720) focus_mask None action Call("login_convidado")

label before_main_menu:



    $ premium = False
    $ persistent.banned = False
    $ persistent.apoiador = True
    $ userlogado = True



    if persistent.intro:



        "???" "E-ei!"



        "???" "TÃ¡ me ouvindo?!"

        scene black with vpunch

        "???" "Acho que eu consegui."



        "???" "Oi. Desculpa por cancelar o carregamento do game. Ã‰ que eu precisava falar com vocÃª antes de vocÃª comeÃ§ar a jogar."



        "???" "O criador do jogo me pediu pra te passar umas informaÃ§Ãµes que o advogado mandou. Fala sÃ©rio... vocÃªs humanos sÃ£o complicados."

        "???" "Resumindo, vocÃª precisa ter mais de 18 anos para jogar este game no Brasil ou ser maior de idade no paÃ­s onde vocÃª mora."

        "???" "AlÃ©m disso, vocÃª precisa estar de acordo com os Termos de Uso e a PolÃ­tica de Privacidade. Os dois estÃ£o no site www.geiko.net."

        menu:
            "Sou maior e concordo":


                "???" "Veja bem, hein. Papai Noel nÃ£o gosta de gente mentirosa."
            "NÃ£o, tÃ´ caindo fora":


                "???" "CrianÃ§as... vai lÃ¡ jogar teu joguinho de arminha."

                $ renpy.quit()





        "???" "Muito bem, aposto que vocÃª vai gostar bastante desta histÃ³ria. Ela tÃ¡ cheia de emoÃ§Ã£o, seduÃ§Ã£o e mistÃ©rio. E baixaria tambÃ©m."

        "???" "Tome cuidado pois suas escolhas vÃ£o determinar como tudo vai acabar. SÃ£o vÃ¡Ã¡Ã¡rios finais diferentes."

        "???" "Se vocǦ gostar do game, vale a pena vocǦ dar uma olhada nas nossas redes sociais e saber mais sobre o trabalho da Geiko."

        "???" "Ufa... era isso."

        "???" "Espero que vocÃª ame seu tempo neste mundo e eu vou estar te esperando do outro lado. NÃ£o me deixa lÃ¡ sozinha. Beijinho!"

        scene black with dissolve



        $ renpy.pause(1, hard=True)

        $ persistent.intro = True

    play music tema

    $ rand = random.randint(1,3)

    scene black
    play sound logo
    $ renpy.pause(1, hard=True)

    show white at transform_white
    $ renpy.pause(2, hard=True)

    show logo at transform_logo
    $ renpy.pause(3, hard=True)

    python:
        renpy.sound.play("audio/geiko.mp3", channel="tec")

    call baixando_nuvem

    hide logo
    $ renpy.pause(2, hard=True)

    hide white
    $ renpy.pause(2, hard=True)

    scene cidade_mapa



    show mensagem_inicial at transform_blink:
        xalign 0.5
        xanchor 0.5
        yalign 0.5
        yanchor 0.5

    pause





    return

label after_load:



    $ premium = False
    $ persistent.banned = False
    $ persistent.apoiador = True



    python:
        renpy.block_rollback()

    call baixando_nuvem

    if renpy.variant("android"):
        $ quick_menu = True



    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

