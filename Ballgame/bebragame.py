import pygame
from pygame.draw import *
from random import randint

FPS = 30
Xbound = 800
Ybound = 800

transparent = (0, 0, 0, 0)
backg = (50, 50, 70)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]


def make_transp(scr):
    """делает surface прозрачным"""
    scr1 = scr.convert_alpha()
    scr1.fill(transparent)
    return scr1


class myobject():  
    """класс объекта, который имеет свой surface для отрисовки и может передвигаться по экране
    surface: принимает surface для использования в качестве текстурки
    x, y , vx, vy: положение объекта на экране и его скорость
    r: радиус коллизии
    type: значение типа, позволяет отличать объекты друг от друга
    """

    def __init__(self, surface, k, type): 
        """конструктор"""
        global Xbound, Ybound
        self.surface = surface
        self.x = randint(1, Xbound-35)
        self.y = randint(1, Ybound-35)
        self.vx = randint(1, 5)
        self.vy = randint(1,5)
        self.r = 35
        self.type = type
        self.k = k # vibrations
        
    def draw(self):
        """отображает себя на экране"""
        screen.blit(self.surface, (self.x-self.r, self.y-self.r))

    def move(self):
        """перемещает себя значение скорости"""
        self.x += self.vx
        self.y += self.vy



class table():
    """класс таблицы, хранит количество очков и координаты отрисовки, позволяет отобразить кол-во очков на экране
    points: число для вывода на экран
    x,y - координаты надписи на экране
    """

    def __init__(self, color, points, x, y):
        """конструктор"""
        self.points = points
        self.color = color
        self.x = x
        self.y = y

    def draw(self):
        """вывод очков на экран"""
        f1 = pygame.font.Font(None, 36)
        tbl = 'points: '
        tbl += str(self.points)
        text1 = f1.render(tbl, True, self.color)
        screen.blit(text1, (self.x, self.y))


def click_object(event, obj):
    """получает объект класса myobject и событие event, при нажатии на объект определенного типа делает действие"""
    if((obj.x-event.pos[0])**2 + (obj.y-event.pos[1])**2 <= obj.r**2):
        if obj.type == 2:
            finished = True
        elif obj.type == 0:
            table1.points += 1
        elif obj.type == 1:
            table1.points += 10
        return(True)
    else:
        return(False)


def collision(obj):
    """функция коллизии, получает объект класса myobject и при столкновении отражает его от стен
    Xbound, Ybound - границы экрана, заданы вне функции
    при типе объекта:
    0 - дает +1 очко
    1 - дает +10 очков
    2 - проиграл
    """
    global Xbound, Ybound
    if(obj.x + obj.r > Xbound):
        obj.vx *= -1
        obj.x = Xbound-obj.r
    elif(obj.x - obj.r < 0):
        obj.vx *= -1
        obj.x = obj.r
    elif(obj.y - obj.r < 0):
        obj.vy *= -1
        obj.y = obj.r
    elif(obj.y + obj.r > Ybound):
        obj.vy *= -1
        obj.y = Ybound-obj.r

def make_transp(scr):
    """делает surface прозрачным"""
    scr1 = scr.convert_alpha()
    scr1.fill(transparent)
    return scr1


class Ball():  
    """класс объекта, который имеет свой surface для отрисовки и может передвигаться по экране
    surface: принимает surface для использования в качестве текстурки
    x, y , vx, vy: положение объекта на экране и его скорость
    r: радиус коллизии
    type: значение типа, позволяет отличать объекты друг от друга
    """

    def __init__(self): 
        """конструктор"""
        global Xbound, Ybound
        self.surface = make_transp(pygame.Surface((70, 70)))
        self.x = randint(1, Xbound-35)
        self.y = randint(1, Ybound-35)
        self.vx = randint(1, 5)
        self.vy = randint(1,5)
        self.r = 35
        self.type = 0
        self.has_collided = False
     
    def draw(self):
        """рисует себя на собственном экране"""
        circle(self.surface, BLUE, (35, 35), 35)
        
    def blit(self):
        """ свою поверхность на экран"""
        
        screen.blit(self.surface, (self.x -self.r, self.y-self.r))

    def move(self):
        """перемещает себя значение скорости"""
        self.x += self.vx
        self.y += self.vy


class Square1(Ball):
    def __init(self):
        super().init(self)
        self.type = 1
        self.vibration = 1

    def draw(self):
        rect(self.surface, GREEN, (0, 0, 70, 70))
        circle(self.surface, BLACK, (20, 25), 5)
        circle(self.surface, BLACK, (50, 25), 5)
        rect(self.surface, BLACK, (15, 50, 40, 7))

    def bebration(self):
        self.x += randint(-10, 10)
        self.y += randint(-10, 10)

    def move(self):
        Square1.bebration(self)
        super().move()
        



class table():
    """класс таблицы, хранит количество очков и координаты отрисовки, позволяет отобразить кол-во очков на экране
    points: число для вывода на экран
    x,y - координаты надписи на экране
    """

    def __init__(self, color, points, x, y):
        """конструктор"""
        self.points = points
        self.color = color
        self.x = x
        self.y = y

    def draw(self):
        """вывод очков на экран"""
        f1 = pygame.font.Font(None, 36)
        tbl = 'points: '
        tbl += str(self.points)
        text1 = f1.render(tbl, True, self.color)
        screen.blit(text1, (self.x, self.y))


def click_object(event, obj):
    """получает объект класса myobject и событие event, при нажатии на объект определенного типа делает действие"""
    if((obj.x-event.pos[0])**2 + (obj.y-event.pos[1])**2 <= obj.r**2):
        if obj.type == 2:
            finished = True
        elif obj.type == 0:
            table1.points += 1
        elif obj.type == 1:
            table1.points += 10
        return(True)
    else:
        return(False)


def collision(obj):
    """функция коллизии, получает объект класса myobject и при столкновении отражает его от стен
    Xbound, Ybound - границы экрана, заданы вне функции
    при типе объекта:
    0 - дает +1 очко
    1 - дает +10 очков
    2 - проиграл
    """
    global Xbound, Ybound
    if(obj.x + obj.r > Xbound):
        obj.vx *= -1
        obj.x = Xbound-obj.r
    elif(obj.x - obj.r < 0):
        obj.vx *= -1
        obj.x = obj.r
    elif(obj.y - obj.r < 0):
        obj.vy *= -1
        obj.y = obj.r
    elif(obj.y + obj.r > Ybound):
        obj.vy *= -1
        obj.y = Ybound-obj.r

pygame.init()
screen = pygame.display.set_mode((Xbound, Ybound))


# создаем таблицу учета очков
table1 = table(YELLOW, 0, 10, 10)

# создаем surface шара и surface квадратикa


square1 = make_transp(pygame.Surface((70, 70)))




# и наконец массив объектов трех типов: шариков и квадратиков
all_objects =[]
for i in range(1, 5):
    ball = Ball()
    square1 = Square1()
    square1.type = 1
    
    all_objects.extend([ball, square1])

pygame.display.update()
clock = pygame.time.Clock()
finished = False


def smashballs():
    global all_objects
    for object1 in all_objects:
        if object1.type == 0:
            for object2 in all_objects:
                if ((object2.type == 0) and (object1 != object2)):
                    distance = (object1.x - object2.x) ** 2 + (object1.y - object2.y) ** 2
                    if distance <= 4900:
                        object1.vx = randint(1, 5)
                        object2.vx = -  randint(1,  5)
                        object1.vy = - randint(1,5)
                        object2.vy = randint(1,5 )
                   
                    
                  
                
                    
while not finished:
    clock.tick(FPS)
    for obj in all_objects:
            obj.draw()
            obj.blit()
            obj.move()
            collision(obj)
    if len(all_objects) == 0:
        finished = True
    

    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            X_m, Y_m = event.pos
            for objects in all_objects:
                for obj in all_objects:
                    click_object(event, obj)
                    if click_object(event, obj):
                        all_objects.remove(obj)

        
    table1.draw()
    smashballs()
    pygame.display.update()
    
    
    
    screen.fill(backg)

pygame.quit()
