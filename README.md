# Raspberry Pi Pico r/Place e-paper frame
A digital frame powered by the Raspberry Pi Pico, displays a piece of [Reddit's r/place](https://www.reddit.com/r/place/) canvas at a random position.

![demo](https://github.com/flodek/rpi-pico-rplace-e-paper-frame/blob/main/IMG_8263.png?raw=true)

## Hardware
 - Raspberry Pi Pico W
 - Waveshare 3.7inch 480×280 E-Paper Display, 4 Grayscale

## How to Cook
### Canvas preparation
The canvas needs to be preprocessed before feeding it to Pico.
Ensure you have ImageMagick installed. Download the canvas from https://www.reddit.com/r/place/comments/15bjm5o/rplace_2023_data/ and execute the following command from the command line:

```cli
magick convert final_2023_place.png -dither FloydSteinberg -define dither:diffusion-amount=85% -remap eink___epaper_eink-4color.png -type truecolor BMP3:!!final_2023_place_encoded.bmp
```

Execute the following script to convert the resulting BMP into the color sequence to be fed to Pico:

```cli
python canvas_transformer.py input_bmp_file output_file height width
```

### Server Side
RP Pico doesn't have enough memory to store the entire canvas. This is why the solution is divided into two parts: the server and the client sides. The server part can be hosted on a Raspberry Pi Zero W using Flask framework:
```python
@app.route('/picture', methods=['GET'])
def picture():
    f = open('/home/pi/final_2023_place_color_sequence.txt', 'r')
    real_w = 6000 #image width
    x = request.args.get('x', default = 0, type = int)
    y = request.args.get('y', default = 0, type = int)
    w = request.args.get('w', default = 1, type = int)
    h = request.args.get('h', default = 1, type = int)
    page = request.args.get('page', default = 0, type = int)
    totl = request.args.get('totl', default = 1, type = int)
    res = ''

    f.read(x * real_w + y)
    for i in range (0, h):
        res += f.read(w)
        f.read(real_w - w)
    f.close()

    p_size = int(len(res) / totl)
    last_size = p_size + len(res) - p_size * totl

    if page >= totl - 1:
        return res[-last_size:]

    return res[page * p_size:page * p_size + p_size]
```
### Client Side
Amend ```main.py``` with your WiFi SSID and password, update the server-side URL, and save the file on the Pico.

## Demo
![demo](https://github.com/flodek/rpi-pico-rplace-e-paper-frame/blob/main/IMG_0126.jpeg?raw=true)

![demo](https://github.com/flodek/rpi-pico-rplace-e-paper-frame/blob/main/IMG_8252.png?raw=true)

![demo](https://github.com/flodek/rpi-pico-rplace-e-link-frame/blob/main/demo.gif?raw=true)
