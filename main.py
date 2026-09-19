# main.py
# Firefighting Safety Poster - Tkinter Canvas Layout
# All text white, dark themed background, with sections for chemicals, safety, and a visual middle panel.

import tkinter as tk

# -----------------------------
# Basic window setup
# -----------------------------
WIDTH = 1200
HEIGHT = 800

root = tk.Tk()
root.title("Firefighting Safety Poster")

canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="black", highlightthickness=0)
canvas.pack()

# -----------------------------
# Colors
# -----------------------------
TITLE_BG = "#1b3b6b"      # darkish blue
PANEL_BG = "#2b2b2b"      # darkish grey
TEXT_COLOR = "white"
ACCENT_ORANGE = "#ff8c00"
ACCENT_RED = "#cc3333"
ACCENT_YELLOW = "#ffcc00"
ACCENT_BLUE = "#3399ff"

# -----------------------------
# Layout dimensions
# -----------------------------
TITLE_HEIGHT = 120
MARGIN = 20

LEFT_PANEL_WIDTH = (WIDTH - 4 * MARGIN) // 3
RIGHT_PANEL_WIDTH = LEFT_PANEL_WIDTH
MIDDLE_PANEL_WIDTH = WIDTH - LEFT_PANEL_WIDTH - RIGHT_PANEL_WIDTH - 4 * MARGIN

LEFT_X1 = MARGIN
LEFT_X2 = LEFT_X1 + LEFT_PANEL_WIDTH

MIDDLE_X1 = LEFT_X2 + MARGIN
MIDDLE_X2 = MIDDLE_X1 + MIDDLE_PANEL_WIDTH

RIGHT_X1 = MIDDLE_X2 + MARGIN
RIGHT_X2 = RIGHT_X1 + RIGHT_PANEL_WIDTH

CONTENT_TOP = TITLE_HEIGHT + MARGIN
CONTENT_BOTTOM = HEIGHT - MARGIN

# -----------------------------
# Draw title bar
# -----------------------------
canvas.create_rectangle(
    0, 0, WIDTH, TITLE_HEIGHT,
    fill=TITLE_BG, outline=""
)

canvas.create_text(
    WIDTH // 2, TITLE_HEIGHT // 2,
    text="Firefighting Safety",
    fill=TEXT_COLOR,
    font=("Helvetica", 40, "bold")
)

# -----------------------------
# Draw left and right panels
# -----------------------------
canvas.create_rectangle(
    LEFT_X1, CONTENT_TOP,
    LEFT_X2, CONTENT_BOTTOM,
    fill=PANEL_BG, outline=""
)

canvas.create_rectangle(
    RIGHT_X1, CONTENT_TOP,
    RIGHT_X2, CONTENT_BOTTOM,
    fill=PANEL_BG, outline=""
)

# -----------------------------
# Draw middle visual panel (not full height)
# -----------------------------
MIDDLE_VISUAL_TOP = CONTENT_TOP
MIDDLE_VISUAL_BOTTOM = CONTENT_TOP + (CONTENT_BOTTOM - CONTENT_TOP) * 0.55

canvas.create_rectangle(
    MIDDLE_X1, MIDDLE_VISUAL_TOP,
    MIDDLE_X2, MIDDLE_VISUAL_BOTTOM,
    fill="#111111", outline=""
)

# Decorative shapes to simulate “images”
# Flames
for i in range(6):
    x_center = MIDDLE_X1 + 60 + i * 80
    canvas.create_polygon(
        x_center, MIDDLE_VISUAL_BOTTOM - 40,
        x_center - 20, MIDDLE_VISUAL_BOTTOM - 10,
        x_center - 10, MIDDLE_VISUAL_BOTTOM - 60,
        x_center + 10, MIDDLE_VISUAL_BOTTOM - 60,
        x_center + 20, MIDDLE_VISUAL_BOTTOM - 10,
        fill=ACCENT_RED, outline=""
    )

# Water droplet
canvas.create_oval(
    MIDDLE_X1 + 80, MIDDLE_VISUAL_TOP + 40,
    MIDDLE_X1 + 140, MIDDLE_VISUAL_TOP + 120,
    fill=ACCENT_BLUE, outline=""
)
canvas.create_polygon(
    MIDDLE_X1 + 110, MIDDLE_VISUAL_TOP + 20,
    MIDDLE_X1 + 80, MIDDLE_VISUAL_TOP + 80,
    MIDDLE_X1 + 140, MIDDLE_VISUAL_TOP + 80,
    fill=ACCENT_BLUE, outline=""
)

# Shield icon
canvas.create_polygon(
    MIDDLE_X2 - 140, MIDDLE_VISUAL_TOP + 40,
    MIDDLE_X2 - 100, MIDDLE_VISUAL_TOP + 30,
    MIDDLE_X2 - 60, MIDDLE_VISUAL_TOP + 40,
    MIDDLE_X2 - 60, MIDDLE_VISUAL_TOP + 100,
    MIDDLE_X2 - 100, MIDDLE_VISUAL_TOP + 130,
    MIDDLE_X2 - 140, MIDDLE_VISUAL_TOP + 100,
    fill=ACCENT_ORANGE, outline=""
)

canvas.create_text(
    (MIDDLE_X1 + MIDDLE_X2) // 2,
    MIDDLE_VISUAL_TOP + 30,
    text="Hazards & Protection",
    fill=TEXT_COLOR,
    font=("Helvetica", 20, "bold")
)

canvas.create_text(
    (MIDDLE_X1 + MIDDLE_X2) // 2,
    MIDDLE_VISUAL_TOP + 70,
    text="Firefighters face dangerous chemicals,\nheat, smoke, and toxic environments.",
    fill=TEXT_COLOR,
    font=("Helvetica", 14),
    justify="center"
)

# -----------------------------
# Left panel content: Chemicals & WHMIS symbols
# -----------------------------
left_text_x = LEFT_X1 + 15
y = CONTENT_TOP + 25

canvas.create_text(
    left_text_x, y,
    text="Chemicals Firefighters Face",
    fill=TEXT_COLOR,
    font=("Helvetica", 18, "bold"),
    anchor="nw"
)
y += 40

def draw_whmis_symbol(x, y, label, color):
    size = 26
    canvas.create_rectangle(
        x, y, x + size, y + size,
        outline=color, width=2
    )
    canvas.create_text(
        x + size / 2, y + size / 2,
        text=label,
        fill=color,
        font=("Helvetica", 10, "bold")
    )

# List of chemicals with WHMIS-style indicators
chemicals = [
    ("Smoke (particulates)", "Respiratory irritation, long-term lung damage", "!", ACCENT_YELLOW),
    ("Carbon Monoxide (CO)", "Reduces oxygen in blood, can cause death", "HH", ACCENT_RED),
    ("Hydrogen Cyanide (HCN)", "Blocks cellular oxygen use, highly toxic", "SK", ACCENT_RED),
    ("Water", "Can cause slips, electrical hazards, steam burns", "W", ACCENT_BLUE),
    ("Blood", "Biological hazard, risk of infection", "BIO", ACCENT_ORANGE),
    ("Diesel Exhaust", "Carcinogenic, respiratory irritation", "HH", ACCENT_YELLOW),
    ("Solvents & Fuels", "Flammable, can cause burns and explosions", "FL", ACCENT_RED),
]

for name, effect, symbol, color in chemicals:
    draw_whmis_symbol(left_text_x, y, symbol, color)
    canvas.create_text(
        left_text_x + 40, y,
        text=name,
        fill=TEXT_COLOR,
        font=("Helvetica", 13, "bold"),
        anchor="nw"
    )
    y += 22
    canvas.create_text(
        left_text_x + 40, y,
        text=f"What it does: {effect}",
        fill=TEXT_COLOR,
        font=("Helvetica", 11),
        anchor="nw"
    )
    y += 32

# Safety from chemicals
y += 10
canvas.create_text(
    left_text_x, y,
    text="How to Stay Safe from Chemicals",
    fill=TEXT_COLOR,
    font=("Helvetica", 16, "bold"),
    anchor="nw"
)
y += 30

safety_points_left = [
    "Wear SCBA (Self-Contained Breathing Apparatus) to avoid inhaling toxic gases.",
    "Use full turnout gear: helmet, coat, pants, gloves, and boots.",
    "Avoid direct contact with blood and bodily fluids; use medical gloves and face shields.",
    "Decontaminate gear after exposure to smoke, chemicals, or biological hazards.",
    "Follow WHMIS training to recognize hazard symbols and safety data sheets.",
    "Limit time in high-smoke areas and rotate crews to reduce exposure.",
]

for point in safety_points_left:
    canvas.create_text(
        left_text_x, y,
        text=f"• {point}",
        fill=TEXT_COLOR,
        font=("Helvetica", 11),
        anchor="nw",
        width=LEFT_PANEL_WIDTH - 30
    )
    y += 28

# -----------------------------
# Right panel content: Equipment & Safety Measures
# -----------------------------
right_text_x = RIGHT_X1 + 15
y = CONTENT_TOP + 25

canvas.create_text(
    right_text_x, y,
    text="Firefighter Safety Equipment",
    fill=TEXT_COLOR,
    font=("Helvetica", 18, "bold"),
    anchor="nw"
)
y += 40

equipment_points = [
    "Helmet: Protects head from falling debris and heat.",
    "Turnout/Bunker Gear: Flame-resistant coat and pants to shield from heat and flames.",
    "Gloves: Protect hands from burns, cuts, and chemical exposure.",
    "Boots: Provide traction and protect feet from sharp objects and heat.",
    "SCBA: Supplies clean air in smoke-filled or toxic environments.",
    "Eye Protection: Goggles or face shields to prevent chemical splashes and debris.",
]

for point in equipment_points:
    canvas.create_text(
        right_text_x, y,
        text=f"• {point}",
        fill=TEXT_COLOR,
        font=("Helvetica", 11),
        anchor="nw",
        width=RIGHT_PANEL_WIDTH - 30
    )
    y += 28

y += 10
canvas.create_text(
    right_text_x, y,
    text="Other Safety Systems",
    fill=TEXT_COLOR,
    font=("Helvetica", 16, "bold"),
    anchor="nw"
)
y += 30

other_safety_points = [
    "Eye-wash stations: Used to flush chemicals or debris from eyes.",
    "Emergency showers: Rinse off hazardous chemicals from skin and gear.",
    "Medical monitoring: Checks heart rate, temperature, and exposure levels.",
    "Rehab areas: Provide rest, hydration, and medical evaluation after intense operations.",
    "Decontamination lines: Clean equipment and personnel after chemical or smoke exposure.",
    "Communication systems: Radios and incident command to coordinate safe operations.",
]

for point in other_safety_points:
    canvas.create_text(
        right_text_x, y,
        text=f"• {point}",
        fill=TEXT_COLOR,
        font=("Helvetica", 11),
        anchor="nw",
        width=RIGHT_PANEL_WIDTH - 30
    )
    y += 28

# -----------------------------
# WHMIS symbol legend (bottom middle)
# -----------------------------
legend_y = MIDDLE_VISUAL_BOTTOM + 40
canvas.create_text(
    (MIDDLE_X1 + MIDDLE_X2) // 2,
    legend_y,
    text="WHMIS Safety Symbols (Simplified)",
    fill=TEXT_COLOR,
    font=("Helvetica", 16, "bold"),
    anchor="n"
)
legend_y += 30

legend_items = [
    ("FL", "Flammable materials (fuels, solvents)"),
    ("HH", "Health hazard (long-term or serious health effects)"),
    ("SK", "Skull & crossbones (acute toxicity, can be fatal)"),
    ("!", "Exclamation mark (irritant, less severe health effects)"),
    ("BIO", "Biohazard (blood, bodily fluids, infectious materials)"),
    ("W", "Water-related hazard (slips, electrical, steam)"),
]

legend_x_start = MIDDLE_X1 + 40
legend_x = legend_x_start
legend_y_row = legend_y

for symbol, meaning in legend_items:
    draw_whmis_symbol(legend_x, legend_y_row, symbol, ACCENT_YELLOW)
    canvas.create_text(
        legend_x + 40, legend_y_row,
        text=meaning,
        fill=TEXT_COLOR,
        font=("Helvetica", 11),
        anchor="nw",
        width=MIDDLE_PANEL_WIDTH - 80
    )
    legend_y_row += 30

# -----------------------------
# Run the Tkinter loop
# -----------------------------
root.mainloop()
