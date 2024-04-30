## Task

> Please extract the edges of your selected image using several methods and so evaluate the methods you used.

> For one of them, design an appropriate kernel and convolve it using FIJI. A kernel, a differential operation, can be used.

I first used the Laplacian operator technique with the approximation kernels shown in the course's PDF:


$$
K_1=\begin{bmatrix}-1&-1&-1\cr-1&8&-1\cr-1&-1&-1\end{bmatrix}, K_2=\begin{bmatrix}1&-2&1\cr-2&4&-2\cr1&-2&1\end{bmatrix}, K_3=\begin{bmatrix}0&-1&0\cr-1&4&-1\cr0&-1&0\end{bmatrix}
$$

Which generated the resulting images:

| Kernel   | Output                                                  |
| -------- | ------------------------------------------------------- |
| Original | ![original](/exercice-4-edge-detection/images/duck.png) |
| K1       | ![k1](/exercice-4-edge-detection/images/duck-k1.png)    |
| K2       | ![k2](/exercice-4-edge-detection/images/duck-k2.png)    |
| K3       | ![k3](/exercice-4-edge-detection/images/duck-k3.png)    |

Notes:

- The first kernel allows a very precise representation of the edges, we can even see here the light reflecting on the chest of the duck.
- The second kernel seems to capture most edges, yet it doesn't make the strong edges brighter than the weak ones.
- The last kernel seems to behave between the two previous ones.

I then used the Canny Edge detector with the tool available [here](https://imagej.net/ij/plugins/canny/index.html). This is the image that I obtained:

![canny](/exercice-4-edge-detection/images/duck-canny-default.png)

This filter shows impressive results, notably for details such as the drops of water that are right below the duck.