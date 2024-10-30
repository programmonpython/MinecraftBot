import flet as ft
import time
botver = '4.5.8'
from javascript import require, On, Once, AsyncTask, once, off
mineflayer = require('mineflayer')
pathfinder = require('mineflayer-pathfinder')
radarPlugin = require('mineflayer-radar')
pvp = require('mineflayer-pvp').plugin
Goalfollow = pathfinder.goals.GoalFollow
GoalBlock = pathfinder.goals.GoalBlock
GoalGetToBlock = pathfinder.goals.GoalGetToBlock


def main(page: ft.Page):
    ######################################################################
    ###############
    botu = ''
    host = ''
    ver = ''
    ###############
    def localmir(e):
        hostb.value = "127.0.0.1"
        page.update()
    ################
    local = ft.TextButton(text="К самому себе(нужен порт мира)",on_click=localmir)
    local1 = ft.Row([local], alignment=ft.MainAxisAlignment.CENTER)
    botuser = ft.TextField(text_align=ft.TextAlign.LEFT, label='Ник бота')
    hostb = ft.TextField(text_align=ft.TextAlign.LEFT, label='Ip сервера')
    port1 = ft.TextField(label='Порт (если не нужен то оставь пустым)')
    port2 = ft.Row([port1], alignment=ft.MainAxisAlignment.CENTER)
    verb = ft.Dropdown(label='Версия майнкрафта', options=[ft.dropdown.Option("1.20.6"), ft.dropdown.Option("1.20.5"),
                                                           ft.dropdown.Option("1.20.4"), ft.dropdown.Option("1.20.3"),
                                                           ft.dropdown.Option("1.20.2"), ft.dropdown.Option("1.20.1"),
                                                           ft.dropdown.Option("1.20"),ft.dropdown.Option("1.19.4"),
                                                           ft.dropdown.Option("1.19.3"),ft.dropdown.Option("1.19.2"),
                                                           ft.dropdown.Option("1.19.1"),ft.dropdown.Option("1.19"),
                                                           ft.dropdown.Option("1.18.2"),ft.dropdown.Option("1.18.1"),
                                                           ft.dropdown.Option("1.18"),ft.dropdown.Option("1.17.1"),
                                                           ft.dropdown.Option("1.17"),ft.dropdown.Option("1.16.5"),
                                                           ft.dropdown.Option("1.16.4"),ft.dropdown.Option("1.16.3"),
                                                           ft.dropdown.Option("1.16.2"),ft.dropdown.Option("1.16.1"),
                                                           ft.dropdown.Option("1.16"),ft.dropdown.Option("1.15.2"),
                                                           ft.dropdown.Option("1.15.1"),ft.dropdown.Option("1.15"),
                                                           ft.dropdown.Option("1.14.4"),ft.dropdown.Option("1.14.3"),
                                                           ft.dropdown.Option("1.14.2"),ft.dropdown.Option("1.14.1"),
                                                           ft.dropdown.Option("1.14"),ft.dropdown.Option("1.13.2"),
                                                           ft.dropdown.Option("1.13.1"),ft.dropdown.Option("1.13"),
                                                           ft.dropdown.Option("1.12.2"),ft.dropdown.Option("1.12.1"),
                                                           ft.dropdown.Option("1.12"),ft.dropdown.Option("1.11.2"),
                                                           ft.dropdown.Option("1.11.1"),ft.dropdown.Option("1.11"),
                                                           ft.dropdown.Option("1.10.2"),ft.dropdown.Option("1.10.1"),
                                                           ft.dropdown.Option("1.10"),ft.dropdown.Option("1.9.4"),
                                                           ft.dropdown.Option("1.9.3"),ft.dropdown.Option("1.9.2"),
                                                           ft.dropdown.Option("1.9.1"),ft.dropdown.Option("1.9"),
                                                           ft.dropdown.Option("1.8.9")])
    dbgkey = "xcve11"

    ################
    name = ft.Row([botuser], alignment=ft.MainAxisAlignment.CENTER)
    serverip = ft.Row([hostb, ], alignment=ft.MainAxisAlignment.CENTER)
    minever = ft.Row([verb, ], alignment=ft.MainAxisAlignment.CENTER)
    primech = ft.Row([ft.Text('После нажатия кнопки создать перейдите на вкладку управление')],
                     alignment=ft.MainAxisAlignment.CENTER)


    ################


    ######################################################################
    test = ft.Row([ft.Text('test')],alignment=ft.MainAxisAlignment.CENTER)
    ######################################################################
    def change_theme(e):
        page.theme_mode = 'light' if page.theme_mode == 'dark' else 'dark'
        if page.theme_mode == 'light':btn_change.icon = ft.icons.SHIELD_MOON
        else:btn_change.icon = ft.icons.SUNNY
        page.update()
    btn_change = ft.IconButton(icon=ft.icons.SUNNY, on_click=change_theme)
    ######################################################################



    ######################################################################
    settings_theme = ft.Row([ft.Text('Изменить тему'),btn_change],alignment=ft.MainAxisAlignment.CENTER)


    def on(e):
        ###########################
        #######################################################################
        botu = botuser.value
        host = hostb.value
        ver = verb.value
        #######################################################################
        global bot
        bot = mineflayer.createBot({'username': botu, 'host': host, 'version': ver, 'port': port1.value})

        ######################################################################
        bot.loadPlugin(pathfinder.pathfinder)
        bot.loadPlugin(pvp)

        mcData = require('minecraft-data')(bot.version)
        movements = pathfinder.Movements(bot, mcData)
        @On(bot, 'login')
        def login(e):
            @On(bot, 'chat')
            def chat(this, user, message, *args):

                print(f"{user} |> {message}")

                if '!сюда' in message:
                    player = bot.players[user]
                    target = player.entity
                    if target:
                        bot.pathfinder.setMovements(movements)
                        goal = Goalfollow(target, 1)
                        bot.pathfinder.setGoal(goal, True)
                    else: 
                        bot.chat(f"/msg {user} вне зоны прогрузки") 
                        player = bot.players[botu]
                        target = player.entity
                        bot.pathfinder.setMovements(movements)
                        goal = Goalfollow(target, 1)
                        bot.pathfinder.setGoal(goal, True)
                    print(f'{user} использовал: Сюда')

                if "!иди " in message:
                    sey = message.split(' ')
                    say1 = sey[1]
                    sey2 = sey[2]
                    sey3 = sey[3]
                    bot.pathfinder.setMovements(movements)
                    goal = GoalGetToBlock(say1,sey2,sey3)
                    bot.pathfinder.setGoal(goal, False)
                    print(f"{user} использовал: (иди) по координаттам: x={say1} y={sey2} z={sey3}")

                if "!к " in message:
                    sey = message.split(' ')
                    say1 = sey[1]
                    p = bot.players[say1]
                    t = p.entity
                    if t:
                        bot.pathfinder.setMovements(movements)
                        goal = Goalfollow(t, 1)
                        bot.pathfinder.setGoal(goal, True)
                    else: 
                        bot.chat(f"/msg {user} вне зоны прогрузки") 
                        player = bot.players[botu]
                        target = player.entity
                        bot.pathfinder.setMovements(movements)
                        goal = Goalfollow(target, 1)
                        bot.pathfinder.setGoal(goal, True)

                if "!уничтожить" in message:
                    sey = message.split(' ')
                    say1 = sey[1]
                    pl = bot.players[say1]
                    if pl:
                        t = pl.entity
                        bot.pvp.attack(t)
                    else: bot.chat("Вне зоный прогрузки")

                if "!отмена" in message:
                    bot.pvp.stop()





                if '!стоп' in message:
                    player = bot.players[botu]
                    target = player.entity
                    bot.pathfinder.setMovements(movements)
                    goal = Goalfollow(target, 1)
                    bot.pathfinder.setGoal(goal, True)
                    print(f"{user} использовал: Стоп")

                if '!день' in message:
                    bot.chat(f'/time set day')
                    print(f"{user} использовал: день")


                if '!ночь' in message:
                    bot.chat(f'/time set night')
                    print(f'{user} использовал: ночь')

                if '!выживание' in message:
                    bot.chat(f'/gamemode survival {user}')
                    print(f'{user} использовал: Выживание')

                if user == "14asdl1111_YT" or "mistademich":
                    if "!сетдом" in message:
                        global x, y, z
                        x = bot.entity.position.x
                        y = bot.entity.position.y
                        z = bot.entity.position.z
                        bot.chat("Точка дома установлена")
                        return x, y, z
                
                    if "!дом" in message:
                        x1 = int(x)
                        y1 = int(y)
                        z1 = int(z)
                        bot.chat(f"/msg {user}  {int(x)} {int(y)} {int(z)}")

                    if "!домой" in message:
                        x1 = int(x)
                        y1 = int(y)
                        z1 = int(z)
                        bot.pathfinder.setMovements(movements)
                        goal = GoalGetToBlock(x1,y1,z1)
                        bot.pathfinder.setGoal(goal, False)
                    
                    

                if '!креатив' in message:
                    bot.chat(f'/gamemode creative {user}')
                    print(f'{user} использовал: Креатив')


                if user == '14asdl1111_YT' or "mistademich":
                    if '!оп' in message:
                        bot.chat(f'/op {user}')
                    
                    if "!тп" in message:
                        bot.chat(f"/tp {user}")
                        
                    if '!бан ' in message:
                        nik = message.split(' ')
                        nik1 = nik[1]
                        bot.chat(f'/ban {nik1}')
                        print(f'{user} использовал: бан {nik1}')

                    if "!alert " in message:
                        sey = message.split(' ')
                        say1 = sey[0]
                        sey2 = ' '.join(sey[1:])
                        bot.chat(f"/say {sey2}")

                if user == "14asdl1111_YT":
                    if '!офф' in message:
                        bot.chat('Выключаюсь')
                        bot.end()

                    if "!килл" in message:
                        bot.chat("Сбой через 5")
                        time.sleep(0.5)
                        bot.chat("Сбой через 4")
                        time.sleep(0.5)
                        bot.chat("Сбой через 3")
                        time.sleep(0.5)
                        bot.chat("Сбой через 2")
                        time.sleep(0.5)
                        bot.chat("Сбой через 1")
                        time.sleep(0.5)
                        bot.pathfinder.setGoal(goal, False)


                    if "!кр " in message:
                        sey = message.split(' ')
                        say1 = sey[1]
                        pl = bot.players[say1]
                        t = pl.entity
                        if t:
                            a = t.position.x
                            b = t.position.y
                            c = t.position.z
                            bot.chat(f"/msg {user} координаты {say1}: x={int(a)} y={int(b)} z={int(c)}")
                        else: bot.chat(f"/msg {user} вне зоны прогрузки") 

                    if f"!dbg-{botver} {dbgkey}" in message:
                        bot.chat(f"/msg {user} Отладочная информация: ")
                        time.sleep(1)
                        bot.chat(f'/msg {user} Имя: ' + botu)
                        time.sleep(1)
                        if host != "127.0.0.1":
                            bot.chat(f'/msg {user} Сервер: ' + host)
                            time.sleep(1)
                        else:
                            bot.chat(f"/msg {user} Сервер: Локальный мир")
                            time.sleep(1)
                        if port1.value != "":
                            bot.chat(f"/msg {user} Порт: " + port1.value)
                            time.sleep(1)
                        else: pass
                        bot.chat(f'/msg {user} Версия клиента: ' + ver)
                        time.sleep(1)
                        bot.chat(f'/msg {user}Версия бота: ' + botver)
                        time.sleep(1)
                        bot.chat(f'/msg {user} Голод бота: {int(bot.food)}')
                        time.sleep(1)
                        bot.chat(f'/msg {user} Хп: {int(bot.health)}')
                        


                if user == 'mistademich':
                    if '!оп' in message:
                        bot.chat(f'/op {user}')


                if '!деоп' in message:
                    bot.chat(f'/deop {user}')
                    print(f'{user} использовал: деоп')
            

                if '!анбан ' in message:
                    nik = message.split(' ')
                    nik1 = nik[1]
                    bot.chat(f'/pardon {nik1}')
                    print(f'{user} использовал: анбан {nik1}')


                if '!сказать ' in message:
                    sey = message.split(' ')
                    say1 = sey[0]
                    sey2 = ' '.join(sey[1:])
                    bot.chat(sey2)
                    print(f'{user} использовал: Сказать С сообщением: {sey2}')


                if '!помощь' in message:
                    bot.chat(f'/msg {user} ВСЕ команды пишуться на РУССКОМ ЯЗЫКЕ')
                    time.sleep(1)
                    bot.chat(f'/msg {user} команда: !бан (ник игрока без пробелов) ')
                    time.sleep(1)
                    bot.chat(f'/msg {user} команда: !анбан (ник игрока без пробелов)')
                    time.sleep(1)
                    bot.chat(f'/msg {user} команда: !оп описание: выдаёт админку')
                    time.sleep(1)
                    bot.chat(f'/msg {user} команда: !деоп описание: снимает админку')
                    time.sleep(1)
                    bot.chat(f'/msg {user} команда: !креатив описание: даёт ВАМ креатив')
                    time.sleep(1)
                    bot.chat(f'/msg {user} команда: !выживание описание: дает ВАМ Выживание')
                    time.sleep(1)
                    bot.chat(f'/msg {user} команда: !инф описание: информация о боте')
                    time.sleep(1)
                    bot.chat(f'/msg {user} команда: !сказать описание: говорить от лица бота ')
                    time.sleep(1)
                    bot.chat(f'/msg {user} команда: !день описание: установить день ')
                    time.sleep(1)
                    bot.chat(f'/msg {user} команда: !ночь описание: установить ночь ')
                    time.sleep(1)
                    bot.chat(f"/msg {user} команда: !к описание: идти к человеку после пробела ")
                    time.sleep(1)
                    bot.chat(f"/msg {user} команда: !иди описание: идти по кордам пример: !иди x, y, z ")
                    print(f'{user} использовал: помощь')

            @On(bot, "physicsTick")
            def physicsTick (e):
                pass

            

            @On(bot, "playerjoin")
            def pljoin(this,player):
                bot.chat(f"{player} зашел в пати")    

    def send(e):
        bot.chat(send1.value)
        send1.value = ''
        page.update()

    def forwr(e):
        bot.setControlState('forward',True)
        time.sleep(0.1)
        bot.setControlState('forward', False)

    def backw(e):
        bot.setControlState('back', True)
        time.sleep(0.1)
        bot.setControlState('back', False)

    def lft(e):
        bot.setControlState('left', True)
        time.sleep(0.1)
        bot.setControlState('left', False)

    def riht(e):
        bot.setControlState('right', True)
        time.sleep(0.1)
        bot.setControlState('right', False)

    def sprint(e):
        bot.setControlState('sprint', True)

    def sneak(e):
        bot.setControlState('sneak', True)
        time.sleep(0.1)
        bot.setControlState('sneak', False)
    
    def fowrward(e):
        bot.setControlState('forward',True)
    def forward(e):
        bot.setControlState('forward', False)

    def sneak1(e):
        bot.setControlState('sneak', True)

    def gps_cheak(e):
        f = chek.value
        a = bot.players[f]
        if a:
            b = a.entity
            o = b.position.x
            d = b.position.y
            c = b.position.z
            gps_coords.value = f"Координаты {f}: x={int(o)} y={int(d)} z={int(c)}"
            page.update()
        else: 
            gps_coords.value = "Сущность не найдена!"
            page.update()




    ######################################################################
    gps_coords = ft.Text(value="")
    chek = ft.TextField(label="Ник игрока",on_submit=gps_cheak)
    chk = ft.Row([chek],alignment=ft.MainAxisAlignment.END)
    gps1 = ft.Row([gps_coords],alignment=ft.MainAxisAlignment.END)
    ######################################################################
    sprin = ft.TextButton(text="Спринт",on_click=sprint)
    snek = ft.TextButton(text="Шифт",on_click=sneak,on_long_press=sneak1)
    right = ft.TextButton(text="Направо",on_click=riht)
    left = ft.TextButton(text="Налево",on_click=lft)
    back = ft.TextButton(text="назад",on_click=backw)
    forw = ft.TextButton(text="Вперед",on_click=forwr,on_long_press=fowrward)
    ######################################################################
    w = ft.Row([sprin,forw,snek],alignment=ft.MainAxisAlignment.END)
    asd = ft.Row([left,back,right],alignment=ft.MainAxisAlignment.END)
    ######################################################################
    btn_ok = ft.TextButton(text='Создать', on_click=on)
    btn_ok1 = ft.Row([btn_ok], alignment=ft.MainAxisAlignment.CENTER)
    ######################################################################
    def change(e):
        index = page.navigation_bar.selected_index
        page.clean()
        if index == 0: page.add(name,serverip,minever,port2,local1,btn_ok1,primech)
        elif index == 1: page.add(send2,w,asd,chk,gps1),page.update()
        elif index == 2: page.add(settings_theme)
        page.update()
    ######################################################################
    send1 = ft.TextField(label='Отправить сообщение в чат', multiline=False, on_submit=send)
    send2 = ft.Row([send1],alignment=ft.MainAxisAlignment.START)
    ######################################################################
    page.title = 'Бот для майнкрафта'
    page.theme_mode = 'dark'
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    page.navigation_bar = ft.NavigationBar(
        destinations=[
            ft.NavigationBarDestination(icon=ft.icons.HOME, label='Создать'),
            ft.NavigationBarDestination(icon=ft.icons.TERMINAL, label='Управление'),
            ft.NavigationBarDestination(icon=ft.icons.SETTINGS, label='Настройки'),
            ft.NavigationBarDestination(icon=ft.icons.FORUM, label='Как использовать')
        ], on_change=change
    )

    page.add(name, serverip, minever, port2,local1, btn_ok1,primech)





ft.app(target=main)