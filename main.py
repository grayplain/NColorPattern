import Pattern

pattern = Pattern.Pattern()

pattern.sampleTiles()
pattern.sampleAdjacentTile2()

# for tile in tiles.tiles:
#     print(str(tile.tileNum) + "," + Color().colorValue(tile.color))

print("before colors")
for tiles in pattern.adjacentTile:
    tiles.setMainColos()

    print(tiles.mainTile.color, end="/")

    for tile in tiles.otherTiles:
        # print(tile.tileNum, end=',')
        print(tile.color, end=',')
    print("")


index = 0
for tiles in pattern.adjacentTile:
    print(tiles.mainTile.color, end=" ")
    index +=1
    if index >= 3:
        print("")
        index = 0
