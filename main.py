#We import all the classes used in the game
import pyxel
import Creature
import Player
import Colision_System
import Bullets
import Regular_Enemy
import Enemy_Manager
import Background



#Creation of the objects used. The player, the background, the enemies, and the colision system
Height = 256
Width = 224
pyxel.init(Width , Height, "1492")
player = Player.Player(16,27,150,150,2,4,5,4)
Colision = Colision_System.Colision_System(player,[],[])
enemy_manager = Enemy_Manager.Enemy_Manager()
background = Background.Background(115,15,90,10)





def update():
    #At the beggining of the game the update of the rest of the objects will not be used.
    if background.value != 0 and player.hurt == False:
        player.update()
        #we give the enemy manager the position of the player.
        enemy_manager.position_player_y = player.position_y
        enemy_manager.position_player_x = player.position_x
        enemy_manager.update()
        #We give the colision system a copy of the enemies
        Colision.enemies = enemy_manager.Total_Enemies.copy()
        Colision.update()
        #The result of the colision system is given to the enemy manager and the background
        enemy_manager.enemies_hit = Colision.Enemies_hit
        background.enemy_dead = Colision.Enemies_hit
        background.Total_Enemies = enemy_manager.Total_Enemies
        #We give the bull manager of the player the result of the colision system
        player.Bull_manager.bullets_hitted = Colision.Bullets_hit
        background.turns = player.turns
    #Moment player has been hitted.
    elif background.value != 0 and player.hurt == True:
        player.position_x = 60
        player.position_y = 170
        #We clear the list of enemies and bullets from the screen.
        enemy_manager.Total_Enemies.clear()
        enemy_manager.enemies_hit.clear()
        Colision.Enemies_hit.clear()
        Colision.bullets_enemies.clear()
    #If player lives gets to 0 the game ends
        if player.health <= -2:
            pyxel.quit()
    #When hurt we resume the game pressing X
        elif pyxel.btn(pyxel.KEY_X):
            player.hurt = False

    background.update()
    enemy_manager.score = background.score

def draw():
    #We call the background, player and enemy draws.
    if background.value != 0:
        pyxel.cls(1)
        player.draw()
        enemy_manager.draw()
    if background.value != 0 and player.hurt == True:
        pyxel.cls(1)
        player.draw()
        enemy_manager.draw()
        background.player_dead()
    background.draw()






pyxel.run(update,draw)



