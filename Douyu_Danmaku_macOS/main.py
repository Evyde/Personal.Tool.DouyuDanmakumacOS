# import esky
# import py2app
import locale, modules

import globalvars

# Get system language
# TODO: When people chose the program language, it should use user's language, not detect locale language.
if "en" in locale.getdefaultlocale()[0]:
    globalvars.lan = "en_US"
else:
    globalvars.lan = locale.getdefaultlocale()[0]



modules.init()


def adjust_f(sender):
    if adjust_f.huh:
        sender.add('$')
        sender.add('%')
        sender['zzz'] = 'zzz'
        sender['separator'] = separator
        sender['ppp'] = MenuItem('ppp')
    else:
        del sender['$']
        del sender['%']
        del sender['separator']
        del sender['ppp']
    adjust_f.huh = not adjust_f.huh
adjust_f.huh = True

def print_f(_):
    print(f)

f = MenuItem('F', callback=adjust_f)

urlretrieve('http://upload.wikimedia.org/wikipedia/commons/thumb/c/'
            'c4/Kiss_Logo.svg/200px-Kiss_Logo.svg.png', 'kiss.png')


@clicked('update method')
def dict_update(menu):
    print(menu)
    print(menu.setdefault('boo', MenuItem('boo',
                                          callback=lambda _: add_separator(menu))))  # lambda gets THIS menu not submenu

def add_separator(menu):
    menu.add(separator)

@clicked('C')
def change_main_menu(_):
    print(app.menu)
    print('goodbye C')
    del app.menu['C']  # DELETE SELF!!!1

@clicked('stuff')
def stuff(sender):
    print(sender)
    if len(sender):
        sender.insert_after('lets', 'go?')
        sender['the'].insert_before('band', 'not')
        sender['the'].insert_before('band', 'a')
    else:
        sender.update(['hey', ['ho', MenuItem('HOOOO')], 'lets', 'teenage'], the=['who', 'is', 'band'])
        sender.add('waste land')

