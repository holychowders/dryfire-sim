from random import random
from random import randint
from random import randrange
from random import choice as randchoice
from time import sleep

import pygame

# SOUND INIT
pygame.mixer.init()
sound_channel = pygame.mixer.Channel(0)

sound_error = pygame.mixer.Sound("audio/error.mp3")
sound_begin = pygame.mixer.Sound("audio/begin.mp3")
sound_reassess = pygame.mixer.Sound("audio/reassess.mp3")
sound_endex = pygame.mixer.Sound("audio/endex.mp3")
sound_threat = pygame.mixer.Sound("audio/threat.mp3")
sound_no_weapon = pygame.mixer.Sound("audio/no_weapon.mp3")
sound_handgun = pygame.mixer.Sound("audio/handgun.mp3")
sound_rifle = pygame.mixer.Sound("audio/rifle.mp3")
sound_bladed_weapon = pygame.mixer.Sound("audio/bladed_weapon.mp3")
sound_blunt_weapon = pygame.mixer.Sound("audio/blunt_weapon.mp3")
sound_idle = pygame.mixer.Sound("audio/idle.mp3")
sound_aggressive = pygame.mixer.Sound("audio/aggressive.mp3")
sound_attacking = pygame.mixer.Sound("audio/attacking.mp3")
sound_10ft = pygame.mixer.Sound("audio/10ft.mp3")
sound_20ft = pygame.mixer.Sound("audio/20ft.mp3")
sound_30ft = pygame.mixer.Sound("audio/30ft.mp3")
sound_40ft = pygame.mixer.Sound("audio/40ft.mp3")
sound_50ft = pygame.mixer.Sound("audio/50ft.mp3")
sound_60ft = pygame.mixer.Sound("audio/60ft.mp3")
sound_70ft = pygame.mixer.Sound("audio/70ft.mp3")
sound_80ft = pygame.mixer.Sound("audio/80ft.mp3")

# CONSTANTS
WEAPON_TYPES = ("NO WEAPON", "BLADED WEAPON", "BLUNT WEAPON", "HANDGUN", "RIFLE")

# STATE
g_weapon_type = None
g_attack_status = None

def main():
    print("[BEGIN...]")
    play_sound(sound_begin)
    sleep(randint(2, 5))

    present_threat()

    print()
    print("[REASSESS]")
    play_sound(sound_reassess)
    sleep(randint(3, 7))

    # Additional threat
    #if random() < .25:
    #    present_threat()

    print("[ENDEX]")
    play_sound(sound_endex)
    sleep(2)

def present_threat():
    global g_attack_status
    #global g_weapon_type

    threat_dist = randrange(10, 80, 10)
    g_weapon_type = randchoice(WEAPON_TYPES)
    g_attack_status = make_attack_status()

    print(f"THREAT - {threat_dist}FT - {g_weapon_type} - {g_attack_status}")

    play_sound(sound_threat)
    play_sound(sound_get_threat_dist(threat_dist))
    play_sound(sound_get_weapon_type(g_weapon_type))
    play_sound(sound_get_attack_status(g_attack_status))

    # Update attack status
    for _ in range(randint(3, 6)):
        new_attack_status = make_attack_status()
        print(new_attack_status)
        if new_attack_status != g_attack_status:
            play_sound(sound_get_attack_status(new_attack_status))
        g_attack_status = new_attack_status
        sleep(randint(2, 10))


def make_attack_status():
    # Chance for new weapon presentation
    #global g_weapon_type
    #if g_weapon_type == "NO WEAPON":
    #    if random() < .25:
    #        g_weapon_type = randchoice(WEAPON_TYPES)
    #        return f"{g_weapon_type} - {new_attack_status}"
    new_attack_status = randchoice(("IDLE", "AGGRESSIVE", "ATTACKING"))
    return f"{new_attack_status}"

def play_sound(sound: pygame.mixer.Sound):
    '''Blocking (waits for mixer)'''
    while pygame.mixer.get_busy():
        pass
    sound.play()
    #sound_channel.queue(sound)

def sound_get_weapon_type(weapon_type):
    match weapon_type:
        case "NO WEAPON": return sound_no_weapon
        case "BLADED WEAPON": return sound_bladed_weapon
        case "BLUNT WEAPON": return sound_blunt_weapon
        case "HANDGUN": return sound_handgun
        case "RIFLE": return sound_rifle
        case _: raise AssertionError("No sound for weapon type")

def sound_get_threat_dist(threat_dist):
    match threat_dist:
        case 10: return sound_10ft
        case 20: return sound_20ft
        case 30: return sound_30ft
        case 40: return sound_40ft
        case 50: return sound_50ft
        case 60: return sound_60ft
        case 70: return sound_70ft
        case 80: return sound_80ft
        case _: raise AssertionError("No sound for threat dist")

def sound_get_attack_status(attack_status):
    match attack_status:
        case "IDLE": return sound_idle
        case "AGGRESSIVE": return sound_aggressive
        case "ATTACKING": return sound_attacking
        case _: raise AssertionError("No sound for attack status")

if __name__ == "__main__":
    main()
    #try:
    #    main()
    #except Exception as e:
    #    play_sound(sound_error)
    #    sleep(1)
    #    raise(e)


#
#
#
#
#
#

