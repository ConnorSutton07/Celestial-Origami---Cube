from PIL import Image, ImageDraw
# 2024-04-18 19:34 IJMC: Added sortxyxy() to ensure correct ordering
#                        for draw.rectangle.


def sortxyxy(fourlist):
    """Sort [x0,y0,x1,y1] to ensure that
        x0 < x1 and y0 < y1.
    """
    # 2024-04-18 19:29 IJMC: Created 
    x0,y0,x1,y1 = fourlist
    xvals = [x0,x1]
    yvals = [y0,y1]
    xvals.sort()
    yvals.sort()
    x0,x1 = xvals
    y0,y1 = yvals
    return([x0,y0,x1,y1])


def draw_tabs(img, padding, c_north, c_south, c_front, c_right, c_back, c_left):
    # 2024-04-18 19:35 IJMC: Added sortxyxy calls to ensure correct coordinate ordering.
    
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

    black = (0, 0, 0)

    #draw tabs on left face
    draw.rectangle((0, adjh * (1/3) + padding * 2, padding - margin, adjh * (2/3)), fill=c_left, outline = black)
    ###draw.rectangle((adjw * (1/8) - 10, adjh * (1/3) + padding - margin, adjw * (1/8) + padding * 2 + 10, adjh * (1/3)), fill = c_left, outline = black)
    xy = sortxyxy((adjw * (1/8) - 10, adjh * (1/3) + padding - margin, adjw * (1/8) + padding * 2 + 10, adjh * (1/3)))
    draw.rectangle(xy, fill=c_left, outline = black)

    draw.rectangle((adjw * (1/8) - 10, adjh * (2/3) + padding + margin, adjw * (1/8) + padding * 2 + 10, adjh * (2/3) + padding * 2), fill = c_left, outline = black)

    #draw tabs on back face
    draw.rectangle((adjw * (1/4) - margin, padding * 2, adjw * (1/4) + padding - margin, adjh * (1/3)), fill=c_back, outline = black)
    draw.rectangle((adjw * (1/2) + padding + margin, padding * 2, adjw * (1/2) + padding * 2 + margin, adjh * (1/3)), fill=c_back, outline = black)
    draw.rectangle((adjw * (1/4) + padding * 2, 0, adjw * (1/2), padding - margin), fill = c_back, outline = black)

    #draw tobs on front face
    draw.rectangle((adjw * (1/4) - margin, adjh * (2/3) + padding * 2, adjw * (1/4) + padding - margin, adjh), fill=c_front, outline = black)
    draw.rectangle((adjw * (1/2) + padding + margin, adjh * (2/3) + padding * 2, adjw * (1/2) + padding * 2 + margin, adjh), fill=c_front, outline = black)
    ###draw.rectangle((adjw * (1/4) + padding * 2, height, adjw * (1/2), adjh + padding + margin), fill = c_front, outline = black)
    xy = sortxyxy((adjw * (1/4) + padding * 2, height, adjw * (1/2), adjh + padding + margin))
    draw.rectangle(xy, fill=c_front, outline = black)

    #draw tabs on right face
    ###draw.rectangle(, fill = c_right, outline = black)
    xy = sortxyxy((adjw * (5/8) - 10, adjh * (1/3) + padding - margin, adjw * (5/8) + padding * 2 + 10, adjh * (1/3)))
    draw.rectangle(xy, fill=c_right, outline = black)

    draw.rectangle((adjw * (5/8) - 10, adjh * (2/3) + padding + margin, adjw * (5/8) + padding * 2 + 10, adjh * (2/3) + padding * 2), fill = c_right, outline = black)

    #draw tabs on south pole
    xy = sortxyxy((adjw + padding + margin, adjh * (1/2) + padding * 2 + 10, adjw + padding * 2 - margin, adjh * (1/2) - 10))
    draw.rectangle(xy, fill=c_left, outline = black)

    xy = sortxyxy((adjw * (7/8) - 10, adjh * (1/3) + padding - margin, adjw * (7/8) + padding * 2 + 10, adjh * (1/3)))
    draw.rectangle(xy, fill=c_south, outline = black)

    draw.rectangle((adjw * (7/8) - 10, adjh * (2/3) + padding + margin, adjw * (7/8) + padding * 2 + 10, adjh * (2/3) + padding * 2), fill = c_south, outline = black)


