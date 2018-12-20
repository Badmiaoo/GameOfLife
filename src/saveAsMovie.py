import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


def saveAsMovie(history, filename, dpi, gridColor, interval, fps, bitrate):
  #Create the movie from a history of a game of life
  # Filename should be *.mp4

  # Create the plot and a subplot for his starting counter
  fig = plt.figure(figsize=(16,9), dpi=dpi)
  ax = fig.add_subplot(111)

  pc = ax.pcolormesh(np.flipud(history[0]), cmap=plt.get_cmap('gray_r'), edgecolors=gridColor, linewidths=0.5)
  counter = ax.text(0.01, 0.99, str(0), color='red', fontsize=30, verticalalignment='top', horizontalalignment='left', transform=ax.transAxes)

  # Hide axis
  plt.axis('off')

  # Automatically adjust subplot on image
  fig.tight_layout()

  # The function as it is called at the n-th iteration
  # It directly modifies the data within the image
  def update_img(n):
    X = np.flipud(history[n])
    # Revert and scale from 0-1 to 0-255
    new_color = plt.get_cmap('gray_r')(255*X.ravel())
    pc.update({'facecolors':new_color})
    counter.set_text(str(n))
    return True

  # Create the animation and save it
  ani = animation.FuncAnimation(fig, update_img, history.shape[0], interval=interval) # 30ms per frame
  writer = animation.FFMpegWriter(fps=fps, bitrate=bitrate)
  ani.save(filename, writer=writer, dpi=dpi)
