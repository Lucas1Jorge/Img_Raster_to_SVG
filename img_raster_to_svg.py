# ** Raster to svg ****** 
# ** 将图片转换成svg格式 ** lucas1jorge


# Replace "raster.png" on line 15 with the name of your raster image

# Set the scale on line 25. Smaller scale means smaller radius of the vector spheres (replacing pixels), and thus leads to better definition:
# ↓ scale - definition ↑


from PIL import Image
import numpy as np

if __name__ == "__main__":
    image_name = "raster.png"       # Use the name of the image you want to vectorize
    img = Image.open(image_name)
    img.load()
    data = np.asarray(img)

    file_output = image_name[:-4] + ".svg"
    with open(file_output, "w") as file_svg:
        width = len(data[0])
        height = len(data)

        file_svg.write("<!DOCTYPE html>\n" \
                       + "<html>\n" \
                       + "<body>\n" \
                       + "\n" \
                       + "<svg width=\"" + str(width) + "\" height=\"" + str(height) + "\" xmlns=\"http://www.w3.org/2000/svg\">\n")

        scale = 1
        for i in range(0, len(data), scale):
            for j in range(0, len(data[0]), scale):
                r = (255 - data[i][j][0]) / 255.0
                circle = "\t<circle cx=\"" + str(j) \
                        + "\" cy=\"" + str(i) \
                        + "\" r=\"" + str(scale*r) \
                        + "\" />\n"

                file_svg.write(circle)

        file_svg.write("</svg>\n" \
                       + "\n" \
                       + "</body>\n" \
+ "</html>\n")
