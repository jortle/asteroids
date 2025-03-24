import pygame
from constants import SCREEN_WIDTH


def render_hud(settings_dict, minute=0, second=0, score=0, accuracy=0, rpm=0):
    # Initialize variables
    # time related
    Font = pygame.font.SysFont("firacodenerdfontpropo", 25)
    White = (255, 255, 255)

    # hud init

    HudRect = None
    vertical_offset = 20  # Starting vertical position
    spacing = 20  # Space between elements

    # List to store rendered elements and their positions
    hud_elements = []

    # Calculate the total width of the HUD based on enabled elements
    total_width = 0
    if settings_dict.get("time"):
        TimeText = Font.render(f" Time {minute:02}:{second:02} ", 0, White)
        total_width += spacing + TimeText.get_width()
    if settings_dict.get("score"):
        ScoreText = Font.render(f" Score {score:d} ", 0, White)
        total_width += spacing + ScoreText.get_width()
    if settings_dict.get("accuracy"):
        AccuracyText = Font.render(f" Accuracy {accuracy:d}% ", 0, White)
        total_width += spacing + AccuracyText.get_width()
    if settings_dict.get("rpm"):
        RPMText = Font.render(f" RPM {rpm:d} ", 0, White)
        total_width += spacing + RPMText.get_width()

    horizontal_offset = (
        SCREEN_WIDTH - total_width
    ) // 2  # Starting horizontal position
    # Render each element based on settings_dict
    if settings_dict.get("time"):
        TimeText = Font.render(f" Time {minute:02}:{second:02} ", 0, White)
        TimeTextR = TimeText.get_rect(midleft=(horizontal_offset, vertical_offset))
        hud_elements.append((TimeText, TimeTextR))
        horizontal_offset += TimeText.get_width() + spacing  # Move to the right

    if settings_dict.get("score"):
        ScoreText = Font.render(f" Score {score:d} ", 0, White)
        ScoreTextR = ScoreText.get_rect(midleft=(horizontal_offset, vertical_offset))
        hud_elements.append((ScoreText, ScoreTextR))
        horizontal_offset += ScoreText.get_width() + spacing  # Move to the right

    if settings_dict.get("accuracy"):
        AccuracyText = Font.render(f" Accuracy {accuracy:d}% ", 0, White)
        AccuracyTextR = AccuracyText.get_rect(
            midleft=(horizontal_offset, vertical_offset)
        )
        hud_elements.append((AccuracyText, AccuracyTextR))
        horizontal_offset += AccuracyText.get_width() + spacing  # Move to the right

    if settings_dict.get("rpm"):
        RPMText = Font.render(f" RPM {rpm:d} ", 0, White)
        RPMTextR = RPMText.get_rect(midleft=(horizontal_offset, vertical_offset))
        hud_elements.append((RPMText, RPMTextR))
        horizontal_offset += RPMText.get_width() + spacing  # Move to the right

    # Calculate the bounding rectangle (HudRect)
    for _, rect in hud_elements:
        if HudRect is None:
            HudRect = rect
        else:
            HudRect = pygame.Rect.union(HudRect, rect)

    if HudRect:
        HudRect.center = (SCREEN_WIDTH // 2, vertical_offset)

    return hud_elements, HudRect
