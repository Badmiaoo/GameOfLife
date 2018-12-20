import numpy as np
import matplotlib.pyplot as plt


def saveAsImage(X, filename, dpi, gridColor):
  fig = plt.figure(figsize=(16, 9), dpi=dpi)

  # Light blue lines as cells boundaries
  plt.pcolormesh(np.flipud(X), cmap=plt.get_cmap('gray_r'), edgecolors=gridColor, linewidth=0.5)

  # Hide axis
  plt.axis('off')

  # Automatically adjust subplot on image
  fig.tight_layout()

  plt.savefig(filename, dpi=dpi)
