from PIL import Image

# answer string: 
answer_string = "Hello, from the Least Significant Bit :)"
#print("length", len(answer_string))

answer_in_bits = ' '.join(format(ord(c), '08b') for c in answer_string)
#print(answer_in_bits)

im = Image.open("challenge_image.png")
#print(im.format, im.size, im.mode)

width = im.size[0]
height = im.size[1]
#print(f"total pixels = {width} * {height} = {width*height}")

binary_list = []

pixels = im.load()
for y in range(height):
    for x in range(width):
        
        channels = pixels[x, y][:3]

        binary_list.append(str(channels[0] & 1))
        binary_list.append(str(channels[1] & 1))
        binary_list.append(str(channels[2] & 1))
        #binary = binary + r_lsb + g_lsb + b_lsb

binary = "".join(binary_list)

split_binary = (binary[i:i+8] for i in range(0,len(binary), 8))
#print(split_binary)
#text = ''.join(chr(int(b, 2)) for b in split_binary)
text = ''
for c in split_binary:
    text += chr(int(c, 2))
    if len(text) > 2 and text[-2:] == (":)"):
        break
print(text)
