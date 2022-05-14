from manim import *

class CyrillicExample(Scene):
    def construct(self):
        r_preamble = r"""
\usepackage[T2A]{fontenc}
\usepackage[utf8]{inputenc}
\usepackage[russian]{babel}
\usepackage{amsmath}
\usepackage{amsfonts}
\usepackage{paratype}
\usepackage{nimbusmononarrow}
\usepackage{everysel}
\EverySelectfont{%
\fontdimen2\font=0.4em% interword space
\fontdimen3\font=0.2em% interword stretch
\fontdimen4\font=0.1em% interword shrink
\fontdimen7\font=0.1em% extra space
\hyphenchar\font=`\-% to allow hyphenation
}
\usepackage{csquotes}
\usepackage[unicode, linktocpage]{hyperref}
\usepackage{cite}
\usepackage{soulutf8}
        """
        template1 = TexTemplate(
            preamble=r_preamble
            )
        Task1 = Tex("Задание 1" , tex_template = template1 , color = ORANGE)
        Task1Tex = Tex(r"Решите систему неравенств" , tex_template = template1).next_to(Task1 , DOWN)
        Task1Tex2 = Matrix([["7 (3x + 2) - 3 (7x + 2) > 2x"], ["(x - 5)(x+8) < 0"]],element_alignment_corner=LEFT,left_bracket="\{",right_bracket=" ").next_to(Task1Tex , DOWN)
        Task1VG = VGroup(Task1 , Task1Tex , Task1Tex2).move_to([0 , 0 , 0]).scale(0.7)
       
        self.play(FadeIn(Task1 , shift=UP/2))
        self.wait(0.5)
        self.play(FadeIn(Task1Tex , Task1Tex2 , shift=UP/2))
        Task1rec = SurroundingRectangle(Task1VG , color = WHITE , buff = 0.3 , stroke_width = .5)
        self.play(Create(Task1rec , run_time = 4 , compass_directions=UP))
        self.wait()
        self.play(FadeOut(Task1rec))
        self.play(FadeOut(Task1 , Task1Tex))
        self.play(Task1Tex2.animate.move_to([-3.5 , 2 , 0]))
        Task1Tex3 = Matrix([["21x + 14 - 21x -6 > 2x"], ["x < 5"] , ["x > -8"]],element_alignment_corner=LEFT,left_bracket="\{",right_bracket=" ").scale(0.7).move_to([1.25 , 2 , 0])
        self.wait(1) 
        self.play(TransformFromCopy(Task1Tex2 , Task1Tex3))
        self.wait(2)
        Task1Tex4 = Matrix([["x < 4"], ["x < 5"] , ["x > -8"]],element_alignment_corner=LEFT,left_bracket="\{",right_bracket=" ").scale(0.7).next_to(Task1Tex3 , RIGHT)
        self.play(TransformFromCopy(Task1Tex3 , Task1Tex4))


        self.play(Task1Tex4[0][0].animate.set_color(YELLOW) , Task1Tex4[0][1].animate.set_color(BLUE) , Task1Tex4[0][2].animate.set_color(RED))

       
        Task1dot4 = Circle(0.07 , stroke_width = 1 , stroke_color = WHITE , fill_color = BLACK , fill_opacity = 1).move_to([0.2 , 0 , 0])
        Task1dot5 = Circle(0.07 , stroke_width = 1 , stroke_color = WHITE , fill_color = BLACK , fill_opacity = 1).move_to([0.6 , 0 , 0])
        Task1dot8 = Circle(0.07 , stroke_width = 1 , stroke_color = WHITE , fill_color = BLACK , fill_opacity = 1).move_to([-1 ,0  , 0])
        Task1Line = Line(start = LEFT*2 , end = RIGHT*2 , stroke_width = 0.5)


        T1LineText4 = MathTex("4" , color = YELLOW).next_to(Task1dot4 , DOWN/4).scale(0.7)
        T1LineText5 = MathTex("5" , color = BLUE).next_to(Task1dot5 , DOWN/4).scale(0.7)
        T1LineText8 = MathTex("-8" , color = RED).next_to(Task1dot8 , DOWN/4).scale(0.7)

        self.play(Create(Task1Line) , FadeIn(Task1dot4 , Task1dot5 , Task1dot8))

        self.play(FadeIn(T1LineText4 , T1LineText5 , T1LineText8 , shift = UP/2))

        self.play(FadeOut(Task1dot4 , Task1dot5 , T1LineText4 , T1LineText5))
        #красный отрезок
        T1Line8 = Line(start = [-0.93 , 0 , 0] , end = RIGHT*2 , color = RED , stroke_width = 2)
        T1TexLine8 = MathTex("x > -8" , color = RED).scale(0.7).next_to(T1Line8 , UP/2)
        self.play(Create(T1Line8) , FadeIn (T1TexLine8 , shift = DOWN / 2 ))
        self.wait(0.5)
        self.play(Uncreate(T1Line8) , FadeOut (T1TexLine8 , shift = UP / 2))
        self.play(FadeOut(Task1dot8 , T1LineText8))
        #желтый отрезок
        self.play(FadeIn(Task1dot4 , T1LineText4))
        T1Line4 = Line(start = [0.13 , 0 , 0] , end = LEFT*2 , color = YELLOW , stroke_width = 2)
        T1TexLine4 = MathTex("x < 4" , color = YELLOW).scale(0.7).next_to(T1Line4 , UP/2)
        self.play(Create(T1Line4) , FadeIn (T1TexLine4 , shift = DOWN / 2 ))
        self.wait(0.5)
        self.play(Uncreate(T1Line4) , FadeOut (T1TexLine4 , shift = UP / 2))
        self.play(FadeOut(Task1dot4 , T1LineText4))
        #синий отрезок
        self.play(FadeIn(Task1dot5 , T1LineText5))
        T1Line5 = Line(start = [0.53 , 0 , 0] , end = LEFT*2 , color = BLUE , stroke_width = 2)
        T1TexLine5 = MathTex("x < 5" , color = BLUE).scale(0.7).next_to(T1Line5 , UP/2)
        self.play(Create(T1Line5) , FadeIn (T1TexLine5 , shift = DOWN / 2 ))
        self.wait(0.5)
        self.play(Uncreate(T1Line5) , FadeOut (T1TexLine5 , shift = UP / 2))
        self.play(FadeOut(Task1dot5 , T1LineText5))
        self.wait(0.5)



        self.play(FadeIn(Task1dot4 , Task1dot5 , Task1dot8 , T1LineText4 , T1LineText5 , T1LineText8))
        T1Line42 = Line(start = [0.13 , 0 , 0] , end = LEFT*2 , color = YELLOW , stroke_width = 2 , stroke_opacity = 0.5)
        T1Line52 = Line(start = [0.53 , 0 , 0] , end = LEFT*2 , color = BLUE , stroke_width = 2 , stroke_opacity = 0.5)
        T1Line82 = Line(start = [-0.93 , 0 , 0] , end = RIGHT*2 , color = RED , stroke_width = 2 , stroke_opacity = 0.5)
        self.play(Create(T1Line42 , run_time = 5) , Create(T1Line52 , run_time = 5) , Create(T1Line82 , run_time = 5))
        T1purLine = Line([-0.93 , 0 , 0] , [0.13 , 0 , 0] , color = ORANGE , stroke_width = 3)
        self.play(Create(T1purLine , run_time = 4))
        self.wait(0.5)
        self.play(FadeOut(T1Line42 ,  run_time = 3) , FadeOut(T1Line52 ,  run_time = 1) , FadeOut(T1Line82 ,  run_time = 1))
        T1Ans = Tex(r"Ответ : (-8 ; 4)" , color = PURPLE , tex_template = template1).scale(0.7).to_edge(DL)
        self.play(FadeIn(T1Ans , shift=UP/2))
        self.wait(2)

        self.play(FadeOut(Task1Tex2 , shift=UP) , run_time = 0.5)
        self.play(FadeOut(Task1Tex3 , shift=UP) , run_time = 0.5)
        self.play(FadeOut(Task1Tex4 , shift=UP) , run_time = 0.5)
        self.play(Uncreate(T1purLine))
        self.play(FadeOut(Task1dot4 , Task1dot5 , Task1dot8 , T1LineText4 , T1LineText5 , T1LineText8))
        self.play(Uncreate(Task1Line))
        self.play(FadeOut(T1Ans))