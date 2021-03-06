"""
Title: Prison Peril
Creators: Michael W. and Jason B.
Description: The guy is doing stuff! oh crap!
"""
@namespace 
class SpriteKind():
    guide = SpriteKind.create()
@namespace
class SpriteKind():
    tunnel = SpriteKind.create()

# Merek = sprites.create(img("""
#     . . . . . . . . . . . . . . . .
#     . . . . . . . . . . . . . . . .
#     . . . . f f f f f f f f . . . .
#     . . . f 4 4 e 4 4 4 4 1 f f . .
#     . . f f 4 4 4 4 4 4 4 f 4 f . .
#     . . f 4 1 4 4 4 4 4 e 4 4 f . .
#     . f e 4 f 4 4 4 4 4 4 4 f . f .
#     . f f 4 4 4 f f f f 4 f . . f .
#     . f . f f 4 e 4 4 4 f f . . f .
#     . f . . f f f f f f f . . . f .
#     . f . . f f f . f f f . . f . f
#     f . f f f f f . f f f f . . . .
#     . . . f f f . . . f f f . . . .
#     . . . f f . . . . f f f . . . .
#     . . . f . . . . . . . f . . . .
#     . . . . . . . . . . . . . . . .
# """), SpriteKind.player)

#Guide
guide1 = sprites.create(img("""
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . 1 1 b b 1 1 . . . . .
    . . . . . 1 b f f b 1 . . . . .
    . . . . . b f f f f b . . . . .
    . . . . . b f f f f b . . . . .
    . . . . . 1 b f f b 1 . . . . .
    . . . . . 1 1 b b 1 1 . . . . .
"""), SpriteKind.guide)
guide1.set_position(400, 264)
guide1.say("Keep an Eye Out For Coins!")
guide2 = sprites.create(img("""
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . 1 1 b b 1 1 . . . . .
    . . . . . 1 b f f b 1 . . . . .
    . . . . . b f f f f b . . . . .
    . . . . . b f f f f b . . . . .
    . . . . . 1 b f f b 1 . . . . .
    . . . . . 1 1 b b 1 1 . . . . .
"""), SpriteKind.guide)
guide2.set_position(500, 328)
guide2.say("Push the Box, and Jump on Top When it Finishes Moving")
guide3 = sprites.create(img("""
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . 1 1 b b 1 1 . . . . .
    . . . . . 1 b f f b 1 . . . . .
    . . . . . b f f f f b . . . . .
    . . . . . b f f f f b . . . . .
    . . . . . 1 b f f b 1 . . . . .
    . . . . . 1 1 b b 1 1 . . . . .
"""), SpriteKind.guide)
guide3.set_position(895, 168)
guide3.say("Clearly Nothing This Way....")
guide4 = sprites.create(img("""
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . 1 1 b b 1 1 . . . . .
    . . . . . 1 b f f b 1 . . . . .
    . . . . . b f f f f b . . . . .
    . . . . . b f f f f b . . . . .
    . . . . . 1 b f f b 1 . . . . .
    . . . . . 1 1 b b 1 1 . . . . .
"""), SpriteKind.guide)
guide4.set_position(645, 120)
guide4.say("Look For Holes In the Wall")
guide5 = sprites.create(img("""
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . 1 1 b b 1 1 . . . . .
    . . . . . 1 b f f b 1 . . . . .
    . . . . . b f f f f b . . . . .
    . . . . . b f f f f b . . . . .
    . . . . . 1 b f f b 1 . . . . .
    . . . . . 1 1 b b 1 1 . . . . .
"""), SpriteKind.guide)
guide5.set_position(1495, 312)
guide5.say("Space Jumps to Get Higher")
guide6 = sprites.create(img("""
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . 1 1 b b 1 1 . . . . .
    . . . . . 1 b f f b 1 . . . . .
    . . . . . b f f f f b . . . . .
    . . . . . b f f f f b . . . . .
    . . . . . 1 b f f b 1 . . . . .
    . . . . . 1 1 b b 1 1 . . . . .
"""), SpriteKind.guide)
guide6.set_position(62, 312)
guide6.say("Excape the Dungeon to Escape! Watch for Lava and Other Obstacles")
Merek_right = img("""
    . . . . . . . . . . e e . . . .
    . . . . . . e e e e e e . . . .
    . . . . . . e d d d d . . . . .
    . . . . . . d d f d f . . . . .
    . . . . . . d d d d d . . . . .
    . . . . . . . . 4 . . . . . . .
    . . . . . . 4 4 4 4 4 . . . . .
    . . . . . . 4 4 4 4 4 . . . . .
    . . . . . . 4 4 4 4 4 . . . . .
    . . . . . . 4 4 4 4 4 . . . . .
    . . . . . . d f f f d . . . . .
    . . . . . . . 4 4 4 . . . . . .
    . . . . . . . 4 . 4 . . . . . .
    . . . . . . . 4 . 4 . . . . . .
    . . . . . . . 4 . 4 . . . . . .
    . . . . . . e e . e e . . . . .
""")
Merek_left = img("""
    . . . . . e e . . . . . . . . .
    . . . . . e e e e e e . . . . .
    . . . . . . d d d d e . . . . .
    . . . . . . f d f d d . . . . .
    . . . . . . d d d d d . . . . .
    . . . . . . . . 4 . . . . . . .
    . . . . . . 4 4 4 4 4 . . . . .
    . . . . . . 4 4 4 4 4 . . . . .
    . . . . . . 4 4 4 4 4 . . . . .
    . . . . . . 4 4 4 4 4 . . . . .
    . . . . . . d f f f d . . . . .
    . . . . . . . 4 4 4 . . . . . .
    . . . . . . . 4 . 4 . . . . . .
    . . . . . . . 4 . 4 . . . . . .
    . . . . . . . 4 . 4 . . . . . .
    . . . . . . e e . e e . . . . .
""")
Merek_jump_right = img("""
    . . . . . . . . e e e . . . . .
    . . . . d . . e e e e . d . . .
    . . . . 4 . e e d d f . 4 . . .
    . . . . 4 . e d f d d . 4 . . .
    . . . . 4 . d d d d d . 4 . . .
    . . . . . 4 . . 4 . . 4 . . . .
    . . . . . . 4 4 4 4 4 . . . . .
    . . . . . . . 4 4 4 . . . . . .
    . . . . . . . 4 4 4 . . . . . .
    . . . . . . . 4 4 4 . . . . . .
    . . . . . . . f f f . . . . . .
    . . . . . . . 4 4 4 . . . . . .
    . . . . . . . 4 . 4 . . . . . .
    . . . . e 4 4 e 4 . . . . . . .
    . . . . e . . e . . . . . . . .
    . . . . . . . . . . . . . . . .
""")
Merek_jump_left = img("""
    . . . . . . e e e . . . . . . .
    . . . . d . e e e e . . d . . .
    . . . . 4 . f d d e e . 4 . . .
    . . . . 4 . d d f d e . 4 . . .
    . . . . 4 . d d d d d . 4 . . .
    . . . . . 4 . . 4 . . 4 . . . .
    . . . . . . 4 4 4 4 4 . . . . .
    . . . . . . . 4 4 4 . . . . . .
    . . . . . . . 4 4 4 . . . . . .
    . . . . . . . 4 4 4 . . . . . .
    . . . . . . . f f f . . . . . .
    . . . . . . . 4 4 4 . . . . . .
    . . . . . . . 4 . 4 . . . . . .
    . . . . . . . . 4 e 4 4 e . . .
    . . . . . . . . . e . . e . . .
    . . . . . . . . . . . . . . . .
""")
coin = sprites.create(img("""
    . . . . . . . . . . . . . . . .
    . . . . . . 5 5 2 4 . . . . . .
    . . . . . 5 5 5 5 2 4 . . . . .
    . . . . 5 5 5 5 5 5 2 4 . . . .
    . . . . 5 5 5 4 5 5 2 4 . . . .
    . . . . 5 5 5 4 5 5 2 4 . . . .
    . . . . 5 5 5 4 5 5 2 4 . . . .
    . . . . 5 5 5 4 5 5 2 4 . . . .
    . . . . 5 5 5 4 5 5 2 4 . . . .
    . . . . 5 5 5 4 5 5 2 4 . . . .
    . . . . 5 5 5 4 5 5 2 4 . . . .
    . . . . 5 5 5 5 5 5 2 4 . . . .
    . . . . 5 5 5 5 5 5 2 4 . . . .
    . . . . . 5 5 5 5 2 4 . . . . .
    . . . . . . 5 5 5 4 . . . . . .
    . . . . . . . . . . . . . . . .
"""),SpriteKind.projectile)
coin.set_position(1175, 100)
# SpriteKind.create(movable) 
block = sprites.create(img("""
    444444444444444444444444444444444444444444444444444444444444444e
    44444444444444444444444444444444444444444444444444444444444f44ee
    4444444444444444444444444444444444444444444444444444444444444eee
    444444f44444444444444444444444444444444444444444444444444444eeee
    44444444444444444444444444444444444444444444444444444444444eeefe
    4444444444444444444444444444444444444444444444444444444444eeeeee
    44f44444444bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbeeeeee
    444444444444bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbeeeeee
    4444444444444bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbeeeeee
    44444444444444bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbeeeeee
    444444444444444bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbeeeeee
    444444b444444444bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbeeeeee
    444444bb444444444bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbeeeeee
    444444bbb444444444bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbeeeeee
    444444bbbb444444444bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbeeeeee
    444444bbbbb444444444bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbeeeeee
    444444bbbbbb444444444bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbeeeeee
    444444bbbbbbb444444444bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbeeeeee
    444444bbbbbbbb444444444bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbeeeeee
    444444bbbbbbbbb444444444bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbeeeeee
    444444bbbbbbbbbb444444444bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbeeeeee
    444444bbbbbbbbbbb444444444bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbeeeeee
    444444bbbbbbbbbbbb444444444bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbeeeeee
    444444bbbbbbbbbbbbb444444444bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbeeeeee
    444444bbbbbbbbbbbbbb444444444bbbbbbbbbbbbbbbbbbbbbbbbbbbbbeeeeee
    444444bbbbbbbbbbbbbbb444444444bbbbbbbbbbbbbbbbbbbbbbbbbbbbeeeeee
    444444bbbbbbbbbbbbbbbb444444444bbbbbbbbbbbbbbbbbbbbbbbbbbbeeeeee
    444444bbbbbbbbbbbbbbbbb444444444bbbbbbbbbbbbbbbbbbbbbbbbbbeeeeee
    444444bbbbbbbbbbbbbbbbbb444444444bbbbbbbbbbbbbbbbbbbbbbbbbeeeeee
    444444bbbbbbbbbbbbbbbbbbb444444444bbbbbbbbbbbbbbbbbbbbbbbbeeeeee
    444444bbbbbbbbbbbbbbbbbbbb44444444ebbbbbbbbbbbbbbbbbbbbbbbeeeeee
    444444bbbbbbbbbbbbbbbbbbbbb444444eeebbbbbbbbbbbbbbbbbbbbbbeeeeee
    444444bbbbbbbbbbbbbbbbbbbbbb4444eeeeebbbbbbbbbbbbbbbbbbbbbeeeeee
    444444bbbbbbbbbbbbbbbbbbbbbbb44eeeeeeebbbbbbbbbbbbbbbbbbbbeeeeee
    444444bbbbbbbbbbbbbbbbbbbbbbbbeeeeeeeeebbbbbbbbbbbbbbbbbbbeeeeee
    444444bbbbbbbbbbbbbbbbbbbbbbbbbeeeeeeeeebbbbbbbbbbbbbbbbbbeeeeee
    444444bbbbbbbbbbbbbbbbbbbbbbbbbbeeeeeeeeebbbbbbbbbbbbbbbbbeeeeee
    444444bbbbbbbbbbbbbbbbbbbbbbbbbbbeeeeeeeeebbbbbbbbbbbbbbbbeeeeee
    444444bbbbbbbbbbbbbbbbbbbbbbbbbbbbeeeeeeeeebbbbbbbbbbbbbbbeeeeee
    444444bbbbbbbbbbbbbbbbbbbbbbbbbbbbbeeeeeeeeebbbbbbbbbbbbbbeeeeee
    444444bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbeeeeeeeeebbbbbbbbbbbbbeeeeee
    444444bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbeeeeeeeeebbbbbbbbbbbbeeeeee
    444444bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbeeeeeeeeebbbbbbbbbbbeeeeee
    444444bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbeeeeeeeeebbbbbbbbbbeeeeee
    444444bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbeeeeeeeeebbbbbbbbbeeeeee
    444444bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbeeeeeeeeebbbbbbbbeeeeee
    444444bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbeeeeeeeeebbbbbbbeeeeee
    444444bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbeeeeeeeeebbbbbbeeeeee
    444444bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbeeeeeeeeebbbbbeeeeee
    444444bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbeeeeeeeeebbbbeeeeee
    444444bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbeeeeeeeeebbbeeeeee
    444444bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbeeeeeeeeebbeeeeee
    444444bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbeeeeeeeeebeeeeee
    444444bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbeeeeeeeeeeeeeee
    444444bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbeeeeeeeeeeeeee
    444444bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbeeeeeeeeeeeee
    444444bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbeeeeeeeeeeee
    444444bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbeeeeeeeefee
    444444bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbeeeeeeeeee
    44444eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
    4f44eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
    444eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefeeeeee
    44eefeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
    4eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
"""), SpriteKind.food)
# scene.place_on_random_tile(block, 3)
Merek = sprites.create(Merek_right, SpriteKind.player)
scene.set_background_color(0)
info.set_life(3)
scene.camera_follow_sprite(Merek)
controller.move_sprite(Merek, 75, 0)
coin1 = sprites.create(img("""
    . . . . . . . . . . . . . . . .
    . . . . . . 5 5 2 4 . . . . . .
    . . . . . 5 5 5 5 2 4 . . . . .
    . . . . 5 5 5 5 5 5 2 4 . . . .
    . . . . 5 5 5 4 5 5 2 4 . . . .
    . . . . 5 5 5 4 5 5 2 4 . . . .
    . . . . 5 5 5 4 5 5 2 4 . . . .
    . . . . 5 5 5 4 5 5 2 4 . . . .
    . . . . 5 5 5 4 5 5 2 4 . . . .
    . . . . 5 5 5 4 5 5 2 4 . . . .
    . . . . 5 5 5 4 5 5 2 4 . . . .
    . . . . 5 5 5 5 5 5 2 4 . . . .
    . . . . 5 5 5 5 5 5 2 4 . . . .
    . . . . . 5 5 5 5 2 4 . . . . .
    . . . . . . 5 5 5 4 . . . . . .
    . . . . . . . . . . . . . . . .
"""),SpriteKind.projectile)
coin1.set_position(370, 215)
Merek.ay = 300
block.ay = 99999
def on_button_event_a_pressed():
    Merek.vy = -150
controller.player1.on_button_event(ControllerButton.A, ControllerButtonEvent.PRESSED, on_button_event_a_pressed)
if not Merek.is_hitting_tile(CollisionDirection.BOTTOM):
    Merek_jump_right = img("""
    . . . . . . . . e e e . . . . .
    . . . . d . . e e e e . d . . .
    . . . . 4 . e e d d f . 4 . . .
    . . . . 4 . e d f d d . 4 . . .
    . . . . 4 . d d d d d . 4 . . .
    . . . . . 4 . . 4 . . 4 . . . .
    . . . . . . 4 4 4 4 4 . . . . .
    . . . . . . . 4 4 4 . . . . . .
    . . . . . . . 4 4 4 . . . . . .
    . . . . . . . 4 4 4 . . . . . .
    . . . . . . . f f f . . . . . .
    . . . . . . . 4 4 4 . . . . . .
    . . . . . . . 4 . 4 . . . . . .
    . . . . e 4 4 e 4 . . . . . . .
    . . . . e . . e . . . . . . . .
    . . . . . . . . . . . . . . . .
    """)

scene.set_tile_map(img("""
    cccccccc666666666666666666666ccccccccccccc.....................ccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
    cccccccc666666666666666666666ccccccccccccc......................cccccccccccccccccccccccccccccccccccccccccccccccccccccccc
    cccccccc6666666366666666666666cccccccccccc.......................ccccccccccccccccccccccccccccc66666666666666666666666ccc
    cccccccc66666666666666366666666ccccccccccc.......................ccccc......ccccccccccccccccc6666666666666666666666666cc
    cccccccc666666666666666666666666cccccccccc......................cccc.........cccccccccccccccc6666666666366666666666666cc
    cccccccc6666666666666666666666666ccccccccc......................cccc.........cccccccccccccccc66666bbbb6666666666666666cc
    cccccccc66666666666666666666666666cccc6666...................................cccccccccccccccc6666beccab666666666666666cc
    cccccccc666636666666666666666666666ccc.6666..................................cccccccccccccccc6666cccccc666666666666666cc
    cccccccc6666666663666666666666666666cabbbbb......................ccccc......ccccccccccccccccab666cccccc666666666666666cc
    cccccccc6666666663666663666666366666666666.....................cccccccccccccccccccccccccccccc6666cccccc666636666666666cc
    cccccccc666666666666666666666666666666666.....bbbb.............cccccccccccccccccccccccccccccc6366cccccc666666666666666cc
    cccccccc663666666666666666666666666666666......1f.....bbbb.....cccccccccccccccccccccccccccccc636beccccc666666666666666cc
    cccccccc66666666666666666666666666666636.......1f......1f......cccccccccccccccccccccccccccccc6666cccccc666666666666666cc
    cccccccc66666336666663666666666666666633.......1f..bbbb1f......cccccccccccccccccccccccccccccc6666cccccc666666666666666cc
    cccccccc6666663666663666666636666636663........1f...1f.1f......cccccccccccccccccccccccccccccab663cccccc666336666666666cc
    cccccccc66666663666666666666666666366666..bbbbbbbb..1f.1f......ccccccccccccccccccccccccccccc66666cccccc666666666666666cc
    cccccccc6666666666666666666666666666666....1f..1f...1f.1f......ccc666666666666666cccccccccc666666cccccc666666666636666cc
    c.8...8.66666666666777777777666666665555...1f..1f...1f.1f......ccc6666663366666663666666666666666cccccc666666666636666cc
    c.......6666666666becccccccc666666666666...1f..1f...1f.1f......ccc666663366666666636666663666666beccccc999977777666666cc
    c...d...666666666beccccccccc6666336666636..1f..1f...1f.1f......ccc66666666666666666666666666666becccccabbbbecccc777666cc
    abbbbbb.bbbbbbbbbecccccccccc666633666666b..1f..1f...1f.1f......ccc666666666666666bbbbbbbbbbbbbbeccccccccccccccccccc666cc
    ccccccc.cccccccccccccccccccabbbbbbbbbbbbe441f441f4441f41f444444cccbbbbbbbbbbbbbbbeccccccccccccccccccccccccccccccccc666cc
    ccccccc.ccccccccccccccccccccccccccccccccc221f221f2221f21f222222cccccccccccccccccccccccccccccccccccccccccccccccccccc666cc
    ccccccc.ccccccccccccccccccccccccccccccccc221f221f2221f21f222222cccccccccccccccccccccccccccccccccccccccccccccccccccc663cc
    ccccccc.ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc666cc
    ccccccc.ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc666cc
    ccccccc.ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc666cc
    .cc..............ccccccc....666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666cc
    .................cccccc.....666666666666666666663666666666666663666366666666666666666636666666666666666666666666666666cc
    .................ccccc......666366666666636666666666663677776663366666666666366663666633666666333666666666666366666666cc
    .................cccc.......6666666666666666666336666366cccc6666666666636666666666666663366666666666666666666666666bbbec
    .......cc........ccc....bbbb6633666663666666666366666666cccc6677776666663666666.6666.66666666666666666666666666666becccc
    .........c.......cc....beccc66636666666366636666666666..cccc66cccc66..6666666666666666666666666666.66666666666666beccccc
    .........cc...........becccc666666666666666..................6cccc6..6..66.6.77777777.6....6...6666..666...66666becccccc
    ...........cc........beccccabbbbbbbbb77777.......777..........cccc..777777...cccccccc........777777.......777777eccccccc
    ............cc......becccccccccccccccccccc4444444ccc4444cccc44cccc44cccccc444cccccccc44444444cccccc4444444cccccccccccccc
    ..............cc.bbbeccccccccccccccccccccc22222222cc2222ccc2222ccc222cccc22222cccccc2222222222cccc222222222ccccccccccccc
    ...............c.cccccccccccccccccccccccc222222222cc2222cc222222c2222ccc2c2222ccccc2222222222222cc2222222222cccccccccccc
    ................cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
    .................ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
    ........................................................................................................................
    ........................................................................................................................
    ........................................................................................................................
    ........................................................................................................................
    ........................................................................................................................
    ........................................................................................................................
    ........................................................................................................................
    ........................................................................................................................
"""))
scene.set_tile(10, img("""
    b b b b b b b b b b b b b d d d
    b c c c c c c c b c c c c c c c
    b c c c c c c c b c c c c c c c
    b c c c c c c c b c c c c c c c
    b b b b b b b b b b b b b b b b
    c c c c c b c c c c c c b c c c
    c c c c c b c c c c c c b c c c
    c c c c c b c c c c c c b c c c
    b b b b b b b b b b b b b b b b
    b c c c c c c c b c c c c c c c
    b c c c c c c c b c c c c c c c
    b c c c c c c c b c c c c c c c
    b b b b b b b b b b b b b b b b
    c c c c c b c c c c c c b c c c
    c c c c c b c c c c c c b c c c
    c c c c c b c c c c c c b c c c
"""),True)
scene.set_tile(11, img("""
    d d d d d d d d d d d d d d d d
    d c c c c c c c d c c c c c c c
    b c c c c c c c b c c c c c c c
    b c c c c c c c b c c c c c c c
    b b b b b b b b b b b b b b b b
    c c c c c b c c c c c c b c c c
    c c c c c b c c c c c c b c c c
    c c c c c b c c c c c c b c c c
    b b b b b b b b b b b b b b b b
    b c c c c c c c b c c c c c c c
    b c c c c c c c b c c c c c c c
    b c c c c c c c b c c c c c c c
    b b b b b b b b b b b b b b b b
    c c c c c b c c c c c c b c c c
    c c c c c b c c c c c c b c c c
    c c c c c b c c c c c c b c c c
"""),True)
scene.set_tile(12, img("""
    b b b b b b b b b b b b b b b b
    b c c c c c c c b c c c c c c c
    b c c c c c c c b c c c c c c c
    b c c c c c c c b c c c c c c c
    b b b b b b b b b b b b b b b b
    c c c c b c c c c c c c b c c c
    c c c c b c c c c c c c b c c c
    c c c c b c c c c c c c b c c c
    b b b b b b b b b b b b b b b b
    b c c c c c c c b c c c c c c c
    b c c c c c c c b c c c c c c c
    b c c c c c c c b c c c c c c c
    b b b b b b b b b b b b b b b b
    c c c c b c c c c c c c b c c c
    c c c c b c c c c c c c b c c c
    c c c c b c c c c c c c b c c c
"""),True)
scene.set_tile(14, img("""
    d d d d b b b b b b b b b b b b
    d c c c c c c c b c c c c c c c
    b c c c c c c c b c c c c c c c
    b c c c c c c c b c c c c c c c
    b b b b b b b b b b b b b b b b
    c c c c b c c c c c c c b c c c
    c c c c b c c c c c c c b c c c
    c c c c b c c c c c c c b c c c
    b b b b b b b b b b b b b b b b
    b c c c c c c c b c c c c c c c
    b c c c c c c c b c c c c c c c
    b c c c c c c c b c c c c c c c
    b b b b b b b b b b b b b b b b
    c c c c b c c c c c c c b c c c
    c c c c b c c c c c c c b c c c
    c c c c b c c c c c c c b c c c
"""),True)
scene.set_tile(4, img("""
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . 4 4 . . 4 4 4 . 4 4 . 4 4 4 .
    4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4
    4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4
    4 4 4 4 4 4 4 4 4 4 4 4 2 2 4 4
    4 2 2 4 4 2 2 4 4 2 2 4 2 2 2 4
    2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2
    2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2
    2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2
    2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2
    2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2
"""),True)
scene.set_tile(13, img("""
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . f . . . . . .
    . . . . . . . . f b f . . . . .
    . . . . . . . f b b f . . . . .
    . . . . . . f b 1 b f . . . . .
    . . . . . . f b 1 1 f . . . . .
    . . . . . f b 1 1 1 f . . . . .
    . . . . . f 1 1 1 1 f . . . . .
    . . . . . f 1 1 1 1 f . . . . .
    . . . . . f 1 1 1 1 f . . . . .
    . . . . . f 1 1 1 1 f . . . . .
    . . . . . f 1 1 1 1 f . . . . .
    . . . . . f 1 1 1 1 f . . . . .
    . . . . . f 1 1 1 1 f . . . . .
"""),False)
scene.set_tile(8, img("""
    . . . . . 1 1 1 1 1 . . . . . .
    . . . . . d 1 1 1 1 . . . . . .
    . . . . . d 1 1 1 1 . . . . . .
    . . . . . d 1 d 1 1 . . . . . .
    . . . . . d d 1 1 1 . . . . . .
    . . . . . d d 1 b 1 . . . . . .
    . . . . . d 1 1 b 1 . . . . . .
    . . . . . b 1 1 1 1 . . . . . .
    . . . . . b 1 1 1 1 . . . . . .
    . . . . . 1 1 1 1 1 . . . . . .
    . . . . . 1 1 1 b b . . . . . .
    . . . . . 1 1 1 1 b . . . . . .
    . . . . . . 1 1 1 b . . . . . .
    . . . . . . . 1 1 b . . . . . .
    . . . . . . . . 1 1 . . . . . .
    . . . . . . . . . 1 . . . . . .
"""),False)
scene.set_tile(7, img("""
    7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7
    7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7
    7 7 7 7 7 7 7 7 7 7 7 7 7 7 7 7
    7 7 7 7 6 7 7 7 6 6 7 7 7 7 7 7
    6 7 7 6 b 6 7 7 6 6 7 7 7 6 6 7
    c 6 6 c c b 6 6 c 6 7 7 7 6 6 6
    7 c c c c b c c c 6 6 7 7 6 c c
    c c c c c b c c c c 6 7 6 c c c
    b b b b b b b b b b 6 6 b b b b
    b c c c c c c c b c c c c c c c
    b c c c c c c c b c 7 c c c c c
    b c c c c c c c b c c c c c c c
    b b b b b b b b b b b b b b b b
    c c c c c b c c c c c c b c c c
    c c c c c b c c c c c c b c c c
    c c c c c b c c c c c c b c c c
"""),True)
scene.set_tile(9, img("""
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    8 8 8 8 8 7 3 7 7 7 8 8 8 8 8 8
    8 8 8 8 7 3 5 3 7 7 7 8 8 8 8 8
    8 8 8 8 8 7 3 7 7 7 8 8 8 8 8 8
    8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8
    8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8
    8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8
    8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8
    8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8
    8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8
    8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8
    8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8
    8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8
    8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8
    8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8
"""))
scene.set_tile(3, img("""
    c 6 7 7 7 c c c c c c c c c c c
    c 6 7 6 b b b b b b b b b b b b
    c b 6 7 b b b b b b b b b b b b
    c b b 6 6 7 7 b b b b b b b b b
    c b b b b 6 6 7 6 b b b b b b b
    c b b b b b 6 6 6 b b b b b b b
    c b b b b b b 6 7 7 b b b b b b
    c b b b b b 6 6 6 6 7 b b b b b
    c c c c c c 7 6 c c 6 7 7 7 c c
    b b b b b 7 6 6 c b b 6 6 7 b b
    b b b b b 7 6 6 c b b b b 6 b b
    b b b b 7 6 7 6 c b b b b 6 7 b
    b b b b 6 6 6 7 c b b b b b 7 b
    b b b b b 6 6 6 c b b b b 7 b b
    b b 6 6 7 7 7 7 c b b b b b b b
    b 6 6 7 6 7 b b c b b b b b b b
"""),False)
scene.set_tile(6, img("""
    c c c c c c c c c c c c c c c c
    c b b b b b b b b b b b b b b b
    c b b b b b b b b b b b b b b b
    c b b b b b b b b b b b b b b b
    c b b b b b b b b b b b b b b b
    c b b b b b b b b b b b b b b b
    c b b b b b b b b b b b b b b b
    c b b b b b b b b b b b b b b b
    c c c c c c c c c c c c c c c c
    b b b b b b b b c b b b b b b b
    b b b b b b b b c b b b b b b b
    b b b b b b b b c b b b b b b b
    b b b b b b b b c b b b b b b b
    b b b b b b b b c b b b b b b b
    b b b b b b b b c b b b b b b b
    b b b b b b b b c b b b b b b b
"""),False)
scene.set_tile(5, img("""
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
"""),False)
scene.set_tile(1, img("""
    . . d b c b b c c b b c c b b c
    . . d b c b b c c b b c c b b c
    . . d b c b b c c b b c c b b c
    . . d b c b b c c b b c c b b c
    . . d b c b b c c b b c c b b c
    . . d b c b b c c b b c c b b c
    . . d b c b b c c b b c c b b c
    . . d b c b b c c b b c c b b c
    . . d b c b b c c b b c c b b c
    . . d b c b b c c b b c c b b c
    . . d b c b b c c b b c c b b c
    . . d b c b b c c b b c c b b c
    . . d b c b b c c b b c c b b c
    . . d b c b b c c b b c c b b c
    . . d b c b b c c b b c c b b c
    . . d b c b b c c b b c c b b c
"""),False)
scene.set_tile(15, img("""
    c b b c c b b c c b b c b a . .
    c b b c c b b c c b b c b a . .
    c b b c c b b c c b b c b a . .
    c b b c c b b c c b b c b a . .
    c b b c c b b c c b b c b a . .
    c b b c c b b c c b b c b a . .
    c b b c c b b c c b b c b a . .
    c b b c c b b c c b b c b a . .
    c b b c c b b c c b b c b a . .
    c b b c c b b c c b b c b a . .
    c b b c c b b c c b b c b a . .
    c b b c c b b c c b b c b a . .
    c b b c c b b c c b b c b a . .
    c b b c c b b c c b b c b a . .
    c b b c c b b c c b b c b a . .
    c b b c c b b c c b b c b a . .
"""),False)
def on_hit_tile(sprite):
    info.change_life_by(-3)
scene.on_hit_tile(SpriteKind.player, 4, on_hit_tile)
def on_overlap_tile(sprite, location):
    info.player1.change_life_by(-1)
    scene.on_overlap_tile(SpriteKind.player, img("""
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . 4 4 . . 4 4 4 . 4 4 . 4 4 4 .
    4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4
    4 4 4 4 4 4 4 4 4 4 4 4 2 2 4 4
    4 2 2 4 4 2 2 4 4 2 2 4 2 2 2 4
    2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2
    2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2
    2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2
    2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2
    2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2
    2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2
"""), on_overlap_tile)
tiles.place_on_tile(Merek, tiles.get_tile_location(2, 19))
meany = sprites.create(img("""
    . . . . 2 2 2 2 2 2 . . . . . .
    . . . 2 2 2 2 2 2 2 2 2 . . . .
    . . 2 2 f 2 2 2 2 2 2 2 2 . . .
    . . 2 2 2 2 2 2 2 2 2 2 2 . . .
    . . 2 2 2 2 2 2 2 2 f 2 2 . . .
    . . . 2 2 f f f 2 2 2 2 2 . . .
    . . . 2 2 2 2 2 2 2 2 2 . . . .
    . . . . . 5 2 2 2 5 . . . . . .
    . . . . 2 2 5 2 5 2 2 . . . . .
    . . . 2 . 2 2 5 2 2 . 2 . . . .
    . . . 2 . 2 5 2 5 2 . 2 . . . .
    . . . 2 . 5 2 2 2 5 . 2 . . . .
    . . . . . 2 . . . 2 . . . . . .
    . . . . . 2 . . . 2 . . . . . .
    . . . . . 2 . . . 2 . . . . . .
    . . . . . 2 . . . 2 . . . . . .
"""), SpriteKind.enemy)
tiles.place_on_tile(meany, tiles.get_tile_location(6, 19))
tiles.place_on_tile(block, tiles.get_tile_location(33, 18))
block.ay = 200

canDoublejump = True
controller.move_sprite(Merek ,75, 0) 
def on_jump():
    global canDoublejump
    if Merek.is_hitting_tile(CollisionDirection.BOTTOM) or canDoublejump:
        Merek.vy = -150
        canDoublejump = Merek.is_hitting_tile(CollisionDirection.BOTTOM)
controller.player1.on_button_event(ControllerButton.A,ControllerButtonEvent.PRESSED,on_jump)

def on_overlap(sprite, otherSprite):
    info.change_life_by(-1)
sprites.on_overlap(SpriteKind.player, SpriteKind.enemy, on_overlap)

def on_update():
    if controller.dx() > 0:
        Merek.set_image(Merek_right)
    elif controller.dx() < 0:
        Merek.set_image(Merek_left)
    if not Merek.is_hitting_tile(CollisionDirection.BOTTOM):
        Merek_jump_right = img("""
               . . . . . . . . e e e . . . . .
               . . . . d . . e e e e . d . . .
               . . . . 4 . e e d d f . 4 . . .
               . . . . 4 . e d f d d . 4 . . .
               . . . . 4 . d d d d d . 4 . . .
               . . . . . 4 . . 4 . . 4 . . . .
               . . . . . . 4 4 4 4 4 . . . . .
               . . . . . . . 4 4 4 . . . . . .
               . . . . . . . 4 4 4 . . . . . .
               . . . . . . . 4 4 4 . . . . . .
               . . . . . . . f f f . . . . . .
               . . . . . . . 4 4 4 . . . . . .
               . . . . . . . 4 . 4 . . . . . .
               . . . . e 4 4 e 4 . . . . . . .
               . . . . e . . e . . . . . . . .
               . . . . . . . . . . . . . . . .
           """)
    

game.on_update(on_update)

game.on_update(on_update)

def on_push(sprite, otherSprite):
    scene.camera_shake(2)
    otherSprite.set_velocity(10, 0)
sprites.on_overlap(SpriteKind.player, SpriteKind.food, on_push)

def on_update2():
    if block.x == 608:
        scene.set_tile(5, img("""
    c c c c c c c c c c c c c c c c
    c b b b b b b b b b b b b b b b
    c b b b b b b b b b b b b b b b
    c b b b b b b b b b b b b b b b
    c b b b b b b b b b b b b b b b
    c b b b b b b b b b b b b b b b
    c b b b b b b b b b b b b b b b
    c b b b b b b b b b b b b b b b
    c c c c c c c c c c c c c c c c
    b b b b b b b b c b b b b b b b
    b b b b b b b b c b b b b b b b
    b b b b b b b b c b b b b b b b
    b b b b b b b b c b b b b b b b
    b b b b b b b b c b b b b b b b
    b b b b b b b b c b b b b b b b
    b b b b b b b b c b b b b b b b
"""),True)
game.on_update(on_update2)
vent = sprites.create(img("""
    c c c c c c c c c f f f f f f c
    c b b b b c c c f f f f f f b b
    c b f f f f f f f f f f f b b b
    c f f f f f f f f f f f c b b b
    c b b c f f f f f f f f c b b b
    c b b c f f f f f f f f f f f f
    c b c f f f f f f f f f f f f b
    c b c f f f f f f f f f f f c b
    c c c f f f f f f f f f f f c c
    b b c f f f f f f f f f f f c b
    b b c f f f f f f f f f f f c b
    b f f f f f f f f f f f f f c b
    b c b f f f f f f f f f f f b f
    f c b f f f f f f c f f c f f f
    b b b f b f f c c b b f f b b b
    b b b f f b b b c b b b f f b b
"""),SpriteKind.tunnel)
vent.set_position(615, 120)
ventout = sprites.create(img("""
    c c c c c c c c c f f f f f f c
    c b b b b c c c f f f f f f b b
    c b f f f f f f f f f f f b b b
    c f f f f f f f f f f f c b b b
    c b b c f f f f f f f f c b b b
    c b b c f f f f f f f f f f f f
    c b c f f f f f f f f f f f f b
    c b c f f f f f f f f f f f c b
    c c c f f f f f f f f f f f c c
    b b c f f f f f f f f f f f c b
    b b c f f f f f f f f f f f c b
    b f f f f f f f f f f f f f c b
    b c b f f f f f f f f f f f b f
    f c b f f f f f f c f f c f f f
    b b b f b f f c c b b f f b b b
    b b b f f b b b c b b b f f b b
"""))
ventout.set_position(1080, 328)

# Vent Mechanic
def on_overlap2(sprite, otherSprite):
    tiles.place_on_tile(Merek, tiles.get_tile_location(66, 20))
sprites.on_overlap(SpriteKind.player, SpriteKind.tunnel, on_overlap2)


flagpole = sprites.create(img("""
    . . . . . . . 2 2 2 . . . . . .
    . . . . . . . 2 2 2 2 2 . . . .
    . . . . . . . 2 2 2 2 2 2 2 . .
    . . . . . . . 2 2 2 2 2 2 2 . .
    . . . . . . . 2 2 2 2 2 . . . .
    . . . . . . . 2 2 2 . . . . . .
    . . . . . . . 2 b . . . . . . .
    . . . . . . . 1 b . . . . . . .
    . . . . . . . 1 b . . . . . . .
    . . . . . . . 1 b . . . . . . .
    . . . . . . . 1 b . . . . . . .
    . . . . . . . 1 b . . . . . . .
    . . . . . . . 1 b . . . . . . .
    . . . . . . . 1 b . . . . . . .
    . . . 5 5 5 5 5 4 4 4 4 4 . . .
    . . 5 5 5 5 5 5 5 5 5 5 4 4 . .
"""),SpriteKind.player)
flagpole.set_position(513, 536)
def on_flag_grab(sprite, otherSprite):
    game.over(True)
sprites.on_overlap(SpriteKind.player, SpriteKind.player, on_flag_grab)

# button = sprites.create(img("""
#     . . . . . . . . . . . . . . . .
#     . . . . . . . . . . . . . . . .
#     . . . . . . . . . . . . . . . .
#     . . . . . . . . . . . . . . . .
#     . . . . . . . . . . . . . . . .
#     . . . . . . . . . . . . . . . .
#     . . . . . . . . . . . . . . . .
#     . . . . . . . . . . . . . . . .
#     . . . . . . . . . . . . . . . .
#     . . . . . . . . . . . . . . . .
#     . . . . . . . . . . . . . . . .
#     . . . 1 1 1 1 1 1 1 1 1 1 . . .
#     . . 1 4 4 4 4 4 4 2 2 2 2 1 . .
#     . . 1 4 4 4 4 4 4 4 2 2 2 1 . .
#     . 1 d d d d d d d d d b b b 1 .
#     1 d d d d d d d d d d d b b b 1
# """))
# button_down = img("""
#     . . . . . . . . . . . . . . . .
#     . . . . . . . . . . . . . . . .
#     . . . . . . . . . . . . . . . .
#     . . . . . . . . . . . . . . . .
#     . . . . . . . . . . . . . . . .
#     . . . . . . . . . . . . . . . .
#     . . . . . . . . . . . . . . . .
#     . . . . . . . . . . . . . . . .
#     . . . . . . . . . . . . . . . .
#     . . . . . . . . . . . . . . . .
#     . . . . . . . . . . . . . . . .
#     . . . . . . . . . . . . . . . .
#     . . . 1 1 1 1 1 1 1 1 1 1 . . .
#     . . 1 4 4 4 4 4 4 4 2 2 2 1 . .
#     . 1 d d d d d d d d d b b b 1 .
#     1 d d d d d d d d d d d b b b 1
# """)
# tiles.place_on_tile(button, tiles.get_tile_location(108, 33))
