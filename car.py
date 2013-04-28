
import hw.car as c

class Car(object):
    moving = False
    @classmethod
    def right(self):
        self.moving = True
        c.left_forward()
        c.right_backward() 
        print 'right'
    @classmethod
    def left(self):
        self.moving = True
        c.left_backward()
        c.right_forward() 
        print 'left'
    @classmethod
    def up(self):
        self.moving = True
        c.left_forward()
        c.right_forward() 
        print 'up'
    @classmethod
    def down(self):
        self.moving = True
        c.left_backward()
        c.right_backward() 
        print 'down'
    @classmethod
    def stop(self):
        self.moving = False
        c.left_stop()
        c.right_stop() 
        print 'stop'
