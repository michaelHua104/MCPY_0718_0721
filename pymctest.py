from mcpi.minecraft import Minecraft
mc = Minecraft.create()
while True:
    pos = mc.player.getTilePos()
    mc.player.setTilePos(pos.x, pos.y-1, pos.z, random.randint(1, 252))
    time.sleep(0.1)