from mcpi import minecraft
from time import sleep

mc=minecraft.Minecraft.create()
mc.postToChat("Hello Minecraft,Motoko")

flower = 38
lava =10
gold =14
gold_block=41
diamond_block=57

while True:
    x, y, z = mc.player.getPos()
    mc.setBlock(x, y, z, flower)
    sleep(0.1)
