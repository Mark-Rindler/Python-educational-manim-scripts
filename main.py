# final_color_stacked.py
from manim import *

class FinalColorEquationStacked(Scene):
    def construct(self):
        # Lines (stacked for readability)
        line1 = MathTex(
            r"\mathbf{C} = \text{ambient}\cdot\text{base}",
            font_size=72
        )
        line2 = MathTex(
            r"+\; k_D\big(\text{diffuse} + \text{specular}\big)",
            font_size=72
        )
        line3 = MathTex(
            r"+\; k_S\cdot\text{reflection}",
            font_size=72
        )

        # Group & layout
        eq = VGroup(line1, line2, line3).arrange(
            DOWN, aligned_edge=LEFT, buff=0.4
        ).to_edge(LEFT).shift(RIGHT*0.5)  # small nudge to center-ish

        # Term colors
        AMB  = YELLOW_E
        BASE = TEAL_A
        KD   = GREEN_B
        DS   = GREEN_C
        KS   = BLUE_B
        REFL = BLUE_D

        # Colorize by token on each line
        for m in (line1, line2, line3):
            m.set_color(WHITE)

        line1.set_color_by_tex(r"\text{ambient}", AMB)
        line1.set_color_by_tex(r"\text{base}", BASE)

        line2.set_color_by_tex(r"k_D", KD)
        line2.set_color_by_tex(r"\text{diffuse}", DS)
        line2.set_color_by_tex(r"\text{specular}", DS)

        line3.set_color_by_tex(r"k_S", KS)
        line3.set_color_by_tex(r"\text{reflection}", REFL)

        # Animations: write each line, then quick emphasis pulses
        self.play(Write(line1), run_time=0.9)
        self.wait(0.2)
        self.play(Write(line2), run_time=0.9)
        self.wait(0.2)
        self.play(Write(line3), run_time=0.9)
        self.wait(0.4)

        # Gentle indicates on each logical group
        self.play(
            Indicate(line1.get_parts_by_tex(r"\text{ambient}"), scale_factor=1.05),
            Indicate(line1.get_parts_by_tex(r"\text{base}"), scale_factor=1.05),
            run_time=0.6
        )
        self.wait(0.2)

        self.play(
            Indicate(line2.get_parts_by_tex(r"k_D"), scale_factor=1.05),
            Indicate(line2.get_parts_by_tex(r"\text{diffuse}"), scale_factor=1.05),
            Indicate(line2.get_parts_by_tex(r"\text{specular}"), scale_factor=1.05),
            run_time=0.6
        )
        self.wait(0.2)

        self.play(
            Indicate(line3.get_parts_by_tex(r"k_S"), scale_factor=1.05),
            Indicate(line3.get_parts_by_tex(r"\text{reflection}"), scale_factor=1.05),
            run_time=0.6
        )
        self.wait(0.6)
