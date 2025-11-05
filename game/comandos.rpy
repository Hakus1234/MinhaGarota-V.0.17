label coragem:

    play sound notificacao

    $ coragem += 1

    show not_aries at notify

    return

label vivencia:

    play sound notificacao

    $ vivencia += 1

    show not_sagitario at notify

    d "A Influência de Sagitário (Vivência) atingiu um novo patamar no seu íntimo."

    return

label sexualidade:

    $ sexualidade_max = 300

    if sexualidade < sexualidade_max:

        play sound notificacao

        $ sexualidade += 1

        show not_escorpiao at notify

        if sexualidade == 5 or sexualidade == 10 or sexualidade == 15 or sexualidade == 20 or sexualidade == 25 or sexualidade == 30 or sexualidade == 35 or sexualidade == 40 or sexualidade == 50 or sexualidade == 60:

            d "A Influência de Escorpião (Sexualidade) atingiu um novo patamar no seu íntimo."

            d "Novas opções ficarão disponíveis e outras não poderão mais ser escolhidas."

        elif sexualidade == 70 or sexualidade == 80 or sexualidade == 90 or sexualidade == 100 or sexualidade == 110 or sexualidade == 120 or sexualidade == 130 or sexualidade == 140 or sexualidade == 150:

            d "A Influência de Escorpião (Sexualidade) atingiu um novo patamar no seu íntimo."

            d "Novas opções ficarão disponíveis e outras não poderão mais ser escolhidas."

    return

label trabalho:

    $ trabalho_exp_max = 300

    if trabalho_exp < trabalho_exp_max:

        play sound notificacao

        $ trabalho_exp += 1

        show not_touro at notify

        if trabalho_exp == 10 or trabalho_exp == 20 or trabalho_exp == 30 or trabalho_exp == 40 or trabalho_exp == 50 or trabalho_exp == 60 or trabalho_exp == 70 or trabalho_exp == 80 or trabalho_exp == 90 or trabalho_exp == 100 or trabalho_exp == 110:

            $ trabalho_nivel += 1

            d "A Influência de Touro (Trabalho) atingiu um novo patamar no seu íntimo."

            d "Atender todos os clientes no horário de pico vai levar menos tempo."

        elif trabalho_exp == 120 or trabalho_exp == 130 or trabalho_exp == 140 or trabalho_exp == 150:

            $ trabalho_nivel += 1

            d "A Influência de Touro (Trabalho) atingiu um novo patamar no seu íntimo."

            d "Atender todos os clientes no horário de pico vai levar menos tempo."

        elif trabalho_exp % 10 == 0 and trabalho_exp > 0:

            $ trabalho_nivel += 1

            d "A Influência de Touro (Trabalho) atingiu um novo patamar no seu íntimo."

            d "Atender todos os clientes no horário de pico vai levar menos tempo."
    else:


        t "Não é possível evoluir mais a Influência de Touro (Trabalho) nesta atualização. Mas trabalhe todos os dias se não quiser perder seu avanço."

    $ trabalhou = True

    return

label trabalho_menos:

    if trabalho_exp > 0:

        play sound notificacao

        $ trabalho_exp -= 1

        show not_touro_menos at notify

        if trabalho_exp == 9 or trabalho_exp == 19 or trabalho_exp == 29 or trabalho_exp == 39 or trabalho_exp == 49 or trabalho_exp == 59 or trabalho_exp == 69 or trabalho_exp == 79 or trabalho_exp == 89 or trabalho_exp == 99 or trabalho_exp == 109:

            $ trabalho_nivel -= 1

            d "A Influência de Touro (Trabalho) regrediu um patamar no seu íntimo."

            d "Atender todos os clientes no horário de pico vai levar mais tempo."

        elif trabalho_exp == 119 or trabalho_exp == 129 or trabalho_exp == 139 or trabalho_exp == 149 or trabalho_exp == 159 or trabalho_exp == 169 or trabalho_exp == 179 or trabalho_exp == 189 or trabalho_exp == 199 or trabalho_exp == 209:

            if trabalho_nivel > 10:

                $ trabalho_nivel -= 1

            d "A Influência de Touro (Trabalho) regrediu um patamar no seu íntimo."

            d "Atender todos os clientes no horário de pico vai levar mais tempo."

        elif trabalho_exp == 219 or trabalho_exp == 229 or trabalho_exp == 239 or trabalho_exp == 249 or trabalho_exp == 259 or trabalho_exp == 269 or trabalho_exp == 279 or trabalho_exp == 289 or trabalho_exp == 299 or trabalho_exp == 309:

            if trabalho_nivel > 10:

                $ trabalho_nivel -= 1

            d "A Influência de Touro (Trabalho) regrediu um patamar no seu íntimo."

            d "Atender todos os clientes no horário de pico vai levar mais tempo."

    return

label dilema:

    play sound notificacao



    show not_dilema at notify

    d "Um novo Dilema surgiu em sua vida. Decida o que fazer no espelho"



    return

label conquista:

    play sound notificacao

    show not_conquista at notify



    return

label gabriel:

    $ gabriel_pontos_max = 305

    if gabriel_pontos < gabriel_pontos_max:

        play sound notificacao

        $ gabriel_pontos += 1

        show not_gabriel at notify

        if gabriel_pontos == 7 or gabriel_pontos == 14 or gabriel_pontos == 21 or gabriel_pontos == 30 or gabriel_pontos == 42 or gabriel_pontos == 49 or gabriel_pontos == 60 or gabriel_pontos == 75 or gabriel_pontos == 90 or gabriel_pontos == 105:

            d "Você nota algo diferente nos olhos do [g]. A forma como ele te olha parece mais intensa."

        elif gabriel_pontos == 130 or gabriel_pontos == 155 or gabriel_pontos == 180 or gabriel_pontos == 205 or gabriel_pontos == 230 or gabriel_pontos == 255 or gabriel_pontos == 280 or gabriel_pontos == 305:

            d "Você nota algo diferente nos olhos do [g]. A forma como ele te olha parece mais intensa."
    else:


        t "Não é possível aprofundar sua relação com ele mais do que isto nesta atualização."

    return

label silva:

    $ silva_pontos_max = 224

    if silva_pontos < silva_pontos_max:

        play sound notificacao

        $ silva_pontos += 1

        show not_silva at notify

        if silva_pontos == 5 or silva_pontos == 15 or silva_pontos == 25 or silva_pontos == 35 or silva_pontos == 50 or silva_pontos == 65 or silva_pontos == 80 or silva_pontos == 90 or silva_pontos == 105 or silva_pontos == 120 or silva_pontos == 135:

            d "Você nota algo diferente nos olhos do [s]. A forma como ele te olha parece mais intensa."

        elif silva_pontos == 150 or silva_pontos == 165 or silva_pontos == 180 or silva_pontos == 195 or silva_pontos == 210:

            d "Você nota algo diferente nos olhos do [s]. A forma como ele te olha parece mais intensa."
    else:


        t "Não é possível aprofundar sua relação com ele mais do que isto nesta atualização."

    return

label chefe:

    $ chefe_pontos_max = 119

    if chefe_pontos < chefe_pontos_max:

        play sound notificacao

        $ chefe_pontos += 1

        show not_chefe at notify
    else:


        t "Não é possível aprofundar sua relação com ele mais do que isto nesta atualização."

    if chefe_pontos == 10 or chefe_pontos == 20 or chefe_pontos == 30 or chefe_pontos == 40 or chefe_pontos == 50 or chefe_pontos == 60 or chefe_pontos == 70 or chefe_pontos == 80 or chefe_pontos == 90 or chefe_pontos == 100 or chefe_pontos == 110:

        d "Você nota algo diferente nos olhos do [c]. Ele te olha de forma mais intensa."

    return

label akemi:

    play sound notificacao

    $ akemi_pontos_max = 64

    if akemi_pontos < akemi_pontos_max:

        $ akemi_pontos += 1

        show not_akemi at notify

        if akemi_pontos == 5 or akemi_pontos == 15 or akemi_pontos == 25 or akemi_pontos == 35 or akemi_pontos == 45 or akemi_pontos == 55:

            d "Você nota algo diferente nos olhos da [a]. A forma como ela te olha parece mais intensa."
    else:


        t "Não é possível aprofundar sua relação com ela mais do que isto nesta atualização."

    return

label fernando:

    play sound notificacao

    $ fernando_pontos_max = 109

    if fernando_pontos < fernando_pontos_max:

        $ fernando_pontos += 1

        show not_fernando at notify

        if fernando_pontos % 10 == 0 and fernando_pontos > 0:

            $ aluguel_perdao += 1

            d "Você nota algo diferente nos olhos do [fe]. A forma como ele te olha parece mais intensa."
    else:


        t "Não é possível aprofundar sua relação com ele mais do que isto nesta atualização."

    return

label jasper:

    play sound notificacao

    $ jasper_pontos_max = 99

    if jasper_pontos < jasper_pontos_max:

        $ jasper_pontos += 1

        show not_jasper at notify

        if jasper_pontos == 4 or jasper_pontos == 12 or jasper_pontos == 20 or jasper_pontos == 30 or jasper_pontos == 40 or jasper_pontos == 50 or jasper_pontos == 60 or jasper_pontos == 70 or jasper_pontos == 80 or jasper_pontos == 90:

            d "Você nota algo diferente nos olhos do [j]. A forma como ele te olha parece mais intensa."
    else:


        t "Não é possível aprofundar sua relação com ele mais do que isto nesta atualização."

    return

label zaza:

    play sound notificacao

    $ zaza_pontos_max = 19

    if zaza_pontos < zaza_pontos_max:

        $ zaza_pontos += 1

        show not_zaza at notify

        if zaza_pontos == 10 or zaza_pontos == 20:

            d "Você nota algo diferente nos olhos da [z]. A forma como ela te olha está mais intensa que antes."
    else:


        t "Não é possível aprofundar sua relação com ele mais do que isto nesta atualização."

    return

label tarados:

    play sound notificacao

    $ trabalho_quente += 1

    show not_tarados at notify

    if trabalho_quente == 5 or trabalho_quente == 10 or trabalho_quente == 15 or trabalho_quente == 20 or trabalho_quente == 25 or trabalho_quente == 30 or trabalho_quente == 35 or trabalho_quente == 40:

        d "Os clientes percebem como você tem trabalhado ultimamente e se sentem mais à vontade com você"

    return

label stalker:

    $ stalker_pontos_max = 59

    if stalker_pontos < stalker_pontos_max:

        play sound notificacao

        $ stalker_pontos += 1

        show not_stalker at notify

        if stalker_pontos == 10 or stalker_pontos == 20 or stalker_pontos == 30 or stalker_pontos == 40 or stalker_pontos == 50:

            d "Você nota algo diferente nos olhos do tarado. A forma como ele te olha parece mais intensa."
    else:


        t "Não é possível aprofundar sua relação com ele mais do que isto nesta atualização."

    return

label beto:

    $ beto_pontos_max = 64

    if beto_pontos < beto_pontos_max:

        play sound notificacao

        $ beto_pontos += 1

        show not_beto at notify

        if beto_pontos == 7 or beto_pontos == 14 or beto_pontos == 21 or beto_pontos == 28 or beto_pontos == 35 or beto_pontos == 45 or beto_pontos == 55 or beto_pontos == 65:

            d "Você nota algo diferente nos olhos do [b]. A forma como ele te olha parece mais intensa."
    else:


        t "Não é possível aprofundar sua relação com ele mais do que isto nesta atualização."

    return

label estudo:

    play sound notificacao

    $ estudo_max = 15

    if estudo < estudo_max:

        $ estudo += 1

        show not_gemeos at notify

        if estudo == 5 or estudo == 10 or estudo == 15:

            d "A Influência de Gêmeos (Estudo) atingiu um novo patamar no seu íntimo."

            d "Você entenderá melhor a matéria durante as aulas na faculdade."

    $ estudou = True

    return

label estudo_menos:

    play sound notificacao

    $ estudo -= 1

    show not_gemeos_menos at notify

    if estudo == 4 or estudo == 9 or estudo == 14:

        d "A Influência de Gêmeos (Estudo) regrediu um patamar no seu íntimo."

    return

label inocencia:

    play sound notificacao

    $ sexualidade -= 1



    show not_touro_menos at notify

    if sexualidade == 4 or sexualidade == 9 or sexualidade == 14 or sexualidade == 19 or sexualidade == 24 or sexualidade == 29 or sexualidade == 34 or sexualidade == 39 or sexualidade == 44 or sexualidade == 49 or sexualidade == 54 or sexualidade == 59:

        d "A Influência de Escorpião (Sexualidade) regrediu um patamar no seu íntimo."

        d "Certas opções não poderão mais ser escolhidas e outras foram liberadas novamente."

    elif sexualidade == 64 or sexualidade == 69 or sexualidade == 74 or sexualidade == 79 or sexualidade == 84 or sexualidade == 89 or sexualidade == 94 or sexualidade == 99 or sexualidade == 104 or sexualidade == 109 or sexualidade == 114 or sexualidade == 119:

        d "A Influência de Escorpião (Sexualidade) regrediu um patamar no seu íntimo."

        d "Certas opções não poderão mais ser escolhidas e outras foram liberadas novamente."

    if sexualidade < 0:

        $ sexualidade = 0

    return

label cuidado:

    $ cuidado_max = 100

    if cuidado < cuidado_max:

        play sound notificacao

        $ cuidado += 1

        show not_sagitario at notify

        if cuidado % 10 == 0 and cuidado > 0:

            d "A Influência de Sagitário (Autoestima) atingiu um novo patamar no seu íntimo."

            d "Melhorar seu amor próprio te garante autoestima para usar novas roupas."
    else:




        d "Não é possível aumentar mais a Autoestima nesta atualização. Mas tome banho a cada dois dias se não quiser perder seu avanço."

    $ cuidou = 0

    return

label cuidado_menos:

    play sound notificacao

    $ cuidado -= 1

    show not_sagitario_menos at notify

    if cuidado == 9 or cuidado == 19 or cuidado == 29 or cuidado == 39 or cuidado == 49 or cuidado == 59 or cuidado == 69 or cuidado == 79 or cuidado == 89 or cuidado == 99:

        d "A Influência de Sagitário (Autoestima) regrediu um patamar no seu íntimo."

    return

label fama:

    $ fama_max = 199

    if fama_pontos < fama_max:

        play sound notificacao

        $ fama_pontos += 1

        show not_leao at notify

        if fama_pontos % 10 == 0 and fama_pontos > 0:

            d "A Influência de Leão (Fama) atingiu um novo patamar no seu íntimo."

            d "Sua popularidade nas redes sociais aumentou, assim como o dinheiro que você recebe com sua imagem."



    return

label exibicionismo:

    $ exibicionismo_max = 94

    if ( exibicionismo_pontos < exibicionismo_max ) and exibicionismo < 12:

        play sound notificacao

        $ exibicionismo_pontos += 1

        show not_libra at notify

        if exibicionismo_pontos % 5 == 0 and exibicionismo_pontos > 0:

            $ exibicionismo += 1

            $ exibicionismo_evento = True

            d "A Influência de Libra (Romantismo) atingiu um novo patamar no seu íntimo."

            d "Sua presença na praia não pode ser ignorada e mais homens esperam para te ver tomando sol."

    return



label dormir:



    scene black with Dissolve(1.0)

    stop music fadeout 2.0

    $ tempo = 1



    if masturbacao == 0 and sexualidade >= 10:

        $ masturbacao = 1

        play sound cama

        scene black with dissolve

        scene mcm_cama1 with Dissolve(1.0)

        mc "Hmmm..."

        "Não tô conseguindo dormir..."

        play sound cama

        scene black with dissolve

        scene mcm_cama2 with Dissolve(1.0)

        "Eu fecho os olhos mas não consigo dormir!"

        "Giro pra cá... giro pra lá..."

        mc "Tá dando até calor! Que droga!"

        "Já abri a janela... mas não resolve. Será que eu compro um ventilador?"

        "Até parece que eu tenho grana pra comprar essas coisas..."

        "Bom... não preciso dormir com um pijamão desses também, né?"

        "M-mas..."

        label masturbacao1:

            pass

        menu:
            "Talvez se eu abrir um pouco meu pijama":


                "Talvez abrir um pouquinho..."
            "Vou dormir pelada de uma vez":


                "Esse calora té me dando vontade... mas imagina se minha mãe soubesse uma coisa dessas?"

                "N-não posso..."

                d "Você não tem Influência de Escorpião (Sexualidade) suficiente para tomar esta decisão."

                jump masturbacao1

        play sound cama

        scene black with dissolve

        if streamer:

            scene cama3_d with Dissolve(1.0)
        else:


            scene cama3 with Dissolve(1.0)

        mc "M-melhor..."

        "Eu nunca teria coragem de fazer isso lá em casa."

        "Mas também nunca senti um calor desses lá..."

        mc "Ah..."

        "Tem muita coisa nova acontecendo comigo aqui na cidade..."

        "Eu tô conhecendo tantas pessoas... o senhor Fernando, o chefe Jasper, o Gabriel..."

        mc "Ai, Gabriel... por que você..."

        mc "T-tá me dando mais calor..."

        "Será que a gente..."

        show black with dissolve

        hide black with dissolve

        "Não vejo a hora de ver o que vai rolar amanhã..."

        scene black with Dissolve(1.0)

    elif masturbacao == 1 and sexualidade >= 20 and rand < 34:

        play sound cama

        scene black with dissolve

        scene mcm_cama2 with Dissolve(1.0)

        "Hmm... de novo eu tô assim..."

        "Eu nunca tive essa dificuldade pra dormir na fazenda."

        menu:
            "Vou abrir o pijama de novo":


                pass

        play sound cama

        scene black with dissolve

        if streamer:

            scene cama3_d with Dissolve(1.0)
        else:


            scene cama3 with Dissolve(1.0)

        "Vê se esse calor passa..."

        call masturbacao_cena

        "Ai... eu não consigo dormir assim!"

        "Minhas pernas..."

        mc "Ahh..."

        "Que sensação m-mais... forte... eu tô sentindo..."

        "Tô tão quente... caramba..."

        "Só abrir o pijama não adianta. O problema é nas minhas coxas."

        menu:
            "Não... [mc]... só dorme, garota...":


                "E-eu... não tá certo dormir toda pelada..."

                "Você nunca fez isso... só aguentar..."

                "Uma hora você vai dormir..."

                "..."

                "Uma hora..."

                show black with dissolve

                hide black with dissolve

                "Tá chegando..."

                $ tempo = 2
            "Eu... eu vou tirar tudo... é o único jeito de acabar com esse calor":


                $ masturbacao = 2

                "Eu preciso... ou vou perder a noite toda virando pra lá e pra cá."

                play sound cama

                scene black with dissolve

                if streamer:

                    scene cama4_d with Dissolve(1.0)
                else:


                    scene cama4 with Dissolve(1.0)

                mc "A-assim... Ah..."

                "O calor tem que passar..."

                "Tenho que parar de pensar nessas coisas... essas coisas que me deixam assim..."

                "Só quero poder dormir..."

                show black with dissolve

                hide black with dissolve

                "Mas essa sensação... hmmm..."

        scene black with Dissolve(1.0)

    elif masturbacao == 2 and sexualidade >= 30 and rand < 20:

        play sound cama

        scene black with dissolve

        if streamer:

            scene cama3_d with Dissolve(1.0)
        else:


            scene cama3 with Dissolve(1.0)

        "Já sei que vai vir aquele calor... deixa eu só abrir isso logo..."

        mc "Hmm... de novo..."

        "As pernas... o problema é nas pernas..."

        play sound cama

        scene black with dissolve

        if streamer:

            scene cama4_d with Dissolve(1.0)
        else:


            scene cama4 with Dissolve(1.0)

        mc "Isso..."

        "Tô tão livre... sinto o ar passando por eu todinha..."

        call masturbacao_cena

        mc "Hmmm... por que tô pensando nessas coisas agora?"

        "Ai, minha nossa senhora.... Como eu vou dormir assim..."

        mc "Nngh..."

        menu:
            "Não... eu sei onde isso vai dar...":


                "Tá na cara o que meu corpo quer... mas não tá certo!"

                "Eu quero... mas não posso. Foi o que a mamãe e todo mundo falou. Só tenho que resistir."

                "Uma hora você vai dormir..."

                "..."

                "Uma hora..."

                show black with dissolve

                hide black with dissolve

                "Tá chegando..."

                $ tempo = 2
            "Eu... preciso entender isso melhor... essa excitação...":


                $ masturbacao = 3

                "Tenho que entender de onde vem esse fogo. Essa vontade tão forte!"

                "Tenho que..."

                play sound cama

                scene black with dissolve

                if streamer:

                    scene cama6_d with Dissolve(1.0)
                else:


                    scene cama6 with Dissolve(1.0)

                mc "A-assim... Ah..."

                "É daqui... bem do meu das minhas pernas... tá me chamando pra mexer."

                "Que vontade de mexer com os dedinhos... passando a mãozinha nela."

                "Meus peitinhos também... eles querem carinho..."

                "O que tá acontecendo comigo? Desde quando eu penso nessas coisas?"

                "Isso não tá certo, [mc]... não foi assim que a mãe te ensinou. Ela disse que isso é errado."

                "Ai... que quente... hmm..."

                show black with dissolve

                hide black with dissolve

                "Mas essa sensação... hmmm... eu só quero dormir..."

        scene black with Dissolve(1.0)

    elif masturbacao == 3 and sexualidade >= 40 and rand < 20:

        play sound cama

        scene black with dissolve

        if streamer:

            scene cama4_d with Dissolve(1.0)
        else:


            scene cama4 with Dissolve(1.0)

        "De novo eu assim... sem calça... com esse fogo no meio das pernas..."

        "Essa dificuldade de dormir..."

        "Cada dia acontece alguma coisa diferente nesta capital."

        play sound cama

        scene black with dissolve

        if streamer:

            scene cama6_d with Dissolve(1.0)
        else:


            scene cama6 with Dissolve(1.0)

        mc "Aahh..."



        "Não tem como eu não perceber as mudanças. Eu não sou mais a mesma que chegou aqui."

        "A mocinha inocente que dava um gritinho por qualquer coisa."

        "Eu tô descobrindo novas sensações... e eu sinto que é um caminho sem volta..."

        "Descobrir esse novo mundo é incrível, é prazeroso demais, mas também me dá medo."

        "O que eu faço?"

        menu:
            "Só vou dormir. Não quero saber disso.":


                "Tá na cara o que meu corpo quer... mas não tá certo!"

                "Eu quero... mas não posso. Foi o que a mamãe e todo mundo falou. Só tenho que resistir."

                "Uma hora você vai dormir..."

                "..."

                "Uma hora..."

                show black with dissolve

                hide black with dissolve

                "Tá chegando..."

                $ tempo = 2
            "Eu quero me tocar. Quero sentir mais.":


                $ masturbacao = 4

                "Tenho que entender de onde vem esse fogo. Essa vontade tão forte!"

                "Tenho que..."

                play sound gemido1

                scene black with dissolve

                if streamer:

                    scene cama7_d with Dissolve(1.0)
                else:


                    scene cama7 with Dissolve(1.0)

                pause 2.0

                mc "Ah... meus peitinhos... meu biquinho..."

                "É tão gostoso quando eu massageio eles assim... de leve... hmmmm..."

                "E quando eu aperto... dói... mas é gostoso..."

                "Meu corpo tá tão sensível... hmmm... eu quero uma mão me apertando..."

                "Quero sentir alguém me fazendo me sentir bem..."

                "Tá tão gostoso... mas não sei o que eu faço... eu... eu tenho que tocar ela?"

                "N-não posso... e agora?"

                show black with dissolve

                hide black with dissolve

                "Mas essa sensação... hmmm... eu só quero dormir..."

        scene black with Dissolve(1.0)

    elif masturbacao == 4 and sexualidade >= 50 and rand < 20:

        play sound cama

        scene black with dissolve

        if streamer:

            scene cama6_d with Dissolve(1.0)
        else:


            scene cama6 with Dissolve(1.0)

        "Eu já tô de perna aberta... com os peitinhos de fora..."

        "Meus biquinhos tão durinhos... esperando minha mão..."

        play sound gemido1

        scene black with dissolve

        if streamer:

            scene cama7_d with Dissolve(1.0)
        else:


            scene cama7 with Dissolve(1.0)

        mc "Aahh..."



        mc "Eu tô cada vez me tocando mais. Isso não pode tá certo..."

        "Que garota que se toca sozinha em casa? Não foi assim que minha mãe me ensinou..."

        mc "Hmmm..."

        mc "Mas não consigo. Tanta coisa acontecendo, e eu tenho cada vez mais desejo."

        "Tenho vontade de sentir no meu corpo todo... alguém me pegando, alguém me fazendo sentir gostoso..."

        "Não tem ninguém... e ela tá chamando..."

        menu:
            "Não posso ceder... não posso tocar nela.":


                "Tá na cara o que meu corpo quer... mas não tá certo!"

                "Eu quero... mas não posso. Foi o que a mamãe e todo mundo falou. Só tenho que resistir."

                "Uma hora você vai dormir..."

                "..."

                "Uma hora..."

                show black with dissolve

                hide black with dissolve

                "Tá chegando..."

                $ tempo = 2
            "Vou tocar gostoso na minha vagina...":


                $ masturbacao = 5

                "Não aguento mais! Ela tá me obrigando!"

                play sound gemido2

                scene black with dissolve

                if streamer:

                    scene cama8_d with Dissolve(1.0)
                else:


                    scene cama8 with Dissolve(1.0)

                pause 2.0

                mc "Isso... ahmmm... finalmente!"

                "Meu dedo acariciando minha preciosa... esse botãozinho delicado..."

                mc "Hmmm..."

                "É tão gostoso quando eu esfrego o dedo nela. Me dá vontade de fazer mais forte, mais rápido."

                mc "Aah... quero um mãozão me esfregando... uma mão gostosa de um homem que me deixa louca."

                mc "Mas só tenho meus dedinhos... eles são tão leves... aahh..."

                "Eles vão me satisfazer assim?!"

                mc "Nnnghhh..."

                "Eu quero mais... preciso de mais..."

                mc "Quero sentir mais gostoso... aaah... quero sentir tudo!"

                show black with dissolve

                hide black with dissolve

                "Mas essa sensação... hmmm... eu só quero dormir..."

        scene black with Dissolve(1.0)

    elif masturbacao == 5 and sexualidade >= 60 and rand < 20:

        play sound cama

        scene black with dissolve

        scene cama7 with Dissolve(1.0)

        "Ai... de novo essa sensação..."

        "Esse calor no meu corpo... essa vontade incontrolável..."

        "Eu preciso... eu preciso tocar..."

        "Mas... será que é certo?"

        "O que a mamãe ia pensar?"

        play sound gemido1

        scene black with dissolve

        scene cama8 with Dissolve(1.0)

        "Ah... que se dane a mamãe..."

        "Eu preciso disso..."

        "Preciso me sentir bem..."

        mc "Aahh..."

        menu:
            "Continuar se tocando":


                $ masturbacao = 6

                "Meus dedos deslizam pela minha pele úmida, explorando cada cantinho do meu corpo. Meus seios estão sensíveis, os mamilos duros e doloridos. Eu os acaricio, os aperto, os chupo, gemendo baixinho."

                "Minha mão desce até minha intimidade, meus dedos encontrando meu clitóris já latejante."

                "Eu o acaricio com movimentos circulares, aumentando a pressão, sentindo o prazer se espalhar por todo meu corpo."

                play sound gemido2

                scene black with dissolve

                scene cama9 with Dissolve(1.0)

                "Nathan... Gabriel... ah... o pai do Gabriel..."

                "Seus rostos se misturam na minha mente, suas vozes roucas sussurrando meu nome... me chamando de gostosa e outras coisas vulgares..."

                "Eu gemo mais alto, meu corpo se contorcendo de prazer. Eu me sinto tão suja... tão depravada..."

                "Mas tão... viva..."

                "Eu não consigo parar... o prazer é intenso demais..."

                "Quero sentir mais... quero gozar..."

                mc "Aahh... mais... mais forte..."

                "Eu aumento a velocidade dos meus movimentos, meus dedos me esfregando com mais força. Meu corpo se contrai, ondas de prazer me levando cada vez mais perto do limite."

                "Eu vou... eu vou..."

                "Por mais que eu tente... algo tá errado... eu não consigo chegar lá..."

                "Ah... ah... ah..."

                "Eu gozei... com tanta força..."

                "Meu corpo inteiro treme de tesão... e eu me sinto... pronta pra explodir..."

                show black with dissolve

                hide black with dissolve

                "Eu quero... hmm..."
            "Parar":


                "Eu preciso parar... isso não está certo..."

                "Eu não posso me entregar a esse desejo..."

                "Eu preciso me controlar..."

                scene black with dissolve

                scene cama10 with Dissolve(1.0)

                mc "Ah... não... eu... eu preciso parar..."

                "Eu tiro a mão do meu corpo, sentindo um vazio doloroso me invadir. Eu estou frustrada... mas também aliviada..."

                "Eu preciso pensar..."

                "Eu preciso entender o que tá acontecendo comigo..."

    elif masturbacao == 6 and sexualidade >= 70 and rand < 20:

        play sound cama

        scene black with dissolve

        scene cama11 with Dissolve(1.0)

        "Ah... de novo essa excitação..."

        "Meu corpo inteiro formiga... pulsa..."

        "Eu preciso de mais..."

        "Meus dedos... explorando minha pele... me tocando... me provocando..."

        "Mas não é o suficiente..."

        "Eu preciso de algo mais... eu quero gozar... quero soltar tudo isso que tá me frustrando pra fora!"

        mc "A-ah... e-eu..."

        "Um pensamento proibido surge na minha mente... me assusta... me excita..."

        "E se... e se eu..."

        "E se eu colocar meu dedo... lá dentro...?"

        "Ai meu Deus... não..."

        "Isso é errado... sujo..."

        "O que a mamãe ia dizer?"

        "Mas... a Zaza..."

        "Ela disse que eu preciso explorar meu corpo... meu desejo..."

        "Que eu preciso ser dona de mim mesma..."

        "E o Gabriel, o idiota do Jasper... o Nathan..."

        "Eles fariam isso comigo... sem pensar duas vezes..."

        "Então... por que eu não posso?"

        menu:
            "Enfiar o dedo e explorar":


                $ masturbacao = 7

                play sound gemido2

                scene black with dissolve

                scene cama12 with Dissolve(1.0)

                pause 2.0

                mc "A-ah..."

                "Com dedos trêmulos, eu me toco... explorando minha entrada... sentindo a umidade..."

                "É tão... sensível..."

                "Tão... apertado..."

                "Eu respiro fundo... e com cuidado... insiro a ponta do meu dedo..."

                mc "A-ai..."

                play sound gemido3

                "Uma onda de prazer percorre meu corpo... me fazendo gemer alto."

                "É tão... diferente..."

                "Tão... intenso..."

                "Eu nunca me senti assim antes..."

                "Eu quero mais..."

                "Eu preciso sentir mais... preciso ir mais fundo..."

                mc "Ah... m-mais..."

                "Eu empurro meu dedo com cuidado... sentindo as paredes da minha vagina se contraírem."

                "É tão... apertado... tão quente..."

                "E tão... gostoso..."

                "Eu gemo... meu corpo se arqueando... buscando mais contato... mais prazer..."

                "Gabriel... Nathan... os tarados do bar..."

                "Quero sentir vocês... dentro de mim..."

                "Quero que vocês me fodam... com força..."

                "Quero que vocês me façam..."

                show black with dissolve

                hide black with dissolve

                "Gozar..."
            "Parar":


                "Eu preciso parar... isso é demais pra mim..."

                "Eu não posso..."

                "Eu não consigo..."

                mc "Ah... n-não... eu preciso parar..."

                "Eu tiro meu dedo, sentindo um vazio doloroso me invadir. Eu estou assustada... confusa..."

                "Mas... excitada..."

                "O que está acontecendo comigo...?"

    elif masturbacao == 8 and sexualidade >= 60:

        ""
    else:


        if rand < 15:

            if masturbacao == 1 and sexualidade >= 10:

                play sound cama

                scene black with dissolve

                scene mcm_cama2 with Dissolve(1.0)

                "De novo aquele calor..."

                menu:
                    "Deixa eu abrir o pijama":


                        pass

                play sound cama

                scene black with dissolve

                if streamer:

                    scene cama3_d with Dissolve(1.0)
                else:


                    scene cama3 with Dissolve(1.0)

                mc "M-melhor..."

                "Sorte que ninguém pode me ver assim..."

                "Imagina o que eles iam falar se me vissem desse jeito?"

                mc "Ai..."

                "O que eu tô pensando?"

                show black with dissolve

                hide black with dissolve

                "Tenho que tomar cuidado com essa cidade. Ela é muito louca..."

            elif masturbacao == 2 and sexualidade >= 20:

                play sound cama

                scene black with dissolve

                if streamer:

                    scene cama3_d with Dissolve(1.0)
                else:


                    scene cama3 with Dissolve(1.0)

                "Hmm..."

                "Sorte que ninguém pode me ver assim..."

                "Imagina o que eles iam falar se me vissem desse jeito?"

                mc "Ai..."

                "Mas se eles vissem... será que eles iam gostar?"

                "Dos meus peitos... das minhas coxas... da minha bunda..."

                mc "Aahhn..."

                play sound cama

                scene black with dissolve

                if streamer:

                    scene cama4_d with Dissolve(1.0)
                else:


                    scene cama4 with Dissolve(1.0)

                "Eu tô tão quente... essa sensação toma conta de mim!"

                "Quero me sentir bem... meu corpo quer carinho... quer atenção..."

                mc "Hmmm..."

                show black with dissolve

                hide black with dissolve

                "Ninguém vai fazer nada comigo?"

            elif masturbacao == 3 and sexualidade >= 30:

                play sound cama

                scene black with dissolve

                if streamer:

                    scene cama3_d with Dissolve(1.0)
                else:


                    scene cama3 with Dissolve(1.0)

                "Já sei que vai vir aquele calor... deixa eu só abrir isso logo..."

                mc "Hmm... de novo..."

                "As pernas... o problema é nas pernas..."

                play sound cama

                scene black with dissolve

                if streamer:

                    scene cama4_d with Dissolve(1.0)
                else:


                    scene cama4 with Dissolve(1.0)

                mc "Isso..."

                "Tô tão livre... sinto o ar passando por eu todinha..."

                call masturbacao_cena

                "Ai, minha nossa senhora.... Como eu vou dormir assim..."

                mc "Nngh..."

                "Tenho que entender de onde vem esse fogo. Essa vontade incontrolável!"

                play sound cama

                scene black with dissolve

                if streamer:

                    scene cama6_d with Dissolve(1.0)
                else:


                    scene cama6 with Dissolve(1.0)

                mc "A-assim... Ah..."

                "É daqui... tá me chamando pra mexer."

                "Que vontade de mexer com os dedinhos... passando a mãozinha neles."

                "Meus peitinhos também... eles querem carinho..."

                "O que tá acontecendo comigo? Desde quando eu penso nessas coisas?"

                "Ai... que quente... hmm..."

                show black with dissolve

                hide black with dissolve

                "Mas essa sensação... hmmm..."

            elif masturbacao == 4 and sexualidade >= 40:

                play sound cama

                scene black with dissolve

                if streamer:

                    scene cama4_d with Dissolve(1.0)
                else:


                    scene cama4 with Dissolve(1.0)

                "De novo eu assim... sem calça... com esse fogo no meio das pernas..."

                "Essa dificuldade de dormir..."

                "Cada dia acontece alguma coisa diferente nesta capital."

                play sound cama

                scene black with dissolve

                if streamer:

                    scene cama6_d with Dissolve(1.0)
                else:


                    scene cama6 with Dissolve(1.0)

                mc "Aahh..."

                "Descobrir esse novo mundo é incrível, é prazeroso demais, mas também me dá medo."

                "Tenho que entender de onde vem esse fogo. Essa vontade tão forte!"

                "Tenho que..."

                play sound gemido1

                scene black with dissolve

                if streamer:

                    scene cama7_d with Dissolve(1.0)
                else:


                    scene cama7 with Dissolve(1.0)

                pause 2.0

                mc "Ah... meus peitinhos... meu biquinho..."

                "É tão gostoso quando eu massageio eles assim... de leve... hmmmm..."

                "E quando eu aperto... dói... mas é gostoso..."

                "Meu corpo tá tão sensível... hmmm... eu quero uma mão me apertando..."

                "Quero sentir alguém me fazendo me sentir bem..."

                "Tá tão gostoso... mas não sei o que eu faço... eu... eu tenho que tocar ela?"

                "N-não posso... e agora?"

                show black with dissolve

                hide black with dissolve

                "Mas essa sensação... hmmm... eu só quero dormir..."

            elif masturbacao == 5:

                play sound cama

                scene black with dissolve

                if streamer:

                    scene cama6_d with Dissolve(1.0)
                else:


                    scene cama6 with Dissolve(1.0)

                "Eu já tô de perna aberta... com os peitinhos de fora..."

                "Meus biquinhos tão durinhos... esperando minha mão..."

                play sound gemido1

                scene black with dissolve

                if streamer:

                    scene cama7_d with Dissolve(1.0)
                else:


                    scene cama7 with Dissolve(1.0)

                mc "Aahh..."

                mc "Eu tô cada vez me tocando mais. Isso não pode tá certo..."

                mc "Hmmm..."

                mc "Mas não consigo. Tanta coisa acontecendo, e eu tenho cada vez mais desejo."

                "Tenho vontade de sentir no meu corpo todo... alguém me pegando, alguém me fazendo sentir gostoso..."

                "Não aguento mais! Ela tá me obrigando!"

                play sound gemido2

                scene black with dissolve

                if streamer:

                    scene cama8_d with Dissolve(1.0)
                else:


                    scene cama8 with Dissolve(1.0)

                pause 2.0

                mc "Isso... ahmmm... finalmente!"

                "Meu dedo acariciando minha preciosa... esse botãozinho delicado aqui..."

                mc "Hmmm..."

                "É tão gostoso quando eu esfrego o dedo nela. Me dá vontade de fazer mais forte, mais rápido."

                mc "Aah... quero um mãozão me esfregando... uma mão gostosa de um homem que me deixa louca."

                mc "Mas só tenho meus dedinhos... eles são tão leves... aahh..."

                "Eles vão me satisfazer assim?!"

                mc "Nnnghhh..."

                "Eu quero mais... preciso de mais..."

                mc "Quero sentir mais gostoso... aaah... quero sentir tudo!"

                show black with dissolve

                hide black with dissolve

                "Mas essa sensação... hmmm... eu preciso de mais..."

            elif masturbacao == 6:

                "Ah... de novo essa excitação..."

                "Meu corpo inteiro formiga... pulsa..."

                "Eu preciso de mais..."

                play sound gemido2

                scene black with dissolve

                scene cama11 with Dissolve(1.0)

                "Minha mão desce até minha intimidade, meus dedos encontrando meu clitóris já latejante."

                "Eu o acaricio com movimentos circulares, aumentando a pressão, sentindo o prazer se espalhar por todo meu corpo."

                call masturbacao_fala

                show black with dissolve

                hide black with dissolve

                "Eu tô... cada vez mais perto..."

            elif masturbacao == 7:

                play sound gemido2

                scene black with dissolve

                scene cama11 with Dissolve(1.0)

                "Ah... de novo essa excitação..."

                "Meu corpo inteiro formiga... pulsa..."

                "Eu preciso de mais..."

                "Meus dedos... explorando minha pele... me tocando... me provocando..."

                play sound gemido3

                scene black with dissolve

                scene cama12 with Dissolve(1.0)

                "Com dedos trêmulos, eu me toco... explorando minha entrada... sentindo a umidade..."

                "É tão... sensível..."

                "Tão... apertado..."

                "Eu respiro fundo... e com cuidado... insiro a ponta do meu dedo..."

                mc "A-ai..."

                play sound gemido3

                "Uma onda de prazer percorre meu corpo... me fazendo gemer alto."

                call masturbacao_fala

                show black with dissolve

                hide black with dissolve

                "Falta pouco... tão pouco... aahhnn..."

            scene black with Dissolve(1.0)



    if fadolandia == 0 and dia_total >= 11:

        jump fadolandia

    label dormir_depois:

        pass



    if estudo > 0 and not estudou:

        call estudo_menos

    if trabalho_exp > 0 and not trabalhou:

        call trabalho_menos

    if cuidado > 0 and cuidou > 4:

        call cuidado_menos

    $ cuidou += 1

    $ dia += 1
    $ dia_total += 1
    $ semana += 1

    if semana > 7:

        $ semana = 1



        $ familia_check = False

    call define_dia_semana

    call daily



    call save_game

    call dormir_evento



    if rand <= 14:

        $ chovendo = True
    else:


        $ chovendo = False

    scene casa sala with Dissolve(1.0)

    "{b}[semana_dia], [dia]/[mes]{/b}"

    if chovendo:

        call chuva_pensamentos
    else:


        call dia_pensamentos

    call passos

    if trabalho == 2:

        jump trabalho_evento

    if semana == 1:

        jump fernando_evento

        $ renpy.save("None-semanal", extra_info="None-semanal")

    $ area = "casa"
    $ mapa = "sala"

    show screen navegar with Dissolve(0.3)

    pause

label masturbacao_fala:

    if mast_fala == 0:
        mc "Ah... como é bom se tocar..."
        mc "Meu corpo todo formiga... essa sensação..."
        mc "Eu quero... quero sentir mais..."

    elif mast_fala == 1:
        mc "Gabriel... Akemi... Nathan......"
        mc "Imagino as mãos deles no meu corpo..."
        mc "Me tocando... me fazendo gemer..."

    elif mast_fala == 2:
        mc "Ah... eu tô tão molhada..."
        mc "Minha calcinha tá encharcada..."
        mc "Eu preciso gozar..."

    elif mast_fala == 3:
        mc "Eu quero sentir um pau dentro de mim..."
        mc "Me fodendo com força... me fazendo gritar..."
        mc "Me levando ao limite..."

    elif mast_fala == 4:
        mc "Eu sou uma vadia... uma putinha..."
        mc "Mas eu gosto... eu adoro..."
        mc "Quero ser usada... abusada..."

    elif mast_fala == 5:
        mc "Meus dedos... deslizando... explorando..."
        mc "Tão molhada... tão sensível..."
        mc "Quero sentir mais... preciso de mais..."
        mc "Ah... isso... bem aqui..."

    elif mast_fala == 6:
        mc "Meu clitóris... pulsando... latejando..."
        mc "Esfregando... pressionando... ah..."
        mc "A cada toque... o prazer aumenta..."
        mc "Eu vou gozar... eu vou..."

    elif mast_fala == 7:
        mc "Com cuidado... eu insiro meu dedo..."
        mc "Tão apertado... tão quente..."
        mc "Uma onda de calor me percorre..."
        mc "Quero ir mais fundo... sentir mais..."

    elif mast_fala == 8:
        mc "Meus gemidos... escapam dos meus lábios..."
        mc "Não consigo me controlar..."
        mc "Jasper... me fode... me possui..."
        mc "Ah... ah... ah..."

    elif mast_fala == 9:
        mc "Eu me sinto... tão suja... tão safada..."
        mc "Mas o prazer... é tão intenso..."
        mc "Eu não quero parar... nunca mais..."
        mc "Eu quero... quero mais..."
    else:


        $ mast_fala = -1

    $ mast_fala += 1

    return

label dia_pensamentos:

    if dia_fala == 0:

        mc "Acordei... ufa... mais um dia nessa cidade maluca..."

    elif dia_fala == 1:

        mc "Hoje eu tô me sentindo meio ansiosa... será que vai dar tudo certo?"

    elif dia_fala == 2:

        mc "Ai... só queria um dia de paz... sem stress..."

    elif dia_fala == 3:

        mc "Preciso focar nos estudos e no trabalho... não posso me distrair..."

    elif dia_fala == 4:

        mc "Credo, que sono... queria ficar na cama o dia todo..."

    elif dia_fala == 5:

        mc "Hoje o dia promete ser difícil... preciso me manter forte..."

    elif dia_fala == 6:

        mc "Eu consigo... eu vou conseguir... é só acreditar em mim mesma..."

    elif dia_fala == 7:

        mc "Será que eu sou capaz de tudo isso? Às vezes, eu duvido..."

    elif dia_fala == 8:

        mc "Todo mundo merece ser feliz... eu também... eu mereço..."

    elif dia_fala == 9:

        mc "Acho que tô no caminho certo... a vida aqui tá me ensinando muito..."

    elif dia_fala == 10:

        mc "Sou grata por ter saúde, um lugar pra morar, amigos... e comida!"

    elif dia_fala == 11:

        mc "Tô aprendendo a me virar sozinha... a vida adulta não é fácil..."

    elif dia_fala == 12:

        mc "Não preciso de homem pra ser feliz... eu sou suficiente..."

    elif dia_fala == 13:

        mc "Será que eu tô ficando mais bonita? Acho que me cuidar tá funcionando..."

    elif dia_fala == 14:

        mc "É bom saber que os homens me acham atraente... me sinto mais confiante..."

    elif dia_fala == 15:

        mc "Eu tenho o poder de escolher o que eu quero pra minha vida... ninguém vai me controlar..."

    elif dia_fala == 16:

        mc "Vou ser psicóloga... vou ajudar as pessoas... esse é o meu sonho..."

    elif dia_fala == 17:

        mc "O mundo precisa de mais mulheres fortes... que lutam pelo que acreditam..."

    elif dia_fala == 18:

        mc "Será que eu vou encontrar o amor verdadeiro aqui na capital?"

    elif dia_fala == 19:

        mc "Hoje é um novo dia... e eu vou fazer dele o melhor possível..."

    elif dia_fala == 20:

        mc "Ai... tô com saudades da minha família..."

    elif dia_fala == 21:

        mc "Será que eu ligo pra mãe hoje? Ela deve estar preocupada..."

    elif dia_fala == 22:

        mc "Meu pai nunca vai entender a minha vida aqui..."

    elif dia_fala == 23:

        mc "Acho que eu tô mudando... não sou mais a mesma garota que saiu da fazenda..."

    elif dia_fala == 24:

        mc "A capital é um lugar cheio de oportunidades... mas também de perigos..."

    elif dia_fala == 25:

        mc "Eu preciso tomar cuidado com os homens aqui... nem todos são confiáveis..."

    elif dia_fala == 26:

        mc "O Jasper é um idiota... mas eu preciso dele... preciso do dinheiro."

    elif dia_fala == 27:

        mc "O Gabriel é um fofo... mas será que ele é o homem certo pra mim?"

    elif dia_fala == 28:

        mc "O Nathan é tão misterioso... e tão sexy..."

    elif dia_fala == 29:

        mc "O Sr. Silva é um grosso... mas tem algo nele que me atrai..."

    elif dia_fala == 30:

        mc "Eu tô tão confusa... eu não sei o que eu quero..."

    elif dia_fala == 31:

        mc "Eu preciso me concentrar em mim... nos meus sonhos..."

    elif dia_fala == 32:

        mc "Eu não vou deixar que ninguém me derrube..."

    elif dia_fala == 33:

        mc "Eu vou ser feliz... custe o que custar..."

    elif dia_fala == 34:

        mc "Eu sou mais forte do que eu penso..."

    elif dia_fala == 35:

        mc "Bom dia, mundo! Eu sou capaz de tudo..."

    elif dia_fala == 36:

        mc "Eu vou realizar meus sonhos... começando hoje!"

    elif dia_fala == 37:

        mc "Eu vou ser a melhor versão de mim mesma... nossa... eu tô muito poética esses dias ksks..."

    elif dia_fala == 38:

        mc "Eu vou amar e ser amada... nossa que otimismo que eu tô sentindo, gente!"

    elif dia_fala == 39:

        mc "Eu vou ser feliz..."

        mc "S-será? Eu... tava tão bem... mas... passou..."

    elif dia_fala == 40:

        mc "Ai... tô com saudades do cheiro da terra molhada depois da chuva..."

    elif dia_fala == 41:

        mc "Lembro do céu estrelado da fazenda... aqui na capital mal dá pra ver as estrelas..."

    elif dia_fala == 42:

        mc "Que vontade de tomar um café da manhã com pão de queijo quentinho que nem a minha mãe fazia..."

    elif dia_fala == 43:

        mc "Sinto falta de acordar com o canto dos passarinhos... aqui só escuto buzina..."

    elif dia_fala == 44:

        mc "A vida na fazenda era mais simples... mas também era mais solitária..."

    elif dia_fala == 45:

        mc "Aqui na capital eu conheci tanta gente... mas será que algum deles é amigo de verdade?"

    elif dia_fala == 46:

        mc "Às vezes me sinto perdida em meio a tanta gente... na fazenda eu me sentia mais conectada com a natureza..."

    elif dia_fala == 47:

        mc "Eu nunca imaginei que a vida na cidade grande fosse tão corrida... na fazenda o tempo passava mais devagar..."

    elif dia_fala == 48:

        mc "Será que eu fiz a escolha certa? Deixar tudo para trás e vir pra cá?"

    elif dia_fala == 49:

        mc "E-eu não posso desistir agora... eu preciso realizar meus sonhos..."

    elif dia_fala == 50:

        mc "Eu sinto falta da minha égua Estrela... será que ela ainda lembra de mim?"

    elif dia_fala == 51:

        mc "Eu me lembro de quando eu era criança e corria pelos campos da fazenda... era tão livre..."

    elif dia_fala == 52:

        mc "Aqui na capital eu me sinto presa... presa nos prédios... presa na rotina..."

    elif dia_fala == 53:

        mc "Aqui eu também me sinto... mais viva... mais conectada com o mundo..."

    elif dia_fala == 54:

        mc "Eu tô aprendendo a ser uma mulher independente... a me cuidar... a me valorizar..."

    elif dia_fala == 55:

        mc "A vida na fazenda me ensinou a ser forte... a ser resiliente..."

    elif dia_fala == 56:

        mc "Eu nunca vou esquecer as minhas raízes... a minha família... a minha história..."

    elif dia_fala == 57:

        mc "Não cou esquecer a fazenda, mas também não vou deixar de viver o presente... de aproveitar as oportunidades que a vida me oferece..."

    elif dia_fala == 58:

        mc "Eu sou uma mistura da garota da fazenda e da mulher da cidade... e eu estou bem com isso! E-eu acho..."

    elif dia_fala == 59:

        mc "Eu sou... eu... ai..."
    else:


        $ dia_fala = -1

    $ dia_fala += 1

    return

label chuva_pensamentos:

    if chuva_fala == 0:

        mc "A chuva cai lá fora... o barulho das gotas batendo na janela me acalma..."

    elif chuva_fala == 1:

        mc "O cheiro da terra molhada... me lembra da fazenda... da minha infância..."

        mc "Eu adorava ficar olhando a chuva cair... era tão relaxante..."

    elif chuva_fala == 2:

        mc "Que saco... essa chuva vai estragar meu cabelo."

    elif chuva_fala == 3:

        mc "A chuva sempre me deixa com um sentimento de nostalgia..."

    elif chuva_fala == 4:

        mc "Eu me lembro de um dia chuvoso... eu era criança... e algo aconteceu..."

        mc "Eu não consigo me lembrar... mas eu sinto que foi algo importante..."

    elif chuva_fala == 5:

        mc "Acho que vou ter que ficar em casa hoje... não dá pra sair com essa chuva."

        mc "Que bom que eu já comprei tudo o que eu precisava no mercado."

    elif chuva_fala == 6:

        mc "A chuva... ela mexe com as minhas emoções..."

        mc "Eu me sinto... vulnerável... quando chove... Mas também me sinto... protegida..."

    elif chuva_fala == 7:

        mc "Será que o Gabriel tá em casa? Podia chamar ele pra cá..."

    elif chuva_fala == 8:

        mc "Tô com preguiça de fazer qualquer coisa... acho que vou só ficar deitada vendo série."

    elif chuva_fala == 9:

        mc "A chuva... ela me faz querer ficar em casa... aconchegada..."

        mc "Mas também me faz querer... sair... me aventurar..."

    elif chuva_fala == 10:

        mc "Acho que vou aproveitar pra estudar... pelo menos a chuva ajuda a me concentrar."

    elif chuva_fala == 11:

        mc "A chuva... ela é como um enigma... Ela me faz questionar... tudo..."

    elif chuva_fala == 12:

        mc "Será que o Jasper tá no bar? Deve tá vazio com essa chuva..."

    elif chuva_fala == 13:

        mc "Eu me sinto... perdida... quando chove... Mas também me sinto... encontrada..."

        if fado:

            f "Qual é o lance dessa garota com a chuva, hein?"

    elif chuva_fala == 14:

        mc "Que vontade de comer pizza... mas não dá pra pedir delivery com essa chuva..."

    elif chuva_fala == 15:

        mc "A chuva... ela me faz querer chorar... Mas também me faz querer... sorrir..."

    elif chuva_fala == 16:

        mc "Espero que a Akemi esteja bem... ela mora longe..."

    elif chuva_fala == 17:

        mc "A chuva... ela é como uma metáfora da vida..."

        mc "Ela é imprevisível... e caótica... Mas também é... linda... e necessária..."

    elif chuva_fala == 18:

        mc "Tô com saudades da minha mãe... será que eu ligo pra ela?"

    elif chuva_fala == 19:

        mc "Será que o Nathan tá na boutique hoje? Com essa chuva..."

    elif chuva_fala == 20:

        mc "Chuva..."

        if fado:

            f "Esse sentimento... esse vazio... qual foi, hein, garota?!"
    else:


        $ chuva_fala = -1

    $ chuva_fala += 1

    return

label daily:







    $ rand = 0
    $ rand1 = 0
    $ rand2 = 0
    $ rand3 = 0
    $ rand4 = 0

    $ gabriel_falou = False
    $ toalha = False
    $ porta_daily = False
    $ estudou = False
    $ trabalhou = False
    $ tv_check = False
    $ celular_check = False
    $ fernando_recusou = False



    $ rand = random.randint(1,100)
    $ rand1 = random.randint(1,100)
    $ rand2 = random.randint(1,100)
    $ rand3 = random.randint(1,100)
    $ rand4 = random.randint(1,100)

    if rand1 <= 60:

        $ caixa_escolhida = 1

    elif rand1 > 60 and rand1 <= 90:

        $ caixa_escolhida = 2

    elif rand1 > 90 and rand1 <= 100:

        $ caixa_escolhida = 3

    return

label define_dia_semana:

    if semana == 1:

        $ semana_dia = "segunda"

    elif semana == 2:

        $ semana_dia = "terça"

    elif semana == 3:

        $ semana_dia = "quarta"

    elif semana == 4:

        $ semana_dia = "quinta"

    elif semana == 5:

        $ semana_dia = "sexta"

    elif semana == 6:

        $ semana_dia = "sábado"

    elif semana == 7:

        $ semana_dia = "domingo"

    elif semana == 8:

        $ semana_dia = "segunda"

    if dia > 30:

        $ dia = 1
        $ mes += 1

    if mes > 12:

        $ mes = 1
        $ ano += 1

    return

label dormir_evento:

    "{cps=4}zZzZzZz{/cps}{nw}"

    pause 1.0

    return

label masturbacao_cena:

    if rand1 < 20 and gabriel_beijo >= 21 and masturbacao_gabriel >= 3:

        $ masturbacao_gabriel = 4

        show gabriel6 with Dissolve(1.0)

        "O gostoso do Gab puxou minha roupa! E meteu aquele mãozão na minha bunda."

        if namorando:

            "Namorado delícia que é só meu..."

        mc "Aiin..."

        "Eu faço o que ele quiser pra deixar ele duro! Porque me deixa toda molhada!"

        "Ele vem esfregando aquele pau duro dele em mim!"

        mc "Nnnghhh... afff..."

        "Eu fico querendo que ele tire tudo, que ele arranque minha roupa e faça eu ser a safada dele!"

        mc "Pensar assim é tão quente!"

        hide gabriel6 with Dissolve(1.0)

    elif rand1 < 40 and gabriel_beijo >= 15 and masturbacao_gabriel >= 2:

        $ masturbacao_gabriel = 3

        show gabriel_beijo6 with Dissolve(1.0)

        mc "Aahhn..."

        "Ele me pegando de costas, chupando meu pescoço."

        "Cada dia ele me pegava mais forte... com aquele jeitinho dele... acabou fazendo tudo o que queria comigo."

        mc "Delícia..."

        "Fui virando uma... aah... não mão dele... e eu gostei. Gostei de cada momento."

        "Quero mais, quero sentir mais!"

        hide gabriel_beijo6 with Dissolve(1.0)

    elif rand1 < 60 and gabriel_beijo >= 4 and masturbacao_gabriel >= 1:

        $ masturbacao_gabriel = 2

        show gabriel_beijo3 with Dissolve(1.0)

        "Quando o Gabriel apertou minha bunda!"

        "Eu senti a mão nele pela minha roupa, aquele mãozão de homem... tão diferente da minha mãozinha..."

        "Imagina aquela mão... imagina ela me apertando sem nada... aqueles dedos..."

        mc "Ahh..."

        hide gabriel_beijo3 with Dissolve(1.0)

    elif rand1 < 80 and gabriel_beijo >= 3 and masturbacao_gabriel >= 0:

        $ masturbacao_gabriel = 1

        "O que eu fiz com o Gabriel..."

        show gabriel_beijo2 with Dissolve(1.0)

        "A gente começou com aqueles beijinhos... selinhos... aqui, ali..."

        "E daí logo... hmm..."

        "B-beijo de língua..."

        "Ele me segurou... me trouxe pra perto e meteu a língua na minha boca."

        "Começou a esfregar a língua dele na minha, me puxando pra boca dele..."

        mc "Ahh..."

        "Foi tão quente... eu quase fiquei sem ar..."

        hide gabriel_beijo2 with Dissolve(1.0)
    else:


        "Tanta coisa que eu tô fazendo aqui na cidade..."

        "Tantos homens dando em cima de mim... em casa... no trabalho..."

        "Todos eles me querem..."

        mc "Ahh..."

        "Por que eles me querem tanto? O que eles fariam pra me ter?"

        mc "Ai..."

        "Isso só tá me deixando mais quente, droga!"

    return

label minigame_trabalho:

    if trabalho_tutorial == 0:

        $ trabalho_tutorial = 1

        $ renpy.pause(delay=6, hard=True)

        $ dinheiro += 25

        play sound dinheiro

        d "Depois de atender os clientes, você recebe {b}C$ 25{/b} em gorjetas"

        mc "Ufa... até que não foi tão difícil. E eu ainda ganhei C$ 25 em gorjetas."

        "Não é muito, mas se eu trabalhar direitinho dois períodos por dia eu consigo pagar o aluguel e sobra."

        "Vai ser um pouco corrido, mas tô otimista!"

        if fado:

            f "As coisas não podem ser fáceis assim pra essa babaquinha."

        return

    elif trabalho_tutorial == 1:

        $ trabalho_tutorial = 2

        $ renpy.pause(delay=6, hard=True)

        $ dinheiro += 20

        play sound dinheiro

        if fado:

            d "Depois de atender os clientes, Melissa recebe {b}C$ 20{/b} em gorjetas"
        else:


            d "Depois de atender os clientes, você recebe {b}C$ 20{/b} em gorjetas"

        "Hmm... ganhei um pouquinho menos."

        "Não posso deixar meu ânimo cair!"

        "???" "Ei, garota!"

        "Ai! Aquela moça que o Jasper chama de Barbie."

        if fado:

            f "Aquela outra com roupa de puta de esquina?"

        "???" "Posso trocar uma ideia?"

        mc "C-claro."

        call passos

        scene black with dissolve

        scene akemi1 with Dissolve(1.0)

        pause 2.0

        "???" "Deu tudo certo no primeiro dia?"

        mc "Deu, sim!"

        "???" "Que bom! A gente vai ser amigas de trabalho, né?!"

        mc "Siimmmm!"

        "???" "Como é seu nome?"

        mc "Eu sou a [mc]."

        menu:
            "E como é seu nome, amiga?":


                pass
            "O Jasper te chama de Barbie... é seu apelido?":


                "???" "Isso é coisa dele. Só porque eu gosto de rosa."

                mc "Ah... haha... imaginei..."

        a "Akemi. Eu tô trabalhando aqui vai fazer um ano já. Comecei tipo com o Jasper."

        if fado:

            f "Quando eu recuperar minha forma humana, tu vai ver o que eu vou fazer contigo, garota."

            f "Magrinha desse jeito, vou te quebrar em duas."

        mc "Legal... hoje foi meu primeiro dia, né?"

        a "E vou te falar, amiga, você leva jeito pra coisa."

        mc "V-você acha?"

        a "Olha só pra você. Quem dera eu tivesse uma coxa dessas."

        mc "Por causa disso?"

        a "Claro que não. Seus peitos são pequenos, iguais os meus, mas olha essas pernas. E você é linda, claro, também."

        if fado:

            f "Elogia ela de volta, sem educação. A gente quer ela de olho em ti também."

        menu:
            "Brigada, [a]. Você também é muito linda.":


                call akemi

                a "Valeu, fofa. Mas não igual você. Olha só pra isso."

                mc "Ai, [a]..."
            "Eu fico com vergonha quando você fala assim.":


                call inocencia

                if fado:

                    f "Odeio quando meu poder falha..."

                a "Por quê?"

                mc "Ficar falando assim do jeito que a outra parece. É meio íntimo demais."

        a "Para com isso! Sua beleza também faz parte de você, fofa."

        a "Você vai ter que aprender isso cedo ou tarde. Ainda mais aqui no café."

        mc "Então realmente os clientes..."

        a "Sim... alguns são bem safadinhos. Mas eles costumam respeitar. Eles vão testar até onde você vai."

        a "E, claro, se você deixar uma coisa aqui e outra ali, eles vão te dar uma graninha."

        if fado:

            f "Já pensou, garota? O tanto que você pode ganhar com esse rabão?"

            f "Não é interessante pra caralho?! Você é viciada em dinheiro..."

        label akemi_menu1:

            pass

        menu:
            "Gostei... de quanto dinheiro você tá falando?":


                if sexualidade < 5:

                    "Que tipo de pensamentos eu tô tendo ultimamente? N-não é certo falar uma coisa dessas!"

                    d "Você não tem Influência de Escorpião (Sexualidade) suficiente para tomar esta decisão."

                    jump akemi_menu1

                call sexualidade

                a "Tô vendo um novo brilho nos seus olhos."

                mc "É que eu realmente preciso da grana. Não ligo se uns pervertidos forem dar uma olhadinha."

                a "Assim que se fala, garota."

                call akemi
            "E-eu não vou querer nada disso!":


                call inocencia

                a "Tem certeza? Você sabe que você vai ganhar por gorjeta, né?"

                mc "Eu sei, mas já falei pro Jasper que se eu não ganhar o suficiente eu tô fora."

                a "Hmm... difícil..."

        a "Eu quase nunca tive problema com um tarado de verdade, sabe? Que realmente tentou me pegar à força."

        mc "Q-quase nunca?"

        a "Quase todo mundo é super de boa. Eles só vão tentar algo se você deixar. Pode ficar tranquila."

        mc "Isso é bom."

        a "Agora, eu acho bom você deixar uma coisa ou outra. No seu tempo, né?"

        a "Você é tão maravilhosa. Só imagino quanta grana eu não ia ganhar se eu fosse perfeita igual você."

        if fado:

            f "Ela tá na tua praticamente... agora é só ser fofinha."

            f "SEJA FOFA, IDIOTA!"

        label akemi_menu2:

            pass

        menu:
            "Para de me elogiar assim, que eu apaixono...":


                if sexualidade < 5:

                    "C-como que eu vou responder isso pra ela? N-não tem como!"

                    d "Você não tem Influência de Escorpião (Sexualidade) suficiente para tomar esta decisão."

                    jump akemi_menu2

                call akemi

                a "Você é muito fofa, [mc]. Eu acho que a gente vai se dar bem, né?"

                mc "Eu também acho..."
            "Ok, ok... entendi.":


                if fado:

                    f "EU DISSE FOFA, IDIOTA!"

                a "D-desculpa. Não queria parecer uma estranha."

                mc "N-não é isso. Eu só... não tô acostumada a ser elogiada assim."

        a "Espero que você continue. Ia ser muito bacana ter uma amiga aqui."

        a "O Jasper pode ter aquele jeito dele, mas ele ama isso aqui. E ele protege a gente também."

        a "Então tomara que você acostume e ganhe o dinheirinho que você tá precisando."

        menu:
            "Brigada, Akemi. Você é muito fofa. A gente se fala.":


                pass

        a "Até mais!"

        mc "Até!"

        if fado:

            f "Logo logo a gente se vê de novo Akemi..."

            a "Hm?"

        return

    elif trabalho_tutorial == 2:

        $ trabalho_tutorial = 3

        $ renpy.pause(delay=6, hard=True)

        $ dinheiro += 15

        play sound dinheiro

        if fado:

            d "Depois de atender os clientes, Melissa recebe {b}C$ 15{/b} em gorjetas"
        else:


            d "Depois de atender os clientes, você recebe {b}C$ 15{/b} em gorjetas"

        "Hm? Neste turno ganhei C$ 15... um pouco menos... devo tá com azar com os clientes..."

        "Na próxima eu consigo mais! Preciso de pelo menos aquelas C$ 25 pra isso funcionar!"

        if fado:

            f "Você não tá usando seus melhores dotes, maninha."

            f "Os homens não tão nem aí pro seu trabalho. Eles querem trabalhar você."

            f "Enquanto você não entender isso, tu tá fodida."

        return

    elif trabalho_tutorial == 3:

        $ trabalho_tutorial = 4

        $ renpy.pause(delay=6, hard=True)

        if fado:

            d "Depois de atender os clientes, Melissa não recebe nenhuma gorjeta"
        else:


            d "Depois de atender os clientes, você não recebe nenhuma gorjeta"

        mc "C-como? Nenhuma?"

        if fado:

            f "Não falei? Tu não entendeu pra que você existe ainda, guria."

        a "[mc]?"

        mc "O-oi!"

        a "Que carinha de triste é essa, fofa?"

        if fado:

            f "Eba! Outra chance..."

        mc "Ai, [a]... posso falar com você?"

        a "Claro. Cola aqui, bestie."

        call passos

        scene black with dissolve

        scene akemi2 with Dissolve(1.0)

        pause 2.0

        a "Que que deu aí?"

        menu:
            "Não ganhei gorjeta... elas tavam caindo, e agora caiu pra zero!":


                pass

        a "Calma, calma... isso é normal."

        mc "Será que eu sou feia demais? Os clientes não tão gostando de mim..."

        if fado:

            f "Você não é feia. Só é normal demais. Mas se for putinha, eles vão gostar."

            f "Só que você não entende!"

        a "Para de falar besteira, fofa. Você é linda demais, entendeu?"

        mc "Mas..."

        a "Isso aconteceu comigo também. E mais rápido do que você."

        if fado:

            f "Você quer a confirmação não quer? Pergunta se ela te acha bonita... ela vai gostar."

            f "Tô vendo nos olhos dela que ela quer ser sua veterana..."

        menu:
            "Você realmente acha que eu sou bonita?":


                "Eu tô me achando tão feia agora, eu quero que ela me fale que eu sou bonita."

                a "Por que eu vou mentir pra você?!"

                a "Seu rosto é lindo, você é magrinha, com um quadril que deixa qualquer homem louco! E até umas minas, viu..."

                call akemi

                mc "Brigada, miga. Tô tão pra baixo hoje, sabe?"

                a "A gente fica assim às vezes."
            "O que aconteceu com você?":


                pass

        a "Você até que ganhou. Eu nem isso. Só depois que eu comecei a xavecar os clientes que comecei ganhar uma coisinha aqui e ali."

        mc "Verdade? Eu até ganhei, mas parou."

        a "Então... no começo tu é novidade, né? Mas eles vão se acostumando..."

        mc "O que eu faço então?"

        a "Eu vou te ensinar como funciona, bestie. Tem dois jeitos."

        mc "Brigada!"

        "A Akemi é tão legal! É tão legal ter uma amiga!"

        a "Quero saber se você tá pronta pra xavecar os clientes."

        mc "Q-quê?!"

        a "É. Talvez mostrar um pouco da coxa, ou do decote, ou falar com eles assim, sabe?"

        if fado:

            f "Imagina esses babacas caindo aos seus pés... e você caindo na pica deles."

            f "É uma relação boa, não é? Você gosta de como isso soa aos seus ouvidos..."

        label akemi_menu3:

            pass

        menu:
            "Hmm... só mostrando um pouquinho eles já caem?":


                if sexualidade < 10:

                    "Eu queria poder aceitar isso... mas não tem como! Eu tenho muita vergonha só de pensar!"

                    d "Você não tem Influência de Escorpião (Sexualidade) suficiente para tomar esta decisão."

                    jump akemi_menu3
                else:


                    d "Você conquistou Sexualidade suficiente para tomar esta decisão."

                call sexualidade

                a "Com certeza! Esses rapazes são tudo meio gado hehe..."

                if fado:

                    f "Ei... não precisa falar assim também. Só queremos usar vocês."

                mc "Tadinhos deles, Akemi... mas se é fácil assim, por que não?"

                if fado:

                    f "Quem você pensa que é pra ter PIEDADE dos homens? Você não passa de um pedaço de carne."

                a "Assim que eu gosto de ouvir. Precisa ter coragem pra isso, fofa."

                mc "É, né?"

                call coragem

                a "Eu acho. Tem que ter coragem e confiar no seus dotes."

                mc "Hehe... não sei se eu confio, mas tô tentando. Quero me abrir pra várias oportunidades."

                call akemi

                a "Isso aí."

                mc "S-sim..."

                a "Hmm... não tô sentindo muita confiança."

                mc "É que... é uma coisa muito nova pra mim, sabe?"

                a "Você quer, mas talvez seja cedo pra você... A gente não quer coloar tudo a perder."

                mc "Então não vai dar?"



                mc "Tá bom."
            "Eu gostaria... m-mas isso não é certo, é?":


                call sexualidade

                a "Você tá ganhando seu dinheiro. A gente tem que sobreviver, né?"

                mc "Bom... isso é verdade..."

                mc "Eu até queria... mas não sou desinibida suficiente pra isso."

                a "Não tem problema."
            "De jeito nenhum! Eu consigo ganhar sem fazer isso!":


                call coragem

                a "Calma! Não precisa se desesperar."

                if fado:

                    f "Idiota..."

                mc "Não é desespero. Eu só não quero, tudo bem?"

                a "Tudo..."

        a "Eu tenho um jeito aqui que vai ser o melhor pra você agora."

        mc "Sério?"

        a "Vou te ensinar como atender um monte de mesa sem cair e quebrar tudo."

        if fado:

            f "Sério? Que você podia ensinar sacanagem pra ela e vai ensinar trabalho duro? A gente quer ela dando pro duro, não dando duro!"

        mc "E-eita..."

        a "Vai ser o jeito, mulher. Correr pra lá e pra cá. Quanto mais gente você atender, maior a chance de ganhar gorjeta."

        menu:
            "Entendi! Eu vou correr e me esforçar bastante!":


                pass

        a "Você é mais esforçada que eu. Eu preferia só deixar eles pegarem em mim..."

        mc "[a]... haha..."

        a "Vamos lá. Presta atenção."

        a "Começa olhando bem pra isto aqui. Dá uma olhada com calma. Quando terminar, a gente continua."

        show tutorial_trabalho with dissolve

        pause

        if fado:

            f "Vai começar o blá blá blá..."

        a "Toda vez que você apertar no botão ACELERAR, você vai ser mais rápida e a barrinha da direita vai subir."

        a "Se você apertar rápido demais a barra fica vermelha e pode acabar quebrando as coisas ou cair. Toma cuidado!"

        a "Se você apertar muito devagar, a barra também fica vermelha. Ser cuidadosa demais pode desagradar os clientes."

        a "Se você tiver indo rápida demais ou cuidadosa demais a barrinha vai ficar vermelha."

        menu:
            "Então tenho que apertar em ACELERAR e controlar a barrinha pra ela ficar verde.":


                pass

        a "É isso mesmo!"

        a "Aperte no botão ACELERAR e deixe a barra sempre verde."

        menu:
            "Posso ver a imagem de novo?":


                if fado:

                    f "Que idiota..."

                a "Claro!"

                window hide

                pause
            "Entendi. Tô pronta!":


                pass

        mc "Agora tô pronta."

        hide tutorial_trabalho with dissolve

        a "Então na próxima você começa a meter o louco, fofa!"

        if fado:

            f "É impressão minha ou ela falou como se fosse o tutorial de um jogo, mas no meio da história?"

            f "Esse desenvolvedor tá cada vez mais preguiçoso."

            play sound soco

            f "Ei! Que foi isso?!"

        a "Nem sempre dá pra fazer isso, é mais quando o bar tá nas horas de pico. Então fica de olho."

        menu:
            "Pode deixar! Eu vou ser a melhor garçonete do mundo!":


                a "Assim que se fala!"
            "Brigada mesmo. Sem você eu tava ferrada.":


                a "Para de falar besteira... você é muito mais bonita e inteligente que eu."

                mc "Você tem muito mais valor do que você se dá crédito, boba."

                call akemi

                a "Eu que vou apaixonar assim..."

                mc "C-calma lá..."

                a "Já tá ficando vermelha."

                mc "Poxa..."

        a "A gente se vê depois? Quero saber como você tá se saindo."

        mc "Combinado! Beijo!"

        a "Beijo!"

        if fado:

            f "Essas duas... eu tenho que fazer elas serem mais que amiguinhas..."

            f "Pensei que essa Akemi tinha jeito de conquistadora, mas é outra 'fofinha'."

            f "Mulheres... se eu deixar na mão delas nada vai dar certo."

        return

    elif trabalho_tutorial == 4:

        $ trabalho_tutorial = 5

        $ trabalho_vez = 12

        "Hoje eu vou começar a me esforçar do jeito que a [a] me ensinou."

        "Tenho que controlar perfeitamente velocidade e cuidado. Nem tão rápida, nem tão devagar."

        t "Mantenha a barra da direita sempre verde apertando no botão ACELERAR. Boa sorte!"

        if fado:

            f "Agora é o Tutorial que tá falando. Então por que não usou Tutorial aquela hora?"

            play sound soco

            f "AI! Já entendi!"

    elif trabalho_tutorial == 5:

        $ trabalho_tutorial += 1

    elif trabalho_tutorial == 6:

        $ trabalho_tutorial += 1

    elif trabalho_tutorial == 7:

        $ trabalho_tutorial += 1

    $ folego = 150

    if trabalho_vez == 0:

        $ menos_folego = 2
        $ esteira_velo = 0.1
        $ mc_folego = 25
        $ velo_horizontal = 2

    elif trabalho_vez == 1:

        $ menos_folego = 1.5
        $ esteira_velo = 0.05
        $ mc_folego = 25
        $ velo_horizontal = 5

    elif trabalho_vez == 2:

        $ menos_folego = 3
        $ esteira_velo = 0.05
        $ mc_folego = 20
        $ velo_horizontal = 3

    elif trabalho_vez == 3:

        $ menos_folego = 4
        $ esteira_velo = 0.05
        $ mc_folego = 20
        $ velo_horizontal = 10

    elif trabalho_vez == 4:

        $ menos_folego = 2
        $ esteira_velo = 0.05
        $ mc_folego = 30
        $ velo_horizontal = 15

    elif trabalho_vez == 5:

        $ menos_folego = 5
        $ esteira_velo = 0.04
        $ mc_folego = 35
        $ velo_horizontal = 20

    elif trabalho_vez == 6:

        $ menos_folego = 1
        $ esteira_velo = 0.04
        $ mc_folego = 30
        $ velo_horizontal = 21

    elif trabalho_vez == 7:

        $ menos_folego = 5
        $ esteira_velo = 0.03
        $ mc_folego = 50
        $ velo_horizontal = 23

    elif trabalho_vez == 8:

        $ menos_folego = 3
        $ esteira_velo = 0.05
        $ mc_folego = 25
        $ velo_horizontal = 24

    elif trabalho_vez == 9:

        $ menos_folego = 4
        $ esteira_velo = 0.08
        $ mc_folego = 30
        $ velo_horizontal = 22

    elif trabalho_vez == 10:

        $ menos_folego = 1
        $ esteira_velo = 0.06
        $ mc_folego = 35
        $ velo_horizontal = 15

    elif trabalho_vez == 11:

        $ menos_folego = 2
        $ esteira_velo = 0.07
        $ mc_folego = 35
        $ velo_horizontal = 25

    elif trabalho_vez == 12:

        $ menos_folego = 10
        $ esteira_velo = 0.5
        $ mc_folego = 30
        $ velo_horizontal = 7

    elif trabalho_vez == 13:

        $ menos_folego = 12
        $ esteira_velo = 0.7
        $ mc_folego = 70
        $ velo_horizontal = 5

    elif trabalho_vez == 14:

        $ menos_folego = 15
        $ esteira_velo = 0.4
        $ mc_folego = 95
        $ velo_horizontal = 3

    elif trabalho_vez == 15:

        $ menos_folego = 17

        $ esteira_velo = 0.6
        $ mc_folego = 90
        $ velo_horizontal = 4

    $ esteira_tempo = 30 - trabalho_nivel

    if esteira_tempo < 10:

        $ esteira_tempo = 10

    $ trabalho_vez += 1

    if trabalho_vez > 15:

        $ trabalho_vez = 0

    show screen academia_esteira
    show screen esteira_tempo
    show screen esteira_reduz_folego
    call screen esteira_base

    pause

screen academia_esteira():
    tag academia

    modal True



    imagebutton auto "botao_conversar_%s.webp" at anda_horizontal:
        yalign 0.99
        xanchor 0.5
        action Jump("esteira_aumenta_folego")



    vbox:

        spacing 10
        xalign 0.9
        yalign 0.224

        text "Rápida":
            xalign 0.5
            text_align 0.5

        bar:
            bar_vertical True
            xalign 0.5
            xsize 40
            ysize 250
            value folego

            if folego >= 240 or folego <= 60:

                left_bar "#ff6d6d"
                right_bar "#ff2424"

            else:

                left_bar "#688635"
                right_bar "#AED768"

            range 300

        text "Cuidadosa":
            xalign 0.5
            text_align 0.5

    vbox:

        spacing 10
        xalign 0.1
        yalign 0.55

        text "Satisfação dos Clientes"

        bar:
            xsize 350
            ysize 30
            value AnimatedValue(old_value=0.0, value=1.0, range=1.0, delay=esteira_tempo)

screen esteira_reduz_folego():
    tag esteira_folego


    timer esteira_velo repeat True action Jump("esteira_reduz_folego")

screen esteira_tempo():
    tag esteira_tempo


    timer esteira_tempo action Jump("termina_esteira")

screen esteira_base():
    tag esteira_base


label esteira_aumenta_folego:

    $ folego += mc_folego

    if folego >= 300:

        jump termina_esteira

    pause

label esteira_reduz_folego:

    $ folego -= menos_folego

    if folego <= 0:

        jump termina_esteira

    pause

label termina_esteira:

    hide screen academia_esteira
    hide screen esteira_tempo
    hide screen esteira_reduz_folego
    hide screen esteira_base



    call trabalho

    if folego <= 0:

        play sound soco

        "Homem" "Que demora!"

        scene trabalho2 with hpunch

        mc "Ai! Eu já tô indo!"

        "Mulher" "A gente entende, fofa, mas demorou demais nosso pedido."

        $ dinheiro += 10

        play sound dinheiro

        d "Você termina o turno sem quebrar nada, mas recebe reclamações por demorar demais, terminando com C$ 10 em gorjetas."

        "Saco... preciso ser mais rápida se eu quiser atender todo mundo à tempo."

        t "Para não receber reclamações, aperte o botão ACELERAR mais rápido para a barra não esvaziar. Mantenha a barra sempre na zona verde."

    elif folego >= 300:

        play sound derrubou

        scene trabalho2 with hpunch

        mc "Ai!"

        "Mulher" "Você quebrou tudo!"

        mc "E-eu corri demais! P-perdão!"

        "Homem" "Só limpe isso aqui por favor."

        $ dinheiro += 10

        play sound dinheiro

        d "Você termina o turno com algumas gorjetas, mas precisa pagar o que quebrou, terminando com C$ 10."

        "Droga. Tenho que tomar cuidado pra não me apressar demais."

        t "Para não quebrar tudo, não aperte demais o botão ACELERAR. Mantenha a barra sempre na zona verde."
    else:


        if dinheiro < dinheiro_max:

            if recusou_trabalho_quente:

                $ dinheiro += 20

                play sound dinheiro

                if fado:

                    d "Melissa perde alguns clientes, mas mesmo assim consegue receber {b}C$ 20{/b} em gorjetas."
                else:


                    d "Você perde alguns clientes, mas mesmo assim consegue receber {b}C$ 20{/b} em gorjetas."

                "Perdi um pouco, mas é melhor que trabalhar com o vestido todo desajustado. Tô tranquila."
            else:


                $ dinheiro += 25

                play sound dinheiro

                if fado:

                    d "Melissa é perfeita atendendo no horário de pico e recebe {b}C$ 25{/b} em gorjetas."
                else:


                    d "Você é perfeita atendendo no horário de pico e recebe {b}C$ 25{/b} em gorjetas."
        else:


            t "Não é possível acumular mais de C$ [dinheiro_max] nesta atualização."

    return

label foto:

    play sound foto

    show white with Dissolve(0.2)

    hide white with Dissolve(0.2)

    return



label pre_tela:

    hide screen navegar with Dissolve(0.3)

    call passos

    scene black with dissolve

    return

label pos_tela:



    if tempo >= 4:

        "Que soninho... Melhor eu deitar se não amanhã eu não levanto."

        jump cama

    show screen navegar with Dissolve(0.3)

    pause

label save_game:

    $ renpy.save("None-continue", extra_info="None-continue")

    return

label checa_logado:

    python:
        if renpy.android:
            userlogado = PythonSDLActivity.pegaLogado();

    if not userlogado:

        t "Você precisa estar conectado à internet e logado em sua conta para continuar"

        t "Conecte-se agora e vamos tentar fazer login em sua conta"

        python:
            if renpy.android:
                PythonSDLActivity.abreLogin()

        t "Autenticando..."

        python:
            if renpy.android:
                userlogado = PythonSDLActivity.pegaLogado();
                email = PythonSDLActivity.pegaEmail()

        if userlogado:

            t "Você logou em sua conta com sucesso."

            t "Você está logado com o e-mail [email]. Não se esqueça de usar ele quando for fazer compras no game."
        else:


            "Não foi possível se conectar à sua conta. Tente novamente mais tarde"

    return

label checa_tempo:

    python:
        if renpy.android:
            PythonSDLActivity.pegaTempo()

    $ renpy.pause(delay=2, hard=True)

    python:
        if renpy.android:
            checatempo = PythonSDLActivity.checaTempo()

    $ renpy.pause(delay=1, hard=True)

    if not checatempo:

        $ renpy.notify("Conectando...")

        python:
            if renpy.android:
                PythonSDLActivity.pegaTempo()

        $ renpy.pause(delay=2, hard=True)

        python:
            if renpy.android:
                checatempo = PythonSDLActivity.checaTempo()

        $ renpy.pause(delay=2, hard=True)

        if not checatempo:

            $ renpy.notify("Tentando conexão...")

            python:
                if renpy.android:
                    PythonSDLActivity.pegaTempo()

            $ renpy.pause(delay=2, hard=True)

            python:
                if renpy.android:
                    checatempo = PythonSDLActivity.checaTempo()

            $ renpy.pause(delay=2, hard=True)

            if not checatempo:

                "{b}Sua conexão com o servidor está lenta. Tentando conectar novamente...{/b}"

                python:
                    if renpy.android:
                        PythonSDLActivity.pegaTempo()

                $ renpy.pause(delay=2, hard=True)

                python:
                    if renpy.android:
                        checatempo = PythonSDLActivity.checaTempo()

                $ renpy.pause(delay=2, hard=True)

                if not checatempo:

                    "{b}Não foi possível recuperar o horário do servidor.{/b}"

                    "{b}Confirme se você está conectado a internet e logado em sua conta e tente novamente em instantes.{/b}"

    return

label checa_compra:

    if renpy.variant("android"):
        $ bronze_banco = PythonSDLActivity.pegaCreditos()

    if bronze_banco > bronze_total:

        $ bronze_adicionar = bronze_banco - bronze_total

        $ bronze += bronze_adicionar
        $ bronze_total += bronze_adicionar

        $ base78 = True

        t "Atenção!"

        t "Um erro no sistema adicionou {b}[bronze_adicionar] bronzelythes{/b} em sua conta"

        $ renpy.save("None-continue", extra_info="None-continue")

    return

label recebe_compra:

    python:
        if renpy.android:
            PythonSDLActivity.carregaJogo()

    $ renpy.notify("Conectando...")

    $ renpy.pause(delay=3, hard=True)

    if renpy.variant("android"):
        $ moeda_banco = PythonSDLActivity.pegaCreditos()

    if moeda_banco > moeda_total:

        $ moeda_adicionar = moeda_banco - moeda_total

        $ moeda += moeda_adicionar
        $ moeda_total += moeda_adicionar

        $ p1341 = True

        scene black with dissolve

        scene fado3 with Dissolve(1.0)

        f "Aqui está, belezinha."

        $ renpy.save("None-continue", extra_info="None-continue")

        play sound magia

        d "Uau! Você recebeu [moeda_adicionar] Moedas de Ouro! Dá para fazer muita coisa com isso!"

        f "Você pode conquistar o mundo muito mais rápido agora, [mc]."

        f "Só toma cuidado não viciar, guria... hehehe..."
    else:


        f "Hmm... pelo que eu vi aqui... você ainda não tem nenhuma Moeda para receber."







        t "Quase todas as vezes que isso acontece, é porque seu pagamento não foi aprovado. Confirme no extrato do seu banco."

        t "Também pode ser problema na internet para se comunicar com sua conta na nuvem. Tente uma nova conexão."

        t "Espere alguns minutos e tente mais algumas vezes. Se passar mais de 1 hora e você não recebeu, entre em contato conosco."

        menu:
            "Acessar a página de Suporte":


                $ renpy.run(OpenURL('https://www.geiko.net/suporte/'))

                t "O email para tirar dúvidas ou informar algum produto não recebido é {b}contato@geiko.net{/b}."

                t "Nosso suporte responderá seu email em até 24 horas. Repetindo: {b}contato@geiko.net{/b}."

                t "Falar com outros jogadores no nosso grupo do Telegram e WhatsApp também pode ajudar."

                t "E, enquanto espera, você pode sempre jogar outros jogos da Geiko! Temos um total de 9 jogos adultos para você curtir!"

                f "Mas não se preocupe, porque se você pagou direitinho, essa galera é firmeza. Eles vão te dar tudo certo."
            "Ver o email para contato":


                t "O email para tirar dúvidas ou informar algum produto não recebido é {b}contato@geiko.net{/b}."

                t "Nosso suporte responderá seu email em até 24 horas. Repetindo: {b}contato@geiko.net{/b}."

                t "Falar com outros jogadores no nosso grupo do Telegram também pode ajudar."

                t "E, enquanto espera, você pode sempre jogar outros jogos da Geiko! Temos um total de 7 jogos adultos para você curtir!"

                f "Mas não se preocupe, porque se você pagou direitinho, essa galera é firmeza. Eles vão te dar tudo direitinho."
            "Eu não comprei nada hehe...":


                f "Fala sério, [mc]... para de xeretar todas as opções."

    return

label baixa_nuvem:

    $ persistent.banned = False

    if renpy.can_load("None-continue"):

        t "Você já tem um jogo iniciado neste aparelho."

        t "Você quer apagar ele para tentar baixar um jogo da nuvem? Cuidado excluir algo que não deve!"

        menu:
            "Sim. Excluir progresso":

                t "Vou excluir seu save agora."

                $ renpy.unlink_save("None-continue")

                t "Excluindo..."

                t "Pronto! Agora vamos tentar baixar seu jogo da nuvem. Qualquer problema, reinicie o processo."
            "Não excluir nada":

                t "Ok!"

                t "Enquanto você tiver um jogo iniciado em seu aparelho, não é possível baixar outro da nuvem."

                t "Quando quiser baixar o que salvou da nuvem, exclua o progresso que está salvo no aparelho."

    if not renpy.can_load("None-continue"):

        if renpy.variant("android"):

            $ userlogado = PythonSDLActivity.pegaLogado();

            if not userlogado:

                t "Você precisa ter feito login em uma conta para comprar Moedas de Ouro."

                t "É essencial você ter uma conta, para caso você compre algo, seu produto fique seguro na nuvem."

                menu:
                    "Fazer login":

                        call fazer_login

                        t "Muito bem."

        t "Agora vamos tentar baixar o jogo da nuvem. Fique de olho na mensagem que vai aparecer."

        if renpy.variant("android"):
            $ PythonSDLActivity.carregaHistoria();

        t "Estamos tentando baixar seu jogo da nuvem agora e vamos reiniciar o jogo para finalizar o processo"

    $ renpy.full_restart()

    return

label baixando_nuvem:

    $ persistent.apoiador = True
    $ persistent.banned = False

    return

label passos:

    $ randp = random.randint(1,3)

    if randp == 1:

        play sound passos1_1

    elif randp == 2:

        play sound passos1_2

    elif randp == 3:

        play sound passos1_3

    return

label menu_load:

    hide screen main_menu

    scene black

    menu:

        "{b}Continuar jogo{/b}" if renpy.can_load("None-continue"):

            t "Carregando jogo salvo atualmente"

            $ renpy.load("None-continue")
        "Carregar outros saves":


            menu:

                "Voltar ao início da semana" if renpy.can_load("None-semanal"):

                    t "Indo para o início da semana atual."

                    $ renpy.load("None-semanal")

                "Auto-save 1" if renpy.can_load("_reload-1"):

                    $ renpy.load("_reload-1")

                "Auto-save 2" if renpy.can_load("_reload-2"):

                    $ renpy.load("_reload-2")
                "Voltar":


                    pass

            jump menu_load
        "Voltar para o Menu Inicial":


            $ renpy.full_restart()



label login_convidado:

    return

label fazer_login:

    if renpy.variant("android"):

        python:
            if renpy.android:
                PythonSDLActivity.abreLogin()



    return

label ban_story:

    hide screen navegar
    hide screen menu_secundario

    scene black

    $ renpy.block_rollback()

    $ persistent.banned = False

    t "O sistema de banimentos foi desativado nesta versão. Seu acesso permanece liberado."

    return

label nao_apoiador:

    hide screen navegar
    hide screen menu_secundario

    scene black

    $ renpy.block_rollback()

    $ persistent.apoiador = True
    $ premium = False

    t "Esta versão pública não possui restrições de acesso. Bom jogo!"

    return

label gabriel_textos:






    "Cada movimento das suas mãos me leva mais perto do abismo do prazer... e eu estou ansiosa para cair de cabeça nele."







    "Eu sinto cada parte do meu corpo pulsando por você... eu só quero ser sua, quero ser fodida por você até não aguentar mais."

    "Eu não consigo pensar em mais nada além de você me tocando... suas mãos me levam a lugares que eu nem sabia que existiam."

    "Eu quero que você me faça gozar tão forte que eu esqueça o próprio nome... eu só quero me perder em você, em todo esse prazer que você me dá."

    "Porra, minha buceta está tão molhada que escorre pelo meu corpo... só de pensar nos seus dedos me fodendo, fico ainda mais excitada."

    "Me fode com esses dedos, Gabriel... quero sentir cada movimento dentro de mim, me fazendo gemer e implorar por mais."

    "Esses dedos... eles me enlouquecem, me deixam tão fodidamente molhada que mal consigo me conter."

    "Eu quero seus dedos dentro de mim, me fodendo até eu não aguentar mais, até eu gozar feito uma cadela no cio."

    "Me fode com esses dedos grossos, Gabriel... eu quero ser preenchida por você, quero sentir cada centímetro de prazer que você pode me dar."

    "Sua mão na minha buceta é como uma droga, Gabriel... eu não posso me controlar, eu só quero mais e mais."

    "Eu quero que você me faça gozar com esses dedos, Gabriel... eu preciso disso, preciso desse prazer que só você pode me dar."

    "Me masturba com força, me faz gozar feito uma vadia... eu quero me perder em você, me entregar completamente ao prazer."

    "Sua mão na minha buceta me deixa tão fodidamente excitada... eu mal posso esperar para sentir você me penetrando com esses dedos."

    "Eu só quero me perder em você, Gabriel... me fode com esses dedos até eu não aguentar mais, até eu gozar feito uma puta descontrolada."









    "Caramba, eu amo quando você me toca assim, Gabriel... é como se cada carícia fosse uma promessa do nosso amor eterno."



    "Sua mão na minha buceta é o lugar onde eu me sinto mais amada, mais desejada... é como se você estivesse me abraçando com todo o seu amor."

    "Eu amo quando você me masturba, Gabriel... é como se nossos corpos estivessem dançando uma dança de amor e luxúria."

    "Eu te amo tanto, Gabriel... e quando você me toca assim, parece que todo o resto do mundo desaparece, deixando apenas o nosso amor ardente."



















    g "E eu vou te foder, minha putinha, vou te foder até você implorar para eu parar. Vou te chupar inteira, te fazer sentir cada movimento da minha língua até você gritar de prazer."

    mc "Sim, me chupa... me chupa toda..."

    g "Você é tão deliciosa, Mel. Vou te chupar até você gozar na minha boca, e então vou te penetrar com força, te fazendo delirar de prazer."

    mc "Ahhh... eu quero isso, Gabriel... eu quero tudo o que você pode me dar..."

    g "Você vai ter tudo o que quer, minha vadia. Vou te fazer gozar tão forte que você vai ver estrelas. Vou te foder em todas as posições até você não aguentar mais."

    mc "Por favor, me fode... me fode até eu não conseguir andar..."

    g "Eu vou te foder como você nunca foi fodida antes, Mel. Vou te dar o melhor orgasmo da sua vida, e depois vou te foder de novo até você implorar por mais."

    mc "Eu te amo, Gabriel... só você pode me fazer sentir assim..."

    g "E eu te amo, Mel... vou te foder até você esquecer o próprio nome."

    mc "Melissa sente as mãos de Gabriel explorando suas coxas, cada toque enviando arrepios de desejo por todo o seu corpo. Ela fecha os olhos e se entrega ao prazer, ansiosa pelo que está por vir."

    g "Você gosta disso, não é? (ele murmura, enquanto seus dedos deslizam suavemente sobre sua pele, causando calafrios excitantes)"

    mc "Melissa geme baixinho, sua respiração ficando mais rápida conforme a excitação toma conta dela. Ela anseia pelo toque de Gabriel, pelo contato íntimo que ele lhe proporciona."

    g "Você é tão molhada pra mim, Mel. (ele sussurra com desejo, provocando-a ainda mais com suas palavras obscenas)"

    mc "Melissa sente o calor entre as suas pernas aumentar, sua intimidade pulsando de desejo pelo toque habilidoso de Gabriel. Ela mal pode esperar para ser tomada por ele, para se entregar completamente ao prazer que ele oferece."

    g "Isso mesmo, querida. Deixe-me te levar ao limite. (ele murmura enquanto a masturba com habilidade, provocando mais gemidos dela)"

    mc "Melissa se perde nas sensações, entregando-se ao prazer que Gabriel lhe proporciona. Ela está completamente submersa na luxúria, desejando mais do que nunca sentir-se preenchida por ele, tanto física quanto emocionalmente."

    g "Isso, minha putinha, você gosta assim, não é? (ele grunhe, intensificando seus movimentos, seu tom agora mais rude e dominante)"

    mc "Sim, me fode, Gabriel! Eu preciso disso!"

    g "Você é tão apertada... tão quente... (ele geme, seus dedos explorando cada vez mais fundo)"

    mc "Ahhh... mais rápido, mais forte!"

    g "Você é uma vadia insaciável, Mel. (ele diz, sua voz rouca de luxúria, enquanto a penetra com vigor)"

    mc "Sim, sim... me faça gozar, Gabriel! Por favor!"

    g "Você vai gozar pra mim, sua safada. (ele grunhe, aumentando o ritmo até ela alcançar o ápice do prazer)"

    mc "Ahhh... Gabriel! Eu estou... eu estou... (ela explode em êxtase, suas palavras interrompidas por gemidos de puro prazer)"

    g "Isso mesmo, goza pra mim, minha vadia. (ele murmura, continuando a estimulá-la até que as ondas de prazer a consumam completamente)"

    mc "Eu te amo tanto... (ela diz, ofegante, enquanto se recupera do orgasmo, seu amor misturado com o desejo que ele desperta nela)"

    g "E eu te amo, Mel. Mais do que qualquer coisa neste mundo. (ele responde, seus olhos brilhando com amor e luxúria)"









    g "Isso mesmo, querida. Deixe-me te levar ao limite. (ele sussurra enquanto a masturba com habilidade, provocando mais gemidos dela)"

    mc "Eu te amo tanto... (ela diz entre gemidos, enquanto se entrega completamente ao prazer que ele lhe proporciona)"

    g "E eu te amo, Mel. Mais do que qualquer coisa. (ele murmura enquanto a leva ao clímax, compartilhando um momento de intenso desejo e paixão)"






    mc "Gabriel, amor da minha vida, que felicidade te encontrar aqui! Estava contando os minutos para esse momento."



    mc "Oi, meu amor! Que bom te ver! Estava sentindo falta do seu sorriso e do seu abraço."

    mc "Oi, meu príncipe encantado! Como foi seu dia? Mal posso esperar para curtir a noite com você."

    mc "Boa noite, meu crush! Estava contando os segundos para te ver e te dar um abraço bem apertado."

    mc "Oi, meu amorzinho! Que bom te encontrar aqui! Mal posso esperar para aproveitar cada segundo ao seu lado."

    mc "E aí, meu bem! Boa noite! Estava morrendo de vontade de te dar um beijo bem apaixonado."





    mc "E aí, meu amor! Que bom te ver! Estava tão empolgada para vir aqui e te encher de carinho."



    mc "Boa noite, meu amor! ."

    " Estava contando os minutos para te dar um beijo bem apaixonado."

    mc "Oi, meu príncipe! Como foi seu dia? Estava morrendo de vontade de estar aqui, curtindo cada segundo com você."









    g "Oi, meu bem! Boa noite! Estava contando os minutos para te ver e sentir seu abraço gostoso."



    g "Oi, minha musa inspiradora! Boa noite! e carinhos."

    g "Boa noite, meu anjo! Só de te ver, meu coração já está batendo mais forte. Você é minha perdição."



    g "Oi, meu amor! Boa noite! "



    g "E aí, minha paixão! Boa noite! Só de estar perto de você, já sinto um calor gostoso aqui dentro."



    g "Boa noite, meu amorzinho! Você chegou e transformou minha noite em um sonho, sabia?"

    g "E aí, minha tentadora! Boa noite! Aposto que você veio aqui só para me deixar louco de desejo."

    g "Oi, minha inspiração! Boa noite! Mal posso esperar para te dar todos os beijos que você merece."

    g "Boa noite, minha musa! Só de olhar para você, já me perco nos seus encantos."

    g "E aí, meu vício! Boa noite! Aposto que você veio aqui só para me deixar completamente apaixonado."

    g "Oi, minha rainha! Boa noite! Só de estar perto de você, já me sinto o homem mais sortudo do mundo."

    g "Boa noite, minha princesa! Você chegou e trouxe toda a doçura e ternura do mundo com você."

    g "E aí, minha deusa! Boa noite! Aposto que você veio aqui só para me deixar completamente sem rumo."

    g "Oi, minha inspiração! Boa noite! Mal posso esperar para te encher de carinho e te fazer sentir especial."

    g "Boa noite, meu amorzinho! Você chegou e trouxe consigo todo o brilho das estrelas, sabia?"










    mc "Gabriel, eu simplesmente adoro estar aqui com você, nos braços um do outro, é tão reconfortante."

    mc "É incrível como seu abraço me faz sentir amada e protegida, Gabriel. Não há lugar onde eu prefira estar agora."

    mc "Estou tão feliz por estarmos juntos, Gabriel. Você é tudo para mim, meu porto seguro neste mundo louco."

    mc "É tão bom estar aqui com você, Gabriel, apenas curtindo esse momento juntos, sem preocupações."

    mc "Você é tão gentil e carinhoso comigo, Gabriel. Me sinto tão sortuda por ter você ao meu lado."

    mc "Às vezes, me pego pensando em como é incrível termos nos encontrado, Gabriel. É como se fôssemos feitos um para o outro."

    mc "Gosto tanto de você, Gabriel. Cada momento ao seu lado é uma lembrança preciosa para mim."

    mc "Sabe, Gabriel, quando estou com você, sinto como se nada mais importasse. É só você e eu, e isso é o suficiente para mim."

    mc "Você me faz tão feliz, Gabriel. Só queria que você soubesse o quanto te amo."

    mc "Acho que nunca me senti tão completa como me sinto agora, ao seu lado, Gabriel. Você é minha outra metade."

    mc "Às vezes, me pego admirando você, Gabriel. Você é tão incrível, tão especial para mim."

    mc "Obrigada por ser tão maravilhoso comigo, Gabriel. Você me faz sentir especial todos os dias."

    mc "Estou tão grata por ter você na minha vida, Gabriel. Você é meu melhor amigo, meu companheiro, meu amor."

    mc "Quero que saiba o quanto te admiro, Gabriel. Você é tão forte, tão gentil, tão incrível em tudo o que faz."

    mc "Estou tão feliz por termos construído essa história juntos, Gabriel. Mal posso esperar para ver o que o futuro nos reserva."

    mc "Às vezes, me pego pensando em como seria minha vida sem você, Gabriel. E não consigo imaginar, porque você é tudo para mim."

    mc "Você me faz querer ser uma pessoa melhor, Gabriel. Obrigada por estar sempre ao meu lado, me apoiando e me amando."

    mc "Adoro quando você sorri para mim, Gabriel. É como se o mundo inteiro desaparecesse e fosse só nós dois."

    mc "Nada no mundo se compara ao amor que sinto por você, Gabriel. É o mais belo sentimento que já conheci."

    mc "Só queria te dizer o quanto te amo, Gabriel. Você é o melhor presente que a vida já me deu."



    g "Mel, estar com você é tipo o melhor abraço depois de um dia longo e cansativo, sabe?"

    g "Às vezes, eu me pego pensando como seria minha vida sem você, e cara, nem quero imaginar isso."

    g "Você é como um ímã de felicidade, Mel. Não tem jeito de ficar triste perto de você."

    g "Sabe, Mel, cada vez que você sorri, eu sinto como se ganhasse na loteria. É uma sensação incrível."

    g "Cara, você é demais, Mel. Não sei o que fiz para merecer alguém tão incrível como você."

    g "Às vezes, me pergunto o que fiz para ter você na minha vida, Mel. E agradeço todo santo dia por isso."

    g "Quando estou com você, parece que o tempo voa, Mel. É como se o mundo desacelerasse só para nos dar um tempinho a mais."

    g "Não tem lugar onde eu prefira estar do que aqui, com você, Mel. É o melhor lugar do mundo."

    g "Obrigado por ser tão maravilhosa, Mel. Você é tipo a minha âncora, sabe? Me mantém firme nos dias turbulentos."

    g "Mel, sua presença deixa tudo mais leve, mais colorido. É como se você trouxesse um pouco de magia para minha vida."

    g "Às vezes, fico me perguntando como consegui viver tanto tempo sem você, Mel. É como se eu tivesse encontrado minha outra metade."

    g "Você é tipo meu raio de sol em dias nublados, Mel. Só de estar perto de você, tudo fica mais claro."

    g "Às vezes, acho que te amo tanto que meu coração vai explodir, Mel. Você é minha maior alegria."

    g "Mel, você é demais, sério. Cada vez que te vejo, parece que o dia fica um pouco melhor."

    g "Não sei o que fiz para ter alguém tão incrível como você na minha vida, Mel. Só sei que sou muito sortudo."

    g "Às vezes, me pego pensando em como seríamos bons juntos, Mel. E aí percebo que já somos ótimos."

    g "Você me faz sentir invencível, Mel. Com você ao meu lado, não tem desafio que eu não encare de cabeça erguida."

    g "Sabe, Mel, só de pensar em você, meu coração dá uma acelerada. É como se ele soubesse que está perto de alguém muito especial."

    g "Obrigado por ser tão incrível, Mel. Você é tipo o melhor presente que a vida me deu."

    g "Quando estou com você, sinto como se o mundo inteiro desaparecesse, Mel. É só nós dois e um amor que não tem fim."

    g "Mel, você é como um raio de sol na minha vida, iluminando todos os meus dias com seu sorriso radiante."

    g "Não há lugar onde eu prefira estar do que nos seus braços, Mel. Você é meu lar, meu refúgio."

    g "Cada momento ao seu lado é um presente para mim, Mel. Você torna cada dia especial."

    g "Obrigado por estar sempre ao meu lado, Mel. Você é meu porto seguro, minha âncora em tempos turbulentos."

    g "Sabe, Mel, quando estou com você, sinto como se o tempo parasse e o mundo desaparecesse. É só nós dois, e isso é tudo que importa."

    g "Seu amor me dá forças para enfrentar qualquer desafio, Mel. Você é minha inspiração."

    g "Não consigo imaginar minha vida sem você, Mel. Você é minha razão de viver, meu combustível para sonhar."

    g "Cada vez que olho nos seus olhos, Mel, vejo um futuro cheio de amor, aventura e felicidade. E mal posso esperar para vivê-lo ao seu lado."

    g "Obrigado por ser tão incrível, Mel. Você é o melhor presente que já recebi."

    g "Às vezes, me pego pensando em como tive sorte de encontrar alguém tão especial como você, Mel. Você é minha felicidade."

    g "Só quero que saiba o quanto te admiro, Mel. Você é forte, corajosa e incrivelmente talentosa em tudo o que faz."

    g "Cada vez que vejo você sorrir, Mel, sinto como se todo o universo estivesse conspirando a nosso favor."

    g "Estou tão grato por termos nos encontrado, Mel. Você é minha parceira de vida, minha alma gêmea."

    g "Você me inspira a ser melhor a cada dia, Mel. Obrigado por me amar do jeito que sou."

    g "Às vezes, me pego pensando em como você mudou minha vida para melhor, Mel. E só posso agradecer por cada momento ao seu lado."

    g "Nada no mundo se compara ao amor que sinto por você, Mel. É o mais belo sentimento que já conheci."

    g "Cada vez que ouço sua voz, Mel, meu coração se enche de alegria e gratidão por tê-la ao meu lado."

    g "Você é a luz que ilumina meu caminho, Mel. Sem você, eu estaria perdido na escuridão."

    g "Adoro quando você me abraça, Mel. É como se todo o universo estivesse em perfeita sintonia."

    g "Só queria te dizer o quanto te amo, Mel. Você é minha razão de viver, meu amor eterno."













    mc "Quero te chupar tão gostoso que você vai esquecer seu próprio nome, amor."
    g "Vou te deixar sem fôlego, te chupando com tanta vontade que você vai implorar por mais."
    mc "Estou molhada só de pensar em envolver meus lábios quentes ao redor do seu pau."
    g "Vou te levar ao paraíso com a minha boca, te chupando até você não aguentar mais."
    mc "Quero sentir seu pau latejando de prazer na minha boca, me enchendo com seu gosto."
    g "Vou te fazer gemer de tanto prazer, te chupando até você explodir na minha boca."
    mc "Estou ansiosa para sentir você todo dentro de mim, me preenchendo por completo."
    g "Vou te foder com força e tesão, te fazendo delirar de prazer a cada estocada."
    mc "Quero que você me pegue de jeito e me faça sua, me fodendo com todo seu desejo."
    g "Vou te mostrar o quão bom pode ser, te fodendo como só eu sei fazer."
    mc "Quero sentir seu pau latejando de prazer dentro de mim, me levando à loucura."
    g "Vou te fazer gozar tão gostoso que você vai ver estrelas, te levando ao êxtase."
    mc "Estou molhada só de pensar em sentir você todo dentro de mim, me fodendo com força."
    g "Vou te fazer gritar de tanto prazer, te levando ao ápice do tesão."
    mc "Quero que você me foda com força e tesão, me deixando completamente louca por você."
    g "Vou te encher com meu pau duro e grosso, te fazendo gemer de tanto prazer."
    mc "Estou ansiosa para sentir você todo dentro de mim, me levando à loucura de tanto tesão."
    g "Vou te foder tão gostoso que você vai implorar por mais, me pedindo para não parar."


    g "Vou te fazer gozar como nunca antes, te enchendo de prazer com minha punheta."

    g "Vou te fazer gozar tão forte que você vai implorar por mais, Mel."
    mc "Estou molhada só de pensar em sentir seu pau duro e latejante na minha mão, te levando ao limite do prazer."
    g "Vou te enlouquecer com minha punheta, te fazendo gozar como um animal."
    g "Vou te fazer gozar tanto que você vai esquecer seu próprio nome, Mel."

    g "Vou te deixar sem fôlego, te masturbando com tanta vontade que você vai implorar por mais."
    mc "Quero te ver gemendo e tremendo de tanto prazer enquanto eu te masturbo com força."
    g "Vou te levar ao êxtase com minha punheta, te fazendo gozar como nunca antes."
    mc "Estou molhada só de pensar em sentir seu pau pulsando na minha mão enquanto eu te masturbo com vontade."
    g "Vou te fazer gozar tão gostoso que você vai implorar por mais, Mel."
    mc "Quero te fazer gozar como um verdadeiro macho alfa, te masturbando com toda minha habilidade."
    g "Vou te deixar sem palavras, te masturbando até você explodir de prazer na minha mão."
    mc "Estou ansiosa para te levar ao orgasmo com minha punheta, te fazendo gemer alto de tanto tesão."
    g "Vou te fazer gozar tão forte que você vai ver estrelas, Mel."
    mc "Quero sentir seu gozo quente e pegajoso escorrendo pelos meus dedos enquanto eu te masturbo com prazer."


    g "Não para, Mel, quero gozar bem gostoso na sua mão."
    g "Estou à beira do orgasmo, Mel, me faz gozar forte."
    g "Que punheta gostosa, Mel, me fazendo perder a cabeça."
    g "Não para agora, Mel, me fazendo querer gozar tão forte."

    g "Estou tão perto, Mel, me fazendo querer explodir de prazer."
    g "Só mais um pouco, Mel, e vou te encher de porra quente."
    g "Quero te cobrir com meu gozo, Mel, continua me masturbando."
    g "Estou quase lá, Mel, me fazendo querer gozar como um animal."



    mc "Estou gemendo intensamente, meu corpo latejando de tesão só de ver Gabriel duro e quase gozando pra mim."
    mc "Meu corpo todo está pegando fogo só de imaginar o que faria com aquele pau duro na minha mão."
    mc "Imagino aquele pau grosso entrando e saindo de mim, me levando ao limite do prazer."
    mc "Quero sentir aquele pau quente e latejante escorrendo pelo meu corpo, me marcando como sua."
    mc "Estou tão molhada que escorrem os pensamentos obscenos, imaginando aquele pau me penetrando com força."
    mc "Quero sentir aquele pau grosso e pulsante me enchendo de prazer, me fazendo gozar como uma louca."
    mc "Sinto meu corpo todo arrepiar de tesão só de imaginar aquela vara dura e latejante me possuindo."
    mc "Mal posso esperar para sentir aquele pau enorme me preenchendo, me levando à loucura de tanto prazer."
    mc "Estou tão excitada que sinto minha boceta latejar só de pensar em como aquele pau vai me deixar completamente saciada."
    mc "Quero sentir aquele pau duro e quente pulsando em minha mão, me levando à beira do orgasmo."
    mc "Imagino aquele pau grande e grosso me penetrando com força, me fazendo gemer alto de tanto prazer."
    mc "Estou tão excitada que sinto minha respiração ficar mais pesada só de imaginar aquela vara dura me fodendo com força."
    mc "Quero sentir aquele pau latejante escorrendo pelo meu corpo, me marcando como sua putinha."
    mc "Sinto meu corpo todo tremendo de desejo só de pensar em como aquele pau vai me deixar completamente louca de prazer."
    mc "Mal posso esperar para sentir aquela vara pulsante me preenchendo, me fazendo gozar como uma verdadeira puta."
    mc "Estou tão molhada que sinto meu clitóris latejar só de pensar em sentir aquele pau duro e pulsante me penetrando."

    mc "Sinto minha boceta ficar ainda mais molhada só de imaginar aquele pau me fodendo com vontade, me fazendo gritar de prazer."
    mc "Estou tão excitada que sinto meu corpo todo se contorcer só de pensar em sentir aquele pau duro e pulsante me invadindo."





    mc "Estou tão molhada que preciso me aliviar enquanto te dou prazer."

    mc "Mal posso esperar para sentir você gozar enquanto me vejo tocando minha buceta molhada."
    g "Vai, safada, se toca com vontade enquanto me masturba. Quero ver você gozar comigo."
    mc "Estou gemendo só de imaginar você gozando enquanto me vejo tocando minha boceta faminta."
    g "Quero ver você se deliciar enquanto me masturba, minha vadia. Me faça gozar com sua mão gostosa."
    mc "Vou me masturbar tão gostoso pensando em você gozando enquanto te masturbo."
    g "Isso, minha putinha, se toca com vontade enquanto me masturba. Quero sentir você gozar junto comigo."
    mc "Estou tão excitada que mal consigo me conter. Vou me masturbar até você gozar na minha mão."
    g "Vou te ensinar a fazer direitinho, minha vadia. Se toca gostoso enquanto eu te mando."
    mc "Quero ver você gemendo de prazer enquanto me vejo tocando minha boceta molhada."
    g "Não para, minha puta, se toca com vontade enquanto me masturba. Quero sentir você gozar comigo."
    mc "Estou tão molhada que preciso me aliviar enquanto te masturbo. Vou gozar junto com você."
    g "Vai, minha putinha safada, se toca com vontade enquanto me masturba. Quero sentir você gozar comigo."
    mc "Mal posso esperar para sentir sua porra quente enquanto me vejo tocando minha buceta faminta."
    g "Isso, se toca com vontade enquanto eu te mando, minha vadia. Quero ver você gozar comigo."
    mc "Estou tão excitada que vou gozar junto com você enquanto me masturbo."
    g "Vou te ensinar a fazer direitinho, minha vadia. Se toca gostoso enquanto eu te mando."



    g "Você me contou que seus pais tinham medo que você se envolvesse com pessoas ruins na capital. E o que eles diriam se soubessem que você está ficando comigo?"

    mc "Eles diriam que você é um sortudo."

    g "Um sortudo? Por quê?"

    mc "Porque você está ficando com a garota mais linda da capital."

    g "E você é convencida também, né?"

    mc "Só um pouquinho."



    mc "Você já pensou em sair da casa do seu pai?"

    g "Já pensei sim. Mas não é tão fácil. Eu ainda dependo dele financeiramente."

    mc "Mas você não trabalha?"

    g "Trabalho sim. Mas não ganho o suficiente para me sustentar sozinho."

    mc "E se eu te ajudasse?"

    g "Você me ajudaria?"

    mc "Claro! A gente podia dividir um apartamento. Seria divertido."

    g "Seria incrível. Mas não quero te colocar em uma situação difícil."

    mc "Eu posso me cuidar. E eu quero estar com você."



    mc "Gab, preciso te contar uma coisa."

    g "O que foi, amor?"

    mc "Outro dia, o Jasper... ele tentou me beijar."

    g "O quê?!"

    mc "Calma, Gab. Não aconteceu nada. Eu não deixei."

    g "Mas ele tentou? O que ele fez?"

    mc "Ele me encurralou na cozinha e tentou me agarrar. Mas eu consegui me soltar e fugi."

    g "Aquele desgraçado! Eu vou acabar com ele!"

    mc "Não, Gab, por favor. Eu não quero que você se meta em problemas."

    g "Mas ele não pode sair impune! Ele te assediou!"

    mc "Eu sei. Mas eu não quero que isso vire um escândalo. Eu só quero esquecer que isso aconteceu."

    g "[mc]..."

    g "Eu sinto muito que você tenha passado por isso. Você não merece."

    mc "Eu sei. Mas eu vou ficar bem. Eu tenho você."

    g "E você sempre vai ter. Eu te amo, [mc]."

    mc "Eu também te amo, Gab."



    mc "Gab, eu preciso te confessar uma coisa."

    g "O que foi, amor?"

    mc "Eu... eu não contei tudo sobre o que aconteceu com o seu pai."

    g "O que você quer dizer?"

    mc "Eu... eu não contei que ele... que ele me beijou."

    g "Ele te beijou? E você... você deixou?"

    mc "Eu... eu não sei. Eu fiquei confusa. Ele me disse que... que eu era especial para ele."

    g "E você acreditou?"

    mc "Eu... eu não sei. Mas eu... eu me sinto atraída por ele."

    g "[mc]..."

    g "Eu não acredito nisso. Eu confiei em você. E você... você me traiu?"

    mc "Não, Gab, não foi traição. Eu... eu não sei o que está acontecendo comigo. Eu só... eu só preciso de tempo para pensar."

    g "Tempo para pensar? Você precisa pensar se você me ama?"

    mc "Eu... eu te amo, Gab. Mas eu também... eu também sinto algo pelo seu pai."

    g "Como você pode sentir algo por ele? Ele é meu pai!"

    mc "Eu sei. E eu sei que isso é errado. Mas eu não consigo evitar."

    g "Eu... eu não sei o que fazer. Eu te amo, [mc]. Mas eu não posso competir com meu pai."

    mc "Eu... eu não quero que você compita. Eu só... eu só preciso de tempo para entender o que está acontecendo comigo."

    g "Eu te amo, [mc]. E eu vou estar aqui pra você, não importa o que aconteça."

    mc "Obrigada, Gab."

    "Eu não sei o que fazer. Eu amo o Gabriel. Mas eu também sinto algo pelo pai dele. E agora?"



    mc "Eu não sei o que fazer. Eu amo o Gabriel. Mas eu também sinto algo pelo pai dele. E eu sei que isso é errado."

    "Mas... e se eu pudesse ajudar o Sr. Silva? E se eu pudesse fazer ele voltar a ser o homem que ele era antes? O homem que o Gabriel tanto amava?"

    "Eu sei que ele está sofrendo. Ele perdeu a esposa e se fechou para o mundo. Mas eu acho que ele ainda tem um bom coração. Eu posso ver em seus olhos."

    "Se eu conseguir fazer o Gabriel aceitar o pai de volta, talvez ele possa voltar a ser feliz. E talvez... talvez eu possa ter uma chance com ele."

    "Eu sei que isso é egoísta. Mas eu não consigo evitar. Eu me sinto tão atraída por ele. E eu quero que ele seja feliz."

    "Eu vou tentar. Eu vou fazer o Gabriel aceitar o pai dele de volta. E eu vou fazer o Sr. Silva voltar a ser o homem que ele era antes."

    "E então... talvez eu possa ter uma chance com ele. E nós três poderemos ser felizes juntos."



    mc "Gab, eu preciso te falar sobre seu pai."

    g "O que foi? Ele fez algo com você?"

    mc "Não, não. Mas... eu conversei com ele sobre o passado dele."

    g "Sobre o passado dele? O que ele te contou?"

    mc "Ele disse que... ele cometeu alguns erros. E que confiou nas pessoas erradas."

    g "Ah... Ele sempre fala isso. Mas ele nunca me contou o que realmente aconteceu."

    mc "Eu sinto muito."

    g "Obrigado, [mc]."

    g "..."

    "Esse parece um assunto muito delicado... pros dois."



    mc "Você sente falta da sua mãe?"

    g "Sim, muita. Ela era... incrível. Ela sempre me apoiou e me incentivou a seguir meus sonhos."

    mc "Como ela era?"

    g "Ela era... gentil, carinhosa, inteligente. Ela era a melhor mãe do mundo."

    mc "Eu gostaria de ter conhecido ela."

    g "Eu também. Vocês iam se dar super bem..."

    "Eu me pergunto o que realmente aconteceu com a mãe do Gabriel. Será que o pai dele está escondendo algo?"



    mc "Gab, eu não consigo parar de pensar no que aconteceu com sua mãe."

    g "Eu também não. Eu preciso saber a verdade."

    mc "O que você acha que aconteceu?"

    g "Eu não sei. Mas eu sei que meu pai estava envolvido em algo com o antigo prefeito. E eu acho que minha mãe descobriu."

    mc "E o que você acha que o antigo prefeito fez?"

    g "Eu não sei. Mas ele era um homem corrupto. Ele era capaz de qualquer coisa."

    mc "A gente precisa descobrir a verdade."

    g "Mas como? Já faz tanto tempo."

    mc "A gente pode investigar. Podemos procurar pistas. Podemos conversar com pessoas que conheciam sua mãe."

    g "Você acha que isso é uma boa ideia? E se a gente se meter em problemas?"

    mc "Eu sei que é arriscado. Mas eu não posso ficar parada sem fazer nada. Eu quero te ajudar, Gab."

    g "Obrigado, [mc]. Você é a melhor."

    "Eu não sei no que eu estou me metendo. Mas eu não posso deixar o Gabriel sozinho nessa. Ele precisa saber a verdade sobre o que aconteceu com sua mãe."



    mc "Lembra que a gente tava falando sobre o passado da empresa do seu pai?"

    g "Sim... e chegamos a conclusão que o velho não vai porra nenhuma."

    mc "Eu acho que... tem algo a ver com o antigo prefeito."

    g "O antigo prefeito? O que ele tem a ver com isso?"

    mc "Eu não sei. Mas eu acho que o seu pai fez algum tipo de acordo com ele. E que esse acordo acabou dando errado."

    g "Eu... eu nunca soube disso."

    mc "E... eu também acho que a morte da sua mãe tem algo a ver com isso."

    g "O quê?!"

    mc "Eu... eu não tenho certeza. Mas é só um palpite."

    g "Mas... como? O que você sabe?"

    mc "Eu não sei muito. Mas eu acho que... a sua mãe descobriu algo sobre o acordo do seu pai com o antigo prefeito. E que... ela foi morta por causa disso."

    g "Meu Deus..."

    g "Eu... eu preciso saber a verdade."

    mc "Eu também. E eu vou te ajudar a descobrir."

    "Eu não sei se estou pronta para me envolver nisso. Mas eu preciso ajudar o Gabriel. Ele precisa saber a verdade sobre o que aconteceu com sua mãe."



label silva_textos:



    mc "Boa noite, Sr. Silva. Só de estar aqui ao seu lado, sinto que a noite promete ser interessante."

    mc "Boa noite, Sr. Silva. Sua presença sempre traz uma aura de mistério e fascínio."

    mc "Boa noite, Sr. Silva. Seu abraço é tão reconfortante... Quase me sinto em casa."

    mc "Boa noite, Sr. Silva. "

    mc "Boa noite, Sr. Silva. "

    mc "Boa noite, Sr. Silva. Só queria dizer que admiro muito sua... autoridade."

    mc "Boa noite, Sr. Silva. Seus gestos tão firmes e decididos me deixam... intrigada."

    mc "Boa noite, Sr. Silva. Às vezes me pego pensando em como sua voz é... envolvente."

    mc "Boa noite, Sr. Silva. Estava ansiosa para estar ao seu lado esta noite... e aqui estou."

    mc "Boa noite, Sr. Silva. Seu perfume é tão... hipnotizante."

    mc "Boa noite, Sr. Silva. "

    mc "Boa noite, Sr. Silva. Sua energia é tão... cativante."

    mc "Boa noite, Sr. Silva. Acho que nunca conheci alguém tão... intrigante como você."

    mc "Boa noite, Sr. Silva. Às vezes me pego pensando em como seria... estar mais próxima de você."



    s "Boa noite, Melissa. Espero que esteja aproveitando a noite... da maneira que lhe convém."

    s "Boa noite, Melissa. Sua energia sempre traz um... certo dinamismo ao ambiente."

    s "Boa noite, Melissa. "

    s "Boa noite, Melissa. Fico contente em vê-la por aqui... mesmo que sua presença seja um tanto... intrigante."

    s "Boa noite, Melissa. Sua... companhia é sempre... estimulante."

    s "Boa noite, Melissa. Espero que esteja se sentindo... confortável aqui."

    s "Boa noite, Melissa. "

    s "Boa noite, Melissa. Sua... presença aqui é sempre... bem-vinda."

    s "Boa noite, Melissa. Sua... presença é sempre... marcante."

    s "Boa noite, Melissa. Seu... jeito sempre... me surpreende."

    s "Boa noite, Melissa. "

    s "Boa noite, Melissa. "

    s "Boa noite, Melissa. Seu... jeito de ser nunca deixa de... chamar minha atenção."

    s "Boa noite, Melissa. Sua... presença aqui sempre... agita as coisas."

    s "Boa noite, Melissa. Espero que esteja... aproveitando a noite até agora."

    s "Boa noite, Melissa. Seu... jeito de ser sempre... desperta minha curiosidade."

    s "Boa noite, Melissa. Sua... presença aqui é sempre... instigante."

    s "Melissa, é interessante como você... sempre chama minha atenção."

    s "Melissa, seus olhos têm um brilho... hipnotizante."

    s "Melissa, cada vez que você está por perto... sinto como se o ambiente ganhasse vida."

    s "Melissa, é difícil ignorar o... impacto que você causa quando está aqui."

    s "Melissa, sua... aura sempre traz uma energia diferente para o ambiente."

    s "Melissa, sua presença... sempre deixa um rastro de mistério no ar."

    s "Melissa, "

    s "Melissa, espero que saiba o quanto... sua presença é notável para mim."

    s "Melissa, é difícil não notar o quanto você... ilumina o ambiente com sua presença."

    s "Melissa, cada vez que você entra em uma sala... parece que tudo fica mais... interessante."

    s "Melissa, você sempre consegue... deixar uma marca por onde passa."

    s "Melissa, sua presença aqui... sempre traz um ar de... expectativa."

    s "Melissa, sua... presença nunca passa despercebida."

    s "Melissa, é curioso como você sempre... consegue capturar a atenção de todos ao seu redor."

    s "Melissa, sua presença sempre... traz um elemento de surpresa para a noite."

    s "Melissa, você tem um jeito único de... deixar sua marca em tudo o que faz."

    s "Melissa, cada vez que você está por perto... sinto como se estivesse diante de algo... excepcional."

    s "Melissa, espero que esteja desfrutando da noite... tanto quanto eu."

    s "Melissa, é difícil não ficar intrigado com... sua presença aqui."



    mc "Será que ele percebe como meus mamilos estão duros só de estar tão perto?"

    mc "Só de olhar para ele, sinto uma onda de desejo me inundando."

    mc "Eu me pergunto como seria sentir suas mãos fortes e dominadoras sobre meu corpo."

    mc "Apenas um toque dele me deixa toda arrepiada... imagina mais do que isso."





    mc "Fico impressionada com sua inteligência e perspicácia, Sr. Silva. É muito estimulante estar perto de alguém tão fascinante como você."

    mc "Gosto da sua companhia, Sr. Silva. Você tem uma maneira cativante de me manter interessada e curiosa."

    mc "Você é uma pessoa tão interessante, Sr. Silva. Sempre me surpreende com suas opiniões e ideias."

    mc "Às vezes me pego pensando em como seria divertido passar mais tempo com você, Sr. Silva. Quem sabe o que poderíamos descobrir juntos."

    mc "Você tem um jeito tão envolvente, Sr. Silva. Às vezes me pego querendo saber mais sobre você e suas experiências."

    mc "Adoro nossas conversas, Sr. Silva. Você sempre me deixa querendo mais, me instigando a explorar novos territórios."

    mc "Sabe, Sr. Silva, às vezes me sinto atraída pela sua aura de mistério e sabedoria. É como se houvesse tanto a descobrir sob a superfície."







    s "Se continuar assim, Melissa, não haverá como voltar atrás. Pense bem nas suas escolhas."

    s "Não subestime as consequências das suas ações, Melissa. Este é um jogo perigoso que você está jogando."

    s "Seja sensata, Melissa. Não brinque comigo. Eu não sou alguém para ser subestimado."

    s "Você está desafiando algo que não compreende, Melissa. Pare enquanto ainda pode."

    s "Esta é sua última chance, Melissa. Não ultrapasse essa linha."

    s "Você está prestes a se queimar, Melissa. Ainda há tempo para recuar."



    mc "Você me enlouquece, Sr. Silva. Mal posso esperar para te fazer gozar gostoso."

    mc "Não consigo parar de pensar em você, Sr. Silva. Preciso sentir seus lábios nos meus."

    mc "Quero ser sua, Sr. Silva. Quero que me possua com todo seu desejo."

    mc "Estou tão molhada só de imaginar você me penetrando com força, Sr. Silva."

    mc "Vou te fazer delirar de prazer, Sr. Silva. Vou te levar ao paraíso com minha boca."

    mc "Sinto minha boceta latejar só de pensar em como você vai me fazer gozar, Sr. Silva."

    mc "Estou faminta por você, Sr. Silva. Quero te sentir dentro de mim, me preenchendo por completo."

    mc "Quero que me faça sua, Sr. Silva. Quero ser sua putinha e te fazer gozar como nunca antes."

    mc "Mal posso esperar para te fazer gozar gostoso, Sr. Silva. Vou te dar prazer como nunca sentiu antes."

    mc "Estou tão excitada que só de pensar em você me tocando, meu corpo todo se contorce de desejo."

    mc "Quero sentir suas mãos explorando cada centímetro do meu corpo, Sr. Silva. Me faça sua."

    mc "Estou pronta para te levar ao êxtase, Sr. Silva. Quero ser usada por você até não aguentar mais."

    mc "Meu corpo todo clama pelo seu toque, Sr. Silva. Vou te fazer gemer de prazer até você perder a cabeça."

    mc "Quero te provocar até você não aguentar mais, Sr. Silva. Vou te fazer gozar como um verdadeiro macho alfa."

    mc "Estou tão molhada só de pensar em sentir você dentro de mim, Sr. Silva. Vou te levar ao paraíso com minha boca."

    mc "Quero te provocar até você perder o controle, Sr. Silva. Vou te fazer implorar por mais enquanto te levo ao ápice do prazer."

    mc "Você é tudo o que eu quero, Sr. Silva. Mal posso esperar para sentir seu pau duro e latejante me preenchendo."



    mc "Devo me conter, mas meu desejo está me consumindo. Não sei mais o que fazer."

    mc "Talvez eu devesse parar, mas a ideia de resistir me deixa ainda mais excitada."

    mc "Não sei se é certo, mas estou tão molhada que mal consigo pensar direito."

    mc "Talvez eu esteja brincando com fogo, mas não consigo evitar."

    mc "Devo me afastar, mas a tentação é irresistível. Estou à beira do delírio."

    mc "Não sei se isso vai acabar bem, mas estou disposta a correr o risco. O desejo é mais forte que a razão."



    mc "Isso é tão errado, mas cada gemido que escapa dos meus lábios é uma confissão do meu desejo pelo Sr. Silva."

    mc "Como posso desejar o pai do meu namorado desse jeito? Mas é como se o Sr. Silva me possuísse."

    mc "Será que ele notaria se eu gemer mais alto? O Sr. Silva está me fazendo perder o controle."

    mc "Isso é tão sujo, tão errado, mas o Sr. Silva sabe exatamente como me deixar molhada."

    mc "Oh Deus, o que estou fazendo? Mas cada toque do Sr. Silva me faz gemer de prazer."

    mc "Gabriel me ama tanto, mas é como se o Sr. Silva fosse a única coisa em que consigo pensar."

    mc "Devo parar, mas meu corpo está tão faminto pelo Sr. Silva que não consigo resistir."

    mc "Isso é uma traição horrível, mas cada beijo do Sr. Silva me deixa ansiando por mais."

    mc "Gabriel é tão bom para mim, mas é como se o Sr. Silva despertasse um lado obscuro dentro de mim."

    mc "Será que ele notaria o cheiro do sexo em mim? Estou tão excitada pelo Sr. Silva que mal consigo me conter."

    mc "Isso é tão errado, mas o Sr. Silva é como uma droga viciante que eu não consigo resistir."

    mc "Gabriel não merece isso, mas é como se o Sr. Silva fosse a única coisa que eu realmente quisesse."

    mc "Devo parar de pensar nele, mas cada pensamento meu é consumido pelo Sr. Silva."

    mc "Oh Deus, o que estou fazendo com Gabriel? Mas o Sr. Silva é tão irresistível, tão tentador."

    mc "Isso é uma traição terrível, mas cada gemido que escapa dos meus lábios é uma confissão do meu desejo pelo Sr. Silva."



    mc "Vou te fazer gemer tão alto que Gabriel vai ouvir, enquanto você me fode gostoso, Sr. Silva."

    mc "Quero te chupar com voracidade, lambendo e sugando seu pau até você implorar por mais, Sr. Silva."

    mc "Vou cavalgar em você como uma puta faminta, rebolando no seu pau até você gozar como um animal, Sr. Silva."

    mc "Quero que me foda com força, Sr. Silva, me fazendo gritar seu nome enquanto gozo no seu pau."

    mc "Estou molhada só de pensar em te sentir dentro de mim, Sr. Silva, me fodendo como uma cadela no cio."

    mc "Vou te fazer delirar de prazer, Sr. Silva, te provocando até você não aguentar mais e me foder com força."

    mc "Quero ser sua putinha, Sr. Silva, sua escrava do prazer, te dando tudo o que você deseja."

    mc "Vou te levar ao limite do prazer, Sr. Silva, te fazendo gozar como nunca antes, me usando como sua vadia."

    mc "Quero sentir seu pau latejando de desejo na minha boca, Sr. Silva, enquanto te chupo com vontade."

    mc "Vou te fazer gemer de tanto tesão, Sr. Silva, te provocando até você implorar para me foder."

    mc "Estou faminta por você, Sr. Silva, quero te devorar inteiro e te fazer gozar como nunca gozou antes."

    mc "Quero sentir suas mãos fortes me explorando inteira, Sr. Silva, me tocando e me fodendo como você quiser."

    mc "Estou molhada só de pensar em você me fodendo com força, Sr. Silva, me dando tudo o que você tem."

    mc "Vou te fazer perder o controle, Sr. Silva, te levando ao êxtase do prazer enquanto te imploro por mais."

    mc "Quero ser sua puta pessoal, Sr. Silva, te satisfazendo em todos os sentidos e te deixando louco de desejo."

    mc "Estou tão excitada só de pensar em sentir seu pau duro e pulsante dentro de mim, Sr. Silva, me fodendo com força."

    mc "Quero que me use como sua vadia particular, Sr. Silva, me fodendo até eu não aguentar mais e gozar como uma cadela no cio."



    s "Não vou te dar escolha, Melissa. Você vai se submeter a mim e pagar pelo seu comportamento imprudente."

    s "Você vai implorar por misericórdia, Melissa, mas vou te fazer implorar por mais enquanto te puno."

    s "Acha que pode brincar comigo, Melissa? Vou te mostrar o que acontece com as garotas más."

    s "Você quer minha atenção, Melissa? Então vai ter que pagar o preço, e a punição será prazer para ambos."

    s "Não pense que pode me manipular, Melissa. Vou te mostrar quem está no controle aqui, enquanto te levo ao limite."

    s "Vou te mostrar como é ser verdadeiramente dominada, Melissa. Prepare-se para uma lição que vai te deixar implorando por mais."

    s "Não importa o quanto você tente resistir, Melissa, no final vai implorar por mais enquanto eu te puno com prazer."

    s "Se quer desafiar minha autoridade, Melissa, prepare-se para as consequências enquanto te levo ao ápice do prazer."

    s "Você vai aprender a respeitar os limites, Melissa, enquanto te mostro como é ser punida com prazer."

    s "Não posso deixar sua rebeldia passar em branco, Melissa. Vou te punir com prazer até você implorar por mais."

    s "Você precisa ser disciplinada, Melissa, mas prometo que a punição será tão prazerosa quanto dolorosa."

    s "Vou te mostrar como é ser completamente dominada, Melissa. Prepare-se para uma experiência que vai te deixar sem fôlego."

    s "Não se atreva a desafiar minha autoridade, Melissa. Vou te punir com prazer até você se entregar completamente."

    s "Você quer brincar de ser má, Melissa? Então prepare-se para ser punida e recompensada da forma mais intensa possível."

    s "Você precisa ser punida, sua putinha insaciável. Mas vou te mostrar como é ser usada da forma correta, fodendo você até implorar por mais."

    s "Acha que pode me provocar e sair ileso, sua vadia atrevida? Vou te mostrar o verdadeiro significado de prazer e dor enquanto te domino com minha rola."

    s "Não vou te dar escolha, sua cadela. Você vai se submeter a mim e pagar pelo seu comportamento imprudente enquanto eu te arrebento com força."

    s "Você quer minha atenção, sua piranha? Então vai ter que pagar o preço, e a punição será prazer para nós dois, quando eu te foder até você delirar."

    s "Você quer desafiar minha autoridade, sua safada? Prepare-se para as consequências enquanto te levo ao ápice do prazer e te faço implorar por mais."

    s "Se quer brincar de ser má, sua cadelinha, prepare-se para ser punida e recompensada da forma mais excitante e obscena possível."



    s "É uma contradição deliciosa, Melissa. Sua inocência combinada com sua sensualidade me deixa louco de desejo."

    s "Você é como um fogo ardente envolto em pura inocência, Melissa. E isso me excita além da medida."

    s "É como se você fosse feita para despertar todos os meus instintos mais primitivos, Melissa. Você me enlouquece de uma forma que não consigo explicar."

    s "Às vezes me pergunto como alguém tão angelical como você pode despertar tantos desejos pecaminosos em mim, Melissa."

    s "Sua pureza só intensifica minha luxúria por você, Melissa. É uma combinação perigosa que me consome por completo."

    s "Você é como uma tentação divina, Melissa. Sua inocência só torna seu corpo ainda mais irresistível para mim."

    s "É como se você fosse feita para me enlouquecer, Melissa. Sua pureza só aumenta meu desejo por você."

    s "Às vezes me pergunto se você tem noção do poder que tem sobre mim, Melissa. Sua inocência só aumenta minha luxúria por você."





    mc "Sr. Silva, o senhor pode me contar mais sobre a sua empresa de reparos?"

    s "Era uma empresa pequena, mas eficiente. Tínhamos uma equipe de profissionais qualificados e experientes. Fazíamos todo tipo de reparo, desde pequenos consertos em casas até grandes reformas em prédios."

    mc "E o senhor também trabalhava para a prefeitura?"

    s "Sim, ganhamos algumas licitações para fazer reparos em escolas, postos de saúde e outros prédios públicos."

    mc "Parece um trabalho muito importante."

    s "Era sim. Eu gostava de saber que estava ajudando a comunidade."

    mc "Então o que aconteceu? Por que o senhor perdeu a empresa?"

    s "Eu... eu cometi alguns erros. Confiei nas pessoas erradas."

    mc "Eu entendo."

    s "Eu... eu sinto falta daquela época. De ter minha própria empresa, de fazer a diferença na vida das pessoas."

    mc "O senhor ainda pode fazer a diferença. O senhor é um homem bom. E o Gabriel precisa do senhor."

    s "Obrigado, Melissa. Você é... muito especial."

    "Eu quero ajudá-lo a superar seus erros do passado. E eu quero que ele seja feliz de novo."



    mc "Sr. Silva, eu... eu não posso mais esconder isso. Eu amo você."

    s "Melissa, eu... eu também te amo. Mas... você sabe que isso é errado."

    mc "Eu sei. Mas eu não consigo evitar. Eu quero estar com você."

    s "Mas e o Gabriel? Ele é meu filho."

    mc "Eu sei. E eu... eu não quero magoá-lo. Mas eu não posso negar o que eu sinto por você."

    s "Então... o que você quer fazer?"

    mc "Eu... eu não sei. Eu preciso pensar."

    s "Eu entendo. Mas... por favor, não demore muito. Eu não sei quanto tempo mais eu vou conseguir ficar sem você."

    "Eu não sei o que fazer. Eu amo o Sr. Silva. Mas eu também amo o Gabriel. E eu não quero machucar ninguém."



    mc "Sr. Silva, eu... eu tenho medo."

    s "Medo de quê?"

    mc "Medo de que o Gabriel descubra sobre nós."

    s "Eu também tenho medo. Mas... eu não posso viver sem você."

    mc "Eu também não. Mas... eu não quero magoar o Gabriel."

    s "Eu sei. Eu... eu vou conversar com ele. Vou contar a verdade."

    mc "O senhor acha que ele vai entender?"

    s "Eu não sei. Mas eu tenho que tentar. Eu não posso mais viver com essa mentira."

    "Eu espero que o Gabriel possa nos perdoar. Eu quero que nós três sejamos felizes."



    mc "Sr. Silva, o senhor pode me contar mais sobre sua esposa?"

    s "Ela... era a mulher mais incrível que eu já conheci. Ela era gentil, carinhosa, inteligente... Ela era tudo para mim."

    mc "O senhor sente muita falta dela?"

    s "Sim, muita. Todos os dias."

    mc "Eu sinto muito."

    s "Obrigado, Melissa. Você é... muito gentil."

    "Eu posso ver a dor em seus olhos. Ele ainda a ama muito."



    menu:
        "Sr. Silva, eu... eu não posso mais continuar com isso.":


            s "Com o quê?"

            mc "Com... com a gente."

            s "Mas... por quê?"

            mc "Eu... eu não posso trair o Gabriel. Ele é meu namorado."

            s "Mas você disse que me amava."

            mc "Eu... eu sei. Mas eu amo o Gabriel também. E eu não posso fazer isso com ele."

            s "Eu... eu entendo."

            "Eu não sei se fiz a coisa certa. Mas eu não podia continuar com o Sr. Silva, sabendo que eu amo o Gabriel."
        "Só vou continuar aproveitando isso que nós temos":


            mc "..."

            s "Tudo bem, garota?"

            mc "Sim... só quero ficar quietinha hoje..."

            s "..."



    "Eu não posso deixar o Gabriel descobrir sobre mim e o Sr. Silva. Eu não quero perdê-lo."

    "Eu não sei o que vai acontecer. Mas eu sei que essa noite vai ser... inesquecível."











    mc "Senhor Silva, o senhor já me contou que sua esposa morreu. Como o senhor superou a perda dela?"

    s "Eu... eu nunca superei. Mas eu aprendi a viver com a dor."

    mc "O senhor ainda a ama?"

    s "Sim, eu a amo. E sempre vou amar."

    mc "Eu sinto muito."

    s "Obrigado, Melissa. Você é... muito compreensiva."

    "Eu sinto tanta pena do Sr. Silva. Ele ainda está sofrendo muito pela morte da esposa."



































    mc "Senhor Silva, eu conversei com o Editor Chefe da revista sobre a corrupção na prefeitura. Ele disse que o senhor pode ter informações sobre o antigo prefeito."

    s "O Editor Chefe? O que ele te disse?"

    mc "Ele disse que o senhor tinha uma boa relação com o antigo prefeito. E que o senhor pode ter testemunhado alguns atos de corrupção."

    s "Isso... isso não é verdade."

    mc "Mas o senhor não me contou que sua empresa perdeu contratos com a prefeitura depois que o novo prefeito assumiu?"

    s "Isso... isso foi apenas uma coincidência."

    mc "Eu não acredito em coincidências."

    "Ele está mentindo. Eu sei que ele está."



    mc "Senhor Silva, eu acho que a morte da sua esposa está ligada à corrupção na prefeitura."

    s "O quê?! Como você pode dizer isso?"

    mc "Eu... eu tenho minhas suspeitas. E eu vou descobrir a verdade."

    s "Melissa, por favor, não se envolva nisso. É perigoso."

    mc "Eu não tenho medo. Eu quero ajudar o senhor. E eu quero que a verdade seja revelada."

    "Eu sei que ele está com medo. Mas eu não vou desistir. Eu vou descobrir o que aconteceu com a esposa dele."







    mc "Senhor Silva, o Gabriel me contou que o senhor e a esposa dele brigavam muito. Por que vocês brigavam?"

    s "Nós... tínhamos problemas. Como qualquer casal."

    mc "Mas o Gabriel disse que as brigas eram feias. Que o senhor era... controlador."

    s "Eu... eu só queria o melhor para a minha família. Eu queria protegê-los."

    mc "Mas às vezes, proteger demais pode sufocar as pessoas."

    s "Você... você está certa. Eu... eu cometi erros."

    "Eu acho que o Sr. Silva está começando a entender que seu comportamento foi prejudicial para o Gabriel."



    mc "Senhor Silva, o Gabriel me contou que o senhor era muito feliz quando a esposa dele estava viva. O que a tornava tão especial?"

    s "Ela... ela era a luz da minha vida. Ela me fazia feliz. Ela me completava."

    mc "E o senhor acha que nunca mais vai encontrar alguém que te faça feliz?"

    s "Eu... eu não sei. Depois que ela morreu, eu perdi a esperança."

    mc "Mas o senhor não pode desistir do amor. O senhor merece ser feliz."

    s "Você acha?"

    mc "Eu tenho certeza. O senhor é um homem bom. E eu... eu me importo com o senhor."

    "Eu quero que ele saiba que eu estou aqui para ele. E que eu posso fazê-lo feliz."







    mc "Senhor Silva, o senhor pode me contar mais sobre os tipos de reparos que sua empresa fazia?"

    s "Claro. Fazíamos de tudo um pouco. Consertávamos telhados, encanamentos, sistemas elétricos... Também fazíamos reformas em geral, como pintura, troca de pisos e azulejos..."

    mc "O senhor era bom no que fazia?"

    s "Eu era o melhor. Eu sempre fui muito exigente com a qualidade do meu trabalho."

    mc "E o senhor gostava do que fazia?"

    s "Sim, eu gostava. Eu gostava de ver a diferença que a gente fazia na vida das pessoas. Quando a gente reformava uma escola, por exemplo, era gratificante ver as crianças felizes com o novo espaço."



    mc "Senhor Silva, o senhor me contou que sua empresa perdeu contratos com a prefeitura depois que o novo prefeito assumiu. Por que isso aconteceu?"

    s "Eu... eu não sei. Talvez o novo prefeito não tenha gostado do meu trabalho."

    mc "Mas o senhor disse que era o melhor no que fazia."

    s "Eu era. Mas... as coisas mudam. E os políticos... nem sempre são honestos."

    mc "O senhor está insinuando que o novo prefeito é corrupto?"

    s "Eu... eu não disse isso. Mas... você é uma garota inteligente. Tire suas próprias conclusões."

    "Ele está me dizendo que o novo prefeito é corrupto? E que isso pode ter algo a ver com a morte da esposa dele?"



    s "Melissa, você está linda hoje."

    mc "Obrigada, senhor Silva."

    s "Venha cá, sente-se ao meu lado."

    mc "Sim, senhor."

    s "Eu quero que você saiba que eu estou muito feliz por você estar aqui. Você me faz sentir... vivo."

    mc "Eu também me sinto feliz quando estou com o senhor."

    s "Mas eu quero mais do que apenas sua companhia. Eu quero você. Só para mim."

    mc "Eu... eu não sei o que dizer."

    s "Você não precisa dizer nada. Apenas me beije."

    "Ele é tão mandão. Mas... eu gosto disso. Eu me sinto... segura com ele."







    s "Melissa, eu quero que você pare de ver o Gabriel."

    mc "O quê?!"

    s "Eu não quero que você o magoe. Ele é meu filho."

    mc "Mas eu não estou magoando ele! Eu o amo!"

    s "Você não sabe o que é amor. Você é apenas uma criança."

    mc "Eu não sou uma criança! Eu sei o que eu sinto!"

    s "Então prove. Fique comigo. Esqueça o Gabriel."

    "Ele está me dando um ultimato? Eu... eu não sei o que fazer."







    mc "Senhor Silva, eu não sei se devo continuar com o Gabriel."

    s "Por que não?"

    mc "Ele é... tão jovem. E eu... eu não sei se ele é o homem certo para mim."

    s "E você acha que eu sou o homem certo para você?"

    mc "Eu... eu não sei. Mas eu me sinto... segura com o senhor. E desejada."

    s "Então fique comigo. Esqueça o Gabriel."

    mc "Mas... e o Gabriel?"

    s "Ele vai superar. Ele é jovem. Ele vai encontrar outra pessoa."

    "Ele está sendo tão egoísta. Mas... eu não consigo negar que eu quero ficar com ele."



    s "Melissa, eu quero que você se mude para cá. Para o meu apartamento."

    mc "O quê?!"

    s "Eu quero que você esteja sempre comigo. Eu quero cuidar de você."

    mc "Mas... e o Gabriel?"

    s "Ele pode ficar com o apartamento dele. Eu vou comprar um novo para nós dois."

    mc "Mas... isso é loucura!"

    s "Loucura? Ou amor?"

    "Ele está falando sério? Ele quer que eu me mude para cá? E o Gabriel? O que eu vou fazer?"

















    mc "Então por que o senhor não demonstra isso?"

    s "Eu... eu não sei. Eu acho que... eu tenho medo."

    mc "Medo de quê?"

    s "Medo de me abrir. Medo de ser... vulnerável."











    mc "Eu... eu sinto muito."

    s "Pelo quê?"

    mc "Pelo que aconteceu no outro dia. Eu não devia ter te beijado."

    s "Mas você me beijou. E eu... eu gostei."

    mc "Eu também. Mas... isso não está certo. Você é o pai do Gabriel."

    s "Eu sei. E eu... eu não quero magoá-lo."

    mc "Então por que o senhor me beijou?"

    s "Eu... eu não sei. Eu me sinto... atraído por você. De um jeito que eu não consigo explicar."

    mc "Eu também me sinto atraída pelo senhor. Mas... isso é errado."

    s "Eu sei. Mas... e se a gente tentasse? Só uma vez?"



    mc "Eu... eu não sei. Eu preciso pensar."

    s "Eu entendo. Mas... não demore muito. Eu não sei quanto tempo mais eu vou conseguir me segurar."







    "Eu sei que esse relacionamento é errado. Mas eu não consigo evitar. Ele me faz sentir coisas que eu nunca senti antes. E eu... eu quero mais."



    s "Você é tão linda, Melissa."

    mc "Obrigada, senhor Silva."

    s "Eu quero que você seja minha. Só minha."

    mc "Eu... eu não sei."

    s "O que você quer dizer com 'não sabe'? Você não me quer?"

    mc "Eu... eu quero. Mas... eu não quero ser apenas sua. Eu quero ter minha própria vida, meus próprios sonhos."

    s "E você pode ter tudo isso. Comigo."

    mc "Mas como? O senhor é tão... controlador."

    s "Esse não sou eu de verdade. Isso é só algo que um pai de verdade tem que fazer. Mas nunca seria assim com você"

    mc "O senhor realmente faria isso? Mudaria por mim?"

    s "Sim. Eu faria qualquer coisa por você."

    "Ele está falando sério? Ele realmente mudaria por mim? Ou será que ele está apenas me manipulando?"

    mc "Eu... eu preciso de tempo para pensar."

    s "Tudo bem. Mas não demore muito. Eu não sei quanto tempo mais eu vou conseguir me segurar."



    "Eu sei que esse relacionamento é errado. Mas eu não consigo evitar. Ele me faz sentir coisas que eu nunca senti antes. E eu... eu quero mais."



    g "Vai, time!"

    mc "Bora!"

    s "Calma, garoto. O jogo ainda está no começo."

    mc "Seu pai está certo, Gab. Não precisa ficar tão nervoso."

    s "Essa garota é ou não é um amor? Dê atenção a ela, menino."

    mc "Obrigada, senhor Silva."

    g "Mas olha esses caras, pai!"

    s "Garoto idiota..."

    mc "Ksks..."









    "Ele está me olhando de novo. Com aquele olhar... intenso. Será que ele está pensando em mim? No que aconteceu no outro dia?"



    g "Ah, não! Eles vão perder!"

    mc "Calma, Gab. Ainda tem tempo."

    s "É só um jogo, garoto. Não precisa ficar tão nervoso."

    "Ele está tão frustrado. Eu queria poder fazer algo para ajudá-lo."

    mc "Senhor Silva, o senhor está bem?"

    s "Estou sim. Só estou... um pouco decepcionado com o time."

    mc "Eu entendo. Mas não fique triste. O Gabriel vai ficar bem."

    s "Obrigado, Melissa. Você é... muito especial."

    g "O que eu perdi?"

    mc "Nada. Seu pai só estava me contando como ele está orgulhoso de você."

    g "É verdade, pai?"

    s "Claro que não... você só me dá trabalho, fedelho."

    g "Agora sim eu acredito..."

    mc "Vocês dois..."















    mc "Senhor Silva, posso te perguntar uma coisa?"

    s "Pode."

    mc "O Gabriel me contou que o senhor já teve uma empresa de reparos. O que aconteceu com ela?"

    s "Eu... eu a perdi. Há alguns anos."

    mc "Como assim?"

    s "Os negócios... não estavam indo bem."

    mc "Mas o senhor não disse que o senhor era um bom empresário?"

    s "Eu era. Mas... as coisas mudam."

    mc "O que mudou?"

    s "..."

    s "Eu não quero falar sobre isso."

    mc "Mas eu quero entender. Eu quero conhecer o senhor melhor."

    s "Não há nada para entender. É passado."

    mc "Mas o passado pode nos ajudar a entender o presente. E o futuro."

    s "Você é muito insistente, sabia?"

    mc "Eu sei. Mas eu me importo com o senhor. E com o Gabriel."

    s "Eu... eu não sei se posso confiar em você."

    mc "O senhor pode. Eu nunca faria nada para machucar o Gabriel. E eu quero ajudar o senhor."

    s "Talvez... um dia eu te conte."

    mc "Eu vou estar esperando."











    mc "Senhor Silva, o senhor já me contou que sua empresa fazia reparos para a prefeitura. O senhor chegou a conhecer o antigo prefeito?"

    s "Sim, cheguei a conversar com ele algumas vezes."

    mc "Sério? Como ele era?"

    s "Era um homem... poderoso. E influente."

    mc "E o senhor gostava dele?"

    s "Ele... era um bom homem. Ele queria o melhor para a cidade."

    s "..."

    mc "O senhor parece ter saudades daquela época."

    s "Sim, eu sinto. Eu era... importante. As pessoas me respeitavam."

    mc "O senhor ainda é importante. E eu te respeito."

    mc "E eu acho que o senhor ainda é muito poderoso."

    s "Você é muito doce, Melissa."

    "Eu adoro quando ele me chama de doce. Me faz sentir... especial. E eu sei que ele gosta de mim. Eu posso ver em seus olhos."

    mc "E o senhor sabe que eu gosto de homens poderosos."

    s "É mesmo?"

    mc "Sim. Homens que sabem o que querem e que não têm medo de ir atrás."

    s "Você é uma garota muito perigosa, sabia?"

    mc "Perigosa? Eu?"

    s "Sim. Você mexe comigo de um jeito que eu não consigo explicar."

    mc "Eu também me sinto assim quando estou com o senhor."



    mc "Senhor Silva, o senhor me contou que conheceu o antigo prefeito. Como era o relacionamento de vocês?"

    s "Era... profissional. Eu tinha uma empresa de reparos e ganhei algumas licitações da prefeitura."

    mc "E o senhor gostava dele?"

    s "Ele... era um homem de negócios. Como eu."

    mc "E o senhor acha que ele era um bom prefeito?"

    s "..."

    s "Ele... fez algumas coisas boas para a cidade."

    mc "E algumas coisas ruins também?"

    s "Todos os políticos cometem erros, garota."

    mc "Mas alguns erros são maiores do que outros, não é?"

    s "..."

    mc "Eu sei que o senhor está escondendo algo de mim. Mas eu não vou te pressionar. Eu vou esperar até que o senhor esteja pronto para me contar."

    s "[mc]..."

    "Eu sei que ele está envolvido em algo. Algo que tem a ver com o antigo prefeito e com a morte da mãe do Gabriel. Mas eu vou ajudá-lo a superar isso. E eu vou conquistá-lo."







    mc "Senhor Silva, posso te perguntar uma coisa?"

    s "Pode."

    mc "O senhor disse que sua esposa era bonita. Mas... eu sou mais bonita que ela?"

    s "!"

    s "Garota, eu... eu não posso responder isso."

    mc "Por que não?"

    s "Porque... é complicado. E eu não quero magoar você."

    mc "Mas eu quero saber. Eu quero saber se o senhor me acha atraente."

    s "[mc], você é uma mulher muito bonita. Mas... minha esposa era... diferente."

    mc "Diferente como?"

    s "Não sei explicar. Mas ela tinha um charme do passado. Algo que eu acho que não existe mais hoje."

    mc "E o senhor prefere mulheres mais maduras?"

    s "Eu não disse isso. Eu só sei que... você mexe comigo de um jeito que eu não consigo explicar."

    "Eu sei que ele está pensando nela. Mas eu vou fazer ele me esquecer dela. Eu vou ser a única mulher na vida dele."



label investigacao_textos:



    "Se a esposa de Silva descobriu seus contratos ilegais com o prefeito e ameaçou denunciá-lo, isso colocaria Silva em uma posição muito difícil."

    "Ele teria que escolher entre sua família e sua carreira."

    "Se ele se recusasse a parar de pagar propina ao prefeito, sua esposa poderia ter denunciado a corrupção, o que teria levado à falência de sua empresa e à sua prisão."

    "Se ele concordasse em parar de pagar propina, ele poderia ter perdido seus contratos com a prefeitura e sua empresa também teria falido."

    "Se Silva contou ao prefeito sobre a ameaça de sua esposa, o prefeito pode ter visto isso como uma oportunidade de se livrar de um problema."

    "Ele pode ter ordenado o assassinato da esposa de Silva para silenciá-la e garantir que seus esquemas de corrupção não fossem descobertos."

    "A morte da esposa de Silva teria um impacto devastador em sua vida e na vida de Gabriel."

    "Silva pode ter se tornado um homem amargo e desconfiado, e Gabriel pode ter crescido com um sentimento de raiva e ressentimento em relação ao pai."

label fernando_textos:



































    mc "Senhor Fernando, o senhor pode me contar mais sobre sua filha?"

    fe "Ela... ela é a coisa mais importante da minha vida. Eu a amo mais do que tudo."

    mc "E o senhor sente falta dela?"

    fe "Sim, sinto. Todos os dias. Eu... eu queria poder vê-la de novo."

    mc "Eu entendo. Eu também sinto falta da minha família."

    fe "[mc]... você... eu sinto algo especial por você, assim como sinto por ela."

    mc "Eu... eu não sei o que dizer."

    fe "Você não precisa dizer nada. Eu só... eu só queria que você soubesse."

    "Eu sei que o seu Fernando gosta de flertar comigo... mas isso... isso foi diferente..."



















    mc "Senhor Fernando, o senhor já foi a algum show na capital?"

    fe "Sim, já fui a alguns. Mas... eu não sou muito fã de música alta."

    mc "Haha... eu também não. Mas eu gosto de ir a shows de vez em quando. É divertido."

    fe "E que tipo de música você gosta?"

    mc "Eu gosto de música pop e sertaneja."

    fe "Sertaneja? Você é do interior mesmo, né?"

    mc "Sim, sou. E o senhor? Que tipo de música o senhor gosta?"

    fe "Eu... eu gosto de música clássica."

    mc "O senhor é um homem de gostos refinados."

    fe "Eu tento ser."











    mc "Senhor Fernando, o senhor viu as notícias sobre a Copa do Mundo que vai ser realizada na capital?"

    fe "Sim, vi. É uma ótima notícia para a cidade. Vai trazer muitos investimentos e empregos."

    mc "Eu também acho. Mas... eu também estou preocupada. A cidade já está tão lotada. Imagina com a Copa do Mundo?"

    fe "Você tem razão. O governo precisa se preparar para receber tantos turistas. É preciso investir em infraestrutura e segurança."

    mc "Eu espero que o governo faça um bom trabalho. Eu não quero que a Copa do Mundo seja um caos."

    fe "Eu também espero. A Copa do Mundo é uma grande oportunidade para a capital. Mas... também é um grande desafio."







    mc "Senhor Fernando, qual é a coisa mais maluca que o senhor já viu na capital?"

    fe "Hmm... essa é uma pergunta difícil. Eu já vi muita coisa maluca nesta cidade."

    mc "Como o quê?"

    fe "Uma vez, eu vi um homem andando na rua com um jacaré na coleira."

    mc "Um jacaré?! Sério? Nem na fazenda! Eu nunca vi um!"

    fe "Sim. E o jacaré estava usando um chapéu de cowboy."

    mc "Só na capital mesmo para se ver uma coisa dessas."

    fe "É verdade. Esta cidade é um lugar único."

    mc "E você sabe como fazer rir..."

    fe "E você sabe como fazer meu dia melhor."

    mc "..."



    fe "Melissa, você já ouviu falar da lenda do fantasma da Ópera?"

    mc "Sim, já ouvi. Mas... isso é só uma lenda, né?"

    fe "Eu não sei. Uma vez, eu estava no Teatro Municipal e ouvi uma voz cantando. Era uma voz linda e melancólica. Mas... não havia ninguém no palco."

    mc "Nossa... isso é assustador."

    fe "Eu não sei se foi o fantasma da Ópera. Mas... foi algo muito estranho."







    mc "Senhor Fernando, o senhor já foi à Ilha das Celebridades?"

    fe "Sim, já fui. Mas... eu não gosto muito de lá."

    mc "Por que não?"

    fe "Eu acho que a ilha é muito... artificial. É como se fosse um mundo à parte."

    mc "Eu entendo. Eu também me sinto um pouco assim quando vou lá."

    fe "Mas... a ilha nem sempre foi assim. Antigamente, era um lugar muito mais simples. Tinha pescadores, agricultores... Era um lugar muito mais autêntico."

    mc "É uma pena que as coisas tenham mudado."

    fe "Sim, é. A ilha se tornou um playground para os ricos."

    mc "Foram os Donatellos que mudaram tudo?"

    fe "Garota... você tá entrando numa pegada perigosa."

    mc "Eu não tenho medo. Eu tenho o sangue forte da minha família."

    fe "Não sei quanto o sangue da sua família vai te ajudar quando eles tem mandarem o M... digo... eu sei, sim..."

    mc "H-hm?"

    fe "Você vai precisar de muita transfusão de sangue."

    mc "O senhor tá me assustando agora."

    fe "Que bom."



    fe "Melissa, você já foi ao Cassino do Barão?"

    mc "Não, ainda não. Eu não sou muito fã de jogos de azar."

    fe "Eu também não. Mas... o Cassino do Barão é mais do que apenas um cassino. É um lugar... especial."

    mc "Especial como?"

    fe "É um lugar onde os sonhos se tornam realidade. Ou... pelo menos é o que dizem."

    mc "Hmm... interessante."

    fe "Mas... também é um lugar perigoso. Muitas pessoas perderam tudo o que tinham no Cassino do Barão."

    mc "Você ganhou ou perdeu mais?"

    fe "Perdi, óbvio."

    mc "Poxa..."

    fe "Mas foi jogando muito que eu consegui meu Gold Card."

    mc "O que é isso?"

    fe "É um cartão que te dá acesso à área VIP do Cassino. E você não tem ideia do que tem lá."

    mc "UAU! O QUÊ?!"

    fe "Quem sabe um dia eu não te leve lá?"

    mc "Ai, seu Fernando... que misterioso."

    fe "Eu sinto que tem mais sabor assim."

    mc "Hmm..."































    mc "Fernando, o que o senhor acha da teoria de que a Faux News pertence à família Donatello?"

    fe "Eu... eu não sei. É uma teoria interessante. Mas eu não tenho provas para confirmá-la."

    mc "Mas o senhor acha que é possível?"

    fe "Tudo é possível na Capital, Melissa. Esta cidade está cheia de segredos."

    mc "E o senhor acha que o Sr. Donatello é corrupto?"

    fe "Eu... eu não posso dizer. Mas... eu sei que ele é um homem muito poderoso. E o poder... o poder pode corromper as pessoas."

    mc "Eu concordo. Mas... eu prefiro acreditar na inocência das pessoas. Eu me sinto melhor assim."

    fe "É porque você é uma pessoa boa. Eu também espero que ele seja uma pessoa honesta. Mas... só o tempo dirá."







    mc "Fernando, o senhor viu as notícias sobre a crise hídrica na Capital?"

    fe "Sim, vi. É uma pena que a cidade esteja passando por isso."

    mc "O senhor acha que o governo está fazendo o suficiente para resolver o problema?"

    fe "Eu... eu não sei. É uma situação complicada. Mas eu espero que eles encontrem uma solução logo."

    mc "Eu também. Eu não quero que a cidade fique sem água."

    fe "Sim, seria um desastre. Mas... eu tenho certeza de que o governo vai dar um jeito."

    mc "Eu não sei se você tá certo. O governo parece tá mais preocupado em se manter no poder do que em resolver os problemas da cidade."

    mc "Pelo menos é o que eu vejo pelas notícias e pelas histórias por aí."

    fe "Vamos torcer pelo melhor..."











    mc "Fernando, o senhor já conheceu muitas pessoas famosas?"

    fe "Sim, já conheci algumas. Políticos, artistas, empresários..."

    mc "Uau! Isso é incrível! Quem foi a pessoa mais famosa que o senhor já conheceu?"

    fe "Eu... eu não posso dizer. Mas... posso te garantir que foi alguém muito importante."

    mc "Você é todo misterioso às vezes."

    fe "Haha... eu gosto de manter um pouco de mistério."

    mc "Sei..."



    mc "Fernando, o senhor tem algum hobby?"

    fe "Eu... eu gosto de ler. E de ouvir música clássica."

    mc "Que tipo de livros o senhor gosta de ler?"

    fe "Eu gosto de romances. E de livros de história."

    mc "Eu também gosto de romances. Qual é o seu livro favorito?"

    fe "Meu livro favorito é... 'Romeu e Julieta'."

    mc "Por quê?"

    fe "Porque... é uma história de amor trágica. E eu... eu me identifico com Romeu."

    "Ele está se comparando a Romeu? Será que ele está tentando me dizer algo?"



    mc "Fernando, o senhor já me contou que viajou para muitos lugares. Qual foi a viagem mais emocionante que o senhor já fez?"

    fe "Hmm... essa é uma pergunta difícil. Já fiz tantas viagens incríveis... Mas acho que a mais emocionante foi quando eu escalei o Monte Everest."

    mc "O Monte Everest?! Isso é incrível!"

    fe "Sim, foi uma experiência única. A vista do topo do mundo é... indescritível."

    mc "Eu não consigo nem imaginar. O senhor deve ser muito corajoso."

    fe "Não sei se sou corajoso. Mas eu gosto de desafios."







    mc "Fernando, você acha que eu poderia viver no mundo da alta sociedade?"

    fe "Você já vive no mundo da alta sociedade, Melissa. Você mora em um dos prédios mais luxuosos da Capital."

    mc "Sim, mas... eu não me sinto parte desse mundo. Eu sou apenas uma garota do interior."

    fe "Você é muito mais do que isso, Melissa. Você é inteligente, bonita e determinada. Você tem tudo para ter sucesso nesse mundo."

    mc "Mas... eu não sei como me comportar. Eu não sei as regras."

    fe "Eu posso te ensinar as regras, Melissa. Eu posso te ajudar a se encaixar nesse mundo."

    mc "Você faria isso por mim?"

    fe "Claro que sim. Eu quero que você seja feliz. E eu quero que você esteja comigo."

    mc "Mas... e o Gabriel?"

    fe "Ele... ele não precisa saber."

    mc "Eu... eu não sei se isso é certo."

    fe "O que é certo, Melissa? O que te faz feliz?"

    "O que mais faz feliz?"

    mc "..."



    mc "Fernando, você pode me contar como são as festas da alta sociedade?"

    fe "As festas da alta sociedade são... eventos únicos. Há muita comida boa, bebida cara e pessoas influentes."

    mc "Parece divertido."

    fe "Pode ser. Mas também pode ser um pouco entediante. As pessoas geralmente só falam de negócios e de dinheiro."

    mc "E o senhor? O senhor se diverte nessas festas?"

    fe "Eu... eu me divirto quando estou com você."

    mc "C-comigo?"

    fe "Sim. Você é... diferente. Você é genuína. E você me faz sentir... vivo."















    fe "Melissa, você está linda esta noite."

    mc "Obrigada, Fernando. Você também está muito elegante."

    fe "Eu... eu queria te perguntar uma coisa."

    mc "Claro, o que é?"

    fe "Você... você está feliz com o Gabriel?"

    mc "Eu... eu não sei. Eu o amo. Mas... às vezes eu sinto que ele não me entende."

    fe "Eu entendo. Eu... eu já passei por isso."

    mc "O senhor quer dizer... com sua esposa?"

    fe "Sim. Nós... nos amávamos. Mas... com o tempo, as coisas mudaram. Ela queria coisas que eu não podia dar a ela."

    mc "Como o quê?"

    fe "Ela queria... mais liberdade. Mais aventura. E eu... eu só queria protegê-la."

    mc "Eu entendo. Eu também quero ser livre. Mas eu também quero me sentir segura."

    fe "Eu posso te dar as duas coisas, Melissa. Eu posso te dar liberdade e segurança."

    mc "Eu... eu não sei o que fazer."

    fe "Você não precisa fazer nada agora. Apenas... me dê uma chance."

    mc "Tudo bem. Eu vou te dar uma chance."

    fe "Obrigado, Melissa. Você não vai se arrepender."









    mc "Senhor Fernando, eu preciso saber a verdade. Como o senhor realmente conseguiu comprar seu primeiro apartamento?"

    fe "Eu... eu não fui totalmente honesto com você."

    mc "Eu sei."

    fe "Eu... eu usei alguns métodos... antiéticos."

    mc "Antiéticos? Como assim?"

    fe "Eu... eu me envolvi com algumas pessoas... que não eram muito honestas."

    mc "O senhor está falando de... crime?"

    fe "Eu... eu não quero falar sobre isso."

    mc "Eu preciso de um tempo para pensar."

    fe "Melissa... por favor... me perdoe."

    mc "Eu... eu não sei se posso."



    mc "Senhor Fernando, eu preciso saber mais. O que o senhor quer dizer com 'métodos antiéticos'?"

    fe "Eu... eu me envolvi com algumas pessoas... que estavam envolvidas em atividades ilegais."

    mc "Que tipo de atividades ilegais?"

    fe "Eu... eu não quero falar sobre isso."

    mc "Mas eu preciso saber. Eu não posso simplesmente ignorar isso."

    fe "Eu... eu me envolvi com um grupo de pessoas que estavam... lavando dinheiro."

    mc "Lavando dinheiro?"

    fe "Sim. Eles estavam usando meu negócio para lavar dinheiro sujo."

    mc "Mas... como o senhor se envolveu com essas pessoas?"

    fe "Eu... eu estava desesperado. Minha empresa estava falindo e eu não sabia o que fazer. Eles me ofereceram uma saída."

    mc "E o senhor aceitou?"

    fe "Sim. Eu... eu não tinha escolha."



    mc "Senhor Fernando, o senhor pode me contar mais sobre como o senhor lavava dinheiro para essas pessoas?"

    fe "Eu... eu usava minha empresa de reparos para lavar dinheiro. Eles me davam dinheiro sujo e eu o usava para pagar por serviços e materiais. Depois, eu devolvia o dinheiro para eles, limpo."

    mc "E o senhor nunca foi pego?"

    fe "Não. Eu era muito cuidadoso. E... eu tinha contatos na polícia."

    mc "Contatos na polícia?"

    fe "Sim. Eu... eu os subornava."

    mc "O senhor... o senhor subornava policiais?"

    fe "Sim. Eu... eu não tinha escolha. "





    fe "O prefeito Vittorino Donatello... ele era um homem muito poderoso. E... ele era corrupto."

    mc "O senhor sabe como ele era corrupto?"

    fe "Ele... ele usava seu poder para beneficiar seus amigos e familiares. Ele desviava dinheiro público para suas próprias contas."

    mc "E o senhor... o senhor participou disso?"

    fe "Sim... eu participei."

    mc "Senhor Fernando, eu... eu não sei o que pensar."

    fe "Eu... eu entendo. Eu fiz coisas terríveis."

    mc "Mas... por que o senhor fez isso?"

    fe "Eu... eu estava desesperado. Minha empresa estava falindo e eu não sabia o que fazer. O prefeito Vittorino Donatello me ofereceu uma saída. E eu... eu aceitei."

    mc "Mas... o senhor não podia ter denunciado ele?"

    fe "Eu... eu tinha medo. Ele era um homem muito poderoso. E... eu não queria perder tudo o que eu tinha conquistado."

    mc "Eu entendo. Mas... o que o senhor vai fazer agora?"

    fe "Eu... eu não sei. Eu só... eu só quero que você me perdoe."






    mc "Fernando, preciso te falar sobre o aluguel deste mês. As coisas estão difíceis para mim, e eu estava pensando se você poderia me dar um desconto."

    fe "Melissa, você sabe que adoro ajudar. Claro que posso te dar um desconto no aluguel."

    mc "Sério? Muito obrigada! Você me salva!"

    fe "Mas, há algo que eu gostaria em troca."

    mc "O que seria?"

    fe "Nada demais. Apenas que você me acompanhe para jantar na sexta-feira."

    mc "Ah, Fernando... Eu não sei."

    fe "Mas Melissa, você sabe como me sinto sozinho. Seria bom ter sua companhia."

    mc "Ok, tudo bem. Eu vou com você."

    fe "Maravilha! Então o desconto está combinado. E quanto ao jantar, podemos ir àquele restaurante italiano que você gosta."

    mc "Ok. Obrigada por tudo, Fernando."

    fe "Não há de que, Melissa."

    fe "Melissa, me diverti muito esta noite."

    mc "Eu também me diverti, Fernando."

    fe "Eu estava pensando... Que tal a gente fazer isso de novo?"

    mc "Eu não sei, Fernando."

    fe "Mas Melissa, você não gostou do jantar? Da minha companhia?"

    mc "Gostei, Fernando. Mas..."

    fe "Mas o quê?"

    mc "Eu não quero me sentir pressionada a fazer algo que não quero."

    fe "Pressionada? Mas Melissa, eu só estou te convidando para jantar."

    mc "Eu sei, Fernando. Mas você sabe que eu dependo de você para o aluguel. E eu não quero me sentir como se tivesse que te dar algo em troca."

    fe "Melissa, você está me interpretando mal. Eu só quero te ajudar."

    mc "Eu sei que você quer me ajudar, Fernando. Mas eu também quero me sentir independente."

    fe "Ok, Melissa. Eu entendo."



    fe "Olá, Melissa. Tudo bem?"

    mc "Oi, Fernando. Mais ou menos. Na verdade, estou um pouco atrasada com o aluguel este mês."

    fe "Ah, não se preocupe com isso, Melissa. Todos nós passamos por momentos difíceis."

    mc "Obrigada, Fernando. Isso me alivia um pouco."

    fe "Mas, falando em aluguel, eu estava pensando... Que tal você me ajudar com algumas tarefas no apartamento em troca de um desconto?"

    mc "Tarefas? Que tipo de tarefas?"

    fe "Coisas simples, como limpar o jardim, organizar a garagem, pequenas coisas que não tenho tempo para fazer."

    mc "Bem, eu poderia ajudar, mas não tenho certeza se sou muito boa em jardinagem..."

    fe "Não se preocupe, Melissa. Eu te ensino tudo o que você precisa saber. E não precisa se esforçar muito, apenas o suficiente para me ajudar."

    mc "Ok, Fernando. Eu posso tentar."

    fe "Ótimo! Então está combinado. Você me ajuda com as tarefas e eu te dou um desconto no aluguel. O que você acha?"

    mc "Parece bom. Obrigada pela sua compreensão, Fernando."

    fe "De nada, Melissa. Sempre que precisar, pode contar comigo."



    fe "Olá, Melissa. Vim verificar se está tudo bem com o apartamento."

    mc "Oi, Fernando. Sim, está tudo bem. Obrigada por perguntar."

    fe "Que bom! Aproveitando que estou aqui, queria te perguntar se você gostaria de tomar um café comigo algum dia."

    mc "Um café? Bem... Eu não sei..."

    fe "Não precisa se preocupar, Melissa. Só um café, como amigos."

    mc "Mas Fernando, você é meu senhorio... Eu não acho que seja uma boa ideia."

    fe "Mas por quê? Somos adultos, podemos ser amigos. E quem sabe, talvez algo mais..."

    mc "Fernando, eu me sinto desconfortável com essa conversa. Por favor, pare."

    fe "Ok, tudo bem. Desculpe se te incomodei. Mas, falando em outra coisa, o aluguel está vencendo em breve. Você já tem o dinheiro?"

    mc "Eu... Eu ainda não o tenho completo."

    fe "Ah, não se preocupe com isso, Melissa. Se você me acompanhar para tomar um café, podemos conversar sobre o aluguel."

    mc "O que você quer dizer?"

    fe "Bem, digamos que se você me fizer companhia, eu posso ser mais flexível com o pagamento do aluguel."

    mc "Fernando, isso é chantagem! Você não pode me pressionar assim."

    fe "Mas Melissa, não é chantagem. É apenas uma proposta. Você decide se quer ou não aceitar."

    mc "Eu não tenho escolha, Fernando. Preciso do desconto no aluguel."

    fe "Então está combinado. Café e desconto no aluguel. O que você acha?"

    mc "Eu acho que você está se aproveitando da minha situação."

    fe "Melissa, você está interpretando mal as coisas. Eu só quero te ajudar."

    mc "..."

    fe "Então, o que você me diz?"

    mc "Ok. Eu vou tomar café com você."

    fe "Ótimo! Que bom que você aceitou. Te vejo amanhã, então."







    fe "Melissa, você está linda esta noite."

    mc "Obrigada, Fernando. Você também está muito elegante."

    fe "Eu me esforço para impressionar a mulher que amo."

    mc "Fernando, você não precisa se esforçar tanto. Eu gosto de você do jeito que você é."

    fe "Mas eu quero ser o melhor para você. Eu quero te fazer feliz."

    mc "Eu sei que você quer, Fernando. E eu aprecio isso."

    fe "Então, me diga, o que você está pensando em fazer depois do jantar?"

    mc "Eu não sei. O que você quer fazer?"

    fe "Bem, eu estava pensando... Que tal irmos ao meu apartamento? Podemos assistir um filme, tomar um vinho..."

    mc "Eu não sei, Fernando. Eu estou um pouco cansada."

    fe "Mas Melissa, estamos apenas começando a noite. Você não quer se divertir um pouco?"

    mc "Eu quero me divertir, Fernando. Mas eu também quero me sentir confortável."

    fe "Mas você estará confortável no meu apartamento. Eu prometo cuidar de você."

    mc "Eu sei que você cuidaria, Fernando. Mas eu não me sinto pronta para isso."

    fe "Tudo bem, Melissa. Eu entendo."

    fe "..."

    mc "Fernando, eu gosto de você. Mas eu preciso de um pouco de tempo. Eu preciso ir devagar."

    fe "Eu sei, Melissa. Eu vou esperar por você. O tempo que for preciso."

    mc "..."

    fe "Mas Melissa, me diga uma coisa. Você me acha atraente?"

    mc "Sim, Fernando. Eu te acho atraente."

    fe "Então, por que você não me dá uma chance? Por que você não me deixa te mostrar o quanto posso te fazer feliz?"

    mc "Eu... Eu não sei, Fernando. Eu preciso pensar."

    fe "Tudo bem, Melissa. Pense o quanto quiser. Mas saiba que estarei aqui, esperando por você."



    fe "Melissa, você é a mulher mais incrível que eu já conheci. Você é linda, inteligente, engraçada..."

    mc "Fernando, você está me deixando sem graça."

    fe "Mas é verdade! Eu nunca me senti assim com ninguém antes. Você me faz sentir especial."

    mc "Você também me faz sentir especial, Fernando. Eu gosto muito de você."

    fe "Eu fico feliz em ouvir isso, Melissa. Eu quero muito te fazer feliz."

    fe "Melissa, eu tenho algo para te dizer."

    mc "O que é, Fernando?"

    fe "Eu... Eu te amo."

    mc "Fernando..."

    fe "Eu sei que é cedo, mas eu não consigo mais negar meus sentimentos. Eu te amo, Melissa."

    mc "Fernando, eu também te amo. Mas eu preciso de um pouco de tempo. Eu não quero me precipitar."

    fe "Eu entendo, Melissa. Eu vou esperar por você. O tempo que for preciso."

    fe "Mas Melissa, me diga uma coisa. Você confia em mim?"

    mc "Sim, Fernando. Eu confio em você."

    fe "Então, por favor, me prometa que você nunca vai me esconder nada. Que você sempre vai ser honesta comigo."

    mc "Eu prometo, Fernando. Eu sempre vou ser honesta com você."

    fe "Melissa, eu preciso te falar algo."

    mc "O que é, Fernando?"

    fe "Eu... Eu encontrei algo no seu celular."

    mc "O que você encontrou?"

    fe "Mensagens de outro homem. Um homem que não sou eu."

    mc "Fernando, eu posso explicar..."

    fe "Explicar o quê? Que você está me traindo? Que você está mentindo para mim?"

    mc "Não, Fernando! Eu nunca te trairia! Eu te amo!"

    fe "Então por que você está me escondendo essas mensagens? Por que você está mentindo para mim?"

    mc "Eu não estou mentindo! Eu só..."

    fe "Chega! Eu não quero mais ouvir suas mentiras! Eu te dei a minha confiança, e você me traiu!"

    fe "Você é uma mentirosa! Uma traidora! Você não merece o meu amor!"

    mc "Fernando, por favor, me escuta! Eu não te trai!"

    fe "Cala a boca! Eu não quero mais te ouvir!"

    mc "Fernando! Você me machucou!"

    fe "Você me machucou mais! Você me traiu!"



    fe "Olá, Melissa. Vim verificar se está tudo bem com o apartamento."

    mc "Oi, Fernando. Sim, está tudo bem. Obrigada por perguntar."

    fe "Que bom! Aproveitando que estou aqui, queria te perguntar sobre o que conversamos da última vez."

    mc "Sobre o que?"

    fe "Sobre o meu amor por você. Você já pensou sobre o que eu disse?"

    mc "Eu... Eu pensei, Fernando. Mas eu ainda não me sinto pronta para um relacionamento."

    fe "Mas Melissa, eu posso te fazer tão feliz. Eu posso te dar tudo o que você precisa."

    mc "Eu sei que você pode, Fernando. Mas eu preciso de tempo para me decidir."

    fe "Quanto tempo você precisa?"

    mc "Eu não sei, Fernando. Preciso seguir meu ritmo."

    fe "Mas Melissa, você não pode me deixar esperando para sempre. Eu tenho necessidades também."

    mc "Eu entendo, Fernando. Mas eu não posso te dar uma resposta agora."

    fe "Tudo bem, Melissa. Mas saiba que estarei aqui, esperando por você."



    mc "Fernando, por favor. Eu não quero isso agora."

    fe "Mas Melissa, você me disse que confia em mim. Você me disse que me daria uma chance."

    mc "Eu confio em você, Fernando. Mas eu preciso de tempo para resolver meus sentimentos."

    fe "Quanto tempo mais você precisa, Melissa? Eu não posso esperar para sempre."

    mc "Eu não sei, Fernando. Me desculpe."



    fe "Melissa, sabe de uma coisa? Eu estava pensando..."

    mc "Sim, Fernando? O que é?"

    fe "Eu estava pensando que você poderia me ajudar com a organização do meu apartamento."

    mc "Fernando, eu já te disse que não posso te ajudar com isso. Eu estou muito ocupada com o trabalho."

    fe "Mas Melissa, você me disse que me ajudaria se eu te desse um desconto no aluguel."

    mc "Eu disse isso, Fernando. Mas eu mudei de ideia."

    fe "Mas Melissa, por que? Você me prometeu."

    mc "Eu sei que prometi, Fernando. Mas eu não posso cumprir minha promessa. Eu simplesmente não tenho tempo."

    fe "Mas Melissa, você não pode me negar depois de tudo que eu fiz por você."

    mc "O que você quer dizer, Fernando?"

    fe "Eu te dei um desconto no aluguel, Melissa. Eu poderia ter cobrado mais de você. Mas eu não fiz isso. Eu fiz isso porque te aprecio."

    mc "Eu sei que você fez, Fernando. E eu agradeço a sua gentileza."

    fe "Então, por favor, Melissa. Ajude-me com a organização do meu apartamento. É a única maneira de você me pagar pelo desconto que eu te dei."

    mc "Fernando, eu..."

    mc "..."

    fe "Melissa, por favor. Eu preciso da sua ajuda."

    mc "Está bem, Fernando. Eu vou te ajudar."

    fe "Ótimo! Eu sabia que você ia me ajudar."











    fe "Sabe, Melissa... eu nunca te contei como minha esposa me deixou."

    mc "Não, senhor Fernando. O senhor nunca me contou."

    fe "Foi... foi há alguns anos. Eu era um homem diferente naquela época. Eu era... ambicioso, workaholic... Eu só pensava em trabalho."

    mc "E... sua esposa?"

    fe "Ela... ela se sentia sozinha. Negligenciada. Eu nunca estava em casa. E quando eu estava, só falava de trabalho."

    mc "Eu sinto muito, senhor Fernando."

    fe "Um dia... ela simplesmente foi embora. Levou nossa filha com ela. Eu nunca mais as vi."

    mc "O senhor... tentou procurá-las?"

    fe "Tentei. Mas... elas não queriam me ver. Eu... eu as magoei muito."

    mc "Calma, senhor Fernando. Eu estou aqui com o senhor."

    fe "Você... você é a única pessoa que me faz sentir... vivo de novo."

    mc "Eu... eu também me importo com o senhor."

    fe "Melissa... eu... eu te amo."

    mc "O senhor... me ama?"

    fe "Sim. Eu sei que isso é errado. Você é jovem... e eu sou um velho. Mas... eu não consigo evitar."

    mc "Eu... eu preciso de um tempo para pensar."

    fe "Eu entendo. Eu... eu vou esperar."

    fe "Só... não se esqueça de mim."



    fe "Melissa... você está ocupada?"

    mc "Ah, senhor Fernando! Não, não estou. Entre."

    fe "Eu... eu trouxe pizza para você. Você deve estar com fome."

    mc "Nossa, senhor Fernando, muito obrigada! Eu estava mesmo precisando de um lanche."

    fe "De nada. Eu... eu também trouxe vinho."





    fe "Melissa... posso entrar?"

    mc "Senhor Fernando... eu... eu não acho que seja uma boa ideia."

    fe "Por favor, Melissa. Eu só quero conversar."

    fe "Eu... eu sei que fui um idiota da outra vez. Me desculpe."

    mc "Tudo bem, senhor Fernando. Eu entendo."

    fe "Mas... eu não posso desistir de você. Eu te amo, Melissa. Eu preciso de você."

    mc "Senhor Fernando... por favor... não faça isso."

    fe "Melissa... você é a única pessoa que me faz feliz. Depois que minha esposa e minha filha me deixaram... eu fiquei sozinho. Eu não tenho mais ninguém."

    mc "Eu sinto muito, senhor Fernando. Mas... eu não posso ser sua muleta emocional."

    fe "Eu não estou te pedindo para ser minha muleta emocional. Eu só... eu só quero estar com você. Eu quero te amar e cuidar de você."

    mc "Mas... eu não sinto o mesmo por você."

    fe "Isso não importa. Eu posso te fazer feliz. Eu posso te dar tudo o que você quiser."

    mc "Não é isso que eu quero. Eu quero alguém que me ame de verdade. Alguém que eu possa amar de volta."

    fe "Eu te amo de verdade, Melissa. Por favor... me dê uma chance."

    mc "Senhor Fernando... por favor... me solte."

    fe "Eu... eu sinto muito. Eu não queria te assustar."



label beto_textos:



    "mc Beto, seus beijos são tão bons..."

    "b: Sério? Eu fico nervoso..."

    "mc Não precisa ficar. Só me beija."

    "mc (Pensamento): Ele é tão doce... mas eu queria mais intensidade."

    "mc Beto, você poderia ser mais... firme?"

    "b: Eu... eu não quero te machucar."

    "mc (Pensamento): Ele é tão cuidadoso... talvez eu precise ser mais direta."

    "mc: Beto, pegue nos meus peitos. Aperta com força."

    "b: O quê? Eu... eu não sei..."

    "mc (Pensamento): Ele está com medo... mas eu preciso que ele entenda."

    "mc: Beto, para de ser um molenga e me obedece."

    "Beto: Tudo bem, eu tento..."



    "mc: Isso, Beto, mais forte."

    "b: Eu... eu não quero te machucar."

    "mc (Pensamento): Ele precisa entender que eu gosto assim."

    "mc: Beto, eu quero que você seja macho, que pegue com força. Isso que mulheres gostam."

    "b: Eu... eu não sei se consigo..."

    "mc (Pensamento): Ele precisa aprender... e eu vou ensinar."

    "mc: Beto, olha pra mim. Eu quero que você me pegue com força. Entendeu?"

    "b: Eu acho que sim..."



    "mc: Isso, Beto, é assim que eu gosto... mais forte."

    "b: Assim?"

    "mc (Pensamento): Ele está aprendendo... e está tão gostoso."

    "mc: Sim, Beto, é assim que eu gosto... continua, mais forte, mais intenso."



    "mc: Uau, Beto, seus beijos estão me deixando sem ar."

    "b: É... eu estou tentando fazer melhor."

    "mc: Você está indo bem, mas quero sentir mais... mais intensidade."

    "b: Eu... eu posso tentar."

    "mc (Pensamento): Ele parece mais confiante... espero que não exagere."



    "mc: Beto, pegue nos meus peitos. Aperta com força."

    "b: Sério? Eu... eu não quero te machucar."

    "mc: Confia em mim, eu sei o que gosto. Me mostra que você é capaz."

    "b: Tudo bem, eu tento..."



    "mc (Pensamento): Caramba, ele está aprendendo rápido demais... isso é bom ou assustador?"

    "mc: Isso, Beto, é assim que eu gosto... mais forte."

    "b: Assim?"

    "mc: Sim, mas... mas não precisa ter medo. Eu estou gostando."

    "b: Eu... eu não quero te machucar, Mel."

    "mc: Você não está me machucando, está me dando prazer. Me faz gemer de tesão."



    "mc (Pensamento): Ele ainda está inseguro... mas está melhorando, e isso está me deixando louca."

    "mc: Isso, Beto, continua assim... mais forte, mais intenso."

    "b: Eu... eu estou melhorando?"

    "mc: Sim, Beto, você está indo muito bem... só precisa continuar se soltando, confiando em si mesmo. Eu estou aqui com você."



    "mc: Beto, eu quero que você pegue na minha bunda. Aperta com força."

    "b: Na... na sua bunda?"

    "mc: Sim, na minha bunda. E não seja molenga, pega com vontade."

    "b: Eu... eu não sei se..."

    "mc (Pensamento): Ele sempre hesita... mas hoje vai ser diferente."

    "mc: Beto, para de pensar tanto e me obedece."

    "b: Tudo bem, eu tento..."



    "mc: Isso, Beto, mais forte. Não precisa ter medo."

    "b: Assim?"

    "mc: Quase lá, mas eu quero sentir mais... e quero que você comece a falar algumas coisas."

    "b: O quê?"

    "mc: Coisas... obscenas. Sobre a minha bunda."

    "b: Eu... eu não sei se consigo..."

    "mc (Pensamento): Ele é tão inocente... mas hoje ele vai aprender."

    "mc: Eu te ajudo. Repete comigo: 'Sua bunda é tão gostosa, Mel. Adoro apertar ela assim.'"

    "b: Sua... sua bunda é tão gostosa, Mel. Adoro apertar ela assim."

    "mc: Isso, continua... 'Quero sentir ela na minha mão, bem apertada.'"

    "b: Quero... quero sentir ela na minha mão, bem apertada."

    "mc: Mais... 'Quero te foder enquanto seguro essa bunda gostosa.'"

    "b: Eu... eu quero te foder enquanto seguro essa bunda gostosa."



    "mc (Pensamento): Ele está aprendendo rápido... e isso está me deixando cada vez mais excitada."

    "mc: Isso, Beto, continua... mas agora quero sentir mais... quero sentir a dor das suas mãos na minha bunda."

    "b: Mas... mas não vai te machucar?"

    "mc: Não, só vai me deixar mais excitada. Eu quero sentir, Beto. Com força."



    "mc: Beto, quero que você aperte minha bunda com mais força desta vez."

    "b: Mais... mais forte?"

    "mc: Isso mesmo, não seja tão delicado."

    "b: Mas... mas não vai doer?"

    "mc: Vai um pouco, e é exatamente isso que eu quero."

    "mc (Pensamento): Ele sempre hesita... mas hoje vai ser diferente."



    "mc: Isso, Beto, assim que eu gosto. Mas agora... quero que você bata."

    "b: Bater?"

    "mc: Sim, quero sentir a dor e o prazer."

    "b: Eu... eu não sei se..."

    "mc (Pensamento): Ele continua tão fraco... talvez eu precise provocá-lo."

    "mc: Beto, será que o Léo faria melhor que você?"

    "b: O Léo?"

    "mc (Pensamento): Ah, agora ele ficou interessado."

    "mc: Sim, o Léo. Mas se você não..."

    "b: Eu... eu vou fazer."



    "mc: Isso, Beto, com mais força. Eu quero sentir."

    "b: Assim?"

    "mc: Quase lá... mas agora quero que você me escute e repita o que eu disser."

    "b: O quê?"

    "mc: Repete comigo... 'Sua bunda é minha, Mel. Eu posso fazer o que eu quiser com ela.'"

    "b: Sua... sua bunda é minha, Mel. Eu posso fazer o que eu quiser com ela."

    "mc: Isso... agora continua... 'Quero te foder enquanto te bato.'"

    "b: Eu... eu quero te foder enquanto te bato."



    "mc (Pensamento): Ele está ficando mais excitado... e isso está me deixando louca de desejo."

    "mc: Isso, Beto, continua... me bate mais forte enquanto eu te provoco."

    "b: Eu... eu não sei..."

    "mc: Confia em mim, Beto. Você está indo muito bem... e eu estou adorando cada segundo."



    "mc (Pensamento): Caramba, ele está ficando duro... ver ele assim só me deixa ainda mais molhada e cheia de tesão."



    "mc: Beto... o que é isso que estou sentindo aí?"

    "b: Eu... eu não sei..."

    "mc (Pensamento): Ele está tentando se esquivar... mas hoje ele não vai escapar."



    "mc: Não se faça de inocente, Beto... sei exatamente o que está acontecendo aqui."

    "b: Mas, Mel..."

    "mc: Quieto. Eu quero ver isso de perto."



    "mc: Você não vai fugir, Beto. Eu quero ver seu pau duro para mim."

    "b: Eu... eu não sei se devemos..."

    "mc: Eu disse, fique quieto. Eu estou no controle agora."



    "mc: Isso, Beto... me deixa te fazer sentir prazer enquanto você me bate. É assim que eu gosto."



    "mc (Pensamento): Ele está tão excitado... e eu adoro ter esse poder sobre ele."

    "mc: Você está gostando, Beto? Está gostando de sentir minha mão te fazendo sentir prazer?"

    "b: Eu... eu não sei..."

    "mc: Você não sabe? Será que o pau do Léo seria maior que o seu?"



    "b: Por que você está falando sobre o Léo agora?"

    "mc: Acho que você está certo, Beto. Eu deveria estar focada em nós dois aqui e agora."



    "mc: Isso, Beto... mais forte. Me mostra o quanto você pode ser dominador."



    "mc (Pensamento): Ele está agindo com mais confiança... e isso está me deixando ainda mais excitada."

    "mc: Isso, Beto... me mostra quem manda aqui. Eu quero mais, eu quero sentir mais."



    "mc: Ah, Beto... você está me deixando louca. Eu quero mais, eu quero tudo que você pode me dar."

    "b: Droga, Mel... eu não consegui segurar mais."



    "mc: Não precisa se desculpar, Beto. Isso só mostra como você estava precisando disso."



    "mc (Pensamento): Ele está tão vulnerável agora... e é tudo por minha causa."



    "mc: Você foi incrível, Beto. Eu estou orgulhosa de você."



    "b: Obrigado, Mel... eu não teria feito isso sem você."



    "mc: Sempre estarei aqui para você, Beto. Agora, vamos nos limpar e aproveitar o resto do dia juntos."



    "b: Sim, vamos aproveitar."





    "mc: Isso, Beto... vem cá e me mostra o quanto você me quer."



    "b: Eu... eu não sei se..."



    "mc: Não se preocupe com nada, Beto... só me mostra como você pode ser ousado."



    "b: Você... você gosta disso?"



    "mc: Oh, sim, Beto... eu adoro sentir seu pau duro roçando na minha bunda. Mais forte."



    "b: Assim?"

    "mc: Isso... assim mesmo. Agora, me diz algumas coisas sujas... me diz o que você quer fazer comigo."



    "b: Eu... eu quero te foder bem gostoso... te fazer gemer de prazer."

    "mc: Isso, Beto... continue... me diz mais coisas safadas."



    "mc: Eu quero sentir seu pau dentro de mim... quero que me foda até eu não aguentar mais."



    "b: Eu... eu quero te fazer gozar tão forte, Mel... quero que você só pense em mim."



    "mc: Isso, Beto... me faz sentir desejada... me faz sentir sua."

    "mc: Isso, Beto... eu quero sentir seu pau bem duro na minha mão."



    "b: Mel... isso é..."

    "mc: Quietinho, Beto... eu sei o que você quer."



    "mc: Eu quero que você seja mais bruto comigo, Beto... me mostra do que você é capaz."

    "b: Mas... eu não quero te machucar."

    "mc: Bobagem, Beto... eu gosto de me sentir dominada por você."



    "mc: Será que o Léo faria melhor que você, Beto?"



    "b: Por que você continua falando sobre o Léo?"

    "mc: Só estou te dando uma comparação, Beto... mas se você não quiser..."







    "b: Eu vou te mostrar do que eu sou capaz, Mel..."

    "mc (Pensamento): Eu preciso gozar também... mas Beto ainda não está lá. Será que o Léo faria melhor?"

    "mc (Pensamento): Droga, eu queria gozar também... será que o Léo saberia como me dominar do jeito certo?"



    "mc: Isso, Beto... eu quero mais, me mostra o que você pode fazer."



    "b: Eu... eu vou tentar, Mel."



    "mc (Pensamento): Ele está se esforçando, mas ainda não está totalmente confiante... eu preciso incentivá-lo mais."

    "mc: Isso, Beto... mais forte, mais firme. Eu quero sentir todo o seu desejo."



    "b: Desculpa, Mel... eu não estou conseguindo..."

    "mc: Não se preocupa, Beto... só continue tentando. Eu sei que você pode fazer melhor."



    "mc (Pensamento): Ele está tentando... mas será que ele vai conseguir me satisfazer?"



    "b: Eu... eu não sei o que fazer, Mel..."

    "mc: Tudo bem, Beto... talvez precisamos tentar algo diferente. Eu só quero que você se sinta confortável."



    "mc (Pensamento): Será que o Léo seria capaz de me satisfazer dessa forma?"

    "mc: Porra, Beto... me come com força, porra!"



    "b: Eu... eu tô tentando, Mel, mas tá difícil..."



    "mc (Pensamento): Porra, ele ainda não tá pegando o jeito... Preciso de mais."

    "mc: Vai, caralho, me fode como você sabe, porra!"



    "b: Desculpa, Mel... eu não tô conseguindo..."

    "mc: Merda, Beto! Eu tô molhada pra caralho e você tá me deixando na mão!"



    "mc (Pensamento): Porra, ele precisa me satisfazer... Mas tá foda."

    "mc: Fode, porra! Eu quero sentir seu pau fundo dentro de mim!"



    "b: Eu... eu não sei o que fazer, Mel..."

    "mc: Caralho, Beto! Seu pau é uma merda? Vai, caralho, me dá o que eu preciso!"



    "mc (Pensamento): Puta merda, será que o Léo seria capaz de me satisfazer dessa forma?"

    "mc: Porra, Beto, você tá me deixando na mão de novo? Que porra é essa?"

    "b: Desculpa, Mel... Eu tô tentando, mas tá difícil."

    "mc: Porra, Beto, você quer que eu ache outro pau pra fazer o serviço direito?"

    "b: Não, não, Mel... Eu só... Eu tô tentando."

    "mc: Merda, Beto! Eu tô toda molhada aqui e você tá me deixando na mão."

    "b: Desculpa, Mel... Eu vou tentar de novo."

    "mc: Caralho, Beto, me fode direito! Eu quero sentir seu pau bem fundo em mim."

    "b: Eu... Eu não sei o que tá acontecendo, Mel..."

    "mc: Foda-se, Beto! Eu preciso gozar e você tá me enrolando."

    "b: Desculpa, Mel... Eu só... Eu tô tentando, tá?"

    "mc: Seu pau é uma merda? Vai, caralho, me dá o que eu preciso!"

    "b: Eu vou tentar de novo, Mel... Eu prometo."

    "mc: Faz isso, porra, antes que eu ache alguém que saiba como me satisfazer de verdade!"

    "mc: Porra, imagina se fosse o Léo aqui... Ele ia me fazer gozar tão gostoso."

    "b: Mel, eu..."

    "mc: Cala a boca, Beto! Eu tô pensando em coisas melhores agora."

    "b: Desculpa, Mel... Eu vou tentar fazer melhor."

    "mc (Pensamento): Puta merda, se fosse o Léo aqui... Ele tem aquela pegada forte, eu me imagino entregue a ele, completamente submissa. Será que ele saberia me fazer gozar como eu preciso? Porra, só de pensar naquele pau dele... Tão grosso, tão duro, pronto para me foder do jeito que eu gosto. Caralho, eu tenho certeza de que ele faria um trabalho muito melhor do que o Beto está fazendo. Eu seria completamente dele, à mercê de seus caprichos. Porra, eu não aguento mais essa frustração... Preciso sentir o prazer que só o Léo poderia me proporcionar."

    "b: Merda, Mel... Eu não vou aguentar..."

    "mc: Vai, caralho, goza pra mim... Eu quero ver você explodir."



    "b: Desculpa, Mel... Eu não consegui segurar..."

    "mc: Foda-se, Beto... Pelo menos alguém está gozando hoje."



    "mc: Eu preciso de alguém que saiba me foder direito... Será que o Léo faria um trabalho melhor do que você?"



    "b: Por que você continua falando sobre o Léo?"

    "mc: Porque ele sabe como me fazer gozar, porra. E você está me deixando na mão."







    "Vamos, Beto, me agarre com força, me faça sentir toda essa luxúria queimando dentro de você."
    "Não se segure, Beto, me possua com toda a sua força, me faça gritar de prazer até os vidros do mercado tremerem."
    "Eu sei que você pode ser mais selvagem, mais dominador, então me mostre do que é capaz, me faça implorar por mais."
    "Não tenha medo de me deixar marcas, Beto, eu quero sentir o calor das suas mãos em mim, me marcando como sua para sempre."
    "Agora é a sua vez de tomar as rédeas, Beto, então me faça sua, me faça sentir que pertenço a você e a mais ninguém."
    "Não pare agora, Beto, estamos só começando, então me leve ao limite e além, até eu não conseguir mais pensar em nada além de você."
    "Quero sentir seu desejo queimando em mim, Beto, então me faça sua de uma vez por todas, me faça sua escrava do prazer."
    "Não se preocupe comigo, Beto, eu posso aguentar, então me dê tudo o que você tem, me faça perder o controle e me entregar completamente a você."
    "Seja o macho alfa que sei que você pode ser, Beto, me domine, me faça sua de corpo e alma, me faça sua única e verdadeira obsessão."
    "Eu sei que você pode me levar ao paraíso, Beto, então me leve lá, me faça sentir como se estivéssemos voando juntos em uma nuvem de prazer e êxtase."

    "Vem, Beto, mostra quem manda aqui, me fazendo sentir cada centímetro desse corpo delicioso dentro de mim."
    "Não enrola, Beto, me dá com força, me fazendo gemer alto e claro até todos no mercado saberem quem está te fodendo."
    "Me usa como sua putinha, Beto, me fazendo implorar por mais da sua vara dura e grossa."
    "Sua pegada é boa, Beto, mas quero que seja mais rude, mais animal, me fazendo gritar de tanto prazer."
    "Aqui não tem essa de segurar, Beto, me come como se fosse a última foda da sua vida, me fazendo gozar como uma cadela no cio."
    "Quero sentir você me preenchendo por completo, Beto, me esticando até o limite, me fazendo sentir cada centímetro da sua rola pulsando dentro de mim."
    "Não para, Beto, me fode como se não houvesse amanhã, me fazendo delirar de tanto tesão até eu não aguentar mais."
    "Não precisa ser delicado, Beto, eu gosto é bruto, me fazendo sentir cada estocada como um soco de prazer direto no meu corpo."
    "Não segura a onda, Beto, me fode com força, me fazendo gritar e gemer até os vidros do mercado tremerem."
    "Me faz sentir seu macho, Beto, me possuindo como se fosse a única coisa que importa, me fazendo gozar como uma louca em cima da sua pica."
    "Isso, Beto, não para agora, me come até eu gritar teu nome e tremer de tanto gozar!"
    "Beto, sua pica é tão gostosa, me arromba com força e me faz sentir toda a tua virilidade."
    "Me faz tua, Beto, me mostra como é que se fode de verdade, me fazendo gemer e suar feito uma cadela no cio."
    "Não enrola, Beto, me come com vontade, me fazendo delirar de tanto tesão até eu não conseguir mais andar direito."
    "Quero sentir tua língua me chupando gostoso, Beto, me fazendo gozar na tua boca como uma puta sedenta por prazer."
    "Beto, me faz tua putinha, me come com força e me faz gritar até todos no mercado saberem quem é o macho que tá me arregaçando."
    "Não tem essa de ser gentil, Beto, me fode como se não houvesse amanhã, me fazendo rebolar feito uma vadia no teu pau duro e grosso."
    "Quero sentir teus dedos me penetrando, Beto, me fazendo gemer e implorar por mais até eu não aguentar mais."
    "Beto, me faz sentir teu macho alfa, me dominando e me fazendo gozar como uma louca em cima do teu corpo suado de tesão."

    "Não para agora, Beto, me come até eu perder as contas de quantos orgasmos tive, me fazendo sentir como uma verdadeira deusa do sexo."
    "Beto, me fode forte e me faz gozar como nunca, me fazendo gritar de prazer e te implorar por mais até eu não aguentar mais."
    "Quero sentir teu pau me arrombando, Beto, me fazendo sentir cada centímetro até o fundo da minha alma, me levando ao limite do prazer."
    "Não segura a onda, Beto, me come com força e me faz gemer alto até eu perder a voz de tanto gritar teu nome de prazer."
    "Beto, me come de jeito, me fazendo delirar de tanto tesão e me levando ao paraíso do prazer em uma explosão de orgasmos."
    "Quero sentir teus lábios me chupando inteira, Beto, me fazendo gemer e contorcer de tanto desejo até eu gozar na tua boca como uma vadia faminta."

    "Não para agora, Beto, me come até eu perder as forças nas pernas e tremer feito gelatina de tanto prazer que você me proporciona."
    "Beto, me fode como um animal, me fazendo sentir toda a tua ferocidade e me levando ao êxtase absoluto em uma onda de prazer."
    "Quero sentir tua mão me batendo gostoso, Beto, me fazendo sentir a dor misturada com o prazer até eu gozar como uma verdadeira putinha."
    "Não tem essa de ser meigo, Beto, me come como um verdadeiro macho, me fazendo gemer e implorar por mais até eu perder a noção de tempo."
    "Beto, me come com força e me faz gozar como nunca, me levando ao ápice do prazer e me deixando extasiada de tanto tesão que você me proporciona."

    "Vem logo, Beto, não seja tímido, quero que me agarre com força, que me faça sua de uma vez por todas."
    "Sua hesitação está me deixando louca, Beto, me faça sentir desejada, me use como sua putinha e me faça implorar por mais."
    "Não tenha medo de me tocar, Beto, quero que meus gemidos sejam um lembrete constante do quanto estou gostando disso."
    "Venha, Beto, me pega como se eu fosse sua presa, me use, abuse, me faça sentir toda a sua luxúria e desejo."
    "Quero que meus gemidos de prazer ecoem por todo o mercado, Beto, me faça sentir viva, me faça gritar seu nome enquanto você me possui."
    "Não pare agora, Beto, quero que meus gemidos sejam a trilha sonora da nossa transa, me faça delirar de tanto tesão."

    "Venha me dominar, Beto, me faça sua escrava do prazer, me use para satisfazer todos os seus desejos mais profundos."
    "Chega de joguinhos, Beto, quero que me possua com toda a sua força, me faça sentir o poder que você tem sobre mim, me deixe completamente submissa ao seu prazer."

    "Oh, Beto, isso, exatamente assim... ah... eu vou gozar, vou gozar tão gostoso pra você..."
    "Ahh, Beto, mais... mais forte... eu tô quase lá, só falta mais um pouquinho..."
    "Isso, isso, isso, Beto... me faz gozar... me faz gozar como só você sabe fazer..."
    "Beto, eu... eu tô quase lá, eu vou... eu vou gozar... ahhh!"
    "Oh, sim, Beto... me faz gozar, me faz gozar gostoso... eu tô quase lá..."
    "Beto, seu safado... eu vou... eu vou gozar... ahhh... isso... isso..."
    "Ahhh, Beto... eu tô chegando lá... mais... mais... eu vou gozar..."
    "Beto, não para... não para... eu tô quase lá... eu vou gozar... ohhh..."
    "Mais forte, Beto... mais... eu tô tão perto... eu vou gozar... ah..."
    "Ahhh, Beto... isso, isso... eu vou gozar... ahh... sim... sim..."




    "Mel, eu... eu acho que não consigo continuar... tá demais pra mim, tá indo rápido demais."
    "Eu... eu tô me sentindo meio sufocado, Mel, acho que é melhor a gente parar um pouco..."
    "Mel, eu tô meio desconfortável com isso tudo, acho que a gente devia dar um tempo..."
    "Eu... eu não quero te decepcionar, Mel, mas acho que a gente tá indo longe demais..."
    "Eu sei que a gente tava se divertindo, Mel, mas agora... agora eu tô me sentindo meio fora de lugar..."

    "Mel, eu... eu não quero que você pense que eu não tô curtindo, mas tá indo rápido demais pra mim..."
    "Eu sei que a gente tava se curtindo, Mel, mas agora eu tô me sentindo meio... sei lá, desconfortável..."
    "Eu não queria estragar o clima, Mel, mas acho que a gente devia parar um pouco... tá demais pra mim."



    "Beto, se você não começar a me satisfazer direito, vou ligar agora mesmo pro Leo e chamar ele aqui pra terminar o que você começou!"
    "Você acha que tá dando conta, Beto? Porque eu posso facilmente ligar pro Leo e dizer que você não tá aguentando o tranco..."
    "Sabe, Beto, o Leo sempre teve um jeito mais... confiante. Talvez eu devesse ligar pra ele, já que você parece estar tendo dificuldades..."
    "Parece que você tá meio perdido aí, Beto. Acho que eu deveria ligar pro Leo e ver se ele está disponível pra me satisfazer de verdade."
    "Beto, se você não começar a agir como um homem de verdade, vou chamar o Leo e deixar vocês dois se entenderem... ou melhor, me satisfazerem."
    "Estou começando a achar que você não é páreo pra mim, Beto. Talvez seja hora de chamar o Leo e ver se ele consegue me dar o que eu quero."
    "Sabe, Beto, o Leo sempre teve uma pegada mais forte. Talvez eu devesse chamá-lo e deixar você assistir enquanto ele me satisfaz como você nunca conseguiu."
    "Parece que você não tá dando conta do recado, Beto. Acho que vou ligar pro Leo e ver se ele consegue me dar o que você não tá conseguindo."
    "Você tá me deixando na mão, Beto. Acho que vou ligar pro Leo e ver se ele está disponível pra me dar tudo o que você não consegue."
    "Se você não começar a trepar direito comigo, Beto, vou chamar o Leo e ver se ele está disposto a me dar o que eu mereço, o que você não consegue me dar."



    "Olha só, Beto, parece que alguém aqui está gostando do que está vendo... você não consegue esconder o quanto está duro pra mim, não é?"
    "Hmm, sinto algo crescendo aí embaixo, Beto... parece que você tá gostando tanto quanto eu, hein?"
    "Uau, Beto, parece que o seu amigo aqui embaixo está pronto para a festa... e eu estou mais do que pronta para aproveitar."
    "Beto, não precisa ficar tímido... sei que você está gostando... olha só como seu pau está pulsando de desejo por mim..."
    "Parece que alguém está animadinho aqui embaixo, Beto... e eu adoro ver como você está reagindo ao meu toque."
    "Beto, você não precisa se esconder... sei que você está gostando... veja só como seu pau está duro para mim..."
    "Acho que o seu amigo aí embaixo está gostando do que vê, Beto... e eu mal posso esperar para brincar com ele um pouco mais..."
    "Não precisa ficar envergonhado, Beto... seu pau está me dizendo tudo o que eu preciso saber sobre como você está se sentindo..."
    "Uau, Beto, parece que o seu pau está animado para a festa... e eu estou pronta para dar a ele toda a atenção que merece."
    "Beto, seu pau não mente... e ele está me dizendo que você está tão excitado quanto eu... mal posso esperar para brincar com ele um pouco mais..."



    "Mel, eu tô fazendo certo? Você tá gostando?"
    "Você acha que tá bom assim, Mel? Eu quero te satisfazer ao máximo."
    "Estou fazendo do jeito certo, Mel? Eu quero que seja perfeito pra você."

    "Mel, isso tá bom pra você? Quero que seja incrível pra nós dois."
    "Você prefere de outro jeito, Mel? Eu faço do jeito que você quiser."
    "Tá doendo? Eu posso ir com mais cuidado, Mel."
    "Eu tô indo rápido demais? Quero que seja bom pra você, sempre."
    "Estou te machucando, Mel? Eu não quero te fazer mal."
    "Mel, me fala se tá tudo bem, se tá gostoso... eu só quero te fazer feliz."




    "Ah, caralho, Beto... continua assim que eu tô quase lá... tô quase gozando só de sentir você me segurando desse jeito."

    "Beto, sua pegada é incrível... tô quase gozando só de sentir suas mãos me apertando assim, me levando à loucura."
    "Ah, porra, Beto... assim que eu gosto... tô quase gozando só de sentir você me segurando desse jeito, me fazendo delirar de prazer."
    "Caralho, Beto, que pegada gostosa... tô quase gozando só de sentir suas mãos me apertando assim, me deixando maluca de tesão."
    "Isso, continua assim, Beto... tô quase lá... tô quase gozando só de sentir você me apertando desse jeito, me fazendo gemer de tanto prazer."

    "Porra, Beto, sua pegada é incrível... tô quase explodindo de tanto tesão, mal posso esperar pra gozar pra você."
    "Caralho, Beto, você sabe como me deixar louca... tô quase gozando só de sentir você me segurando assim, me fazendo gemer e implorar por mais."
    "Beto, seu corpo é uma delícia... mal posso esperar para sentir cada centímetro dele dentro de mim, me preenchendo, me fazendo gritar de prazer."
    "Ah, Beto, seus músculos... tão rígidos, tão definidos... me deixam louca de desejo, querendo te agarrar com toda a minha luxúria e te fazer meu."
    "Seu corpo é uma verdadeira obra de arte, Beto... mal posso esperar para explorar cada curva, cada recanto secreto enquanto nos entregamos a uma paixão avassaladora."
    "Eu amo a sensação da sua pele sob os meus dedos, Beto... é como se eu estivesse tocando o próprio pecado, me fazendo arder de desejo por você."
    "Ah, Beto, você é tão gostoso... tão perfeito... mal posso esperar para te saborear, te sentir dentro de mim, me levando ao paraíso do prazer."
    "Seu corpo é minha perdição, Beto... cada curva, cada músculo me faz querer te devorar com toda a minha sede de prazer, me faz querer te possuir até o fim dos tempos."
    "Beto, eu adoro como seu corpo se move contra o meu, como se encaixa perfeitamente, como se fôssemos feitos um para o outro, para nos entregar a essa paixão incontrolável que nos consome."
    "Seu corpo é um convite para o pecado, Beto... eu quero me perder nele, me entregar a essa luxúria que nos consome, nos domina, nos faz perder o controle e nos leva a um êxtase sem igual."
    "Cada vez que te toco, Beto, sinto meu corpo incendiar de desejo, ansiando por mais, mais da sua pele suada contra a minha, mais dos seus gemidos de prazer ecoando em meus ouvidos."
    "Você é tão intenso, Beto... tão ardente... mal posso esperar para me derreter em seus braços, me entregar a toda essa paixão que nos consome, nos une, nos faz um só."



    "Caralho, esse Beto sabe mesmo como me deixar louca de tesão... tô quase gozando só de sentir ele me pegando desse jeito, me fazendo arder de desejo."
    "Porra, que beijo é esse... tô me sentindo toda molhada, toda quente, como se eu fosse explodir de tanto tesão a qualquer momento."
    "Que delícia de pegada... esse Beto sabe como me fazer gemer de prazer, como me deixar alucinada por mais e mais desse fogo que queima dentro de mim."
    "Porra, esse Beto é foda... cada beijo, cada toque me deixa mais excitada, mais faminta por mais desse prazer selvagem que ele me oferece."
    "Putaqueopariu, esse beijo tá me deixando louca... tô molhadinha, toda arrepiada, implorando por mais dessa pegada gostosa que só o Beto sabe dar."
    "Que tesão do caralho... tô me sentindo nas nuvens, completamente entregue ao desejo, querendo me perder nesse fogo que arde entre nós."
    "Ah, caralho, esse Beto é um safado dos bons... cada toque dele me deixa alucinada, me fazendo gemer de prazer, pedindo por mais dessa loucura que a gente tá vivendo."
    "Que vontade de foder gostoso... esse Beto sabe mesmo como me fazer delirar de tesão, como me deixar louca por mais dessa pegada selvagem que ele tem."
    "Tô toda arrepiada, toda molhada... esse Beto é um perigo, me deixando completamente fora de controle, implorando por mais desse prazer que só ele sabe me dar."
    "Foda pra caralho... é assim que eu tô me sentindo, toda quente, toda excitada, querendo me jogar de cabeça nesse desejo insano que o Beto despertou em mim."




    "Beto tá me agarrando com uma pegada de macho, me deixando toda arrepiada, me fazendo sentir como se eu fosse derreter de tesão a qualquer momento."
    "Ele tá me beijando com uma intensidade que me deixa sem fôlego, me fazendo gemer de prazer a cada toque dos seus lábios nos meus."
    "Caralho, Beto tá me apertando com força, me fazendo sentir cada músculo do corpo dele contra o meu, me deixando louca de desejo por mais."
    "Beto tá me deixando toda molhada com esses beijos quentes, me fazendo sentir como se eu fosse explodir de tanto tesão a qualquer momento."
    "Ele tá me tocando de um jeito que me deixa fora de controle, me fazendo gemer de prazer, implorando por mais desse tesão que ele desperta em mim."
    "Porra, Beto tá me enlouquecendo com esses beijos, me fazendo sentir como se eu fosse perder a cabeça de tanto desejo, de tanto tesão."
    "Ele tá me provocando de um jeito que me deixa completamente submissa ao desejo, me fazendo implorar por mais desse prazer que ele me proporciona."
    "Caralho, Beto tá me pegando com tanta vontade, me fazendo delirar de tesão, me fazendo querer mais e mais desse fogo que arde entre nós."
    "Ele tá me deixando louca com esses beijos molhados, me fazendo sentir como se eu fosse explodir de tanto prazer a qualquer momento."
    "Porra, Beto tá me fazendo gemer de tanto tesão, me deixando completamente entregue a esse desejo que queima dentro de mim."





    "Porra, Beto tá me deixando louca de tesão... mal posso esperar para chupar esse pau gostoso e fazer ele gemer de prazer."
    "Putaqueopariu, ele tá me provocando tanto... tô louca pra sentar nessa vara e cavalgar até não aguentar mais."
    "Que vontade de morder esse pescoço gostoso dele e deixar marcas que vão fazer ele gemer o meu nome a noite toda."
    "Caralho, esse homem me deixa tão excitada... mal posso esperar para sentir ele me pegando com força, me fazendo implorar por mais."
    "Porra, eu quero sentir ele me chupando dos pés à cabeça, me fazendo delirar de prazer e implorar por mais."
    "Putamerda, eu quero sentir ele me comendo de quatro, me fazendo gritar de tesão e gozar como nunca antes."
    "Caralho, eu só consigo pensar em me ajoelhar na frente dele e engolir esse pau delicioso até ele me encher de porra quente."
    "Que vontade de fazer um 69 bem gostoso com ele, sentir a língua desse safado me enlouquecer enquanto eu retribuo cada chupada com uma gemida."
    "Porra, eu quero sentir ele me penetrando com força, me fazendo perder o controle e gozar como uma puta no cio."






    "Porra, tô sendo muito intensa? Foda-se, eu quero ele tanto... e o jeito como ele me toca, me beija, me deixa louca de desejo. Acho que o tesão que estamos compartilhando supera qualquer preocupação."
    "Será que tô passando dos limites? Cacete, eu sei que ele é todo tímido, mas quando sinto o calor do corpo dele contra o meu, quando ouço os gemidos de prazer que ele solta, parece que todas essas dúvidas desaparecem. O desejo fala mais alto, e eu não consigo resistir."
    "Caramba, tô sendo muito impulsiva? Mas quando ele me olha com aqueles olhos cheios de desejo, quando sinto suas mãos ávidas explorando cada curva do meu corpo, tudo o que eu consigo pensar é em como quero mais, como esse prazer vale qualquer risco."
    "Será que tô forçando demais a barra? Mas quando ele me beija com tanto desejo, quando me toca com tanta vontade, todas as minhas dúvidas desaparecem. O prazer que ele me proporciona é tão intenso, tão alucinante, que eu sei que vale a pena cada segundo."
    "Putz, tô indo rápido demais? Mas quando sinto o calor do seu corpo contra o meu, quando ouço seus gemidos de prazer ecoando no ar, toda essa hesitação some. O prazer que ele me dá é tão intenso, tão arrebatador, que eu não posso deixar de me entregar a ele."
    "Será que tô sendo injusta com ele? Mas quando sinto suas mãos ávidas explorando cada parte do meu corpo, quando o vejo gemendo de prazer sob meus toques, todas as minhas preocupações desaparecem. O que importa é o prazer que estamos compartilhando, o êxtase que estamos alcançando juntos."
    "Caramba, tô exagerando? Mas quando sinto o desejo queimando entre nós, quando vejo o quanto ele se entrega ao prazer, todas as minhas dúvidas se dissipam. O que importa é a paixão que estamos vivendo agora, o tesão que nos consome e nos une de uma forma única."
    "Será que tô sendo egoísta? Mas quando o vejo gemendo de prazer sob meus toques, quando sinto o calor do seu corpo contra o meu, todas as minhas dúvidas desaparecem. O que importa é o prazer que estamos compartilhando, a conexão que estamos construindo através do desejo."
    "Putz, será que tô indo rápido demais pra ele? Mas quando o sinto dentro de mim, me preenchendo por completo, todas as minhas dúvidas desaparecem. O prazer que ele me dá é tão intenso, tão arrebatador, que eu sei que vale a pena cada segundo, cada gemido, cada suspiro de êxtase que compartilhamos juntos."

    "Será que tô indo rápido demais com ele? O cara é tão tímido, não quero assustar o coitado."
    "Porra, tô sendo muito intensa? Acho que preciso maneirar um pouco, não quero deixar o Beto desconfortável."
    "Será que tô passando dos limites? Melhor ir com calma, não quero que ele se sinta pressionado."
    "Caramba, tô sendo muito impulsiva? Acho que preciso dar um passo para trás e deixar o Beto se sentir mais à vontade."
    "Será que tô forçando demais a barra? Acho que preciso dar um tempo e deixar as coisas fluírem naturalmente."
    "Putz, tô indo rápido demais? Talvez seja melhor dar um tempinho e ver como o Beto se sente em relação a tudo isso."
    "Será que tô sendo injusta com ele? Acho que preciso me controlar um pouco e dar mais espaço para o Beto."
    "Caramba, tô exagerando? Melhor ir com mais calma e ver como o Beto está lidando com toda essa situação."
    "Será que tô sendo egoísta? Acho que devo levar mais em conta os sentimentos do Beto e não só os meus desejos."
    "Putz, será que tô indo rápido demais pra ele? Acho que é melhor dar um passo para trás e garantir que o Beto esteja confortável com tudo isso."


    "Oh, Beto, você me deixa tão louca de desejo, mal posso esperar para sentir você me tocando."

    "Eu quero sentir suas mãos percorrendo meu corpo, me deixando em chamas de desejo por você."
    "Não segure seus desejos, Beto, me mostre o quanto você me quer, me possua com todo o seu desejo."
    "Cada vez que você me olha desse jeito, eu só consigo pensar em você me devorando com seu desejo."
    "Seu toque é como fogo em minha pele, queimando de desejo por mais."
    "Você desperta um fogo dentro de mim que não pode ser apagado, Beto, e eu quero queimar com você."
    "Eu me derreto toda quando você me toca assim, com tanta intensidade e paixão."
    "Quero sentir você me possuindo, me fazendo sua em cada respiração, em cada gemido de prazer."
    "Beto, você é a personificação dos meus desejos mais secretos, e eu quero explorar cada um deles com você."
    "Beto, mostre-me o seu lado mais selvagem, deixe-me ver o animal que há dentro de você."
    "Eu quero que você me agarre com força, me faça sentir que você é o homem que sabe o que quer."
    "Me tome com toda a sua masculinidade, me faça sua de uma vez por todas."
    "Sinta o poder que você tem sobre mim, Beto, e use-o para me dominar, me possuir completamente."
    "Quero que você me mostre quem manda aqui, que você é o macho alfa que eu tanto desejo."
    "Não tenha medo de mostrar sua força, Beto, eu quero sentir você me dominando com todo o seu vigor."
    "Mostre-me que você é capaz de me levar ao limite, de me fazer implorar por mais do seu toque dominador."
    "Eu quero ser sua presa, Beto, e quero que você me caçe com toda a sua fome de prazer."
    "Deixe-me sentir o peso do seu corpo sobre o meu, me fazendo sentir toda a sua virilidade."
    "Beto, mostre-me o quão poderoso você pode ser, me faça sentir sua força e sua determinação em me possuir."
    "Oh, Beto, seus gemidos são como música para os meus ouvidos, me enlouquecendo de desejo."
    "Cada gemido seu é uma prova do prazer que eu posso te proporcionar, e isso me deixa ainda mais excitada."
    "Seu gemido rouco me diz que estou fazendo tudo certo, que estou te levando ao ápice do prazer."
    "Quando você geme assim, Beto, eu sinto que tenho o controle total sobre seu corpo, e isso me deixa ainda mais excitada."
    "Eu adoro ouvir seus gemidos de prazer, Beto, eles me fazem querer te dar ainda mais prazer."
    "Cada gemido seu me deixa mais faminta por você, mais determinada a te levar ao máximo do êxtase."
    "Seus gemidos são como um afrodisíaco para mim, Beto, me deixando ainda mais excitada e sedenta por você."
    "Não pare de gemer, Beto, eu adoro ouvir sua voz carregada de prazer enquanto você se entrega ao nosso momento."
    "Seus gemidos me dizem que você está gostando tanto quanto eu, que está se entregando completamente ao nosso prazer."
    "Quanto mais você geme, mais eu sinto que estou te levando ao paraíso do prazer, Beto, e isso me deixa louca de desejo por você."
    "Melissa, eu... eu não sei se estou fazendo isso certo, mas... Deus, você é tão incrível."
    "Eu me sinto meio perdido aqui, Melissa, mas com você ao meu lado, sinto que posso descobrir tudo."
    "Não sei como fazer isso, Melissa, mas... quero aprender com você, quero te dar prazer como você merece."
    "Às vezes me sinto inseguro, Melissa, mas quando estou com você, sinto que posso ser quem eu realmente sou."
    "Melissa, eu não sei se sou bom nisso, mas quero tentar... quero te dar tudo o que você merece."
    "Sinto como se estivesse em território desconhecido, Melissa, mas você me faz sentir seguro o suficiente para explorar."
    "Não sei se estou à altura do que você espera, Melissa, mas vou me esforçar para te fazer feliz."
    "Às vezes sinto que não sei o que estou fazendo, Melissa, mas quando estou com você, tudo parece se encaixar."
    "Tenho medo de te decepcionar, Melissa, mas prometo que vou dar o meu melhor para te satisfazer."
    "Mesmo incerto do que estou fazendo, Melissa, uma coisa é certa: quero te fazer sentir especial, querida e amada."
    "Beto, seu corpo é uma tentação irresistível, cada curva, cada músculo me faz ansiar por você ainda mais."
    "Sua pele contra a minha é como fogo e gelo se encontrando, e eu quero me queimar em seu calor, sentir cada centímetro do seu corpo."
    "Cada vez que vejo seu membro pulsando de desejo por mim, meu corpo inteiro se incendeia, desejando tê-lo dentro de mim."
    "Beto, o cheiro da sua pele é como um afrodisíaco para mim, me deixando louca de desejo, ansiando por mais de você."
    "Quando você se aproxima, sinto o aroma do seu desejo, e isso só aumenta minha ânsia de tê-lo completamente."
    "Seu membro, pulsante e pronto para me possuir, é a prova viva do quanto você me deseja, e isso só aumenta minha luxúria por você."
    "Cada vez que sinto seu corpo contra o meu, Beto, desejo me perder na sua essência, no calor da sua pele, na sua paixão incontrolável por mim."
    "Seu corpo é como uma escultura de prazer, Beto, esculpido para me levar à loucura, para me fazer implorar por mais."
    "O jeito como seu membro late de desejo por mim me deixa sem fôlego, ansiando por senti-lo dentro de mim, preenchendo-me completamente."
    "Beto, você é uma visão de desejo encarnado, cada parte do seu corpo é uma tentação que eu não posso resistir, um convite para me entregar ao nosso prazer sem limites."



    mc "Oi, Beto. Pronto para a aula de hoje?"

    b "A-aula? Q-que aula?"

    mc "Sua aula de como conquistar garotas, é claro!"

    b "A-ah... s-sim..."

    mc "Então, vamos começar. Hoje, eu quero que você pratique comigo."

    b "C-com você?"

    mc "Sim. Eu vou ser a garota que você está tentando conquistar. E você vai ter que flertar comigo."

    b "M-mas... eu não sei como fazer isso."

    mc "Eu vou te ajudar. Só relaxa e seja você mesmo."

    b "T-tá bom..."

    b "[mc]... você... você está muito bonita hoje."

    mc "Obrigada, Beto. Você também está muito bonito."

    b "E-eu?"

    mc "Sim. Você tem um sorriso lindo."

    b "A-ah... obrigado..."

    mc "E seus olhos também são lindos"

    b "V-verdade?"

    mc "Sim. Você é um cara muito bonito, Beto. E você também é inteligente, engraçado e gentil. Qualquer garota teria sorte de ter você."

    b "A-ah... [mc]... eu... eu não sei o que dizer..."

    mc "Você não precisa dizer nada. Só continue sendo você mesmo. E confie em mim, você vai conquistar a garota dos seus sonhos."

    b "E-eu... eu espero que sim..."

    mc "Beto... eu..."

    le "E aí, Beto! Tá tudo bem?"

    b "A-ah... Léo! S-sim, tá tudo bem..."

    le "Quem é essa gata?"

    b "E-essa é a [mc]..."

    le "Prazer, [mc]. Eu sou o Léo, amigo do Beto."

    mc "Prazer, Léo."

    le "Então, Beto, você tava flertando com a [mc]?"

    b "Q-quê?! N-não! Claro que não!"

    le "Haha! Tá bom, tá bom. Eu acredito em você."

    le "A gente se vê, [mc]."

    mc "Até mais, Léo."

    mc "Então... onde a gente tava?"

    b "E-eu... eu não sei..."

    mc "Eu acho que você tava me elogiando."

    b "S-sim... eu... eu acho que você é a garota mais linda que eu já vi."

    mc "Ai, Beto..."

    mc "Hmmm..."

    b "A-ah..."

    mc "Eu acho que você está aprendendo direitinho."

    b "E-eu... eu acho que sim..."



    mc "Oi, Beto. Pronto para a aula de hoje?"

    b "O-oi, [mc]. S-sim, eu acho..."

    mc "Ótimo! Então vamos continuar de onde paramos. Você estava me elogiando."

    b "S-sim... eu... eu disse que você é a garota mais linda que eu já vi."

    mc "E eu disse que você também é muito bonito."

    b "V-verdade?"

    mc "Sim. E eu também gosto do seu sorriso."

    b "O-obrigado..."

    mc "Então, continue. O que mais você pode me dizer?"

    b "Eu... eu gosto do seu jeito. Você é... você é diferente."

    mc "Diferente como?"

    b "Você é... você é forte, independente e... e você não tem medo de ser você mesma."

    mc "Ai, Beto... você é tão fofo."

    mc "Você está aprendendo direitinho."

    b "E-eu... eu acho que sim..."

    mc "Então, continue me elogiando. O que mais você gosta em mim?"

    b "Eu... eu gosto do seu cabelo. Ele é tão... tão bonito."

    mc "Obrigada, Beto. Eu gosto do seu cabelo também. Ele é tão macio."

    b "V-verdade?"

    mc "Sim. E eu também gosto do seu estilo. Você se veste muito bem."

    b "O-obrigado... eu... eu tento."

    mc "Você está indo muito bem, Beto. Continue assim."

    mc "Beto, eu acho que você está pronto para convidar uma garota para sair."

    b "S-sério?"

    mc "Sim. Você tem tudo o que é preciso. Você é bonito, inteligente, engraçado e gentil. E agora você também está confiante."

    b "E-eu... eu não sei..."

    mc "Confie em mim, Beto. Você vai conseguir."

    b "T-tá bom... eu vou tentar."

    b "[mc], você... você gostaria de sair comigo?"

    mc "Eu... eu adoraria."

    b "Ó-ótimo! E-então... o que você acha de irmos ao cinema no sábado?"

    mc "Eu adoraria."

    b "E-então... está combinado!"



    mc "Oi, Beto. Como foi seu encontro com a Lúcia?"

    b "A-ah... foi... foi bom."

    mc "Só bom?"

    b "É... eu... eu não sei. Eu acho que ela não gostou muito de mim."

    mc "Por que você acha isso?"

    b "Ela... ela não parecia muito interessada em mim. Ela ficava olhando para o celular o tempo todo."

    mc "Hmm... talvez ela estivesse nervosa. Ou talvez ela não seja a garota certa para você."

    b "É... talvez..."

    b "[mc]... eu... eu queria te pedir uma coisa."

    mc "O quê?"

    b "Você... você pode continuar me dando aulas?"

    mc "Aulas? Mas... você já sabe como conquistar garotas."

    b "Eu sei... mas... eu gosto das aulas. É... é um momento que eu tenho com você."

    mc "Beto..."

    b "Eu... eu sei que você gosta do Gabriel. E... e eu não quero atrapalhar. Mas... eu só queria poder passar mais tempo com você."

    mc "Beto, eu... eu também gosto de passar tempo com você. E... eu gosto dos seus elogios."

    b "V-verdade?"

    mc "Sim. Você me faz sentir... especial."

    b "A-ah... [mc]..."

    mc "Então... você quer continuar com as aulas?"

    b "S-sim! Por favor!"

    mc "Tá bom. Eu vou continuar te dando aulas."

    b "O-obrigado, [mc]! Você é a melhor!"



    mc "Oi, Beto. Pronto para a aula de hoje?"

    b "O-oi, [mc]. S-sim, eu estou."

    mc "Então, vamos começar. O que você quer aprender hoje?"

    b "Eu... eu quero aprender a como... como elogiar uma garota."

    mc "Ótimo! Elogiar uma garota é uma ótima maneira de mostrar que você está interessado nela. Mas é importante ser sincero e específico."

    b "S-sincero e específico?"

    mc "Sim. Não diga apenas que ela é bonita. Diga o que você acha bonito nela. Por exemplo, você pode elogiar o cabelo dela, os olhos dela, o sorriso dela, o estilo dela..."

    b "E-entendi..."

    mc "Então, vamos praticar. Me elogie."

    b "O-ok... [mc], você... você tem um sorriso lindo."

    mc "Obrigada, Beto. Isso foi muito bom."

    b "E-eu... eu também gosto do seu cabelo. Ele é tão... tão brilhante."

    mc "Obrigada. Eu gosto do seu cabelo também. Ele é tão macio."

    mc "Você está indo muito bem, Beto. Agora, me conte sobre a Lúcia. Quem é ela? O que ela faz?"

    b "A Lúcia... ela é uma garota que eu conheci na faculdade. Ela é muito bonita e inteligente. Ela está estudando para ser médica."

    mc "Uau! Ela parece ser incrível."

    b "É... sim. Mas... eu não sei. Eu acho que ela não está interessada em mim."

    mc "Por que você acha isso?"

    b "Ela... ela não parece muito interessada em mim. Ela ficava olhando para o celular o tempo todo."

    mc "Hmm... talvez ela estivesse nervosa. Ou talvez ela não seja a garota certa para você."

    b "É... talvez..."

    mc "Beto, você não precisa se preocupar com a Lúcia. Você é um cara incrível. Você vai encontrar a garota certa para você."

    b "O-obrigado, [mc]. Você sempre sabe como me fazer sentir melhor."

    mc "Eu... eu gosto muito de você, Beto."

    b "E-eu também gosto muito de você, [mc]."

    mc "Eu acho que você está pronto para conquistar qualquer garota."

    b "E-eu... eu também acho."























































































    mc "Oi, Beto."

    b "O-oi, [mc]."

    mc "Beto, você pode me contar mais sobre sua relação com seu pai?"

    b "Meu pai... ele sempre foi muito rígido. Ele sempre cuidou da casa e da família, mas... ele nunca foi muito carinhoso."

    mc "Eu sinto muito, Beto."

    b "Obrigado, [mc]. Mas... agora que ele está doente, eu... eu sinto que preciso crescer. Eu preciso ser forte para ele."

    mc "E você é forte, Beto. Você é um dos caras mais fortes que eu conheço."

    b "V-você acha mesmo?"

    mc "Sim. Você está trabalhando duro para ajudar sua família. E você está enfrentando seus medos. Isso é muita força."

    b "Obrigado, [mc]. Você sempre sabe como me fazer sentir melhor."



    mc "Beto, me conta mais sobre seus irmãos mais velhos."

    b "O Lucas é advogado, e o Marcos é engenheiro. Eles são ambos muito inteligentes e bem-sucedidos."

    mc "Uau! Eles parecem ser incríveis."

    b "É... sim. Mas... a gente nunca foi muito próximo. Eles sempre me viram como o irmão mais novo e... meio bobo."

    mc "Eu sinto muito, Beto."

    b "Tudo bem. Eu já me acostumei. Mas... às vezes eu queria que eles me levassem mais a sério."

    mc "Você já tentou conversar com eles sobre isso?"

    b "Não... eu... eu tenho medo."

    mc "Medo de quê?"

    b "Medo de que eles... de que eles me rejeitem."

    mc "Beto, você não pode ter medo de ser rejeitado. Se você quer ter um relacionamento melhor com seus irmãos, você precisa se arriscar."

    b "Você... você acha mesmo?"

    mc "Sim. E eu vou estar aqui para te ajudar."



    mc "Beto, você pode me contar mais sobre o Lucas?"

    b "O Lucas... ele é meu irmão mais velho. Ele é advogado e trabalha em um escritório de advocacia de grande porte na capital."

    mc "Uau! Ele parece ser bem-sucedido."

    b "É... sim. Ele sempre foi o filho favorito dos meus pais. Ele é muito inteligente e ambicioso."

    mc "E você se dá bem com ele?"

    b "Eu... eu não sei. A gente nunca foi muito próximo. Ele sempre me viu como o irmão mais novo e... meio bobo."

    mc "Eu sinto muito, Beto."

    b "Tudo bem. Eu já me acostumei. Mas... às vezes eu queria que ele me levasse mais a sério."

    mc "Eu tenho certeza que ele te ama, Beto. Ele só precisa de um tempo para perceber o quão incrível você é."



    mc "Beto, você pode me contar mais sobre o Marcos?"

    b "O Marcos... ele é meu segundo irmão mais velho. Ele é engenheiro e trabalha em uma grande construtora."

    mc "Uau! Ele também parece ser bem-sucedido."

    b "É... sim. Ele sempre foi o atleta da família. Ele é muito bom em tudo que faz."

    mc "E você se dá bem com ele?"

    b "Eu... eu não sei. A gente nunca foi muito próximo. Ele sempre foi muito competitivo, e eu nunca fui bom em esportes."

    mc "Mas você é bom em outras coisas, Beto. Você é inteligente, engraçado e gentil."

    b "V-você acha mesmo?"

    mc "Claro que sim! E eu tenho certeza que o Marcos te ama. Ele só precisa de um tempo para perceber o quão incrível você é."

    b "Obrigado, [mc]. Você sempre sabe como me fazer sentir melhor."

    b "Eu... eu gosto muito de você, [mc]."

    mc "Eu também gosto muito de você, Beto."



    mc "Beto, você pode me contar mais sobre a Ana?"

    b "A Ana... ela é minha irmã mais nova. Ela ainda está na escola, mas é muito inteligente e dedicada."

    mc "Ela parece ser incrível."

    b "Ela é. Ela é a minha melhor amiga."

    mc "Vocês são muito próximos?"

    b "Sim, muito. Eu sempre a protegi. Ela é como uma irmã mais nova para mim."

    mc "Eu entendo. Eu tenho uma prima que é como uma irmã para mim também."

    b "A Ana... ela é a única pessoa da minha família que apoia o nosso relacionamento."

    mc "Sério?"

    b "Sim. Ela acha que você é perfeita para mim."

    mc "Ai, que fofa! Eu preciso conhecê-la."

    b "Eu adoraria que vocês se conhecessem."

    b "Eu... eu tenho muita sorte de ter você na minha vida, [mc]."

    mc "Eu também tenho muita sorte de ter você, Beto."



    mc "Beto, eu... eu preciso te contar uma coisa."

    b "O que foi, [mc]?"

    mc "É sobre o seu Fernando."

    b "O que tem ele?"

    mc "Outro dia, ele me pediu para... para tomar um banho para ele."

    b "O quê?!"

    mc "Sim. Ele disse que... que eu o deixava feliz. E que ele queria me ajudar com o aluguel."

    b "E... e você fez?"

    mc "Eu... eu não sei. Uma parte de mim queria. Mas... outra parte de mim sabia que era errado."

    b "E o que você fez?"

    mc "Eu... eu recusei. Mas... eu não sei se fiz a coisa certa."

    b "[mc], você fez a coisa certa. O que o meu pai fez foi errado. Ele não deveria ter te pedido isso."

    mc "Mas... eu não sei. Eu... eu me sinto atraída por ele."

    b "O quê?!"

    mc "Eu sei que é errado. Mas... eu não consigo evitar. Ele me faz sentir coisas que eu nunca senti antes."

    b "[mc]... eu... eu não sei o que dizer."

    mc "Eu... eu sinto muito, Beto."



    mc "Beto, você já descobriu alguma coisa sobre o Sr. Fernando?"

    b "Eu... eu tentei perguntar ao Lucas sobre ele, mas... ele ficou bravo."

    mc "Bravo? Por quê?"

    b "Eu... eu não sei. Ele disse que era para eu não me meter nos negócios dele."

    mc "Hmm... isso é estranho."

    b "É... eu também achei."

    mc "Por que você acha que o Lucas ficou tão bravo?"

    b "Eu... eu não sei. Talvez... talvez ele esteja envolvido em algo com o Sr. Fernando."

    mc "É possível. O Sr. Silva também mencionou que o Sr. Fernando era um homem de negócios importante. E que ele tinha muitos contatos na prefeitura."

    b "Sério?"

    mc "Sim. E... eu me lembro de que o Sr. Fernando me disse que ele já trabalhou com o antigo prefeito."

    b "Hmm... isso é... preocupante."

    mc "Por quê?"

    b "Porque... o antigo prefeito era conhecido por ser... corrupto."

    mc "Você acha que o Sr. Fernando e o Lucas estão envolvidos em algum tipo de esquema de corrupção?"

    b "Eu... eu não sei. Mas é possível."

    mc "A gente precisa investigar."

    b "Mas... como?"

    mc "Eu não sei. Mas a gente precisa descobrir a verdade."



    mc "Oi, Beto."

    b "O-oi, [mc]. T-tudo bem?"

    mc "Sim, e com você?"

    b "T-tô bem..."

    mc "Sabe, Beto, eu... eu preciso conversar com alguém."

    b "C-comigo?"

    mc "Sim. Você é meu amigo. E eu confio em você."

    b "O-ok... o que você quer falar?"

    mc "É que... outro dia, eu fui ao cinema com o Gabriel."

    b "C-com o Gabriel?"

    mc "Sim. E... no meio do filme, ele... ele me beijou."

    b "E-ele te beijou?!"

    mc "Sim. E... eu... eu gostei."

    b "V-você gostou?"

    mc "Sim. Mas... eu não sei o que fazer. Eu... eu também me sinto atraída pelo pai dele."

    b "P-pelo pai dele?!"

    mc "Sim. Eu sei que é errado. Mas... eu não consigo evitar. Ele me faz sentir coisas que eu nunca senti antes."

    b "M-mas... e o Gabriel?"

    mc "Eu não quero machucar ele. Mas... eu não sei o que fazer."

    b "[mc]... eu... eu não sei o que te dizer. Mas... eu acho que você precisa seguir seu coração."

    mc "Meu coração? Mas... e se eu acabar magoando alguém?"

    b "É um risco que você precisa correr. Se você não seguir seu coração, você pode acabar se arrependendo."

    mc "Você... você acha mesmo?"

    b "Sim. Eu... eu sei como é gostar de alguém e não saber o que fazer."

    mc "Beto..."

    b "Eu... eu sempre vou estar aqui pra você, [mc]. Não importa o que aconteça."

    mc "Obrigada, Beto. Você é um ótimo amigo."

    b "D-de nada, [mc]."

    mc "Eu... eu vou pensar no que você disse."

    b "Tá bom. E... se você precisar de qualquer coisa... eu tô aqui."

    mc "Obrigada, Beto. Você é o melhor."

    mc "Eu vou indo. Até mais."

    b "A-até mais, [mc]."

    b "[mc]... eu... eu te amo."

label tarado_textos:



    ta "Mel, suas coxas são tão gostosas que eu mal consigo me controlar."

    ta "Quando eu te pegar, vou segurar suas coxas com tanta força que você vai implorar por mais."

    ta "Quando eu te jogar na cama, suas coxas vão ficar abertas para mim, implorando para serem tocadas."
    ta "Mel, suas coxas são como um convite para o paraíso do prazer, e eu vou te levar lá."

    ta "Quando eu passar minhas mãos por suas coxas, você vai sentir o calor do meu desejo, queimando por você."
    ta "Quando eu finalmente te pegar, Mel, suas coxas vão tremer de prazer sob meu toque intenso."
    ta "Suas coxas são minha obsessão, Mel, e eu vou fazê-las implorar por mais, uma e outra vez."




    ta "Vou segurar suas coxas com tanta força que você vai sentir cada centímetro do meu pau te arrombando."

    ta "Mel, suas coxas são a chave para o paraíso, e eu vou te foder tão forte que você vai esquecer seu próprio nome."
    ta "Ah, suas coxas... elas me deixam com tanto tesão que eu mal consigo me segurar para não te rasgar com meu pau duro."


    ta "Quando eu te tiver em minhas mãos, suas coxas vão ser o palco para a mais intensa foda da sua vida, e eu vou te fazer implorar por mais."

    ta "Vou abrir suas pernas com força e te mostrar o que é um verdadeiro homem te fodendo."


    ta "Suas pernas vão tremer quando eu te segurar pelos tornozelos e te foder com tudo o que tenho."

    ta "Suas pernas vão estar tão abertas para mim que vou poder te fazer gozar só com a língua."


    ta "Vou deixar suas pernas bambas de tanto prazer, Mel, e você vai me agradecer por cada segundo disso."
    ta "Quando eu terminar com você, suas pernas vão estar tão fracas que você mal vai conseguir andar."


















    ta "Oh, você quer mais? Pois vou te dar mais do que você pode aguentar, sua vadia insaciável."
    ta "Vou te foder tão forte que você vai implorar para eu parar, mas eu não vou parar até você implorar por mais."
    ta "Quando eu terminar com você, você vai estar tão arrebentada que vai precisar de dias para se recuperar."


    ta "Você acha que pode me desafiar? Eu vou te dominar de uma maneira que você nunca vai esquecer."

    ta "Vou te usar como quiser, sem nenhum remorso, até que você esteja completamente entregue a mim."

    ta "Você achou que ia sair impune depois de me provocar? Vou te punir de uma maneira que vai te fazer pensar duas vezes antes de me desafiar novamente."



    ta "Ah, essa bunda... Mal posso esperar para apertá-la com força enquanto te fodo por trás."


    ta "Vou encher essa bunda gostosa com tanto tesão que você não vai conseguir se mexer."

    ta "Essa bunda vai ser minha para marcar e possuir como eu quiser, até você não conseguir sentar direito."

    ta "Quando eu te pegar, vou te segurar pelos quadris e te empurrar para baixo, até você gemer de prazer."

    ta "Você vai sentir cada estocada do meu pau na sua bunda e vai implorar por mais, como a putinha que é."

    ta "Vou bater nessa bunda até ela ficar vermelha e dolorida, só para ver você implorar por mais."

    ta "Vou te espancar com tanta força que você vai implorar para eu parar, mas eu não vou parar até eu me satisfazer."

    ta "Vou te fazer sentir a dor e o prazer ao mesmo tempo, te espancando enquanto te fodo sem dó."


    ta "Essa bunda vai ficar tão dolorida que você não vai conseguir sentar direito por semanas."
    ta "Vou te fazer implorar por misericórdia enquanto te espanco com minha mão, te mostrando quem manda aqui."
    ta "Quando eu terminar com você, sua bunda vai estar tão espancada que você vai se lembrar de mim cada vez que se olhar no espelho."



    ta "Ah, seus peitos... mal posso esperar para apertá-los com força enquanto te fodo."
    ta "Vou chupar esses peitos com tanta força que você vai implorar para eu parar."
    ta "Quando eu te tiver em minhas mãos, seus peitos vão ser meus brinquedos pessoais, e eu vou brincar com eles como quiser."


    ta "Quando eu terminar com você, seus peitos vão estar tão sensíveis que até o toque mais suave vai te fazer gemer de prazer."

    ta "Vou apertar esses peitos com tanta força que você vai sentir o calor do meu desejo queimando por você."
    ta "Esses peitos são minha obsessão, e eu vou fazê-los implorar por mais, uma e outra vez."
    ta "Quando eu te jogar na cama, seus peitos vão estar tão expostos para mim que vou poder chupá-los e mordê-los à vontade."

    ta "Vou morder esses peitos com tanta força que você vai gritar de dor e prazer ao mesmo tempo, sua vadia."

    ta "Esses peitos vão ser meus para esmagar e torcer até você implorar por misericórdia, sua putinha."

    ta "Vou espancar esses peitos até eles ficarem vermelhos e doloridos, só para ver você implorar por mais, sua vagabunda."
    ta "Esses peitos são só minhas propriedades agora, e eu vou usá-los como bem entender, sem dó nem piedade."

    ta "Seus peitos são tão suculentos que eu mal posso esperar para afundar meus dedos neles enquanto te como de todas as maneiras possíveis."
    ta "Esses peitos vão ser meus brinquedos pessoais, e eu vou brincar com eles até você não conseguir mais se segurar, sua puta."
    ta "Quando eu terminar com você, seus peitos vão estar tão arrebentados que você não vai conseguir nem olhar para eles sem se lembrar de mim, sua vadia."

    ta "Esses peitos vão ser o meu playground pessoal, onde vou explorar cada centímetro deles com minha língua e meus dentes."
    ta "Vou sugar seus mamilos com tanta voracidade que você vai sentir meu desejo pulsando através deles, sua puta."
    ta "Seus peitos são tão convidativos que eu mal posso esperar para cobri-los com minha saliva e fazer você gemer de prazer."
    ta "Quando eu te tiver de joelhos, seus peitos vão balançar na minha frente, implorando para serem chupados e apertados."
    ta "Esses peitos vão ser minha obsessão, e eu vou dedicar cada segundo a eles até você implorar por misericórdia, sua vadia insaciável."
    ta "Vou usar seus peitos como alças enquanto te fodo por trás, apertando-os com força até você gritar de prazer."
    ta "Seus peitos são tão perfeitos que eu vou fazer questão de cobri-los com minha porra quente, marcando-os como meus para sempre."
    ta "Vou fazer você se contorcer de prazer enquanto aperto seus peitos com força, fazendo você implorar por mais da minha luxúria."
    ta "Quando eu te tiver em meus braços, vou mergulhar meus lábios nesses peitos e chupar cada centímetro deles até você gritar meu nome."
    ta "Esses peitos são um convite para o paraíso, e eu vou te levar ao êxtase enquanto os devoro com minha paixão incontrolável."



    ta "Você, sua puta, vai se masturbar agora mesmo enquanto eu assisto, entendido?"
    ta "Não espere por permissão, sua vadia. Comece a se tocar agora e me mostre como você é obediente."
    ta "Eu quero ver você se contorcendo de prazer enquanto enfia os dedos na sua buceta molhada, sua cadela."
    ta "Nada de desculpas, sua puta. Se você não começar a se masturbar agora, eu mesmo vou te fazer implorar por isso."
    ta "Se você não quer uma surra, é melhor começar a se masturbar e gemer como a puta que você é."
    ta "Não seja uma idiota, sua vadia. Comece a se tocar agora mesmo ou vai se arrepender."
    ta "Eu quero ver você gozando para mim, sua puta. Então, comece a se masturbar até eu mandar parar."
    ta "Eu quero que você se masturbe até não aguentar mais, sua vagabunda. Eu quero ver você gozar para mim agora."
    ta "Não perca tempo, sua cadela. Se masturbe e me mostre o quão desesperada você está por mim."
    ta "Se você não começar a se tocar agora, vou ter que te punir de uma maneira que você não vai gostar, sua puta insubordinada."

    ta "Vou contar até três e se você ainda não estiver se masturbando, vai se arrepender, sua vadia. Um... dois... três! Agora!"
    ta "Não me faça repetir, sua puta. Comece a se tocar imediatamente ou vou ter que tomar medidas drásticas."
    ta "Se masturbe para mim, sua cadela no cio. Eu quero ver você gemendo de prazer enquanto se toca para mim."
    ta "Eu quero ver você gozar para mim agora mesmo, sua vadia insaciável. Então, não perca tempo e comece a se masturbar."
    ta "Você não tem escolha, sua puta. Se masturbe agora e prove que você é minha putinha obediente."
    ta "Nada de enrolação, sua vagabunda. Quero que você se toque com força e me mostre o quão desesperada está por mim."
    ta "Eu quero ouvir você gemendo enquanto se masturba para mim, sua cadela suja. Então, não me faça esperar."
    ta "Se você não começar a se tocar imediatamente, vou te punir de uma maneira que você jamais esquecerá, sua puta desobediente."
    ta "Se masturbe agora, sua vadia, e prove o quanto você precisa de mim para gozar como a puta que você é."
    ta "Eu não estou brincando, sua cadela. Se masturbe agora e prove que você merece ser minha."





    ta "Você é só uma vadia desesperada por atenção, não é?"

    ta "Quem você pensa que é, sua putinha barata?"


    ta "Eu vou te usar e te jogar fora como a vadia que você é."
    ta "Cadela, você merece ser tratada com brutalidade até aprender a respeitar os homens de verdade."

    ta "Você não passa de uma vadia faminta por atenção, ansiosa para ser usada e abusada."
    ta "Vou te mostrar quem manda aqui, sua cadela insolente. Prepare-se para ser tratada como merece."



    ta "Ah, sua putinha, gozando enquanto seu corno está do seu lado? Que delícia!"
    ta "Você é tão safada, se tocando enquanto seu namoradinho está tão perto, não é?"


    ta "Ah, eu adoro pensar que você está gozando enquanto seu namoradinho bobo está ao seu lado, sem saber de nada."

    ta "Sua safada, se tocando escondida, enquanto ele está tão próximo. Que tesão proibido, não é?"
    ta "Você é uma vadia insaciável, gozando enquanto seu namoradinho está aí, sem desconfiar de nada."
    ta "É tão excitante pensar que você está se tocando enquanto seu corno está tão próximo, sem ter a menor ideia."


    mc "Ah, por favor, não fale dele agora... Eu estou gozando tanto, tão gostoso, só pense em mim, seu tarado!"

    mc "Ah, não mencione ele agora... Estou gozando para você, só para você, seu tarado!"
    mc "Por favor, esqueça dele... Eu estou gozando tanto, tão forte, só pense em mim, seu safado!"
    mc "Ah, não quero saber dele agora... Estou gozando para você, só para você, seu tarado!"
    mc "Não estrague o momento, seu safado... Eu estou gozando tanto, tão delicioso, só pense em me fazer sentir bem!"
    mc "Por favor, não fale dele... Estou gozando tanto, tão intenso, só pense em me fazer gozar mais, seu tarado!"
    mc "Ah, não mencione ele agora... Estou gozando para você, só para você, seu safado!"
    mc "Não estrague o momento, seu tarado... Eu estou gozando tanto, tão delicioso, só pense em me dar prazer!"
    mc "Por favor, esqueça dele... Eu estou gozando para você, só para você, seu safado!"






    ta "Pode fingir que não está pedindo por isso, mas eu sei que você quer, sua cadela safada. Vou te usar até você não conseguir nem se lembrar do seu próprio nome."


    mc " Eu já vi gente como você antes e, spoiler alert, você não vai chegar nem perto de me tocar."
    ta "Sua língua afiada vai te colocar em problemas, cadela. "
    mc "Então me mostre, tarado. Mostre o quão patético você é tentando me intimidar. Eu não vou ceder ao seu joguinho sujo."



    " Porque, francamente, eu estou mais para dominadora do que para submissa."
    ta "Vadia, você merece ser tratada com brutalidade até aprender a respeitar os homens de verdade."
    mc "Brutalidade? Isso soa tão... tentador. Mas acho que você vai ter que se esforçar muito mais se quiser me mostrar quem manda de verdade."
    " apenas não tenho certeza se você é capaz de me dar o que eu realmente quero."
    ta "Vou te mostrar quem manda aqui, sua cadela insolente. Prepare-se para ser tratada como merece."
    mc "Uau, isso soa tão... sexy. Mas acho que eu só posso ser dominada por alguém que realmente saiba o que está fazendo. Você parece mais um cachorro latindo do que um verdadeiro dominador."




    mc "Está bem, eu aceito o desafio. Mas só se você conseguir me fazer sentir alguma coisa, seu tarado."

    mc "Se é isso que você quer, vamos fazer. Mas se você conseguir me deixar animada, eu vou dar o braço a torcer, seu tarado."
    mc "Aceito o desafio, seu tarado. Mas se você conseguir me deixar molhada, vou ter que admitir que você sabe como me excitar."
    mc "Tudo bem, vamos ver do que você é capaz, seu tarado. "
    mc "Se é isso que você quer, tarado, vamos fazer. Mas se você conseguir me fazer sentir algo, vou ter que te dar os parabéns."
    mc "Está bem, eu topo. "
    mc "Vamos ver o que você tem, tarado. Mas se você conseguir me deixar ofegante de tanto tesão, vou ter que admitir que você sabe como me excitar."
    mc "Aceito o desafio, seu tarado. Mas se você conseguir me fazer sentir alguma coisa, vou ter que te dar crédito por isso."

    mc "Tudo bem, vamos ver no que isso vai dar. Mas se você conseguir me fazer arrepiar, eu vou reconhecer que você tem seu charme, seu tarado."
    mc "Aceito o desafio, seu tarado. Mas só se você conseguir me deixar com um formigamento entre as pernas."
    mc "Vamos lá, tarado, mostre o que você tem. Se conseguir me deixar ansiosa por mais, eu vou ter que admitir que você tem seus truques."
    mc "Está bem, eu topo a brincadeira. Mas se você conseguir me deixar querendo mais, vou ter que dar o braço a torcer, seu tarado."
    mc "Se é assim que você quer jogar, vamos lá. Mas se você conseguir me fazer sentir alguma coisa, eu vou te dar os parabéns, seu tarado."
    mc "Tudo bem, vamos ver se você consegue me impressionar. Mas se você conseguir me fazer suspirar de desejo, eu vou ter que reconhecer seu talento, seu tarado."
    mc "Aceito o desafio, seu tarado. Mas se você conseguir me deixar com borboletas no estômago, vou ter que admitir que você tem seus méritos."
    mc "Vamos ver do que você é capaz, tarado. Mas se você conseguir me fazer perder o fôlego, eu vou ter que reconhecer que você tem seu charme."
    mc "Está bem, eu topo. Mas só se você conseguir me deixar com um sorriso bobo no rosto, seu tarado."
    mc "Se é isso que você quer, vamos fazer. Mas se você conseguir me fazer sentir algo especial, eu vou ter que te dar crédito por isso, seu tarado."



    mc "Isso é tudo que você tem? Eu estava esperando muito mais das suas provocações."
    mc "Hmm, suas palavras são tão fracas quanto suas investidas... eu esperava mais de alguém que se acha tão ousado."
    mc "Você prometeu tanto, mas no final, tudo o que você fez foi me deixar desapontada."
    mc "Suas tentativas foram tão patéticas que mal conseguiram me excitar, querido."
    mc "Você realmente achou que suas palavras vazias e toques fracos iam me satisfazer?"
    mc "Que decepção... eu esperava algo muito mais excitante vindo de alguém como você."
    mc "Pensei que você fosse um homem de verdade, mas tudo o que vejo é um menininho tentando parecer grande."
    mc "Você não passou de uma decepção, incapaz de me fazer sentir o que prometeu."
    mc "Suas tentativas foram tão fracas que mal valeram o esforço de responder."
    mc "Se você não pode me dar o que eu quero, é melhor nem tentar. Eu mereço alguém que possa me satisfazer de verdade."

    mc "Sério isso? Tava esperando mais do que umas frases de efeito baratas."
    mc "Você tá brincando, né? Pensei que você ia chegar com algo mais... substancial."
    mc "Ah, por favor, suas tentativas foram tão broxantes que eu mal consigo me segurar para não rir na sua cara."
    mc "E eu aqui pensando que você ia chegar com algo que realmente mexesse comigo, mas tudo o que vejo é mais do mesmo."
    mc "Que desperdício de tempo... Eu poderia ter passado esse tempo fazendo algo mais interessante."
    mc "Sabe, eu esperava um pouco mais de criatividade da sua parte. Essa abordagem básica não vai me levar a lugar nenhum."
    mc "Você acha que tá arrasando com essas palavras sujas? Desculpa te informar, mas isso só me faz querer rir da sua cara."
    mc "Ah, cara, você tá tentando tão duro, mas tudo o que consegue é me deixar entediada."
    mc "Parece que alguém não sabe como me deixar excitada... Tá na hora de você aprender alguns truques novos."
    mc "Sabe, você devia tentar mais. Eu gosto de um desafio, e até agora, você tá longe de ser um."
















    mc "Mais... me fode com suas palavras... eu preciso de mais de você, até eu não conseguir mais me conter."
    mc "Isso... continua... eu tô tão molhada que meu corpo inteiro treme de desejo só de ouvir sua voz."
    mc "Hmm, sua crueldade me excita tanto... eu quero que você me possua completamente, me faça sua putinha."
    mc "Não para agora... eu quero mais, quero tudo o que você tem para me dar, até eu não aguentar mais."
    mc "Sua brutalidade me deixa tão excitada... eu quero sentir toda essa violência misturada com prazer, até eu gozar feito uma vadia."
    mc "Isso... me faz gemer mais alto... eu quero que todo mundo saiba como você me faz sentir, como você me deixa louca de tesão."
    mc "Ah, sim... me faz sua... me faz gozar com sua brutalidade... eu sou sua para fazer o que quiser."
    mc "Me mostra quem manda... me domina completamente... eu quero ser sua, só sua, até eu não conseguir pensar em mais nada além de você."
    mc "Eu preciso de mais... de mais de você... eu quero que você me foda até eu não conseguir mais andar."



    mc "Hmm, interessante... mas você ainda tem muito o que provar se quiser me impressionar de verdade."




    mc "Bem... não é exatamente o que eu esperava ouvir, mas pelo menos é... criativo, de certa forma."







    mc "Bom... não posso negar que você tem uma maneira... intrigante de falar comigo."










    mc "Ah, mal posso esperar para você ver o que sou capaz de fazer com meus dedos, seu tarado. Vou me tocar bem na sua frente e você vai assistir cada segundo com atenção."
    mc "Está pronto para ver como eu posso me dar prazer sozinha, seu safado? Porque eu estou prestes a te mostrar."
    mc "Vou me masturbar para você, seu tarado, e você vai ver cada gemido e cada tremor enquanto eu gozo feito uma puta."
    mc "Você quer ver como eu posso me satisfazer, seu safado? Então prepare-se para assistir a um show particular meu."
    mc "Ah, eu estou tão molhada e pronta para gozar, seu tarado. Vou me tocar bem na sua frente e você vai adorar cada momento."
    mc "Estou prestes a me masturbar até gozar, seu safado, e você vai ser o único a testemunhar toda essa luxúria."
    mc "Agora é minha vez de te mostrar como eu posso me dar prazer, seu tarado. Prepare-se para um espetáculo que vai te deixar de joelhos."
    mc "Vou me masturbar para você, seu tarado, e vou fazer isso com tanto tesão que você vai implorar para participar."
    mc "Estou pronta para me tocar até gozar, seu safado. E você vai ver cada momento, cada gemido, cada arrepio de prazer."
    mc "Você quer ver como eu me dou prazer, seu tarado? Então prepare-se para assistir a uma exibição que vai te deixar implorando por mais."

    mc "Sabe, tarado, eu decidi que é hora de você assistir enquanto eu me toco. Eu quero que você veja exatamente como eu posso me satisfazer."
    mc "Eu estou no comando agora, tarado. E você vai assistir enquanto eu me toco até gozar, porque eu quero que você saiba quem está no controle aqui."
    mc "Prepare-se para assistir a um espetáculo, seu tarado, porque eu decidi que é hora de você ver como eu posso me dar prazer."
    mc "Eu não estou fazendo isso por você, tarado. Eu estou me tocando porque eu quero, e você vai ficar aí e assistir, como eu mando."
    mc "Está na hora de eu assumir o controle, tarado. E você vai assistir enquanto eu me toco, porque é isso que eu quero, e você vai obedecer."
    mc "Eu decidi que é hora de você ver como eu posso me satisfazer, tarado. E você vai ficar aí e assistir, porque eu estou no comando agora."
    mc "Eu quero que você veja exatamente como eu posso me dar prazer, tarado. E você vai ficar aí e assistir, porque eu estou no controle."
    mc "Eu estou no controle agora, tarado. E você vai assistir enquanto eu me toco, porque é isso que eu quero, e você vai obedecer aos meus desejos."
    mc "Eu decidi que é hora de você ver como eu posso me dar prazer, tarado. E você vai ficar aí e assistir, porque é isso que eu quero, e você vai obedecer."
    mc "Está na hora de você ver quem manda aqui, tarado. E você vai assistir enquanto eu me toco até gozar, porque é isso que eu quero, e você vai obedecer aos meus comandos."



    mc "Oh, sim, isso é incrível! Eu estou gozando tão gostoso, tão forte!"
    mc "Ah, sim, eu estou gozando! Eu estou gozando tão forte, seu tarado!"
    mc "Isso é tão bom, eu estou gozando tão gostoso para você, seu safado!"
    mc "Ah, porra, sim! Eu estou gozando tão gostoso, seu tarado, tão delicioso!"
    mc "Oh, Deus, sim! Eu estou gozando para você, eu estou gozando tanto!"
    mc "Isso é incrível, eu estou gozando tanto! Eu não consigo parar, seu tarado!"
    mc "Ah, sim! Eu estou gozando para você, eu estou gozando tão gostoso, tão intenso!"
    mc "Oh, sim! Eu estou gozando tão gostoso, tão forte, seu safado!"
    mc "Porra, sim! Eu estou gozando, estou gozando tão gostoso para você, seu tarado!"
    mc "Ah, isso é tão bom! Eu estou gozando para você, estou gozando tanto, tão delicioso!"

    mc "Oh, sim, isso é incrível! Minha buceta está tão molhada para você, seu tarado! Eu estou gozando tão gostoso, tão forte!"
    mc "Ah, porra, sim! Minha buceta está tão apertada, tão faminta por você, seu safado! Eu estou gozando tão gostoso para você!"
    mc "Isso é tão bom, minha buceta está latejando de desejo por você, seu tarado! Eu estou gozando tão gostoso, tão intenso!"
    mc "Oh, sim! Minha buceta está tão molhada pensando em como você me fode, seu safado! Eu estou gozando para você, eu estou gozando tanto!"
    mc "Ah, sim! Eu estou gozando para você, minha buceta está tão molhada, tão ansiosa por você, seu tarado!"
    mc "Isso é incrível, minha buceta está pulsando de desejo por você, seu safado! Eu estou gozando tão gostoso, tão intenso!"
    mc "Oh, sim! Minha buceta está tão apertada, tão faminta por você, seu tarado! Eu estou gozando para você, eu estou gozando tanto!"
    mc "Porra, sim! Minha buceta está tão molhada imaginando como você me fode, seu safado! Eu estou gozando tão gostoso para você!"
    mc "Ah, isso é tão bom! Minha buceta está tão molhada para você, tão ansiosa por você, seu tarado! Eu estou gozando tanto, tão delicioso!"
    mc "Oh, sim, isso é incrível! Minha buceta está tão apertada, tão quente para você, seu tarado! Eu estou gozando tão gostoso, tão forte!"

label akemi_textos:



























    mc "Ele... ele me chama para o estoque... e..."
    a "E...?"
    mc "E... ele me faz... coisas..."
    a "Coisas?"
    mc "Sim... coisas... sujas..."
    a "Sujas?"
    mc "Sim... ele... ele me toca... ele me beija... ele..."
    "E-eu... eu não consigo falar..."
    "Mas... eu lembro..."
    "Eu lembro da mão dele... no meu corpo..."
    "Dos lábios dele... nos meus..."
    "Da língua dele... na minha buceta..."
    "E-eu... eu tô ficando excitada..."

    if fado:

        f "Ela tá gostando de lembrar... essa vadia..."

    a "[mc]..."
    mc "E-eu..."
    a "Você gosta?"
    mc "Eu... eu não sei..."
    a "Você gosta do Jasper?"
    mc "Eu... eu não sei..."
    a "Mas... você gosta do que ele faz com você?"
    mc "Eu... eu acho que sim..."
    a "Então... por que você tá confusa?"
    mc "Porque... eu não devia gostar..."
    a "Por que não?"
    mc "Porque... ele é um idiota. Ele é... um homem sujo."
    a "E daí?"
    "E daí?"
    "Ela tem razão..."
    "E daí se ele é um idiota?"
    "E daí se ele é um homem sujo?"
    "O que importa é que... eu gosto..."
    mc "E daí..."
    a "[mc]..."























label textos_prontos:

    pass

label textos_nathan_muitobons:




































































































































































































































































































































































































































































































































































































































































































































































































label sexo_gemini_akemi:



















































































































































































































label onlyfans_akemi_live_hot:




    scene black with dissolve

    scene akemi30 with dissolve

    mc "Akemi, você tem certeza disso? Uma live... no OnlyFans?"

    a "Claro, meu amor. Você não disse que queria mais? Que queria sentir tudo?"

    mc "Eu... eu disse... mas... e se alguém descobrir? E se o Gabriel..."

    a "Esquece o Gabriel, [mc]. Hoje você é minha. E você vai adorar isso."

    "Ela me puxa para perto e me beija, um beijo quente e provocante que me deixa sem fôlego. Seus lábios têm gosto de vinho e desejo... e eu quero mais..."

    play sound beijo_intenso_2

    mc "Hmmm... Akemi..."

    a "Pronta pra começar o show, querida?"

    mc "Acho que sim..."



    scene onlyfans_live_akemi with dissolve

    "Akemi liga a câmera e a live começa. Os comentários dos fãs pipocam na tela, cheios de excitação e expectativa."

    "Fã_Tarado1" "Aí sim! A [mc] voltou! Que saudade dessa gostosa!"

    "Fã_Doidinho2" "Finalmente! Akemi e Melissa juntas! Vou gozar só de olhar!"

    "Seguidor_Safado3" "Que delícia! Queria estar aí com vocês... 😉🔥"

    "Fã_Obcecado4" "Mostra a buceta, [mc]! Implora pra Akemi te lamber!"

    "Seguidor_Bruto5" "Arranca a roupa dela, Akemi! Quero ver essa vadia nua!"



    play sound roupas 

    mc "O que vocês acham, meus amores? Gostaram da surpresa?"

    a "A gente preparou algo especial pra vocês hoje... Vocês vão adorar..."

    "Fã_Tarado1" "Porra, [mc], você tá linda demais! Que corpão!"

    "Fã_Doidinho2" "Akemi, você é uma deusa! Queria te chupar todinha!"

    "Seguidor_Safado3" "Vocês duas juntas... é demais pro meu coração! 🤤🔥"

    "Fã_Obcecado4" "Akemi, lambe a buceta dela! Faz ela gemer pra gente!"

    "Seguidor_Bruto5" "Arranca essa calcinha, porra! Quero ver essa xota!"




    play sound beijo_pescoço 

    "{i}Ai... Akemi... seus lábios... tão quentes... tão macios...{/i}"

    a "Você gosta disso, né, [mc]? De ser beijada... de ser tocada... de ser desejada..."

    mc "Hmmm... sim... eu gosto..."

    "Fã_Tarado1" "Caralho, que delícia! Elas tão se pegando!"

    "Fã_Doidinho2" "Akemi, chupa as tetas dela! Faz ela gritar!"

    "Seguidor_Safado3" "Que tesão! Queria estar aí no lugar da Akemi..."

    "Fã_Obcecado4" "Abre as pernas, [mc]! Mostra essa buceta pra gente!"

    "Seguidor_Bruto5" "Fode ela, Akemi! Acaba com essa vadia!"


    a "Eles querem ver seus peitos, [mc]... quer mostrar pra eles?"


    menu:
        "Sim":


            call sexualidade
            $ onlyfans_exibicao += 1
            mc "Sim... eu quero mostrar... quero que eles me vejam... me desejem..."

            a "Então mostra pra eles, querida... mostra pra eles o quão gostosa você é..."



            scene black with dissolve
            scene akemi31 with dissolve

            "Fã_Tarado1" "Porra, que peitões! Queria apertar eles com força!"

            "Fã_Doidinho2" "Akemi, chupa esses mamilos! Deixa eles bem duros!"

            "Seguidor_Safado3" "Que tesão! Queria estar aí mamando nessas tetas!"

            "Fã_Obcecado4" "Abre mais as pernas, [mc]! Quero ver sua buceta!"

            "Seguidor_Bruto5" "Fode ela logo, caralho! Não aguento mais esperar!"



            play sound gemido_alto_2
            mc "Ahnnn... Akemi... isso... tão gostoso..."

            a "Você gosta, né, vadia? De ser tocada assim? De ser desejada por todos esses homens?"

            mc "Hmmm... sim... adoro..."

            a "Eles querem ver mais, [mc]... querem ver tudo... Quer mostrar pra eles?"

            menu:
                "Sim, eu quero mostrar tudo.":


                    call sexualidade
                    $ onlyfans_exibicao += 1



                    scene black with dissolve
                    scene akemi32 with dissolve

                    "Fã_Tarado1" "Caralho, que buceta linda! Queria lamber ela todinha!"

                    "Fã_Doidinho2" "Akemi, enfia os dedos nessa xota! Faz ela gozar pra gente!"

                    "Seguidor_Safado3" "Que tesão! Queria estar aí comendo essa buceta!"

                    "Fã_Obcecado4" "Geme mais alto, [mc]! Mostra pra gente como você é gostosa!"

                    "Seguidor_Bruto5" "Fode ela logo, porra! Quero ver essa vadia gozando!"



                    mc "Aahnn... Akemi... mais... mais forte..."
                "Não, isso é demais pra mim.":



                    call inocencia

                    mc "Não... isso é demais pra mim... eu não consigo..."

                    a "Tudo bem, querida... A gente faz no seu ritmo..."
        "Não, ainda não.":


            call inocencia

            mc "Não... ainda não... eu tô com vergonha..."

            a "Vergonha? Bobagem. Você não tem nada que se envergonhar."

            if (namorando or gabriel_beijo >= 13):
                mc "Mas e se o Gabriel vir isso?"

                if akemi_beijo >= 1 and akemi_pontos >= 70:
                    a "Relaxa, meu anjo. Eu já te mostrei que não preciso de homem nenhum pra te satisfazer."
                else:

                    a "Ele não precisa saber, ué. Segredos apimentam a relação."

            "Ai... e se o meu pai ver isso...? Ou o Pedro...?"




label onlyfans_akemi_live:

    menu:
        "Continuar...":


            call sexualidade

            mc "N-não... continua... me toca... me faz gozar..."

            a "Com prazer, querida... com prazer..."



            a "Senta aqui, querida... Deixa eu cuidar de você..."

            mc "A-Akemi..."

            "Ela me ajuda a sentar na privada, e se ajoelha na minha frente. Seus olhos brilham com desejo e carinho... e eu me sinto... segura... amada..."

            a "Você é tão linda, [mc]... tão gostosa..."

            "Ela beija minhas coxas... seus lábios quentes e úmidos... deixando um rastro de fogo na minha pele... Eu gemo baixinho, sentindo meu corpo inteiro arrepiar..."

            mc "A-Akemi... eu..."

            a "Shhh... apenas sinta, querida... Deixe eu te dar prazer..."

            "Ela me beija... na minha buceta... sua língua quente e ágil... me explorando... me provocando... me levando à loucura..."

            play sound gemido_alto_2 

            mc "Aaaaahhhhnnn!!! Akemi!!!"

            "Eu grito seu nome, sem conseguir me conter... O prazer é intenso demais... e eu me sinto... completamente entregue a ela..."

            a "Isso, [mc]... geme pra mim... geme alto... mostra pra mim o quanto você gosta..."

            "Ela continua me beijando, me chupando, me fodendo com os dedos... e eu gemo cada vez mais alto, meu corpo se contorcendo em espasmos de prazer..."

            a "Eu vou fazer isso pra você gravar pro seu OF, tá? Imagina os seus fãs vendo você assim... sendo devorada pela minha boca... eles vão pirar!"

            "{i}Ai, meu Deus... ela tá falando isso enquanto me chupa... enquanto me fode com os dedos... isso é tão... excitante...{/i}"

            a "Eles vão se masturbar olhando pra você, [mc]... vão gozar pensando na minha língua na sua buceta... nos meus dedos te fodendo..."

            mc "A-ahnn... Akemi... eu... eu tô gostando... tô gostando muito..."

            "{i}Ela é tão delicada... tão carinhosa... mesmo sendo tão experiente... Ela tá focada no meu prazer... 100% no meu prazer... É como se ela estivesse... fazendo amor comigo...{/i}"

            "Eu nunca me senti tão amada por alguém... nem mesmo pelo Gabriel..."

            play sound gemido_alto_3 

            mc "A-Akemi... e-eu vou... eu vou..."

            a "Goza, [mc]... goza pra mim... goza e me mostra como você é gostosa..."

            "Ela aumenta a intensidade dos movimentos, sua língua me fodendo com mais força, seus dedos me penetrando mais fundo..."

            play sound climax2 

            mc "AAAAAHHHHHHHNNNN!!!!!"

            scene black with dissolve

            pause 2.0

            "Meu corpo se contrai em espasmos violentos... ondas de prazer me invadindo, me consumindo... Eu grito seu nome, no auge do meu êxtase... e ela sorri... um sorriso doce e satisfeito..."

            "Eu... eu nunca tinha gozado assim antes... com tanta intensidade... com tanto prazer..."

            "O toque de uma mulher... é tão diferente... tão... especial..."

            scene akemi29 with dissolve

            mc "Akemi... eu... eu quero retribuir..."

            a "Não precisa, querida... Eu só quero te beijar..."

            "Ela me beija... um beijo suave e delicado... cheio de carinho e afeto..."

            play sound beijo

            mc "Hmmm... Akemi..."

            a "Pensa na minha proposta, tá? A gente podia fazer vídeos incríveis juntas... pro seu OnlyFans..."

            mc "Eu vou pensar..."

            "Ela sai do banheiro, me deixando sozinha com meus pensamentos... e com um sorriso bobo no rosto..."

            play sound cama



    scene akemi30 with dissolve

    mc "Akemi, você tem certeza disso? Uma live... no OnlyFans...?"

    a "Claro que sim, querida! Vai ser incrível! Os seus fãs vão pirar vendo a gente juntas..."

    mc "Mas... e se o Gabriel descobrir? E se meus pais...?"

    a "Relaxa, [mc]. Ninguém precisa saber. Este é o nosso segredo... nosso pequeno paraíso de prazer..."

    "Ela sorri, e eu sinto um arrepio percorrer meu corpo. Ela está certa. Ninguém precisa saber. Esta noite é só nossa..."



    scene black with dissolve

    scene akemi31 with dissolve

    "Akemi liga a câmera, e a live começa. A tela do celular mostra os comentários dos fãs em tempo real."



    "Fã1" "Caralho, que gostosas! 🔥🔥🔥"
    "Fã2" "Finalmente juntas! 😍😈"
    "Fã3" "Que peitinhos deliciosos! Queria morder eles todinha... 😋"
    "Fã4" "Mostra a buceta, [mc]! Quero ver essa xota rosadinha! 😈💦"
    "Fã5" "Akemi, chupa a buceta dela! Imploro!"
    "Fã6" "Duas putas gostosas! Me masturbem juntas! 🍆💦"

    mc "Ai... meu Deus... esses comentários... eles são tão... diretos..."

    a "Eles querem você, [mc]. Eles te desejam. E você vai dar a eles o que eles querem..."

    mc "O que... o que você vai fazer, Akemi?"

    a "Vou te mostrar, querida... vou te mostrar como se faz..."



    "{i}Ela me beija... seus lábios quentes e macios... sua língua explorando minha boca... me deixando sem ar...{/i}"

    play sound beijo_intenso_2 

    mc "Hmmm... Akemi..."

    a "Você é tão gostosa, [mc]... tão macia... tão... perfeita..."



    "{i}Suas mãos... tão quentes... tão delicadas... me tocando... me acariciando... me deixando louca...{/i}"

    play sound gemido2

    mc "Ahnn... Akemi..."

    a "Eu vou te fazer gozar, [mc]... vou te fazer gozar na frente de todos esses tarados..."



    "{i}Seus dedos... dentro de mim... me fodendo... me possuindo... Ai, meu Deus... eu tô pegando fogo...{/i}"

    play sound gemido3

    mc "A-ahnn... Akemi... mais... mais rápido..."

    a "Você gosta disso, né, sua putinha? Gosta de ser fodida assim? Na frente de todo mundo?"

    mc "S-sim... eu gosto... eu adoro..."



    "{i}Ela me fode com os dedos... com força... com raiva... com desejo... e eu me sinto... tão pequena... tão vulnerável... tão... puta...{/i}"



    "Fã7" "Caralho, que tesão! 😈💦"
    "Fã8" "Ela tá gozando! Akemi, faz ela gozar de novo!"
    "Fã9" "Que buceta deliciosa! Queria estar aí no lugar da Akemi!"
    "Fã10" "Mete com força, Akemi! Arrebenta essa vadia!"

    a "Eles querem que você goze, [mc]... Querem ver você se desfazer em prazer... Querem te ver... minha..."

    mc "Eu... eu vou... eu vou..."

    play sound gemido5



    mc "Aaaahhhhhhhnnnn!!! Akemi!!!"

    scene black with dissolve

    pause 2.0

    "Meu corpo inteiro treme... convulsionando em espasmos de puro prazer... Eu gozei... gozei na frente de todos aqueles homens... e eu... eu adorei..."

    "Eu sou uma puta... uma exibicionista... e eu nunca me senti tão bem na minha vida..."

    a "Você foi incrível, querida... Eles adoraram... "



    "{i}Ela me beija... um beijo doce e suave... tão diferente dos beijos brutais e selvagens que eu tive antes...{/i}"

    mc "Akemi... eu... "

    a "Shhh... não precisa dizer nada, meu amor. Eu sei o que você está sentindo..."



    scene black with dissolve

    scene akemi29 with dissolve

    mc "Eu... eu quero retribuir... quero te dar prazer também..."

    a "Outro dia, querida. Hoje, eu só quero te amar..."




label sexo_gemini_frases_beto:







































































































































































































label cena_leo_beto_gemini:

    l "Beto, seu merda! O que você pensa que tá fazendo?"

    scene black with dissolve

    scene beto_provocando_mel with dissolve

    pause 2.0

    mc "Léo! Que susto!"

    b "L-Léo... e-eu..."

    l "Eu te pego no flagra com essa... com essa garota e você ainda gagueja?!"

    l "Que porra é essa, Beto?! Você tava se esfregando nela? Na minha frente?!"

    "Ele encara Beto com ódio, e eu sinto um frio na barriga... Será que ele vai bater no Beto? Eu preciso fazer alguma coisa..."

    b "E-eu... eu não tava... a gente só tava..."

    l "Cala a boca, seu merda! Você não serve pra nada! Nem pra pegar uma garota direito!"

    "Ele avança sobre Beto, e eu vejo... medo em seus olhos... e... desejo? Será que ele quer que o Léo faça o que ele não tem coragem?"

    l "Você é um fracassado, Beto! Um bosta! E você, [mc]..."

    "Ele se vira pra mim, seu olhar queimando de raiva e desprezo. E... tesão? Meu corpo se arrepia... "

    l "Você devia ter vergonha de se rebaixar a esse nível! De se esfregar nesse... nesse..."

    mc "Ele é melhor que você, Léo! Pelo menos ele me trata bem!"

    l "Melhor que eu?! Hahaha! Duvido! Esse aí não consegue nem te fazer gozar!"

    "Ele ri, com desdém, e eu sinto meu rosto queimar. Ele tá certo... mas... mas isso não é motivo pra humilhar o Beto..."

    mc "E você consegue, é? Seu machão de merda!"

    l "Eu consigo, sim. E muito melhor que ele. Quer ver?"

    "Ele tá tão perto... eu consigo sentir seu cheiro... sua respiração... seu desejo..."

    "E eu... eu não sei se consigo resistir... "

    b "Léo... não... "

    l "Cala a boca, seu merda! Isso não é da sua conta!"

    "Ele... ele tem medo do Léo... Mas por quê?"

    l "Agora, [mc]... você vai ver o que é um homem de verdade..."

    "Ele me agarra pela cintura, me puxando para perto. Sinto seu corpo duro contra o meu... sua respiração quente no meu pescoço..."

    l "Eu vou te foder, [mc]... aqui... agora... na frente desse bosta..."

    "Ele me beija com força, um beijo bruto, possessivo. Eu tento resistir, mas ele é mais forte... e eu... eu não sei se quero resistir..."

    "Suas mãos apertam minha bunda, me puxando contra seu pau duro... e eu... eu gemo baixinho... Eu tô tão confusa..."

    if fado:

        f "Você quer isso, vadia... você quer ser fodida por ele... admita..."

    "O que eu faço? O que eu quero?"

    menu:
        "Tentar se afastar de Léo e pedir ajuda a Beto":


            call inocencia

            mc "Beto, me ajuda! Ele tá me forçando!"

            "Eu grito, tentando me soltar de Léo, mas ele é muito mais forte."

            b "Léo, solta ela! Você tá machucando ela!"

            "Beto finalmente reage, mas sua voz ainda é insegura... Ele tenta me puxar para longe de Léo, mas não tem força suficiente."

            l "Cala a boca, seu merda! Isso não é da sua conta!"

            "Léo me aperta com mais força, me fazendo gemer de dor e... prazer?"

            "Ai, meu Deus... o que tá acontecendo comigo? Por que eu tô gostando disso?"
        "Se entregar ao desejo e provocar Léo":


            call sexualidade

            mc "Léo... você me quer mesmo? Mais do que o Beto?"

            l "Hmmm... você nem imagina o quanto, gata... Eu vou te fazer esquecer desse fracasso..."

            "Ele aperta minha cintura com força, me puxando para mais perto, e eu sinto seu pau duro contra a minha coxa... "

            b "Léo! Solta ela! Você tá louco?!"

            l "Cala a boca, seu merda! Ela é minha agora... "

            play sound beijo_intenso_4  

            mc "A-ahnn..."

            "Eu gemo, me entregando ao beijo, sentindo seu corpo contra o meu... sua força... seu desejo... "

            "Ele me aperta com mais força... me puxa para um canto mais escuro do provador... e eu... eu não consigo resistir... "

            "Eu quero ele... eu quero os dois... "



            jump continua_cena_triangulo

    label continua_cena_triangulo:



        l "Você gosta disso, né, vadia? De ser tocada assim... na frente do seu namoradinho... "

        "Ele sussurra no meu ouvido, me fazendo arrepiar. Suas mãos apertam meus seios, minha bunda... me explorando sem pudor..."

        mc "A-ahnn... Léo... "

        "Eu gemo, sem conseguir me controlar. Meu corpo queima de desejo... e a presença de Beto, assistindo a tudo, só aumenta a minha excitação..."

        b "Léo... para com isso... por favor... "

        l "Cala a boca, seu merda! Ou você quer que eu te foda também?"

        "Léo ameaça, e Beto se encolhe, com medo. Eu... eu sinto uma pontada de pena dele... mas o desejo por Léo é mais forte... "

        "Eu quero que ele continue... eu quero que ele me possua... aqui e agora... na frente do Beto... "

        mc "C-continua, Léo... me fode... me faz sua... "

        "Eu sussurro, e Léo sorri, um sorriso cruel e vitorioso. Ele me joga no chão do provador, subindo em cima de mim... "

        l "Você é minha, [mc]... minha putinha... minha vadia... "

        "Ele começa a tirar minha roupa, com brutalidade, rasgando meu vestido, arrancando meu sutiã... me deixando completamente nua e vulnerável... "

        mc "A-ahhnn... Léo... "

        "Eu gemo, me contorcendo de prazer... sentindo seu corpo contra o meu... sua respiração ofegante... seu pau duro me pressionando... "

        "Eu olho para Beto... ele está parado ali, nos observando... seus olhos cheios de... raiva... tristeza... e... tesão?"

        "Ele tá duro! E-eu consigo ver através da calça!"

        "Será que... será que ele quer se juntar a nós? Será que ele quer... me foder também?"

        if fado:

            f "Ele quer, sua vadia... ele quer... mas ele é um covarde... um fraco..."

        "E eu... eu quero que ele se junte... eu quero sentir os dois... me fodendo... me usando... me possuindo..."

        "Essa ideia me deixa ainda mais molhada... me faz gozar só de pensar..."

        play sound climax2

        mc "Aaaahhhhh!!!"

        "Eu grito, me contorcendo de prazer, enquanto Léo me fode com os dedos... me fazendo gozar de novo e de novo... "

        l "Isso, vadia... goza pra mim... goza pro Beto ver... "

        "Ele sussurra, e eu sinto meu corpo inteiro se arrepiar... Ele tá me usando... me humilhando... mas eu adoro... "

        mc "B-Beto... olha... olha o que ele tá fazendo comigo..."

        "Eu gemo, olhando para Beto, implorando por sua ajuda... ou por sua participação... "

        b "Eu... eu não posso, [mc]... eu não consigo..."

        "Ele fala, com a voz embargada, e se vira, escondendo o rosto... mas eu vejo... eu vejo que ele tá chorando... "

        "E... e ele tá duro... tão duro... "

        mc "Beto... por favor... me ajuda..."

        "Eu imploro, mas no fundo... eu não quero que ele me ajude... eu quero que ele assista... eu quero que ele participe... "

        "Eu quero que ele se entregue ao desejo... assim como eu... "

        l "Chega de choro, porra! Agora é a minha vez!"

        "Ele vai me foder... aqui... agora... na frente do Beto... "

        "E eu... eu tô tão excitada... tão molhada... tão pronta pra ele... "





















    mc "A-a-ahnnn... Léo... mais... mais forte..."

    l "Você gosta, né, vadia? Gosta de ser fodida assim... no meio do mercado... com seu amiguinho olhando..."

    "Ele segura meu cabelo com força, puxando minha cabeça para trás, e eu gemo mais alto, sentindo seu pau bater fundo dentro de mim..."

    mc "A-ahnnn... f-fode... fode a sua putinha... a-assim..."

    b "..."

    "{i}Eu consigo ver... o pau dele tá duro... e ele nem tenta esconder... Ele quer isso... ele quer participar...{/i}"

    if fado:
        f "Isso, vadia... provoca o Betinho... faz ele se juntar a essa foda... faz ele se entregar ao desejo... hehehe..."

    l "Geme pra mim, [mc]... geme e mostra pro Beto o que ele tá perdendo..."

    mc "Aaaahhhnnn... L-Léo... eu... eu vou gozar..."

    l "Goza pra mim, vadia... goza e me deixa te encher com a minha porra..."

    play sound climax2

    scene beto_leo_fodem with vpunch

    mc "AAAAHHHHHNNN!!!"

    l "Isso... goza... goza, sua puta..."

    "Ele tá... ele tá gozando também..."

    l "Aaaahhhnnn... [mc]... sua vadia... a-ahnn..."

    "Ele se afasta, e eu caio no chão, exausta, ofegante, mas... completamente satisfeita... e ainda mais excitada."

    b "[mc]... você... você tá bem?"

    mc "B-Beto... eu..."

    l "Ela adorou, Beto... E se você for homem de verdade, vai fazer ela gozar de novo... agora mesmo..."

    b "Cala a boca, Léo... isso não é da sua conta..."

    l "Não é da minha conta? Eu acabei de foder a sua namoradinha, e você não fez nada pra impedir!"

    b "Ela não é minha namorada... e... e você não devia ter feito isso..."

    l "Ela é uma puta, Beto... e as putas foram feitas pra serem fodidas... usadas... e eu vou usar essa aqui até não poder mais..."

    "Ele... ele tem razão... Eu sou uma puta... e eu quero ser usada... Eu quero ser fodida..."

    mc "Beto..."

    b "[mc]... eu... eu não sei o que dizer..."

    l "Não precisa dizer nada, Beto... só olha... e aprende..."

    "Ele se ajoelha na minha frente... e pega meu rosto entre as mãos... me forçando a olhá-lo nos olhos."

    l "Você quer mais, não quer, [mc]? Você quer que eu te foda de novo... aqui... agora... na frente do Beto..."

    "Eu... eu não consigo resistir... eu quero... eu quero ele... eu quero os dois..."

    if fado:
        f "Isso, vadia... se entrega... se entrega pra eles... deixa eles te usarem... te possuírem... você nasceu pra isso..."

    mc "S-sim... eu quero... eu quero..."

    l "Então vem, putinha... vem que eu vou te dar o que você quer..."





















































    mc "A-ahhnnn... Léo... Beto... a-assim... i-isso..."

    "Eu gemo sem parar, entregue ao prazer avassalador que os dois me proporcionam. O corpo de Léo... suado... musculoso... me prensando contra o chão frio do provador... Seu pau me fodendo com força... sem piedade..."

    l "Você gosta, né, vadia? De ser fodida assim... por dois homens ao mesmo tempo..."

    "Ele sussurra no meu ouvido, sua voz rouca e cheia de malícia... E eu gosto... eu adoro... essa sensação de ser dominada... usada... possuída..."

    mc "S-sim... eu gosto... me fode... me fode mais forte..."

    "Eu imploro, e ele atende, me fodendo com ainda mais intensidade, me fazendo gritar de prazer... e de dor... "

    "Sinto as mãos de Beto em mim... em todo lugar... tocando meus seios... minha barriga... minha buceta..."

    "Ele me masturba enquanto Léo me fode... seus dedos ágeis e experientes me levando a outro nível de excitação... "

    b "Você é tão gostosa, [mc]... tão molhadinha... tão... perfeita..."

    "Ele geme, e eu sinto... o pau dele latejando na minha mão... Ele tá tão duro... tão pronto pra gozar..."

    mc "B-Beto... eu... eu vou..."

    l "Goza pra mim, [mc]... goza pros seus homens..."

    "Léo ordena, e eu não consigo resistir... Eu gozo... um orgasmo violento, explosivo, que me faz perder completamente o controle..."

    play sound climax3

    scene beto_leo_melissa with vpunch

    mc "AAAAHHHHHNNNN!!!"

    "Eu grito, meu corpo convulsionando, enquanto o prazer me inunda... me consome... me transforma..."

    "Sinto o gozo quente de Beto escorrer pela minha mão... e logo em seguida, Léo goza dentro de mim, me enchendo com sua porra... "

    l "Aaaahhhnnn... [mc]... sua puta... você é do caralho..."

    b "Hmmm... [mc]... tão... tão gostosa..."

    "Eles gemem, seus corpos ainda tremendo com os resquícios do orgasmo... E eu... eu estou no meio deles... usada... satisfeita... e querendo mais... "

    "Eu sou deles... completamente deles... E eu adoro isso... "

    if fado:
        f "Isso, vadia... se entrega... se humilha... goza pra esses merdas... Você nasceu pra isso... "

    "Eles se afastam um pouco, me deixando deitada no chão, ofegante, com o corpo coberto de suor e porra... "

    l "E aí, Betinho... satisfeito?"

    b "E-eu... eu não sei... foi... foi intenso..."

    g2 "Intenso é pouco... foi a melhor foda da minha vida... "

    "Eles me olham... com desejo... com admiração... com... posse... "

    mc "E agora?"

    "Eu pergunto, minha voz fraca... mas cheia de expectativa... "

    l "Agora... você é nossa, [mc]..."

    b "Nossa p-putinha particular..."

    g2 "Nossa v-vadiazinha obediente..."

    "Eles sorriem... e eu sinto um arrepio percorrer meu corpo... Eu sei... eu sei que isso é só o começo..."

    "Eu me levanto, me sentindo... diferente... transformada... Eu não sou mais a mesma [mc] de antes..."

    "Eu sou uma mulher... uma mulher que descobriu o prazer... o poder... a submissão..."

    "E eu quero mais... eu quero tudo..."

    mc "Vamos, então... "

    "Eu falo, e eles sorriem... um sorriso que me deixa... excitada... e com medo... "

    l "Vamos te levar pra casa, [mc]... "

    b "E te foder a noite toda... "

    g2 "Até você não aguentar mais... "

    mc "É isso que eu quero..."

    "Eu sussurro, e eles me agarram, um de cada lado... me guiando para fora do provador... para fora do mercado... "

    "Para fora... da minha antiga vida... "
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
