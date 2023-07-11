from typing import List

import Tile

# TODO: Pattern クラスに縦＊横の大きさを定義すれば、otherTile を計算で定義可能。
class Pattern:
    tiles: List[Tile.Tile] = []
    adjacentTile: List[Tile.AdjacentTile] = []

    def emptyTiles(self, tileNum):
        for i in range(0, tileNum):
            hoge = Tile.Tile(tileNum=i)
            self.tiles.append(hoge)

    def sampleTiles(self):
        huga = Tile.Tile(tileNum=1)
        self.tiles.append(huga)
        huga = Tile.Tile(tileNum=1)
        self.tiles.append(huga)
        huga = Tile.Tile(tileNum=2)
        self.tiles.append(huga)
        huga = Tile.Tile(tileNum=1)
        self.tiles.append(huga)
        huga = Tile.Tile(tileNum=3)
        self.tiles.append(huga)
        huga = Tile.Tile(tileNum=4)
        self.tiles.append(huga)
        huga = Tile.Tile(tileNum=5)
        self.tiles.append(huga)
        huga = Tile.Tile(tileNum=6)
        self.tiles.append(huga)
        huga = Tile.Tile(tileNum=7)
        self.tiles.append(huga)

    def sampleAdjacentTile(self):
        adjacentTile = Tile.AdjacentTile(self.tiles[0],
                                         [self.tiles[1],
                                          self.tiles[3]])
        self.adjacentTile.append(adjacentTile)

        adjacentTile = Tile.AdjacentTile(self.tiles[1],
                                         [self.tiles[0],
                                          self.tiles[2],
                                          self.tiles[4]])
        self.adjacentTile.append(adjacentTile)

        adjacentTile = Tile.AdjacentTile(self.tiles[2],
                                         [self.tiles[1],
                                          self.tiles[5]])
        self.adjacentTile.append(adjacentTile)

        adjacentTile = Tile.AdjacentTile(self.tiles[3],
                                         [self.tiles[0],
                                          self.tiles[4]])
        self.adjacentTile.append(adjacentTile)

        adjacentTile = Tile.AdjacentTile(self.tiles[4],
                                         [self.tiles[1],
                                          self.tiles[3],
                                          self.tiles[5],
                                          self.tiles[7]])
        self.adjacentTile.append(adjacentTile)

        adjacentTile = Tile.AdjacentTile(self.tiles[5],
                                         [self.tiles[2],
                                          self.tiles[4],
                                          self.tiles[8]])
        self.adjacentTile.append(adjacentTile)

        adjacentTile = Tile.AdjacentTile(self.tiles[6],
                                         [self.tiles[3],
                                          self.tiles[7]])
        self.adjacentTile.append(adjacentTile)

        adjacentTile = Tile.AdjacentTile(self.tiles[7],
                                         [self.tiles[4],
                                          self.tiles[6],
                                          self.tiles[8]])
        self.adjacentTile.append(adjacentTile)

        adjacentTile = Tile.AdjacentTile(self.tiles[8],
                                         [self.tiles[5],
                                          self.tiles[7]])
        self.adjacentTile.append(adjacentTile)


    def sampleAdjacentTile2(self):
        adjacentTile = Tile.AdjacentTile(self.tiles[0],
                                         [self.tiles[1],
                                          self.tiles[3]])
        self.adjacentTile.append(adjacentTile)

        adjacentTile = Tile.AdjacentTile(self.tiles[1],
                                         [self.tiles[0],
                                          self.tiles[2],
                                          self.tiles[4]])
        self.adjacentTile.append(adjacentTile)

        adjacentTile = Tile.AdjacentTile(self.tiles[2],
                                         [self.tiles[1],
                                          self.tiles[5]])
        self.adjacentTile.append(adjacentTile)

        adjacentTile = Tile.AdjacentTile(self.tiles[3],
                                         [self.tiles[0],
                                          self.tiles[4]])
        self.adjacentTile.append(adjacentTile)

        adjacentTile = Tile.AdjacentTile(self.tiles[4],
                                         [self.tiles[1],
                                          self.tiles[3],
                                          self.tiles[5],
                                          self.tiles[7]])
        self.adjacentTile.append(adjacentTile)

        adjacentTile = Tile.AdjacentTile(self.tiles[5],
                                         [self.tiles[2],
                                          self.tiles[4],
                                          self.tiles[8]])
        self.adjacentTile.append(adjacentTile)

        adjacentTile = Tile.AdjacentTile(self.tiles[6],
                                         [self.tiles[3],
                                          self.tiles[7]])
        self.adjacentTile.append(adjacentTile)

        adjacentTile = Tile.AdjacentTile(self.tiles[7],
                                         [self.tiles[4],
                                          self.tiles[6],
                                          self.tiles[8]])
        self.adjacentTile.append(adjacentTile)

        adjacentTile = Tile.AdjacentTile(self.tiles[8],
                                         [self.tiles[5],
                                          self.tiles[7]])
        self.adjacentTile.append(adjacentTile)