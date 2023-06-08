from direct.showbase.ShowBase import ShowBase
from panda3d.core import PointLight, Point3
from panda3d.core import GeomVertexFormat, GeomVertexData
from panda3d.core import Geom, GeomTriangles, GeomNode
from panda3d.core import LVector3

class Visualiser(ShowBase):
    def __init__(self, rows, cols, stack):
        ShowBase.__init__(self)

        self.rows = rows
        self.cols = cols
        self.stack = stack



        z = -10
        x = -8
        y = 42
        for _ in range(self.stack):
            for _ in range(self.cols):
                for _ in range(int(self.rows)):
                    self.cube(x,y,z)
                    z += 5
                z = -10
                x += 5
            x = -8
            y -= 5
        self.camera.setPos(0, -100, 0)
    def cube(self, x, y, z):
        self.sphere = self.loader.loadModel("cube")
        self.sphere.reparentTo(self.render)
        self.sphere.setPos(x, y, z)
        self.sphere.setScale(1, 1, 1)

    def lines(self):
        pass


run = Visualiser(3, 5, 4)
run.run()