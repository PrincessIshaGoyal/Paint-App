from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scatter import Scatter
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.slider import Slider
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.textinput import TextInput
from kivy.graphics import Rectangle, Color, Line, Ellipse
from kivy.core.window import Window
Window.show_cursor = False
from datetime import datetime

class DrawingWidget(Widget):
    def __init__(self):
        Window.bind(mouse_pos=self.on_mouse_pos)
        super(DrawingWidget, self).__init__()

        with self.canvas:
            Color(1, 1, 1, 1)
            self.rect = Rectangle(size=self.size, pos=self.pos)
            Color(0,0,0)
            Rectangle(size=(800,200), pos=(0,0))
        self.bind(pos=self.update_rectangle, size=self.update_rectangle)
        
        self.color = [0,0,0]
        self.color_2 = [0,0,0]
        self.color_grid = GridLayout(cols=2, size=(400,200), pos=(0,0))
        self.label = Label(text='CC')
        self.color_grid.add_widget(self.label)
        self.label = Label(text='  ')
        self.color_grid.add_widget(self.label)
        self.label = Label(text='Red')
        self.color_grid.add_widget(self.label)
        self.red = Slider(min=0, max=100)
        self.red.bind(value = self.change_red)
        self.color_grid.add_widget(self.red)
        self.label = Label(text='Green')
        self.color_grid.add_widget(self.label)
        self.green = Slider(min=0, max=100)
        self.green.bind(value = self.change_green)
        self.color_grid.add_widget(self.green)
        self.label = Label(text='Blue')
        self.color_grid.add_widget(self.label)
        self.blue = Slider(min=0, max=100)
        self.blue.bind(value = self.change_blue)
        self.color_grid.add_widget(self.blue)
        self.add_widget(self.color_grid)

        self.shape_details = {'pos_x':400, 'pos_y':205, 'size_x':100, 'size_y':100, 'text':'Text'}
        self.shape = Ellipse(size=(1,1), pos=(400,205))
        self.shape_state = ''
        self.shape_grid = GridLayout(cols=2, size=(400,200), pos=(400,0))
        self.b_rect = Button(text='Rectangle')
        self.b_rect.bind(on_release = self.shape_rect)
        self.shape_grid.add_widget(self.b_rect)
        self.b_circle = Button(text='Circle')
        self.b_circle.bind(on_release = self.shape_circle)
        self.shape_grid.add_widget(self.b_circle)
        self.b_star = Button(text='Star')
        self.b_star.bind(on_release = self.shape_star)
        self.shape_grid.add_widget(self.b_star)
        self.b_bez = Button(text='Image')
        self.b_bez.bind(on_release = self.shape_bez)
        self.shape_grid.add_widget(self.b_bez)
        self.b_line = Button(text='Straight Line')
        self.b_line.bind(on_release = self.shape_line)
        self.shape_grid.add_widget(self.b_line)
        self.b_text = Button(text='Text Box')
        self.b_text.bind(on_release = self.shape_text)
        self.shape_grid.add_widget(self.b_text)
        self.b_erase = Button(text='Eraser')
        self.b_erase.bind(on_release = self.shape_erase)
        self.shape_grid.add_widget(self.b_erase)
        self.b_pen = Button(text='Pencil')
        self.b_pen.bind(on_release = self.shape_pen)
        self.shape_grid.add_widget(self.b_pen)
        self.add_widget(self.shape_grid)

        self.pen_size = 10
        with self.canvas:
            Color(0,0,0)
            self.mouse = Ellipse(pos=(400, 210), size=(10,10))

    def change_red(self, instance, value):
        self.color[0] = int(value)/100
        self.remove_widget(self.color_grid)
        with self.canvas:
            Color(0,0,0)
            Rectangle(size=(400,200), pos=(0,0))
            Color(*self.color)
            Rectangle(size=(200,40), pos=(200,150))
        self.add_widget(self.color_grid)
        with self.canvas:
            Color(*self.color)
            self.mouse = Ellipse(size=(self.pen_size, self.pen_size), pos=Window.mouse_pos)

    def change_green(self, instance, value):
        self.color[1] = int(value)/100
        self.remove_widget(self.color_grid)
        with self.canvas:
            Color(0,0,0)
            Rectangle(size=(400,200), pos=(0,0))
            Color(*self.color)
            Rectangle(size=(200,40), pos=(200,150))
        self.add_widget(self.color_grid)
        with self.canvas:
            Color(*self.color)
            self.mouse = Ellipse(size=(self.pen_size, self.pen_size), pos=Window.mouse_pos)

    def change_blue(self, instance, value):
        self.color[2] = int(value)/100
        self.remove_widget(self.color_grid)
        with self.canvas:
            Color(0,0,0)
            Rectangle(size=(400,200), pos=(0,0))
            Color(*self.color)
            Rectangle(size=(200,40), pos=(200,150))
        self.add_widget(self.color_grid)
        with self.canvas:
            Color(*self.color)
            self.mouse = Ellipse(size=(self.pen_size, self.pen_size), pos=Window.mouse_pos)

    def shape_rect(self, event):
        self.shape_state = 'rect'
        self.remove_widget(self.shape_grid)
        self.shape.pos = (2000,2000)
        with self.canvas:
            Color(0,0,0)
            Rectangle(size=(1000,200), pos=(400,0))
            Color(*self.color)
            self.shape = Rectangle(size=(self.shape_details['size_x'], self.shape_details['size_y']),
                                   pos=(self.shape_details['pos_x'], self.shape_details['pos_y']))
        self.add_widget(self.shape_grid)

        self.detail_grid = GridLayout(cols = 2, size=(600,200), pos=(800,0))
        self.label = Label(text='Position')
        self.detail_grid.add_widget(self.label)
        self.label = Label(text='Size')
        self.detail_grid.add_widget(self.label)
        self.pos_x = Slider(min=0, max=1000, value=self.shape_details['pos_x'])
        self.pos_x.bind(value = self.update_pos_x)
        self.detail_grid.add_widget(self.pos_x)
        self.size_x = Slider(min=0, max=1000, value=self.shape_details['size_x'])
        self.size_x.bind(value = self.update_size_x)
        self.detail_grid.add_widget(self.size_x)
        self.pos_y = Slider(min=205, max=700, value=self.shape_details['pos_y'])
        self.pos_y.bind(value = self.update_pos_y)
        self.detail_grid.add_widget(self.pos_y)
        self.size_y = Slider(min=0, max=1000, value=self.shape_details['size_y'])
        self.size_y.bind(value = self.update_size_y)
        self.detail_grid.add_widget(self.size_y)
        self.b1 = Button(text = "Change Color")
        self.b1.bind(on_press = self.update_color)
        self.detail_grid.add_widget(self.b1)
        self.b2 = Button(text = "Done")
        self.b2.bind(on_press = self.done_shape)
        self.detail_grid.add_widget(self.b2)
        self.add_widget(self.detail_grid)

        with self.canvas:
            Color(*self.color)
            self.mouse = Ellipse(size=(self.pen_size, self.pen_size), pos=Window.mouse_pos)

    def shape_circle(self, event):
        self.shape_state = 'circle'
        self.remove_widget(self.shape_grid)
        self.shape.pos = (2000,2000)
        with self.canvas:
            Color(0,0,0)
            Rectangle(size=(1000,200), pos=(400,0))
            Color(*self.color)
            self.shape = Ellipse(size=(self.shape_details['size_x'], self.shape_details['size_y']),
                                   pos=(self.shape_details['pos_x'], self.shape_details['pos_y']))
        self.add_widget(self.shape_grid)

        self.detail_grid = GridLayout(cols = 2, size=(600,200), pos=(800,0))
        self.label = Label(text='Position')
        self.detail_grid.add_widget(self.label)
        self.label = Label(text='Size')
        self.detail_grid.add_widget(self.label)
        self.pos_x = Slider(min=0, max=1000, value=self.shape_details['pos_x'])
        self.pos_x.bind(value = self.update_pos_x)
        self.detail_grid.add_widget(self.pos_x)
        self.size_x = Slider(min=0, max=1000, value=self.shape_details['size_x'])
        self.size_x.bind(value = self.update_size_x)
        self.detail_grid.add_widget(self.size_x)
        self.pos_y = Slider(min=205, max=700, value=self.shape_details['pos_y'])
        self.pos_y.bind(value = self.update_pos_y)
        self.detail_grid.add_widget(self.pos_y)
        self.size_y = Slider(min=0, max=1000, value=self.shape_details['size_y'])
        self.size_y.bind(value = self.update_size_y)
        self.detail_grid.add_widget(self.size_y)
        self.b1 = Button(text = "Change Color")
        self.b1.bind(on_press = self.update_color)
        self.detail_grid.add_widget(self.b1)
        self.b2 = Button(text = "Done")
        self.b2.bind(on_press = self.done_shape)
        self.detail_grid.add_widget(self.b2)
        self.add_widget(self.detail_grid)

        with self.canvas:
            Color(*self.color)
            self.mouse = Ellipse(size=(self.pen_size, self.pen_size), pos=Window.mouse_pos)

    def shape_star(self, event):
        self.shape_state = 'star'
        self.remove_widget(self.shape_grid)
        self.shape.pos = (2000,2000)
        with self.canvas:
            Color(0,0,0)
            Rectangle(size=(1000,200), pos=(400,0))
            Color(*self.color)
            self.shape = Line(points = [self.shape_details['pos_x'], self.shape_details['pos_y'],
                                        self.shape_details['pos_x'] + self.shape_details['size_x']//2, self.shape_details['pos_y'] + self.shape_details['size_y'],
                                        self.shape_details['pos_x'] + self.shape_details['size_x'], self.shape_details['pos_y'],
                                        self.shape_details['pos_x'] -20, self.shape_details['pos_y'] + self.shape_details['size_y']/1.5,
                                        self.shape_details['pos_x'] + self.shape_details['size_x'] +20, self.shape_details['pos_y'] + self.shape_details['size_y']/1.5,
                                        self.shape_details['pos_x'], self.shape_details['pos_y']], width=self.pen_size//2)
        self.add_widget(self.shape_grid)

        self.detail_grid = GridLayout(cols = 2, size=(600,200), pos=(800,0))
        self.label = Label(text='Position')
        self.detail_grid.add_widget(self.label)
        self.label = Label(text='Size')
        self.detail_grid.add_widget(self.label)
        self.pos_x = Slider(min=0, max=1000, value=self.shape_details['pos_x'])
        self.pos_x.bind(value = self.update_pos_x)
        self.detail_grid.add_widget(self.pos_x)
        self.size_x = Slider(min=0, max=1000, value=self.shape_details['size_x'])
        self.size_x.bind(value = self.update_size_x)
        self.detail_grid.add_widget(self.size_x)
        self.pos_y = Slider(min=205, max=700, value=self.shape_details['pos_y'])
        self.pos_y.bind(value = self.update_pos_y)
        self.detail_grid.add_widget(self.pos_y)
        self.size_y = Slider(min=0, max=1000, value=self.shape_details['size_y'])
        self.size_y.bind(value = self.update_size_y)
        self.detail_grid.add_widget(self.size_y)
        self.b1 = Button(text = "Change Color")
        self.b1.bind(on_press = self.update_color)
        self.detail_grid.add_widget(self.b1)
        self.b2 = Button(text = "Done")
        self.b2.bind(on_press = self.done_shape)
        self.detail_grid.add_widget(self.b2)
        self.add_widget(self.detail_grid)

        with self.canvas:
            Color(*self.color)
            self.mouse = Ellipse(size=(self.pen_size, self.pen_size), pos=Window.mouse_pos)

    def shape_bez(self, event):
        self.shape_state = 'img'
        self.remove_widget(self.shape_grid)
        self.shape.pos = (2000,2000)
        with self.canvas:
            Color(0,0,0)
            Rectangle(size=(1000,200), pos=(400,0))
        self.add_widget(self.shape_grid)

        self.detail_grid = GridLayout(cols=1, size=(600,200), pos=(800,0))
        self.label = Label(text='Enter image path with name and ".png"')
        self.detail_grid.add_widget(self.label)
        self.img_path = TextInput(text = 'Image')
        self.detail_grid.add_widget(self.img_path)
        self.b1 = Button(text='Load Image')
        self.b1.bind(on_press = self.shape_img)
        self.detail_grid.add_widget(self.b1)
        self.add_widget(self.detail_grid)

        with self.canvas:
            Color(*self.color)
            self.mouse = Ellipse(size=(self.pen_size, self.pen_size), pos=Window.mouse_pos)

    def shape_img(self, event):
        self.remove_widget(self.detail_grid)
        with self.canvas:
            Color(0,0,0)
            Rectangle(size=(600,200), pos=(800,0))
        self.shape = Image(source = self.img_path.text, allow_stretch=True, keep_ratio=False,
                           size=(self.shape_details['size_x'], self.shape_details['size_y']),
                           pos=(self.shape_details['pos_x'], self.shape_details['pos_y']))
        self.add_widget(self.shape)

        self.detail_grid = GridLayout(cols = 2, size=(600,200), pos=(800,0))
        self.label = Label(text='Position')
        self.detail_grid.add_widget(self.label)
        self.label = Label(text='Size')
        self.detail_grid.add_widget(self.label)
        self.pos_x = Slider(min=0, max=1000, value=self.shape_details['pos_x'])
        self.pos_x.bind(value = self.update_pos_x)
        self.detail_grid.add_widget(self.pos_x)
        self.size_x = Slider(min=0, max=1000, value=self.shape_details['size_x'])
        self.size_x.bind(value = self.update_size_x)
        self.detail_grid.add_widget(self.size_x)
        self.pos_y = Slider(min=205, max=700, value=self.shape_details['pos_y'])
        self.pos_y.bind(value = self.update_pos_y)
        self.detail_grid.add_widget(self.pos_y)
        self.size_y = Slider(min=0, max=1000, value=self.shape_details['size_y'])
        self.size_y.bind(value = self.update_size_y)
        self.detail_grid.add_widget(self.size_y)
        self.b1 = Button(text = "Change Image")
        self.b1.bind(on_press = self.update_color)
        self.detail_grid.add_widget(self.b1)
        self.b2 = Button(text = "Done")
        self.b2.bind(on_press = self.done_shape)
        self.detail_grid.add_widget(self.b2)
        self.add_widget(self.detail_grid)

        with self.canvas:
            Color(*self.color)
            self.mouse = Ellipse(size=(self.pen_size, self.pen_size), pos=Window.mouse_pos)

    def shape_line(self, event):
        self.shape_state = 'line'
        self.remove_widget(self.shape_grid)
        self.shape.pos = (2000,2000)
        with self.canvas:
            Color(0,0,0)
            Rectangle(size=(1000,200), pos=(400,0))
            Color(*self.color)
        self.add_widget(self.shape_grid)

        self.detail_grid = GridLayout(cols = 2, size=(600,200), pos=(800,0))
        self.label = Label(text='Draw!!')
        self.detail_grid.add_widget(self.label)
        self.b2 = Button(text = "Done")
        self.b2.bind(on_press = self.done_shape)
        self.detail_grid.add_widget(self.b2)
        self.add_widget(self.detail_grid)

        with self.canvas:
            Color(*self.color)
            self.mouse = Ellipse(size=(self.pen_size, self.pen_size), pos=Window.mouse_pos)

    def shape_text(self, event):
        self.shape_state = 'text'
        self.remove_widget(self.shape_grid)
        self.shape.pos = (2000,2000)
        with self.canvas:
            Color(0,0,0)
            Rectangle(size=(1000,200), pos=(400,0))
            Color(*self.color)
            self.shape = Label(text = self.shape_details['text'], font_size = self.shape_details['size_x'], color = self.color,
                               pos=(self.shape_details['pos_x'], self.shape_details['pos_y']))
        self.add_widget(self.shape_grid)

        self.detail_grid = GridLayout(cols = 2, size=(600,200), pos=(800,0))
        self.label = Label(text='Position')
        self.detail_grid.add_widget(self.label)
        self.label = Label(text='Size')
        self.detail_grid.add_widget(self.label)
        self.pos_x = Slider(min=0, max=1000, value=self.shape_details['pos_x'])
        self.pos_x.bind(value = self.update_pos_x)
        self.detail_grid.add_widget(self.pos_x)
        self.size_x = Slider(min=1, max=120, value=self.shape_details['size_x'])
        self.size_x.bind(value = lambda instance, x: setattr(self.shape, 'font_size', x))
        self.detail_grid.add_widget(self.size_x)
        self.pos_y = Slider(min=205, max=700, value=self.shape_details['pos_y'])
        self.pos_y.bind(value = self.update_pos_y)
        self.detail_grid.add_widget(self.pos_y)
        self.text_of_shape = TextInput(text = self.shape_details['text'])
        self.detail_grid.add_widget(self.text_of_shape)
        self.b1 = Button(text = "Change Text")
        self.b1.bind(on_press = self.update_text)
        self.detail_grid.add_widget(self.b1)
        self.b2 = Button(text = "Done")
        self.b2.bind(on_press = self.done_shape)
        self.detail_grid.add_widget(self.b2)
        self.add_widget(self.detail_grid)

        with self.canvas:
            Color(*self.color)
            self.mouse = Ellipse(size=(self.pen_size, self.pen_size), pos=Window.mouse_pos)

    def update_pos_x(self, instance, value):
        self.shape_details['pos_x'] = value
        if(self.shape_state == 'star'):
            self.shape.points = [self.shape_details['pos_x'], self.shape_details['pos_y'],
                                 self.shape_details['pos_x'] + self.shape_details['size_x']//2, self.shape_details['pos_y'] + self.shape_details['size_y'],
                                 self.shape_details['pos_x'] + self.shape_details['size_x'], self.shape_details['pos_y'],
                                 self.shape_details['pos_x'] -20, self.shape_details['pos_y'] + self.shape_details['size_y']/1.5,
                                 self.shape_details['pos_x'] + self.shape_details['size_x'] +20, self.shape_details['pos_y'] + self.shape_details['size_y']/1.5,
                                 self.shape_details['pos_x'], self.shape_details['pos_y']]
        else:
            self.shape.pos = (value, self.shape.pos[1])

    def update_size_x(self, instance, value):
        self.shape_details['size_x'] = value
        if(self.shape_state == 'star'):
            self.shape.points = [self.shape_details['pos_x'], self.shape_details['pos_y'],
                                 self.shape_details['pos_x'] + self.shape_details['size_x']//2, self.shape_details['pos_y'] + self.shape_details['size_y'],
                                 self.shape_details['pos_x'] + self.shape_details['size_x'], self.shape_details['pos_y'],
                                 self.shape_details['pos_x'] -20, self.shape_details['pos_y'] + self.shape_details['size_y']/1.5,
                                 self.shape_details['pos_x'] + self.shape_details['size_x'] +20, self.shape_details['pos_y'] + self.shape_details['size_y']/1.5,
                                 self.shape_details['pos_x'], self.shape_details['pos_y']]
        else:
            self.shape.size = (value, self.shape.size[1])

    def update_pos_y(self, instance, value):
        self.shape_details['pos_y'] = value
        if(self.shape_state == 'star'):
            self.shape.points = [self.shape_details['pos_x'], self.shape_details['pos_y'],
                                 self.shape_details['pos_x'] + self.shape_details['size_x']//2, self.shape_details['pos_y'] + self.shape_details['size_y'],
                                 self.shape_details['pos_x'] + self.shape_details['size_x'], self.shape_details['pos_y'],
                                 self.shape_details['pos_x'] -20, self.shape_details['pos_y'] + self.shape_details['size_y']/1.5,
                                 self.shape_details['pos_x'] + self.shape_details['size_x'] +20, self.shape_details['pos_y'] + self.shape_details['size_y']/1.5,
                                 self.shape_details['pos_x'], self.shape_details['pos_y']]
        else:
            self.shape.pos = (self.shape.pos[0], value)

    def update_size_y(self, instance, value):
        self.shape_details['size_y'] = value
        if(self.shape_state == 'star'):
            self.shape.points = [self.shape_details['pos_x'], self.shape_details['pos_y'],
                                 self.shape_details['pos_x'] + self.shape_details['size_x']//2, self.shape_details['pos_y'] + self.shape_details['size_y'],
                                 self.shape_details['pos_x'] + self.shape_details['size_x'], self.shape_details['pos_y'],
                                 self.shape_details['pos_x'] -20, self.shape_details['pos_y'] + self.shape_details['size_y']/1.5,
                                 self.shape_details['pos_x'] + self.shape_details['size_x'] +20, self.shape_details['pos_y'] + self.shape_details['size_y']/1.5,
                                 self.shape_details['pos_x'], self.shape_details['pos_y']]
        else:
            self.shape.size = (self.shape.size[0], value)

    def update_text(self, event):
        self.shape_details['text'] = self.text_of_shape.text
        self.shape.text = self.text_of_shape.text

    def update_color(self, event):
        if(self.shape_state == 'star'):
            self.shape.points = [0,0]
        else:
            self.shape.pos = (2000, 2000)
        with self.canvas:
            Color(*self.color)
            if(self.shape_state=='rect'):
                self.shape = Rectangle(size=(self.shape_details['size_x'], self.shape_details['size_y']),
                                   pos=(self.shape_details['pos_x'], self.shape_details['pos_y']))
            elif(self.shape_state=='circle'):
                self.shape = Ellipse(size=(self.shape_details['size_x'], self.shape_details['size_y']),
                                   pos=(self.shape_details['pos_x'], self.shape_details['pos_y']))
            elif(self.shape_state=='star'):
                self.shape = Line(points =[self.shape_details['pos_x'], self.shape_details['pos_y'],
                                           self.shape_details['pos_x'] + self.shape_details['size_x']//2, self.shape_details['pos_y'] + self.shape_details['size_y'],
                                           self.shape_details['pos_x'] + self.shape_details['size_x'], self.shape_details['pos_y'],
                                           self.shape_details['pos_x'] -20, self.shape_details['pos_y'] + self.shape_details['size_y']/1.5,
                                           self.shape_details['pos_x'] + self.shape_details['size_x'] +20, self.shape_details['pos_y'] + self.shape_details['size_y']/1.5,
                                           self.shape_details['pos_x'], self.shape_details['pos_y']], width=self.pen_size//2)
            elif(self.shape_state=='img'):
                self.done_shape('ok')
                self.shape_bez('ok')

    def done_shape(self, event):
        self.shape_details = {'pos_x':400, 'pos_y':205, 'size_x':100, 'size_y':100, 'text':'Text'}
        self.shape = Ellipse(size=(1,1), pos=(400,205))
        self.shape_state = ''
        self.remove_widget(self.detail_grid)
        del self.detail_grid
        with self.canvas:
            Color(1,1,1)
            Rectangle(size=(600,200), pos=(800,0))
            Color(*self.color)
            self.mouse = Ellipse(size=(self.pen_size, self.pen_size), pos=Window.mouse_pos)

    def shape_erase(self, event):
        self.color_2 = self.color
        self.color = [1,1,1]
        self.shape.pos = (2000, 2000)
        self.remove_widget(self.shape_grid)
        with self.canvas:
            Color(0,0,0)
            Rectangle(size=(1000,200), pos=(400,0))
        self.add_widget(self.shape_grid)

        self.detail_grid = GridLayout(cols = 2, size=(600,200), pos=(800,0))
        self.label = Label(text='Size : '+str(self.pen_size))
        self.detail_grid.add_widget(self.label)
        self.s = Slider(min=1, max=100, value=self.pen_size)
        self.s.bind(value = self.update_pen_size)
        self.detail_grid.add_widget(self.s)
        self.b = Button(text="Clear Screen")
        self.b.bind(on_release = self.clear_screen)
        self.detail_grid.add_widget(self.b)
        self.b = Button(text="Done")
        self.b.bind(on_release = self.done_shape_erase)
        self.detail_grid.add_widget(self.b)
        self.add_widget(self.detail_grid)

        with self.canvas:
            Color(.5,.5,.5)
            self.mouse = Ellipse(size=(self.pen_size, self.pen_size), pos=Window.mouse_pos)

    def shape_pen(self, event):
        self.shape.pos = (2000, 2000)
        self.remove_widget(self.shape_grid)
        with self.canvas:
            Color(0,0,0)
            Rectangle(size=(1000,200), pos=(400,0))
        self.add_widget(self.shape_grid)

        self.detail_grid = GridLayout(cols = 2, size=(600,200), pos=(800,0))
        self.label = Label(text='Size : '+str(self.pen_size))
        self.detail_grid.add_widget(self.label)
        self.s = Slider(min=1, max=100, value=self.pen_size)
        self.s.bind(value = self.update_pen_size)
        self.detail_grid.add_widget(self.s)
        self.b = Button(text="Fill Screen")
        self.b.bind(on_release = self.fill_screen)
        self.detail_grid.add_widget(self.b)
        self.b2 = Button(text="Save")
        self.b2.bind(on_release = self.save_screen)
        self.detail_grid.add_widget(self.b2)
        self.add_widget(self.detail_grid)

        with self.canvas:
            Color(*self.color)
            self.mouse = Ellipse(size=(self.pen_size, self.pen_size), pos=Window.mouse_pos)

    def update_pen_size(self, instance, value):
        self.pen_size = value
        self.mouse.size = (value, value)
        self.label.text = "Size : "+str(value)

    def fill_screen(self, event):
        with self.canvas:
            Color(*self.color)
            Rectangle(size=(1600,800), pos=(0, 200))

    def clear_screen(self, event):
        with self.canvas:
            Color(1,1,1)
            Rectangle(size=(1600,800), pos=(0, 200))

    def save_screen(self, event):
        s = str(datetime.today())[:-7]
        self.export_to_png('C:\\Users\\ISHA\\Desktop\\{}-{}-{}-{}.png'.format(s[:10],s[11:13],s[14:16],s[17:]))

    def done_shape_erase(self, event):
        self.color = self.color_2
        self.remove_widget(self.detail_grid)
        del self.detail_grid
        with self.canvas:
            Color(1,1,1)
            Rectangle(size=(600,200), pos=(800,0))
            Color(*self.color)
            self.mouse = Ellipse(size=(self.pen_size, self.pen_size), pos=Window.mouse_pos)

    def update_rectangle(self, instance, value):
        self.rect.pos = self.pos
        self.rect.size = self.size

    def on_touch_down(self, touch):
        super(DrawingWidget, self).on_touch_down(touch)

        if(touch.pos[1]<200+(self.pen_size//2)):
            pass
        else:
            with self.canvas:
                Color(*self.color)
                self.line = Line(points=[touch.pos[0], touch.pos[1]], width=self.pen_size//2)

    def on_touch_move(self, touch):
        try:
            if(touch.pos[1]<200+(self.pen_size//2)):
                self.line.points = self.line.points + [touch.pos[0], 200+(self.pen_size//2)]
            else:
                self.line.points = self.line.points + [touch.pos[0], touch.pos[1]]
        except:
            pass

    def on_touch_up(self, touch):
        try:
            if(self.shape_state == 'line'):
                c = self.line.points
                self.line.points = [c[0], c[1], c[-2], c[-1]]
            del self.line
        except:
            pass

    def on_mouse_pos(self, *args):
        x,y = args[1]
        self.mouse.pos = [x,y]


class DrawingApp(App):

    def build(self):
        root_widget = DrawingWidget()
        return root_widget

DrawingApp().run()
