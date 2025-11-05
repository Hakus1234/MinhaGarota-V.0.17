













define config.name = _("Minha Garota")





define gui.show_name = True



define config.version = "0.16.3"

define config.quit_action = Quit(confirm=False)
define config.all_character_callbacks = [ type_sound ]
define config.default_music_volume = 0.3
define config.default_sfx_volume = 1.0
define config.default_voice_volume = 0.2
define config.has_autosave = False
define config.autosave_slots = 0
define config.autosave_on_choice = False
default preferences.skip_unseen = False




define gui.about = _p("""
""")






define build.name = "MinhaGarota"







define config.has_sound = True
define config.has_music = True
define config.has_voice = True
























define config.enter_transition = dissolve
define config.exit_transition = dissolve




define config.intra_transition = dissolve




define config.after_load_transition = None




define config.end_game_transition = None
















define config.window = "auto"




define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)







default preferences.text_cps = 50





default preferences.afm_time = 15
















define config.save_directory = "MinhaGarota-1641691388"






define config.window_icon = "gui/window_icon.png"






init python:




















    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)









    build.documentation('*.html')
    build.documentation('*.txt')
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
