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

```magick convert final_2023_place.png -dither FloydSteinberg -define dither:diffusion-amount=85% -remap eink___epaper_eink-4color.png -type truecolor BMP3:!!final_2023_place_encoded.bmp```

Execute the following script to convert the resulting BMP into the color sequence to be fed to Pico:

```python canvas_transformer.py input_bmp_file output_file height width```

### Server Side
TBD

### Client Side
TBD

## Demo
![demo](https://github.com/flodek/rpi-pico-rplace-e-paper-frame/blob/main/IMG_0126.jpeg?raw=true)

![demo](https://github.com/flodek/rpi-pico-rplace-e-paper-frame/blob/main/IMG_8252.png?raw=true)

![demo](https://github.com/flodek/rpi-pico-rplace-e-link-frame/blob/main/demo.gif?raw=true)
