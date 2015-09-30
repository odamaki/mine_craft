from mcpi import minecraft
from time import sleep

mc=minecraft.Minecraft.create()
mc.postToChat("Hello Minecraft")

flower = 38
lava =10
gold =14
gold_block=41
diamond_block=57

while True:
    x, y, z = mc.player.getPos()
    for xx in range(-3,3):
        for zz in range(-3,3):
            if mc.getBlock(x+xx,y-1,z+zz)!=0:
                mc.setBlock(x+xx, y-1, z+zz, gold_block) 
    sleep(0.1)
