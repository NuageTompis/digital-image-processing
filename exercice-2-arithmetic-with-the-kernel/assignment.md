## Question 1

> Convolute the below kernel to the image you like.

Kernel :

$$K=\frac{1}{10} * \begin{bmatrix}
1 & 1 & 1 \\
1 & 2 & 1 \\
1 & 1 & 1
\end{bmatrix}$$    

| Original image                                                      | Convoluted image                                                                 |
| ------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| ![original](/exercice-2-arithmetic-with-the-kernel/images/duck.png) | ![convoluted](/exercice-2-arithmetic-with-the-kernel/images/duck-convoluted.png) |

## Question 2

> Convolute other kernels to the image you like.

Using different kernels on the same image as before, I obtain the following:

| Kernel                                                                                              | Resulting image                                                             |
| --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| $K=\begin{bmatrix}-1&-1&-1\cr-1&8&-1\cr-1&-1&-1\end{bmatrix}$                                       | ![ridge](/exercice-2-arithmetic-with-the-kernel/images/duck-ridge.png)      |
| $K=\begin{bmatrix}2&2&2&2&2\cr1&1&1&1&1\cr0&0&0&0&0\cr-1&-1&-1&-1&-1\cr-2&-2&-2&-2&-2\end{bmatrix}$ | ![filter2](/exercice-2-arithmetic-with-the-kernel/images/duck-filter-2.png) |
| $K=\begin{bmatrix}4&4&4&4&4\cr4&8&8&8&4\cr4&8&16&8&4\cr4&8&8&8&4\cr4&4&4&4&4\cr\end{bmatrix}$       | ![filter3](/exercice-2-arithmetic-with-the-kernel/images/duck-filter-3.png) |

## Question 3

> Create an image with a noise in the high spatial frequency and then reduce the noise from it to become a clearer image.

Here are the image I selected, then artificially blurred, then the result after applying a low-pass filter, using the kernel $K_A=\begin{bmatrix}1&1&1\cr1&1&1\cr1&1&1\end{bmatrix}$:

I didn't get satisfying results using Fiji so I tried implementing python scripts to have more control. I generated a noise to which I applied a high-pass filter using the kernel $K_B=\begin{bmatrix}-1&-1&-1\cr-1&9&-1\cr-1&-1&-1\end{bmatrix}$. I then combined the two images and applied a low-pass filter to reduce the noise using another convolution with the kernel $K_A$.

| Original noise                                                           | High-frequency noise                                                               | Image with high noise                                                             | Image with reduced noise                                                              |
| ------------------------------------------------------------------------ | ---------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| ![noise](/exercice-2-arithmetic-with-the-kernel/images/random-image.png) | ![high-noise](/exercice-2-arithmetic-with-the-kernel/images/random-image-high.png) | ![noised](/exercice-2-arithmetic-with-the-kernel/images/duck-with-high-noise.png) | ![reduced](/exercice-2-arithmetic-with-the-kernel/images/duck-with-reduced-noise.png) |