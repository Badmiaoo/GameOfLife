Forked from [scienceetonnante/GameOfLife](https://github.com/scienceetonnante/GameOfLife)
From  Youtube video https://www.youtube.com/watch?v=S-W0NX97DB0

# Game of Life

This game of life according to Conway has the following rules :
- A dead cell with exactly three living neighbors becomes alive.
- A live cell with two or three living neighbors stays alive; otherwise it dies.
But you can change the rules. :)

## Usage
```
Usage: GameOfLife.py [OPTIONS]

  Connexion parameters and output file

Options:
  --rle_path TEXT      Path of RLE file to read (ex.:
                       ../toto/tutu/rlefile.rle)  [required]
  --output_dir TEXT    Directory to save frames and movies (ex.: ../toto/tutu)
  --ffmpeg_path TEXT   Path of ffmpeg movie to save (ex.: ../toto/tutu)
  --frame INTEGER      Name of frame for the movie (ex.: 100)
  --map_x INTEGER      Size of game in axis X (ex.: 100)
  --map_y INTEGER      Size of game in axis Y (ex.: 100)
  --filename TEXT      Set name if you want different as rle filename (ex.
                       toto)
  --dpi_image INTEGER  Number of DPI (Dots per inch) for image. (ex. 600)
  --dpi_movie INTEGER  Number of DPI (Dots per inch) for movie. (ex. 600)
  --interval INTEGER   Delay between frames in milliseconds. (ex 30)
  --fps INTEGER        Framerate for movie. (ex. 24)
  --bitrate INTEGER    The bitrate for the saved movie file, which is one way
                       to control the output file size and quality. (ex. 5000)
  --hide_grid TEXT     Show the grid, True or False
  --help               Show this message and exit.
```

## Setup needed

python:3.6+
pip:8.1.1+
python3-tk:3.6+