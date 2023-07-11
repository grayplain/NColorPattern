from Color import Color
from Color import ColorType
from typing import List
import random

class Tile:
    color: Color = Color.NoColor
    tileNum = -1
    def __init__(self, tileNum):
        self.tileNum = tileNum


class AdjacentTile:
    mainTile = Tile(tileNum=0)
    # ToDO: otherTile の設定方法は要検討。
    # otherTile 自体はあってもOKだと思う。
    otherTiles = List[Tile]

    def __init__(self, mainTile: Tile, otherTiles: List[Tile]):
        self.mainTile = mainTile
        self.otherTiles = otherTiles

    def setMainColos(self):
        # TODO: mainTile の tileNum と otherTile の tileNum を比較する
        # もし otherTile に mainTile と tileNum が同じものがあれば、
        #  そのtile に設定されている色をmainTile に設定して処理を終了する。そのとき、otherTile の色はそのままにする。
        # 色が設定されていなかったり、otherTile に同じ tileNum がなければ、
        #  mainTile にランダムに色をつけるので、decideTileColor を実行する。
        # decideTileColor の引数に渡す Tile のリストは、mainTile と異なるotherTile のみ。

        filterOtherTiles:List[Tile] = []
        for tile in self.otherTiles:
            if self.mainTile.tileNum == tile.tileNum and tile.color != Color.NoColor:
                filterOtherTiles.append(tile)

        if len(filterOtherTiles) == 0:
            self.mainTile.color = TileModel().decideTileColor(self.otherTiles)
        else:
            self.mainTile.color = filterOtherTiles.pop().color

class TileModel:
    def decideTileColor(self, tiles: List[Tile]):
        allColor = ColorType().allColorPattern()
        colors = []
        for tile in tiles:
            colors.append(tile.color)

        colorsSet = set(colors)

        if len(colorsSet) == 1 and colorsSet.pop() == Color.NoColor:
            return random.choice(list(allColor))
        else:
            diff = allColor - colorsSet
            return random.choice(list(diff))

