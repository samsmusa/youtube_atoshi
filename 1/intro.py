from manim import *
import numpy as np
from random import randint, shuffle
import random



class intro_1(Scene):
    def construct(self):
        text = Tex(
            r"\[E = mc^2\]",
            r"\[e^{i\pi}+1=0\]",
            r"\[dq=du+dw\]",
            r"\[\int dx = x\]",
            r"\[cos(2\theta) = cos^2(\theta) - sin^2(\theta)\]",
            r"\[sin(2\theta) = 2sin(\theta)cos(\theta)\]",
            r"\[tan(a+b)=\frac{tan(a)+tan(b)}{1-tan(a)tan(b)}\]",
            r"\[tan(\alpha)= \frac{sin(\alpha)}{cos(\alpha)}\]",
            r"\[a^2=b^2+c^2-2bc cos(A)\]",
            r"\[sin^2(\theta)+cos^2(\theta)=1\]",
            r"\[log_a\left ( \frac{u}{v} \right )=log_au - log_av\]",
            r"\[z^{-1}=\frac{1}{\left | z \right |^{2}}\cdot \bar{z}\]",
            r"\[z^{n}= \left | z \right |^{n}.e^{in\theta}\]",
            r"\[a^m\div a^n=a^{m-n}\]",
            r"\[A^2+B^2=C^2\]",
            r"\[a^m\times a^n=a^{m+n}\]",
            r"\[a^{\frac{p}{q}}=\sqrt[q]{a^p}\]",
            r"\[\frac{x-x_o}{u_1}=\frac{y-y_o}{u_2}=\frac{z-z_o}{u_3}\]",
            r"\[(x-x_o)^2+(y-y_o)^2=r^2\]",
            r"\[(x-x_o)^2+(y-y_o)^2+(z-z_o)^2=r^2\]",
            r"\[{(\frac{x-h}{a})}^{2}+{(\frac{y-k}{b})}^{2}=1\]",
            r"\[p\wedge (q\vee r) \Leftrightarrow (p\wedge q)\vee(p \wedge r)\]",
            r"\[\sim (\exists x:p(x))\Leftrightarrow \forall x,\sim p(x)\]",
            r"\[cos(\alpha)=\frac{\left | \vec{u}\cdot\vec{v } \right |}{\left |\left | \vec{u} \right |\right | \cdot \left | \left | \vec{v } \right |\right |}\]",
            r"\[P(A\mid B) = \frac{P(A\cap B)}{P(B)}\]",
     )

        pyth = Tex(
            r"\[A^2+B^2=C^2\]"
        )
        pyth.set_color(RED_A)

        col = [RED,YELLOW,RED_A,RED_C,RED_D,GREEN,GREEN_B,GREEN_E,YELLOW_B,YELLOW_A]
        col1 = [[p,q,r] for p in [RED_A,RED_B,RED_D] for q in [BLUE_A,BLUE_C,BLUE_E] for r in [GREEN_A,GREEN_C,GREEN_E]]


        li = []

        for i,j in zip([0,-3,3,3,-3,3,-3],[0,-3,3,-3,3,0,0]):
            li.append([i,j,0])
            
        # text[0].scale(1.2)

        for tex_,co, po in zip(text[:5],col[:5], li[:5]):
            tex_.scale(1.2)
            tex_.set_color_by_gradient(co)
            tex_.move_to(po)
            self.add_sound(f"assets\\sound\\bul.mp3")
            self.play(GrowFromCenter(tex_), run_time = 0.4)
            



        

        st1 = []

        for i,j in zip([5,3,2,1],[3,1,3,2]):
            st1.append([i,j,0])
            st1.append([i,-j,0])
            st1.append([-i,j,0])
            st1.append([-i,-j,0])
            
        
        st = st1+li[5:]
        st.append([-3,3,0])

        

        
        for tex, pos in zip(text[5: ], st):
 
            tex.set_color(col[randint(0,len(col)-1)])
            tex.move_to(pos)
            self.add_sound(f"assets\\sound\\bul.mp3")
            self.play(GrowFromCenter(tex), run_time= 0.2)

        self.wait(1)

        lin = list(range(0,len(text)))
        shuffle(lin)

        for i_ in lin:
            if i_ == 14:
                pass
            else:
                self.add_sound(f"assets\\sound\\fade.mp3")
                self.play(FadeOut(text[i_]), run_time = 0.1)

        self.play(
            ReplacementTransform(text[14], pyth)
        )
        
        self.wait(2)