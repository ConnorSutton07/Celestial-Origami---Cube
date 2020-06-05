from PIL import Image, ImageDraw

def draw_tabs(img, padding, c_north, c_south, c_front, c_right, c_back, c_left):
    width = img.width
    height = img.height
    # height and width adjusted to account for padding
    adjw = width - 2 * padding
    adjh = height - 2 * padding

    #draw all the lines around each square (gets a bit complicated because of padding for folding tabs)
    draw = ImageDraw.Draw(img)
    draw.line((0 + padding, adjh / 3 + padding, width - padding, adjh / 3 + padding), fill=0, width = 5)
    draw.line((0 + padding, adjh * (2/3) + padding, width - padding, adjh * (2/3) + padding), fill=0, width = 5)
    draw.line((adjw / 4 + padding, 0 + padding, adjw / 4 + padding, height - padding), fill = 0, width = 5)
    draw.line((adjw / 2 + padding, 0 + padding, adjw / 2 + padding, height - padding), fill = 0, width = 5)
    draw.line((0 + padding, adjh / 3 + padding, 0 + padding, adjh * (2/3) + padding), fill = 0, width = 5)
    draw.line((width - padding, adjh / 3 + padding, width - padding, adjh * (2/3) + padding), fill = 0, width = 5)
    draw.line((adjw / 4 + padding, 0 + padding, adjw / 2 + padding, 0 + padding), fill = 0, width = 5)
    draw.line((adjw / 4 + padding, height - padding, adjw / 2 + padding, height - padding), fill = 0, width = 5)
    draw.line((adjw * (3/4) + padding, adjh * (1/3) + padding, adjw * (3/4) + padding, adjh * (2/3) + padding), fill = 0, width = 5)

    #margin = distance that each tab needs to be from main block
    margin = 2
    triangle_base = 35
    #'black' = (0, 0, 0)

    #draw tabs on left face
    draw.rectangle((0, adjh * (1/3) + padding * 2, padding - margin, adjh * (2/3)), fill=c_left, outline = 'black')
    draw.rectangle((adjw * (1/8) - 10, adjh * (1/3) + padding - margin, adjw * (1/8) + padding * 2 + 10, adjh * (1/3)), fill = c_left, outline = 'black')
    draw.rectangle((adjw * (1/8) - 10, adjh * (2/3) + padding + margin, adjw * (1/8) + padding * 2 + 10, adjh * (2/3) + padding * 2), fill = c_left, outline = 'black')

    draw.polygon([(adjw * (1/8) - 10, adjh * (1/3) + padding - margin), (adjw * (1/8) - 10,  adjh * (1/3)), (adjw * (1/8) - triangle_base, adjh * (1/3))], fill = c_left, outline = 'black')
    draw.polygon([(adjw * (1/8) + padding * 2 + 10, adjh * (1/3) + padding - margin), (adjw * (1/8) + padding * 2 + 10,  adjh * (1/3)), adjw * (1/8) + padding * 2 + triangle_base, adjh * (1/3)], fill = c_left, outline = 'black')

    draw.polygon([(adjw * (1/8) - 10, adjh * (2/3) + padding + margin), (adjw * (1/8) - 10, adjh * (2/3) + padding * 2), (adjw * (1/8) - triangle_base, adjh * (2/3) + padding * 2)], fill = c_left, outline = 'black')
    draw.polygon([(adjw * (1/8) + padding * 2 + 10, adjh * (2/3) + padding + margin), (adjw * (1/8) + padding * 2 + 10, adjh * (2/3) + padding * 2), (adjw * (1/8) + padding * 2 + triangle_base, adjh * (2/3) + padding * 2)], fill = c_left, outline = 'black')

    draw.line((padding, adjh * (1/2) - 10, padding, adjh * (1/2) + padding * 2 + 10), fill = 'white', width = 3)
    for i in range (int(adjh * (1/2) - 10), int(adjh * (1/2) + padding * 2 + 10), 8):
        draw.line((padding, i, padding, i + 1), fill = 'black', width = 3)

    #draw tabs on back face
    draw.rectangle((adjw * (1/4) - margin, padding * 2, adjw * (1/4) + padding - margin, adjh * (1/3)), fill=c_back, outline = 'black')
    draw.rectangle((adjw * (1/2) + padding + margin, padding * 2, adjw * (1/2) + padding * 2 + margin, adjh * (1/3)), fill=c_back, outline = 'black')
    draw.rectangle((adjw * (1/4) + padding * 2, 0, adjw * (1/2), padding - margin), fill = c_back, outline = 'black')

    draw.line((adjw * (1/4) + padding, adjh * (1/6) - 10, adjw * (1/4) + padding, adjh * (1/6) + padding * 2 + 10), fill = 'white', width = 3)
    draw.line((adjw * (1/2) + padding, adjh * (1/6) - 10, adjw * (1/2) + padding, adjh * (1/6) + padding * 2 + 10), fill = 'white', width = 3)
    draw.line((adjw * (3/8) - 10, padding, adjw * (3/8) + padding * 2 + 10, padding), fill = "white", width = 3)

    for i in range (int(adjw * (3/8) - 10), int(adjw * (3/8) + padding * 2 + 10), 8):
        draw.line((i, padding, i + 1, padding), fill = 'black', width = 3)

    for i in range (int(adjh * (1/6) - 10), int(adjh * (1/6) + padding * 2 + 10), 8):
        draw.line((adjw * (1/4) + padding, i, adjw * (1/4) + padding, i + 1), fill = 'black', width = 3)
        draw.line((adjw * (1/2) + padding, i, adjw * (1/2) + padding, i + 1), fill = 'black', width = 3)

    #draw tobs on front face
    draw.rectangle((adjw * (1/4) - margin, adjh * (2/3) + padding * 2, adjw * (1/4) + padding - margin, adjh), fill=c_front, outline = 'black')
    draw.rectangle((adjw * (1/2) + padding + margin, adjh * (2/3) + padding * 2, adjw * (1/2) + padding * 2 + margin, adjh), fill=c_front, outline = 'black')
    draw.rectangle((adjw * (1/4) + padding * 2, height, adjw * (1/2), adjh + padding + margin), fill = c_front, outline = 'black')

    draw.line((adjw * (1/4) + padding, adjh * (5/6) - 10, adjw * (1/4) + padding, adjh * (5/6) + padding * 2 + 10), fill = 'white', width = 3)
    draw.line((adjw * (1/2) + padding, adjh * (5/6) - 10, adjw * (1/2) + padding, adjh * (5/6) + padding * 2 + 10), fill = 'white', width = 3)
    draw.line((adjw * (3/8) - 10, adjh + padding, adjw * (3/8) + padding * 2 + 10, adjh + padding), fill = "white", width = 3)

    for i in range (int(adjw * (3/8) - 10), int(adjw * (3/8) + padding * 2 + 10), 8):
        draw.line((i, adjh + padding, i + 1, adjh + padding), fill = 'black', width = 3)

    for i in range (int(adjh * (5/6) - 10), int(adjh * (5/6) + padding * 2 + 10), 8):
        draw.line((adjw * (1/4) + padding, i, adjw * (1/4) + padding, i + 1), fill = 'black', width = 3)
        draw.line((adjw * (1/2) + padding, i, adjw * (1/2) + padding, i + 1), fill = 'black', width = 3)



    #draw tabs on right face
    draw.rectangle((adjw * (5/8) - 10, adjh * (1/3) + padding - margin, adjw * (5/8) + padding * 2 + 10, adjh * (1/3)), fill = c_right, outline = 'black')
    draw.rectangle((adjw * (5/8) - 10, adjh * (2/3) + padding + margin, adjw * (5/8) + padding * 2 + 10, adjh * (2/3) + padding * 2), fill = c_right, outline = 'black')

    draw.polygon([(adjw * (5/8) - 10, adjh * (1/3) + padding - margin), (adjw * (5/8) - 10,  adjh * (1/3)), (adjw * (5/8) - triangle_base, adjh * (1/3))], fill = c_right, outline = 'black')
    draw.polygon([(adjw * (5/8) + padding * 2 + 10, adjh * (1/3) + padding - margin), (adjw * (5/8) + padding * 2 + 10,  adjh * (1/3)), adjw * (5/8) + padding * 2 + triangle_base, adjh * (1/3)], fill = c_right, outline = 'black')

    draw.polygon([(adjw * (5/8) - 10, adjh * (2/3) + padding + margin), (adjw * (5/8) - 10, adjh * (2/3) + padding * 2), (adjw * (5/8) - triangle_base, adjh * (2/3) + padding * 2)], fill = c_right, outline = 'black')
    draw.polygon([(adjw * (5/8) + padding * 2 + 10, adjh * (2/3) + padding + margin), (adjw * (5/8) + padding * 2 + 10, adjh * (2/3) + padding * 2), (adjw * (5/8) + padding * 2 + triangle_base, adjh * (2/3) + padding * 2)], fill = c_right, outline = 'black')

    #draw tabs on south pole
    draw.rectangle((adjw + padding + margin, adjh * (1/2) + padding * 2 + 10, adjw + padding * 2 - margin, adjh * (1/2) - 10), fill=c_left, outline = 'black')
    draw.rectangle((adjw * (7/8) - 10, adjh * (1/3) + padding - margin, adjw * (7/8) + padding * 2 + 10, adjh * (1/3)), fill = c_south, outline = 'black')
    draw.rectangle((adjw * (7/8) - 10, adjh * (2/3) + padding + margin, adjw * (7/8) + padding * 2 + 10, adjh * (2/3) + padding * 2), fill = c_south, outline = 'black')

    draw.polygon([(adjw * (7/8) - 10, adjh * (1/3) + padding - margin), (adjw * (7/8) - 10,  adjh * (1/3)), (adjw * (7/8) - triangle_base, adjh * (1/3))], fill = c_south, outline = 'black')
    draw.polygon([(adjw * (7/8) + padding * 2 + 10, adjh * (1/3) + padding - margin), (adjw * (7/8) + padding * 2 + 10,  adjh * (1/3)), adjw * (7/8) + padding * 2 + triangle_base, adjh * (1/3)], fill = c_south, outline = 'black')

    draw.polygon([(adjw * (7/8) - 10, adjh * (2/3) + padding + margin), (adjw * (7/8) - 10, adjh * (2/3) + padding * 2), (adjw * (7/8) - triangle_base, adjh * (2/3) + padding * 2)], fill = c_south, outline = 'black')
    draw.polygon([(adjw * (7/8) + padding * 2 + 10, adjh * (2/3) + padding + margin), (adjw * (7/8) + padding * 2 + 10, adjh * (2/3) + padding * 2), (adjw * (7/8) + padding * 2 + triangle_base, adjh * (2/3) + padding * 2)], fill = c_south, outline = 'black')

    draw.polygon([(adjw + padding + margin, adjh * (1/2) + padding * 2 + 10), (adjw + padding * 2 - margin, adjh * (1/2) + padding * 2 + triangle_base), (adjw + padding * 2 - margin, adjh * (1/2) + padding * 2 + 10)], fill = c_south, outline = 'black')
    draw.polygon([(adjw + padding + margin, adjh * (1/2) - 10), (adjw + padding * 2 - margin, adjh * (1/2) - triangle_base), (adjw + padding * 2 - margin, adjh * (1/2) - 10)], fill = c_south, outline = 'black')