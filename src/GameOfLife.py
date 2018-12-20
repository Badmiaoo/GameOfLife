import os

import click

from reader import rleReader
from initGame import initGame
from core import core
from saveAsImage import saveAsImage
from saveAsMovie import saveAsMovie


@click.command(help='Connexion parameters and output file')
@click.option(
    '--rle_path',
    help='Path of RLE file to read (ex.: ../toto/tutu/rlefile.rle)',
    required=True
)
@click.option(
    '--output_dir',
    help='Directory to save frames and movies (ex.: ../toto/tutu)',
    default='../output'
)
@click.option(
    '--ffmpeg_path',
    help='Path of ffmpeg movie to save (ex.: ../toto/tutu)'
)
@click.option(
    '--frame',
    help='Name of frame for the movie (ex.: 100)',
    default=100
)
@click.option(
    '--map_x',
    help='Size of game in axis X (ex.: 100)',
    default=100
)
@click.option(
    '--map_y',
    help='Size of game in axis Y (ex.: 100)',
    default=100
)
@click.option(
    '--filename',
    help='Set name if you want different as rle filename (ex. toto)'
)
@click.option(
    '--dpi_image',
    help='Number of DPI (Dots per inch) for image. (ex. 600)',
    default=600
)
@click.option(
    '--dpi_movie',
    help='Number of DPI (Dots per inch) for movie. (ex. 600)',
    default=600
)
@click.option(
    '--interval',
    help='Delay between frames in milliseconds. (ex 30)',
    default=30
)
@click.option(
    '--fps',
    help='Framerate for movie. (ex. 24)',
    default=24
)
@click.option(
    '--bitrate',
    help='The bitrate for the saved movie file, which is one way to control the output file size and quality. (ex. 5000)',
    default=5000
)
@click.option(
    '--hide_grid',
    help='Show the grid, True or False',
    default=True
)
def GameOfLife(**kwargs):
  # Dict with all command line arguments
  d_args = {**kwargs}

  # Dict of setup from rle file
  rleSetup = rleReader(d_args.get('rle_path'))

  # Initialize game
  game = initGame(
    rleSetup.get('pattern'),
    rleSetup.get('#P', {'x': '0', 'y': '0'}),
    d_args.get('map_x'),
    d_args.get('map_y')
  )

  evolution = core(game, d_args.get('frame'), rleSetup.get('#r', {'s': '23', 'b': '3'}))

  if not os.path.exists(d_args.get('output_dir')):
    os.makedirs(d_args.get('output_dir'))

  # Get name of file
  filename = os.path.split(d_args.get('rle_path'))[-1]

  # Get name of file without extension .rle
  name = d_args.get('filename') if d_args.get('filename', False) else filename.split('.')[0]

  # Get if the grid will be hide
  isGrid = True if d_args.get('filename') == True else False
  gridColor = 'white' if isGrid else 'cadetblue'

  # need comment
  saveAsImage(evolution[0], os.path.join(d_args.get('output_dir'), name + '_init.png'), d_args.get('dpi_image'), gridColor)
  saveAsImage(evolution[-1], os.path.join(d_args.get('output_dir'), name + '_end.png'), d_args.get('dpi_image'), gridColor)
  saveAsMovie(evolution, os.path.join(d_args.get('output_dir'), name + '.mp4'), d_args.get('dpi_movie'), gridColor, d_args.get('interval'), d_args.get('fps'), d_args.get('bitrate'))


if __name__ == '__main__':
  GameOfLife()
