from manim import *
import numpy as np
from random import randint, shuffle
import random

class trangle35(Scene):
    def construct(self):

        text = Tex(
            "A",
            "B",
            "C",
            r"\[A^2\]",
            r"\[B^2\]",
            r"\[C^2\]",
        )

        dots = [[-1,-1,0],[1,-1,0],[1,1,0]]
        line1 = Line(dots[0],dots[1])
        line2 = Line(dots[2],dots[1])
        line3 = Line(dots[2],dots[0])
        line11 = line1.copy()
        
        line21 = line2.copy()

        line1.set_color(BLUE)
        line2.set_color(GREEN)
        line3.set_color(RED)

        sq1 = self.next(line1,dots[2])
        sq2 = self.next(line2,dots[0])
        sq3 = self.next(line3, dots[1])

        text[0].move_to(line1.get_center()+DOWN)
        text[0].set_color(line1.get_color())
        text[1].set_color(line2.get_color())
        text[2].set_color(line3.get_color())
        text[3].set_color(sq1.get_color())
        text[4].set_color(sq2.get_color())
        text[5].set_color(sq3.get_color())
        
        text[1].move_to(line2.get_center()+RIGHT)
        text[2].move_to(line3.get_center()+UL)
        text[3].move_to(sq1)
        text[4].move_to(sq2)
        text[5].move_to(sq3)

        VGroup(text[0],text[1],text[2]).scale(0.5)

  

        
        
    


        self.add(line1)
        el = self.get_elbow(line1)
        
        self.play(
            Create(el),
            ReplacementTransform(line11,line2))
        self.play(ReplacementTransform(line21, line3))
        self.play(
            Write(text[0]),
            Write(text[1]),
            Write(text[2]),
        )
        self.add_sound(f"assets\\sound\\cre.mp3")
        self.play(Create(sq1))
        self.add_sound(f"assets\\sound\\tr.mp3")
        self.play(ReplacementTransform(text[0],text[3]))
        
        self.add_sound(f"assets\\sound\\cre.mp3")
        self.play(Create(sq2))
        
        self.add_sound(f"assets\\sound\\tr.mp3")
        self.play(ReplacementTransform(text[1],text[4]))
        
        self.add_sound(f"assets\\sound\\cre.mp3")
        self.play(Create(sq3))
        
        self.add_sound(f"assets\\sound\\tr.mp3")
        self.play(ReplacementTransform(text[2],text[5]))
        
                    
        self.wait()

    def get_elbow(self, line):
        elbow = VGroup( Line(UL, LEFT), Line(UP, UL))
        elbow.set_stroke(width=1)
        elbow.scale(0.2, about_point=ORIGIN)
        elbow.rotate(
            line.get_angle() + 0 * DEGREES,
            about_point=ORIGIN
        )
        elbow.shift(line.get_end())
        return elbow

    def next(self,line, dot):
        square = Square(line.get_length(), color = line.get_color())   
        square.rotate(line.get_angle(), about_point=ORIGIN)
        square.move_to(line,aligned_edge=dot)
        return square
