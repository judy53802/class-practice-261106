from pathlib import Path

from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.util import Inches, Pt


OUTPUT = Path(__file__).parent / "곽주은_자기소개_포트폴리오.pptx"
prs = Presentation()
prs.slide_width = Inches(13.333)
prs.slide_height = Inches(7.5)

COLORS = {
    "ink": RGBColor(23, 32, 42),
    "paper": RGBColor(255, 250, 242),
    "pink": RGBColor(255, 79, 129),
    "yellow": RGBColor(255, 209, 102),
    "blue": RGBColor(76, 201, 240),
    "green": RGBColor(128, 237, 153),
    "purple": RGBColor(131, 56, 236),
    "orange": RGBColor(255, 126, 87),
    "red": RGBColor(239, 71, 111),
    "teal": RGBColor(42, 157, 143),
    "lavender": RGBColor(205, 180, 219),
    "white": RGBColor(255, 255, 255),
}


def add_background(slide, color):
    shape = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
    shape.fill.solid()
    shape.fill.fore_color.rgb = color
    shape.line.fill.background()
    slide.shapes._spTree.remove(shape._element)
    slide.shapes._spTree.insert(2, shape._element)


def add_shape(slide, kind, x, y, w, h, fill, line=None, radius=False):
    shape = slide.shapes.add_shape(kind, Inches(x), Inches(y), Inches(w), Inches(h))
    shape.fill.solid()
    shape.fill.fore_color.rgb = fill
    if line is None:
        shape.line.fill.background()
    else:
        shape.line.color.rgb = line
        shape.line.width = Pt(2)
    return shape


def add_text(slide, text, x, y, w, h, size=20, color=None, bold=False, font="Aptos", align=PP_ALIGN.LEFT):
    box = slide.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h))
    frame = box.text_frame
    frame.clear()
    frame.word_wrap = True
    frame.margin_left = Inches(0.06)
    frame.margin_right = Inches(0.06)
    frame.vertical_anchor = MSO_ANCHOR.MIDDLE
    paragraph = frame.paragraphs[0]
    paragraph.alignment = align
    run = paragraph.add_run()
    run.text = text
    run.font.name = font
    run.font.size = Pt(size)
    run.font.bold = bold
    run.font.color.rgb = color or COLORS["ink"]
    return box


def add_label(slide, text, x, y, color=None):
    return add_text(slide, text, x, y, 4, 0.3, 10, color or COLORS["purple"], True, "Aptos", PP_ALIGN.LEFT)


def add_card(slide, x, y, w, h, color, icon, title, body):
    add_shape(slide, MSO_SHAPE.ROUNDED_RECTANGLE, x, y, w, h, color, COLORS["ink"])
    add_text(slide, icon, x + 0.25, y + 0.2, 0.6, 0.55, 24, COLORS["ink"], False, "Aptos")
    add_text(slide, title, x + 0.25, y + 0.82, w - 0.5, 0.38, 17, COLORS["ink"], True, "Aptos Display")
    add_text(slide, body, x + 0.25, y + 1.28, w - 0.5, h - 1.5, 12, COLORS["ink"], False, "Aptos")


# 1. Cover
slide = prs.slides.add_slide(prs.slide_layouts[6])
add_background(slide, COLORS["paper"])
add_shape(slide, MSO_SHAPE.RECTANGLE, 0, 0, 4.4, 7.5, COLORS["pink"])
add_shape(slide, MSO_SHAPE.RECTANGLE, 4.4, 0, 2.8, 7.5, COLORS["yellow"])
add_shape(slide, MSO_SHAPE.RECTANGLE, 7.2, 0, 3.2, 7.5, COLORS["blue"])
add_shape(slide, MSO_SHAPE.RECTANGLE, 10.4, 0, 2.933, 7.5, COLORS["green"])
add_shape(slide, MSO_SHAPE.OVAL, 9.3, 0.6, 2.4, 2.4, COLORS["purple"])
add_shape(slide, MSO_SHAPE.STAR_5_POINT, 10.7, 4.8, 1.1, 1.1, COLORS["orange"])
add_text(slide, "PERSONAL PORTFOLIO / 2026", 0.7, 0.7, 6, 0.4, 14, COLORS["ink"], True)
add_text(slide, "곽주은", 0.7, 2.0, 8.5, 1.45, 54, COLORS["ink"], True, "Aptos Display")
add_text(slide, "배우고 만들며 성장하는 사람", 0.75, 3.65, 6.5, 0.55, 22, COLORS["ink"], True)
add_text(slide, "청주교육대학교", 0.75, 4.28, 5.5, 0.45, 17, COLORS["ink"], False)
add_text(slide, "CURIOUS  •  CREATIVE  •  ALWAYS LEARNING", 0.75, 6.55, 7.5, 0.35, 12, COLORS["ink"], True)


# 2. About and affiliation
slide = prs.slides.add_slide(prs.slide_layouts[6])
add_background(slide, COLORS["paper"])
add_label(slide, "01 / ABOUT ME", 0.65, 0.45)
add_text(slide, "저를 소개합니다", 0.65, 0.85, 7, 0.7, 32, COLORS["ink"], True, "Aptos Display")
add_shape(slide, MSO_SHAPE.ROUNDED_RECTANGLE, 0.65, 2.0, 7.1, 3.8, COLORS["white"], COLORS["ink"])
add_text(slide, "안녕하세요!\n새로운 것을 배우고, 직접 시도하고, 경험을 나누는 일을 좋아합니다.", 1.0, 2.45, 6.4, 1.5, 23, COLORS["ink"], True, "Aptos Display")
add_text(slide, "이 발표는 제가 어떤 사람인지, 무엇을 배우고 어떤 꿈을 향해 가고 있는지 담은 작은 기록입니다.", 1.0, 4.35, 5.9, 0.8, 15, COLORS["ink"])
add_shape(slide, MSO_SHAPE.ROUNDED_RECTANGLE, 8.2, 1.55, 4.45, 4.7, COLORS["purple"], COLORS["ink"])
add_text(slide, "MY HOME BASE", 8.65, 2.0, 3.3, 0.35, 12, COLORS["yellow"], True)
add_text(slide, "청주교육대학교", 8.65, 2.65, 3.5, 0.95, 29, COLORS["white"], True, "Aptos Display")
add_text(slide, "배움과 실천을 연결하며\n미래의 교사를 준비하는 곳", 8.65, 4.0, 3.2, 0.9, 16, COLORS["white"])
add_text(slide, "EDUCATION  •  CARE  •  POSSIBILITY", 8.65, 5.55, 3.6, 0.4, 11, COLORS["yellow"], True)


# 3. Dream
slide = prs.slides.add_slide(prs.slide_layouts[6])
add_background(slide, COLORS["blue"])
add_shape(slide, MSO_SHAPE.OVAL, 9.9, -0.5, 4.1, 4.1, COLORS["yellow"])
add_shape(slide, MSO_SHAPE.OVAL, -1.0, 5.5, 3.0, 3.0, COLORS["green"])
add_label(slide, "02 / MY DREAM", 0.7, 0.6, COLORS["ink"])
add_text(slide, "내가 그리고 있는 미래", 0.7, 1.15, 8.2, 0.75, 35, COLORS["ink"], True, "Aptos Display")
add_shape(slide, MSO_SHAPE.ROUNDED_RECTANGLE, 0.7, 2.35, 11.9, 3.25, COLORS["purple"], COLORS["ink"])
add_text(slide, "“", 1.15, 2.55, 0.7, 0.8, 55, COLORS["yellow"], True)
add_text(slide, "아이들이 자신의 꿈을 마음껏 펼칠 수 있도록\n격려해주는 초등교사가 되고 싶습니다.", 1.85, 3.0, 9.8, 1.35, 28, COLORS["white"], True, "Aptos Display")
add_text(slide, "아이들의 가능성을 발견하고, 용기를 주는 선생님", 1.9, 4.75, 7.5, 0.4, 15, COLORS["yellow"], True)
add_text(slide, "DREAM BIG  •  HELP OTHERS  •  KEEP GROWING", 0.75, 6.65, 7.5, 0.35, 12, COLORS["ink"], True)


# 4. Lessons
slide = prs.slides.add_slide(prs.slide_layouts[6])
add_background(slide, COLORS["paper"])
add_label(slide, "03 / WHAT I LEARNED", 0.65, 0.4)
add_text(slide, "배운 수업들", 0.65, 0.85, 7, 0.65, 32, COLORS["ink"], True, "Aptos Display")
lessons = [
    ("🐍", "Python 기초", "변수, 조건문, 반복문으로 문제를 해결했습니다.", COLORS["pink"]),
    ("📊", "데이터 분석", "데이터를 정리하고 차트로 의미를 발견했습니다.", COLORS["yellow"]),
    ("🎨", "웹 디자인", "사용자가 보기 좋은 화면과 색을 고민했습니다.", COLORS["blue"]),
    ("🚀", "프로젝트 실습", "배운 내용을 작은 서비스로 직접 구현했습니다.", COLORS["green"]),
]
for index, (icon, title, body, color) in enumerate(lessons):
    add_card(slide, 0.65 + (index % 2) * 6.25, 1.9 + (index // 2) * 2.25, 5.55, 1.8, color, icon, title, body)
add_text(slide, "배운 것을 나누고, 교실에서 다시 활용하는 사람이 되고 싶습니다.", 0.7, 6.55, 10, 0.4, 15, COLORS["purple"], True)


# 5. Travel
slide = prs.slides.add_slide(prs.slide_layouts[6])
add_background(slide, COLORS["ink"])
add_label(slide, "04 / PLACES I HAVE BEEN", 0.65, 0.4, COLORS["yellow"])
add_text(slide, "여행의 장면들", 0.65, 0.85, 7, 0.65, 32, COLORS["white"], True, "Aptos Display")
travels = [
    ("SEOUL", "대한민국", "🌆", "익숙하지만 매번 새로운 동네", COLORS["yellow"]),
    ("TOKYO", "일본", "🗼", "빠르고 섬세한 도시의 에너지", COLORS["blue"]),
    ("PARIS", "프랑스", "🥐", "천천히 걷고 오래 바라본 거리", COLORS["green"]),
    ("BALI", "인도네시아", "🌴", "마음의 속도를 낮춘 여행", COLORS["pink"]),
]
for index, (place, country, emoji, note, color) in enumerate(travels):
    x = 0.65 + index * 3.1
    add_shape(slide, MSO_SHAPE.ROUNDED_RECTANGLE, x, 2.05, 2.7, 3.55, color, COLORS["white"])
    add_text(slide, emoji, x + 0.25, 2.35, 0.65, 0.6, 26, COLORS["ink"])
    add_text(slide, place, x + 0.25, 3.15, 2.1, 0.45, 20, COLORS["ink"], True, "Aptos Display")
    add_text(slide, country, x + 0.25, 3.7, 2, 0.35, 12, COLORS["ink"], True)
    add_text(slide, note, x + 0.25, 4.45, 2.15, 0.65, 13, COLORS["ink"])
add_text(slide, "여행은 새로운 시선으로 세상을 바라보는 연습입니다.", 0.7, 6.45, 9.5, 0.4, 16, COLORS["white"], True)


# 6. Closing
slide = prs.slides.add_slide(prs.slide_layouts[6])
add_background(slide, COLORS["orange"])
add_shape(slide, MSO_SHAPE.OVAL, 9.6, 0.2, 3.2, 3.2, COLORS["purple"])
add_shape(slide, MSO_SHAPE.STAR_5_POINT, 0.7, 5.25, 1.2, 1.2, COLORS["yellow"])
add_label(slide, "05 / KEEP IN TOUCH", 0.75, 0.7, COLORS["ink"])
add_text(slide, "고맙습니다", 0.75, 1.35, 7.5, 0.85, 44, COLORS["ink"], True, "Aptos Display")
add_text(slide, "배우고, 만들고, 나누는 사람\n곽주은의 이야기였습니다.", 0.8, 2.65, 6.8, 1.1, 25, COLORS["white"], True, "Aptos Display")
add_shape(slide, MSO_SHAPE.ROUNDED_RECTANGLE, 7.8, 3.15, 4.45, 2.05, COLORS["white"], COLORS["ink"])
add_text(slide, "📮  hello@example.com\n💻  github.com/your-id\n📸  @your_id", 8.25, 3.55, 3.7, 1.2, 16, COLORS["ink"], True)
add_text(slide, "Made with curiosity, color, and care ✦", 0.8, 6.65, 7.5, 0.35, 13, COLORS["ink"], True)


prs.save(OUTPUT)
print(f"created: {OUTPUT}")