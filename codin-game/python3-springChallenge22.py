from collections import namedtuple
import math
import sys


# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

def distances(x, y, base_x, base_y):
    return math.sqrt((int(x) - int(base_x)) ** 2 + (int(y) - int(base_y)) ** 2)


def defend_base(base_x, ):
    if base_x == 0:
        print(f"MOVE 4300 3900 ID: {my_heroes[i].id + 1}")
    if base_x == 17630:
        print(f"MOVE 13100 5500 ID: {my_heroes[i].id + 1}")


Entity = namedtuple('Entity', [
    'id', 'type', 'x', 'y', 'shield_life', 'is_controlled', 'health', 'vx', 'vy', 'near_base', 'threat_for', "distance"
])

TYPE_MONSTER = 0
TYPE_MY_HERO = 1
TYPE_OP_HERO = 2

spells = ["MOVE", "SPELL WIND", "SPELL CONTROL"]

# base_x,base_y: The corner of the map representing your base
base_x, base_y = [int(i) for i in input().split()]
heroes_per_player = int(input())

if base_x == 0:
    my_base = "0 0"
    enemy_base = "17630 9000"
else:
    my_base = "17630 9000"
    enemy_base = "0 0"

turn = 0
rango_control = 2200

if base_x == 0:
    target = "3"
else:
    target = "0"

# game loop
while True:
    print(f"{base_x}", file=sys.stderr, flush=True)
    my_health, my_mana = [int(j) for j in input().split()]
    enemy_health, enemy_mana = [int(j) for j in input().split()]
    entity_count = int(input())  # Amount of heroes and monsters you can see

    turn += 1

    monsters = []
    my_heroes = []
    opp_heroes = []
    for i in range(entity_count):
        _id, _type, x, y, shield_life, is_controlled, health, vx, vy, near_base, threat_for = [int(j) for j in
                                                                                               input().split()]
        entity = Entity(
            _id,  # _id: Unique identifier
            _type,  # _type: 0=monster, 1=your hero, 2=opponent hero
            x, y,  # x,y: Position of this entity
            shield_life,  # shield_life: Ignore for this league; Count down until shield spell fades
            is_controlled,  # is_controlled: Ignore for this league; Equals 1 when this entity is under a control spell
            health,  # health: Remaining health of this monster
            vx, vy,  # vx,vy: Trajectory of this monster
            near_base,  # near_base: 0=monster with no target yet, 1=monster targeting a base
            threat_for,
            distance=distances(x, y, base_x, base_y)
            # threat_for: Given this monster's trajectory, is it a threat to 1=your base, 2=your opponent's base,
            # 0=neither
        )

        if _type == TYPE_MONSTER:
            monsters.append(entity)
        elif _type == TYPE_MY_HERO:
            my_heroes.append(entity)
        elif _type == TYPE_OP_HERO:
            opp_heroes.append(entity)

    monsters.sort(
        key=lambda x: x.distance
    )

    for i in range(len(monsters)):
        print(f"ID: {monsters[i].id}  D {monsters[i].distance}"
              f" InBase {monsters[i].near_base} Threat {monsters[i].threat_for}", file=sys.stderr, flush=True)

    for i in range(len(my_heroes)):

        if i == 0:
            if monsters:
                if monsters[i].distance < 1500 and (
                        distances(monsters[i].x, monsters[i].y, my_heroes[i].x, my_heroes[i].y) < 2100):
                    print(f"SPELL CONTROL {monsters[i].id} {enemy_base} ID: {my_heroes[i].id + 1}")
                elif monsters[i].distance < 3000 and ((monsters[i].x - my_heroes[i].x) < 200) and (
                        (monsters[i].y - my_heroes[i].y) < 200) and distances(monsters[i].x, monsters[i].y, my_heroes[i].x, my_heroes[i].y) < 200 :
                    print(f"SPELL WIND {enemy_base}")
                else:
                    print(f"MOVE {monsters[i].x} {monsters[i].y} ID: {my_heroes[i].id + 1}")
            else:
                defend_base(base_x)


        elif i == 1:
            if len(monsters) >= 2:
                if monsters[i].distance < 1500 and (
                        distances(monsters[i].x, monsters[i].y, my_heroes[i].x, my_heroes[i].y) < 2100):
                    print(f"SPELL CONTROL {monsters[i].id} {enemy_base} ID: {my_heroes[i].id + 1}")
                elif monsters[i].distance < 3000 and ((monsters[i].x - my_heroes[i].x) < 200) and (
                        (monsters[i].y - my_heroes[i].y) < 200):
                    print(f"SPELL WIND {enemy_base}")
                else:
                    print(f"MOVE {monsters[i].x} {monsters[i].y} ID: {my_heroes[i].id + 1}")
            elif len(monsters) == 1:
                print(f"MOVE {monsters[0].x} {monsters[0].y} ID: {my_heroes[i].id + 1}")
            else:
                if base_x == 0:
                    print(f"MOVE 3000 5500 ID: {my_heroes[i].id + 1} ")
                else:
                    print(f"MOVE 10839 6470 {my_heroes[i].id + 1}")



        elif i == 2:
            if turn > 145:
                if my_heroes[i].distance <= 14000:
                    print(f"MOVE {enemy_base}")
                elif my_heroes[i].distance > 14000:
                    if turn < 195:
                        print(f"SPELL CONTROL {target} {my_base} ID: {my_heroes[2].id + 1}")
                    else:
                        print(f"SPELL WIND {enemy_base}")

            else:
                if len(monsters) >= 3:

                    if my_mana > 300 and (
                        distances(monsters[i].x, monsters[i].y, my_heroes[i].x, my_heroes[i].y) < 2100):
                        print(f"SPELL CONTROL {monsters[i].id} {enemy_base} ID: {my_heroes[i].id + 1}")
                    else:
                        print(f"MOVE {monsters[i].x} {monsters[i].y} ID: {my_heroes[i].id + 1}")
                elif i == 2 and len(monsters) >= 2:
                    print(f"MOVE {monsters[1].x} {monsters[1].y} ID: {my_heroes[i].id + 1}")
                else:
                    if base_x == 0:
                        print(f"MOVE 6400 2000 ID: {my_heroes[i].id + 1} ")
                    else:
                        print(f"MOVE 15363 3761 {my_heroes[i].id + 1}")                 
