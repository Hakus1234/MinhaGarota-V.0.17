style default:
    outlines [(0, "#000", 1, 1)]

transform anda_horizontal:
    xpos + 70

    linear velo_horizontal xpos + 1210
    linear velo_horizontal xpos + 70

    repeat

transform transform_blink:
    linear 1.0 alpha 0.2
    linear 1.0 alpha 1.0
    repeat

transform transform_logo:
    on show:
        alpha 0 xalign 0.5 yalign 0.5
        linear 2.0 alpha 1
    on hide:
        linear 2.0 alpha 0

transform transform_white:
    on show:
        alpha 0
        linear 2.0 alpha 1
    on hide:
        linear 2.0 alpha 0

transform notify:
    alpha 0
    xpos 10
    ypos 125

    parallel:
        linear 0.5 alpha 1
        pause 2.0
        linear 0.5 alpha 0

    parallel:
        linear 4.0 ypos 25

transform flutuando:

    linear 1.0 ypos +5
    linear 1.0 ypos -5
    repeat

transform z03:
    zoom 0.3

transform z04:
    zoom 0.4

transform z045:
    zoom 0.45

transform z05:
    zoom 0.5

transform z055:
    zoom 0.55

transform z06:
    zoom 0.6

transform z065:
    zoom 0.65

transform z07:
    zoom 0.7

transform z08:
    zoom 0.8

transform z09:
    zoom 0.9

transform seta_cima:
    xanchor 0.5
    yanchor 0.5
    yalign 0.0
    xalign 0.5

    block:
        linear 0.8 yalign -0.01
        linear 0.8 yalign 0.0
        repeat

transform seta_direita:
    rotate 90
    xanchor 0.5
    yanchor 0.5
    yalign 0.5
    xalign 1.0

    block:
        linear 0.8 xalign 1.01
        linear 0.8 xalign 1.0
        repeat

transform seta_baixo:
    rotate 180
    xanchor 0.5
    yanchor 0.5
    yalign 1.0
    xalign 0.5

    block:
        linear 0.8 yalign 1.01
        linear 0.8 yalign 1.0
        repeat

transform seta_esquerda:
    rotate 270
    xanchor 0.5
    yanchor 0.5
    yalign 0.5
    xalign 0.0

    block:
        linear 0.8 xalign -0.01
        linear 0.8 xalign 0.0
        repeat
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
