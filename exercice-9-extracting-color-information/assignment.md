## Task

> We would like to extract and count the grain structure represented in red from the attached file of an image. How can we do this? It would be desirable to perform this process using FIJI, etc., but just describing the algorithm is also fine.

To achieve this, I first splitted the right, blue and green channels and only kept the red one as a 8-bit black and white image.

| Original                                                               | Red channel as black and white                                             |
| ---------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| ![ori](/exercice-9-extracting-color-information/images/hela-cells.png) | ![red](/exercice-9-extracting-color-information/images/hela-cells-red.png) |

Then I used a fixed global threshold algorithm to binarize the image by trying to keep only the grain structures. But I was not really satisfied with the results because some grains of the image are quite dark, and because of the dust-like shapes surrounding the grains, it was impossible to correctly segregate the grains only. So I also used a local threshold algorithm, I went for Phansalkar's algorithm.

This is what I obtained:

| Global threshold                                                                        | Local threshold                                                             |
| --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| ![global](/exercice-9-extracting-color-information/images/hela-cells-red-threshold.png) | ![local](/exercice-9-extracting-color-information/images/phansalkar-15.png) |

I couldn't find a way to use a *shrink* algorithm like the one shown in chapter 6 slide 13, so I used the hint that you provided and I obtained the following results:

| Global threshold                                                       | Local threshold                                                                  |
| ---------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| ![global](/exercice-9-extracting-color-information/images/summary.png) | ![local](/exercice-9-extracting-color-information/images/summary-phansalkar.png) |
| `158 grains`                                                           | `222 grains`                                                                     |