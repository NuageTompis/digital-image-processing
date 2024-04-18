## Summary

- [Task](/images/#task)
- [Examples of image processing](/images/#examples-of-image-processing)
  - [Projection](/images/#projection)
  - [Compression](/images/#compression)
    - [Lossy compressions](/images/#lossy-compressions)
    - [Lossless compressions](/images/#lossless-compressions)
  - [Image enhancement](/images/#image-enhancement)
  - [Feature extraction](/images/#feature-extraction)
  - [Photograph manipulation](/images/#photograph-manipulation)
    - [Background removal](/images/#background-removal)
- [Image processing techniques](/images/#image-processing-techniques)
  - [Process I am interested in](/images/#process-i-am-interested-in)

# Task

> Show some examples of image processing that you are interested in, use in your research, or are familiar with. Then research and report on what image processing techniques are used. If you have any digital image processing that you would like to learn, please describe it.

# Examples of image processing

Some examples of image processing include that I am interested in include: *projection*, to display representations of 3D objects according to various perspectives, *compression*, which aims at efficiently storing images in a computer, and more generally *image transformation*, which modifies the aspect of the image by applying a filter on each pixel, for instance.

## Projection

When 3-dimensional objects are rendered on a 2-dimensional surface, such as a sheet of paper or a screen, we generally use 2 graphical projection categories: *perspective projection* and *parallel projection*. *Perspective* projection represents an object on a plane as it is seen by the eye, whereas *parallel* projection, the lines of sight from the object to the plane are parallel to each other. In a *parallel* projection, lines that were parallel in the 3D object remain parallel on the plane.

The following pictures are taken from the game engine *Unity*. On the left is a perspective view of a scene, and on the right is a parallel projection of the same scene. 

| Perspective view                  | Parallel view               |
| --------------------------------- | --------------------------- |
| ![persp](/images/perspective.jpg) | ![ortho](/images/ortho.jpg) |

## Compression

### Lossy compressions

### Lossless compressions

## Image transformation

Some basic image manipulation tools are often directly integrated into rendering softwares such as *Android*'s *Gallery* or *Windows*' *Photos* app. Such manipulations include: reversing (vertical or horizontal), rotation, black and white filter, blur, etc.

| Initial Image               | Reversed image                      | Black & White image           | Blurred image                   |
| --------------------------- | ----------------------------------- | ----------------------------- | ------------------------------- |
| ![duck](/images//duck.webp) | ![duck](/images//duck-reversed.jpg) | ![duck](/images//duck-bw.jpg) | ![duck](/images//duck-blur.png) |

| Initial Image               | Edge detection                  |
| --------------------------- | ------------------------------- |
| ![duck](/images//duck.webp) | ![duck](/images//duck-lapl.png) |

| Initial image                | Image with background removed         |
| ---------------------------- | ------------------------------------- |
| ![bg](/images/surfboard.jpg) | ![no-bg](/images/surfboard-no-bg.png) |

# Image processing techniques

## Filters

A common technique is the use of *convolution kernels*. The idea is to apply a *mask*, or *kernel*, to each pixel by taking into account its direct neighbors.

For instance, such a kernel is called *Spatial Highpass* and can be represented like this:

$$\begin{bmatrix}
0 & -1 & 0 \\
-1 & 4 & -1 \\
0 & -1 & 0
\end{bmatrix}$$

Here each pixel is computed one by one, by multiplying its value by 4 and substracting the value of the 4 adjacent pixels. The resulting value is processed into the resulting image. This kernel is often used for edge detection.

Another common example are blur filters, such as the *Spatial Lowpass*, whose kernel is the following:

$$\frac{1}{9} * \begin{bmatrix}
1 & 1 & 1 \\
1 & 1 & 1 \\
1 & 1 & 1
\end{bmatrix}$$

The previous kernels are all $3*3$ matrices, however digital image processing isn't limited to $3*3$ matrices, for instance $5*5$ or $7*7$ matrices are also frequently used.

Other kinds of filters exist. For instance, to remove a background, we can ask the user the color that he wants to remove (on the example above it is `rgb(0, 197, 254)`), and then iterate through each pixel: if its value is close to this color then we set its transparancy to 1. This kind of filter doesn't take the neighbor pixels into account. The algorithms for *reversing* and *black & white* filters are similar in that sense.

## Processes I am interested in

### Image enhancement

### Feature extraction
